"""Checkpoint architecture discovery shared by inference, API and trainers.

The checkpoints store architecture in two places: ``state.json`` (scale only
for some trainers) and the safetensors shapes. Relying on a hardcoded scale
silently loads a wrong model, so every entrypoint should use this module.
"""

from __future__ import annotations

import json
from dataclasses import fields
from pathlib import Path
from typing import Any

_D_MODEL_TO_SCALE = {
    64: "micro",
    256: "small",
    512: "medium",  # disambiguated by layer count below
    576: "xlarge",
    768: "gpt2",
}


def read_state(checkpoint_dir: str | Path) -> dict[str, Any]:
    path = Path(checkpoint_dir) / "state.json"
    if not path.is_file():
        return {}
    try:
        data = json.loads(path.read_text())
    except (OSError, ValueError):
        return {}
    return data if isinstance(data, dict) else {}


def probe_checkpoint(checkpoint_dir: str | Path) -> dict[str, Any]:
    """Infer scale, dimensions and KV heads from ``state.json`` + weights."""
    from safetensors import safe_open

    path = Path(checkpoint_dir) / "model.safetensors"
    if not path.is_file():
        raise FileNotFoundError(f"model.safetensors not found in {checkpoint_dir}")

    state = read_state(checkpoint_dir)
    state_scale = state.get("SCALE") or state.get("config", {}).get("SCALE")

    with safe_open(str(path), framework="pt", device="cpu") as handle:
        keys = list(handle.keys())
        embed = handle.get_tensor("token_embed.weight")
        vocab, d_model = int(embed.shape[0]), int(embed.shape[1])
        layers = sorted(
            {
                int(key.split(".")[1])
                for key in keys
                if key.startswith("layers.") and key.split(".")[1].isdigit()
            }
        )
        n_layers = (max(layers) + 1) if layers else 1

        k_dim = None
        for key in keys:
            if key.endswith("attn.k_proj.weight"):
                k_dim = int(handle.get_tensor(key).shape[0])
                break

    scale = str(state_scale) if state_scale else _D_MODEL_TO_SCALE.get(d_model)
    if d_model == 512:
        scale = "large" if n_layers >= 13 else "medium"
    if scale is None:
        scale = "custom"

    return {
        "scale": scale,
        "vocab_size": vocab,
        "d_model": d_model,
        "n_layers": n_layers,
        "k_dim": k_dim,
        "state": state,
    }


def config_from_checkpoint(
    checkpoint_dir: str | Path,
    device: str = "cpu",
    scale: str | None = None,
):
    """Build a ``TopoGPT2Config`` that matches the checkpoint on disk."""
    from .model import TopoGPT2Config

    meta = probe_checkpoint(checkpoint_dir)
    chosen = scale or meta["scale"]

    preset_scales = {"micro", "small", "medium", "large", "xlarge", "gpt2"}
    if chosen not in preset_scales:
        chosen = "custom"

    cfg = TopoGPT2Config(SCALE=chosen, DEVICE=device)
    cfg.VOCAB_SIZE = meta["vocab_size"]

    # If the preset disagrees with the tensor shapes, force a custom config.
    if cfg.D_MODEL != meta["d_model"] or cfg.N_LAYERS != meta["n_layers"]:
        cfg.SCALE = "custom"
        cfg.D_MODEL = meta["d_model"]
        cfg.N_LAYERS = meta["n_layers"]
        if cfg.D_MODEL % cfg.N_HEADS:
            for heads in (12, 8, 6, 4, 2, 1):
                if cfg.D_MODEL % heads == 0:
                    cfg.N_HEADS = heads
                    break
        cfg.D_HEAD = cfg.D_MODEL // cfg.N_HEADS
        cfg.D_QUAT = cfg.D_MODEL // 4
        cfg.ATTN_WINDOW = min(cfg.ATTN_WINDOW or cfg.MAX_SEQ_LEN, cfg.MAX_SEQ_LEN)

    if meta["k_dim"] and cfg.D_HEAD:
        cfg.N_KV_HEADS = max(1, meta["k_dim"] // cfg.D_HEAD)
        cfg.GQA_GROUPS = cfg.N_HEADS // cfg.N_KV_HEADS

    return cfg, meta


def state_summary(checkpoint_dir: str | Path) -> dict[str, Any]:
    """Small JSON-friendly summary for logs and /v1/models metadata."""
    try:
        meta = probe_checkpoint(checkpoint_dir)
    except (OSError, ValueError, KeyError):
        return {}
    return {k: v for k, v in meta.items() if k != "state"}


def config_dict(cfg: Any) -> dict[str, Any]:
    return {f.name: getattr(cfg, f.name) for f in fields(cfg) if hasattr(cfg, f.name)}
