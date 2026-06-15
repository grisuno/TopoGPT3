#!/usr/bin/env python3
"""Analyze a HumanEval JSONL produced by harness.py.

For each failed problem the report shows:
  - the prompt fed to the model
  - the generated candidate after extraction
  - the hidden test that failed
  - the captured stdout/stderr and traceback

This makes it easy to see *how* and *why* a candidate failed without
re-running the harness.

Usage:
    python eval/analyze_results.py eval/runs/run.jsonl
    python eval/analyze_results.py eval/runs/run.jsonl --summary
    python eval/analyze_results.py eval/runs/run.jsonl --task-id HumanEval/0
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path


def load_records(path: str):
    with Path(path).open("r", encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def summarize(records):
    total = len(records)
    passed = sum(1 for r in records if r.get("passed"))
    error_types = Counter(r.get("error_type", "unknown") for r in records if not r.get("passed"))

    print(f"Total problems : {total}")
    print(f"Passed         : {passed} ({100 * passed / total:.1f}%)")
    print(f"Failed         : {total - passed}")
    print("\nError breakdown:")
    for etype, count in error_types.most_common():
        print(f"  {count:3d}  {etype}")


def show_failures(records, task_id: str | None = None):
    for rec in records:
        if rec.get("passed"):
            continue
        if task_id and rec.get("task_id") != task_id:
            continue
        tid = rec.get("task_id", "unknown")
        entry = rec.get("entry_point", "unknown")
        print("=" * 80)
        print(f"TASK: {tid}  ENTRY_POINT: {entry}  ERROR_TYPE: {rec.get('error_type', 'unknown')}")
        print("-" * 80)
        print("PROMPT:")
        print(rec.get("prompt", "<missing>"))
        print("-" * 80)
        print("CANDIDATE:")
        print(rec.get("candidate", "<missing>"))
        print("-" * 80)
        print("TEST CODE:")
        print(rec.get("test_code", "<missing>"))
        if rec.get("stdout"):
            print("-" * 80)
            print("STDOUT:")
            print(rec["stdout"])
        if rec.get("stderr"):
            print("-" * 80)
            print("STDERR:")
            print(rec["stderr"])
        if rec.get("error"):
            print("-" * 80)
            print("ERROR MESSAGE:")
            print(rec["error"])
        if rec.get("traceback"):
            print("-" * 80)
            print("TRACEBACK:")
            print(rec["traceback"])
        print()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("jsonl", help="path to harness output JSONL")
    ap.add_argument("--summary", action="store_true", help="print aggregate stats only")
    ap.add_argument("--task-id", default=None, help="show only this task_id")
    args = ap.parse_args()

    records = load_records(args.jsonl)
    summarize(records)
    if not args.summary:
        print()
        show_failures(records, task_id=args.task_id)


if __name__ == "__main__":
    main()
