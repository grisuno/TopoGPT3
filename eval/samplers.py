"""Registry of sampler constructors for the HumanEval harness.

Replaces the hardcoded `if mode == "standard": ... elif mode == "hrm": ...`
chain in `eval.harness.make_sampler` with a decorator-based registry that
mirrors the pattern in `claude-code-main/src/tools.ts`.

The pattern:
  - `@register_sampler("name")` decorates a factory function that
    takes a `settings_kwargs` dict (already filtered for sampler-specific
    keys) and returns an object with a `run()` method (or just a sampler
    object that `harness.evaluate_problem` knows how to drive).
  - `build_sampler("name", settings_kwargs)` is the public entry point.
  - `list_samplers()` returns the registered names for `--help` output.

Adding a new sampler is then a one-decorator change, not an edit to
the harness's control flow.
"""
from __future__ import annotations

import os
from typing import Callable, Dict, List

from topogpt3 import (
    InferencePipeline,
    InferenceSettings,
    HRMInferencePipeline,
    HRMInferenceSettings,
    RecursiveReasoningConfig,
)


SamplerFactory = Callable[[dict], object]
SAMPLER_REGISTRY: Dict[str, SamplerFactory] = {}


def register_sampler(name: str, *, enabled_env: str | None = None):
    """
    Decorator. Register a factory under `name`. If `enabled_env` is set,
    the factory is only registered when that env var is truthy. This
    mirrors the `feature('XXX')` gating in claude-code-main/src/tools.ts.
    """
    def deco(fn: SamplerFactory) -> SamplerFactory:
        if enabled_env is not None and not _is_env_truthy(enabled_env):
            return fn
        if name in SAMPLER_REGISTRY:
            raise ValueError(
                f"sampler {name!r} already registered as "
                f"{SAMPLER_REGISTRY[name].__name__}"
            )
        SAMPLER_REGISTRY[name] = fn
        return fn
    return deco


def _is_env_truthy(name: str) -> bool:
    return os.environ.get(name, "").lower() in ("1", "true", "yes", "on")


# ---------------------------------------------------------------------------
# Built-in samplers
# ---------------------------------------------------------------------------

@register_sampler("standard")
def _make_standard(settings_kwargs: dict):
    return InferencePipeline(InferenceSettings(**settings_kwargs))


@register_sampler("hrm")
def _make_hrm(settings_kwargs: dict):
    reasoning_cfg = settings_kwargs.pop("reasoning", None)
    if reasoning_cfg is None:
        reasoning_cfg = RecursiveReasoningConfig(
            max_high_level_iters=2,
            max_low_level_iters=3,
            low_level_window=2,
        )
    return HRMInferencePipeline(
        HRMInferenceSettings(reasoning=reasoning_cfg, **settings_kwargs)
    )


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def list_samplers() -> List[str]:
    return sorted(SAMPLER_REGISTRY.keys())


def build_sampler(mode: str, settings_kwargs: dict):
    """Construct a sampler. Drop-in replacement for the old
    `make_sampler(mode, settings_kwargs)` in `eval.harness`."""
    if mode not in SAMPLER_REGISTRY:
        raise ValueError(
            f"unknown sampler mode {mode!r}. "
            f"Available: {list_samplers()}"
        )
    return SAMPLER_REGISTRY[mode](settings_kwargs)


# Backwards-compatible alias
make_sampler = build_sampler
