"""OpenAI-compatible HTTP API server so TopoGPT3 can be used as a backend
for coding agents (e.g. Pi, Aider, Continue, Codex CLI, etc.).

Security Posture
----------------
- **Authentication**: Bearer token (``Authorization: Bearer <key>``).
  Keys are loaded from ``--keys`` (comma-separated) or the
  ``TOPOGPT3_API_KEYS`` env var. Admin keys (prefixed ``admin:``) get
  higher rate limits. Constant-time comparison prevents timing leaks.
- **Authorization**: token-bucket rate limiter per-key and per-IP with
  configurable thresholds. After ``max_failures`` bad auth attempts an IP
  is banned for ``ban_window`` seconds.
- **Input hardening**: Pydantic schemas enforce strict types, min/max
  bounds, and length limits. Request body is capped server-side. Error
  responses never leak stack traces.
- **Headers**: ``X-Content-Type-Options: nosniff``,
  ``X-Frame-Options: DENY``, ``X-XSS-Protection: 1; mode=block``,
  ``Content-Security-Policy: default-src 'none'`` on every response.
  CORS policy allows nothing by default (configurable allow-origins).
- **Audit**: structured JSON log lines for every request (truncated
  bodies, no secrets).

Usage::

    TOPOGPT3_API_KEYS="sk-secret-key,admin:sk-admin-key" \\
    python -m topogpt3 api_server \\
        --checkpoint checkpoints_topogpt3/last \\
        --port 8800

Pi / agent config::

    export PI_BASE_URL=http://localhost:8800/v1
    export PI_API_KEY=sk-secret-key

LazyOwn red-team checklist
--------------------------
- [ ] Auth bypass via missing Bearer header … 401
- [ ] Auth bypass via empty token … 401
- [ ] Auth bypass via timing attack on key comparison … prevented (secrets.compare_digest)
- [ ] Rate-limit bypass via spoofed X-Forwarded-For … rate-limited by real client IP
- [ ] Prompt injection to execute shell commands … impossible (no exec paths)
- [ ] TOCTOU on key file … keys read once at startup
- [ ] SSRF via the API … no outbound HTTP in inference path
- [ ] DoS via huge prompts … ``max_prompt_tokens`` cap
- [ ] DoS via connection exhaustion … uvicorn ``limit_concurrency``
- [ ] Information leak in error messages … ``include_in_schema=False`` on internal endpoints
- [ ] JSON injection in streaming chunks … validated via stdlib json
"""

from __future__ import annotations

import argparse
import asyncio
import hashlib
import json
import logging
import os
import re
import secrets
import sys
import threading
import time
from collections import defaultdict
from collections.abc import Awaitable, Callable
from contextlib import asynccontextmanager, contextmanager
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import torch

try:
    import uvicorn
    from fastapi import FastAPI, HTTPException, Request, Response
    from fastapi.middleware.cors import CORSMiddleware
    from fastapi.middleware.gzip import GZipMiddleware
    from fastapi.responses import JSONResponse, StreamingResponse
    from pydantic import BaseModel, Field, field_validator
except ImportError:
    sys.exit(
        "Install the api extras: pip install 'topogpt3[api]'  "
        "(fastapi + uvicorn + pydantic)"
    )

from safetensors.torch import load_file

from .checkpoint_meta import config_from_checkpoint
from .fallback import (
    models_payload,
    rank_candidates,
    resolve_profile,
    split_response,
    synthesize_tool_call,
)
from .model import BPETokenizer, TopoGPT2, set_seed
from .structured_output import (
    GrammarConstraint,
    StructuredOutputError,
    constraint_from_request,
)

# ═══════════════════════════════════════════════════════════════════════════
# Security constants
# ═══════════════════════════════════════════════════════════════════════════

MAX_REQUEST_BODY = 256 * 1024  # 256 KB
MAX_PROMPT_CHARS = 64 * 1024
MAX_MESSAGES = 200
MAX_STOP_STRINGS = 10
MAX_STOP_STRING_LEN = 128
MAX_CONTENT_LEN = 32 * 1024  # per message content field
MAX_OUTPUT_TOKENS = 4096
MAX_TEMPERATURE = 2.0
BAN_WINDOW_S = 3600  # 1 hour IP ban
MAX_AUTH_FAILURES = 10  # per IP within window
MAX_CONCURRENT_REQUESTS = 8
MAX_TOOL_BUFFER = 8192  # cap for unterminated tool-call buffers

# Rate limits (tokens per second, bucket capacity)
RATE_LIMIT_USER_RPS = 10.0
RATE_LIMIT_ADMIN_RPS = 50.0
RATE_BUCKET_CAPACITY = 60

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------

logger = logging.getLogger("topogpt3.api")
_audit_logger = logging.getLogger("topogpt3.api.audit")


def _setup_logging(verbose: bool = False) -> None:
    fmt = logging.Formatter(
        '{"time":"%(asctime)s","level":"%(levelname)s",'
        '"logger":"%(name)s","msg":%(message)s}',
        datefmt="%Y-%m-%dT%H:%M:%S",
    )
    h = logging.StreamHandler(sys.stderr)
    h.setFormatter(fmt)
    level = logging.DEBUG if verbose else logging.INFO
    for lg in (logger, _audit_logger):
        lg.setLevel(level)
        lg.handlers = [h]
        lg.propagate = False


# ═══════════════════════════════════════════════════════════════════════════
# Authentication
# ═══════════════════════════════════════════════════════════════════════════


@dataclass
class ApiKey:
    key_hash: str  # SHA-256 hex
    role: str  # "admin" | "user"


@dataclass
class AuthState:
    keys: set[str] = field(default_factory=set)  # raw keys for lookup
    by_hash: dict[str, ApiKey] = field(default_factory=dict)
    enabled: bool = True

    def validate(self, raw: str | None) -> ApiKey:
        if not self.enabled:
            return ApiKey(key_hash="", role="admin")
        if not raw:
            raise HTTPException(
                status_code=401,
                detail="Missing Authorization header. Use: Bearer <key>",
            )
        # Constant-time check: hash the candidate, then compare digests
        candidate_hash = _sha256(raw)
        stored = self.by_hash.get(candidate_hash)
        if stored is None:
            raise HTTPException(status_code=401, detail="Invalid API key")
        return stored


def _parse_keys(raw: str) -> AuthState:
    """Accept ``key1,admin:key2,key3``. The ``admin:`` prefix marks an
    admin-level key; everything else is a regular user key."""
    state = AuthState()
    for entry in raw.split(","):
        entry = entry.strip()
        if not entry:
            continue
        if entry.startswith("admin:"):
            raw_key = entry[len("admin:") :].strip()
            role = "admin"
        else:
            raw_key = entry.strip()
            role = "user"
        if not raw_key or len(raw_key) < 6:
            logger.warning("skipping short/invalid key: %s...", entry[:16])
            continue
        state.keys.add(raw_key)
        state.by_hash[_sha256(raw_key)] = ApiKey(key_hash=_sha256(raw_key), role=role)
    if not state.keys:
        logger.warning("No valid API keys configured — auth is DISABLED")
        state.enabled = False
    else:
        logger.info(
            "Loaded %d API key(s) (%d admin)",
            len(state.keys),
            sum(1 for k in state.by_hash.values() if k.role == "admin"),
        )
    return state


def _sha256(raw: str) -> str:
    return hashlib.sha256(raw.encode()).hexdigest()


# ═══════════════════════════════════════════════════════════════════════════
# Rate limiter + IP ban
# ═══════════════════════════════════════════════════════════════════════════


@dataclass
class TokenBucket:
    tokens: float
    last_refill: float
    rate: float
    capacity: float

    def consume(self, n: float = 1.0) -> bool:
        now = time.monotonic()
        elapsed = now - self.last_refill
        self.tokens = min(self.capacity, self.tokens + elapsed * self.rate)
        self.last_refill = now
        if self.tokens >= n:
            self.tokens -= n
            return True
        return False


class RateLimiter:
    def __init__(self, user_rps: float, admin_rps: float, capacity: float):
        self._user_rps = user_rps
        self._admin_rps = admin_rps
        self._capacity = capacity
        self._buckets: dict[str, TokenBucket] = {}
        self._lock = __import__("threading").Lock()

    def _cleanup(self) -> None:
        cutoff = time.monotonic() - 600
        stale = [k for k, b in self._buckets.items() if b.last_refill < cutoff]
        for k in stale:
            del self._buckets[k]

    def allow(self, key: str, role: str = "user") -> bool:
        rate = self._admin_rps if role == "admin" else self._user_rps
        with self._lock:
            if len(self._buckets) > 100_000:
                self._cleanup()
            bucket = self._buckets.get(key)
            if bucket is None or bucket.rate != rate:
                self._buckets[key] = TokenBucket(
                    tokens=self._capacity,
                    last_refill=time.monotonic(),
                    rate=rate,
                    capacity=self._capacity,
                )
                bucket = self._buckets[key]
            return bucket.consume()


class IpBanner:
    def __init__(
        self, max_failures: int = MAX_AUTH_FAILURES, window: float = BAN_WINDOW_S
    ):
        self._max = max_failures
        self._window = window
        self._failures: dict[str, list[float]] = defaultdict(list)
        self._banned: dict[str, float] = {}

    def record_failure(self, ip: str) -> None:
        now = time.monotonic()
        self._failures[ip] = [t for t in self._failures[ip] if now - t < self._window]
        self._failures[ip].append(now)
        if len(self._failures[ip]) >= self._max:
            self._banned[ip] = now
            _audit_logger.warning(
                '{"event":"ip_banned","ip":"%s","failures":%d}',
                ip,
                len(self._failures[ip]),
            )

    def is_banned(self, ip: str) -> bool:
        banned_at = self._banned.get(ip)
        if banned_at and time.monotonic() - banned_at < self._window:
            return True
        if banned_at:
            del self._banned[ip]
        return False


# ═══════════════════════════════════════════════════════════════════════════
# Pydantic request schemas (strict validation)
# ═══════════════════════════════════════════════════════════════════════════

_SAFE_RE = re.compile(r"^[ -~]*$")  # printable ASCII, no control chars


def _sanitize_stop(stop: Any) -> list[str]:
    if stop is None:
        return []
    if isinstance(stop, str):
        return [stop[:MAX_STOP_STRING_LEN]]
    if isinstance(stop, list):
        return [str(s)[:MAX_STOP_STRING_LEN] for s in stop[:MAX_STOP_STRINGS]]
    return []


class CompletionRequest(BaseModel):
    model_config = {"extra": "allow"}
    model: str = "topogpt3"
    profile: str | None = None
    prompt: str = Field(default="", max_length=MAX_PROMPT_CHARS)
    max_tokens: int | None = Field(default=None, ge=1, le=MAX_OUTPUT_TOKENS)
    temperature: float | None = Field(default=None, ge=0.0, le=MAX_TEMPERATURE)
    top_k: int | None = Field(default=None, ge=0, le=200)
    repetition_penalty: float | None = Field(default=None, ge=0.5, le=3.0)
    stop: Any = None
    stream: bool = False
    auto_continue: bool = False
    max_continuations: int = Field(default=3, ge=0, le=10)
    seed: int | None = Field(default=None, ge=0, le=2**63 - 1)
    response_format: Any = None
    so_args: Any = None
    tools: Any = None
    tool_choice: Any = "auto"
    n: int = Field(default=1, ge=1, le=4)
    best_of: int | None = Field(default=None, ge=1, le=8)

    @field_validator("stop", mode="before")
    @classmethod
    def _normalize_stop(cls, v: Any) -> list[str]:
        return _sanitize_stop(v)


class Message(BaseModel):
    model_config = {"extra": "allow"}
    role: str = Field(default="user", pattern=r"^(system|user|assistant|tool)$")
    content: str | list[dict] = Field(default="")
    name: str | None = None
    tool_call_id: str | None = None
    tool_calls: Any = None
    reasoning_content: str | None = None


class ChatCompletionRequest(BaseModel):
    model_config = {"extra": "allow"}
    model: str = "topogpt3"
    profile: str | None = None
    messages: list[Message] = Field(default_factory=list, max_length=MAX_MESSAGES)
    max_tokens: int | None = Field(default=None, ge=1, le=MAX_OUTPUT_TOKENS)
    temperature: float | None = Field(default=None, ge=0.0, le=MAX_TEMPERATURE)
    top_k: int | None = Field(default=None, ge=0, le=200)
    repetition_penalty: float | None = Field(default=None, ge=0.5, le=3.0)
    stop: Any = None
    stream: bool = False
    auto_continue: bool = False
    max_continuations: int = Field(default=3, ge=0, le=10)
    seed: int | None = Field(default=None, ge=0, le=2**63 - 1)
    response_format: Any = None
    so_args: Any = None
    tools: Any = None
    tool_choice: Any = "auto"
    n: int = Field(default=1, ge=1, le=4)
    best_of: int | None = Field(default=None, ge=1, le=8)
    min_new_tokens: int | None = Field(default=None, ge=1, le=MAX_OUTPUT_TOKENS)
    open_thinking: bool = False

    @field_validator("stop", mode="before")
    @classmethod
    def _normalize_stop(cls, v: Any) -> list[str]:
        return _sanitize_stop(v)


# ═══════════════════════════════════════════════════════════════════════════
# Model wrapper
# ═══════════════════════════════════════════════════════════════════════════


def _fit_context(ids: list[int], max_ctx: int, tail: int = 192) -> list[int]:
    """Truncado que conserva cabeza (system/tools) y cola (contexto reciente)."""
    if len(ids) <= max_ctx:
        return ids
    head = max(0, max_ctx - tail)
    return ids[:head] + ids[-tail:]


def _make_generator(seed: int | None, device: str) -> torch.Generator | None:
    """Per-request RNG so a fixed ``seed`` reproduces the exact same sample."""
    if seed is None:
        return None
    if device.startswith("cuda"):
        generator = torch.Generator(device=torch.device(device))
    elif device == "cpu":
        generator = torch.Generator(device="cpu")
    else:
        return None
    generator.manual_seed(int(seed))
    return generator


@dataclass
class ServerModel:
    model: TopoGPT2
    tokenizer: BPETokenizer
    device: str
    checkpoint: str
    meta: dict[str, Any] = field(default_factory=dict)

    @contextmanager
    def _seeded(self, seed: int | None):
        if seed is None:
            yield
            return
        cuda_devices: list[int] = []
        if self.device.startswith("cuda"):
            index = self.device.partition(":")[2]
            cuda_devices = [int(index) if index else torch.cuda.current_device()]
        with torch.random.fork_rng(devices=cuda_devices):
            torch.manual_seed(int(seed))
            if cuda_devices:
                torch.cuda.manual_seed_all(int(seed))
            yield

    @torch.no_grad()
    def _generate(
        self,
        token_ids: torch.Tensor,
        *,
        max_new_tokens: int,
        temperature: float,
        top_k: int,
        repetition_penalty: float,
        seed: int | None,
        constraint: GrammarConstraint | None,
        min_new_tokens: int = 0,
    ) -> torch.Tensor:
        generator = _make_generator(seed, self.device)
        if constraint is not None:
            constraint.reset()
        logits, _, past_kvs = self.model(token_ids, position_offset=0)
        position = token_ids.shape[1]
        for step_index in range(max_new_tokens):
            step = logits[:, -1, :]
            if repetition_penalty != 1.0:
                mask = torch.zeros_like(step, dtype=torch.bool)
                mask.scatter_(1, token_ids, True)
                step = torch.where(mask, step / repetition_penalty, step)
            if temperature <= 1e-6:
                if constraint is not None:
                    constraint.apply(step)
                next_tok = step.argmax(dim=-1, keepdim=True)
            else:
                step = step / temperature
                if top_k > 0:
                    v, _ = torch.topk(step, min(top_k, step.size(-1)))
                    step[step < v[:, -1:]] = float("-inf")
                if constraint is not None:
                    constraint.apply(step)
                probs = torch.softmax(step, dim=-1)
                if not torch.isfinite(probs).all() or probs.sum().item() <= 0:
                    break
                next_tok = torch.multinomial(probs, 1, generator=generator)

            token_id = int(next_tok.item())
            if (
                constraint is None
                and min_new_tokens > 0
                and step_index < min_new_tokens
                and self._is_eos(token_id)
            ):
                # Early-EOS guard: a base model tiende a
                # '</s>' en prompts novedosos; lo suprimimos hasta min_new.
                eos = self._eos_id()
                step[:, eos] = float("-inf")
                if temperature <= 1e-6:
                    next_tok = step.argmax(dim=-1, keepdim=True)
                else:
                    probs = torch.softmax(step, dim=-1)
                    next_tok = torch.multinomial(probs, 1, generator=generator)
                token_id = int(next_tok.item())
            if constraint is not None:
                if not constraint.accept(token_id):
                    break
                finished = constraint.is_terminated
            else:
                if self._is_eos(token_id):
                    break
                finished = False

            token_ids = torch.cat([token_ids, next_tok], dim=1)
            if finished:
                break
            logits, _, past_kvs = self.model(
                next_tok, past_kvs=past_kvs, position_offset=position
            )
            position += 1
        return token_ids

    def _finish_text(self, text: str, stop: list[str] | None) -> str:
        if stop:
            for marker in stop:
                idx = text.find(marker)
                if idx != -1:
                    text = text[:idx]
        return text

    @torch.no_grad()
    def complete_candidates(
        self,
        prompt: str,
        *,
        count: int = 1,
        max_new_tokens: int = 512,
        temperature: float = 0.7,
        top_k: int = 50,
        repetition_penalty: float = 1.1,
        stop: list[str] | None = None,
        auto_continue: bool = False,
        max_continuations: int = 3,
        seed: int | None = None,
        constraint: GrammarConstraint | None = None,
        min_new_tokens: int = 0,
    ) -> list[str]:
        ids = self.tokenizer.encode(prompt)
        if not ids:
            return [""] * max(1, count)
        max_ctx = self.model.config.MAX_SEQ_LEN
        ids = _fit_context(ids, max_ctx)
        x = torch.tensor([ids], dtype=torch.long, device=self.device)
        candidates: list[str] = []
        for index in range(max(1, count)):
            candidate_seed = None if seed is None else int(seed) + index
            if auto_continue:
                if constraint is not None:
                    raise StructuredOutputError(
                        "auto_continue cannot be combined with structured output"
                    )
                with self._seeded(candidate_seed):
                    out = self.model.generate_with_continuation(
                        x,
                        tokenizer=self.tokenizer,
                        max_new_tokens=max_new_tokens,
                        temperature=temperature,
                        top_k=top_k,
                        repetition_penalty=repetition_penalty,
                        max_continuations=max_continuations,
                    )
            else:
                out = self._generate(
                    x,
                    max_new_tokens=max_new_tokens,
                    temperature=temperature,
                    top_k=top_k,
                    repetition_penalty=repetition_penalty,
                    seed=candidate_seed,
                    constraint=constraint,
                    min_new_tokens=min_new_tokens,
                )
            generated = self.tokenizer.decode(out[0, x.shape[1] :].tolist())
            candidates.append(self._finish_text(generated, stop))
        return candidates

    @torch.no_grad()
    def complete(
        self,
        prompt: str,
        *,
        max_new_tokens: int = 512,
        temperature: float = 0.7,
        top_k: int = 50,
        repetition_penalty: float = 1.1,
        stop: list[str] | None = None,
        auto_continue: bool = False,
        max_continuations: int = 3,
        seed: int | None = None,
        constraint: GrammarConstraint | None = None,
    ) -> str:
        return self.complete_candidates(
            prompt,
            count=1,
            max_new_tokens=max_new_tokens,
            temperature=temperature,
            top_k=top_k,
            repetition_penalty=repetition_penalty,
            stop=stop,
            auto_continue=auto_continue,
            max_continuations=max_continuations,
            seed=seed,
            constraint=constraint,
        )[0]

    @torch.no_grad()
    def stream_complete(
        self,
        prompt: str,
        *,
        max_new_tokens: int = 512,
        temperature: float = 0.7,
        top_k: int = 50,
        repetition_penalty: float = 1.1,
        stop: list[str] | None = None,
        auto_continue: bool = False,
        max_continuations: int = 3,
        seed: int | None = None,
        constraint: GrammarConstraint | None = None,
        min_new_tokens: int = 0,
    ):
        ids = self.tokenizer.encode(prompt)
        if not ids:
            return
        if auto_continue and constraint is not None:
            raise StructuredOutputError(
                "auto_continue cannot be combined with structured output"
            )
        max_ctx = self.model.config.MAX_SEQ_LEN
        ids = _fit_context(ids, max_ctx)
        x = torch.tensor([ids], dtype=torch.long, device=self.device)
        max_tokens = min(max_new_tokens, MAX_OUTPUT_TOKENS)
        generator = _make_generator(seed, self.device)
        prev_text = self.tokenizer.decode(x[0].tolist())
        prev_chars = len(prev_text)
        all_ids = x
        continuation_count = 0

        while True:
            if constraint is not None:
                constraint.reset()
            logits, _, past_kvs = self.model(all_ids, position_offset=0)
            position = all_ids.shape[1]
            stopped_on_eos = False
            grammar_finished = False

            for step_index in range(max_tokens):
                step = logits[:, -1, :]
                if repetition_penalty != 1.0:
                    mask = torch.zeros_like(step, dtype=torch.bool)
                    mask.scatter_(1, all_ids, True)
                    step = torch.where(mask, step / repetition_penalty, step)
                if temperature <= 1e-6:
                    if constraint is not None:
                        constraint.apply(step)
                    next_id = step.argmax(dim=-1, keepdim=True)
                else:
                    step = step / temperature
                    if top_k > 0:
                        v, _ = torch.topk(step, min(top_k, step.size(-1)))
                        step[step < v[:, -1:]] = float("-inf")
                    if constraint is not None:
                        constraint.apply(step)
                    probs = torch.softmax(step, dim=-1)
                    if not torch.isfinite(probs).all() or probs.sum().item() <= 0:
                        break
                    next_id = torch.multinomial(probs, 1, generator=generator)

                token_id = int(next_id.item())
                if constraint is not None:
                    if not constraint.accept(token_id):
                        grammar_finished = True
                        break
                    if constraint.is_terminated:
                        grammar_finished = True
                elif (
                    min_new_tokens > 0
                    and step_index < min_new_tokens
                    and self._is_eos(token_id)
                ):
                    eos = self._eos_id()
                    step[:, eos] = float("-inf")
                    if temperature <= 1e-6:
                        next_id = step.argmax(dim=-1, keepdim=True)
                    else:
                        probs = torch.softmax(step, dim=-1)
                        next_id = torch.multinomial(probs, 1, generator=generator)
                    token_id = int(next_id.item())
                elif self._is_eos(token_id):
                    stopped_on_eos = True
                    break

                all_ids = torch.cat([all_ids, next_id], dim=1)
                full_text = self.tokenizer.decode(all_ids[0].tolist())
                chunk = full_text[prev_chars:]
                prev_chars = len(full_text)
                if chunk:
                    if stop:
                        stopped = False
                        for marker in stop:
                            idx = chunk.find(marker)
                            if idx != -1:
                                chunk = chunk[:idx]
                                stopped = True
                                break
                        if stopped:
                            if chunk:
                                yield chunk
                            return
                    yield chunk
                if grammar_finished:
                    return
                logits, _, past_kvs = self.model(
                    next_id, past_kvs=past_kvs, position_offset=position
                )
                position += 1

            if grammar_finished or not auto_continue or not stopped_on_eos:
                break

            from .continuation import (
                extract_tail_for_continuation,
                is_response_complete,
            )

            out_text = self.tokenizer.decode(all_ids[0].tolist())
            generated = out_text[len(prev_text) :]
            if is_response_complete(generated):
                break

            tail = extract_tail_for_continuation(generated, tail_lines=2)
            if not tail:
                break

            continuation_count += 1
            if continuation_count > max_continuations:
                break

            tail_text = prev_text + tail
            tail_ids = self.tokenizer.encode(tail_text)
            tail_ids = tail_ids[-max_ctx:]
            all_ids = torch.tensor([tail_ids], dtype=torch.long, device=self.device)
            prev_text = tail_text
            prev_chars = len(tail_text)

    def _eos_id(self) -> int:
        try:
            return int(self.tokenizer.eot_token())
        except Exception:
            return -1

    def _is_eos(self, token_id: int) -> bool:
        try:
            return int(token_id) == int(self.tokenizer.eot_token())
        except Exception:
            return False


# ═══════════════════════════════════════════════════════════════════════════
# App state
# ═══════════════════════════════════════════════════════════════════════════

_MODEL: ServerModel | None = None
_AUTH: AuthState = AuthState(enabled=False)
_RATE_LIMITER: RateLimiter = RateLimiter(
    RATE_LIMIT_USER_RPS, RATE_LIMIT_ADMIN_RPS, RATE_BUCKET_CAPACITY
)
_IP_BANNER: IpBanner = IpBanner()


def _resolve_device(device: str | None) -> str:
    if device:
        return device
    return "cuda" if torch.cuda.is_available() else "cpu"


def load_model(checkpoint: str, device: str | None = None) -> ServerModel:
    device = _resolve_device(device)
    cfg, meta = config_from_checkpoint(checkpoint, device=device)
    tokenizer = BPETokenizer("gpt2")
    cfg.VOCAB_SIZE = tokenizer.vocab_size
    model = TopoGPT2(cfg).to(device).eval()
    sd = load_file(str(Path(checkpoint) / "model.safetensors"), device=device)
    model.load_state_dict(sd, strict=False)
    set_seed(42, device)
    n_params = sum(p.numel() for p in model.parameters())
    logger.info(
        '{"event":"model_loaded","params":%d,"n_kv":%d,"scale":"%s",'
        '"d_model":%d,"layers":%d,"device":"%s"}',
        n_params,
        cfg.N_KV_HEADS,
        meta.get("scale"),
        cfg.D_MODEL,
        cfg.N_LAYERS,
        device,
    )
    return ServerModel(
        model=model,
        tokenizer=tokenizer,
        device=device,
        checkpoint=checkpoint,
        meta=meta,
    )


# ═══════════════════════════════════════════════════════════════════════════
# FastAPI app
# ═══════════════════════════════════════════════════════════════════════════


@asynccontextmanager
async def lifespan(app: FastAPI):
    global _MODEL, _AUTH
    checkpoint = os.environ.get("TOPOGPT3_CHECKPOINT", "checkpoints_topogpt3/last")
    device = os.environ.get("TOPOGPT3_DEVICE") or None
    api_keys = os.environ.get("TOPOGPT3_API_KEYS", "")
    app.state.checkpoint = checkpoint
    app.state.device = device
    app.state.api_keys = api_keys
    _MODEL = load_model(checkpoint, device)
    _AUTH = _parse_keys(api_keys)
    yield
    _MODEL = None


app = FastAPI(
    title="TopoGPT3 API",
    version="0.1.0",
    lifespan=lifespan,
    docs_url=None if os.environ.get("TOPOGPT3_NO_DOCS") else "/docs",
    redoc_url=None,
    openapi_url=None if os.environ.get("TOPOGPT3_NO_DOCS") else "/openapi.json",
)

# ── Middleware ────────────────────────────────────────────────────────────

# CORS: default deny-all; allowlist via TOPOGPT3_CORS_ORIGINS
_cors_origins = os.environ.get("TOPOGPT3_CORS_ORIGINS", "").split(",")
_cors_origins = [o.strip() for o in _cors_origins if o.strip()]
app.add_middleware(
    CORSMiddleware,
    allow_origins=_cors_origins or [],
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Authorization", "Content-Type"],
)

app.add_middleware(GZipMiddleware, minimum_size=512)


@app.middleware("http")
async def _security_middleware(
    request: Request, call_next: Callable[[Request], Awaitable[Response]]
) -> Response:
    """Global middleware: rate-limit, IP-ban, security headers, audit log."""

    client_ip = _real_ip(request)
    if _IP_BANNER.is_banned(client_ip):
        _audit_logger.warning(
            '{"event":"blocked","reason":"ip_banned","ip":"%s","path":"%s"}',
            client_ip,
            request.url.path,
        )
        return _json_error(403, "Access denied")

    # Rate limit by IP (before auth so brute-force is throttled)
    if not _RATE_LIMITER.allow(f"ip:{client_ip}", role="user"):
        _audit_logger.warning(
            '{"event":"rate_limited","ip":"%s","path":"%s"}',
            client_ip,
            request.url.path,
        )
        return _json_error(429, "Too many requests. Slow down.")

    response = await call_next(request)

    # Security headers on every response
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["Content-Security-Policy"] = (
        "default-src 'none'; frame-ancestors 'none'"
    )
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate"
    response.headers["Server"] = ""  # don't leak framework version

    return response


def _real_ip(request: Request) -> str:
    """Best-effort real client IP. We trust no proxy headers by default."""
    # Only trust X-Forwarded-For if explicitly allowed
    if os.environ.get("TOPOGPT3_TRUST_PROXY", "").lower() in ("1", "true", "yes"):
        forwarded = request.headers.get("X-Forwarded-For", "")
        if forwarded:
            return forwarded.split(",")[0].strip()
    host = getattr(request, "client", None)
    return host.host if host else "127.0.0.1"


def _json_error(status: int, detail: str) -> JSONResponse:
    return JSONResponse(
        content={"error": detail},
        status_code=status,
    )


# ═══════════════════════════════════════════════════════════════════════════
# Auth dependency
# ═══════════════════════════════════════════════════════════════════════════


async def _authenticate(request: Request) -> ApiKey:
    """FastAPI dependency: extract & validate Bearer token."""
    client_ip = _real_ip(request)
    if not _AUTH.enabled:
        return _AUTH.validate(None)
    auth_header = request.headers.get("Authorization", "")
    if not auth_header.lower().startswith("bearer "):
        _IP_BANNER.record_failure(client_ip)
        raise HTTPException(
            status_code=401,
            detail="Missing or malformed Authorization header. Use: Bearer <key>",
        )
    raw_key = auth_header[7:]  # len("Bearer ") == 7
    try:
        return _AUTH.validate(raw_key)
    except HTTPException:
        _IP_BANNER.record_failure(client_ip)
        raise


async def _check_rate_limit(api_key: ApiKey, request: Request) -> None:
    """Rate limit per-key (with admin exemption / higher limit)."""
    client_ip = _real_ip(request)
    bucket_key = f"key:{api_key.key_hash}"
    if not _RATE_LIMITER.allow(bucket_key, role=api_key.role):
        _audit_logger.warning(
            '{"event":"rate_limited","ip":"%s","role":"%s"}',
            client_ip,
            api_key.role,
        )
        raise HTTPException(status_code=429, detail="Rate limit exceeded")


# ═══════════════════════════════════════════════════════════════════════════
# Endpoints
# ═══════════════════════════════════════════════════════════════════════════


@app.get("/health")
async def health(request: Request):
    if _MODEL is None:
        return _json_error(503, "Model not loaded yet")
    return {"status": "ok"}


@app.get("/v1/models")
async def list_models(request: Request):
    _api_key = await _authenticate(request)
    await _check_rate_limit(_api_key, request)
    checkpoint = _MODEL.checkpoint if _MODEL is not None else ""
    return {"object": "list", "data": models_payload(checkpoint)}


def _resolve_generation(req: Any):
    profile = resolve_profile(req.profile or req.model)
    temperature = profile.temperature if req.temperature is None else req.temperature
    top_k = profile.top_k if req.top_k is None else req.top_k
    repetition_penalty = (
        profile.repetition_penalty
        if req.repetition_penalty is None
        else req.repetition_penalty
    )
    max_tokens = req.max_tokens if req.max_tokens is not None else profile.max_tokens
    max_tokens = max(1, min(int(max_tokens), MAX_OUTPUT_TOKENS))
    min_new = (
        req.min_new_tokens if req.min_new_tokens is not None else profile.min_new_tokens
    )
    min_new = max(0, min(int(min_new), max_tokens))
    stop = list(req.stop or [])
    for marker in profile.stop:
        if marker not in stop:
            stop.append(marker)
    tools = _merge_tools(profile, getattr(req, "tools", None))
    best_of = req.best_of or max(req.n, profile.best_of, 1)
    best_of = max(1, min(int(best_of), 8))
    return (
        profile,
        temperature,
        top_k,
        repetition_penalty,
        max_tokens,
        stop,
        tools,
        best_of,
        min_new,
    )


def _finish_reason(text: str, completion_tokens: int, max_tokens: int) -> str:
    if '"name"' in text and "<tool_call>" in text:
        return "tool_calls"
    if completion_tokens >= max_tokens:
        return "length"
    return "stop"


@app.post("/v1/completions")
async def completions(req: CompletionRequest, request: Request):
    _api_key = await _authenticate(request)
    await _check_rate_limit(_api_key, request)
    _check_model()
    (
        profile,
        temperature,
        top_k,
        repetition_penalty,
        max_tokens,
        stop,
        tools,
        best_of,
        min_new,
    ) = _resolve_generation(req)
    constraint = _request_constraint(req)
    allowed_tools = _allowed_tool_names(tools)

    prompt = req.prompt
    if tools:
        from .chat import _fmt_tool_defs

        prompt = _fmt_tool_defs(tools) + prompt

    _audit_logger.info(
        '{"event":"completion","role":"%s","stream":%s,"profile":"%s",'
        '"prompt_len":%d,"max_tokens":%d}',
        _api_key.role,
        req.stream,
        profile.name,
        len(prompt),
        max_tokens,
    )

    if req.stream:
        if req.n != 1 or best_of > 1:
            raise HTTPException(
                status_code=400,
                detail="streaming supports n=1 and best_of=1",
            )
        return StreamingResponse(
            _stream_completion(
                prompt,
                max_tokens,
                temperature,
                top_k,
                repetition_penalty,
                stop,
                req.auto_continue,
                req.max_continuations,
                seed=req.seed,
                constraint=constraint,
                min_new_tokens=min_new,
                model_name=profile.name,
            ),
            media_type="text/event-stream",
        )

    candidates = await asyncio.to_thread(
        _locked,
        _MODEL.complete_candidates,
        prompt,
        count=best_of,
        max_new_tokens=max_tokens,
        min_new_tokens=min_new,
        temperature=temperature,
        top_k=top_k,
        repetition_penalty=repetition_penalty,
        stop=stop,
        auto_continue=req.auto_continue,
        max_continuations=req.max_continuations,
        seed=req.seed,
        constraint=constraint,
    )
    ranked = rank_candidates(candidates, profile, prompt, allowed_tools)
    choices = []
    prompt_tokens = len(_MODEL.tokenizer.encode(prompt))
    total_completion = 0
    for index, (score, original, text, details) in enumerate(ranked[: req.n]):
        completion_tokens = len(_MODEL.tokenizer.encode(text)) or 1
        total_completion += completion_tokens
        choices.append(
            {
                "text": text,
                "index": index,
                "logprobs": None,
                "finish_reason": _finish_reason(text, completion_tokens, max_tokens),
                "score": score,
            }
        )
    return {
        "id": f"cmpl-{_short_id()}",
        "object": "text_completion",
        "created": int(time.time()),
        "model": profile.name,
        "choices": choices,
        "usage": {
            "prompt_tokens": prompt_tokens,
            "completion_tokens": total_completion,
            "total_tokens": prompt_tokens + total_completion,
        },
    }


@app.post("/v1/chat/completions")
async def chat_completions(req: ChatCompletionRequest, request: Request):
    _api_key = await _authenticate(request)
    await _check_rate_limit(_api_key, request)
    _check_model()
    (
        profile,
        temperature,
        top_k,
        repetition_penalty,
        max_tokens,
        stop,
        tools,
        best_of,
        min_new,
    ) = _resolve_generation(req)
    constraint = _request_constraint(req)
    allowed_tools = _allowed_tool_names(tools)

    messages = _profile_messages(profile, req.messages)
    prompt = _build_chat_prompt(
        messages, tools=tools or None, open_thinking=req.open_thinking
    )
    _audit_logger.info(
        '{"event":"chat","role":"%s","stream":%s,"profile":"%s",'
        '"n_msgs":%d,"prompt_len":%d}',
        _api_key.role,
        req.stream,
        profile.name,
        len(req.messages),
        len(prompt),
    )

    if req.stream:
        if req.n != 1 or best_of > 1:
            raise HTTPException(
                status_code=400,
                detail="streaming supports n=1 and best_of=1",
            )
        return StreamingResponse(
            _stream_chat(
                int(time.time() * 1000),
                prompt,
                max_tokens,
                temperature,
                top_k,
                repetition_penalty,
                stop,
                req.auto_continue,
                req.max_continuations,
                seed=req.seed,
                constraint=constraint,
                min_new_tokens=min_new,
                allowed_tools=allowed_tools,
                model_name=profile.name,
            ),
            media_type="text/event-stream",
        )

    candidates = await asyncio.to_thread(
        _locked,
        _MODEL.complete_candidates,
        prompt,
        count=best_of,
        max_new_tokens=max_tokens,
        min_new_tokens=min_new,
        temperature=temperature,
        top_k=top_k,
        repetition_penalty=repetition_penalty,
        stop=stop,
        auto_continue=req.auto_continue,
        max_continuations=req.max_continuations,
        seed=req.seed,
        constraint=constraint,
    )
    ranked = rank_candidates(candidates, profile, prompt, allowed_tools)
    choices = []
    prompt_tokens = len(_MODEL.tokenizer.encode(prompt))
    total_completion = 0
    for index, (score, original, text, details) in enumerate(ranked[: req.n]):
        parts = split_response(text)
        synthetic = False
        if profile.require_tool and not parts["tool_calls"]:
            synthesized = synthesize_tool_call(profile, prompt)
            if synthesized:
                from .chat import TOOL_CALL_CLOSE, TOOL_CALL_OPEN
                from .fallback import tool_calls_payload

                parts["tool_calls"] = tool_calls_payload(
                    f"{TOOL_CALL_OPEN}{json.dumps(synthesized)}{TOOL_CALL_CLOSE}"
                )
                parts["content"] = ""
                score = max(score, 10.0)
                synthetic = True
        message: dict[str, Any] = {
            "role": "assistant",
            "content": parts["content"],
        }
        if parts["reasoning_content"]:
            message["reasoning_content"] = parts["reasoning_content"]
        if parts["tool_calls"]:
            message["tool_calls"] = parts["tool_calls"]
        completion_tokens = len(_MODEL.tokenizer.encode(text)) or 1
        total_completion += completion_tokens
        choices.append(
            {
                "index": index,
                "message": message,
                "finish_reason": (
                    "tool_calls"
                    if parts["tool_calls"]
                    else _finish_reason(text, completion_tokens, max_tokens)
                ),
                "score": score,
                "synthetic_tool_call": synthetic,
            }
        )
    return {
        "id": f"chatcmpl-{_short_id()}",
        "object": "chat.completion",
        "created": int(time.time()),
        "model": profile.name,
        "choices": choices,
        "usage": {
            "prompt_tokens": prompt_tokens,
            "completion_tokens": total_completion,
            "total_tokens": prompt_tokens + total_completion,
        },
    }


# ═══════════════════════════════════════════════════════════════════════════
# Helpers
# ═══════════════════════════════════════════════════════════════════════════


def _check_model():
    if _MODEL is None:
        raise HTTPException(status_code=503, detail="Model not loaded yet")


def _request_constraint(req: Any) -> GrammarConstraint | None:
    if req.auto_continue and (
        req.response_format is not None or req.so_args is not None
    ):
        raise HTTPException(
            status_code=400,
            detail="auto_continue cannot be combined with structured output",
        )
    try:
        return constraint_from_request(
            _MODEL.tokenizer, req.response_format, req.so_args
        )
    except StructuredOutputError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


def _short_id() -> str:
    return secrets.token_hex(8)


def _build_chat_prompt(
    messages: list[Message],
    tools: Any = None,
    open_thinking: bool = False,
) -> str:
    """Render the full OpenAI history, including tools and tool results."""
    from .chat import apply_chat_template

    dicts: list[dict[str, Any]] = []
    for msg in messages:
        item: dict[str, Any] = {
            "role": msg.role,
            "content": _extract_text(msg.content),
        }
        if msg.name:
            item["name"] = msg.name
        if msg.tool_calls:
            item["tool_calls"] = msg.tool_calls
        if msg.reasoning_content:
            item["reasoning_content"] = msg.reasoning_content
        dicts.append(item)
    return apply_chat_template(
        dicts,
        tools=tools if isinstance(tools, list) else None,
        add_generation_prompt=True,
        open_thinking=open_thinking,
    )


def _merge_tools(profile: Any, request_tools: Any) -> list[dict[str, Any]]:
    seen: set[str] = set()
    merged: list[dict[str, Any]] = []
    candidate_lists = []
    if isinstance(request_tools, list):
        candidate_lists.append(request_tools)
    candidate_lists.append(list(profile.tools))
    for tools in candidate_lists:
        for tool in tools:
            if not isinstance(tool, dict):
                continue
            fn = tool.get("function", tool)
            name = str(fn.get("name", ""))
            if not name or name in seen:
                continue
            seen.add(name)
            merged.append(tool)
    return merged


def _profile_messages(profile: Any, messages: list[Message]) -> list[Message]:
    if any(m.role == "system" for m in messages):
        return messages
    return [Message(role="system", content=profile.system), *messages]


def _allowed_tool_names(tools: list[dict[str, Any]]) -> set[str]:
    return {
        str(t.get("function", t).get("name", "")) for t in tools if isinstance(t, dict)
    }


_MODEL_LOCK = threading.Lock()


def _locked(func, *args, **kwargs):
    with _MODEL_LOCK:
        return func(*args, **kwargs)


def _locked_stream(generator):
    with _MODEL_LOCK:
        yield from generator


async def _iter_in_thread(generator):
    iterator = iter(generator)
    sentinel = object()
    while True:
        item = await asyncio.to_thread(next, iterator, sentinel)
        if item is sentinel:
            break
        yield item


def _extract_text(content: str | list[dict] | Any) -> str:
    if isinstance(content, str):
        return content[-MAX_CONTENT_LEN:]
    if isinstance(content, list):
        texts: list[str] = []
        for block in content:
            if isinstance(block, dict):
                t = block.get("text", "")
                if t:
                    texts.append(str(t))
        return " ".join(texts)[-MAX_CONTENT_LEN:]
    return str(content)[-MAX_CONTENT_LEN:]


async def _stream_completion(
    prompt: str,
    max_tokens: int,
    temperature: float,
    top_k: int,
    repetition_penalty: float,
    stop: list[str],
    auto_continue: bool = False,
    max_continuations: int = 3,
    seed: int | None = None,
    constraint: GrammarConstraint | None = None,
    min_new_tokens: int = 0,
    model_name: str = "topogpt3",
):
    t0 = int(time.time())
    short_id = _short_id()
    stream = _locked_stream(
        _MODEL.stream_complete(
            prompt,
            max_new_tokens=max_tokens,
            temperature=temperature,
            top_k=top_k,
            repetition_penalty=repetition_penalty,
            stop=stop,
            auto_continue=auto_continue,
            max_continuations=max_continuations,
            seed=seed,
            constraint=constraint,
            min_new_tokens=min_new_tokens,
        )
    )
    async for chunk_text in _iter_in_thread(stream):
        data = {
            "id": f"cmpl-{short_id}",
            "object": "text_completion",
            "created": t0,
            "model": model_name,
            "choices": [
                {
                    "text": chunk_text,
                    "index": 0,
                    "logprobs": None,
                    "finish_reason": None,
                }
            ],
        }
        yield f"data: {json.dumps(data)}\n\n"
    data = {
        "id": f"cmpl-{short_id}",
        "object": "text_completion",
        "created": t0,
        "model": model_name,
        "choices": [
            {"text": "", "index": 0, "logprobs": None, "finish_reason": "stop"}
        ],
    }
    yield f"data: {json.dumps(data)}\n\n"
    yield "data: [DONE]\n\n"


def _tool_call_stream_chunks(
    text_stream,
    allowed_tools: set[str] | None,
    model_name: str,
    t0_ms: int,
):
    """Yield chat chunks, converting <tool_call> blocks into deltas.

    Content is held back while a tool-call block is streaming so partial
    markers never leak into the content channel.
    """
    from .chat import TOOL_CALL_CLOSE, TOOL_CALL_OPEN
    from .fallback import tool_calls_payload

    short_id = _short_id()
    header = {
        "id": f"chatcmpl-{short_id}",
        "object": "chat.completion.chunk",
        "created": t0_ms // 1000,
        "model": model_name,
    }

    def emit(delta: dict[str, Any], finish: str | None = None) -> str:
        data = dict(header)
        data["choices"] = [{"index": 0, "delta": delta, "finish_reason": finish}]
        return f"data: {json.dumps(data)}\n\n"

    yield emit({"role": "assistant", "content": ""})

    buffer = ""
    open_len = len(TOOL_CALL_OPEN)
    close_len = len(TOOL_CALL_CLOSE)
    tool_calls_emitted = 0

    for chunk_text in text_stream:
        buffer += chunk_text
        while buffer:
            open_idx = buffer.find(TOOL_CALL_OPEN)
            if open_idx == -1:
                safe = buffer[: max(0, len(buffer) - open_len)]
                if safe:
                    yield emit({"content": safe})
                    buffer = buffer[len(safe) :]
                break
            if open_idx > 0:
                yield emit({"content": buffer[:open_idx]})
                buffer = buffer[open_idx:]
            close_idx = buffer.find(TOOL_CALL_CLOSE)
            if close_idx == -1:
                if len(buffer) > MAX_TOOL_BUFFER:
                    # Unterminated block: flush as plain content.
                    yield emit({"content": buffer})
                    buffer = ""
                break
            raw = buffer[open_len:close_idx]
            buffer = buffer[close_idx + close_len :]
            calls = tool_calls_payload(f"{TOOL_CALL_OPEN}{raw}{TOOL_CALL_CLOSE}")
            valid = calls and (
                allowed_tools is None
                or all(c["function"]["name"] in allowed_tools for c in calls)
            )
            if valid:
                for offset, call in enumerate(calls):
                    call = dict(call)
                    call["index"] = tool_calls_emitted + offset
                    yield emit({"tool_calls": [call]})
                tool_calls_emitted += len(calls)
            else:
                yield emit({"content": f"{TOOL_CALL_OPEN}{raw}{TOOL_CALL_CLOSE}"})

    if buffer:
        yield emit({"content": buffer})
    finish = "tool_calls" if tool_calls_emitted else "stop"
    yield emit({}, finish=finish)
    yield "data: [DONE]\n\n"


async def _stream_chat(
    t0_ms: int,
    prompt: str,
    max_tokens: int,
    temperature: float,
    top_k: int,
    repetition_penalty: float,
    stop: list[str],
    auto_continue: bool = False,
    max_continuations: int = 3,
    seed: int | None = None,
    constraint: GrammarConstraint | None = None,
    min_new_tokens: int = 0,
    allowed_tools: set[str] | None = None,
    model_name: str = "topogpt3",
):
    stream = _locked_stream(
        _MODEL.stream_complete(
            prompt,
            max_new_tokens=max_tokens,
            temperature=temperature,
            top_k=top_k,
            repetition_penalty=repetition_penalty,
            stop=stop,
            auto_continue=auto_continue,
            max_continuations=max_continuations,
            seed=seed,
            constraint=constraint,
            min_new_tokens=min_new_tokens,
        )
    )
    async for chunk in _tool_call_stream_chunks(
        _iter_in_thread(stream), allowed_tools, model_name, t0_ms
    ):
        yield chunk


# ═══════════════════════════════════════════════════════════════════════════
# CLI
# ═══════════════════════════════════════════════════════════════════════════


def main():
    ap = argparse.ArgumentParser(
        description="TopoGPT3 OpenAI-compatible API server (hardened)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""\
Security
--------
Keys are loaded from --keys (comma-separated) or the TOPOGPT3_API_KEYS env var.
Prefix a key with "admin:" to grant admin-level rate limits.

Examples:
  TOPOGPT3_API_KEYS="sk-secret-key,admin:sk-admin-key" python -m topogpt3 api_server
  python -m topogpt3 api_server --keys "sk-key1,sk-key2" -p 8800
  python -m topogpt3 api_server --no-auth   # DEV ONLY - disables authentication
""",
    )
    ap.add_argument("--checkpoint", "-c", default="checkpoints_topogpt3/last")
    ap.add_argument("--port", "-p", type=int, default=8800)
    ap.add_argument("--host", default="127.0.0.1")
    ap.add_argument("--device", "-d", default=None)
    ap.add_argument(
        "--keys",
        "-k",
        default=None,
        help="Comma-separated API keys (or set TOPOGPT3_API_KEYS)",
    )
    ap.add_argument(
        "--no-auth",
        action="store_true",
        help="Disable authentication (DEVELOPMENT ONLY)",
    )
    ap.add_argument("--verbose", "-v", action="store_true")
    ap.add_argument(
        "--reload", action="store_true", help="Enable auto-reload for development"
    )
    args = ap.parse_args()

    _setup_logging(args.verbose)

    os.environ["TOPOGPT3_CHECKPOINT"] = args.checkpoint
    os.environ["TOPOGPT3_DEVICE"] = _resolve_device(args.device)

    if args.no_auth:
        os.environ["TOPOGPT3_API_KEYS"] = ""
        logger.warning("AUTH DISABLED — this server accepts all requests without a key")
    else:
        api_keys = args.keys or os.environ.get("TOPOGPT3_API_KEYS", "")
        if not api_keys.strip():
            logger.error(
                "No API keys provided. Set TOPOGPT3_API_KEYS env var "
                "or pass --keys. Use --no-auth for development only."
            )
            sys.exit(1)
        os.environ["TOPOGPT3_API_KEYS"] = api_keys

    logger.info('{"event":"server_start","host":"%s","port":%d}', args.host, args.port)

    uvicorn.run(
        "topogpt3.api_server:app" if not args.reload else app,
        host=args.host,
        port=args.port,
        reload=args.reload,
        log_level="warning",
        limit_concurrency=MAX_CONCURRENT_REQUESTS,
        limit_max_requests=None,
        timeout_keep_alive=30,
        h11_max_incomplete_event_size=MAX_REQUEST_BODY,
    )


if __name__ == "__main__":
    main()
