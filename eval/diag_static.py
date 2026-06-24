#!/usr/bin/env python3
"""Diagnostico estatico de un checkpoint TopoGPT3 congelado.

Calcula sobre los pesos espectrales congelados (sin reentrenar):

  kappa_F   = sigma_max / sigma_min  del kernel espectral apilado
              (proxy del condition number de la Grassmanniana)
  delta     = max |theta - round(theta)|  sobre los arg det de overlaps
              (cuantifica cuanto se "discretizan" las fases complejas)
  W         = (1/2pi) sum arg det <U_n | U_{n+1}>  (winding acumulado
              sobre barridos en frecuencia — sin trayectoria temporal
              real, usamos un barrido sintetico sobre los modos FFT)
  r         = rango dominante por elbow de los valores singulares
  sigma_*   = valores singulares principales

NOTA IMPORTANTE: Este script NO reentrena. Trabaja unicamente con los
kernels espectrales cuaternionicos ya aprendidos. La "trayectoria" W
se define barriendo sobre los modos de frecuencia (no sobre pasos de
entrenamiento), asi que W aqui mide coherencia de fase intra-modelo,
no winding temporal. Esta distincion se reporta explicitamente en
el JSONL de salida.

Salida: eval/runs/diag_static_<timestamp>.jsonl
"""
from __future__ import annotations

import argparse
import json
import math
import sys
import time
from pathlib import Path
from typing import Any, Dict, List

import torch

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from topogpt3 import GrassmannianTracker  # noqa: E402
from topogpt3.model import TopoGPT2Config, TopoGPT2  # noqa: E402
from safetensors.torch import load_file  # noqa: E402


# ---------------------------------------------------------------------------
# delta: discretizacion de fases complejas
# ---------------------------------------------------------------------------

def phase_discretization(K: torch.Tensor, n_samples: int = 1024,
                         seed: int = 0) -> Dict[str, float]:
    """
    Muestrea n_samples overlaps aleatorios <u_i | u_j> sobre los vectores
    singulares de K y mide cuanto se aleja su fase arg del reticulo 2*pi*Z.

    delta = max |theta/2pi - round(theta/2pi)| sobre la muestra.

    Tambien devuelve:
      delta_mean, delta_median, frac_near_integer (|.| < 0.05)
    """
    g = torch.Generator().manual_seed(seed)
    U, S, Vh = torch.linalg.svd(K, full_matrices=False)
    n_vecs = U.shape[1]
    if n_vecs < 2:
        return {"delta_max": 0.0, "delta_mean": 0.0, "delta_median": 0.0,
                "frac_near_integer": 1.0, "n_samples": 0}

    # Muestrear pares (i, j) con i != j
    idx_i = torch.randint(0, n_vecs, (n_samples,), generator=g)
    idx_j = torch.randint(0, n_vecs, (n_samples,), generator=g)
    idx_j = torch.where(idx_j == idx_i, (idx_j + 1) % n_vecs, idx_j)

    phases = []
    for k in range(n_samples):
        i, j = int(idx_i[k]), int(idx_j[k])
        ov = (U[:, i].conj() @ U[:, j])
        ph = float(torch.atan2(ov.imag, ov.real).item())
        phases.append(ph)

    # Normalizar a [0, 1) sobre el circulo unidad
    norm = [abs((p / (2 * math.pi)) - round(p / (2 * math.pi))) for p in phases]
    norm_t = torch.tensor(norm)
    return {
        "delta_max": float(norm_t.max().item()),
        "delta_mean": float(norm_t.mean().item()),
        "delta_median": float(norm_t.median().item()),
        "frac_near_integer": float((norm_t < 0.05).float().mean().item()),
        "n_samples": n_samples,
    }


# ---------------------------------------------------------------------------
# W sintetico: barrido sobre modos de frecuencia
# ---------------------------------------------------------------------------

def synthetic_winding(K: torch.Tensor, n_windows: int = 16,
                      window_size: int | None = None) -> float:
    """
    Como el checkpoint es estatico, no hay trayectoria temporal.
    Construimos una pseudo-trayectoria deslizando una ventana sobre
    los modos de frecuencia (filas de K) y acumulando arg det del
    overlap entre ventanas consecutivas.

    W = (1/2pi) sum_n arg det <U_{n} | U_{n+1}>
    """
    U, S, _Vh = torch.linalg.svd(K, full_matrices=False)
    N = U.shape[0]
    r = min(U.shape[1], 32)  # cap para que el det no explote
    U = U[:, :r]
    if window_size is None:
        window_size = max(1, N // n_windows)
    accum = 0.0
    prev = None
    for w0 in range(0, N - window_size, window_size):
        chunk = U[w0 : w0 + window_size, :]
        # SVD local para quedarnos con el subespacio dominante de la ventana
        try:
            u, _s, _vh = torch.linalg.svd(chunk, full_matrices=False)
            U_w = u[:, : min(r, u.shape[1])]
            if U_w.shape[1] < r:
                pad = torch.zeros(U_w.shape[0], r - U_w.shape[1],
                                  dtype=U_w.dtype)
                U_w = torch.cat([U_w, pad], dim=1)
        except RuntimeError:
            continue
        if prev is not None:
            rmin = min(prev.shape[1], U_w.shape[1])
            rrows = min(prev.shape[0], U_w.shape[0])
            overlap = prev[:rrows, :rmin].conj().T @ U_w[:rrows, :rmin]
            try:
                det = torch.linalg.det(overlap)
                accum += float(torch.atan2(det.imag, det.real).item()) / (
                    2 * math.pi
                )
            except RuntimeError:
                continue
        prev = U_w
    return accum


# ---------------------------------------------------------------------------
# kappa y singulares
# ---------------------------------------------------------------------------

def static_kappa(K: torch.Tensor) -> Dict[str, Any]:
    try:
        U, S, _Vh = torch.linalg.svd(K, full_matrices=False)
    except RuntimeError:
        return {"kappa": float("inf"), "sigma_max": 0.0, "sigma_min": 0.0,
                "n_singular": 0}
    S_abs = S.abs().float()
    nz = S_abs[S_abs > 1e-12]
    if nz.numel() == 0:
        return {"kappa": float("inf"), "sigma_max": 0.0, "sigma_min": 0.0,
                "n_singular": int(S_abs.numel())}
    return {
        "kappa": float(nz[0].item() / nz[-1].item()),
        "sigma_max": float(nz[0].item()),
        "sigma_min": float(nz[-1].item()),
        "n_singular": int(S_abs.numel()),
        "sigma_top16": [float(x) for x in S_abs[:16].tolist()],
    }


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--checkpoint-dir", default="checkpoints_topogpt3")
    parser.add_argument("--checkpoint-name", default="last")
    parser.add_argument("--out", default=None)
    parser.add_argument("--n-phase-samples", type=int, default=1024)
    args = parser.parse_args()

    out_path = Path(args.out) if args.out else (
        REPO_ROOT / "eval" / "runs" / f"diag_static_{int(time.time())}.jsonl"
    )
    out_path.parent.mkdir(parents=True, exist_ok=True)

    print(f"Loading checkpoint: {args.checkpoint_dir}/{args.checkpoint_name}")
    cfg = TopoGPT2Config(SCALE="small")
    model = TopoGPT2(cfg)
    state_path = Path(args.checkpoint_dir) / args.checkpoint_name / "model.safetensors"
    state = load_file(state_path)
    # Inyectar fp32 / float en caso de que el checkpoint guarde fp16
    state = {k: v.float() for k, v in state.items()}
    missing, unexpected = model.load_state_dict(state, strict=False)
    if missing:
        print(f"  WARN missing keys: {len(missing)} (showing first 5) {missing[:5]}")
    if unexpected:
        print(f"  WARN unexpected keys: {len(unexpected)} (showing first 5) {unexpected[:5]}")
    model.eval()
    n_params = sum(p.numel() for p in model.parameters())
    print(f"  loaded: {n_params:,} parameters, {len(state)} tensors")

    print("Stacking spectral kernels K(theta)...")
    K = GrassmannianTracker._stack_spectral_kernels(model)
    print(f"  K shape: {tuple(K.shape)}, dtype: {K.dtype}")

    print("Computing static kappa / singulars...")
    k = static_kappa(K)
    print(f"  kappa = {k['kappa']:.4e}   sigma_max = {k['sigma_max']:.4e}   sigma_min = {k['sigma_min']:.4e}")

    print("Computing delta (phase discretisation)...")
    d = phase_discretization(K, n_samples=args.n_phase_samples)
    print(f"  delta_max = {d['delta_max']:.4f}   delta_mean = {d['delta_mean']:.4f}   frac_near_integer = {d['frac_near_integer']:.3f}")

    print("Computing synthetic winding W (frequency-window sweep)...")
    W = synthetic_winding(K)
    print(f"  W = {W:+.4f}")

    # SVD top-k para inspección
    U, S, _Vh = torch.linalg.svd(K, full_matrices=False)
    sv_top = [float(x) for x in S.abs()[:32].tolist()]

    record = {
        "timestamp": time.time(),
        "checkpoint": f"{args.checkpoint_dir}/{args.checkpoint_name}",
        "n_params": n_params,
        "K_shape": list(K.shape),
        "K_dtype": str(K.dtype),
        "kappa": k["kappa"],
        "sigma_max": k["sigma_max"],
        "sigma_min": k["sigma_min"],
        "n_singular": k["n_singular"],
        "sigma_top16": k["sigma_top16"],
        "delta_max": d["delta_max"],
        "delta_mean": d["delta_mean"],
        "delta_median": d["delta_median"],
        "frac_near_integer": d["frac_near_integer"],
        "delta_n_samples": d["n_samples"],
        "W_synthetic": W,
        "W_note": "synthetic: window sweep over frequency modes, NOT temporal training trajectory",
        "sv_top32": sv_top,
    }

    with open(out_path, "w") as f:
        f.write(json.dumps(record) + "\n")
    print(f"\nWrote: {out_path}")
    print()
    print("=" * 60)
    print("INTERPRETATION (ver marco teorico):")
    print("=" * 60)
    if k["kappa"] < 10:
        print(f"  kappa = {k['kappa']:.2e}  -> REGIMEN ESTABLE (cristal)")
    elif k["kappa"] < 1e4:
        print(f"  kappa = {k['kappa']:.2e}  -> REGIMEN INTERMEDIO")
    else:
        print(f"  kappa = {k['kappa']:.2e}  -> REGIMEN CAOTICO (vidrio)")
    if d["delta_max"] < 0.05:
        print(f"  delta_max = {d['delta_max']:.4f}  -> fases cuasi-discretas (orden topologico)")
    elif d["delta_max"] < 0.25:
        print(f"  delta_max = {d['delta_max']:.4f}  -> fases parcialmente ordenadas")
    else:
        print(f"  delta_max = {d['delta_max']:.4f}  -> fases difusas (no hay orden topologico)")


if __name__ == "__main__":
    main()
