"""GRPO / CISPO for TopoGPT3.

Group-relative advantages, k3 KL to frozen ref, no Critic needed —
ideal for complex/quaternion weights that are hard to stabilize with a
value head. Spectral bonus is opt-in (default 0 = base behavior).
"""
from __future__ import annotations

import argparse
import copy
import os
import sys

import torch
import torch.nn.functional as F
from torch import optim
from torch.optim.lr_scheduler import CosineAnnealingLR
from torch.utils.data import DataLoader

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from topogpt3.model import BPETokenizer, TopoGPT2, TopoGPT2Config
from topogpt3.datasets_chat import RLAIFDatasetJSONL
from topogpt3.rewards import base_rewards, grpo_advantages, grpo_loss
from topogpt3.rollout import create_rollout_engine
from topogpt3.trainer_utils_topo import Logger, is_main_process, setup_seed
from safetensors.torch import load_file


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default="data/rlaif.jsonl")
    ap.add_argument("--checkpoint", default="checkpoints_topogpt3/last")
    ap.add_argument("--out", default="out/topo_grpo.pt")
    ap.add_argument("--epochs", type=int, default=1)
    ap.add_argument("--batch-size", type=int, default=2)
    ap.add_argument("--lr", type=float, default=3e-7)
    ap.add_argument("--num-generations", type=int, default=4)
    ap.add_argument("--max-gen-len", type=int, default=256)
    ap.add_argument("--max-len", type=int, default=512)
    ap.add_argument("--beta", type=float, default=0.1)
    ap.add_argument("--loss-type", default="cispo", choices=["grpo", "cispo"])
    ap.add_argument("--epsilon", type=float, default=0.2)
    ap.add_argument("--epsilon-high", type=float, default=5.0)
    ap.add_argument("--device", default="cuda" if torch.cuda.is_available() else "cpu")
    args = ap.parse_args()
    setup_seed(1337)
    device = args.device
    tok = BPETokenizer()

    cfg = TopoGPT2Config()
    model = TopoGPT2(cfg)
    sf = os.path.join(args.checkpoint, "model.safetensors")
    if os.path.exists(sf):
        model.load_state_dict(load_file(sf, device="cpu"), strict=False)
    model = model.to(device)
    ref = copy.deepcopy(model).eval()
    for p in ref.parameters():
        p.requires_grad = False

    opt = optim.AdamW(model.parameters(), lr=args.lr)
    ds = RLAIFDatasetJSONL(args.data, tok, max_length=args.max_len)
    loader = DataLoader(ds, batch_size=args.batch_size, shuffle=True,
                        collate_fn=lambda b: [x["prompt"] for x in b])
    sched = CosineAnnealingLR(opt, T_max=max(1, args.epochs * max(1, len(loader))))
    engine = create_rollout_engine(model, tok, device=device,
                                   decode=lambda ids: tok.decode(ids))
    step = 0
    model.train()
    for ep in range(args.epochs):
        for prompts in loader:
            step += 1
            # tokenize prompts (left-truncate to max len)
            ids = [tok.encode(p)[-args.max_len:] for p in prompts]
            L = max(len(x) for x in ids)
            prompt_ids = torch.tensor([([0] * (L - len(x))) + x for x in ids],
                                      dtype=torch.long)
            rr = engine.rollout(prompt_ids, num_generations=args.num_generations,
                                max_new_tokens=args.max_gen_len, temperature=0.8)
            rewards = base_rewards(prompts, rr.completions, device=device)
            adv = grpo_advantages(rewards, args.num_generations)
            # per-token logps over completion span
            with torch.no_grad():
                ref_logits, _, _ = ref(rr.output_ids.to(device))
            logits, aux, _ = model(rr.output_ids.to(device))
            R = rr.completion_ids.size(1)
            plen = rr.prompt_lens[0].item()
            # gather completion logps: positions plen-1 .. plen+R-2 in shifted space
            def _gather(lg, _plen=plen, _R=R, _comp=rr.completion_ids.to(device)):
                lp = F.log_softmax(lg[:, :-1, :], dim=-1)
                idx = torch.arange(_plen - 1, _plen - 1 + _R, device=lg.device)
                return torch.gather(lp[:, idx, :], 2,
                                    _comp.unsqueeze(-1)).squeeze(-1)
            new_lp = _gather(logits)
            ref_lp = _gather(ref_logits)
            old_lp = rr.per_token_logps.to(device)
            mask = rr.completion_mask.float().to(device)
            loss = grpo_loss(new_lp, old_lp, ref_lp, adv.to(device), mask,
                             beta=args.beta, eps=args.epsilon,
                             loss_type=args.loss_type, eps_high=args.epsilon_high)
            loss = loss + 0.01 * aux
            opt.zero_grad()
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            opt.step()
            sched.step()
            if step % 5 == 0:
                Logger(f"ep{ep} step{step} reward={rewards.mean().item():.3f} "
                       f"loss={loss.item():.4f}")
            if step % 20 == 0:
                engine.update_policy(model)
    if is_main_process():
        os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)
        torch.save({k: v.half().cpu() for k, v in model.state_dict().items()}, args.out)
        Logger(f"saved GRPO -> {args.out}")


if __name__ == "__main__":
    main()
