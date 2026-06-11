#!/usr/bin/env python3
"""Smoke test: load the TopoGPT3 checkpoint and produce a small completion.

Used as the first gate: if this fails we abort HumanEval.
"""
import time
import torch
from topogpt3 import (
    InferencePipeline,
    InferenceSettings,
    HRMInferencePipeline,
    HRMInferenceSettings,
    RecursiveReasoningConfig,
)


def run_standard():
    print("\n=== Standard sampler ===")
    settings = InferenceSettings(
        checkpoint_dir="checkpoints_topogpt3",
        checkpoint_name="last",
        prompt="def fibonacci(n):\n    ",
        max_new_tokens=120,
        temperature=0.2,
        top_k=40,
        repetition_penalty=1.1,
        log_level="WARNING",
    )
    t = time.time()
    report = InferencePipeline(settings).execute()
    dt = time.time() - t
    print(f"  new_tokens={report.new_tokens}  elapsed={dt:.2f}s  tok/s={report.new_tokens/dt:.1f}")
    print(f"  ---\n{report.output}\n---")


def run_hrm():
    print("\n=== HRM sampler ===")
    settings = HRMInferenceSettings(
        checkpoint_dir="checkpoints_topogpt3",
        checkpoint_name="last",
        prompt="def fibonacci(n):\n    ",
        max_new_tokens=120,
        temperature=0.2,
        top_k=40,
        repetition_penalty=1.1,
        reasoning=RecursiveReasoningConfig(
            max_high_level_iters=2,
            max_low_level_iters=3,
            low_level_window=2,
            high_level_window=4,
            high_level_persist_tokens=4,
        ),
        log_level="WARNING",
    )
    t = time.time()
    report = HRMInferencePipeline(settings).execute()
    dt = time.time() - t
    print(f"  new_tokens={report.new_tokens}  elapsed={dt:.2f}s  tok/s={report.new_tokens/dt:.1f}")
    rs = report.reasoning_summary
    print(f"  reasoning: h_iters_total={rs.total_high_level_iters} l_iters_total={rs.total_low_level_iters} convergences={rs.high_level_convergences} cache_reuses={rs.h_cache_reuses}")
    print(f"  ---\n{report.output}\n---")


if __name__ == "__main__":
    run_standard()
    run_hrm()
