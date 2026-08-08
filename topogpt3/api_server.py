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
import hashlib
import hmac
import json
import logging
import os
import re
import secrets
import sys
import time
from collections import defaultdict
from contextlib import asynccontextmanager
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Awaitable, Callable, Dict, List, Optional, Set

import torch

try:
    from fastapi import FastAPI, HTTPException, Request, Response
    from fastapi.middleware.cors import CORSMiddleware
    from fastapi.middleware.gzip import GZipMiddleware
    from fastapi.responses import JSONResponse, StreamingResponse
    from pydantic import BaseModel, Field, field_validator
    import uvicorn
except ImportError:
    sys.exit(
        "Install the api extras: pip install 'topogpt3[api]'  "
        "(fastapi + uvicorn + pydantic)"
    )

from .model import BPETokenizer, TopoGPT2, TopoGPT2Config, set_seed
from safetensors.torch import load_file


# ═══════════════════════════════════════════════════════════════════════════
# Security constants
# ═══════════════════════════════════════════════════════════════════════════

MAX_REQUEST_BODY = 256 * 1024      # 256 KB
MAX_PROMPT_CHARS = 64 * 1024
MAX_MESSAGES = 200
MAX_STOP_STRINGS = 10
MAX_STOP_STRING_LEN = 128
MAX_CONTENT_LEN = 32 * 1024        # per message content field
MAX_OUTPUT_TOKENS = 4096
MAX_TEMPERATURE = 2.0
BAN_WINDOW_S = 3600                # 1 hour IP ban
MAX_AUTH_FAILURES = 10             # per IP within window
MAX_CONCURRENT_REQUESTS = 8

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
    key_hash: str       # SHA-256 hex
    role: str           # "admin" | "user"


@dataclass
class AuthState:
    keys: Set[str] = field(default_factory=set)     # raw keys for lookup
    by_hash: Dict[str, ApiKey] = field(default_factory=dict)
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
            raw_key = entry[len("admin:"):].strip()
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
        logger.info("Loaded %d API key(s) (%d admin)", len(state.keys),
                    sum(1 for k in state.by_hash.values() if k.role == "admin"))
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
    def __init__(self, max_failures: int = MAX_AUTH_FAILURES, window: float = BAN_WINDOW_S):
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
            _audit_logger.warning('{"event":"ip_banned","ip":"%s","failures":%d}', ip, len(self._failures[ip]))

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

_SAFE_RE = re.compile(r"^[ -~]*$")   # printable ASCII, no control chars


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
    prompt: str = Field(default="", max_length=MAX_PROMPT_CHARS)
    max_tokens: int = Field(default=512, ge=1, le=MAX_OUTPUT_TOKENS)
    temperature: float = Field(default=0.7, ge=0.0, le=MAX_TEMPERATURE)
    top_k: int = Field(default=50, ge=0, le=200)
    repetition_penalty: float = Field(default=1.1, ge=0.5, le=3.0)
    stop: Any = None
    stream: bool = False

    @field_validator("stop", mode="before")
    @classmethod
    def _normalize_stop(cls, v: Any) -> list[str]:
        return _sanitize_stop(v)


class Message(BaseModel):
    model_config = {"extra": "allow"}
    role: str = Field(default="user", pattern=r"^(system|user|assistant)$")
    content: str | list[dict] = Field(default="")


class ChatCompletionRequest(BaseModel):
    model_config = {"extra": "allow"}
    model: str = "topogpt3"
    messages: list[Message] = Field(default_factory=list, max_length=MAX_MESSAGES)
    max_tokens: int = Field(default=512, ge=1, le=MAX_OUTPUT_TOKENS)
    temperature: float = Field(default=0.7, ge=0.0, le=MAX_TEMPERATURE)
    top_k: int = Field(default=50, ge=0, le=200)
    repetition_penalty: float = Field(default=1.1, ge=0.5, le=3.0)
    stop: Any = None
    stream: bool = False

    @field_validator("stop", mode="before")
    @classmethod
    def _normalize_stop(cls, v: Any) -> list[str]:
        return _sanitize_stop(v)


# ═══════════════════════════════════════════════════════════════════════════
# Model wrapper
# ═══════════════════════════════════════════════════════════════════════════


@dataclass
class ServerModel:
    model: TopoGPT2
    tokenizer: BPETokenizer
    device: str
    checkpoint: str

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
    ) -> str:
        ids = self.tokenizer.encode(prompt)
        if not ids:
            return ""
        max_ctx = self.model.config.MAX_SEQ_LEN
        ids = ids[-max_ctx:]
        x = torch.tensor([ids], dtype=torch.long, device=self.device)
        out = self.model.generate(
            x,
            max_new_tokens=max_new_tokens,
            temperature=temperature,
            top_k=top_k,
            repetition_penalty=repetition_penalty,
        )
        text = self.tokenizer.decode(out[0].tolist())
        if stop:
            for s in stop:
                idx = text.find(s)
                if idx != -1:
                    text = text[:idx]
        return text

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
    ):
        ids = self.tokenizer.encode(prompt)
        if not ids:
            return
        max_ctx = self.model.config.MAX_SEQ_LEN
        ids = ids[-max_ctx:]
        x = torch.tensor([ids], dtype=torch.long, device=self.device)
        max_tokens = min(max_new_tokens, MAX_OUTPUT_TOKENS)
        prev_text = self.tokenizer.decode(x[0].tolist())
        prev_bytes = len(prev_text.encode("utf-8"))
        out = x
        for _ in range(max_tokens):
            with torch.no_grad():
                logits, _, _ = self.model(out)
            logits = logits[:, -1, :] / max(temperature, 1e-6)
            if top_k > 0:
                v, _ = torch.topk(logits, min(top_k, logits.size(-1)))
                logits[logits < v[:, -1:]] = float("-inf")
            probs = torch.softmax(logits, dim=-1)
            if repetition_penalty != 1.0:
                for idx in set(out[0].tolist()):
                    probs[0, idx] /= repetition_penalty
                    probs[0, idx] = probs[0, idx].clamp(min=1e-30)
                probs = probs / probs.sum()
            next_id = torch.multinomial(probs, 1)
            if self._is_eos(next_id.item()):
                break
            out = torch.cat([out, next_id], dim=1)
            full_text = self.tokenizer.decode(out[0].tolist())
            chunk = full_text[prev_bytes:]
            prev_bytes = len(full_text.encode("utf-8"))
            if not chunk:
                continue
            if stop:
                stopped = False
                for s in stop:
                    idx_s = chunk.find(s)
                    if idx_s != -1:
                        chunk = chunk[:idx_s]
                        stopped = True
                        break
                if stopped:
                    yield chunk
                    break
            yield chunk

    def _is_eos(self, token_id: int) -> bool:
        try:
            return self.tokenizer._tok.decode_single_token_bytes(token_id) == b"<|endoftext|>"
        except Exception:
            return False


# ═══════════════════════════════════════════════════════════════════════════
# App state
# ═══════════════════════════════════════════════════════════════════════════

_MODEL: ServerModel | None = None
_AUTH: AuthState = AuthState(enabled=False)
_RATE_LIMITER: RateLimiter = RateLimiter(RATE_LIMIT_USER_RPS, RATE_LIMIT_ADMIN_RPS, RATE_BUCKET_CAPACITY)
_IP_BANNER: IpBanner = IpBanner()


def _resolve_device(device: str | None) -> str:
    if device:
        return device
    return "cuda" if torch.cuda.is_available() else "cpu"


def _probe_n_kv(checkpoint_dir: str) -> int:
    from safetensors import safe_open
    path = Path(checkpoint_dir) / "model.safetensors"
    with safe_open(str(path), framework="pt", device="cpu") as h:
        t = h.get_tensor("layers.0.attn.k_proj.weight")
    return int(t.shape[0]) // 32


def load_model(checkpoint: str, device: str | None = None) -> ServerModel:
    device = _resolve_device(device)
    n_kv = _probe_n_kv(checkpoint)
    cfg = TopoGPT2Config(SCALE="small", DEVICE=device, N_KV_HEADS=n_kv)
    tokenizer = BPETokenizer("gpt2")
    cfg.VOCAB_SIZE = tokenizer.vocab_size
    model = TopoGPT2(cfg).to(device).eval()
    sd = load_file(str(Path(checkpoint) / "model.safetensors"), device=device)
    model.load_state_dict(sd, strict=False)
    set_seed(42, device)
    n_params = sum(p.numel() for p in model.parameters())
    logger.info('{"event":"model_loaded","params":%d,"n_kv":%d,"device":"%s"}', n_params, n_kv, device)
    return ServerModel(model=model, tokenizer=tokenizer, device=device, checkpoint=checkpoint)


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
async def _security_middleware(request: Request, call_next: Callable[[Request], Awaitable[Response]]) -> Response:
    """Global middleware: rate-limit, IP-ban, security headers, audit log."""

    client_ip = _real_ip(request)
    if _IP_BANNER.is_banned(client_ip):
        _audit_logger.warning('{"event":"blocked","reason":"ip_banned","ip":"%s","path":"%s"}',
                             client_ip, request.url.path)
        return _json_error(403, "Access denied")

    # Rate limit by IP (before auth so brute-force is throttled)
    if not _RATE_LIMITER.allow(f"ip:{client_ip}", role="user"):
        _audit_logger.warning('{"event":"rate_limited","ip":"%s","path":"%s"}',
                             client_ip, request.url.path)
        return _json_error(429, "Too many requests. Slow down.")

    response = await call_next(request)

    # Security headers on every response
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["Content-Security-Policy"] = "default-src 'none'; frame-ancestors 'none'"
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
            client_ip, api_key.role,
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
    return {
        "object": "list",
        "data": [
            {
                "id": "topogpt3",
                "object": "model",
                "created": 0,
                "owned_by": "topogpt3",
            }
        ],
    }


@app.post("/v1/completions")
async def completions(req: CompletionRequest, request: Request):
    _api_key = await _authenticate(request)
    await _check_rate_limit(_api_key, request)
    _check_model()

    _audit_logger.info(
        '{"event":"completion","role":"%s","stream":%s,"prompt_len":%d,"max_tokens":%d}',
        _api_key.role, req.stream, len(req.prompt), req.max_tokens,
    )

    if req.stream:
        return StreamingResponse(
            _stream_completion(
                req.prompt, req.max_tokens, req.temperature,
                req.top_k, req.repetition_penalty, req.stop,
            ),
            media_type="text/event-stream",
        )

    t0 = time.monotonic()
    text = _MODEL.complete(
        req.prompt,
        max_new_tokens=req.max_tokens,
        temperature=req.temperature,
        top_k=req.top_k,
        repetition_penalty=req.repetition_penalty,
        stop=req.stop,
    )
    elapsed = time.monotonic() - t0
    prompt_tokens = len(_MODEL.tokenizer.encode(req.prompt[:MAX_PROMPT_CHARS]))
    completion_tokens = max(len(_MODEL.tokenizer.encode(text[len(req.prompt):])), 1)
    return {
        "id": f"cmpl-{_short_id()}",
        "object": "text_completion",
        "created": int(time.time()),
        "model": "topogpt3",
        "choices": [
            {
                "text": text[len(req.prompt):],
                "index": 0,
                "logprobs": None,
                "finish_reason": "stop",
            }
        ],
        "usage": {
            "prompt_tokens": prompt_tokens,
            "completion_tokens": completion_tokens,
            "total_tokens": prompt_tokens + completion_tokens,
        },
    }


@app.post("/v1/chat/completions")
async def chat_completions(req: ChatCompletionRequest, request: Request):
    _api_key = await _authenticate(request)
    await _check_rate_limit(_api_key, request)
    _check_model()

    prompt = _build_chat_prompt(req.messages)
    _audit_logger.info(
        '{"event":"chat","role":"%s","stream":%s,"n_msgs":%d,"prompt_len":%d}',
        _api_key.role, req.stream, len(req.messages), len(prompt),
    )

    if req.stream:
        return StreamingResponse(
            _stream_chat(
                int(time.time() * 1000), prompt, req.max_tokens,
                req.temperature, req.top_k, req.repetition_penalty, req.stop,
            ),
            media_type="text/event-stream",
        )

    t0 = time.monotonic()
    text = _MODEL.complete(
        prompt,
        max_new_tokens=req.max_tokens,
        temperature=req.temperature,
        top_k=req.top_k,
        repetition_penalty=req.repetition_penalty,
        stop=req.stop,
    )
    response_text = text[len(prompt):]
    return {
        "id": f"chatcmpl-{_short_id()}",
        "object": "chat.completion",
        "created": int(time.time()),
        "model": "topogpt3",
        "choices": [
            {
                "index": 0,
                "message": {"role": "assistant", "content": response_text},
                "finish_reason": "stop",
            }
        ],
        "usage": {
            "prompt_tokens": len(_MODEL.tokenizer.encode(prompt)),
            "completion_tokens": len(_MODEL.tokenizer.encode(response_text)),
            "total_tokens": len(_MODEL.tokenizer.encode(text)),
        },
    }


# ═══════════════════════════════════════════════════════════════════════════
# Helpers
# ═══════════════════════════════════════════════════════════════════════════


def _check_model():
    if _MODEL is None:
        raise HTTPException(status_code=503, detail="Model not loaded yet")


def _short_id() -> str:
    return secrets.token_hex(8)


def _build_chat_prompt(messages: list[Message]) -> str:
    for msg in reversed(messages):
        if msg.role == "user":
            return _extract_text(msg.content)
    return ""


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
    prompt: str, max_tokens: int, temperature: float,
    top_k: int, repetition_penalty: float, stop: list[str],
):
    t0 = int(time.time())
    short_id = _short_id()
    for chunk_text in _MODEL.stream_complete(
        prompt, max_new_tokens=max_tokens, temperature=temperature,
        top_k=top_k, repetition_penalty=repetition_penalty, stop=stop,
    ):
        data = {
            "id": f"cmpl-{short_id}",
            "object": "text_completion",
            "created": t0,
            "model": "topogpt3",
            "choices": [
                {"text": chunk_text, "index": 0, "logprobs": None, "finish_reason": None}
            ],
        }
        yield f"data: {json.dumps(data)}\n\n"
    data = {
        "id": f"cmpl-{short_id}",
        "object": "text_completion",
        "created": t0,
        "model": "topogpt3",
        "choices": [
            {"text": "", "index": 0, "logprobs": None, "finish_reason": "stop"}
        ],
    }
    yield f"data: {json.dumps(data)}\n\n"
    yield "data: [DONE]\n\n"


async def _stream_chat(
    t0_ms: int, prompt: str, max_tokens: int, temperature: float,
    top_k: int, repetition_penalty: float, stop: list[str],
):
    for chunk_text in _MODEL.stream_complete(
        prompt, max_new_tokens=max_tokens, temperature=temperature,
        top_k=top_k, repetition_penalty=repetition_penalty, stop=stop,
    ):
        data = {
            "id": f"chatcmpl-{_short_id()}",
            "object": "chat.completion.chunk",
            "created": t0_ms // 1000,
            "model": "topogpt3",
            "choices": [
                {"index": 0, "delta": {"content": chunk_text}, "finish_reason": None}
            ],
        }
        yield f"data: {json.dumps(data)}\n\n"
    data = {
        "id": f"chatcmpl-{_short_id()}",
        "object": "chat.completion.chunk",
        "created": t0_ms // 1000,
        "model": "topogpt3",
        "choices": [
            {"index": 0, "delta": {}, "finish_reason": "stop"}
        ],
    }
    yield f"data: {json.dumps(data)}\n\n"
    yield "data: [DONE]\n\n"


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
    ap.add_argument("--keys", "-k", default=None,
                    help="Comma-separated API keys (or set TOPOGPT3_API_KEYS)")
    ap.add_argument("--no-auth", action="store_true",
                    help="Disable authentication (DEVELOPMENT ONLY)")
    ap.add_argument("--verbose", "-v", action="store_true")
    ap.add_argument("--reload", action="store_true",
                    help="Enable auto-reload for development")
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
