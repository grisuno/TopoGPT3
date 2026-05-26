#!/usr/bin/env python3
"""Drop-in entry point that demonstrates how to use the topogpt3 package.

This file lives outside the package on purpose. Copy it (or its sections)
into your own project after running ``pip install topogpt3``. Three usage
patterns are shown:

1. ``run_inference`` calls the standard autoregressive sampler.
2. ``run_inference_hrm`` calls the hierarchical recursive reasoning
   sampler that reuses the same checkpoint with no extra trained
   parameters.
3. ``run_training`` launches the full curriculum trainer.

The script's main() exposes them through a tiny ``--mode`` CLI so the
file is runnable as-is for a quick smoke test once a checkpoint exists.
"""
from __future__ import annotations

import argparse
import sys
from typing import Optional, Sequence

import torch

from topogpt3 import (
    HRMInferencePipeline,
    HRMInferenceSettings,
    InferencePipeline,
    InferenceSettings,
    RecursiveReasoningConfig,
    TopoGPT3Config,
    TopoGPT3Trainer,
    __version__,
)


DEFAULT_CHECKPOINT_DIR = "checkpoints_topogpt3"
DEFAULT_CHECKPOINT_SLOT = "last"
DEFAULT_PROMPT = "def fibonacci(n):\n"
DEFAULT_MAX_NEW_TOKENS = 200
DEFAULT_TEMPERATURE = 0.3
DEFAULT_TOP_K = 50
DEFAULT_REPETITION_PENALTY = 1.1


def run_inference(
    prompt: str = DEFAULT_PROMPT,
    checkpoint_dir: str = DEFAULT_CHECKPOINT_DIR,
    checkpoint_name: str = DEFAULT_CHECKPOINT_SLOT,
    max_new_tokens: int = DEFAULT_MAX_NEW_TOKENS,
    temperature: float = DEFAULT_TEMPERATURE,
    top_k: int = DEFAULT_TOP_K,
    repetition_penalty: float = DEFAULT_REPETITION_PENALTY,
    device: Optional[str] = None,
) -> str:
    """Run the standard sampler and return the generated completion text."""
    settings = InferenceSettings(
        prompt=prompt,
        checkpoint_dir=checkpoint_dir,
        checkpoint_name=checkpoint_name,
        max_new_tokens=max_new_tokens,
        temperature=temperature,
        top_k=top_k,
        repetition_penalty=repetition_penalty,
        device=device or ("cuda" if torch.cuda.is_available() else "cpu"),
    )
    report = InferencePipeline(settings).execute()
    return report.output


def run_inference_hrm(
    prompt: str = DEFAULT_PROMPT,
    checkpoint_dir: str = DEFAULT_CHECKPOINT_DIR,
    checkpoint_name: str = DEFAULT_CHECKPOINT_SLOT,
    max_new_tokens: int = DEFAULT_MAX_NEW_TOKENS,
    temperature: float = DEFAULT_TEMPERATURE,
    top_k: int = DEFAULT_TOP_K,
    repetition_penalty: float = DEFAULT_REPETITION_PENALTY,
    high_level_iters: int = 2,
    low_level_iters: int = 3,
    low_level_window: int = 2,
    device: Optional[str] = None,
) -> str:
    """Run the hierarchical recursive sampler and return the completion."""
    reasoning = RecursiveReasoningConfig(
        max_high_level_iters=high_level_iters,
        max_low_level_iters=low_level_iters,
        low_level_window=low_level_window,
    )
    settings = HRMInferenceSettings(
        prompt=prompt,
        checkpoint_dir=checkpoint_dir,
        checkpoint_name=checkpoint_name,
        max_new_tokens=max_new_tokens,
        temperature=temperature,
        top_k=top_k,
        repetition_penalty=repetition_penalty,
        reasoning=reasoning,
        device=device or ("cuda" if torch.cuda.is_available() else "cpu"),
    )
    report = HRMInferencePipeline(settings).execute()
    return report.output


def run_training(
    scale: str = "small",
    start_tier: Optional[int] = None,
    device: Optional[str] = None,
    prepare_data: bool = False,
) -> None:
    """Run the full TopoGPT3 curriculum trainer."""
    config = TopoGPT3Config(SCALE=scale)
    if device is not None:
        config.DEVICE = device
    trainer = TopoGPT3Trainer(config, start_tier=start_tier)
    if prepare_data:
        trainer.prepare_all()
    trainer.run()


def _build_parser() -> argparse.ArgumentParser:
    """Build the top-level CLI for this entry point script."""
    parser = argparse.ArgumentParser(
        description=(
            f"topogpt3 example entry point (package version {__version__}). "
            "Use --mode to pick infer / infer-hrm / train."
        ),
    )
    parser.add_argument(
        "--mode", type=str, default="infer",
        choices=["infer", "infer-hrm", "train"],
        help="Which pipeline to run.",
    )
    parser.add_argument("--prompt", type=str, default=DEFAULT_PROMPT)
    parser.add_argument("--ckpt-dir", type=str, default=DEFAULT_CHECKPOINT_DIR)
    parser.add_argument("--ckpt-name", type=str, default=DEFAULT_CHECKPOINT_SLOT)
    parser.add_argument("--max-new", type=int, default=DEFAULT_MAX_NEW_TOKENS)
    parser.add_argument("--temp", type=float, default=DEFAULT_TEMPERATURE)
    parser.add_argument("--top-k", type=int, default=DEFAULT_TOP_K)
    parser.add_argument(
        "--rep-penalty", type=float, default=DEFAULT_REPETITION_PENALTY,
    )
    parser.add_argument("--device", type=str, default=None)
    parser.add_argument(
        "--scale", type=str, default="small",
        choices=["micro", "small", "medium", "gpt2"],
    )
    parser.add_argument("--start-tier", type=int, default=None)
    parser.add_argument(
        "--prepare-data", action="store_true",
        help="Train mode only: download and tokenize datasets first.",
    )
    parser.add_argument("--hrm-h-iters", type=int, default=2)
    parser.add_argument("--hrm-l-iters", type=int, default=3)
    parser.add_argument("--hrm-l-window", type=int, default=2)
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    """Entry point invoked when the file is executed as a script."""
    args = _build_parser().parse_args(argv)

    if args.mode == "infer":
        run_inference(
            prompt=args.prompt,
            checkpoint_dir=args.ckpt_dir,
            checkpoint_name=args.ckpt_name,
            max_new_tokens=args.max_new,
            temperature=args.temp,
            top_k=args.top_k,
            repetition_penalty=args.rep_penalty,
            device=args.device,
        )
        return 0

    if args.mode == "infer-hrm":
        run_inference_hrm(
            prompt=args.prompt,
            checkpoint_dir=args.ckpt_dir,
            checkpoint_name=args.ckpt_name,
            max_new_tokens=args.max_new,
            temperature=args.temp,
            top_k=args.top_k,
            repetition_penalty=args.rep_penalty,
            high_level_iters=args.hrm_h_iters,
            low_level_iters=args.hrm_l_iters,
            low_level_window=args.hrm_l_window,
            device=args.device,
        )
        return 0

    if args.mode == "train":
        run_training(
            scale=args.scale,
            start_tier=args.start_tier,
            device=args.device,
            prepare_data=args.prepare_data,
        )
        return 0

    raise ValueError(f"Unknown mode: {args.mode}")


if __name__ == "__main__":
    sys.exit(main())
