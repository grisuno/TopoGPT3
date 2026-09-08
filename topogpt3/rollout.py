"""Rollout engine for TopoGPT3 RL self-sampling.

Works with TopoGPT2.generate(token_ids [B,S]) instead of HF generate.
No architecture change: sampling reuses the model's own generate/HRM path.
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List

import torch
import torch.nn.functional as F
from torch.nn.parallel import DistributedDataParallel


@dataclass
class RolloutResult:
    output_ids: torch.Tensor
    completion_ids: torch.Tensor
    per_token_logps: torch.Tensor
    completions: List[str]
    prompt_lens: torch.Tensor
    completion_mask: torch.Tensor


def compute_per_token_logps(model, input_ids: torch.Tensor, n_keep: int) -> torch.Tensor:
    if n_keep <= 0:
        return input_ids.new_empty((input_ids.size(0), 0), dtype=torch.float32)
    unwrapped = model.module if isinstance(model, DistributedDataParallel) else model
    with torch.no_grad():
        out = unwrapped(input_ids)
        logits = out[0] if isinstance(out, tuple) else out.logits
        lp = F.log_softmax(logits[:, -n_keep - 1:-1, :], dim=-1)
        ids = input_ids[:, -n_keep:].unsqueeze(-1)
        return torch.gather(lp, 2, ids).squeeze(-1)


class RolloutEngine(ABC):
    @abstractmethod
    def rollout(self, prompt_ids, num_generations=4, max_new_tokens=256,
                temperature=0.8, tokenizer=None) -> RolloutResult:
        ...

    @abstractmethod
    def update_policy(self, model) -> None:
        ...


class TorchRolloutEngine(RolloutEngine):
    def __init__(self, policy_model, tokenizer, device="cpu", decode=None):
        self.policy_model = policy_model
        self.tokenizer = tokenizer
        self.device = device
        self.decode = decode or (lambda ids: tokenizer.decode(ids))

    def rollout(self, prompt_ids, num_generations=4, max_new_tokens=256,
                temperature=0.8, tokenizer=None) -> RolloutResult:
        tok = tokenizer or self.tokenizer
        model = self.policy_model.module if isinstance(
            self.policy_model, DistributedDataParallel) else self.policy_model
        prompt_ids = prompt_ids.to(self.device)
        rep = prompt_ids.repeat_interleave(num_generations, dim=0)
        with torch.no_grad():
            out = model.generate(rep, max_new_tokens=max_new_tokens,
                                 temperature=temperature)
        plen = prompt_ids.size(1)
        comp = out[:, plen:]
        old_lp = compute_per_token_logps(self.policy_model, out, comp.size(1))
        texts = [self.decode(c.tolist()) for c in comp]
        return RolloutResult(
            output_ids=out, completion_ids=comp, per_token_logps=old_lp,
            completions=texts,
            prompt_lens=torch.full((out.size(0),), plen, dtype=torch.long,
                                   device=out.device),
            completion_mask=torch.ones(out.size(0), comp.size(1),
                                       dtype=torch.long, device=out.device))

    def update_policy(self, model) -> None:
        self.policy_model = model


def create_rollout_engine(policy_model, tokenizer, device="cpu", **kw):
    return TorchRolloutEngine(policy_model, tokenizer, device=device, **kw)
