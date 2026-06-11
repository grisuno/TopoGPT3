#!/usr/bin/env python3
"""Aggregate every JSONL in eval/runs into a final report.

Reads runs from the original pass@k runs, the HRM run, the repair run,
and produces:
  - pass@1 / pass@k tables
  - error-class breakdowns
  - wall-clock / throughput
  - a comparison standard vs HRM
  - a self-repair impact summary
  - emits REPORT.md next to the runs/
"""
from __future__ import annotations

import argparse
import json
import math
import re
import shutil
import statistics
from collections import Counter, defaultdict
from pathlib import Path


def pass_at_k(n, c, k):
    if n - c < k:
        return 1.0
    return 1.0 - math.prod(1.0 - k / (n - i) for i in range(c)) if c > 0 else 0.0


def classify_error(msg):
    if not msg:
        return "ok"
    m = msg.lower()
    if "syntaxerror" in m or "indentationerror" in m or "unexpected eof" in m:
        return "syntax"
    if "nameerror" in m:
        return "undefined_name"
    if "typeerror" in m:
        return "type_error"
    if "indexerror" in m:
        return "off_by_one"
    if "valueerror" in m or "keyerror" in m or "attributeerror" in m or "zerodivisionerror" in m:
        return "edge_case"
    if "assertionerror" in m:
        return "wrong_output"
    if "runner_crash" in m:
        return "runner_crash"
    return "other"


def load_jsonl(p):
    return [json.loads(l) for l in open(p) if l.strip()]


def summarize_run(p):
    recs = load_jsonl(p)
    by_problem = defaultdict(list)
    for r in recs:
        by_problem[r["task_id"]].append(r)
    n_p = len(by_problem)
    n_s = max((len(v) for v in by_problem.values()), default=0)
    pass1 = sum(1 for v in by_problem.values() if v[0]["passed"])
    passk = (
        sum(pass_at_k(len(v), sum(1 for s in v if s["passed"]), n_s) for v in by_problem.values())
        / max(n_p, 1)
        if n_s > 1
        else pass1 / max(n_p, 1)
    )
    elapsed = [r["elapsed_s"] for r in recs if r["elapsed_s"] > 0]
    toks = [r["new_tokens"] for r in recs]
    throughput = [r["new_tokens"] / max(r["elapsed_s"], 1e-3) for r in recs if r["elapsed_s"] > 0]
    err = Counter()
    for v in by_problem.values():
        s0 = v[0]
        if not s0["passed"]:
            err[classify_error(s0.get("error") or "")] += 1
    return {
        "n_problems": n_p,
        "n_samples": n_s,
        "pass@1": f"{pass1}/{n_p} = {100*pass1/max(n_p,1):.2f}%",
        f"pass@{n_s}": f"{100*passk:.2f}%" if n_s > 1 else "n/a",
        "mean_latency_s": f"{(sum(elapsed)/max(len(elapsed),1)):.2f}",
        "mean_new_tokens": f"{(sum(toks)/max(len(toks),1)):.1f}",
        "mean_tok_per_s": f"{(sum(throughput)/max(len(throughput),1)):.1f}",
        "first_try_error_breakdown": dict(err.most_common()),
    }


def repair_summary(repair_path, baseline_path):
    base = {r["task_id"]: r for r in load_jsonl(baseline_path)}
    recs = load_jsonl(repair_path)
    by_tid = defaultdict(list)
    for r in recs:
        by_tid[r["task_id"]].append(r)
    n = len(by_tid)
    n_fixed = 0
    rounds_to_fix = Counter()
    for tid, rounds in by_tid.items():
        was_failed = not base[tid]["passed"]
        if not was_failed:
            continue
        for r in rounds:
            if r["passed"]:
                n_fixed += 1
                rounds_to_fix[r["round"]] += 1
                break
    fixed_pct = 100 * n_fixed / max(n, 1)
    return {
        "n_failed_baseline": n,
        "n_fixed_via_repair": n_fixed,
        "fixed_pct_of_failed": f"{fixed_pct:.2f}%",
        "rounds_to_fix": dict(sorted(rounds_to_fix.items())),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs-dir", default="eval/runs")
    ap.add_argument("--out", default="eval/REPORT.md")
    args = ap.parse_args()
    runs = Path(args.runs_dir)
    jsonls = sorted(runs.glob("*.jsonl"))
    summary = {p.name: summarize_run(p) for p in jsonls}
    # Pretty markdown
    lines = ["# TopoGPT3 HumanEval evaluation", ""]
    lines += [
        "## Checkpoint reality",
        "",
        "- safetensors: `checkpoints_topogpt3/last/model.safetensors`  (149.7 MB, 447 tensors, 37.4M tensor elements)",
        "- model parameters (logical): 24,457,622 (~24.5M)",
        "- d_model=256, n_layers=6, n_heads=8, d_head=32, n_kv_heads=2 (GQA), vocab=50257 (gpt2 BPE), fp32",
        "- completed_tiers=[] in state.json (mixed training, not tier-bounded)",
        "- device: CPU (no CUDA available in this environment; torch installed as 2.12.0+cpu)",
        "- discrepancy: README says 24.5M, tensors say 37M; the 24.5M is the *logical* parameter count after complex/quaternion factorization, the 37M is the stored tensor count",
        "",
    ]
    lines.append("## Headline pass@k (164 problems unless noted)")
    lines.append("")
    names = list(summary.keys())
    keys = list(next(iter(summary.values())).keys())
    lines.append("| run | " + " | ".join(keys) + " |")
    lines.append("|" + "---|" * (len(keys) + 1))
    for n in names:
        row = summary[n]
        lines.append(f"| {n} | " + " | ".join(str(row[k]) for k in keys) + " |")
    lines.append("")
    # Repair
    repair_files = list(runs.glob("repair*.jsonl"))
    if repair_files and (runs / "greedy.jsonl").exists():
        lines.append("## Self-repair impact")
        lines.append("")
        for rf in repair_files:
            r = repair_summary(rf, runs / "greedy.jsonl")
            lines.append(f"**{rf.name}**")
            for k, v in r.items():
                lines.append(f"- {k}: {v}")
            lines.append("")
    # Error breakdown
    lines.append("## Error breakdown (first-try failures)")
    lines.append("")
    for n, row in summary.items():
        eb = row.get("first_try_error_breakdown", {})
        if eb:
            lines.append(f"**{n}**: " + ", ".join(f"{k}={v}" for k, v in eb.items()))
    lines.append("")
    Path(args.out).write_text("\n".join(lines))
    print("\n".join(lines))


if __name__ == "__main__":
    main()
