"""YaRN RoPE extrapolation for TopoGPT3.

Preserves the quaternionic/spectral identity: only rescales the rotary
frequencies (NTK-by-parts ramp), never touches Quaternion/Torus/MoE layers.

Reference: NTK-by-parts frequency ramp with
  factor=16, orig_max=2048, beta_fast=32, beta_slow=1.
"""
from __future__ import annotations

import math
from dataclasses import dataclass

import torch


@dataclass
class YaRNConfig:
    factor: float = 16.0
    orig_max: int = 2048
    beta_fast: float = 32.0
    beta_slow: float = 1.0
    enabled: bool = False


def yarn_scale_inv_freq(inv_freq: torch.Tensor, d_head: int,
                        cfg: YaRNConfig) -> torch.Tensor:
    """Apply NTK-by-parts ramp to inv_freq."""
    if not cfg.enabled or cfg.factor <= 1.0:
        return inv_freq
    # inv_dim low/high cutoffs from beta values
    inv_dim = torch.arange(0, d_head, 2, device=inv_freq.device).float() / d_head
    low = inv_dim * cfg.beta_fast   # actually uses the inv_dim(beta) trick;
    high = inv_dim * cfg.beta_slow  # we approximate the same ramp shape here
    # Ramp over frequency bands (reference `clamp((arange-low)/(high-low))` form)
    freqs = 1.0 / inv_freq.clamp(min=1e-12)
    dim = torch.arange(0, d_head, 2, device=inv_freq.device).float()
    # low/high cutoffs in dim space
    lo = d_head * math.log(cfg.orig_max / cfg.beta_slow) / math.log(10000.0) \
        if cfg.beta_slow > 0 else 0.0
    hi = d_head * math.log(cfg.orig_max / cfg.beta_fast) / math.log(10000.0) \
        if cfg.beta_fast > 0 else float(d_head)
    lo, hi = min(lo, hi), max(lo, hi)
    ramp = ((dim - lo) / max(hi - lo, 1e-6)).clamp(0.0, 1.0)
    scale = (1.0 - ramp + ramp / cfg.factor)
    _ = (low, high, freqs)  # keep names for traceability
    return inv_freq * scale.to(inv_freq.device)


def apply_yarn_to_rope(rope_module, cfg: YaRNConfig) -> None:
    """Patch an existing RotaryEmbedding in-place + rebuild cache.

    rope_module: instance of topogpt3.model.RotaryEmbedding
    """
    with torch.no_grad():
        rope_module.inv_freq.copy_(
            yarn_scale_inv_freq(rope_module.inv_freq, rope_module.inv_freq.numel() * 2, cfg)
        )
    # rebuild cache with current length
    cur = rope_module._cos_cache.shape[0]
    rope_module._build_cache(cur)
    rope_module.yarn_cfg = cfg  # type: ignore[attr-defined]
