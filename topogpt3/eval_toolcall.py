"""Tool-call evaluation for TopoGPT3 agents.

Runs TOOLS cases through a generate_fn and checks name/args parsing,
including apt_chain cases (LazyOwn fallback contract).
"""

from __future__ import annotations

import json

from .chat import apply_chat_template, parse_tool_calls
from .fallback import validate_tool_call
from .tools_agent import CHECK_ARGS, TOOLS, execute_tool

CASES = [
    {"prompt": "Compute 12*34 with calculate_math.", "expect_tool": "calculate_math"},
    {"prompt": "Run python: print(2+2) with run_python.", "expect_tool": "run_python"},
    {
        "prompt": "Run the full chain against 10.10.11.78 (dry run).",
        "expect_tool": "apt_chain",
        "args": {"target": "10.10.11.78", "dry_run": True},
    },
    {
        "prompt": "Emulate chain apt_rocke against 10.0.0.5, dry-run json.",
        "expect_tool": "apt_chain",
        "args": {"chain": "apt_rocke", "target": "10.0.0.5", "dry_run": True},
    },
    {
        "prompt": "Run the command nmap -sV against 10.0.0.5 via run_command.",
        "expect_tool": "run_command",
        "args": {"command": "nmap -sV 10.0.0.5"},
    },
]


def run_case(
    generate_fn, prompt: str, expect_tool: str, expect_args: dict | None = None
):
    msgs = [{"role": "user", "content": prompt}]
    text = generate_fn(
        apply_chat_template(msgs, tools=TOOLS, add_generation_prompt=True)
    )
    calls = parse_tool_calls(text)
    ok_tool = any(c.get("name") == expect_tool for c in calls)
    ok_args = (
        all(
            CHECK_ARGS.get(c.get("name", ""), lambda a: True)(
                c.get("arguments", {}) if isinstance(c.get("arguments"), dict) else {}
            )
            for c in calls
        )
        if calls
        else False
    )
    ok_schema = True
    schema_reason = "ok"
    if calls:
        allowed = {t["function"]["name"] for t in TOOLS}
        ok_schema, schema_reason = validate_tool_call(calls[0], allowed)
        if ok_schema and expect_args:
            args = calls[0].get("arguments", {})
            if isinstance(args, str):
                try:
                    args = json.loads(args)
                except json.JSONDecodeError:
                    args = {}
            for key, want in expect_args.items():
                if str(args.get(key, "")).strip() != str(want).strip():
                    ok_schema = False
                    schema_reason = f"args[{key}]={args.get(key)!r} != {want!r}"
                    break
    results = [
        execute_tool(
            c.get("name", ""),
            c.get("arguments", {}) if isinstance(c.get("arguments"), dict) else {},
        )
        for c in calls
    ]
    return {
        "prompt": prompt,
        "text": text,
        "calls": calls,
        "ok_tool": ok_tool,
        "ok_args": ok_args,
        "ok_schema": ok_schema,
        "schema_reason": schema_reason,
        "results": results,
    }


def evaluate(generate_fn):
    rows = [
        run_case(generate_fn, c["prompt"], c["expect_tool"], c.get("args"))
        for c in CASES
    ]
    acc = sum(r["ok_tool"] for r in rows) / max(len(rows), 1)
    schema_acc = sum(r["ok_schema"] for r in rows) / max(len(rows), 1)
    return {"accuracy": acc, "schema_accuracy": schema_acc, "cases": rows}
