"""Generic task eval tests (no model load)."""

import json

from eval.tasks import (
    evaluate_cases,
    load_cases,
    summary,
    verify_regex,
    verify_tool_call,
)
from topogpt3.chat import TOOL_CALL_CLOSE, TOOL_CALL_OPEN
from topogpt3.fallback import resolve_profile, synthesize_tool_call


def _gen(prompt, profile_name=""):
    call = synthesize_tool_call(resolve_profile(profile_name), prompt)
    return f"{TOOL_CALL_OPEN}{json.dumps(call)}{TOOL_CALL_CLOSE}" if call else ""


def test_apt_chain_cases_full_pass():
    cases = load_cases("eval/apt_chain_cases.jsonl")
    results = evaluate_cases(cases, _gen)
    stats = summary(results)
    assert stats["accuracy"] == 1.0, [
        (r["id"], r["reason"]) for r in results if not r["ok"]
    ]


def test_regex_verifier():
    case = {"verifier": {"type": "regex", "pattern": r"[A-Z]{2}-[0-9]{3}"}}
    assert verify_regex(case, "AB-123")[0]
    assert not verify_regex(case, "ab-123")[0]


def test_tool_call_verifier_rejects_wrong_target():
    case = {
        "verifier": {"type": "apt_chain", "tool": "apt_chain", "target": "10.0.0.9"}
    }
    completion = _gen("Run the full chain against 10.10.11.78.", "apt-chain")
    ok, reason = verify_tool_call(case, completion)
    assert not ok and "target" in reason
