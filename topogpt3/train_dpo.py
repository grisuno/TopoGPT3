"""DPO for TopoGPT3. Policy + frozen ref share
TopoGPT2 quaternion/spectral weights; only preference direction is learned."""
from __future__ import annotations

import argparse
import copy
import os
import sys

import torch
from torch import optim
from torch.utils.data import DataLoader
from safetensors.torch import load_file

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from topogpt3.model import BPETokenizer, TopoGPT2, TopoGPT2Config
from topogpt3.datasets_chat import DPODatasetJSONL
from topogpt3.rewards import dpo_loss_fn, logits_to_log_probs
from topogpt3.trainer_utils_topo import (Logger, get_lr, init_distributed_mode,
                                         is_main_process, setup_seed,
                                         topo_checkpoint)


def load_model(checkpoint, device):
    cfg = TopoGPT2Config()
    m = TopoGPT2(cfg)
    sf = os.path.join(checkpoint, "model.safetensors")
    if os.path.exists(sf):
        m.load_state_dict(load_file(sf, device="cpu"), strict=False)
    return m.to(device)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default="data/dpo.jsonl")
    ap.add_argument("--checkpoint", default="checkpoints_topogpt3/last")
    ap.add_argument("--out", default="out/topo_dpo.pt")
    ap.add_argument("--epochs", type=int, default=1)
    ap.add_argument("--batch-size", type=int, default=2)
    ap.add_argument("--lr", type=float, default=4e-8)
    ap.add_argument("--beta", type=float, default=0.15)
    ap.add_argument("--max-len", type=int, default=512)
    ap.add_argument("--device", default="cuda" if torch.cuda.is_available() else "cpu")
    args = ap.parse_args()
    setup_seed(1337)
    init_distributed_mode()
    device = args.device
    tok = BPETokenizer()

    model = load_model(args.checkpoint, device)
    ref = copy.deepcopy(model).eval()
    for p in ref.parameters():
        p.requires_grad = False
    opt = optim.AdamW(model.parameters(), lr=args.lr)
    loader = DataLoader(DPODatasetJSONL(args.data, tok, args.max_len),
                        batch_size=args.batch_size, shuffle=True)
    total = args.epochs * max(1, len(loader))
    step = 0
    model.train()
    for ep in range(args.epochs):
        for b in loader:
            step += 1
            xc, yc, mc = b["x_chosen"].to(device), b["y_chosen"].to(device), b["mask_chosen"].to(device)
            xr, yr, mr = b["x_rejected"].to(device), b["y_rejected"].to(device), b["mask_rejected"].to(device)
            x = torch.cat([xc, xr], 0)
            y = torch.cat([yc, yr], 0)
            mask = torch.cat([mc, mr], 0)
            lr = get_lr(step, total, args.lr)
            for pg in opt.param_groups:
                pg["lr"] = lr
            with torch.no_grad():
                ref_logits, _, _ = ref(x)
            logits, aux, _ = model(x)
            # shift for next-token prediction
            ref_lp = logits_to_log_probs(ref_logits[:, :-1], y[:, 1:])
            pol_lp = logits_to_log_probs(logits[:, :-1], y[:, 1:])
            m = mask[:, 1:]
            loss = dpo_loss_fn(ref_lp, pol_lp, m, beta=args.beta) + 0.01 * aux
            opt.zero_grad()
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            opt.step()
            if step % 10 == 0:
                Logger(f"ep{ep} step{step}/{total} dpo_loss={loss.item():.4f}")
    if is_main_process():
        topo_checkpoint(os.path.dirname(args.out) or ".", os.path.splitext(os.path.basename(args.out))[0],
                        model=model, optimizer=opt, epoch=args.epochs, step=step)
        Logger(f"saved DPO -> {args.out}")


if __name__ == "__main__":
    main()
