#!/usr/bin/env python3
"""Self-repair loop on top of a greedy JSONL.

Takes the failed problems from --input, builds a rejection-feedback prompt
that contains:
  - the original HumanEval prompt (signature + docstring)
  - the candidate the model wrote on its first attempt
  - the traceback from the hidden test
  - a "# fix:" cue

and re-prompts the model to rewrite the function. Runs N rounds. Each
problem's *best* outcome across rounds is recorded.

Output: a new JSONL with the same shape as harness.py.
"""
from __future__ import annotations

import argparse
import contextlib
import io
import json
import re
import time
import traceback
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Tuple

import torch
from safetensors import safe_open
from safetensors.torch import load_file

from topogpt3 import TopoGPT2Config, TopoGPT2, BPETokenizer  # noqa: F401


def _new_loader(ckpt_dir, ckpt_name):
    with safe_open(f"{ckpt_dir}/{ckpt_name}/model.safetensors", framework="pt", device="cpu") as h:
        kdim = h.get_tensor("layers.0.attn.k_proj.weight").shape[0]
    n_kv = kdim // 32
    cfg = TopoGPT2Config(SCALE="small", DEVICE="cpu", N_KV_HEADS=n_kv)
    tok = BPETokenizer("gpt2")
    cfg.VOCAB_SIZE = tok.vocab_size
    model = TopoGPT2(cfg).to("cpu").eval()
    sd = load_file(f"{ckpt_dir}/{ckpt_name}/model.safetensors", device="cpu")
    model.load_state_dict(sd, strict=False)
    return model, tok


def extract_candidate(prompt: str, completion: str) -> str:
    if completion.startswith(prompt):
        body = completion[len(prompt):]
    else:
        body = completion
    code = prompt + body
    lines = code.splitlines(keepends=True)
    out: List[str] = []
    started = False
    for i, line in enumerate(lines):
        out.append(line)
        if started and not line.startswith((" ", "\t")) and (
            line.lstrip().startswith("def ") or line.lstrip().startswith("class ")
            or line.lstrip().startswith("if __name__")
        ):
            out.pop()
            break
        if not started:
            if i >= 1 and line.lstrip() == '"""':
                started = True
            elif i >= 1 and line.startswith("def ") and i + 1 < len(lines):
                if not lines[i + 1].lstrip().startswith(('"""', "'", '"')):
                    started = True
    return "".join(out)


def run_test(problem: dict, candidate_src: str) -> Tuple[bool, str]:
    entry_point = problem["entry_point"]
    program = candidate_src + "\n" + problem["test"] + f"\ncheck({entry_point})\n"
    ns: Dict[str, object] = {}
    out, err = io.StringIO(), io.StringIO()
    try:
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            exec(compile(program, "<humaneval-repair>", "exec"), ns, ns)
        return True, "ok"
    except Exception as exc:
        tb = traceback.format_exc(limit=2)
        return False, f"{type(exc).__name__}: {exc}\n{tb}".strip()


def build_repair_prompt(prompt: str, candidate: str, err: str, entry_point: str) -> str:
    # Trim candidate to first ~25 lines to avoid prompt bloat
    cand_lines = candidate.splitlines()
    if len(cand_lines) > 30:
        candidate = "\n".join(cand_lines[:30]) + "\n    # ... (truncated)"
    err_short = (err or "").split("\n")[0][:200]
    return (
        f"{prompt}\n"
        f"# previous attempt:\n{candidate}\n"
        f"# the test failed with:\n# {err_short}\n"
        f"# fix and rewrite the body of {entry_point}:\n"
    )


@torch.no_grad()
def gen(model, tok, text: str, max_new_tokens: int, temperature: float, top_k: int,
        rep_penalty: float) -> Tuple[str, int, float]:
    ids = tok.encode(text)
    if not ids:
        return text, 0, 0.0
    x = torch.tensor([ids], dtype=torch.long, device="cpu")
    t0 = time.time()
    out = model.generate(
        x, max_new_tokens=max_new_tokens, temperature=temperature, top_k=top_k,
        repetition_penalty=rep_penalty,
    )
    dt = time.time() - t0
    return tok.decode(out[0].tolist()), int(out.shape[1] - len(ids)), dt


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True, help="greedy JSONL with task_id/passed/candidate/error")
    ap.add_argument("--problems-jsonl", required=True, help="HumanEval cache JSONL we re-emit here")
    ap.add_argument("--ckpt-dir", default="checkpoints_topogpt3")
    ap.add_argument("--ckpt-name", default="last")
    ap.add_argument("--out", required=True)
    ap.add_argument("--rounds", type=int, default=3)
    ap.add_argument("--max-new-tokens", type=int, default=384)
    ap.add_argument("--temperature", type=float, default=0.2)
    ap.add_argument("--top-k", type=int, default=40)
    ap.add_argument("--rep-penalty", type=float, default=1.1)
    ap.add_argument("--repair-only-failed", action="store_true", default=True)
    args = ap.parse_args()

    # Load HumanEval problems (re-fetch to get full prompt/test)
    from datasets import load_dataset
    ds = load_dataset("openai/openai_humaneval", cache_dir="data/humaneval")
    problems = {p["task_id"]: p for p in ds["test"]}
    print(f"[repair] {len(problems)} HumanEval problems loaded", flush=True)

    base = [json.loads(l) for l in open(args.input)]
    print(f"[repair] {len(base)} baseline records loaded", flush=True)

    # Group by task_id, take first sample
    by_tid: Dict[str, dict] = {}
    for r in base:
        by_tid.setdefault(r["task_id"], r)
    failed = {tid: r for tid, r in by_tid.items() if not r["passed"]}
    print(f"[repair] {len(failed)}/{len(by_tid)} problems failed baseline", flush=True)
    if not failed:
        print("[repair] nothing to repair")
        return

    print(f"[repair] loading model from {args.ckpt_dir}/{args.ckpt_name}", flush=True)
    model, tok = _new_loader(args.ckpt_dir, args.ckpt_name)
    print(f"[repair] model ready", flush=True)

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    n_fixed_round = [0] * (args.rounds + 1)  # round 0 = baseline
    n_total = 0
    t_start = time.time()
    with out_path.open("w") as f:
        for tid, baseline in failed.items():
            problem = problems[tid]
            prompt = problem["prompt"]
            current_cand = baseline["candidate"]
            current_err = baseline["error"] or ""
            current_passed = False
            best_round = 0
            round_records = []
            for r_idx in range(args.rounds):
                torch.manual_seed(42 + r_idx * 9973)
                if current_passed:
                    break
                repair_prompt = build_repair_prompt(prompt, current_cand, current_err, problem["entry_point"])
                full, new_tok, dt = gen(
                    model, tok, repair_prompt,
                    max_new_tokens=args.max_new_tokens,
                    temperature=args.temperature,
                    top_k=args.top_k,
                    rep_penalty=args.rep_penalty,
                )
                new_cand = extract_candidate(repair_prompt, full)
                passed, err = run_test(problem, new_cand)
                rec = {
                    "task_id": tid,
                    "round": r_idx + 1,
                    "passed": bool(passed),
                    "error": None if passed else err,
                    "new_tokens": new_tok,
                    "elapsed_s": dt,
                    "candidate_len": len(new_cand),
                    "candidate_first_line": new_cand.splitlines()[0] if new_cand else "",
                }
                f.write(json.dumps(rec) + "\n")
                f.flush()
                round_records.append(rec)
                if passed and not current_passed:
                    n_fixed_round[r_idx + 1] += 1
                    current_passed = True
                    best_round = r_idx + 1
                current_cand = new_cand
                current_err = err
            n_total += 1
            if (n_total % 5) == 0 or n_total <= 3:
                elapsed = time.time() - t_start
                rate = n_total / max(elapsed, 1e-3)
                fixed_total = sum(n_fixed_round[1:])
                print(
                    f"[repair] {n_total}/{len(failed)} fixed_total={fixed_total} "
                    f"({100*fixed_total/n_total:.1f}%) rate={rate:.2f} prob/s "
                    f"last={tid} best_round={best_round}",
                    flush=True,
                )
    print(
        f"[repair] DONE. fixed_by_round={n_fixed_round[1:]} total_problems_attempted={n_total} "
        f"wall={time.time()-t_start:.1f}s",
        flush=True,
    )


if __name__ == "__main__":
    main()
