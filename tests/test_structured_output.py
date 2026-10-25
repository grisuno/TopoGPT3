"""Tests for DeepInfer-style structured outputs and deterministic seeds."""

import json

import pytest
import torch

from topogpt3.structured_output import (
    GrammarSpec,
    StructuredOutputError,
    build_constraint,
    constraint_from_request,
    parse_response_format,
    parse_so_args,
)


@pytest.fixture(scope="module")
def tokenizer():
    pytest.importorskip("tiktoken")
    from topogpt3.model import BPETokenizer

    try:
        return BPETokenizer("gpt2")
    except Exception as exc:  # noqa: BLE001 - offline environments should skip
        pytest.skip(f"gpt2 tokenizer unavailable: {exc}")


class TestParseResponseFormat:
    def test_none_and_text(self):
        assert parse_response_format(None) is None
        assert parse_response_format({"type": "text"}) is None

    def test_json_object(self):
        assert parse_response_format({"type": "json_object"}) == GrammarSpec(
            "json_object"
        )

    def test_json_schema(self):
        spec = parse_response_format(
            {
                "type": "json_schema",
                "json_schema": {"name": "person", "schema": {"type": "object"}},
            }
        )
        assert spec == GrammarSpec("json_schema", {"type": "object"})

    def test_regex(self):
        spec = parse_response_format({"type": "regex", "regex": "[A-Z]{2}"})
        assert spec == GrammarSpec("regex", "[A-Z]{2}")

    def test_grammar(self):
        spec = parse_response_format({"type": "grammar", "grammar": 'root ::= "a"'})
        assert spec == GrammarSpec("ebnf", 'root ::= "a"')

    @pytest.mark.parametrize(
        "bad",
        [
            {"type": "bogus"},
            {"type": "json_schema"},
            {"type": "regex"},
            {"type": "grammar"},
        ],
    )
    def test_invalid_payloads(self, bad):
        with pytest.raises(StructuredOutputError):
            parse_response_format(bad)


class TestParseSoArgs:
    def test_json_string_schema(self):
        spec = parse_so_args(
            {"schema_type": "json", "schema": json.dumps({"type": "object"})}
        )
        assert spec == GrammarSpec("json_schema", {"type": "object"})

    def test_regex(self):
        assert parse_so_args({"schema_type": "regex", "schema": "a+"}) == GrammarSpec(
            "regex", "a+"
        )

    def test_ebnf(self):
        spec = parse_so_args({"schema_type": "ebnf", "schema": 'root ::= "a"'})
        assert spec == GrammarSpec("ebnf", 'root ::= "a"')

    def test_requires_schema(self):
        with pytest.raises(StructuredOutputError):
            parse_so_args({"schema_type": "regex"})

    def test_unknown_schema_type(self):
        with pytest.raises(StructuredOutputError):
            parse_so_args({"schema_type": "lark", "schema": "start: /a/"})


class TestGrammarConstraint:
    def test_json_schema_accepts_and_terminates(self, tokenizer):
        pytest.importorskip("xgrammar")
        spec = parse_response_format(
            {
                "type": "json_schema",
                "json_schema": {
                    "name": "person",
                    "schema": {
                        "type": "object",
                        "properties": {"name": {"type": "string"}},
                        "required": ["name"],
                        "additionalProperties": False,
                    },
                },
            }
        )
        constraint = build_constraint(tokenizer, spec)

        logits = torch.zeros(1, tokenizer.vocab_size)
        constraint.apply(logits)
        assert torch.isfinite(logits).any()

        for token_id in tokenizer.encode('{"name":"x"}'):
            assert constraint.accept(token_id)
        assert constraint.is_terminated

    def test_regex_masks_illegal_first_token(self, tokenizer):
        pytest.importorskip("xgrammar")
        constraint = build_constraint(
            tokenizer, parse_so_args({"schema_type": "regex", "schema": "[a-z]+"})
        )

        logits = torch.zeros(1, tokenizer.vocab_size)
        constraint.apply(logits)

        (a_id,) = tokenizer.encode("a")
        (brace_id,) = tokenizer.encode("{")
        assert torch.isfinite(logits[0, a_id])
        assert not torch.isfinite(logits[0, brace_id])

    def test_reset_restores_initial_state(self, tokenizer):
        pytest.importorskip("xgrammar")
        constraint = build_constraint(
            tokenizer, parse_response_format({"type": "json_object"})
        )
        for token_id in tokenizer.encode('{"a":1}'):
            assert constraint.accept(token_id)
        assert constraint.is_terminated

        constraint.reset()
        assert not constraint.is_terminated

    def test_invalid_regex_raises(self, tokenizer):
        pytest.importorskip("xgrammar")
        with pytest.raises(StructuredOutputError):
            build_constraint(tokenizer, GrammarSpec("regex", "("))


def test_constraint_from_request_rejects_both_surfaces(tokenizer):
    with pytest.raises(StructuredOutputError):
        constraint_from_request(
            tokenizer,
            {"type": "json_object"},
            {"schema_type": "regex", "schema": "a+"},
        )


class TestRequestModels:
    def test_chat_accepts_seed_and_response_format(self):
        pytest.importorskip("fastapi")
        from topogpt3.api_server import ChatCompletionRequest

        req = ChatCompletionRequest(
            messages=[{"role": "user", "content": "hi"}],
            seed=7,
            response_format={"type": "json_object"},
        )
        assert req.seed == 7
        assert req.response_format == {"type": "json_object"}

    def test_completion_accepts_so_args(self):
        pytest.importorskip("fastapi")
        from topogpt3.api_server import CompletionRequest

        req = CompletionRequest(
            prompt="x", so_args={"schema_type": "regex", "schema": "a+"}
        )
        assert req.so_args["schema_type"] == "regex"

    def test_negative_seed_rejected(self):
        pytest.importorskip("fastapi")
        from pydantic import ValidationError

        from topogpt3.api_server import CompletionRequest

        with pytest.raises(ValidationError):
            CompletionRequest(prompt="x", seed=-1)


def test_auto_continue_with_constraint_rejected():
    pytest.importorskip("fastapi")
    from fastapi import HTTPException

    from topogpt3.api_server import CompletionRequest, _request_constraint

    req = CompletionRequest(
        prompt="x",
        auto_continue=True,
        response_format={"type": "json_object"},
    )
    with pytest.raises(HTTPException) as exc:
        _request_constraint(req)
    assert exc.value.status_code == 400


def test_make_generator_is_reproducible():
    pytest.importorskip("fastapi")
    from topogpt3.api_server import _make_generator

    probs = torch.ones(1, 20) / 20
    first = torch.multinomial(probs, 5, generator=_make_generator(123, "cpu"))
    second = torch.multinomial(probs, 5, generator=_make_generator(123, "cpu"))
    assert torch.equal(first, second)
