"""Reward + advantage + loss helpers for TopoGPT3 group-RL.

Adds an *optional* spectral-coherence bonus unique to TopoGPT3 identity:
rewards answers whose generation kept Fisher gap healthy / drift bounded
(when diagnostics are supplied). Defaults to 0 so the base reward
is reproduced exactly when no geometry stats are passed.
"""
from __future__ import annotations

import re
from typing import Optional

import torch
import torch.nn.functional as F


def rep_penalty(text: str, n: int = 3, cap: float = 0.5) -> float:
    toks = re.findall(r"\w+|[^\w\s]", text.lower())
    grams = [tuple(toks[i:i + n]) for i in range(len(toks) - n + 1)]
    if not grams:
        return 0.0
    return min(cap, (len(grams) - len(set(grams))) * cap * 2 / len(grams))


def base_rewards(prompts, completions, reward_fn=None, device="cpu"):
    """Group-RL reward skeleton: length + thinking + RM - repetition."""
    R = torch.zeros(len(completions), device=device)
    scores = []
    ng = max(1, len(completions) // max(1, len(prompts)))
    for i in range(len(prompts)):
        for j in range(ng):
            idx = i * ng + j
            if idx >= len(completions):
                break
            resp = completions[idx] or ""
            R[idx] += 0.5 if 20 <= len(resp.strip()) <= 800 else -0.5
            if "</think>" in resp:
                think, ans = resp.split("</think>", 1)
                R[idx] += 1.0 if 20 <= len(think.strip()) <= 300 else -0.5
                R[idx] += 0.25 if resp.count("</think>") == 1 else -0.25
                R[idx] -= rep_penalty(ans)
            else:
                R[idx] -= rep_penalty(resp)
            if reward_fn is not None:
                try:
                    messages = [{"role": "user", "content": prompts[i]}]
                    scores.append(float(reward_fn(messages, resp)))
                except Exception:
                    scores.append(0.0)
    if reward_fn is not None and scores:
        R = R + torch.tensor(scores, device=device)
    return R.clamp(-3.0, 3.0) if reward_fn is not None else R


def spectral_bonus(fisher_gap: Optional[float] = None,
                   drift: Optional[float] = None,
                   w_fisher: float = 0.05, w_drift: float = 0.05) -> float:
    """Small bonus preserving topological identity (0 when stats absent)."""
    b = 0.0
    if fisher_gap is not None:
        b += w_fisher * max(0.0, min(1.0, fisher_gap * 100.0))
    if drift is not None:
        b += w_drift * max(0.0, 1.0 - min(1.0, abs(drift)))
    return b


def grpo_advantages(rewards: torch.Tensor, num_generations: int):
    g = rewards.view(-1, num_generations)
    mean = g.mean(dim=1).repeat_interleave(num_generations)
    std = g.std(dim=1, unbiased=False).repeat_interleave(num_generations)
    return (rewards - mean) / (std + 1e-4)


def k3_kl(ref_logp: torch.Tensor, new_logp: torch.Tensor):
    d = ref_logp - new_logp
    return torch.exp(d) - d - 1


def grpo_loss(new_logp, old_logp, ref_logp, adv, mask, beta=0.1,
              eps=0.2, loss_type="cispo", eps_high=5.0):
    kl = k3_kl(ref_logp, new_logp)
    ratio = torch.exp(new_logp - old_logp)
    if loss_type == "cispo":
        clamped = torch.clamp(ratio, max=eps_high).detach()
        per_tok = -(clamped * adv.unsqueeze(1) * new_logp - beta * kl)
    else:
        clipped = torch.clamp(ratio, 1 - eps, 1 + eps)
        per_tok = -(torch.min(ratio * adv.unsqueeze(1),
                              clipped * adv.unsqueeze(1)) - beta * kl)
    denom = mask.sum(dim=1).clamp(min=1)
    return ((per_tok * mask).sum(dim=1) / denom).mean()


def logits_to_log_probs(logits: torch.Tensor, labels: torch.Tensor):
    return torch.gather(F.log_softmax(logits, dim=-1), 2,
                        labels.unsqueeze(2)).squeeze(-1)


def dpo_loss_fn(ref_lp, pol_lp, mask, beta=0.15):
    ref_s = (ref_lp * mask).sum(1)
    pol_s = (pol_lp * mask).sum(1)
    b = ref_s.shape[0] // 2
    pi = pol_s[:b] - pol_s[b:]
    rf = ref_s[:b] - ref_s[b:]
    return (-F.logsigmoid(beta * (pi - rf))).mean()


def distillation_loss(student_logits, teacher_logits, mask, labels=None,
                      alpha: float = 0.5, temp: float = 1.5):
    """White-box distill: CE + T^2*KL on masked response tokens."""
    t_vocab = teacher_logits.size(-1)
    s = student_logits[..., :t_vocab]
    ce = F.cross_entropy(s.reshape(-1, t_vocab),
                         labels.reshape(-1) if labels is not None else
                         teacher_logits.argmax(-1).reshape(-1),
                         ignore_index=-100)
    tp = F.softmax(teacher_logits / temp, dim=-1).detach()
    sl = F.log_softmax(s / temp, dim=-1)
    kl = (F.kl_div(sl.reshape(-1, t_vocab), tp.reshape(-1, t_vocab),
                   reduction="none").sum(-1).view_as(mask) * mask).sum() \
        / mask.sum().clamp(min=1)
    return alpha * ce + (1 - alpha) * (temp ** 2) * kl
