from __future__ import annotations

import json
from collections.abc import Sequence
from dataclasses import dataclass, field
from pathlib import Path
from types import SimpleNamespace
from typing import Any, Protocol

import torch
from torch import nn
from safetensors.torch import load_file


__all__ = [
    "LensModel",
    "TopoGPT3LensConfig",
    "TopoGPT3LensModel",
    "TinyDecoder",
]


class LensModel(Protocol):
    """What the lens needs from a model.

    Attributes:
        n_layers: Number of residual blocks.
        d_model: Residual-stream width.
        layers: The residual blocks, indexable by integer; what
            ActivationRecorder hooks.
        tokenizer: Tokenizer used by the visualisation helpers; must provide
            ``decode(token_ids) -> str``. Fitting and apply() never touch it.
    """

    n_layers: int
    d_model: int
    layers: Sequence[nn.Module]
    tokenizer: Any

    def encode(self, text: str, *, max_length: int = ...) -> torch.Tensor:
        """Tokenize ``text`` to ``input_ids`` of shape ``[1, seq_len]`` on the
        model's input device."""
        ...

    def forward(self, input_ids: torch.Tensor) -> Any:
        """Run the residual stack on ``input_ids`` (no LM head). Must build an
        autograd graph through layers when grad is enabled, and must be
        deterministic across batch elements (eval mode, dropout off) --- the
        fitting estimator replicates the prompt along the batch axis."""
        ...

    def unembed(self, residual: torch.Tensor) -> torch.Tensor:
        """Map a residual-stream tensor ``[..., d_model]`` to logits
        ``[..., vocab_size]`` (final norm + LM head)."""
        ...


@dataclass(frozen=True)
class TopoGPT3LensConfig:
    """Centralized configuration for the TopoGPT3 lens model adapter.

    Every value consumed downstream resides here. Adding a new tunable means
    extending this class; no other module should embed literals.
    """

    d_model: int = 256
    n_layers: int = 6
    n_heads: int = 8
    n_kv_heads: int = 0
    vocab_size: int = 50257
    max_seq_len: int = 256
    dropout: float = 0.1
    device: str = field(
        default_factory=lambda: "cuda" if torch.cuda.is_available() else "cpu"
    )
    encoding: str = "gpt2"
    scale: str = "small"
    moe_enabled: bool = True
    n_experts: int = 4
    moe_top_k: int = 2
    gradient_checkpointing: bool = True

    @classmethod
    def from_topogpt2_config(cls, cfg: Any) -> TopoGPT3LensConfig:
        """Construct a lens config from a TopoGPT2Config dataclass."""
        return cls(
            d_model=cfg.D_MODEL,
            n_layers=cfg.N_LAYERS,
            n_heads=cfg.N_HEADS,
            n_kv_heads=getattr(cfg, "N_KV_HEADS", 0),
            vocab_size=cfg.VOCAB_SIZE,
            max_seq_len=cfg.MAX_SEQ_LEN,
            dropout=cfg.DROPOUT,
            device=cfg.DEVICE,
            encoding=getattr(cfg, "ENCODING", "gpt2"),
            scale=cfg.SCALE,
            moe_enabled=cfg.MOE_ENABLED,
            n_experts=cfg.N_EXPERTS,
            moe_top_k=cfg.MOE_TOP_K,
            gradient_checkpointing=cfg.GRADIENT_CHECKPOINTING,
        )

    @classmethod
    def probe_checkpoint(
        cls,
        checkpoint_dir: str = "checkpoints_topogpt3",
        *,
        state_filename: str = "state.json",
    ) -> TopoGPT3LensConfig:
        """Probe a checkpoint directory and infer lens config from state.json.

        Args:
            checkpoint_dir: Path to the checkpoint slot directory.
            state_filename: JSON file containing training config.

        Returns:
            A TopoGPT3LensConfig matching the checkpoint.

        Raises:
            FileNotFoundError: If state.json is missing.
            ValueError: If required fields are absent from the state.
        """
        state_path = Path(checkpoint_dir) / state_filename
        if not state_path.exists():
            raise FileNotFoundError(
                f"State file not found at {state_path}. "
                f"Provide a valid checkpoint directory."
            )
        with open(state_path) as f:
            state = json.load(f)
        raw = state.get("config", state)
        scale = raw.get("SCALE", "small")
        from .model import TopoGPT2Config
        cfg = TopoGPT2Config(SCALE=scale, DEVICE="cpu")
        for k, v in cfg.__dataclass_fields__.items():
            if k in raw and isinstance(raw[k], type(getattr(cfg, k, None))):
                setattr(cfg, k, raw[k])
        cfg.__post_init__()
        return cls.from_topogpt2_config(cfg)


class _TopoGPT3ResidualForward(nn.Module):
    """Runs the residual block stack only (no final norm, no LM head).

    This is the forward subgraph that ActivationRecorder hooks capture.
    Extracted from TopoGPT2.forward() to expose the residual stream for
    Jacobian lens fitting and application.
    """

    def __init__(self, model: nn.Module) -> None:
        super().__init__()
        self._model = model

    def forward(self, input_ids: torch.Tensor) -> torch.Tensor:
        x = self._model.token_embed(input_ids)
        for layer in self._model.layers:
            x, _aux_loss, _kv_cache = layer(x, past_kv=None)
        return x


class TopoGPT3LensModel(nn.Module):
    """LensModel adapter over a loaded TopoGPT2 model.

    Wraps a TopoGPT2 instance and implements the LensModel protocol for use
    with ActivationRecorder, JacobianLens fitting, and apply().

    The adapter owns no parameters --- all weights live in the wrapped model.
    Call ``.eval()`` and set ``requires_grad_(False)`` on the wrapped model
    before fitting.
    """

    def __init__(
        self,
        model: nn.Module,
        tokenizer: Any | None = None,
    ) -> None:
        super().__init__()
        self._model = model
        self._residual_forward = _TopoGPT3ResidualForward(model)
        self._tokenizer = tokenizer
        self._input_device: torch.device | None = None

    @property
    def n_layers(self) -> int:
        return len(self._model.layers)

    @property
    def d_model(self) -> int:
        return self._model.config.D_MODEL

    @property
    def layers(self) -> nn.ModuleList:
        return self._model.layers

    @property
    def tokenizer(self) -> Any:
        return self._tokenizer

    @tokenizer.setter
    def tokenizer(self, tok: Any) -> None:
        self._tokenizer = tok

    @property
    def input_device(self) -> torch.device:
        if self._input_device is not None:
            return self._input_device
        return self._model.token_embed.weight.device

    @input_device.setter
    def input_device(self, device: torch.device) -> None:
        self._input_device = device

    def encode(self, text: str, *, max_length: int = 512) -> torch.Tensor:
        """Tokenize text to input_ids of shape ``[1, seq_len]``.

        Uses BPETokenizer if available, otherwise falls back to a byte-level
        encoding compatible with GPT-2 BPE tokenization.
        """
        if self._tokenizer is not None:
            ids = self._tokenizer.encode(text)
            if max_length and len(ids) > max_length:
                ids = ids[:max_length]
            return torch.tensor([ids], dtype=torch.long, device=self.input_device)
        encoded = text.encode("utf-8")[: max_length - 1] if max_length else text.encode("utf-8")
        ids = [0] + [1 + (b % 30) for b in encoded]
        return torch.tensor([ids], dtype=torch.long, device=self.input_device)

    def forward(self, input_ids: torch.Tensor) -> torch.Tensor:
        """Run the residual stack on ``input_ids``.

        Returns hidden states of shape ``[batch, seq_len, d_model]``
        (pre-final-norm, pre-LM-head). The autograd graph is retained through
        all layers when grad is enabled.
        """
        return self._residual_forward(input_ids)

    def unembed(self, residual: torch.Tensor) -> torch.Tensor:
        """Map residual ``[..., d_model]`` to logits ``[..., vocab_size]``.

        Applies the model's final norm and LM head projection.
        """
        x = self._model.final_norm(residual.to(dtype=self._model.lm_head.weight.dtype))
        return self._model.lm_head(x.to(device=self._model.lm_head.weight.device))

    @classmethod
    def from_checkpoint(
        cls,
        checkpoint_dir: str = "checkpoints_topogpt3",
        *,
        device: str | None = None,
        encoding: str = "gpt2",
        strict: bool = False,
    ) -> TopoGPT3LensModel:
        """Build a TopoGPT3LensModel from a checkpoint directory.

        Probes state.json for configuration, instantiates the model, loads
        safetensors weights, and wraps the result.

        Args:
            checkpoint_dir: Path to the checkpoint slot directory.
            device: Target device. Defaults to cuda if available else cpu.
            encoding: Tokenizer encoding name (passed to BPETokenizer).
            strict: Whether to enforce strict state dict loading.

        Returns:
            A TopoGPT3LensModel in eval mode with requires_grad_(False).

        Raises:
            FileNotFoundError: If model.safetensors or state.json is missing.
        """
        from .model import BPETokenizer, TopoGPT2, TopoGPT2Config

        device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        resolved = Path(checkpoint_dir)
        weights_path = resolved / "model.safetensors"

        if not weights_path.exists():
            raise FileNotFoundError(
                f"Weights not found at {weights_path}. "
                f"Download from https://huggingface.co/grisiscomeback/TopoGPT3"
            )

        lens_cfg = TopoGPT3LensConfig.probe_checkpoint(str(resolved))
        model_cfg = TopoGPT2Config(
            SCALE=lens_cfg.scale,
            DEVICE=device,
        )
        model_cfg.__post_init__()

        model = TopoGPT2(model_cfg)
        state_dict = load_file(str(weights_path), device=device)
        missing, unexpected = model.load_state_dict(state_dict, strict=strict)
        model.to(device)
        model.eval()

        tokenizer = BPETokenizer(encoding=encoding)
        instance = cls(model, tokenizer=tokenizer)
        instance.input_device = torch.device(device)

        for param in model.parameters():
            param.requires_grad_(False)

        return instance


class TinyDecoder(nn.Module):
    """A tiny CPU-only decoder for end-to-end tests.

    Implements the LensModel protocol indirectly (wrapped by
    TopoGPT3LensModel). Residual blocks are ``h + 0.1 * linear(h)``:
    the small gain keeps the Jacobian well-conditioned so the late-layer
    ``diag(J) ~= 1`` property holds.
    """

    def __init__(
        self, n_layers: int = 4, d_model: int = 8, vocab_size: int = 32, seed: int = 0
    ) -> None:
        super().__init__()
        torch.manual_seed(seed)
        config = SimpleNamespace(
            D_MODEL=d_model,
            N_LAYERS=n_layers,
            N_HEADS=1,
            N_KV_HEADS=1,
            VOCAB_SIZE=vocab_size,
            MAX_SEQ_LEN=128,
            DROPOUT=0.0,
            DEVICE="cpu",
            SCALE="custom",
            MOE_ENABLED=False,
            N_EXPERTS=1,
            MOE_TOP_K=1,
            GRADIENT_CHECKPOINTING=False,
        )
        self.config = config
        self.token_embed = nn.Embedding(vocab_size, d_model)
        self.layers = nn.ModuleList(
            [_ResidualBlock(d_model) for _ in range(n_layers)]
        )
        self.final_norm = nn.LayerNorm(d_model)
        self.lm_head = nn.Linear(d_model, vocab_size, bias=False)
        self.lm_head.weight = self.token_embed.weight

    def forward(
        self, token_ids: torch.Tensor, past_kvs: Any = None
    ) -> tuple[torch.Tensor, torch.Tensor, list]:
        x = self.token_embed(token_ids)
        new_kvs: list = []
        total_aux = torch.tensor(0.0, device=x.device)
        for layer in self.layers:
            x, aux, _ = layer(x, past_kv=None)
            total_aux = total_aux + aux
            new_kvs.append(None)
        x = self.final_norm(x)
        logits = self.lm_head(x)
        return logits, total_aux / len(self.layers), new_kvs


class _ResidualBlock(nn.Module):
    def __init__(self, d_model: int) -> None:
        super().__init__()
        self.linear = nn.Linear(d_model, d_model, bias=False)
        with torch.no_grad():
            self.linear.weight.mul_(0.1)

    def forward(
        self, x: torch.Tensor, past_kv: Any = None
    ) -> tuple[torch.Tensor, torch.Tensor, None]:
        return x + self.linear(x), torch.tensor(0.0), None


if __name__ == "__main__":
    import time
    cfg = TopoGPT3LensConfig.probe_checkpoint("checkpoints_topogpt3/last")
    device = "cpu"
    import torch
    t0 = time.perf_counter()
    model = TopoGPT3LensModel.from_checkpoint(
        "checkpoints_topogpt3/last", device=device
    )
    t1 = time.perf_counter()
    n_params = sum(p.numel() for p in model._model.parameters())
    print(f"TopoGPT3LensModel: n_layers={model.n_layers}, d_model={model.d_model}, params={n_params:,}, load={t1-t0:.1f}s")
    ids = model.encode("def fibonacci(n):", max_length=32)
    with torch.no_grad():
        hidden = model.forward(ids)
        logits = model.unembed(hidden)
    print(f"encode: {ids.shape}  forward: {hidden.shape}  unembed: {logits.shape}")
    print("Model is ready. Use: python3 -m topogpt3.jlens --prompt 'def hello('")
