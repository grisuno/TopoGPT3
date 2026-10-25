"""Data pipeline for SFT/distillation: dedup, quality filter, teacher traces.

Stages (each independently runnable, JSONL in / JSONL out):
    - load/clean: normalize whitespace, strip control chars
    - quality filter: language noise, line length, special-token ratio
    - dedup: content-hash (exact) + optional fuzzy (first 200 chars)
    - teacher: generate traces via an OpenAI-compatible endpoint
    - verify: python_ast (always), optional sandboxed execution for Python
    - export: chat-format JSONL ready for datasets_chat/export_chat

CLI:
    python -m topogpt3.data_pipeline --input raw.jsonl --out clean.jsonl
    python -m topogpt3.data_pipeline --input prompts.jsonl --out sft.jsonl \
        --teacher-url http://localhost:11434/v1 --teacher-model llama3.1 \
        --verify python
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import os
import re
import sys
import urllib.request
from collections.abc import Iterable
from pathlib import Path
from typing import Any

CONTROL_RE = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]")
WHITESPACE_RE = re.compile(r"[ \t]+")
_NEWLINE_RE = re.compile(r"\n{3,}")


def normalize_text(text: str) -> str:
    text = CONTROL_RE.sub("", text or "")
    text = WHITESPACE_RE.sub(" ", text)
    text = _NEWLINE_RE.sub("\n\n", text)
    return text.strip()


def content_hash(text: str) -> str:
    return hashlib.sha256(normalize_text(text).encode()).hexdigest()


def quality_filter(
    text: str,
    *,
    max_line_len: int = 500,
    min_chars: int = 24,
    max_special_ratio: float = 0.25,
) -> tuple[bool, str]:
    if len(text) < min_chars:
        return False, "too_short"
    lines = text.splitlines() or [text]
    if max(len(line) for line in lines) > max_line_len:
        return False, "long_line"
    special = sum(1 for ch in text if not ch.isprintable())
    if special / max(1, len(text)) > max_special_ratio:
        return False, "special_ratio"
    return True, "ok"


def dedup_stream(
    rows: Iterable[dict[str, Any]], key_field: str = "text", fuzzy: bool = False
) -> Iterable[dict[str, Any]]:
    seen_exact: set[str] = set()
    seen_fuzzy: set[str] = set()
    for row in rows:
        text = normalize_text(str(row.get(key_field, "")))
        digest = content_hash(text)
        if digest in seen_exact:
            continue
        seen_exact.add(digest)
        if fuzzy:
            prefix = content_hash(text[:200])
            if prefix in seen_fuzzy:
                continue
            seen_fuzzy.add(prefix)
        yield {**row, key_field: text}


def parse_jsonl(path: str | Path) -> Iterable[dict[str, Any]]:
    with open(path, "r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line and not line.startswith("#"):
                try:
                    yield json.loads(line)
                except json.JSONDecodeError:
                    continue


def write_jsonl(path: str | Path, rows: Iterable[dict[str, Any]]) -> int:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")
            count += 1
    return count


class TeacherClient:
    """Minimal OpenAI-compatible chat client for teacher generation."""

    def __init__(
        self,
        base_url: str,
        model: str,
        api_key: str = "",
        timeout: int = 240,
        temperature: float = 0.2,
        max_tokens: int = 512,
    ):
        self.base_url = base_url.rstrip("/")
        self.model = model
        self.api_key = api_key
        self.timeout = timeout
        self.temperature = temperature
        self.max_tokens = max_tokens

    def chat(self, system: str, user: str) -> str:
        body = json.dumps(
            {
                "model": self.model,
                "messages": [
                    {"role": "system", "content": system},
                    {"role": "user", "content": user},
                ],
                "temperature": self.temperature,
                "max_tokens": self.max_tokens,
                "stream": False,
            }
        ).encode()
        headers = {"Content-Type": "application/json"}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        elif re.match(r"^https?://(localhost|127\.0\.0\.1)", self.base_url):
            headers["Authorization"] = "Bearer sk-no-key-required"
        request = urllib.request.Request(
            self.base_url + "/chat/completions",
            data=body,
            headers=headers,
            method="POST",
        )
        with urllib.request.urlopen(request, timeout=self.timeout) as response:
            data = json.loads(response.read())
        return str(data["choices"][0]["message"].get("content", "")).strip()


def sandbox_python(code: str, timeout: int = 10) -> tuple[bool, str]:
    """Run Python through the eval sandbox when available; AST-only fallback."""
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
    try:
        from eval.sandbox import safe_exec  # type: ignore

        result = safe_exec(code, timeout=timeout)
        return bool(result.get("passed", True)), str(result.get("stderr", ""))[:400]
    except Exception:  # noqa: BLE001 - sandbox optional
        try:
            ast.parse(code)
        except SyntaxError as exc:
            return False, f"syntax error: {exc}"
        return True, "ast_only"


def verify_completion(completion: str, mode: str = "python_ast") -> tuple[bool, str]:
    blocks = re.findall(r"```(?:python|py)?\s*(.*?)```", completion, re.DOTALL)
    code = blocks[0] if blocks else completion
    if mode in ("python", "sandbox"):
        return sandbox_python(code)
    try:
        ast.parse(code)
    except SyntaxError as exc:
        return False, f"syntax error: {exc}"
    return True, "ast_ok"


CODE_TEACHER_SYSTEM = (
    "You are a senior code assistant. Given an instruction, produce a "
    "correct, complete solution in one ```python block. No placeholders."
)

EXPLOIT_TEACHER_SYSTEM = (
    "You are a senior red-team analyst. Given an ExploitGym task "
    "(vulnerability analysis / patch analysis / exploit development), produce "
    "the requested artifact. Authorized lab use only."
)


def generate_teacher_rows(
    rows: Iterable[dict[str, Any]],
    teacher: TeacherClient,
    domain: str = "code",
    verify: str = "python_ast",
    max_keep: int | None = None,
) -> Iterable[dict[str, Any]]:
    system = EXPLOIT_TEACHER_SYSTEM if domain == "exploit" else CODE_TEACHER_SYSTEM
    kept = 0
    for row in rows:
        prompt = normalize_text(str(row.get("prompt", row.get("instruction", ""))))
        if not prompt:
            continue
        try:
            completion = teacher.chat(system, prompt)
        except Exception as exc:  # noqa: BLE001 - teacher failures are data
            yield {
                **row,
                "prompt": prompt,
                "ok": False,
                "error": f"teacher_failed: {exc}",
            }
            continue
        ok, reason = verify_completion(completion, mode=verify)
        record = {
            **row,
            "prompt": prompt,
            "completion": completion,
            "ok": ok,
            "reason": reason,
        }
        if ok:
            kept += 1
            yield record
        if max_keep is not None and kept >= max_keep:
            break


def to_chat_row(row: dict[str, Any]) -> dict[str, Any]:
    return {
        "messages": [
            {"role": "user", "content": str(row.get("prompt", ""))},
            {"role": "assistant", "content": str(row.get("completion", ""))},
        ]
    }


def clean_stage(input_path: str, output_path: str, *, fuzzy: bool = True) -> int:
    rows = parse_jsonl(input_path)
    cleaned = (
        {**row, "text": normalize_text(str(row.get("text", "")))} for row in rows
    )
    filtered = (row for row in cleaned if quality_filter(row["text"])[0])
    deduped = dedup_stream(filtered, fuzzy=fuzzy)
    return write_jsonl(output_path, deduped)


def teacher_stage(
    input_path: str,
    output_path: str,
    teacher_url: str,
    teacher_model: str,
    api_key: str = "",
    domain: str = "code",
    verify: str = "python_ast",
    max_keep: int | None = None,
) -> int:
    teacher = TeacherClient(teacher_url, teacher_model, api_key)
    rows = parse_jsonl(input_path)
    kept = generate_teacher_rows(
        rows, teacher, domain=domain, verify=verify, max_keep=max_keep
    )
    return write_jsonl(output_path, kept)


def main() -> int:
    parser = argparse.ArgumentParser(description="SFT data pipeline")
    parser.add_argument("--input", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument(
        "--stage", choices=["clean", "teacher", "chat"], default="clean"
    )
    parser.add_argument("--key-field", default="text")
    parser.add_argument("--no-fuzzy", action="store_true")
    parser.add_argument("--teacher-url", default=os.environ.get("TEACHER_URL", ""))
    parser.add_argument(
        "--teacher-model", default=os.environ.get("TEACHER_MODEL", "llama3.1")
    )
    parser.add_argument("--teacher-key", default=os.environ.get("TEACHER_API_KEY", ""))
    parser.add_argument("--domain", choices=["code", "exploit"], default="code")
    parser.add_argument(
        "--verify", choices=["python_ast", "python"], default="python_ast"
    )
    parser.add_argument("--max-keep", type=int, default=None)
    args = parser.parse_args()

    if args.stage == "clean":
        rows = parse_jsonl(args.input)
        cleaned = (
            {**row, args.key_field: normalize_text(str(row.get(args.key_field, "")))}
            for row in rows
        )
        filtered = (row for row in cleaned if quality_filter(row[args.key_field])[0])
        deduped = dedup_stream(
            filtered, key_field=args.key_field, fuzzy=not args.no_fuzzy
        )
        written = write_jsonl(args.out, deduped)
    elif args.stage == "teacher":
        if not args.teacher_url:
            print("--teacher-url required for stage=teacher", file=sys.stderr)
            return 2
        written = teacher_stage(
            args.input,
            args.out,
            args.teacher_url,
            args.teacher_model,
            args.teacher_key,
            args.domain,
            args.verify,
            args.max_keep,
        )
    else:
        written = write_jsonl(
            args.out, (to_chat_row(r) for r in parse_jsonl(args.input))
        )
    print(json.dumps({"written": written, "stage": args.stage, "out": args.out}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
