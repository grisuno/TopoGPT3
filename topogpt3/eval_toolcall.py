"""Tool-call evaluation for TopoGPT3 agents.

Runs TOOLS cases through a generate_fn and checks name/args parsing.
"""
from __future__ import annotations

from .chat import apply_chat_template
from .tools_agent import CHECK_ARGS, TOOLS, execute_tool
from .chat import parse_tool_calls

CASES = [
    {"prompt": "Compute 12*34 with calculate_math.",
     "expect_tool": "calculate_math"},
    {"prompt": "Run python: print(2+2) with run_python.",
     "expect_tool": "run_python"},
]


def run_case(generate_fn, prompt: str, expect_tool: str):
    msgs = [{"role": "user", "content": prompt}]
    text = generate_fn(apply_chat_template(msgs, tools=TOOLS,
                                           add_generation_prompt=True))
    calls = parse_tool_calls(text)
    ok_tool = any(c.get("name") == expect_tool for c in calls)
    ok_args = all(CHECK_ARGS.get(c.get("name", ""), lambda a: True)(
        c.get("arguments", {}) if isinstance(c.get("arguments"), dict) else {})
        for c in calls) if calls else False
    results = [execute_tool(c.get("name", ""), c.get("arguments", {})
                            if isinstance(c.get("arguments"), dict) else {})
               for c in calls]
    return {"prompt": prompt, "text": text, "calls": calls,
            "ok_tool": ok_tool, "ok_args": ok_args, "results": results}


def evaluate(generate_fn):
    rows = [run_case(generate_fn, c["prompt"], c["expect_tool"]) for c in CASES]
    acc = sum(r["ok_tool"] for r in rows) / max(len(rows), 1)
    return {"accuracy": acc, "cases": rows}
