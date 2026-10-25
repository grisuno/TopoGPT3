"""Generic task eval: JSONL cases + safe verifiers.

Case schema (one JSON object per line):
    {"id": "...",
     "prompt": "user text",
     "profile": "topoexploit-apt-chain",     # optional, forwarded as model/profile
     "verifier": {
         "type": "apt_chain|tool_call|json|regex|exact|contains|python_ast",
         ...type-specific fields...
     }}

Verifiers are deterministic and never execute model output; ``python_ast``
only parses. Execution-based scoring belongs to the caller's sandbox.
"""

from __future__ import annotations

import argparse
import ast
import json
import re
import sys
import time
from collections.abc import Callable, Iterable
from pathlib import Path
from typing import Any

from topogpt3.chat import parse_tool_calls
from topogpt3.fallback import resolve_profile, validate_tool_call

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


def _extract_code(text: str) -> str:
    blocks = re.findall(r"```(?:python|py)?\s*(.*?)```", text, re.DOTALL)
    return blocks[0] if blocks else text


def _extract_json(text: str) -> Any | None:
    stripped = text.strip()
    if stripped.startswith("```"):
        stripped = re.sub(r"^```[a-zA-Z]*\s*", "", stripped)
        stripped = re.sub(r"\s*```$", "", stripped)
    try:
        return json.loads(stripped)
    except json.JSONDecodeError:
        return None


def verify_tool_call(case: dict[str, Any], completion: str) -> tuple[bool, str]:
    spec = case.get("verifier", {})
    expected = spec.get("tool")
    if expected is None:
        expected = case.get("expected_tool")
    allowed = {expected} if expected else None
    calls = parse_tool_calls(completion)
    if not calls:
        return False, "no tool call emitted"
    call = calls[0]
    ok, reason = validate_tool_call(call, allowed)
    if not ok:
        return False, reason
    args = call.get("arguments", {})
    want_target = spec.get("target")
    if want_target and str(args.get("target", "")).strip() != str(want_target).strip():
        return False, f"target mismatch: {args.get('target')!r} != {want_target!r}"
    want_chain = spec.get("chain")
    if (
        want_chain
        and str(args.get("chain", "apt_chain")).strip() != str(want_chain).strip()
    ):
        return False, f"chain mismatch: {args.get('chain')!r} != {want_chain!r}"
    if bool(spec.get("dry_run")) and not bool(args.get("dry_run", True)):
        return False, "expected dry_run=true"
    return True, "ok"


def verify_json(case: dict[str, Any], completion: str) -> tuple[bool, str]:
    value = _extract_json(completion)
    if value is None:
        return False, "no valid JSON"
    required = case.get("verifier", {}).get("required") or []
    if isinstance(value, dict):
        for key in required:
            if key not in value:
                return False, f"missing key: {key}"
    return True, "ok"


def verify_regex(case: dict[str, Any], completion: str) -> tuple[bool, str]:
    pattern = case.get("verifier", {}).get("pattern", "")
    if not re.fullmatch(pattern, completion.strip(), re.DOTALL):
        return False, "regex mismatch"
    return True, "ok"


def verify_exact(case: dict[str, Any], completion: str) -> tuple[bool, str]:
    want = str(case.get("verifier", {}).get("value", ""))
    got = completion.strip()
    if got != want:
        return False, f"exact mismatch: {got!r}"
    return True, "ok"


def verify_contains(case: dict[str, Any], completion: str) -> tuple[bool, str]:
    items = case.get("verifier", {}).get("value") or []
    lowered = completion.lower()
    for item in items if isinstance(items, list) else [items]:
        if str(item).lower() not in lowered:
            return False, f"missing: {item!r}"
    return True, "ok"


def verify_python_ast(case: dict[str, Any], completion: str) -> tuple[bool, str]:
    try:
        ast.parse(_extract_code(completion))
    except SyntaxError as exc:
        return False, f"syntax error: {exc}"
    return True, "ok"


VERIFIERS = {
    "apt_chain": verify_tool_call,
    "tool_call": verify_tool_call,
    "json": verify_json,
    "regex": verify_regex,
    "exact": verify_exact,
    "contains": verify_contains,
    "python_ast": verify_python_ast,
}


def load_cases(path: str | Path) -> list[dict[str, Any]]:
    cases: list[dict[str, Any]] = []
    with open(path, "r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line and not line.startswith("#"):
                cases.append(json.loads(line))
    if not cases:
        raise ValueError(f"no cases in {path}")
    return cases


def evaluate_case(
    case: dict[str, Any], generate_fn: Callable[[str, str], str]
) -> dict[str, Any]:
    profile = resolve_profile(case.get("profile", case.get("model")))
    verifier_name = case.get("verifier", {}).get("type", "general")
    verifier = VERIFIERS.get(verifier_name)
    if verifier is None:
        verifier = verify_contains
    t0 = time.monotonic()
    completion = generate_fn(
        case.get("prompt", ""), case.get("profile", case.get("model", ""))
    )
    try:
        ok, reason = verifier(case, completion)
    except Exception as exc:  # noqa: BLE001 - verifier bugs must not kill the run
        ok, reason = False, f"verifier error: {exc}"
    return {
        "id": case.get("id", ""),
        "task": case.get("task", ""),
        "profile": profile.name,
        "verifier": verifier_name,
        "prompt": case.get("prompt", ""),
        "completion": completion,
        "ok": bool(ok),
        "reason": reason,
        "duration_s": time.monotonic() - t0,
    }


def evaluate_cases(
    cases: Iterable[dict[str, Any]],
    generate_fn: Callable[[str, str], str],
    limit: int | None = None,
) -> list[dict[str, Any]]:
    results = []
    for index, case in enumerate(cases):
        if limit is not None and index >= limit:
            break
        results.append(evaluate_case(case, generate_fn))
    return results


def summary(results: list[dict[str, Any]]) -> dict[str, Any]:
    total = len(results)
    passed = sum(1 for r in results if r["ok"])
    return {
        "total": total,
        "passed": passed,
        "accuracy": round(passed / total, 4) if total else 0.0,
    }


def build_generate_fn(
    ckpt_dir: str,
    ckpt_name: str = "last",
    device: str = "cpu",
    max_new_tokens: int = 160,
):
    import torch

    from topogpt3.checkpoint_meta import config_from_checkpoint
    from topogpt3.model import BPETokenizer, TopoGPT2

    checkpoint = str(Path(ckpt_dir) / ckpt_name)
    cfg, _meta = config_from_checkpoint(checkpoint, device=device)
    tokenizer = BPETokenizer("gpt2")
    cfg.VOCAB_SIZE = tokenizer.vocab_size
    model = TopoGPT2(cfg).to(device).eval()
    from safetensors.torch import load_file

    model.load_state_dict(
        load_file(str(Path(checkpoint) / "model.safetensors"), device=device),
        strict=False,
    )

    @torch.no_grad()
    def generate(prompt: str, profile_name: str = "") -> str:
        from topogpt3.fallback import synthesize_tool_call

        profile = resolve_profile(profile_name)
        ids = tokenizer.encode(prompt)
        if not ids:
            return ""
        ids = ids[-cfg.MAX_SEQ_LEN :]
        x = torch.tensor([ids], dtype=torch.long, device=device)
        out = model.generate(
            x,
            max_new_tokens=max_new_tokens,
            temperature=profile.temperature,
            top_k=profile.top_k,
            repetition_penalty=profile.repetition_penalty,
        )
        completion = tokenizer.decode(out[0, x.shape[1] :].tolist()).strip()
        if profile.require_tool and not parse_tool_calls(completion):
            synthesized = synthesize_tool_call(profile, prompt)
            if synthesized:
                from topogpt3.chat import TOOL_CALL_CLOSE, TOOL_CALL_OPEN

                completion = (
                    f"{TOOL_CALL_OPEN}{json.dumps(synthesized)}{TOOL_CALL_CLOSE}"
                )
        return completion

    return generate


def main() -> int:
    parser = argparse.ArgumentParser(description="Run JSONL task cases")
    parser.add_argument("--tasks-file", default="eval/apt_chain_cases.jsonl")
    parser.add_argument("--ckpt-dir", default="checkpoints_topogpt3")
    parser.add_argument("--ckpt-name", default="last")
    parser.add_argument("--device", default="cpu")
    parser.add_argument("--max-new-tokens", type=int, default=160)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--out", default=None)
    args = parser.parse_args()

    cases = load_cases(args.tasks_file)
    generate_fn = build_generate_fn(
        args.ckpt_dir, args.ckpt_name, args.device, args.max_new_tokens
    )
    results = evaluate_cases(cases, generate_fn, args.limit)
    stats = summary(results)
    print(json.dumps(stats))

    if args.out:
        out_path = Path(args.out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with out_path.open("a", encoding="utf-8") as handle:
            for row in results:
                handle.write(json.dumps(row) + "\n")
    return 0 if stats["accuracy"] >= 1.0 else 1


if __name__ == "__main__":
    sys.exit(main())
