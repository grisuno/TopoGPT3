"""White-box distillation for TopoGPT3.

Teacher: any HF causal LM (e.g. Qwen/StarCoder) or a larger TopoGPT2.
Student: TopoGPT2 quaternion/spectral — learns to mimic teacher geometry
in logit space while keeping its own spectral diagnostics intact.
"""
from __future__ import annotations

import argparse
import os
import sys

import torch
from torch import optim
from torch.utils.data import DataLoader

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from topogpt3.model import BPETokenizer, TopoGPT2, TopoGPT2Config
from topogpt3.rewards import distillation_loss
from topogpt3.trainer_utils_topo import Logger, get_lr, is_main_process, setup_seed
from safetensors.torch import load_file


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default="data/sft_toolcall.jsonl")
    ap.add_argument("--checkpoint", default="checkpoints_topogpt3/last")
    ap.add_argument("--teacher", default="", help="HF model id or TopoGPT2 ckpt dir")
    ap.add_argument("--out", default="out/topo_distill.pt")
    ap.add_argument("--epochs", type=int, default=1)
    ap.add_argument("--batch-size", type=int, default=2)
    ap.add_argument("--lr", type=float, default=1e-4)
    ap.add_argument("--alpha", type=float, default=0.5)
    ap.add_argument("--temp", type=float, default=1.5)
    ap.add_argument("--max-len", type=int, default=512)
    ap.add_argument("--device", default="cuda" if torch.cuda.is_available() else "cpu")
    args = ap.parse_args()
    setup_seed(1337)
    device = args.device
    tok = BPETokenizer()

    cfg = TopoGPT2Config()
    student = TopoGPT2(cfg).to(device)
    sf = os.path.join(args.checkpoint, "model.safetensors")
    if os.path.exists(sf):
        student.load_state_dict(load_file(sf, device="cpu"), strict=False)

    teacher = None
    use_hf = bool(args.teacher)
    if args.teacher:
        try:
            from transformers import AutoModelForCausalLM
        except ImportError:
            raise SystemExit(
                "train-distill --teacher needs 'transformers' (your env lacks it).\n"
                "  pip install transformers   # or run without --teacher for self-distill")
        try:
            teacher = AutoModelForCausalLM.from_pretrained(
                args.teacher, trust_remote_code=True,
                torch_dtype=torch.float16 if "cuda" in device else torch.float32)
            teacher = teacher.to(device).eval()
            Logger(f"teacher HF: {args.teacher}")
        except Exception as e:
            raise SystemExit(f"HF teacher load failed: {e}")
    else:
        import copy as _c
        teacher = _c.deepcopy(student).eval()
    for p in teacher.parameters():
        p.requires_grad = False

    from topogpt3.datasets_chat import SFTDatasetJSONL
    loader = DataLoader(SFTDatasetJSONL(args.data, tok, args.max_len),
                        batch_size=args.batch_size, shuffle=True)
    opt = optim.AdamW(student.parameters(), lr=args.lr)
    total = args.epochs * max(1, len(loader))
    step = 0
    student.train()
    for ep in range(args.epochs):
        for x, y in loader:
            step += 1
            x, y = x.to(device), y.to(device)
            s_logits, aux, _ = student(x)
            with torch.no_grad():
                if use_hf and teacher is not None:
                    # HF ids live in another vocab; map by truncation to overlap
                    t_out = teacher(input_ids=x % teacher.config.vocab_size)
                    t_logits = t_out.logits[..., :s_logits.size(-1)]
                else:
                    t_logits, _, _ = teacher(x)
            mask = (y != -100).float()
            loss = distillation_loss(s_logits[:, :-1], t_logits[:, :-1].detach(),
                                     mask[:, 1:], labels=y[:, 1:],
                                     alpha=args.alpha, temp=args.temp)
            loss = loss + cfg.AE_RECON_WEIGHT * 0.0 + 0.0 * aux
            lr = get_lr(step, total, args.lr)
            for pg in opt.param_groups:
                pg["lr"] = lr
            opt.zero_grad()
            loss.backward()
            torch.nn.utils.clip_grad_norm_(student.parameters(), 1.0)
            opt.step()
            if step % 20 == 0:
                Logger(f"ep{ep} step{step}/{total} distill_loss={loss.item():.4f}")
    if is_main_process():
        os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)
        torch.save({k: v.half().cpu() for k, v in student.state_dict().items()}, args.out)
        Logger(f"saved distilled student -> {args.out}")


if __name__ == "__main__":
    main()
