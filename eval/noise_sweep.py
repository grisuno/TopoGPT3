#!/usr/bin/env python3
"""Barrido de ruido en los pesos espectrales del checkpoint TopoGPT3.

Para cada nivel sigma en --sigmas:
  1. Carga el checkpoint base (NO modifica el archivo, solo los pesos en RAM)
  2. Inyecta ruido gaussiano N(0, sigma) en los kernels espectrales
     cuaternionicos (kr_w/x/y/z, ki_w/x/y/z) y solo en ellos.
     Asi aislamos el efecto del ruido sobre la parte que el marco
     teorico dice que esta protegida topologicamente.
  3. Genera pass@1 (greedy, T=0) sobre los primeros N problemas de
     HumanEval (subset para mantener tiempo de pared manejable)
  4. Ejecuta los tests canonicos y mide pass rate

Salida: eval/runs/noise_<sigma>_<tag>.jsonl
        eval/runs/noise_sweep_<timestamp>.jsonl (resumen agregado)
"""
from __future__ import annotations

import argparse
import json
import math
import sys
import time
from pathlib import Path
from typing import Dict, List

import torch

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from topogpt3 import TopoGPT2, TopoGPT2Config, BPETokenizer, set_seed  # noqa: E402
from topogpt3.model import QuaternionSpectralLayer  # noqa: E402
from safetensors.torch import load_file  # noqa: E402
from safetensors import safe_open  # noqa: E402

# Reutilizar la maquinaria del harness ya escrita
from eval.harness import (  # noqa: E402
    load_humaneval,
    build_prompt,
    extract_candidate,
    run_one_test,
)


def inject_noise(model: TopoGPT2, sigma: float, seed: int) -> Dict[str, int]:
    """
    Anade N(0, sigma) a TODOS los kernels espectrales (kr_*, ki_*).
    Retorna un dict con conteo de tensores ruidosos y de parametros
    modificados.
    """
    if sigma <= 0.0:
        return {"tensors_noised": 0, "params_noised": 0}
    g = torch.Generator(device="cpu").manual_seed(seed)
    n_tensors = 0
    n_params = 0
    with torch.no_grad():
        for mod in model.modules():
            if isinstance(mod, QuaternionSpectralLayer):
                for c in ("w", "x", "y", "z"):
                    for prefix in ("kr_", "ki_"):
                        pname = f"{prefix}{c}"
                        if hasattr(mod, pname):
                            p = getattr(mod, pname)
                            noise = torch.randn(
                                p.shape, generator=g, dtype=torch.float32
                            ) * sigma
                            p.add_(noise.to(p.dtype))
                            n_tensors += 1
                            n_params += p.numel()
    return {"tensors_noised": n_tensors, "params_noised": n_params}


def load_model(ckpt_dir: str, ckpt_name: str, device: str):
    """Reconstruye TopoGPT2 alineado con el checkpoint, sin acceso a
    harness.ModelLoader (queremos un loader limpio que no comparta
    estado con corridas paralelas)."""
    with safe_open(
        f"{ckpt_dir}/{ckpt_name}/model.safetensors",
        framework="pt", device="cpu"
    ) as h:
        t = h.get_tensor("layers.0.attn.k_proj.weight")
        k_dim = int(t.shape[0])
    d_head = 32
    n_kv = k_dim // d_head
    cfg = TopoGPT2Config(SCALE="small", DEVICE=device, N_KV_HEADS=n_kv)
    tok = BPETokenizer("gpt2")
    cfg.VOCAB_SIZE = tok.vocab_size
    model = TopoGPT2(cfg).to(device).eval()
    sd = load_file(
        f"{ckpt_dir}/{ckpt_name}/model.safetensors", device=device
    )
    model.load_state_dict(sd, strict=False)
    set_seed(42, device)
    return model, tok, cfg


@torch.no_grad()
def generate_one(model, tok, prompt: str, max_new_tokens: int, device: str):
    ids = tok.encode(prompt)
    if not ids:
        return prompt, 0
    x = torch.tensor([ids], dtype=torch.long, device=device)
    t0 = time.time()
    out = model.generate(
        x,
        max_new_tokens=max_new_tokens,
        temperature=0.0,   # greedy para pass@1 deterministico
        top_k=0,
        repetition_penalty=1.0,
    )
    dt = time.time() - t0
    text = tok.decode(out[0].tolist())
    return text, dt


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--checkpoint-dir", default="checkpoints_topogpt3")
    ap.add_argument("--checkpoint-name", default="last")
    ap.add_argument("--sigmas", default="0,1e-4,1e-3,1e-2",
                    help="lista separada por comas, e.g. 0,1e-4,1e-3")
    ap.add_argument("--n-problems", type=int, default=50,
                    help="subset de HumanEval (max 164)")
    ap.add_argument("--max-new-tokens", type=int, default=256)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--out-dir", default="eval/runs")
    ap.add_argument("--tag", default=None)
    args = ap.parse_args()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    tag = args.tag or time.strftime("%Y%m%d_%H%M%S")

    sigmas = [float(s) for s in args.sigmas.split(",")]

    print(f"Loading HumanEval ({args.n_problems} problems)...")
    he = load_humaneval()
    he = he[: args.n_problems]
    print(f"  loaded {len(he)} problems")

    print(f"Loading model from {args.checkpoint_dir}/{args.checkpoint_name}...")
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model, tok, _ = load_model(
        args.checkpoint_dir, args.checkpoint_name, device
    )
    n_params = sum(p.numel() for p in model.parameters())
    print(f"  model ready: {n_params:,} params, device={device}")

    summary_records = []
    for sigma in sigmas:
        print(f"\n=== sigma = {sigma} ===")
        # Snapshot del state_dict base para restauracion
        # (mas simple: recargar el modelo entre sigmas, ~150MB)
        if sigma != 0.0:
            del model
            model, tok, _ = load_model(
                args.checkpoint_dir, args.checkpoint_name, device
            )
        n_info = inject_noise(model, sigma, args.seed)
        print(f"  noise injected: {n_info['tensors_noised']} tensors, "
              f"{n_info['params_noised']:,} params")

        results = []
        n_pass = 0
        t_start = time.time()
        for i, prob in enumerate(he):
            prompt = build_prompt(prob)
            try:
                raw, dt = generate_one(
                    model, tok, prompt, args.max_new_tokens, device
                )
                candidate = extract_candidate(prompt, raw)
                passed, msg, _so, _se, _tb = run_one_test(
                    prob, candidate, timeout=20.0
                )
            except Exception as exc:
                passed, msg, candidate = False, f"runner_crash: {exc}", ""
                dt = 0.0
            if passed:
                n_pass += 1
            results.append({
                "task_id": prob["task_id"],
                "passed": bool(passed),
                "error": msg if not passed else None,
                "elapsed_s": dt,
            })
            if (i + 1) % 10 == 0:
                print(f"  [{i+1}/{len(he)}]  pass@1 so far = "
                      f"{n_pass}/{i+1} = {100*n_pass/(i+1):.1f}%")
        wall = time.time() - t_start
        pass1 = n_pass / len(he)
        print(f"  --> pass@1 = {n_pass}/{len(he)} = {100*pass1:.2f}%  "
              f"(wall {wall:.1f}s)")

        per_run = {
            "sigma": sigma,
            "n_problems": len(he),
            "n_pass": n_pass,
            "pass_at_1": pass1,
            "wall_s": wall,
            "noise_info": n_info,
        }
        summary_records.append(per_run)
        out_path = out_dir / f"noise_sigma{sigma:.0e}_{tag}.jsonl"
        with out_path.open("w") as f:
            for r in results:
                f.write(json.dumps(r) + "\n")
        print(f"  wrote {out_path}")

    summary_path = out_dir / f"noise_sweep_{tag}.jsonl"
    with summary_path.open("w") as f:
        for r in summary_records:
            f.write(json.dumps(r) + "\n")
    print(f"\nSummary: {summary_path}")
    print()
    print("=" * 60)
    print("ROBUSTEZ TOPOLOGICA (prediccion del marco):")
    print("=" * 60)
    if summary_records:
        baseline = summary_records[0]["pass_at_1"]
        print(f"  baseline (sigma=0): pass@1 = {100*baseline:.2f}%")
        for r in summary_records[1:]:
            drop = 100 * (baseline - r["pass_at_1"])
            print(f"  sigma={r['sigma']:.0e}: pass@1 = "
                  f"{100*r['pass_at_1']:.2f}%  (drop = {drop:+.2f} pp)")


if __name__ == "__main__":
    main()
