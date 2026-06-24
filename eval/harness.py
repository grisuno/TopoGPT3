#!/usr/bin/env python3
"""Harness for evaluating TopoGPT3 on HumanEval (164 problems).

Faithful to the official HumanEval protocol: for each problem we feed the
model the function signature and docstring, let it produce a completion,
extract the candidate function (everything from `def` up to a sentinel),
and run the hidden test against it. We do NOT use `entry_point` from the
dataset because the prompt we feed the model already contains it.

Two sampler modes are supported:
  - "standard" -> topogpt3.InferencePipeline
  - "hrm"      -> topogpt3.HRMInferencePipeline

Results are written to JSONL so multiple sampler configurations can share
a single HumanEval cache and be compared later.
"""
from __future__ import annotations

import argparse
import contextlib
import io
import json
import os
import re
import signal
import subprocess
import sys
import time
import traceback
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Callable, Dict, List, Optional, Tuple

import torch
from torch import tensor, long as torch_long  # noqa: F401  (used dynamically)

from topogpt3 import (  # noqa: F401
    InferencePipeline,
    InferenceSettings,
    HRMInferencePipeline,
    HRMInferenceSettings,
    RecursiveReasoningConfig,
    TopoGPT2Config,
    TopoGPT2,
    BPETokenizer,
    set_seed,
)
from eval.samplers import make_sampler, list_samplers  # noqa: F401
from safetensors.torch import load_file


# ---------------------------------------------------------------------------
# HumanEval loader (uses HuggingFace datasets, falls back to a vendored copy)
# ---------------------------------------------------------------------------

HF_HE_REPO = "openai/openai_humaneval"


def load_humaneval(cache_dir: str = "data/humaneval"):
    from datasets import load_dataset
    os.makedirs(cache_dir, exist_ok=True)
    ds = load_dataset(HF_HE_REPO, cache_dir=cache_dir)
    return list(ds["test"])


# ---------------------------------------------------------------------------
# Prompt construction
# ---------------------------------------------------------------------------

# HumanEval prompts are the canonical function header. We feed them verbatim
# (with the docstring already inside) and let the model write the body. The
# model occasionally keeps emitting more functions; we cut at the first
# top-level `def ` that is not nested inside the function body.

def build_prompt(problem: dict) -> str:
    """Return the exact prompt text fed to the model.

    HumanEval's `prompt` field already contains the function signature and
    docstring, with the body to be completed starting on the next line.
    """
    return problem["prompt"]


# ---------------------------------------------------------------------------
# Candidate extraction
# ---------------------------------------------------------------------------

# We extract everything from the start of the model's completion up to a
# heuristic end-of-function marker, and then prepend the original prompt.
# HumanEval tests are designed to import the function defined in `prompt`,
# so the candidate must start with the same signature and define the entry
# point function (whose name is `entry_point`).

_END_OF_FUNCTION_RE = re.compile(
    r"\n(?=def\s+\w+\s*\(|class\s+\w+\s*[:\(]|\nif\s+__name__\s*==\s*['\"]__main__['\"])",
    re.MULTILINE,
)


def extract_candidate(prompt: str, completion: str) -> str:
    """Combine prompt + completion into a single Python source string.

    The completion may itself start with whitespace/indentation that
    belongs inside the function body. We strip leading blank lines and
    then concatenate; we also stop at the first top-level `def ` or
    `class ` to avoid the model continuing with extra functions.

    Robustness fixes:
      - Strip the special <|endoftext|> (GPT-2 EOT) token that the model
        emits at the end of every generation. Leaving it in the candidate
        produces a SyntaxError and zeroes the pass rate.
      - Drop any training-format delimiters (### Response, <|assistant|>,
        <|user|>) that leak from the instruction-tuning corpus.
      - Cut at the first top-level def/class/__main__ guard after the
        function body has started.
    """
    # 1. Remove the EOS sentinel and any text after it.
    completion = re.split(r"<\|endoftext\|>", completion, maxsplit=1)[0]

    # 2. Drop common instruction-format artifacts that contaminate code
    #    generations from the mixed corpus the model was trained on.
    for artifact in ("### Response", "### Instruction", "### Input",
                     "<|user|>", "<|assistant|>", "<|system|>"):
        completion = completion.split(artifact)[0]

    # 3. Separate the body from the prompt. If the decoded completion does
    #    not start with the prompt (e.g. tokenizer whitespace drift), keep
    #    only the generated suffix and re-attach the canonical prompt.
    if completion.startswith(prompt):
        body = completion[len(prompt):]
    else:
        # Sometimes the model repeats the signature; avoid double prompts.
        body = completion
        if prompt in completion:
            body = completion[completion.index(prompt) + len(prompt):]

    # 4. Build the full source and cut after the entry-point function.
    code = prompt + body
    match = _END_OF_FUNCTION_RE.search(code[len(prompt):])
    if match:
        code = code[:len(prompt) + match.start()]

    return code.rstrip() + "\n"


# ---------------------------------------------------------------------------
# Test execution (HumanEval canonical protocol)
# ---------------------------------------------------------------------------

def run_one_test(problem: dict, candidate_src: str, timeout: float) -> Tuple[bool, str, str, str, str]:
    """Execute the candidate against the hidden test.

    Returns (passed, message, stdout, stderr, traceback). We follow HumanEval's
    `evaluate` function: build namespace, exec the candidate, exec the test,
    expect `check(candidate) == None`.
    """
    entry_point = problem["entry_point"]
    test_code = problem["test"] + f"\ncheck({entry_point})\n"
    program = candidate_src + "\n" + test_code
    ns: Dict[str, object] = {}
    stdout, stderr = io.StringIO(), io.StringIO()
    try:
        with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
            exec(compile(program, "<humaneval-eval>", "exec"), ns, ns)
        return True, "ok", stdout.getvalue(), stderr.getvalue(), ""
    except Exception as exc:
        full_tb = traceback.format_exc()
        msg = f"{type(exc).__name__}: {exc}"
        return False, msg, stdout.getvalue(), stderr.getvalue(), full_tb


def run_one_test_sandboxed(
    problem: dict, candidate_src: str, timeout: float,
    sandbox_cfg=None,
) -> Tuple[bool, str, str, str, str]:
    """Sandboxed variant of `run_one_test`. Runs the candidate in a
    subprocess with stripped builtins, AST pre-check, and OS-enforced
    timeout. Drop-in replacement: same 5-tuple return.

    Enable by passing `--sandbox` to `harness.py` (not yet wired) or
    by calling this function directly from your own evaluation script.
    """
    from eval.sandbox import safe_exec, SandboxConfig
    cfg = sandbox_cfg or SandboxConfig(timeout=timeout)
    entry_point = problem["entry_point"]
    test_code = problem["test"] + f"\ncheck({entry_point})\n"
    program = candidate_src + "\n" + test_code
    return safe_exec(program, cfg)


# ---------------------------------------------------------------------------
# Sampler wrappers (return raw completion text only — no banners)
# ---------------------------------------------------------------------------

def make_sampler(mode: str, settings_kwargs: dict):  # type: ignore[no-untyped-def]
    """Backwards-compatible shim. The real implementation lives in
    `eval.samplers` as a decorator-based registry. We re-export here
    so existing imports of `from eval.harness import make_sampler`
    keep working. New code should import from `eval.samplers`."""
    from eval.samplers import build_sampler
    return build_sampler(mode, settings_kwargs)


def completion_for_problem(sampler, prompt: str) -> Tuple[str, dict]:
    """Run a single completion and return (raw_output_text, metrics_dict)."""
    # We rebuild the sampler pipeline per problem so that each call is
    # independent (KV cache isolation). The pipeline object is light: it
    # only orchestrates; the heavy model+tokenizer is built once via a
    # shared loader.
    raise NotImplementedError("Use ModelLoader below to share the model.")


# ---------------------------------------------------------------------------
# Shared model + tokenizer (avoid reloading 150MB on every call)
# ---------------------------------------------------------------------------

class ModelLoader:
    """Build the model and tokenizer once, run many generations."""

    def __init__(self, ckpt_dir: str, ckpt_name: str = "last", device: str = None):
        from safetensors import safe_open
        if device is None:
            device = "cuda" if torch.cuda.is_available() else "cpu"
        self.device = device
        # 1. probe kv heads
        with safe_open(f"{ckpt_dir}/{ckpt_name}/model.safetensors", framework="pt", device="cpu") as h:
            t = h.get_tensor("layers.0.attn.k_proj.weight")
            k_dim = int(t.shape[0])
        d_head = 32  # small preset
        n_kv = k_dim // d_head
        # 2. build aligned config
        cfg = TopoGPT2Config(SCALE="small", DEVICE=device, N_KV_HEADS=n_kv)
        # 3. tokenizer
        self.tok = BPETokenizer("gpt2")
        cfg.VOCAB_SIZE = self.tok.vocab_size
        # 4. model + weights
        self.model = TopoGPT2(cfg).to(device).eval()
        sd = load_file(f"{ckpt_dir}/{ckpt_name}/model.safetensors", device=device)
        self.model.load_state_dict(sd, strict=False)
        # 5. seed
        set_seed(42, device)
        n_params = sum(p.numel() for p in self.model.parameters())
        print(f"[loader] model ready: {n_params:,} params, n_kv_heads={n_kv}, device={device}", flush=True)

    @torch.no_grad()
    def generate(self, prompt: str, max_new_tokens: int, temperature: float,
                 top_k: int, repetition_penalty: float) -> Tuple[str, dict]:
        ids = self.tok.encode(prompt)
        if not ids:
            return prompt, {"new_tokens": 0, "elapsed_s": 0.0}
        x = torch.tensor([ids], dtype=torch.long, device=self.device)
        t0 = time.time()
        out = self.model.generate(
            x,
            max_new_tokens=max_new_tokens,
            temperature=temperature,
            top_k=top_k,
            repetition_penalty=repetition_penalty,
        )
        dt = time.time() - t0
        text = self.tok.decode(out[0].tolist())
        return text, {
            "new_tokens": int(out.shape[1] - len(ids)),
            "elapsed_s": dt,
        }


# ---------------------------------------------------------------------------
# One problem, one pass
# ---------------------------------------------------------------------------

def evaluate_problem(problem: dict, loader: ModelLoader, args, sample_idx: int = 0) -> dict:
    prompt = build_prompt(problem)
    # Vary seed per sample so pass@10/20 actually samples diverse outputs.
    # Keep temperature+top_k from args; the loader reseeds once at init.
    if sample_idx > 0:
        torch.manual_seed(42 + sample_idx * 9973)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(42 + sample_idx * 9973)
    raw, m = loader.generate(
        prompt,
        max_new_tokens=args.max_new_tokens,
        temperature=args.temperature,
        top_k=args.top_k,
        repetition_penalty=args.repetition_penalty,
    )
    candidate = extract_candidate(prompt, raw)
    passed, msg, stdout, stderr, full_tb = run_one_test(problem, candidate, timeout=20.0)
    error_type = "ok" if passed else msg.split(":", 1)[0]
    return {
        "task_id": problem["task_id"],
        "sample_idx": sample_idx,
        "entry_point": problem["entry_point"],
        "passed": bool(passed),
        "error_type": error_type,
        "error": None if passed else msg,
        "traceback": full_tb,
        "stdout": stdout,
        "stderr": stderr,
        "prompt": prompt,
        "test_code": problem["test"] + f"\ncheck({problem['entry_point']})\n",
        "candidate_first_line": candidate.splitlines()[0] if candidate else "",
        "candidate_len": len(candidate),
        "new_tokens": m["new_tokens"],
        "elapsed_s": m["elapsed_s"],
        "completion": raw,
        "candidate": candidate,
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ckpt-dir", default="checkpoints_topogpt3")
    ap.add_argument("--ckpt-name", default="last")
    ap.add_argument("--cache", default="data/humaneval")
    ap.add_argument("--out", required=True, help="output JSONL path")
    ap.add_argument("--limit", type=int, default=0, help="0 = all 164")
    ap.add_argument("--n-samples", type=int, default=1, help="k for pass@k")
    ap.add_argument("--temperature", type=float, default=0.0)
    ap.add_argument("--top-k", type=int, default=0)
    ap.add_argument("--repetition-penalty", type=float, default=1.0)
    ap.add_argument("--max-new-tokens", type=int, default=512)
    ap.add_argument("--device", default=None)
    ap.add_argument("--mode", choices=["standard", "hrm"], default="standard")
    ap.add_argument("--repair-from", default=None, help="JSONL of failed problems to retry")
    ap.add_argument("--repair-rounds", type=int, default=0)
    args = ap.parse_args()

    print(f"[eval] loading HumanEval from {HF_HE_REPO} (cache {args.cache})", flush=True)
    problems = load_humaneval(args.cache)
    if args.limit > 0:
        problems = problems[: args.limit]
    print(f"[eval] {len(problems)} problems", flush=True)

    print(f"[eval] loading model from {args.ckpt_dir}/{args.ckpt_name} (mode={args.mode})", flush=True)
    loader = ModelLoader(args.ckpt_dir, args.ckpt_name, args.device)

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    n_total = 0
    n_pass = 0
    t_start = time.time()
    with out_path.open("w") as f:
        for p_idx, problem in enumerate(problems):
            for s_idx in range(args.n_samples):
                t0 = time.time()
                try:
                    rec = evaluate_problem(problem, loader, args, sample_idx=s_idx)
                except Exception as exc:
                    rec = {
                        "task_id": problem["task_id"],
                        "sample_idx": s_idx,
                        "entry_point": problem["entry_point"],
                        "passed": False,
                        "error_type": type(exc).__name__,
                        "error": f"runner_crash: {type(exc).__name__}: {exc}",
                        "traceback": traceback.format_exc(),
                        "stdout": "",
                        "stderr": "",
                        "prompt": build_prompt(problem),
                        "test_code": problem["test"] + f"\ncheck({problem['entry_point']})\n",
                        "candidate_first_line": "",
                        "candidate_len": 0,
                        "new_tokens": 0,
                        "elapsed_s": time.time() - t0,
                        "completion": "",
                        "candidate": "",
                    }
                f.write(json.dumps(rec) + "\n")
                f.flush()
                n_total += 1
                if rec["passed"]:
                    n_pass += 1
                if (n_total % 10) == 0 or n_total <= 5:
                    elapsed = time.time() - t_start
                    rate = n_total / max(elapsed, 1e-3)
                    print(
                        f"[eval] {n_total:3d}/{len(problems)*args.n_samples} "
                        f"pass={n_pass} ({100*n_pass/n_total:.1f}%) "
                        f"rate={rate:.2f} prob/s "
                        f"last={problem['task_id']} passed={rec['passed']} "
                        f"({rec['elapsed_s']:.1f}s, {rec['new_tokens']} tok)",
                        flush=True,
                    )
    print(f"[eval] DONE. pass@1 = {n_pass}/{n_total} = {100*n_pass/n_total:.2f}%, "
          f"total time = {time.time() - t_start:.1f}s", flush=True)


if __name__ == "__main__":
    main()
