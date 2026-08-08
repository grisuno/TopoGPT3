#!/usr/bin/env python3
"""
Auto-continuation engine: detects truncated responses and feeds the last
incomplete lines back so the model can resume where it left off.

Used by both the standard inference pipeline and the HRM "thinking" mode.
"""
from __future__ import annotations

import re
from typing import List, Tuple


# ── Fence / block structures ────────────────────────────────────────────────


_OPENING = {"{": "}", "(": ")", "[": "]", "<": ">"}
_CLOSING = {v: k for k, v in _OPENING.items()}
_OPENERS = frozenset(_OPENING)
_CLOSERS = frozenset(_CLOSING)

_CODE_FENCE_RE = re.compile(r"^```(\w*)$")


def _count_unclosed_brackets(text: str) -> int:
    stack: List[str] = []
    for ch in text:
        if ch in _OPENERS:
            stack.append(ch)
        elif ch in _CLOSERS:
            if stack and _CLOSING.get(ch) == stack[-1]:
                stack.pop()
    return len(stack)


def _count_unclosed_fences(text: str) -> int:
    fences = 0
    for line in text.splitlines():
        m = _CODE_FENCE_RE.match(line.strip())
        if m:
            fences += 1
    return fences % 2  # 0 = balanced, 1 = unclosed


def is_response_complete(text: str, min_chars: int = 10) -> bool:
    """Heuristic to decide whether a model response looks finished.

    Returns True when the response seems naturally complete (no need to
    continue), False when it appears truncated and continuation may help.
    """
    stripped = text.rstrip()

    if len(stripped) < min_chars:
        return False

    if _count_unclosed_fences(stripped):
        return False

    if _count_unclosed_brackets(stripped) > 0:
        return False

    if not stripped:
        return False

    last_ch = stripped[-1]
    if last_ch in {":", ",", ";", "\\"}:
        return False

    if last_ch in {"\n", ".", "!", "?", ")", "}", "]", "`", '"', "'"}:
        return True

    return True


def extract_tail_for_continuation(text: str, tail_lines: int = 2,
                                  tail_chars: int = 512) -> str:
    """Return the last N lines (or up to tail_chars) of `text` as a
    continuation prefix to feed back into the model.

    The returned string can be prepended as context for the model's next
    generation call so it continues naturally from that point.
    """
    stripped = text.rstrip()
    if not stripped:
        return ""

    lines: List[str] = text.splitlines()
    result: List[str] = []
    total_chars = 0

    for line in reversed(lines):
        candidate = line
        new_total = total_chars + len(candidate) + 1
        if len(result) >= tail_lines:
            break
        if new_total > tail_chars:
            break
        result.append(candidate)
        total_chars = new_total

    result.reverse()
    return "\n".join(result)


def split_at_last_newline(text: str) -> Tuple[str, str]:
    """Split `text` at the last newline.

    Returns (prefix_without_last_line, last_line).
    Useful for discarding a trailing incomplete line before continuation.
    """
    if "\n" not in text:
        return "", text
    idx = text.rfind("\n")
    return text[:idx], text[idx + 1:]
