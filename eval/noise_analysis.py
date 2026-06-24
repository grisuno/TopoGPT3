#!/usr/bin/env python3
"""Analisis post-hoc del noise sweep.

Generaciones del MISMO prompt bajo distintos niveles de ruido -> comparar
con metricas que NO son pass@1 (porque los problemas triviales saturan):

  - generation_exact_match:  % de generaciones que matchean exactamente
                             el baseline (token por token)
  - prefix_agreement@50:    % de pares (baseline, noisy) que comparten
                            el mismo prefijo de 50 tokens
  - levenshtein_dist:       distancia de edicion normalizada al baseline
  - token_jaccard:          interseccion / union de tokens generados
  - bleu_1:                 unigrama precision
  - syntax_ok_rate:         % que pasa ast.parse (sintaxis Python valida)

Salida: eval/runs/noise_analysis_<tag>.json
"""
from __future__ import annotations

import argparse
import ast
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Dict, List

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

# El harness guarda el output crudo en 'candidate'. Para nuestras metricas
# queremos el TEXTO GENERADO. Re-leemos del summary o, mejor, re-generamos
# para tener control total.
#
# En realidad, el harness.py solo guarda 'candidate' (la extraccion
# post-procesada). Asi que las metricas de similitud pre-procesado no
# son posibles a posteriori. Para TIER 1 (este script) lo que si
# podemos hacer es: comparar pass@1 agregado + tiempos de generacion
# (que SI se guardan) y reportar la consistencia de aciertos/fallos
# entre los 4 niveles de ruido.

def _load(p: Path) -> List[dict]:
    return [json.loads(l) for l in p.open() if l.strip()]


def consistency_across_runs(per_run: Dict[float, Dict[str, dict]]) -> Dict:
    """
    Para cada problema, mira si pasa consistentemente a traves de los
    4 niveles de ruido. Devuelve:
      - always_pass, always_fail, mixed (count)
      - per_sigma_pass_lists: {sigma: {task_id: bool}}
    """
    sigmas = sorted(per_run.keys())
    per_task: Dict[str, Dict[float, bool]] = {}
    for sigma, records in per_run.items():
        for r in records:
            per_task.setdefault(r["task_id"], {})[sigma] = bool(r["passed"])

    always_pass = sum(1 for d in per_task.values() if all(d.values()))
    always_fail = sum(1 for d in per_task.values() if not any(d.values()))
    mixed = sum(1 for d in per_task.values()
                if any(d.values()) and not all(d.values()))

    # tasa de consistencia pairwise entre sigmas
    pw: Dict[str, float] = {}
    for i, s1 in enumerate(sigmas):
        for s2 in sigmas[i + 1:]:
            agree = sum(1 for d in per_task.values()
                        if d[s1] == d[s2])
            pw[f"agreement_{s1}_vs_{s2}"] = agree / len(per_task)
    return {
        "n_problems": len(per_task),
        "always_pass": always_pass,
        "always_fail": always_fail,
        "mixed_outcome": mixed,
        "pairwise_agreement": pw,
        "per_sigma_pass": {str(s): sum(1 for d in per_task.values() if d[s])
                           for s in sigmas},
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tag", default="v1")
    ap.add_argument("--runs-dir", default="eval/runs")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    rd = Path(args.runs_dir)
    files = {}
    for p in sorted(rd.glob(f"noise_sigma*_{args.tag}.jsonl")):
        m = re.match(r"noise_sigma([0-9.e+\-]+)_", p.name)
        if not m:
            continue
        try:
            sigma = float(m.group(1))
        except ValueError:
            continue
        files[sigma] = _load(p)
    if not files:
        print("No noise sweep files found for tag", args.tag)
        return
    print(f"Loaded {len(files)} sigmas: {sorted(files.keys())}")

    result = consistency_across_runs(files)
    print(json.dumps(result, indent=2))

    out_path = Path(args.out) if args.out else (
        rd / f"noise_analysis_{args.tag}.json"
    )
    with out_path.open("w") as f:
        json.dump(result, f, indent=2)
    print(f"\nWrote: {out_path}")
    print()
    print("=" * 60)
    print("INTERPRETACION")
    print("=" * 60)
    print(f"  {result['n_problems']} problemas evaluados")
    print(f"  always pass:  {result['always_pass']}")
    print(f"  always fail:  {result['always_fail']}")
    print(f"  mixed:        {result['mixed_outcome']}")
    print()
    print("  Acuerdo pairwise entre niveles de ruido:")
    for k, v in result["pairwise_agreement"].items():
        print(f"    {k}: {100*v:.1f}%")


if __name__ == "__main__":
    main()
