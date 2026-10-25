"""Code-first tool definitions for TopoGPT3 Agent-RL.

Keeps TopoGPT3 identity: primary tool is sandboxed Python execution
(eval/sandbox.py + Pi harness); mock tools kept for offline use.
"""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
try:
    from eval.sandbox import safe_exec  # type: ignore
    _HAS_SANDBOX = True
except Exception:
    _HAS_SANDBOX = False

from .chat import parse_tool_calls
from .fallback import APT_CHAIN_TOOL, validate_tool_call

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
    APT_CHAIN_TOOL,
]

MOCK = {
    "calculate_math": lambda a: {"result": str(__import__("math") and eval(
        str(a.get("expression", "0")).replace("^", "**"),
        {"__builtins__": {}, "math": math}))},
    "translate_text": lambda a: {"translated_text": a.get("text", "")},
}


def _apt_chain_preview(args: dict[str, Any]) -> dict[str, Any]:
    """Validate an apt_chain call and return the exact command, never execute it.

    Execution belongs to LazyOwn. The model-side agent only needs a safe,
    verifiable tool response for SFT/RL traces.
    """
    ok, reason = validate_tool_call({"name": "apt_chain", "arguments": args})
    if not ok:
        return {"ok": False, "error": reason}
    parts = ["apt_chain", str(args.get("chain", "apt_chain"))]
    if args.get("target"):
        parts.append(str(args["target"]))
    if args.get("playbook"):
        parts.extend(["--playbook", str(args["playbook"])])
    if args.get("steps"):
        parts.extend(["--step", str(args["steps"])])
    if args.get("dry_run", True):
        parts.append("--dry-run")
    if args.get("json", True):
        parts.append("--json")
    if args.get("no_checkpoint"):
        parts.append("--no-checkpoint")
    if args.get("timeout_s"):
        parts.extend(["--timeout", str(args["timeout_s"])])
    for key, value in (args.get("vars") or {}).items():
        parts.extend(["--var", f"{key}={value}"])
    return {"ok": True, "command": " ".join(parts), "target": args.get("target")}


MOCK["apt_chain"] = _apt_chain_preview

CHECK_ARGS = {
    "run_python": lambda a: bool(a.get("code")),
    "calculate_math": lambda a: bool(a.get("expression")),
    "translate_text": lambda a: bool(a.get("text")),
    "apt_chain": lambda a: validate_tool_call(
        {"name": "apt_chain", "arguments": a}
    )[0],
}


def execute_tool(name: str, args: dict[str, Any]) -> dict[str, Any] | None:
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


def rollout_multiturn(generate_fn, tokenizer, messages: list[dict[str, Any]],
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
