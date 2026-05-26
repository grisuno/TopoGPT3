#!/usr/bin/env python3
"""TopoGPT3.1: Hierarchical Recursive Reasoning Inference Engine.

This module extends TopoGPT3 with a parameter-free hierarchical recursive
reasoning pipeline inspired by:

    * Hierarchical Reasoning Model (HRM), Sapient Intelligence: a biologically
      motivated two-speed architecture with a slow high-level loop and a fast
      low-level loop.
    * Tiny Recursive Model (TRM) and Generative Recursive Reasoning Models
      (GRAM): latent-space recurrence that iterates token vectors until they
      reach an attractor before projecting them outward.

The pipeline is intentionally built so that the underlying TopoGPT2 weight
matrices remain bit-identical to those produced by the TopoGPT3 trainer. No
new learnable parameters are introduced. The pretrained transformer layers
are repurposed as the recurrent step function of a hierarchical fixed-point
iteration whose halting condition is the empirical stabilization of the
latent state.

The high-level slow state is persisted across multiple emitted tokens to
achieve sparse temporal reasoning: the full network is iterated only at
configurable intervals, while a short suffix of layers refines the low-level
state at every emitted token.

All configurable values reside in dedicated configuration dataclasses; no
magic numbers or hardcoded constants are embedded in business logic. Path
resolution rejects traversal escapes. State dict loading defers strictness
to settings, so an architecturally aligned TopoGPT3 checkpoint loads
unchanged.

Usage:

    python3 inference_hrm.py --prompt "def fibonacci(" --hrm-h-iters 4 \\
        --hrm-l-iters 6 --hrm-l-window 3 --max-new 256
"""
from __future__ import annotations

import argparse
import logging
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Mapping, Optional, Tuple

import torch
import torch.nn.functional as F
from safetensors import safe_open
from safetensors.torch import load_file


@dataclass(frozen=True)
class ScalePreset:
    """Immutable architecture preset for a named model scale."""

    d_model: int
    n_heads: int
    n_layers: int
    max_seq_len: int


@dataclass(frozen=True)
class RecursiveReasoningConfig:
    """Hyperparameters governing the hierarchical recursive thinking loop.

    The semantics follow the HRM and GRAM literature, adapted to operate
    safely with zero additional learnable parameters on a model that was
    not trained with recurrence in its computational graph. The reasoner
    performs damped fixed-point iteration entirely in the residual-stream
    space produced by the baseline forward pass; deep activations are never
    fed back into the token-embedding-input layers, preserving the trained
    activation distribution at every layer boundary.

    Attributes:
        enabled: master switch; when False the pipeline degrades to the
            standard non-recursive autoregressive loop.
        max_high_level_iters: maximum slow-loop iterations per emitted token.
            Each iteration applies a deeper trailing window of layers.
        max_low_level_iters: maximum fast-loop iterations per high-level step.
            Each iteration applies the short trailing window of layers.
        low_level_window: number of trailing transformer layers iterated by
            the low-level fast loop.
        high_level_window: number of trailing transformer layers iterated by
            the high-level slow loop. Should be greater than or equal to
            low_level_window so the hierarchy matches the HRM coarse/fine
            split.
        low_level_step: damping coefficient in [0, 1] for the low-level
            update rule z <- z + step * (window(z) - z).
        high_level_step: damping coefficient for the high-level update.
        attractor_low_epsilon: relative L2 change threshold that declares the
            low-level state converged.
        attractor_high_epsilon: relative L2 change threshold that declares the
            high-level state converged.
        high_level_persist_tokens: tokens during which the refinement vector
            is reused as a warm start before being re-initialized to zero.
            This is the sparse temporal-memory dimension.
        cache_warm_start_weight: scalar in [0, 1] applied to the cached
            refinement before warm-starting the next token's iteration.
        max_drift_relative: relative L2 distance ceiling between the iterated
            latent and the baseline latent; exceeding it triggers a reset to
            the baseline state and aborts thinking for the current token.
        latent_change_eps: floor used in the denominator of relative change
            computations to avoid division by zero.
        safety_max_total_iterations: hard cap on total layer invocations per
            emitted token regardless of configured iters.
        minimum_low_level_iters: floor on low-level iterations before
            convergence checks may halt the loop.
        minimum_high_level_iters: floor on high-level iterations before
            convergence checks may halt the loop.
        diagnostic_logging: when True, emits per-token iteration statistics.
    """

    enabled: bool = True
    max_high_level_iters: int = 0
    max_low_level_iters: int = 0
    low_level_window: int = 2
    high_level_window: int = 4
    low_level_step: float = 0.1
    high_level_step: float = 0.1
    attractor_low_epsilon: float = 5e-3
    attractor_high_epsilon: float = 1e-2
    high_level_persist_tokens: int = 4
    cache_warm_start_weight: float = 0.5
    max_drift_relative: float = 0.3
    latent_change_eps: float = 1e-8
    safety_max_total_iterations: int = 256
    minimum_low_level_iters: int = 0
    minimum_high_level_iters: int = 0
    diagnostic_logging: bool = False


@dataclass
class HRMInferenceSettings:
    """Centralized configuration for the TopoGPT3.1 inference pipeline.

    Every value consumed downstream resides here. Extending the pipeline with
    a new tunable means extending this dataclass; no other module should
    embed literals.
    """

    model_scale: str = "small"
    device: str = field(
        default_factory=lambda: "cuda" if torch.cuda.is_available() else "cpu"
    )
    seed: int = 42

    checkpoint_dir: str = "checkpoints_topogpt3"
    checkpoint_name: str = "last"
    model_filename: str = "model.safetensors"
    state_filename: str = "state.json"

    topogpt31_source_filename: str = "inference_hrm.py"
    topogpt3_source_filename: str = "train.py"
    topogpt2_source_filename: str = "model.py"
    source_directory: str = "."

    tokenizer_encoding: str = "gpt2"
    weight_probe_key: str = "layers.0.attn.k_proj.weight"

    apply_gauss_patch_at_load: bool = True
    strict_state_dict: bool = False

    prompt: str = "def main("
    max_new_tokens: int = 256
    temperature: float = 0.3
    top_k: int = 50
    repetition_penalty: float = 1.1
    end_of_text_token_id: int = 50256

    reasoning: RecursiveReasoningConfig = field(
        default_factory=RecursiveReasoningConfig
    )

    log_level: str = "INFO"
    log_name: str = "TopoGPT3.1Inference"
    log_format: str = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    log_date_format: str = "%Y-%m-%d %H:%M:%S"

    result_separator_char: str = "="
    result_separator_width: int = 72
    prompt_label: str = "PROMPT"
    completion_label: str = "COMPLETION"
    reasoning_label: str = "REASONING_STATS"
    elapsed_floor_seconds: float = 1e-3

    min_max_new_tokens: int = 1
    max_max_new_tokens: int = 8192
    min_temperature: float = 1e-3
    max_temperature: float = 5.0
    min_top_k: int = 0
    min_repetition_penalty: float = 0.5
    max_repetition_penalty: float = 5.0
    max_checkpoint_bytes: int = 50 * (1024 ** 3)
    min_checkpoint_bytes: int = 1024

    min_hrm_h_iters: int = 0
    max_hrm_h_iters: int = 32
    min_hrm_l_iters: int = 0
    max_hrm_l_iters: int = 64
    min_hrm_l_window: int = 1
    max_hrm_l_window: int = 64
    min_hrm_h_window: int = 1
    max_hrm_h_window: int = 64
    min_hrm_persist: int = 1
    max_hrm_persist: int = 256
    min_hrm_step: float = 0.0
    max_hrm_step: float = 1.0
    min_hrm_warm_start: float = 0.0
    max_hrm_warm_start: float = 1.0
    min_hrm_drift: float = 0.0
    max_hrm_drift: float = 10.0

    runtime_module_alias: str = "topogpt3_runtime_hrm"

    @staticmethod
    def scale_presets() -> Mapping[str, ScalePreset]:
        """Return the architecture preset table indexed by scale name."""
        return {
            "micro":  ScalePreset(d_model=64,  n_heads=4,  n_layers=2,
                                  max_seq_len=128),
            "small":  ScalePreset(d_model=256, n_heads=8,  n_layers=6,
                                  max_seq_len=256),
            "medium": ScalePreset(d_model=512, n_heads=8,  n_layers=12,
                                  max_seq_len=512),
            "gpt2":   ScalePreset(d_model=768, n_heads=12, n_layers=12,
                                  max_seq_len=1024),
        }

    def preset(self) -> ScalePreset:
        """Return the resolved preset for the configured model scale."""
        table = self.scale_presets()
        if self.model_scale not in table:
            raise ValueError(
                f"Unknown model scale '{self.model_scale}'. "
                f"Allowed: {sorted(table.keys())}"
            )
        return table[self.model_scale]

    def validate(self) -> None:
        """Raise ValueError if any setting falls outside its safety bounds."""
        if not (self.min_max_new_tokens
                <= self.max_new_tokens <= self.max_max_new_tokens):
            raise ValueError(
                f"max_new_tokens={self.max_new_tokens} outside "
                f"[{self.min_max_new_tokens}, {self.max_max_new_tokens}]"
            )
        if not (self.min_temperature
                <= self.temperature <= self.max_temperature):
            raise ValueError(
                f"temperature={self.temperature} outside "
                f"[{self.min_temperature}, {self.max_temperature}]"
            )
        if self.top_k < self.min_top_k:
            raise ValueError(
                f"top_k={self.top_k} must be >= {self.min_top_k}"
            )
        if not (self.min_repetition_penalty
                <= self.repetition_penalty <= self.max_repetition_penalty):
            raise ValueError(
                f"repetition_penalty={self.repetition_penalty} outside "
                f"[{self.min_repetition_penalty}, "
                f"{self.max_repetition_penalty}]"
            )
        if self.result_separator_width <= 0:
            raise ValueError("result_separator_width must be positive")
        if self.elapsed_floor_seconds <= 0:
            raise ValueError("elapsed_floor_seconds must be positive")
        r = self.reasoning
        if not (self.min_hrm_h_iters
                <= r.max_high_level_iters <= self.max_hrm_h_iters):
            raise ValueError(
                f"max_high_level_iters={r.max_high_level_iters} outside "
                f"[{self.min_hrm_h_iters}, {self.max_hrm_h_iters}]"
            )
        if not (self.min_hrm_l_iters
                <= r.max_low_level_iters <= self.max_hrm_l_iters):
            raise ValueError(
                f"max_low_level_iters={r.max_low_level_iters} outside "
                f"[{self.min_hrm_l_iters}, {self.max_hrm_l_iters}]"
            )
        if not (self.min_hrm_l_window
                <= r.low_level_window <= self.max_hrm_l_window):
            raise ValueError(
                f"low_level_window={r.low_level_window} outside "
                f"[{self.min_hrm_l_window}, {self.max_hrm_l_window}]"
            )
        if not (self.min_hrm_h_window
                <= r.high_level_window <= self.max_hrm_h_window):
            raise ValueError(
                f"high_level_window={r.high_level_window} outside "
                f"[{self.min_hrm_h_window}, {self.max_hrm_h_window}]"
            )
        if r.high_level_window < r.low_level_window:
            raise ValueError(
                f"high_level_window={r.high_level_window} must be >= "
                f"low_level_window={r.low_level_window}"
            )
        if not (self.min_hrm_persist
                <= r.high_level_persist_tokens <= self.max_hrm_persist):
            raise ValueError(
                f"high_level_persist_tokens={r.high_level_persist_tokens} "
                f"outside [{self.min_hrm_persist}, {self.max_hrm_persist}]"
            )
        if not (self.min_hrm_step <= r.low_level_step <= self.max_hrm_step):
            raise ValueError(
                f"low_level_step={r.low_level_step} outside "
                f"[{self.min_hrm_step}, {self.max_hrm_step}]"
            )
        if not (self.min_hrm_step <= r.high_level_step <= self.max_hrm_step):
            raise ValueError(
                f"high_level_step={r.high_level_step} outside "
                f"[{self.min_hrm_step}, {self.max_hrm_step}]"
            )
        if not (self.min_hrm_warm_start
                <= r.cache_warm_start_weight <= self.max_hrm_warm_start):
            raise ValueError(
                f"cache_warm_start_weight={r.cache_warm_start_weight} "
                f"outside [{self.min_hrm_warm_start}, "
                f"{self.max_hrm_warm_start}]"
            )
        if not (self.min_hrm_drift
                <= r.max_drift_relative <= self.max_hrm_drift):
            raise ValueError(
                f"max_drift_relative={r.max_drift_relative} outside "
                f"[{self.min_hrm_drift}, {self.max_hrm_drift}]"
            )
        if r.attractor_low_epsilon <= 0 or r.attractor_high_epsilon <= 0:
            raise ValueError("attractor epsilons must be positive")
        if r.latent_change_eps <= 0:
            raise ValueError("latent_change_eps must be positive")
        if r.safety_max_total_iterations < 1:
            raise ValueError("safety_max_total_iterations must be >= 1")
        if r.minimum_low_level_iters < 0 or r.minimum_high_level_iters < 0:
            raise ValueError("minimum iteration floors must be non-negative")
        self.preset()


class HRMLoggerFactory:
    """Builds a stdout-attached logger from inference settings."""

    @staticmethod
    def build(settings: HRMInferenceSettings) -> logging.Logger:
        """Return a configured Logger with a single deduplicated stdout handler."""
        logger = logging.getLogger(settings.log_name)
        level = getattr(logging, settings.log_level.upper(), logging.INFO)
        logger.setLevel(level)
        if not logger.handlers:
            handler = logging.StreamHandler(sys.stdout)
            handler.setFormatter(logging.Formatter(
                fmt=settings.log_format,
                datefmt=settings.log_date_format,
            ))
            logger.addHandler(handler)
        logger.propagate = False
        return logger


class SecurePathResolver:
    """Resolves filesystem paths while rejecting traversal outside their root."""

    @staticmethod
    def resolve_under(root: Path, *parts: str) -> Path:
        """Join parts under root and return the canonical resolved path.

        Raises ValueError if the resolved path escapes root.
        """
        resolved_root = root.resolve()
        candidate = resolved_root.joinpath(*parts).resolve()
        try:
            candidate.relative_to(resolved_root)
        except ValueError as exc:
            raise ValueError(
                f"Path '{candidate}' escapes root '{resolved_root}'."
            ) from exc
        return candidate

    @staticmethod
    def require_existing_file(path: Path,
                              expected_suffix: Optional[str] = None) -> Path:
        """Validate path points to an existing regular file with the expected suffix."""
        if not path.exists():
            raise FileNotFoundError(f"Required file not found: {path}")
        if not path.is_file():
            raise ValueError(f"Path is not a regular file: {path}")
        if expected_suffix is not None and path.suffix != expected_suffix:
            raise ValueError(
                f"Expected suffix '{expected_suffix}', got '{path.suffix}': {path}"
            )
        return path


class SourceModuleLoader:
    """Resolves the TopoGPT3 runtime module via the package import system."""

    def __init__(self, settings: HRMInferenceSettings, logger: logging.Logger):
        self._settings = settings
        self._logger = logger

    def load(self) -> Any:
        """Return the topogpt3.train module which re-exports model symbols."""
        from . import train as runtime_module
        self._logger.info(
            "Loaded TopoGPT3 runtime module: %s", runtime_module.__name__,
        )
        return runtime_module


class CheckpointPaths:
    """Computes and validates checkpoint file paths under a single root."""

    def __init__(self, settings: HRMInferenceSettings):
        self._settings = settings
        self._root = Path(settings.checkpoint_dir).resolve()
        self._slot = SecurePathResolver.resolve_under(
            self._root, settings.checkpoint_name,
        )

    @property
    def slot_dir(self) -> Path:
        """Directory holding the active checkpoint slot."""
        return self._slot

    def model_file(self) -> Path:
        """Resolved path to the safetensors weights file inside the slot."""
        return SecurePathResolver.resolve_under(
            self._slot, self._settings.model_filename,
        )

    def state_file(self) -> Path:
        """Resolved path to the JSON training-state file inside the slot."""
        return SecurePathResolver.resolve_under(
            self._slot, self._settings.state_filename,
        )

    def assert_ready(self) -> None:
        """Verify weights exist and the on-disk size lies within safety bounds."""
        weights = self.model_file()
        SecurePathResolver.require_existing_file(
            weights, expected_suffix=Path(self._settings.model_filename).suffix,
        )
        size_bytes = weights.stat().st_size
        if size_bytes < self._settings.min_checkpoint_bytes:
            raise ValueError(
                f"Checkpoint too small ({size_bytes} bytes): {weights}"
            )
        if size_bytes > self._settings.max_checkpoint_bytes:
            raise ValueError(
                f"Checkpoint exceeds allowed size "
                f"({size_bytes} > {self._settings.max_checkpoint_bytes} bytes): "
                f"{weights}"
            )


class WeightShapeProbe:
    """Reads tensor metadata from safetensors to infer architecture details."""

    def __init__(self, settings: HRMInferenceSettings, logger: logging.Logger):
        self._settings = settings
        self._logger = logger

    def detect_n_kv_heads(self, weights_path: Path,
                          d_model: int, n_heads: int) -> Optional[int]:
        """Recover N_KV_HEADS used at training by inspecting the k_proj shape.

        Returns None when the probe key is absent, signalling the caller to
        fall back to scale defaults rather than guess.
        """
        if n_heads <= 0 or d_model <= 0:
            raise ValueError("d_model and n_heads must be positive")
        if d_model % n_heads != 0:
            raise ValueError("d_model must be divisible by n_heads")
        d_head = d_model // n_heads

        probe_key = self._settings.weight_probe_key
        with safe_open(str(weights_path), framework="pt", device="cpu") as handle:
            keys = set(handle.keys())
            if probe_key not in keys:
                self._logger.warning(
                    "Probe key '%s' missing from checkpoint; "
                    "falling back to scale defaults.", probe_key,
                )
                return None
            tensor = handle.get_tensor(probe_key)
        k_dim = int(tensor.shape[0])
        if k_dim % d_head != 0:
            raise ValueError(
                f"k_proj output dim ({k_dim}) is not divisible by d_head ({d_head})"
            )
        n_kv = k_dim // d_head
        self._logger.info(
            "Detected N_KV_HEADS=%d (k_dim=%d, d_head=%d).",
            n_kv, k_dim, d_head,
        )
        return n_kv


class TopoGPT2ConfigAligner:
    """Builds a TopoGPT2Config matching the loaded checkpoint and tokenizer."""

    def __init__(self, settings: HRMInferenceSettings, source_module: Any,
                 logger: logging.Logger):
        self._settings = settings
        self._source = source_module
        self._logger = logger

    def build(self, n_kv_heads: Optional[int], vocab_size: int) -> Any:
        """Return a TopoGPT2Config dataclass ready to instantiate the model."""
        cfg_cls = getattr(self._source, "TopoGPT2Config")
        kwargs: Dict[str, Any] = {
            "SCALE": self._settings.model_scale,
            "DEVICE": self._settings.device,
            "RANDOM_SEED": self._settings.seed,
            "CHECKPOINT_DIR": self._settings.checkpoint_dir,
        }
        if n_kv_heads is not None and n_kv_heads > 0:
            kwargs["N_KV_HEADS"] = n_kv_heads
        cfg = cfg_cls(**kwargs)
        cfg.VOCAB_SIZE = vocab_size
        self._logger.info(
            "Aligned TopoGPT2Config: scale=%s d_model=%d n_heads=%d "
            "n_layers=%d n_kv_heads=%d vocab=%d max_seq=%d device=%s",
            cfg.SCALE, cfg.D_MODEL, cfg.N_HEADS, cfg.N_LAYERS,
            cfg.N_KV_HEADS, cfg.VOCAB_SIZE, cfg.MAX_SEQ_LEN, cfg.DEVICE,
        )
        return cfg


class TokenizerFactory:
    """Builds a BPETokenizer instance using the configured encoding."""

    def __init__(self, settings: HRMInferenceSettings, source_module: Any):
        self._settings = settings
        self._source = source_module

    def build(self) -> Any:
        """Return an instance of BPETokenizer bound to the configured encoding."""
        tokenizer_cls = getattr(self._source, "BPETokenizer")
        return tokenizer_cls(self._settings.tokenizer_encoding)


class GaussPatchApplier:
    """Applies the idempotent Gauss complex-multiply patch when enabled."""

    def __init__(self, settings: HRMInferenceSettings, source_module: Any,
                 logger: logging.Logger):
        self._settings = settings
        self._source = source_module
        self._logger = logger

    def apply_if_enabled(self) -> None:
        """Patch QuaternionSpectralLayer to use the 3-multiply Gauss contract."""
        if not self._settings.apply_gauss_patch_at_load:
            self._logger.info("Gauss complex-multiply patch disabled by settings.")
            return
        patch_fn = getattr(self._source, "apply_gauss_patch")
        patch_fn(self._logger)


class ModelAssembler:
    """Instantiates the model and loads weights from safetensors."""

    def __init__(self, settings: HRMInferenceSettings, source_module: Any,
                 logger: logging.Logger):
        self._settings = settings
        self._source = source_module
        self._logger = logger

    def assemble(self, aligned_cfg: Any,
                 paths: CheckpointPaths) -> torch.nn.Module:
        """Build the TopoGPT2 graph, load weights into it, and return it in eval mode."""
        model_cls = getattr(self._source, "TopoGPT2")
        model = model_cls(aligned_cfg)
        model.to(aligned_cfg.DEVICE)
        model.eval()

        params = model.count_params()
        self._logger.info(
            "Model parameters: total=%s trainable=%s",
            f"{params['total']:,}", f"{params['trainable']:,}",
        )

        weights_path = paths.model_file()
        self._logger.info("Loading weights from %s", weights_path)
        state_dict = load_file(str(weights_path), device=aligned_cfg.DEVICE)
        missing, unexpected = model.load_state_dict(
            state_dict, strict=self._settings.strict_state_dict,
        )
        if missing:
            self._logger.info("Missing keys (likely tied weights): %s", missing)
        if unexpected:
            self._logger.info("Unexpected keys ignored: %s", unexpected)
        self._logger.info("Weights loaded successfully (zero new parameters introduced).")
        return model


class SeedSynchronizer:
    """Applies deterministic seeds across torch, CUDA and the model package."""

    def __init__(self, settings: HRMInferenceSettings, source_module: Any,
                 logger: logging.Logger):
        self._settings = settings
        self._source = source_module
        self._logger = logger

    def apply(self) -> None:
        """Seed all relevant RNGs using the model package helper when available."""
        torch.manual_seed(self._settings.seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(self._settings.seed)
        set_seed_fn = getattr(self._source, "set_seed", None)
        if callable(set_seed_fn):
            set_seed_fn(self._settings.seed, self._settings.device)
        self._logger.info(
            "Seed synchronized (seed=%d device=%s).",
            self._settings.seed, self._settings.device,
        )


class LatentChangeMetric:
    """Computes the relative L2 distance between two latent tensors."""

    def __init__(self, epsilon_floor: float):
        if epsilon_floor <= 0:
            raise ValueError("epsilon_floor must be positive")
        self._epsilon_floor = epsilon_floor

    def relative_change(self, current: torch.Tensor,
                        previous: torch.Tensor) -> float:
        """Return ||current - previous|| / max(||previous||, epsilon_floor)."""
        if current.shape != previous.shape:
            raise ValueError(
                f"Shape mismatch in latent change: "
                f"{tuple(current.shape)} vs {tuple(previous.shape)}"
            )
        delta = (current - previous).detach()
        ref = previous.detach()
        delta_norm = float(torch.linalg.vector_norm(delta).item())
        ref_norm = float(torch.linalg.vector_norm(ref).item())
        return delta_norm / max(ref_norm, self._epsilon_floor)


@dataclass
class ReasoningIterationStats:
    """Aggregated counters describing a single token's reasoning episode."""

    high_level_iters: int = 0
    low_level_iters_total: int = 0
    converged_high_level: bool = False
    halted_by_safety_cap: bool = False
    final_high_level_change: float = float("nan")
    final_low_level_change: float = float("nan")
    h_reused_from_cache: bool = False


@dataclass
class GenerationReasoningSummary:
    """Aggregated statistics over the full generation episode."""

    tokens_generated: int = 0
    total_high_level_iters: int = 0
    total_low_level_iters: int = 0
    safety_halts: int = 0
    high_level_convergences: int = 0
    h_cache_reuses: int = 0

    def absorb(self, sample: ReasoningIterationStats) -> None:
        """Fold a per-token sample into the running totals."""
        self.tokens_generated += 1
        self.total_high_level_iters += sample.high_level_iters
        self.total_low_level_iters += sample.low_level_iters_total
        if sample.halted_by_safety_cap:
            self.safety_halts += 1
        if sample.converged_high_level:
            self.high_level_convergences += 1
        if sample.h_reused_from_cache:
            self.h_cache_reuses += 1


class SparseHighLevelStateCache:
    """Persists the high-level latent state across consecutive emitted tokens.

    The cache is reset whenever its age in tokens reaches the configured
    persistence horizon, at which point the next reasoning episode begins
    with a zero high-level state. This is the temporal-sparsity mechanism:
    expensive full-stack passes are amortized across multiple emissions.
    """

    def __init__(self, persist_tokens: int):
        if persist_tokens < 1:
            raise ValueError("persist_tokens must be >= 1")
        self._persist_tokens = persist_tokens
        self._state: Optional[torch.Tensor] = None
        self._age: int = 0

    def get_or_init(self, reference: torch.Tensor) -> Tuple[torch.Tensor, bool]:
        """Return the cached high-level state or a zeroed one when stale.

        The boolean flag indicates whether the returned tensor came from a
        live cache hit (True) or a fresh zero initialization (False).
        """
        if (self._state is None
                or self._state.shape != reference.shape
                or self._state.dtype != reference.dtype
                or self._state.device != reference.device
                or self._age >= self._persist_tokens):
            self._state = torch.zeros_like(reference)
            self._age = 0
            return self._state, False
        return self._state, True

    def commit(self, new_state: torch.Tensor) -> None:
        """Store a fresh high-level state and increment the cache age."""
        self._state = new_state.detach()
        self._age += 1

    def invalidate(self) -> None:
        """Drop any cached state and reset the age counter."""
        self._state = None
        self._age = 0


class HierarchicalRecursiveReasoner:
    """Parameter-free hierarchical recursive reasoning over a trained stack.

    The reasoner does not own any learnable parameters. It treats the trained
    TopoGPT2 transformer layers as a deterministic recurrent step function
    and composes them into a two-speed damped fixed-point iteration that
    mirrors HRM, while never violating the activation distribution the
    trained layers expect.

    Algorithm per emitted token:

        1. Run the standard full forward pass once to obtain the baseline
           residual-stream latent z_base and the per-layer kv caches that
           will cross the token boundary. z_base is the trained model's
           native answer for this position.
        2. If recursion is disabled or both iteration budgets are zero,
           return z_base unchanged.
        3. Optionally warm-start z by adding a fraction of the cached
           refinement vector from previous tokens (sparse temporal memory).
        4. Hierarchical refinement, all in residual-stream space:
              for h_step in range(max_high_level_iters):
                  for l_step in range(max_low_level_iters):
                      z <- z + low_level_step * (W_low(z) - z)
                  z <- z + high_level_step * (W_high(z) - z)
           where W_low and W_high are the last low_level_window and
           high_level_window trained layers respectively, invoked with the
           prefix kv cache treated as immutable. Each update is damped, so
           layer inputs remain close to the trained residual-stream
           distribution.
        5. Hard divergence guard: if the iterated latent drifts farther
           from the baseline than max_drift_relative, reset to the baseline
           and abort thinking for this token. This eliminates the
           catastrophic-attractor failure mode without retraining.
        6. Attractor halting per loop, plus a global cap on total layer
           invocations.

    The cached refinement returned to the sparse cache is z_final - z_base,
    a small residual-stream displacement that persists across configurable
    horizons to amortize thinking effort over multiple tokens.
    """

    def __init__(self, layers: List[torch.nn.Module],
                 final_norm: torch.nn.Module,
                 reasoning_config: RecursiveReasoningConfig,
                 logger: logging.Logger):
        if reasoning_config.low_level_window > len(layers):
            raise ValueError(
                f"low_level_window={reasoning_config.low_level_window} "
                f"exceeds number of layers={len(layers)}"
            )
        if reasoning_config.high_level_window > len(layers):
            raise ValueError(
                f"high_level_window={reasoning_config.high_level_window} "
                f"exceeds number of layers={len(layers)}"
            )
        self._layers = layers
        self._final_norm = final_norm
        self._config = reasoning_config
        self._logger = logger
        self._metric = LatentChangeMetric(reasoning_config.latent_change_eps)

    @property
    def num_layers(self) -> int:
        """Return the number of trained transformer layers."""
        return len(self._layers)

    def _full_pass(self, z_in: torch.Tensor,
                   base_kvs: List[Optional[Tuple[torch.Tensor, torch.Tensor]]]
                   ) -> Tuple[torch.Tensor, List[Tuple[torch.Tensor, torch.Tensor]]]:
        """Forward z_in through every layer using base_kvs as immutable prefix cache.

        Returns the layer-stack output and the freshly produced per-layer kv
        caches that incorporate the K and V derived from z_in.
        """
        x = z_in
        produced: List[Tuple[torch.Tensor, torch.Tensor]] = []
        for layer_idx, layer in enumerate(self._layers):
            x, _aux_loss, kv_cache = layer(x, past_kv=base_kvs[layer_idx])
            produced.append(kv_cache)
        return x, produced

    def _window_pass(self, z_in: torch.Tensor,
                     base_kvs: List[Optional[Tuple[torch.Tensor, torch.Tensor]]],
                     window: int) -> torch.Tensor:
        """Forward z_in through the trailing `window` layers only.

        The per-layer kv caches produced during this read-only pass are
        discarded; only the baseline pass's committed kvs cross the token
        boundary, preserving cache consistency across thinking iterations.
        """
        if window <= 0:
            return z_in
        n = self.num_layers
        x = z_in
        for layer_idx in range(n - window, n):
            x, _aux_loss, _kv_cache = self._layers[layer_idx](
                x, past_kv=base_kvs[layer_idx],
            )
        return x

    def reason(self,
               z_initial: torch.Tensor,
               base_kvs: List[Optional[Tuple[torch.Tensor, torch.Tensor]]],
               cached_refinement: Optional[torch.Tensor],
               ) -> Tuple[torch.Tensor,
                          List[Tuple[torch.Tensor, torch.Tensor]],
                          torch.Tensor,
                          ReasoningIterationStats]:
        """Run hierarchical recursive thinking for a single emission step.

        Args:
            z_initial: token embedding of the new position, shape [B, 1, D].
            base_kvs: per-layer kv cache for all previously emitted tokens,
                treated as immutable during thinking iterations.
            cached_refinement: persistent refinement displacement from prior
                tokens, or None to skip the warm start.

        Returns:
            A tuple (z_final, committed_kvs, refinement_for_cache, stats):
                z_final is the latent state about to enter the final norm
                and lm head; committed_kvs is the new per-layer kv cache
                including this token's K and V from the baseline pass;
                refinement_for_cache is z_final - z_baseline, to be
                persisted across tokens; stats holds the loop counters.
        """
        cfg = self._config
        stats = ReasoningIterationStats()

        z_baseline, committed_kvs = self._full_pass(z_initial, base_kvs)

        recursion_requested = (cfg.enabled
                               and (cfg.max_high_level_iters > 0
                                    or cfg.max_low_level_iters > 0))
        if not recursion_requested:
            return (z_baseline, committed_kvs,
                    torch.zeros_like(z_baseline), stats)

        z = z_baseline
        if (cached_refinement is not None
                and cached_refinement.shape == z_baseline.shape):
            z = z + cfg.cache_warm_start_weight * cached_refinement
            stats.h_reused_from_cache = True

        total_layer_calls = 0
        low_change = float("nan")
        high_change = float("nan")

        for h_step in range(cfg.max_high_level_iters):
            for l_step in range(cfg.max_low_level_iters):
                z_new = self._window_pass(z, base_kvs, cfg.low_level_window)
                delta = z_new - z
                low_change = self._metric.relative_change(z_new, z)
                z = z + cfg.low_level_step * delta
                total_layer_calls += cfg.low_level_window
                stats.low_level_iters_total += 1
                stats.final_low_level_change = low_change

                drift = self._metric.relative_change(z, z_baseline)
                if drift > cfg.max_drift_relative:
                    z = z_baseline
                    stats.halted_by_safety_cap = True
                    break
                if (l_step + 1 >= cfg.minimum_low_level_iters
                        and low_change < cfg.attractor_low_epsilon):
                    break
                if total_layer_calls >= cfg.safety_max_total_iterations:
                    stats.halted_by_safety_cap = True
                    break

            if stats.halted_by_safety_cap:
                break

            z_new = self._window_pass(z, base_kvs, cfg.high_level_window)
            delta = z_new - z
            high_change = self._metric.relative_change(z_new, z)
            z = z + cfg.high_level_step * delta
            total_layer_calls += cfg.high_level_window
            stats.high_level_iters += 1
            stats.final_high_level_change = high_change

            drift = self._metric.relative_change(z, z_baseline)
            if drift > cfg.max_drift_relative:
                z = z_baseline
                stats.halted_by_safety_cap = True
                break
            if (h_step + 1 >= cfg.minimum_high_level_iters
                    and high_change < cfg.attractor_high_epsilon):
                stats.converged_high_level = True
                break
            if total_layer_calls >= cfg.safety_max_total_iterations:
                stats.halted_by_safety_cap = True
                break

        refinement_for_cache = (z - z_baseline).detach()

        if cfg.diagnostic_logging:
            self._logger.debug(
                "HRM token: h_iters=%d l_iters=%d converged=%s safety=%s "
                "h_change=%.3e l_change=%.3e h_reused=%s",
                stats.high_level_iters, stats.low_level_iters_total,
                stats.converged_high_level, stats.halted_by_safety_cap,
                stats.final_high_level_change, stats.final_low_level_change,
                stats.h_reused_from_cache,
            )

        return z, committed_kvs, refinement_for_cache, stats


class LogitsSampler:
    """Applies temperature, repetition penalty, top-k filtering and multinomial draw."""

    def __init__(self, logger: logging.Logger):
        self._logger = logger

    def sample(self, logits: torch.Tensor, token_history: torch.Tensor,
               temperature: float, top_k: int,
               repetition_penalty: float) -> torch.Tensor:
        """Return a sampled token id tensor of shape [B, 1] from raw logits [B, V]."""
        if temperature <= 0:
            raise ValueError("temperature must be positive at sampling time")
        scaled = logits / temperature
        if repetition_penalty != 1.0:
            mask = torch.zeros_like(scaled, dtype=torch.bool)
            mask.scatter_(1, token_history, True)
            scaled = torch.where(mask, scaled / repetition_penalty, scaled)
        if top_k > 0:
            effective_k = min(top_k, scaled.size(-1))
            top_values, _ = torch.topk(scaled, effective_k)
            threshold = top_values[:, -1:].expand_as(scaled)
            scaled = torch.where(scaled < threshold,
                                 torch.full_like(scaled, float("-inf")), scaled)
        probabilities = F.softmax(scaled, dim=-1)
        return torch.multinomial(probabilities, 1)


@dataclass(frozen=True)
class SamplingPolicy:
    """Immutable sampling parameters consumed by the generation engine."""

    max_new_tokens: int
    temperature: float
    top_k: int
    repetition_penalty: float
    end_of_text_token_id: int

    @classmethod
    def from_settings(cls, settings: HRMInferenceSettings) -> "SamplingPolicy":
        """Construct a SamplingPolicy from inference settings."""
        return cls(
            max_new_tokens=settings.max_new_tokens,
            temperature=settings.temperature,
            top_k=settings.top_k,
            repetition_penalty=settings.repetition_penalty,
            end_of_text_token_id=settings.end_of_text_token_id,
        )


@dataclass(frozen=True)
class GenerationReport:
    """Quantitative summary of a single generation call."""

    prompt: str
    output: str
    prompt_tokens: int
    new_tokens: int
    elapsed_seconds: float
    reasoning_summary: GenerationReasoningSummary

    def tokens_per_second(self, elapsed_floor: float) -> float:
        """Return throughput in tokens/sec, clamped to avoid divide-by-zero."""
        return self.new_tokens / max(self.elapsed_seconds, elapsed_floor)


class HRMGenerationEngine:
    """Runs autoregressive sampling driven by hierarchical recursive reasoning.

    The engine reimplements the prompt encoding and token emission loop so
    that the per-token latent state can be intercepted before final norm and
    LM-head projection. The intercepted state is handed to a
    HierarchicalRecursiveReasoner, which iterates the trained layer stack in
    a two-speed loop until the attractor is reached. The final stabilized
    latent is then projected to logits and sampled in the standard fashion.
    """

    def __init__(self, settings: HRMInferenceSettings, logger: logging.Logger):
        self._settings = settings
        self._logger = logger
        self._sampler = LogitsSampler(logger)

    def _encode_prompt(self, model: torch.nn.Module, prompt_ids: List[int]
                       ) -> Tuple[torch.Tensor,
                                  List[Tuple[torch.Tensor, torch.Tensor]],
                                  torch.Tensor]:
        """Run the prompt through the full stack once, returning the final
        hidden state of the last position, the per-layer base kv caches that
        cover all prompt tokens except the last one, and the embedding of the
        last prompt token as the seed for the first reasoning episode.
        """
        device = self._settings.device
        if len(prompt_ids) < 1:
            raise ValueError("Prompt must contain at least one token")

        token_tensor = torch.tensor([prompt_ids], dtype=torch.long, device=device)
        if len(prompt_ids) == 1:
            base_kvs: List[Optional[Tuple[torch.Tensor, torch.Tensor]]] = [
                None for _ in model.layers
            ]
            seed_embed = model.token_embed(token_tensor)
            return seed_embed, base_kvs, token_tensor

        prefix_tokens = token_tensor[:, :-1]
        last_token = token_tensor[:, -1:]
        x = model.token_embed(prefix_tokens)
        base_kvs_built: List[Tuple[torch.Tensor, torch.Tensor]] = []
        for layer in model.layers:
            x, _aux_loss, kv_cache = layer(x, past_kv=None)
            base_kvs_built.append(kv_cache)
        seed_embed = model.token_embed(last_token)
        return seed_embed, base_kvs_built, token_tensor

    @torch.no_grad()
    def run(self, model: torch.nn.Module, tokenizer: Any, prompt: str,
            policy: SamplingPolicy) -> GenerationReport:
        """Generate a completion for prompt and return a GenerationReport."""
        prompt_ids = tokenizer.encode(prompt)
        if len(prompt_ids) == 0:
            raise ValueError("Prompt encodes to zero tokens; refusing to generate.")

        device = self._settings.device
        reasoning_cfg = self._settings.reasoning
        reasoner = HierarchicalRecursiveReasoner(
            layers=list(model.layers),
            final_norm=model.final_norm,
            reasoning_config=reasoning_cfg,
            logger=self._logger,
        )
        h_cache = SparseHighLevelStateCache(
            persist_tokens=reasoning_cfg.high_level_persist_tokens,
        )
        summary = GenerationReasoningSummary()

        self._logger.info(
            "Sampling: temp=%.3f top_k=%d rep_pen=%.3f max_new=%d "
            "prompt_tokens=%d hrm_enabled=%s h_iters=%d l_iters=%d "
            "l_window=%d persist=%d",
            policy.temperature, policy.top_k, policy.repetition_penalty,
            policy.max_new_tokens, len(prompt_ids), reasoning_cfg.enabled,
            reasoning_cfg.max_high_level_iters,
            reasoning_cfg.max_low_level_iters,
            reasoning_cfg.low_level_window,
            reasoning_cfg.high_level_persist_tokens,
        )

        start = time.time()
        z_seed, base_kvs, full_history = self._encode_prompt(model, prompt_ids)

        emitted_ids: List[int] = []
        z_input = z_seed
        active_history = full_history

        for new_token_index in range(policy.max_new_tokens):
            cached_refinement, _hit = h_cache.get_or_init(z_input)
            z_final, committed_kvs, refinement_next, stats = reasoner.reason(
                z_initial=z_input,
                base_kvs=base_kvs,
                cached_refinement=cached_refinement,
            )
            summary.absorb(stats)
            base_kvs = list(committed_kvs)
            h_cache.commit(refinement_next)

            hidden = model.final_norm(z_final)
            logits = model.lm_head(hidden)[:, -1, :]
            next_tok = self._sampler.sample(
                logits=logits,
                token_history=active_history,
                temperature=policy.temperature,
                top_k=policy.top_k,
                repetition_penalty=policy.repetition_penalty,
            )
            next_id = int(next_tok.item())
            emitted_ids.append(next_id)
            active_history = torch.cat([active_history, next_tok], dim=1)

            if next_id == policy.end_of_text_token_id:
                break

            z_input = model.token_embed(next_tok)

        elapsed = time.time() - start
        full_text = tokenizer.decode(active_history[0].tolist())
        return GenerationReport(
            prompt=prompt,
            output=full_text,
            prompt_tokens=len(prompt_ids),
            new_tokens=len(emitted_ids),
            elapsed_seconds=elapsed,
            reasoning_summary=summary,
        )


class ResultRenderer:
    """Prints a GenerationReport to stdout using settings-defined formatting."""

    def __init__(self, settings: HRMInferenceSettings, logger: logging.Logger):
        self._settings = settings
        self._logger = logger

    def render(self, report: GenerationReport) -> None:
        """Emit a banner with prompt, completion, throughput and reasoning stats."""
        s = self._settings
        sep = s.result_separator_char * s.result_separator_width
        completion = (
            report.output[len(report.prompt):]
            if report.output.startswith(report.prompt)
            else report.output
        )
        summary = report.reasoning_summary
        avg_h = (summary.total_high_level_iters / summary.tokens_generated
                 if summary.tokens_generated > 0 else 0.0)
        avg_l = (summary.total_low_level_iters / summary.tokens_generated
                 if summary.tokens_generated > 0 else 0.0)
        self._logger.info(
            "Generated %d new tokens in %.2fs (%.1f tok/s)",
            report.new_tokens, report.elapsed_seconds,
            report.tokens_per_second(s.elapsed_floor_seconds),
        )
        self._logger.info(
            "%s: avg_h=%.2f avg_l=%.2f h_converged=%d safety_halts=%d "
            "h_cache_reuses=%d",
            s.reasoning_label, avg_h, avg_l,
            summary.high_level_convergences, summary.safety_halts,
            summary.h_cache_reuses,
        )
        out = sys.stdout
        out.write("\n" + sep + "\n")
        out.write(f"[{s.prompt_label}] {report.prompt}\n")
        out.write(f"[{s.completion_label}]\n{completion}\n")
        out.write(sep + "\n")
        out.flush()


class HRMInferencePipeline:
    """Orchestrator wiring loader, builder, reasoner, engine and renderer."""

    def __init__(self, settings: HRMInferenceSettings,
                 logger: Optional[logging.Logger] = None):
        settings.validate()
        self._settings = settings
        self._logger = logger or HRMLoggerFactory.build(settings)

    def execute(self) -> GenerationReport:
        """Run the full inference pipeline end-to-end and return the report."""
        source_module = SourceModuleLoader(
            self._settings, self._logger,
        ).load()

        SeedSynchronizer(
            self._settings, source_module, self._logger,
        ).apply()

        GaussPatchApplier(
            self._settings, source_module, self._logger,
        ).apply_if_enabled()

        paths = CheckpointPaths(self._settings)
        paths.assert_ready()

        preset = self._settings.preset()
        n_kv = WeightShapeProbe(
            self._settings, self._logger,
        ).detect_n_kv_heads(
            paths.model_file(),
            d_model=preset.d_model,
            n_heads=preset.n_heads,
        )

        tokenizer = TokenizerFactory(self._settings, source_module).build()
        aligned_cfg = TopoGPT2ConfigAligner(
            self._settings, source_module, self._logger,
        ).build(n_kv_heads=n_kv, vocab_size=tokenizer.vocab_size)

        model = ModelAssembler(
            self._settings, source_module, self._logger,
        ).assemble(aligned_cfg, paths)

        engine = HRMGenerationEngine(self._settings, self._logger)
        report = engine.run(
            model, tokenizer, self._settings.prompt,
            SamplingPolicy.from_settings(self._settings),
        )
        ResultRenderer(self._settings, self._logger).render(report)
        return report


class CliArgumentParser:
    """Translates command-line arguments into an HRMInferenceSettings instance."""

    @staticmethod
    def build_parser() -> argparse.ArgumentParser:
        """Return the configured argparse.ArgumentParser."""
        defaults = HRMInferenceSettings()
        reasoning_defaults = defaults.reasoning
        parser = argparse.ArgumentParser(
            description=(
                "TopoGPT3.1 inference engine: hierarchical recursive reasoning "
                "over a parameter-frozen TopoGPT3 checkpoint."
            ),
        )
        parser.add_argument(
            "--prompt", type=str, default=defaults.prompt,
            help="Code prefix to complete.",
        )
        parser.add_argument(
            "--scale", type=str, default=defaults.model_scale,
            choices=sorted(HRMInferenceSettings.scale_presets().keys()),
            help="Model scale preset.",
        )
        parser.add_argument(
            "--max-new", type=int, default=defaults.max_new_tokens,
            help="Maximum number of new tokens to generate.",
        )
        parser.add_argument(
            "--temp", type=float, default=defaults.temperature,
            help="Sampling temperature (lower means more deterministic).",
        )
        parser.add_argument(
            "--top-k", type=int, default=defaults.top_k,
            help="Top-k filtering (0 disables it).",
        )
        parser.add_argument(
            "--rep-penalty", type=float, default=defaults.repetition_penalty,
            help="Repetition penalty (values above 1 reduce repeats).",
        )
        parser.add_argument(
            "--device", type=str, default=defaults.device,
            help="Compute device, e.g. cuda, cpu, cuda:0.",
        )
        parser.add_argument(
            "--ckpt-dir", type=str, default=defaults.checkpoint_dir,
            help="Root directory holding TopoGPT3 checkpoints.",
        )
        parser.add_argument(
            "--ckpt-name", type=str, default=defaults.checkpoint_name,
            help="Checkpoint slot to load (e.g. 'last').",
        )
        parser.add_argument(
            "--source-dir", type=str, default=defaults.source_directory,
            help="Directory containing train.py and model.py.",
        )
        parser.add_argument(
            "--no-gauss", action="store_true",
            help="Disable the Gauss complex-multiply patch at load.",
        )
        parser.add_argument(
            "--strict-load", action="store_true",
            help="Require strict state_dict matching when loading weights.",
        )
        parser.add_argument(
            "--seed", type=int, default=defaults.seed,
            help="Deterministic seed for sampling reproducibility.",
        )
        parser.add_argument(
            "--log-level", type=str, default=defaults.log_level,
            choices=["DEBUG", "INFO", "WARNING", "ERROR"],
            help="Logging verbosity.",
        )
        parser.add_argument(
            "--disable-hrm", action="store_true",
            help="Disable hierarchical recursive reasoning (fallback to "
                 "standard autoregressive generation).",
        )
        parser.add_argument(
            "--hrm-h-iters", type=int,
            default=reasoning_defaults.max_high_level_iters,
            help="Maximum high-level (slow) iterations per emitted token.",
        )
        parser.add_argument(
            "--hrm-l-iters", type=int,
            default=reasoning_defaults.max_low_level_iters,
            help="Maximum low-level (fast) iterations per high-level step.",
        )
        parser.add_argument(
            "--hrm-l-window", type=int,
            default=reasoning_defaults.low_level_window,
            help="Number of trailing layers used by the low-level loop.",
        )
        parser.add_argument(
            "--hrm-h-window", type=int,
            default=reasoning_defaults.high_level_window,
            help="Number of trailing layers used by the high-level loop "
                 "(must be >= --hrm-l-window).",
        )
        parser.add_argument(
            "--hrm-l-step", type=float,
            default=reasoning_defaults.low_level_step,
            help="Damping coefficient for the low-level update in [0, 1].",
        )
        parser.add_argument(
            "--hrm-h-step", type=float,
            default=reasoning_defaults.high_level_step,
            help="Damping coefficient for the high-level update in [0, 1].",
        )
        parser.add_argument(
            "--hrm-persist", type=int,
            default=reasoning_defaults.high_level_persist_tokens,
            help="Tokens during which the refinement vector is reused as a "
                 "warm start before being re-initialized.",
        )
        parser.add_argument(
            "--hrm-warm-start", type=float,
            default=reasoning_defaults.cache_warm_start_weight,
            help="Scalar in [0, 1] applied to the cached refinement vector "
                 "when warm-starting the next token's iteration.",
        )
        parser.add_argument(
            "--hrm-max-drift", type=float,
            default=reasoning_defaults.max_drift_relative,
            help="Relative L2 ceiling between the iterated latent and the "
                 "baseline; exceeding it aborts thinking and resets to "
                 "baseline for the current token.",
        )
        parser.add_argument(
            "--hrm-low-eps", type=float,
            default=reasoning_defaults.attractor_low_epsilon,
            help="Relative L2 threshold halting the low-level loop.",
        )
        parser.add_argument(
            "--hrm-high-eps", type=float,
            default=reasoning_defaults.attractor_high_epsilon,
            help="Relative L2 threshold halting the high-level loop.",
        )
        parser.add_argument(
            "--hrm-safety-cap", type=int,
            default=reasoning_defaults.safety_max_total_iterations,
            help="Hard cap on total layer invocations per emitted token.",
        )
        parser.add_argument(
            "--hrm-diagnostic", action="store_true",
            help="Enable per-token HRM diagnostic logging.",
        )
        return parser

    @staticmethod
    def parse(argv: Optional[List[str]] = None) -> HRMInferenceSettings:
        """Parse argv (or sys.argv) and return a populated HRMInferenceSettings."""
        namespace = CliArgumentParser.build_parser().parse_args(argv)
        defaults = HRMInferenceSettings()
        reasoning_defaults = defaults.reasoning
        reasoning = RecursiveReasoningConfig(
            enabled=not namespace.disable_hrm,
            max_high_level_iters=namespace.hrm_h_iters,
            max_low_level_iters=namespace.hrm_l_iters,
            low_level_window=namespace.hrm_l_window,
            high_level_window=namespace.hrm_h_window,
            low_level_step=namespace.hrm_l_step,
            high_level_step=namespace.hrm_h_step,
            attractor_low_epsilon=namespace.hrm_low_eps,
            attractor_high_epsilon=namespace.hrm_high_eps,
            high_level_persist_tokens=namespace.hrm_persist,
            cache_warm_start_weight=namespace.hrm_warm_start,
            max_drift_relative=namespace.hrm_max_drift,
            latent_change_eps=reasoning_defaults.latent_change_eps,
            safety_max_total_iterations=namespace.hrm_safety_cap,
            minimum_low_level_iters=reasoning_defaults.minimum_low_level_iters,
            minimum_high_level_iters=reasoning_defaults.minimum_high_level_iters,
            diagnostic_logging=namespace.hrm_diagnostic,
        )
        return HRMInferenceSettings(
            prompt=namespace.prompt,
            model_scale=namespace.scale,
            max_new_tokens=namespace.max_new,
            temperature=namespace.temp,
            top_k=namespace.top_k,
            repetition_penalty=namespace.rep_penalty,
            device=namespace.device,
            checkpoint_dir=namespace.ckpt_dir,
            checkpoint_name=namespace.ckpt_name,
            source_directory=namespace.source_dir,
            apply_gauss_patch_at_load=not namespace.no_gauss,
            strict_state_dict=namespace.strict_load,
            seed=namespace.seed,
            log_level=namespace.log_level,
            reasoning=reasoning,
        )


def main(argv: Optional[List[str]] = None) -> int:
    """CLI entry point. Returns a process exit code."""
    settings = CliArgumentParser.parse(argv)
    HRMInferencePipeline(settings).execute()
    return 0


if __name__ == "__main__":
    sys.exit(main())
