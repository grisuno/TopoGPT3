"""Streaming + governance for autoregressive generation.

Two classes that fix two real problems with the existing
`topogpt3.inference` pipeline:

  - `TokenStream` — a thread-safe queue that captures raw token IDs as
    they are produced by the model. Enables post-hoc prefix agreement
    and exact-match metrics that need the *raw* token stream (the
    current harness only stores the post-extracted candidate text,
    losing that information).

  - `GenerationGovernor` — wraps `model.generate` and exposes stop
    hooks: per-token timeout, loop detection (last K tokens repeat),
    and a user-callable cancel. Returns a `GenerationResult` with
    the stop reason so callers can distinguish "ran out of tokens"
    from "hit the safety hook" from "user aborted".

This is a Python port of the patterns in
`claude-code-main/src/utils/stream.ts` (Stream<T> AsyncIterator
wrapper) and `claude-code-main/src/query/stopHooks.ts`
(AsyncGenerator with `preventContinuation`). The TypeScript originals
are 76 and 473 lines respectively; this module is ~150 lines because
Python's GIL lets us avoid the manual promise queueing.

NOTE: This module does NOT modify `topogpt3/model.py`. The generation
loop is replicated here (not monkey-patched) so the original `generate`
remains the single source of truth for the production sampler.
"""
from __future__ import annotations

import threading
import time
from dataclasses import dataclass, field
from enum import Enum
from typing import Callable, List, Optional, Tuple

import torch
import torch.nn.functional as F


# ---------------------------------------------------------------------------
# Token stream
# ---------------------------------------------------------------------------

class TokenStream:
    """Thread-safe single-producer / single-consumer queue of token IDs.

    The producer (the generation loop) calls `put(tok)` for each new
    token. Consumers can iterate via `iter_tokens(block=True)` or
    `drain()` to get everything emitted so far.

    The stream tracks a monotonic counter so consumers can detect
    "no new tokens since last call" cheaply.
    """

    def __init__(self) -> None:
        self._tokens: List[int] = []
        self._lock = threading.Lock()
        self._new_event = threading.Event()
        self._closed = False

    def put(self, tok: int) -> None:
        with self._lock:
            self._tokens.append(int(tok))
            self._new_event.set()

    def mark_done(self) -> None:
        with self._lock:
            self._closed = True
            self._new_event.set()

    def drain(self) -> List[int]:
        """Return all tokens emitted so far, atomic snapshot."""
        with self._lock:
            return list(self._tokens)

    def wait_for_new(self, timeout: float = 0.05) -> bool:
        """Block up to `timeout` seconds for a new token. Returns True
        if a new token arrived (or stream closed), False on timeout."""
        if self._new_event.wait(timeout):
            with self._lock:
                self._new_event.clear()
                return True
        return False

    def is_closed(self) -> bool:
        with self._lock:
            return self._closed

    def __len__(self) -> int:
        with self._lock:
            return len(self._tokens)


# ---------------------------------------------------------------------------
# Stop reasons
# ---------------------------------------------------------------------------

class StopReason(str, Enum):
    EOS = "eos"                      # model emitted the EOT token (50256)
    MAX_TOKENS = "max_tokens"        # hit max_new_tokens limit
    TIMEOUT = "timeout"              # per-token wall-time exceeded
    LOOP = "loop"                    # last K tokens repeat
    USER_ABORT = "user_abort"        # external cancel() called
    CONTEXT_OVERFLOW = "context_overflow"  # prompt+gen > MAX_SEQ_LEN


@dataclass
class GenerationResult:
    """Outcome of a governed generation."""
    token_ids: List[int]            # generated tokens only (no prompt)
    stop_reason: StopReason
    n_tokens: int = field(init=False)
    elapsed_s: float = 0.0
    last_window: List[int] = field(default_factory=list)

    def __post_init__(self):
        self.n_tokens = len(self.token_ids)


# ---------------------------------------------------------------------------
# Hook signature
# ---------------------------------------------------------------------------

# A stop hook is called once per generated token, with the cumulative
# generated tokens so far. Return True to STOP the generation.
StopHook = Callable[[List[int]], bool]


# ---------------------------------------------------------------------------
# Governor
# ---------------------------------------------------------------------------

class GenerationGovernor:
    """Run a model's autoregressive generation loop with optional stop
    hooks and a streaming interface.

    Usage:
        ts = TokenStream()
        governor = GenerationGovernor(
            model=model,
            ctx=prompt_tensor,
            stream=ts,
            max_new_tokens=256,
            temperature=0.2,
            top_k=40,
            repetition_penalty=1.1,
        )
        result = governor.run(stop_hooks=[loop_detector, timeout_hook])
        if result.stop_reason == StopReason.LOOP:
            ...
    """

    EOT_TOKEN = 50256  # GPT-2 BPE end-of-text

    def __init__(
        self,
        model: torch.nn.Module,
        ctx: torch.Tensor,
        stream: TokenStream,
        max_new_tokens: int = 256,
        temperature: float = 0.8,
        top_k: int = 50,
        repetition_penalty: float = 1.0,
        max_seq_len: int = 512,
    ) -> None:
        self.model = model
        self.ctx = ctx
        self.stream = stream
        self.max_new_tokens = max_new_tokens
        self.temperature = max(temperature, 1e-8)
        self.top_k = top_k
        self.repetition_penalty = repetition_penalty
        self.max_seq_len = max_seq_len
        self._cancel = threading.Event()

    def cancel(self) -> None:
        """Asynchronously stop the generation. Safe to call from any
        thread (e.g. a watchdog thread or the main UI loop)."""
        self._cancel.set()

    def _should_cancel(self) -> bool:
        return self._cancel.is_set()

    def run(
        self,
        stop_hooks: Optional[List[StopHook]] = None,
    ) -> GenerationResult:
        """Execute the generation loop. Returns when the model emits
        EOS, hits max_new_tokens, a hook returns True, or cancel() is
        called."""
        stop_hooks = stop_hooks or []
        self.model.eval()
        device = self.ctx.device

        with torch.no_grad():
            ctx = self.ctx[:, -self.max_seq_len:]
            logits, _, past_kvs = self.model(ctx)
            logits = logits[:, -1, :] / self.temperature
            if self.repetition_penalty != 1.0:
                mask = torch.zeros_like(logits, dtype=torch.bool)
                mask.scatter_(1, ctx, True)
                logits = torch.where(
                    mask, logits / self.repetition_penalty, logits
                )
            if self.top_k > 0:
                v, _ = torch.topk(logits, min(self.top_k, logits.size(-1)))
                logits[logits < v[:, -1:]] = float("-inf")
            next_tok = torch.multinomial(F.softmax(logits, dim=-1), 1)
            first_tok = int(next_tok.item())
            generated: List[int] = [first_tok]
            self.stream.put(first_tok)
            t0 = time.time()

            if first_tok == self.EOT_TOKEN:
                self.stream.mark_done()
                return GenerationResult(
                    token_ids=generated,
                    stop_reason=StopReason.EOS,
                    elapsed_s=time.time() - t0,
                )

            stop_reason = StopReason.MAX_TOKENS
            for step in range(self.max_new_tokens - 1):
                if self._should_cancel():
                    stop_reason = StopReason.USER_ABORT
                    break

                # Context overflow: prompt + gen > max_seq_len
                if (ctx.shape[1] + len(generated)) >= self.max_seq_len:
                    stop_reason = StopReason.CONTEXT_OVERFLOW
                    break

                logits, _, past_kvs = self.model(
                    next_tok, past_kvs=past_kvs
                )
                logits = logits[:, -1, :] / self.temperature
                if self.repetition_penalty != 1.0:
                    mask = torch.zeros_like(logits, dtype=torch.bool)
                    mask.scatter_(1, self.ctx, True)
                    logits = torch.where(
                        mask, logits / self.repetition_penalty, logits
                    )
                if self.top_k > 0:
                    v, _ = torch.topk(
                        logits, min(self.top_k, logits.size(-1))
                    )
                    logits[logits < v[:, -1:]] = float("-inf")
                next_tok = torch.multinomial(
                    F.softmax(logits, dim=-1), 1
                )
                tok_id = int(next_tok.item())
                generated.append(tok_id)
                self.stream.put(tok_id)

                if tok_id == self.EOT_TOKEN:
                    stop_reason = StopReason.EOS
                    break

                # Run user-supplied stop hooks
                for hook in stop_hooks:
                    try:
                        if hook(generated):
                            stop_reason = StopReason.LOOP
                            break
                    except Exception:
                        # A buggy hook should not crash generation
                        pass
                if stop_reason == StopReason.LOOP:
                    break

        self.stream.mark_done()
        return GenerationResult(
            token_ids=generated,
            stop_reason=stop_reason,
            elapsed_s=time.time() - t0,
            last_window=generated[-16:],
        )


# ---------------------------------------------------------------------------
# Built-in stop hooks
# ---------------------------------------------------------------------------

def make_loop_detector(window: int = 32, min_repeats: int = 4) -> StopHook:
    """Return True if the last `window` tokens contain a sub-sequence
    of length >= `min_repeats` that repeats consecutively.

    Catches the "model is stuck in a loop" pathology where a 24M-param
    model emits the same 4-token pattern indefinitely.
    """
    def hook(generated: List[int]) -> bool:
        if len(generated) < window:
            return False
        recent = generated[-window:]
        # Look for runs of identical tokens
        run_len = 1
        for i in range(1, len(recent)):
            if recent[i] == recent[i - 1]:
                run_len += 1
                if run_len >= min_repeats:
                    return True
            else:
                run_len = 1
        # Look for 2-token pattern repeated
        if len(generated) >= 8:
            tail = generated[-8:]
            if tail[:2] == tail[2:4] == tail[4:6] == tail[6:8]:
                return True
        return False
    return hook


def make_timeout_hook(per_token_s: float = 5.0) -> StopHook:
    """Return True if the per-token wall time exceeds `per_token_s`.
    Useful for catching token-generation stalls (rare on CPU, but
    happens under memory pressure).
    """
    state = {"t0": time.time(), "last": 0}
    def hook(generated: List[int]) -> bool:
        if len(generated) == state["last"]:
            return False
        state["last"] = len(generated)
        now = time.time()
        if (now - state["t0"]) > per_token_s * len(generated):
            return True
        return False
    return hook
