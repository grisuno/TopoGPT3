"""Fallback profiles, apt_chain validation and candidate reranking tests."""

import json

from topogpt3.chat import TOOL_CALL_CLOSE, TOOL_CALL_OPEN
from topogpt3.fallback import (
    APT_CHAIN_TOOL,
    LAZYOWN_TOOLS,
    PROFILES,
    rank_candidates,
    resolve_profile,
    score_candidate,
    synthesize_tool_call,
    tool_calls_payload,
    validate_tool_call,
)


def _call(name, args):
    return f"{TOOL_CALL_OPEN}{json.dumps({'name': name, 'arguments': args})}{TOOL_CALL_CLOSE}"


class TestProfiles:
    def test_resolve_by_name_and_alias(self):
        assert resolve_profile("topogpt3").name == "topogpt3"
        assert resolve_profile("apt_chain").name == "topoexploit-apt-chain"
        assert resolve_profile(None).name == "topogpt3"

    def test_unknown_falls_back(self):
        assert resolve_profile("nope-xyz").name == "topogpt3"

    def test_apt_chain_tools_registered(self):
        names = {t["function"]["name"] for t in LAZYOWN_TOOLS}
        assert "apt_chain" in names
        assert APT_CHAIN_TOOL["function"]["parameters"]["required"] == ["target"]


class TestValidateToolCall:
    def test_valid_apt_chain(self):
        ok, reason = validate_tool_call(
            {
                "name": "apt_chain",
                "arguments": {"target": "10.10.11.78", "dry_run": True},
            }
        )
        assert ok, reason

    def test_requires_target(self):
        ok, reason = validate_tool_call({"name": "apt_chain", "arguments": {}})
        assert not ok and "target" in reason

    def test_invalid_chain_name(self):
        ok, _reason = validate_tool_call(
            {
                "name": "apt_chain",
                "arguments": {"target": "10.0.0.1", "chain": "bad chain;"},
            }
        )
        assert not ok

    def test_run_command_forbidden_chars(self):
        ok, _ = validate_tool_call(
            {"name": "run_command", "arguments": {"command": "ls; rm -rf /"}}
        )
        assert not ok

    def test_unknown_tool(self):
        ok, reason = validate_tool_call({"name": "web_get", "arguments": {}})
        assert not ok and "unknown" in reason


class TestScoring:
    def test_tool_profile_prefers_valid_call(self):
        profile = resolve_profile("apt-chain")
        good = _call("apt_chain", {"target": "10.10.11.78", "dry_run": True})
        prose = "I would run the chain for you."
        best_text, score = "", -1e18
        for text in (prose, good):
            s, _d = score_candidate(text, profile)
            if s > score:
                best_text, score = text, s
        assert best_text == good and score > 0

    def test_require_tool_penalizes_prose(self):
        profile = resolve_profile("apt-chain")
        score, _ = score_candidate("Sure, tell me more.", profile)
        assert score < 0

    def test_code_profile_scores_parseable_code(self):
        profile = resolve_profile("topogpt3-code")
        good = "```python\ndef f(n):\n    return n+1\n```"
        bad = "```python\ndef f(n):\n    return n+\n```"
        assert score_candidate(good, profile)[0] > score_candidate(bad, profile)[0]

    def test_rank_candidates_sorted(self):
        profile = resolve_profile("apt-chain")
        ranked = rank_candidates(
            ["prose", _call("apt_chain", {"target": "10.0.0.1"})], profile
        )
        assert ranked[0][2].find("apt_chain") != -1


class TestSynthesize:
    def test_ip_prompt(self):
        profile = resolve_profile("apt-chain")
        call = synthesize_tool_call(profile, "Run the full chain against 10.10.11.78.")
        assert call and call["name"] == "apt_chain"
        assert call["arguments"]["target"] == "10.10.11.78"
        assert call["arguments"]["dry_run"] is True

    def test_playbook_extraction(self):
        call = synthesize_tool_call(
            resolve_profile("apt-chain"),
            "Emulate APT29 with chain apt_rocke against 10.0.0.5",
        )
        assert call and call["arguments"]["chain"] == "apt_rocke"

    def test_no_target_no_call(self):
        assert synthesize_tool_call(resolve_profile("apt-chain"), "hello world") is None


class TestToolCallsPayload:
    def test_openai_shape(self):
        calls = tool_calls_payload(_call("apt_chain", {"target": "10.0.0.1"}))
        assert calls[0]["type"] == "function"
        assert calls[0]["function"]["name"] == "apt_chain"
        args = json.loads(calls[0]["function"]["arguments"])
        assert args["target"] == "10.0.0.1"


def test_all_profiles_have_system():
    for profile in PROFILES.values():
        assert profile.system.strip()
