#!/usr/bin/env python3
"""Aggregate HumanEval result JSONL files into a summary table.

Reads one or more .jsonl files produced by harness.py and computes:
  - pass@1, pass@k (using the unbiased estimator from the HumanEval paper
    when k > 1)
  - mean latency, mean generation length, tok/s
  - per-error classification
"""
from __future__ import annotations

import argparse
import json
import math
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Dict, List


def pass_at_k(n: int, c: int, k: int) -> float:
    """Unbiased estimator from the HumanEval paper.

    pass@k = 1 - C(n-c, k) / C(n, k)   if n - c >= k else 1.0
    n = total samples, c = correct samples, k = target
    """
    if n - c < k:
        return 1.0
    return 1.0 - math.prod(1.0 - k / (n - i) for i in range(c)) if c > 0 else 0.0


def classify_error(msg: str, candidate_src: str) -> str:
    """Heuristic single-label error classifier."""
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
    if "valueerror" in m or "keyerror" in m or "attributeerror" in m:
        return "edge_case"
    if "assertionerror" in m:
        return "wrong_output"
    if "zerodivisionerror" in m:
        return "edge_case"
    if "runner_crash" in m:
        return "runner_crash"
    return "other"


def load_jsonl(path: Path) -> List[dict]:
    with path.open() as f:
        return [json.loads(line) for line in f if line.strip()]


def summarize(paths: List[Path]) -> dict:
    runs = {p.name: load_jsonl(p) for p in paths}
    summary: Dict[str, dict] = {}
    for name, recs in runs.items():
        by_problem = defaultdict(list)
        for r in recs:
            by_problem[r["task_id"]].append(r)
        n_problems = len(by_problem)
        n_samples_per = max(len(v) for v in by_problem.values()) if by_problem else 0
        # pass@1
        pass1 = sum(1 for v in by_problem.values() if v[0]["passed"])
        # pass@k
        k = n_samples_per
        passk_each = []
        for tid, samples in by_problem.items():
            n = len(samples)
            c = sum(1 for s in samples if s["passed"])
            passk_each.append(pass_at_k(n, c, k) if k > 1 else float(c > 0))
        passk = sum(passk_each) / max(len(passk_each), 1)
        # latency
        elapsed = [r["elapsed_s"] for r in recs if r["elapsed_s"] > 0]
        toks = [r["new_tokens"] for r in recs]
        throughput = [r["new_tokens"] / max(r["elapsed_s"], 1e-3) for r in recs if r["elapsed_s"] > 0]
        # error classes (first-try failures)
        err = Counter()
        for tid, samples in by_problem.items():
            s0 = samples[0]
            if not s0["passed"]:
                err[classify_error(s0.get("error") or "", s0.get("candidate") or "")] += 1
        summary[name] = {
            "n_problems": n_problems,
            "n_samples_per_problem": n_samples_per,
            "pass@1": f"{pass1}/{n_problems} = {100*pass1/n_problems:.2f}%",
            f"pass@{k}": f"{sum(passk_each):.2f}/{n_problems} = {100*passk:.2f}%",
            "mean_latency_s": f"{sum(elapsed)/max(len(elapsed),1):.2f}",
            "mean_new_tokens": f"{sum(toks)/max(len(toks),1):.1f}",
            "mean_tok_per_s": f"{sum(throughput)/max(len(throughput),1):.1f}",
            "first_try_error_breakdown": dict(err.most_common()),
        }
    return summary


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("jsonls", nargs="+", help="harness.py output JSONL files")
    ap.add_argument("--md", action="store_true", help="print markdown table")
    args = ap.parse_args()
    summary = summarize([Path(p) for p in args.jsonls])
    if args.md:
        names = list(summary.keys())
        keys = list(next(iter(summary.values())).keys())
        print("| run | " + " | ".join(keys) + " |")
        print("|" + "---|" * (len(keys) + 1))
        for name in names:
            row = summary[name]
            print(f"| {name} | " + " | ".join(str(row[k]) for k in keys) + " |")
    else:
        for name, s in summary.items():
            print(f"\n=== {name} ===")
            for k, v in s.items():
                print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
