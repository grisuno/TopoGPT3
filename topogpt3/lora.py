"""Native LoRA for TopoGPT3.

Quaternion-safe: in addition to plain nn.Linear, it descends into
QuaternionLinear's four sub-linears (Ww/Wx/Wy/Wz) and SwiGLU projections,
so the spectral/torus identity is preserved — adapters are purely additive
deltas initialized at zero, base weights untouched until explicit merge.
"""
from __future__ import annotations

from typing import Dict, List

import torch
from torch import nn


class LoRA(nn.Module):
    def __init__(self, in_features: int, out_features: int, rank: int = 16):
        super().__init__()
        self.rank = rank
        self.A = nn.Linear(in_features, rank, bias=False)
        self.B = nn.Linear(rank, out_features, bias=False)
        nn.init.normal_(self.A.weight, mean=0.0, std=0.02)
        nn.init.zeros_(self.B.weight)

    def forward(self, x):
        return self.B(self.A(x))


def _is_quaternion_sublayer(name: str) -> bool:
    return any(k in name for k in (".Ww", ".Wx", ".Wy", ".Wz", "Ww", "Wx", "Wy", "Wz")) \
        or "quaternion" in name.lower()


def lora_targets(model: nn.Module, include_mlp: bool = False):
    """Yield (name, nn.Linear) candidates.

    Default targets square Q/K/V/O projections; include_mlp=True also adapts SwiGLU gate/up/down + torus proj.
    QuaternionLinear sub-linears are square by construction (D_QUAT x D_QUAT)
    and are included by default.
    """
    for name, mod in model.named_modules():
        if not isinstance(mod, nn.Linear):
            continue
        square = mod.in_features == mod.out_features
        mlp = any(k in name for k in ("gate_proj", "up_proj", "down_proj",
                                      "torus_proj", "enc_proj", "dec_proj"))
        if square or (include_mlp and mlp):
            # skip tied lm_head to preserve weight tying
            if name.endswith("lm_head"):
                continue
            yield name, mod


def apply_lora(model: nn.Module, rank: int = 16,
               include_mlp: bool = False) -> List[str]:
    """Monkey-patch target linears with additive LoRA. Returns patched names."""
    patched = []
    device = next(model.parameters()).device
    for name, mod in list(lora_targets(model, include_mlp)):
        if hasattr(mod, "lora"):
            continue
        lora = LoRA(mod.in_features, mod.out_features, rank=rank).to(device)
        mod.lora = lora  # type: ignore[attr-defined]
        orig_forward = mod.forward

        def _fwd(x, _o=orig_forward, _l=lora):
            return _o(x) + _l(x)
        mod.forward = _fwd  # type: ignore[method-assign]
        patched.append(name)
    return patched


def lora_parameters(model: nn.Module):
    for _, mod in model.named_modules():
        if hasattr(mod, "lora"):
            for p in mod.lora.parameters():  # type: ignore[attr-defined]
                yield p


def freeze_non_lora(model: nn.Module) -> None:
    for n, p in model.named_parameters():
        if ".lora." not in n:
            p.requires_grad = False
        else:
            p.requires_grad = True


def save_lora(model: nn.Module, path: str) -> None:
    raw = getattr(model, "_orig_mod", model)
    sd: Dict[str, torch.Tensor] = {}
    for name, mod in raw.named_modules():
        if hasattr(mod, "lora"):
            clean = name[7:] if name.startswith("module.") else name
            for k, v in mod.lora.state_dict().items():  # type: ignore[attr-defined]
                sd[f"{clean}.lora.{k}"] = v.cpu().half()
    torch.save(sd, path)


def load_lora(model: nn.Module, path: str, device=None) -> None:
    sd = torch.load(path, map_location=device or "cpu")
    sd = {(k[7:] if k.startswith("module.") else k): v for k, v in sd.items()}
    for name, mod in model.named_modules():
        if hasattr(mod, "lora"):
            sub = {k.replace(f"{name}.lora.", ""): v
                   for k, v in sd.items() if f"{name}.lora." in k}
            if sub:
                mod.lora.load_state_dict(sub)  # type: ignore[attr-defined]


def merge_lora(model: nn.Module, lora_path: str, save_path: str) -> None:
    """Merge LoRA deltas into base weights and save (fp16, no .lora. keys)."""
    load_lora(model, lora_path)
    raw = getattr(model, "_orig_mod", model)
    sd = {k: v.cpu().half() for k, v in raw.state_dict().items() if ".lora." not in k}
    for name, mod in raw.named_modules():
        if isinstance(mod, nn.Linear) and ".lora." not in name and hasattr(mod, "lora"):
            delta = (mod.lora.B.weight.data @ mod.lora.A.weight.data).cpu().half()  # type: ignore[attr-defined]
            sd[f"{name}.weight"] = (mod.weight.data.cpu().half() + delta)
    torch.save(sd, save_path)
