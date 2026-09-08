"""Code-first tool definitions for TopoGPT3 Agent-RL.

Keeps TopoGPT3 identity: primary tool is sandboxed Python execution
(eval/sandbox.py + Pi harness); mock tools kept for offline use.
"""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
try:
    from eval.sandbox import safe_exec  # type: ignore
    _HAS_SANDBOX = True
except Exception:
    _HAS_SANDBOX = False

from .chat import parse_tool_calls

TOOLS = [
    {"type": "function", "function": {
        "name": "run_python",
        "description": "Execute Python code in sandbox, returns stdout/stderr.",
        "parameters": {"type": "object",
                       "properties": {"code": {"type": "string"}},
                       "required": ["code"]}}},
    {"type": "function", "function": {
        "name": "calculate_math",
        "description": "Evaluate a math expression.",
        "parameters": {"type": "object",
                       "properties": {"expression": {"type": "string"}},
                       "required": ["expression"]}}},
    {"type": "function", "function": {
        "name": "translate_text",
        "description": "Toy translator (compat).",
        "parameters": {"type": "object",
                       "properties": {"text": {"type": "string"},
                                      "target_language": {"type": "string"}},
                       "required": ["text", "target_language"]}}},
]

MOCK = {
    "calculate_math": lambda a: {"result": str(__import__("math") and eval(
        str(a.get("expression", "0")).replace("^", "**"),
        {"__builtins__": {}, "math": math}))},
    "translate_text": lambda a: {"translated_text": a.get("text", "")},
}

CHECK_ARGS = {
    "run_python": lambda a: bool(a.get("code")),
    "calculate_math": lambda a: bool(a.get("expression")),
    "translate_text": lambda a: bool(a.get("text")),
}


def execute_tool(name: str, args: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    if name == "run_python":
        code = args.get("code", "")
        if _HAS_SANDBOX:
            try:
                res = safe_exec(code, timeout=5)
                return {"stdout": res.get("stdout", ""),
                        "stderr": res.get("stderr", ""),
                        "passed": res.get("passed", True)}
            except Exception as e:
                return {"stderr": str(e), "passed": False}
        return {"stderr": "sandbox unavailable", "passed": False}
    fn = MOCK.get(name)
    if not fn:
        return None
    try:
        return fn(args)
    except Exception:
        return None


def rollout_multiturn(generate_fn, tokenizer, messages: List[Dict[str, Any]],
                      tools=None, max_turns: int = 3, max_new_tokens: int = 256,
                      open_thinking: bool = False):
    """generate_fn(prompt_text)->text. Returns (full_text, tool_trace)."""
    from .chat import apply_chat_template
    tools = tools if tools is not None else TOOLS
    hist = [dict(m) for m in messages]
    trace = []
    full = ""
    for _ in range(max_turns):
        prompt = apply_chat_template(hist, tools=tools, add_generation_prompt=True,
                                     open_thinking=open_thinking and not full)
        out = generate_fn(prompt)
        full += out
        calls = parse_tool_calls(out)
        hist.append({"role": "assistant", "content": out,
                     "tool_calls": calls})
        if not calls:
            break
        for c in calls:
            name = c.get("name", "")
            cargs = c.get("arguments", {})
            if isinstance(cargs, str):
                try:
                    cargs = json.loads(cargs)
                except Exception:
                    cargs = {}
            res = execute_tool(name, cargs)
            trace.append({"name": name, "result": res})
            hist.append({"role": "tool", "content": json.dumps(res or {})})
    return full, trace
