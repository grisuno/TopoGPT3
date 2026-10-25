"""Constrained decoding for the TopoGPT3 OpenAI-compatible server.

DeepInfer exposes structured output through ``SamplingParams.so_args``
(``json`` / ``regex`` / ``ebnf``). This module mirrors that surface and also
understands OpenAI-style ``response_format`` payloads:

    {"type": "text"}
    {"type": "json_object"}
    {"type": "json_schema", "json_schema": {"name": "...", "schema": {...}}}
    {"type": "regex", "regex": "[A-Z]{2}-[0-9]{3}"}
    {"type": "grammar", "grammar": "root ::= ..."}

``xgrammar`` is imported lazily. The server keeps working without it; only
requests that ask for a constraint fail with a clear error.
"""

from __future__ import annotations

import json
import threading
from dataclasses import dataclass
from typing import Any

MAX_CACHED_GRAMMARS = 64


class StructuredOutputError(ValueError):
    """Invalid or unsupported structured-output request."""


@dataclass(frozen=True)
class GrammarSpec:
    kind: str  # json_object | json_schema | regex | ebnf
    payload: Any = None

    def cache_key(self) -> str:
        if isinstance(self.payload, str):
            body = self.payload
        else:
            body = json.dumps(
                self.payload, sort_keys=True, separators=(",", ":"), default=str
            )
        return f"{self.kind}:{body}"


def _import_xgrammar():
    try:
        import xgrammar  # type: ignore[import-not-found]
    except ImportError as exc:  # pragma: no cover - exercised without extra
        raise StructuredOutputError(
            "structured outputs require xgrammar: pip install 'topogpt3[structured]'"
        ) from exc
    return xgrammar


def parse_response_format(response_format: Any) -> GrammarSpec | None:
    """Translate an OpenAI ``response_format`` payload into a GrammarSpec."""
    if response_format is None:
        return None
    if not isinstance(response_format, dict):
        raise StructuredOutputError("response_format must be an object")

    kind = response_format.get("type")
    if kind in (None, "text"):
        return None
    if kind == "json_object":
        return GrammarSpec("json_object")
    if kind == "json_schema":
        body = response_format.get("json_schema")
        if body is None:
            body = response_format.get("schema")
        if body is None:
            raise StructuredOutputError("json_schema requires a schema field")
        if isinstance(body, dict) and "schema" in body:
            schema = body["schema"]
        else:
            schema = body
        return GrammarSpec("json_schema", schema)
    if kind == "regex":
        pattern = response_format.get("regex", response_format.get("pattern"))
        if not isinstance(pattern, str) or not pattern:
            raise StructuredOutputError("regex response_format requires a pattern")
        return GrammarSpec("regex", pattern)
    if kind in ("grammar", "ebnf"):
        grammar = response_format.get("grammar", response_format.get("ebnf"))
        if not isinstance(grammar, str) or not grammar:
            raise StructuredOutputError("grammar response_format requires a grammar")
        return GrammarSpec("ebnf", grammar)

    raise StructuredOutputError(f"unsupported response_format type: {kind!r}")


def parse_so_args(so_args: Any) -> GrammarSpec | None:
    """Translate a DeepInfer-style ``so_args`` payload into a GrammarSpec."""
    if so_args is None:
        return None
    if not isinstance(so_args, dict):
        raise StructuredOutputError("so_args must be an object")

    schema_type = so_args.get("schema_type")
    schema = so_args.get("schema")
    if schema_type in (None, "text"):
        return None
    if schema_type == "json_object":
        return GrammarSpec("json_object")
    if schema_type == "json":
        if isinstance(schema, str):
            try:
                schema = json.loads(schema)
            except json.JSONDecodeError as exc:
                raise StructuredOutputError(f"invalid JSON schema: {exc}") from exc
        if not isinstance(schema, dict):
            raise StructuredOutputError("schema_type='json' requires a JSON schema")
        return GrammarSpec("json_schema", schema)
    if schema_type == "regex":
        if not isinstance(schema, str) or not schema:
            raise StructuredOutputError("schema_type='regex' requires a pattern")
        return GrammarSpec("regex", schema)
    if schema_type in ("ebnf", "grammar"):
        if not isinstance(schema, str) or not schema:
            raise StructuredOutputError("schema_type='ebnf' requires a grammar")
        return GrammarSpec("ebnf", schema)

    raise StructuredOutputError(f"unsupported schema_type: {schema_type!r}")


_COMPILER_LOCK = threading.Lock()
_COMPILERS: dict[tuple[str, int], tuple[Any, int]] = {}
_COMPILED: dict[tuple[tuple[str, int], str], Any] = {}


def _tokenizer_key(tokenizer: Any) -> tuple[str, int]:
    enc = getattr(tokenizer, "enc", None)
    if enc is None:
        raise StructuredOutputError("tokenizer does not expose a tiktoken encoding")
    return (getattr(enc, "name", "bpe"), int(enc.n_vocab))


def _get_compiler(tokenizer: Any) -> tuple[Any, int]:
    xg = _import_xgrammar()
    enc = tokenizer.enc
    key = _tokenizer_key(tokenizer)

    with _COMPILER_LOCK:
        cached = _COMPILERS.get(key)
    if cached is not None:
        return cached

    vocab = [enc.decode_single_token_bytes(i) for i in range(enc.n_vocab)]
    eot = getattr(tokenizer, "eot_token", None)
    stop_ids = [int(eot())] if callable(eot) else None
    tokenizer_info = xg.TokenizerInfo(
        vocab, vocab_size=enc.n_vocab, stop_token_ids=stop_ids
    )
    compiler = xg.GrammarCompiler(tokenizer_info)

    with _COMPILER_LOCK:
        _COMPILERS.setdefault(key, (compiler, enc.n_vocab))
        return _COMPILERS[key]


def _compile(spec: GrammarSpec, compiler: Any) -> Any:
    xg = _import_xgrammar()
    try:
        if spec.kind == "json_object":
            grammar = xg.Grammar.builtin_json_grammar()
        elif spec.kind == "json_schema":
            grammar = xg.Grammar.from_json_schema(spec.payload)
        elif spec.kind == "regex":
            grammar = xg.Grammar.from_regex(spec.payload)
        elif spec.kind == "ebnf":
            grammar = xg.Grammar.from_ebnf(spec.payload)
        else:  # pragma: no cover - guarded by the parsers
            raise StructuredOutputError(f"unsupported grammar kind: {spec.kind}")
        return compiler.compile_grammar(grammar)
    except StructuredOutputError:
        raise
    except Exception as exc:
        raise StructuredOutputError(f"invalid {spec.kind} constraint: {exc}") from exc


class GrammarConstraint:
    """Per-request xgrammar matcher that masks logits in place."""

    def __init__(self, xg: Any, compiled: Any, vocab_size: int):
        self._xg = xg
        self._compiled = compiled
        self.vocab_size = vocab_size
        self._matcher = self._new_matcher()
        self._bitmask = xg.allocate_token_bitmask(1, vocab_size)

    def _new_matcher(self):
        return self._xg.GrammarMatcher(
            self._compiled, terminate_without_stop_token=True
        )

    def reset(self) -> None:
        self._matcher = self._new_matcher()

    @property
    def is_terminated(self) -> bool:
        return bool(self._matcher.is_terminated())

    def apply(self, logits: Any) -> None:
        """Mask disallowed tokens in ``logits`` with ``-inf`` in place."""
        if self._matcher.is_terminated():
            return
        self._matcher.fill_next_token_bitmask(self._bitmask, 0)
        self._xg.apply_token_bitmask_inplace(logits, self._bitmask)

    def accept(self, token_id: int) -> bool:
        """Feed an emitted token to the matcher. Returns False if it is invalid."""
        if self._matcher.is_terminated():
            return True
        return bool(self._matcher.accept_token(int(token_id)))


def build_constraint(
    tokenizer: Any, spec: GrammarSpec | None
) -> GrammarConstraint | None:
    """Compile ``spec`` (cached) and return a fresh matcher for one request."""
    if spec is None:
        return None

    compiler, vocab_size = _get_compiler(tokenizer)
    cache_key = (_tokenizer_key(tokenizer), spec.cache_key())

    with _COMPILER_LOCK:
        compiled = _COMPILED.get(cache_key)
    if compiled is None:
        compiled = _compile(spec, compiler)
        with _COMPILER_LOCK:
            if len(_COMPILED) >= MAX_CACHED_GRAMMARS:
                _COMPILED.clear()
            _COMPILED[cache_key] = compiled

    return GrammarConstraint(_import_xgrammar(), compiled, vocab_size)


def constraint_from_request(
    tokenizer: Any,
    response_format: Any = None,
    so_args: Any = None,
) -> GrammarConstraint | None:
    """Resolve either request surface into a ready-to-use constraint."""
    if response_format is not None and so_args is not None:
        raise StructuredOutputError("use either response_format or so_args, not both")
    spec = parse_response_format(response_format)
    if spec is None:
        spec = parse_so_args(so_args)
    return build_constraint(tokenizer, spec)
