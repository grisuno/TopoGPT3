"""SFT with native LoRA for TopoGPT3.

Freezes quaternion/spectral base, trains only LoRA deltas. DDP + AMP ready.
"""
from __future__ import annotations

import argparse
import os
import sys

import torch
from torch import optim
from torch.nn.parallel import DistributedDataParallel
from torch.utils.data import DataLoader
from safetensors.torch import load_file

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from topogpt3.model import BPETokenizer, TopoGPT2, TopoGPT2Config
from topogpt3.datasets_chat import SFTDatasetJSONL
from topogpt3.lora import apply_lora, freeze_non_lora, lora_parameters, save_lora
from topogpt3.trainer_utils_topo import (Logger, get_lr, init_distributed_mode,
                                         is_main_process, setup_seed)


def load_base(checkpoint: str, device: str):
    cfg = TopoGPT2Config()
    model = TopoGPT2(cfg)
    sf = os.path.join(checkpoint, "model.safetensors")
    if os.path.exists(sf):
        sd = load_file(sf, device="cpu")
        model.load_state_dict(sd, strict=False)
        Logger(f"loaded base {sf}")
    return model.to(device), cfg


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default="data/sft_toolcall.jsonl")
    ap.add_argument("--checkpoint", default="checkpoints_topogpt3/last")
    ap.add_argument("--out", default="out/topo_lora.pt")
    ap.add_argument("--rank", type=int, default=16)
    ap.add_argument("--epochs", type=int, default=1)
    ap.add_argument("--batch-size", type=int, default=4)
    ap.add_argument("--lr", type=float, default=1e-4)
    ap.add_argument("--max-len", type=int, default=512)
    ap.add_argument("--include-mlp", action="store_true")
    ap.add_argument("--device", default="cuda" if torch.cuda.is_available() else "cpu")
    ap.add_argument("--seed", type=int, default=1337)
    args = ap.parse_args()

    setup_seed(args.seed)
    local_rank = init_distributed_mode()
    device = f"cuda:{local_rank}" if torch.cuda.is_available() and os.environ.get("RANK") else args.device

    tok = BPETokenizer()
    model, _ = load_base(args.checkpoint, device)
    patched = apply_lora(model, rank=args.rank, include_mlp=args.include_mlp)
    freeze_non_lora(model)
    Logger(f"LoRA patched {len(patched)} linears (quaternion-safe): {patched[:5]}")
    if os.environ.get("RANK"):
        model = DistributedDataParallel(model, device_ids=[local_rank])

    ds = SFTDatasetJSONL(args.data, tok, max_length=args.max_len)
    loader = DataLoader(ds, batch_size=args.batch_size, shuffle=True)
    opt = optim.AdamW(list(lora_parameters(model)), lr=args.lr)
    scaler = torch.cuda.amp.GradScaler(enabled=(device.startswith("cuda")))
    total = args.epochs * max(1, len(loader))
    step = 0
    model.train()
    for ep in range(args.epochs):
        for x, y in loader:
            step += 1
            x, y = x.to(device), y.to(device)
            lr = get_lr(step, total, args.lr)
            for pg in opt.param_groups:
                pg["lr"] = lr
            with torch.autocast(device_type="cuda" if "cuda" in device else "cpu",
                                enabled=device.startswith("cuda")):
                out = model.module if isinstance(model, DistributedDataParallel) else model
                logits, aux, _ = out(x)
                loss = torch.nn.functional.cross_entropy(
                    logits[:, :-1].reshape(-1, logits.size(-1)),
                    x[:, 1:].reshape(-1), ignore_index=-100) if (y == -100).all() else \
                    torch.nn.functional.cross_entropy(
                    logits.reshape(-1, logits.size(-1)), y.reshape(-1), ignore_index=-100)
                loss = loss + 0.0 * aux  # aux kept for logging, LoRA doesn't route MoE
            scaler.scale(loss).backward()
            scaler.unscale_(opt)
            torch.nn.utils.clip_grad_norm_(list(lora_parameters(model)), 1.0)
            scaler.step(opt)
            scaler.update()
            opt.zero_grad()
            if step % 20 == 0:
                Logger(f"ep{ep} step{step}/{total} loss={loss.item():.4f} lr={lr:.2e}")
    if is_main_process():
        os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)
        raw = model.module if isinstance(model, DistributedDataParallel) else model
        save_lora(raw, args.out)
        Logger(f"saved LoRA -> {args.out}")


if __name__ == "__main__":
    main()
