#!/usr/bin/env python3
"""
TopoGPT3 inference engine.

Production-grade autoregressive code completion pipeline for TopoGPT3
checkpoints. Loads weights from safetensors, aligns the underlying TopoGPT2
architecture against the stored tensors, optionally applies the Gauss
complex-multiply patch for numerical parity with training, and performs
sampling with repetition penalty and top-k filtering.

The pipeline is decomposed into single-responsibility collaborators wired by
an orchestrator. All paths, sampling parameters, safety bounds and string
identifiers live inside InferenceSettings so that business logic contains no
magic numbers or hardcoded constants.
"""
from __future__ import annotations

import argparse
import logging
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Mapping, Optional

import torch
from safetensors import safe_open
from safetensors.torch import load_file


@dataclass(frozen=True)
class ScalePreset:
    """Immutable architecture preset for a named model scale."""

    d_model: int
    n_heads: int
    n_layers: int
    max_seq_len: int


@dataclass
class InferenceSettings:
    """Centralized configuration container for the inference pipeline.

    Every value consumed downstream resides here. Adding a new tunable means
    extending this class; no other module should embed literals.
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
    auto_continue: bool = False
    max_continuations: int = 3
    continuation_tail_lines: int = 2

    log_level: str = "INFO"
    log_name: str = "TopoGPT3Inference"
    log_format: str = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    log_date_format: str = "%Y-%m-%d %H:%M:%S"

    result_separator_char: str = "="
    result_separator_width: int = 72
    prompt_label: str = "PROMPT"
    completion_label: str = "COMPLETION"
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

    runtime_module_alias: str = "topogpt3_inference_runtime"

    @staticmethod
    def scale_presets() -> Mapping[str, ScalePreset]:
        """Return the architecture preset table indexed by scale name."""
        return {
            "micro":  ScalePreset(d_model=64,  n_heads=4,  n_layers=2,
                                  max_seq_len=256),
            "small":  ScalePreset(d_model=256, n_heads=8,  n_layers=6,
                                  max_seq_len=512),
            "medium": ScalePreset(d_model=512, n_heads=8,  n_layers=12,
                                  max_seq_len=1024),
            "gpt2":   ScalePreset(d_model=768, n_heads=12, n_layers=12,
                                  max_seq_len=2048),
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
        self.preset()


class InferenceLoggerFactory:
    """Builds a stdout-attached logger from inference settings."""

    @staticmethod
    def build(settings: InferenceSettings) -> logging.Logger:
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
        """Join `parts` under `root` and return the canonical resolved path.

        Raises ValueError if the resolved path escapes `root`.
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
        """Validate `path` points to an existing regular file with the expected suffix."""
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

    def __init__(self, settings: InferenceSettings, logger: logging.Logger):
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

    def __init__(self, settings: InferenceSettings):
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

    def __init__(self, settings: InferenceSettings, logger: logging.Logger):
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
                    "falling back to scale defaults.",
                    probe_key,
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

    def __init__(self, settings: InferenceSettings, source_module: Any,
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

    def __init__(self, settings: InferenceSettings, source_module: Any):
        self._settings = settings
        self._source = source_module

    def build(self) -> Any:
        """Return an instance of BPETokenizer bound to the configured encoding."""
        tokenizer_cls = getattr(self._source, "BPETokenizer")
        return tokenizer_cls(self._settings.tokenizer_encoding)


class GaussPatchApplier:
    """Applies the idempotent Gauss complex-multiply patch when enabled."""

    def __init__(self, settings: InferenceSettings, source_module: Any,
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

    def __init__(self, settings: InferenceSettings, source_module: Any,
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
        self._logger.info("Weights loaded successfully.")
        return model


class SeedSynchronizer:
    """Applies deterministic seeds across torch, CUDA and the model package."""

    def __init__(self, settings: InferenceSettings, source_module: Any,
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


@dataclass(frozen=True)
class SamplingPolicy:
    """Immutable sampling parameters consumed by the generation engine."""

    max_new_tokens: int
    temperature: float
    top_k: int
    repetition_penalty: float

    @classmethod
    def from_settings(cls, settings: InferenceSettings) -> "SamplingPolicy":
        """Construct a SamplingPolicy from inference settings."""
        return cls(
            max_new_tokens=settings.max_new_tokens,
            temperature=settings.temperature,
            top_k=settings.top_k,
            repetition_penalty=settings.repetition_penalty,
        )


@dataclass(frozen=True)
class GenerationReport:
    """Quantitative summary of a single generation call."""

    prompt: str
    output: str
    prompt_tokens: int
    new_tokens: int
    elapsed_seconds: float

    def tokens_per_second(self, elapsed_floor: float) -> float:
        """Return throughput in tokens/sec, clamped to avoid divide-by-zero."""
        return self.new_tokens / max(self.elapsed_seconds, elapsed_floor)


class GenerationEngine:
    """Runs autoregressive sampling against a loaded model and tokenizer."""

    def __init__(self, settings: InferenceSettings, logger: logging.Logger):
        self._settings = settings
        self._logger = logger

    @torch.no_grad()
    def run(self, model: torch.nn.Module, tokenizer: Any, prompt: str,
            policy: SamplingPolicy) -> GenerationReport:
        """Generate a completion for `prompt` and return a GenerationReport."""
        prompt_ids = tokenizer.encode(prompt)
        if len(prompt_ids) == 0:
            raise ValueError("Prompt encodes to zero tokens; refusing to generate.")

        device = self._settings.device
        input_ids = torch.tensor([prompt_ids], dtype=torch.long, device=device)

        self._logger.info(
            "Sampling: temp=%.3f top_k=%d rep_pen=%.3f "
            "max_new=%d prompt_tokens=%d",
            policy.temperature, policy.top_k, policy.repetition_penalty,
            policy.max_new_tokens, len(prompt_ids),
        )

        start = time.time()
        if self._settings.auto_continue:
            output_ids = model.generate_with_continuation(
                input_ids,
                tokenizer=tokenizer,
                max_new_tokens=policy.max_new_tokens,
                temperature=policy.temperature,
                top_k=policy.top_k,
                repetition_penalty=policy.repetition_penalty,
                max_continuations=self._settings.max_continuations,
                tail_lines=self._settings.continuation_tail_lines,
            )
        else:
            output_ids = model.generate(
                input_ids,
                max_new_tokens=policy.max_new_tokens,
                temperature=policy.temperature,
                top_k=policy.top_k,
                repetition_penalty=policy.repetition_penalty,
            )
        elapsed = time.time() - start

        full_text = tokenizer.decode(output_ids[0].tolist())
        new_tokens = int(output_ids.shape[1]) - len(prompt_ids)
        return GenerationReport(
            prompt=prompt,
            output=full_text,
            prompt_tokens=len(prompt_ids),
            new_tokens=new_tokens,
            elapsed_seconds=elapsed,
        )


class ResultRenderer:
    """Prints a GenerationReport to stdout using settings-defined formatting."""

    def __init__(self, settings: InferenceSettings, logger: logging.Logger):
        self._settings = settings
        self._logger = logger

    def render(self, report: GenerationReport) -> None:
        """Emit a banner with prompt and completion, plus a throughput log line."""
        s = self._settings
        sep = s.result_separator_char * s.result_separator_width
        completion = (
            report.output[len(report.prompt):]
            if report.output.startswith(report.prompt)
            else report.output
        )
        self._logger.info(
            "Generated %d new tokens in %.2fs (%.1f tok/s)",
            report.new_tokens, report.elapsed_seconds,
            report.tokens_per_second(s.elapsed_floor_seconds),
        )
        out = sys.stdout
        out.write("\n" + sep + "\n")
        out.write(f"[{s.prompt_label}] {report.prompt}\n")
        out.write(f"[{s.completion_label}]\n{completion}\n")
        out.write(sep + "\n")
        out.flush()


class InferencePipeline:
    """Orchestrator wiring loader, builder, engine and renderer."""

    def __init__(self, settings: InferenceSettings,
                 logger: Optional[logging.Logger] = None):
        settings.validate()
        self._settings = settings
        self._logger = logger or InferenceLoggerFactory.build(settings)

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

        engine = GenerationEngine(self._settings, self._logger)
        report = engine.run(
            model, tokenizer, self._settings.prompt,
            SamplingPolicy.from_settings(self._settings),
        )
        ResultRenderer(self._settings, self._logger).render(report)
        return report


class CliArgumentParser:
    """Translates command-line arguments into an InferenceSettings instance."""

    @staticmethod
    def build_parser() -> argparse.ArgumentParser:
        """Return the configured argparse.ArgumentParser."""
        defaults = InferenceSettings()
        parser = argparse.ArgumentParser(
            description=(
                "TopoGPT3 inference engine "
                "(Grassmannian-trained, Gauss complex-multiply enabled)."
            ),
        )
        parser.add_argument(
            "--prompt", type=str, default=defaults.prompt,
            help="Code prefix to complete.",
        )
        parser.add_argument(
            "--scale", type=str, default=defaults.model_scale,
            choices=sorted(InferenceSettings.scale_presets().keys()),
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
            "--auto-continue", "-C", action="store_true",
            default=defaults.auto_continue,
            help="Auto-continue truncated responses by feeding tail lines back.",
        )
        parser.add_argument(
            "--max-continuations", type=int, default=defaults.max_continuations,
            help="Max number of continuation rounds (requires --auto-continue).",
        )
        parser.add_argument(
            "--log-level", type=str, default=defaults.log_level,
            choices=["DEBUG", "INFO", "WARNING", "ERROR"],
            help="Logging verbosity.",
        )
        return parser

    @staticmethod
    def parse(argv: Optional[List[str]] = None) -> InferenceSettings:
        """Parse `argv` (or sys.argv) and return a populated InferenceSettings."""
        namespace = CliArgumentParser.build_parser().parse_args(argv)
        return InferenceSettings(
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
            auto_continue=namespace.auto_continue,
            max_continuations=namespace.max_continuations,
            log_level=namespace.log_level,
        )


def main(argv: Optional[List[str]] = None) -> int:
    """CLI entry point. Returns a process exit code."""
    settings = CliArgumentParser.parse(argv)
    InferencePipeline(settings).execute()
    return 0


if __name__ == "__main__":
    sys.exit(main())
