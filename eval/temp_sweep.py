#!/usr/bin/env python3
"""Barrido de temperatura x top-k sobre HumanEval.

Mide pass@1 en modo greedy (T=0) y pass@5 a temperaturas crecientes
para mapear la "fase" de generacion del modelo:

  - cristal: pass@1 alto, poca varianza entre samples
  - vidrio:  pass@1 bajo, alta varianza
  - caotico: pass@1 ~= 0, alta diversidad pero sin aciertos

Salida: eval/runs/temp_sweep_<tag>.jsonl (resumen)
        eval/runs/temp_<T>_top<k>_<tag>.jsonl (detalle por config)
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

from eval.noise_sweep import load_model  # noqa: E402
from eval.harness import (  # noqa: E402
    load_humaneval,
    build_prompt,
    extract_candidate,
    run_one_test,
)


@torch.no_grad()
def generate_one(model, tok, prompt, max_new_tokens, temperature, top_k,
                 device, seed_offset):
    if seed_offset:
        torch.manual_seed(42 + seed_offset * 9973)
    ids = tok.encode(prompt)
    if not ids:
        return prompt, 0.0
    x = torch.tensor([ids], dtype=torch.long, device=device)
    t0 = time.time()
    out = model.generate(
        x,
        max_new_tokens=max_new_tokens,
        temperature=temperature,
        top_k=top_k,
        repetition_penalty=1.0,
    )
    return tok.decode(out[0].tolist()), time.time() - t0


def evaluate_problems(model, tok, problems, max_new_tokens, temperature,
                      top_k, n_samples, device) -> List[dict]:
    results = []
    for prob in problems:
        prompt = build_prompt(prob)
        samples = []
        for s in range(n_samples):
            try:
                raw, dt = generate_one(
                    model, tok, prompt, max_new_tokens,
                    temperature, top_k, device, s
                )
                cand = extract_candidate(prompt, raw)
                passed, msg, *_ = run_one_test(prob, cand, timeout=20.0)
            except Exception as exc:
                passed, msg, cand = False, f"runner_crash: {exc}", ""
                dt = 0.0
            samples.append({
                "sample_idx": s,
                "passed": bool(passed),
                "error": msg if not passed else None,
                "elapsed_s": dt,
            })
        results.append({
            "task_id": prob["task_id"],
            "samples": samples,
        })
    return results


def pass_at_k_unbiased(n: int, c: int, k: int) -> float:
    if n - c < k:
        return 1.0
    if c == 0:
        return 0.0
    return 1.0 - math.prod(1.0 - k / (n - i) for i in range(c))


def summarize(results: List[dict], n_samples: int) -> Dict:
    n_probs = len(results)
    pass1_each = [1.0 if r["samples"][0]["passed"] else 0.0 for r in results]
    passk_each = []
    for r in results:
        c = sum(1 for s in r["samples"] if s["passed"])
        if n_samples == 1:
            passk_each.append(float(c > 0))
        else:
            passk_each.append(pass_at_k_unbiased(n_samples, c, n_samples))
    return {
        "n_problems": n_probs,
        "n_samples": n_samples,
        "pass@1": sum(pass1_each) / n_probs,
        f"pass@{n_samples}": sum(passk_each) / n_probs,
        "any_pass_rate": sum(1 for r in results
                             if any(s["passed"] for s in r["samples"])) / n_probs,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--checkpoint-dir", default="checkpoints_topogpt3")
    ap.add_argument("--checkpoint-name", default="last")
    ap.add_argument("--n-problems", type=int, default=30)
    ap.add_argument("--max-new-tokens", type=int, default=256)
    ap.add_argument("--tag", default=None)
    ap.add_argument("--out-dir", default="eval/runs")
    ap.add_argument("--configs", default="0.0/0,0.2/40,0.5/40,0.8/40,1.0/40",
                    help="lista T/k separadas por coma, e.g. 0.0/0,0.2/40")
    ap.add_argument("--n-samples", type=int, default=5)
    args = ap.parse_args()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    tag = args.tag or time.strftime("%Y%m%d_%H%M%S")

    print(f"Loading HumanEval ({args.n_problems} problems)...")
    he = load_humaneval()[: args.n_problems]
    print(f"  {len(he)} problems")

    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Loading model on {device}...")
    model, tok, _ = load_model(
        args.checkpoint_dir, args.checkpoint_name, device
    )

    configs = []
    for c in args.configs.split(","):
        t, k = c.split("/")
        configs.append((float(t), int(k)))
    print(f"Configs: {configs}, n_samples={args.n_samples}")

    summary = []
    for T, k in configs:
        print(f"\n=== T={T}, top_k={k}, n_samples={args.n_samples} ===")
        t0 = time.time()
        results = evaluate_problems(
            model, tok, he, args.max_new_tokens, T, k,
            args.n_samples, device
        )
        s = summarize(results, args.n_samples)
        s["T"] = T
        s["top_k"] = k
        s["wall_s"] = time.time() - t0
        summary.append(s)
        print(f"  pass@1 = {100*s['pass@1']:.2f}%   "
              f"pass@{args.n_samples} = {100*s[f'pass@{args.n_samples}']:.2f}%   "
              f"any-pass = {100*s['any_pass_rate']:.2f}%   "
              f"wall = {s['wall_s']:.0f}s")
        # Guardar detalle
        detail_path = out_dir / f"temp_T{T}_top{k}_{tag}.jsonl"
        with detail_path.open("w") as f:
            for r in results:
                f.write(json.dumps(r) + "\n")

    summary_path = out_dir / f"temp_sweep_{tag}.jsonl"
    with summary_path.open("w") as f:
        for s in summary:
            f.write(json.dumps(s) + "\n")
    print(f"\nSummary: {summary_path}")
    print()
    print("=" * 60)
    print("MAPA DE FASES DE GENERACION")
    print("=" * 60)
    print(f"{'T':>5} {'top_k':>6} {'pass@1':>8} "
          f"{'pass@'+str(args.n_samples):>9} {'any-pass':>10}")
    for s in summary:
        print(f"{s['T']:>5.2f} {s['top_k']:>6d} "
              f"{100*s['pass@1']:>7.2f}% "
              f"{100*s[f'pass@{args.n_samples}']:>8.2f}% "
              f"{100*s['any_pass_rate']:>9.2f}%")


if __name__ == "__main__":
    main()
