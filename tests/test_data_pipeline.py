"""Data pipeline tests: dedup, filters, teacher/verify/export (offline)."""

import json

from topogpt3.data_pipeline import (
    dedup_stream,
    normalize_text,
    quality_filter,
    to_chat_row,
    verify_completion,
    write_jsonl,
)


def test_normalize_strips_control_and_collapses_space():
    text = "a \x00b\t\t c\n\n\n\n\n\nd"
    cleaned = normalize_text(text)
    assert "\x00" not in cleaned
    assert "b c" in cleaned
    assert cleaned.count("\n\n") == 1


def test_dedup_exact_and_fuzzy():
    rows = [
        {"text": "hello world"},
        {"text": "hello  world"},
        {"text": "different content here"},
    ]
    out = list(dedup_stream(rows, fuzzy=False))
    assert len(out) == 2
    out = list(dedup_stream(rows, fuzzy=True))
    assert len(out) == 2


def test_quality_filter_bounds():
    ok, reason = quality_filter("short")
    assert not ok
    ok, reason = quality_filter("x" * 600)
    assert not ok and reason == "long_line"
    ok, _reason = quality_filter("valid content with enough chars")
    assert ok


def test_verify_python_ast_and_sandbox():
    ok, _ = verify_completion("```python\nprint(1)\n```", mode="python_ast")
    assert ok
    ok, _reason = verify_completion("```python\ndef broken(:\n```", mode="python_ast")
    assert not ok


def test_write_jsonl_roundtrip(tmp_path):
    path = tmp_path / "out.jsonl"
    n = write_jsonl(path, [{"a": 1}, {"a": 2}])
    rows = [json.loads(line) for line in path.read_text().splitlines()]
    assert n == 2 and rows[0]["a"] == 1


def test_to_chat_row():
    row = to_chat_row({"prompt": "p", "completion": "c"})
    assert row["messages"][0]["role"] == "user"
    assert row["messages"][1]["role"] == "assistant"
