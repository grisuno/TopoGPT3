"""PPO for TopoGPT3.

Critic = frozen TopoGPT2 trunk + fresh Linear value head (quaternion trunk
untouched by value gradients except through shared trunk).
GAE + clipped actor + clipped value + k3 KL to ref.
"""
from __future__ import annotations

import argparse
import copy
import os
import sys

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch import optim
from torch.utils.data import DataLoader

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from topogpt3.model import BPETokenizer, TopoGPT2, TopoGPT2Config
from topogpt3.datasets_chat import RLAIFDatasetJSONL
from topogpt3.rewards import base_rewards, k3_kl
from topogpt3.rollout import create_rollout_engine
from topogpt3.trainer_utils_topo import Logger, is_main_process, setup_seed
from safetensors.torch import load_file


class TopoCritic(nn.Module):
    def __init__(self, trunk: TopoGPT2):
        super().__init__()
        self.trunk = trunk
        self.v_head = nn.Linear(trunk.config.D_MODEL, 1, bias=False)
        nn.init.normal_(self.v_head.weight, std=0.02)

    def forward(self, ids):
        # reuse trunk embeddings+layers without rebuilding: forward returns logits
        x = self.trunk.token_embed(ids)
        for layer in self.trunk.layers:
            x, _, _ = layer(x)
        x = self.trunk.final_norm(x)
        return self.v_head(x).squeeze(-1)  # [B,S]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default="data/rlaif.jsonl")
    ap.add_argument("--checkpoint", default="checkpoints_topogpt3/last")
    ap.add_argument("--out", default="out/topo_ppo.pt")
    ap.add_argument("--epochs", type=int, default=1)
    ap.add_argument("--batch-size", type=int, default=2)
    ap.add_argument("--lr", type=float, default=1e-6)
    ap.add_argument("--num-generations", type=int, default=4)
    ap.add_argument("--max-gen-len", type=int, default=256)
    ap.add_argument("--max-len", type=int, default=512)
    ap.add_argument("--gamma", type=float, default=1.0)
    ap.add_argument("--lam", type=float, default=0.95)
    ap.add_argument("--eps", type=float, default=0.2)
    ap.add_argument("--kl-coef", type=float, default=0.02)
    ap.add_argument("--vf-coef", type=float, default=0.5)
    ap.add_argument("--device", default="cuda" if torch.cuda.is_available() else "cpu")
    args = ap.parse_args()
    setup_seed(1337)
    device = args.device
    tok = BPETokenizer()
    cfg = TopoGPT2Config()
    actor = TopoGPT2(cfg)
    sf = os.path.join(args.checkpoint, "model.safetensors")
    if os.path.exists(sf):
        actor.load_state_dict(load_file(sf, device="cpu"), strict=False)
    actor = actor.to(device)
    ref = copy.deepcopy(actor).eval()
    for p in ref.parameters():
        p.requires_grad = False
    critic = TopoCritic(copy.deepcopy(actor)).to(device)

    opt_a = optim.AdamW(actor.parameters(), lr=args.lr)
    opt_c = optim.AdamW(critic.parameters(), lr=args.lr)
    ds = RLAIFDatasetJSONL(args.data, tok, max_length=args.max_len)
    loader = DataLoader(ds, batch_size=args.batch_size, shuffle=True,
                        collate_fn=lambda b: [x["prompt"] for x in b])
    engine = create_rollout_engine(actor, tok, device=device,
                                   decode=lambda ids: tok.decode(ids))
    step = 0
    for ep in range(args.epochs):
        for prompts in loader:
            step += 1
            ids = [tok.encode(p)[-args.max_len:] for p in prompts]
            L = max(len(x) for x in ids)
            prompt_ids = torch.tensor([([0] * (L - len(x))) + x for x in ids])
            rr = engine.rollout(prompt_ids, num_generations=args.num_generations,
                                max_new_tokens=args.max_gen_len, temperature=0.8)
            out_ids = rr.output_ids.to(device)
            rewards = base_rewards(prompts, rr.completions, device=device)
            R = rr.completion_ids.size(1)
            plen = rr.prompt_lens[0].item()
            comp_ids = rr.completion_ids.to(device)
            mask = rr.completion_mask.float().to(device)
            with torch.no_grad():
                rl, _, _ = ref(out_ids)
                rlp = F.log_softmax(rl[:, :-1, :], dim=-1)
                idx = torch.arange(plen - 1, plen - 1 + R, device=device)
                ref_lp = torch.gather(rlp[:, idx, :], 2,
                                      comp_ids.unsqueeze(-1)).squeeze(-1)
                old_lp = rr.per_token_logps.to(device)
            # reward broadcast (gamma=1); normalized advantages
            adv_g = rewards.view(-1, 1).expand(-1, R)
            adv = (adv_g - adv_g.mean()) / (adv_g.std() + 1e-4)
            # actor + critic forwards WITH grad (disjoint param sets)
            logits, _, _ = actor(out_ids)
            values = critic(out_ids)  # [N, P+R]
            lp = F.log_softmax(logits[:, :-1, :], dim=-1)
            new_lp = torch.gather(lp[:, idx, :], 2,
                                  comp_ids.unsqueeze(-1)).squeeze(-1)
            ratio = torch.exp(new_lp - old_lp)
            a_loss = -torch.min(adv * ratio,
                                adv * torch.clamp(ratio, 1 - args.eps, 1 + args.eps))
            kl = k3_kl(ref_lp, new_lp)
            actor_loss = ((a_loss + args.kl_coef * kl) * mask).mean()
            v_pred = values[:, plen - 1:plen - 1 + R]
            v_target = adv_g.detach()
            v_loss = 0.5 * (((v_pred - v_target) ** 2) * mask).mean()
            loss = actor_loss + args.vf_coef * v_loss
            opt_a.zero_grad()
            opt_c.zero_grad()
            loss.backward()
            torch.nn.utils.clip_grad_norm_(actor.parameters(), 1.0)
            torch.nn.utils.clip_grad_norm_(critic.parameters(), 1.0)
            opt_a.step()
            opt_c.step()
            if step % 5 == 0:
                Logger(f"ep{ep} step{step} actor={actor_loss.item():.4f} "
                       f"value={v_loss.item():.4f}")
    if is_main_process():
        os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)
        torch.save({k: v.half().cpu() for k, v in actor.state_dict().items()}, args.out)
        Logger(f"saved PPO actor -> {args.out}")


if __name__ == "__main__":
    main()
