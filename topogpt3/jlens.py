from __future__ import annotations

import logging
import math
import os
import time
from collections.abc import Callable, Iterable, Sequence
from dataclasses import dataclass, field
from typing import Any

import torch
from torch import nn

from .lens_model import LensModel


__all__ = [
    "ActivationRecorder",
    "JacobianLens",
    "SliceData",
    "TopoGPT3JLensFitConfig",
    "TopoGPT3JLensAppConfig",
    "compute_slice",
    "fit",
    "jacobian_for_prompt",
    "text_slice",
    "valid_position_mask",
]

logger = logging.getLogger(__name__)


SKIP_FIRST_N_POSITIONS = 16


@dataclass(frozen=True)
class TopoGPT3JLensFitConfig:
    """Centralized configuration for Jacobian lens fitting.

    Every value consumed downstream resides here. Adding a new tunable means
    extending this class; no other module should embed literals.
    """

    source_layers: tuple[int, ...] | None = None
    target_layer: int | None = None
    dim_batch: int = 8
    max_seq_len: int = 128
    skip_first: int = SKIP_FIRST_N_POSITIONS
    checkpoint_path: str | None = None
    checkpoint_every: int | None = 1
    resume: bool = True
    seed: int = 42


@dataclass(frozen=True)
class TopoGPT3JLensAppConfig:
    """Centralized configuration for Jacobian lens application.

    Every value consumed downstream resides here. Adding a new tunable means
    extending this class; no other module should embed literals.
    """

    layers: tuple[int, ...] | None = None
    positions: tuple[int, ...] | None = None
    max_seq_len: int = 512
    use_jacobian: bool = True


class ActivationRecorder:
    """Captures residual-stream tensors at the given block indices.

    Registers a forward hook on each requested block on ``__enter__`` and
    removes them on ``__exit__``. On the next forward pass each block's output
    is stored in ``activations``, keyed by block index. Stored tensors are
    not detached, so they can be passed straight to ``torch.autograd.grad``.

    Args:
        blocks: The sequence of residual blocks (e.g. ``model.layers``).
        at: Block indices to record at.
        start_graph_at: If given, the captured tensor at this index is marked
            ``requires_grad_(True)`` before downstream blocks see it. When the
            model's parameters all have ``requires_grad=False``, this makes the
            captured residual the leaf that roots the autograd graph, so the
            retained graph spans only this block onward.
    """

    def __init__(
        self,
        blocks: Sequence[nn.Module],
        at: Iterable[int],
        *,
        start_graph_at: int | None = None,
    ) -> None:
        self._blocks = blocks
        self._indices = sorted(set(at))
        self._start_graph_at = start_graph_at
        if start_graph_at is not None and start_graph_at not in self._indices:
            self._indices = sorted({*self._indices, start_graph_at})
        self.activations: dict[int, torch.Tensor] = {}
        self._handles: list[torch.utils.hooks.RemovableHandle] = []

    def _make_hook(self, index: int) -> Callable[..., None]:
        is_graph_root = index == self._start_graph_at

        def hook(module: nn.Module, inputs: Any, output: Any) -> None:
            tensor = output if torch.is_tensor(output) else output[0]
            if is_graph_root:
                tensor.requires_grad_(True)
            self.activations[index] = tensor

        return hook

    def __enter__(self) -> ActivationRecorder:
        try:
            for index in self._indices:
                self._handles.append(
                    self._blocks[index].register_forward_hook(self._make_hook(index))
                )
        except Exception:
            for handle in self._handles:
                handle.remove()
            self._handles = []
            raise
        return self

    def __exit__(self, *exc: Any) -> None:
        for handle in self._handles:
            handle.remove()
        self._handles = []


def valid_position_mask(
    seq_len: int, *, skip_first: int = SKIP_FIRST_N_POSITIONS
) -> torch.Tensor:
    """Boolean mask over sequence positions to include in the Jacobian average.

    Early positions are dominated by attention-sink behaviour and the final
    position has no next-token target, so both are excluded.

    Args:
        seq_len: Length of the tokenized prompt.
        skip_first: Number of leading positions to exclude.

    Returns:
        Boolean tensor of shape ``[seq_len]``.

    Raises:
        ValueError: If ``skip_first`` is negative or the prompt is too short to
            leave any valid positions.
    """
    if skip_first < 0:
        raise ValueError(f"skip_first must be >= 0, got {skip_first}")
    mask = torch.zeros(seq_len, dtype=torch.bool)
    mask[skip_first : seq_len - 1] = True
    if mask.sum() == 0:
        raise ValueError(
            f"prompt too short: seq_len={seq_len}, need > {skip_first + 1} tokens"
        )
    return mask


def _check_layer_indices(
    source_layers: Sequence[int] | None, target_layer: int | None, n_layers: int
) -> tuple[list[int], int]:
    """Resolve None/negative layer indices, bounds-check, enforce source < target."""
    target = n_layers - 1 if target_layer is None else target_layer
    if target < 0:
        target += n_layers
    if not 0 <= target < n_layers:
        raise ValueError(
            f"target_layer={target_layer} out of range for {n_layers} layers"
        )
    if source_layers is None:
        return list(range(target)), target
    sources = sorted({layer + n_layers if layer < 0 else layer for layer in source_layers})
    if not sources or sources[0] < 0 or sources[-1] >= n_layers:
        raise ValueError(
            f"source_layers {sorted(source_layers)} out of range for {n_layers} layers"
        )
    if sources[-1] >= target:
        raise ValueError(
            f"source_layers must all be < target_layer={target}; got max={sources[-1]}"
        )
    return sources, target


def jacobian_for_prompt(
    model: LensModel,
    prompt: str,
    source_layers: Sequence[int],
    *,
    target_layer: int | None = None,
    dim_batch: int = 8,
    max_seq_len: int = 128,
    skip_first: int = SKIP_FIRST_N_POSITIONS,
) -> tuple[dict[int, torch.Tensor], int, int]:
    """Compute the per-layer Jacobian estimator ``J_l`` for one prompt.

    Runs one forward pass on the prompt replicated ``dim_batch`` times along
    the batch axis, retains the graph, then runs ``ceil(d_model / dim_batch)``
    backward passes against it. Each backward computes ``dim_batch`` rows of
    ``J_l`` at once: batch element ``b`` carries a one-hot cotangent at output
    dimension ``dim_start + b``, set at every valid target position.

    Args:
        model: The model to compute Jacobians for.
        prompt: Input text.
        source_layers: Layer indices ``l`` to compute ``J_l`` at.
        target_layer: Layer to take gradients with respect to. Defaults to the
            final layer; negative indices count from the end.
        dim_batch: Output dimensions computed per backward pass.
        max_seq_len: Truncate the prompt to this many tokens.
        skip_first: Leading positions to exclude.

    Returns:
        ``(jacobians, seq_len, n_valid_positions)``. ``jacobians`` maps each
        source layer to a ``[d_model, d_model]`` fp32 CPU tensor.
    """
    n_layers, d_model = model.n_layers, model.d_model
    source_layers, target_layer = _check_layer_indices(
        source_layers, target_layer, n_layers
    )

    input_ids = model.encode(prompt, max_length=max_seq_len)
    seq_len = input_ids.shape[1]
    position_mask = valid_position_mask(seq_len, skip_first=skip_first)
    n_valid_positions = int(position_mask.sum())

    jacobians = {
        layer: torch.zeros(d_model, d_model, dtype=torch.float32)
        for layer in source_layers
    }
    n_passes = math.ceil(d_model / dim_batch)

    with (
        ActivationRecorder(
            model.layers,
            at=[*source_layers, target_layer],
            start_graph_at=min(source_layers),
        ) as recorder,
        torch.enable_grad(),
    ):
        replicated_ids = input_ids.expand(dim_batch, -1)
        model.forward(replicated_ids)
        target_activation = recorder.activations[target_layer]
        source_activations = [recorder.activations[layer] for layer in source_layers]

        valid_positions = position_mask.nonzero(as_tuple=True)[0].to(
            target_activation.device
        )
        batch_indices = torch.arange(dim_batch, device=target_activation.device)
        cotangent = torch.zeros_like(target_activation)

        for pass_idx, dim_start in enumerate(range(0, d_model, dim_batch)):
            n_dims_this_pass = min(dim_batch, d_model - dim_start)
            cotangent.zero_()
            cotangent[
                batch_indices[:n_dims_this_pass, None],
                valid_positions[None, :],
                dim_start + batch_indices[:n_dims_this_pass, None],
            ] = 1.0
            grads = torch.autograd.grad(
                outputs=target_activation,
                inputs=source_activations,
                grad_outputs=cotangent,
                retain_graph=(pass_idx < n_passes - 1),
            )
            for layer, grad in zip(source_layers, grads, strict=True):
                positions_on_device = valid_positions.to(grad.device, non_blocking=True)
                rows = (
                    grad[:n_dims_this_pass, positions_on_device, :]
                    .float()
                    .mean(dim=1)
                )
                jacobians[layer][dim_start : dim_start + n_dims_this_pass, :] = (
                    rows.cpu()
                )
            del grads

    return jacobians, seq_len, n_valid_positions


def _atomic_save(obj: object, path: str) -> None:
    """``torch.save`` to a temp file then ``os.replace`` so a crash never
    leaves a half-written checkpoint."""
    tmp_path = f"{path}.tmp.{os.getpid()}"
    torch.save(obj, tmp_path)
    os.replace(tmp_path, path)


def fit(
    model: LensModel,
    prompts: Sequence[str],
    *,
    source_layers: Sequence[int] | None = None,
    target_layer: int | None = None,
    dim_batch: int = 8,
    max_seq_len: int = 128,
    skip_first: int = SKIP_FIRST_N_POSITIONS,
    checkpoint_path: str | None = None,
    checkpoint_every: int | None = 1,
    resume: bool = True,
) -> JacobianLens:
    """Fit ``J_l`` over a list of prompts and return a JacobianLens.

    Per-prompt Jacobians from ``jacobian_for_prompt`` are accumulated as a
    running mean. If ``checkpoint_path`` is set, the running sum is written
    every ``checkpoint_every`` prompts (atomic) and resumed from on restart.

    Args:
        model: The model to fit on.
        prompts: Text prompts to average over.
        source_layers: Layers to fit at. Defaults to every layer below
            ``target_layer``; negative indices count from the end.
        target_layer: See ``jacobian_for_prompt``.
        dim_batch: See ``jacobian_for_prompt``.
        max_seq_len: Truncate each prompt to this many tokens.
        skip_first: See ``jacobian_for_prompt``.
        checkpoint_path: If set, write a resumable checkpoint here.
        checkpoint_every: Write checkpoint every N prompts (default 1).
        resume: If True and checkpoint_path exists, resume from it.

    Returns:
        The fitted JacobianLens.

    Raises:
        ValueError: If no prompts are long enough to fit on, or if checkpoint
            settings mismatch.
    """
    n_layers, d_model = model.n_layers, model.d_model
    source_layers, target_layer = _check_layer_indices(
        source_layers, target_layer, n_layers
    )

    logger.info(
        "fit: n_layers=%d d_model=%d, fitting %d source layers "
        "(target=L%d) on %d prompts",
        n_layers,
        d_model,
        len(source_layers),
        target_layer,
        len(prompts),
    )

    jacobian_sum: dict[int, torch.Tensor]
    n_done: int
    next_idx: int
    if resume and checkpoint_path is not None and os.path.exists(checkpoint_path):
        state = torch.load(checkpoint_path, map_location="cpu", weights_only=True)
        for key, expected in (
            ("source_layers", source_layers),
            ("target_layer", target_layer),
            ("skip_first", skip_first),
        ):
            if key in state and state[key] != expected:
                raise ValueError(
                    f"checkpoint at {checkpoint_path} was fitted with {key}="
                    f"{state[key]!r}, not {expected!r}; pass resume=False to discard it"
                )
        jacobian_sum, n_done, next_idx = (
            state["jacobian_sum"],
            state["n_done"],
            state["next_idx"],
        )
        logger.info(
            "  resuming from checkpoint: %d/%d prompts processed",
            next_idx,
            len(prompts),
        )
    else:
        jacobian_sum = {
            layer: torch.zeros(d_model, d_model, dtype=torch.float32)
            for layer in source_layers
        }
        n_done = 0
        next_idx = 0

    def write_checkpoint() -> None:
        if checkpoint_path is not None:
            _atomic_save(
                {
                    "jacobian_sum": jacobian_sum,
                    "n_done": n_done,
                    "next_idx": next_idx,
                    "source_layers": source_layers,
                    "target_layer": target_layer,
                    "skip_first": skip_first,
                },
                checkpoint_path,
            )

    sqrt_d = math.sqrt(d_model)
    for prompt_idx, prompt in enumerate(prompts):
        if prompt_idx < next_idx:
            continue
        start_time = time.perf_counter()
        try:
            per_prompt_J, _seq_len, _n_valid = jacobian_for_prompt(
                model,
                prompt,
                source_layers,
                target_layer=target_layer,
                dim_batch=dim_batch,
                max_seq_len=max_seq_len,
                skip_first=skip_first,
            )
        except ValueError as exc:
            logger.warning("  skipping prompt %d: %s", prompt_idx, exc)
            next_idx = prompt_idx + 1
            continue

        prompt_norm = (
            max(per_prompt_J[layer].norm().item() for layer in source_layers) / sqrt_d
        )
        if n_done > 0:
            mean_rel_change = max(
                (
                    (
                        per_prompt_J[layer]
                        - jacobian_sum[layer] / n_done
                    ).norm()
                    / ((n_done + 1) * (jacobian_sum[layer] / n_done).norm())
                ).item()
                for layer in source_layers
            )
        else:
            mean_rel_change = float("nan")

        for layer in source_layers:
            jacobian_sum[layer] += per_prompt_J[layer]
        n_done += 1
        next_idx = prompt_idx + 1

        logger.info(
            "  prompt %d/%d  n_valid=%d  %.0fs  "
            "max||J||/sqrt(d)=%.3f  max_d_mean=%.2e",
            prompt_idx + 1,
            len(prompts),
            _n_valid,
            time.perf_counter() - start_time,
            prompt_norm,
            mean_rel_change,
        )
        if checkpoint_every is not None and next_idx % checkpoint_every == 0:
            write_checkpoint()

    write_checkpoint()
    if n_done == 0:
        raise ValueError("no prompts were long enough to fit on")
    jacobian_mean = {
        layer: jacobian_sum[layer] / n_done for layer in source_layers
    }
    logger.info("fit: done, %d prompts", n_done)
    return JacobianLens(
        jacobians=jacobian_mean, n_prompts=n_done, d_model=d_model
    )


class JacobianLens:
    """A fitted Jacobian lens: per-layer ``J_l`` matrices and the readout method.

    Attributes:
        jacobians: ``{layer_index: Tensor[d_model, d_model]}``. Each ``J_l``
            maps the residual at layer ``l`` into the final-layer basis.
        source_layers: Sorted list of fitted layer indices.
        n_prompts: Number of prompts the lens was averaged over.
        d_model: Residual-stream width.
    """

    def __init__(
        self,
        jacobians: dict[int, torch.Tensor],
        *,
        n_prompts: int,
        d_model: int,
    ) -> None:
        self.jacobians = {layer: J.float() for layer, J in jacobians.items()}
        self.source_layers = sorted(self.jacobians)
        self.n_prompts = n_prompts
        self.d_model = d_model

    def __repr__(self) -> str:
        return (
            f"JacobianLens(d_model={self.d_model}, n_prompts={self.n_prompts}, "
            f"source_layers=[{self.source_layers[0]}..{self.source_layers[-1]}] "
            f"({len(self.source_layers)} layers))"
        )

    def save(self, path: str, *, dtype: torch.dtype = torch.float16) -> None:
        """Save to ``path``. Jacobians are stored as ``dtype`` (default fp16)."""
        torch.save(
            {
                "J": {
                    layer: J.to(dtype) for layer, J in self.jacobians.items()
                },
                "n_prompts": self.n_prompts,
                "source_layers": self.source_layers,
                "d_model": self.d_model,
            },
            path,
        )

    @classmethod
    def load(cls, path: str) -> JacobianLens:
        """Load a lens previously written by ``save``."""
        checkpoint = torch.load(path, map_location="cpu", weights_only=True)
        if "J" not in checkpoint:
            raise ValueError(
                f"{path} is not a JacobianLens file "
                f"(found keys {sorted(checkpoint)!r}; a fit() checkpoint?)"
            )
        return cls(
            jacobians=checkpoint["J"],
            n_prompts=checkpoint["n_prompts"],
            d_model=checkpoint["d_model"],
        )

    @classmethod
    def from_pretrained(
        cls,
        name_or_path: str,
        *,
        filename: str = "lens.pt",
        revision: str | None = None,
    ) -> JacobianLens:
        """Load a lens from a local file, a local directory, or a HuggingFace
        Hub ``repo_id``.

        ``filename`` is the path inside the directory or repo; ignored when
        ``name_or_path`` is itself a file. ``revision`` selects a Hub branch,
        tag, or commit.
        """
        if os.path.isfile(name_or_path):
            return cls.load(name_or_path)
        if not os.path.isdir(name_or_path):
            from huggingface_hub import snapshot_download
            name_or_path = snapshot_download(
                name_or_path, allow_patterns=[filename], revision=revision
            )
        return cls.load(os.path.join(name_or_path, filename))

    @classmethod
    def merge(cls, lenses: Sequence[JacobianLens]) -> JacobianLens:
        """Combine lenses fitted on disjoint prompt subsets into one
        (``n_prompts``-weighted mean of the inputs).

        Args:
            lenses: Lenses to merge. Must agree on ``source_layers`` and
                ``d_model``.

        Raises:
            ValueError: If ``lenses`` is empty or the inputs disagree on shape.
        """
        if not lenses:
            raise ValueError("merge() needs at least one lens")
        first = lenses[0]
        for other in lenses[1:]:
            if (
                other.source_layers != first.source_layers
                or other.d_model != first.d_model
            ):
                raise ValueError("lenses disagree on source_layers / d_model")
        n_total = sum(lens.n_prompts for lens in lenses)
        merged: dict[int, torch.Tensor] = {}
        for layer in first.source_layers:
            weighted_sum = sum(
                lens.jacobians[layer] * lens.n_prompts for lens in lenses
            )
            merged[layer] = weighted_sum / n_total
        return cls(
            jacobians=merged, n_prompts=n_total, d_model=first.d_model
        )

    def transport(self, residual: torch.Tensor, layer: int) -> torch.Tensor:
        """Map a residual at ``layer`` into the final-layer basis: ``J_l @ h``.

        Args:
            residual: Tensor of shape ``[..., d_model]``.
            layer: Source layer index (must be in ``source_layers``).
        """
        J_bar = self.jacobians[layer].to(residual.device)
        return residual @ J_bar.T

    @torch.no_grad()
    def apply(
        self,
        model: LensModel,
        prompt: str,
        *,
        layers: Sequence[int] | None = None,
        positions: Sequence[int] | None = None,
        max_seq_len: int = 512,
        use_jacobian: bool = True,
    ) -> tuple[dict[int, torch.Tensor], torch.Tensor, torch.Tensor]:
        """Run ``model`` on ``prompt`` and return lens logits at ``positions``.

        Args:
            model: The model to read out from.
            prompt: Input text.
            layers: Layers to read out at. Defaults to all of
                ``source_layers``. Must be a subset of ``source_layers`` when
                ``use_jacobian`` is True.
            positions: Token positions to read out (Python indexing into the
                sequence; negative indices count from the end). None returns
                every position.
            max_seq_len: Truncate the prompt to this many tokens.
            use_jacobian: If False, skip the ``J_l`` transport (vanilla
                logit-lens baseline).

        Returns:
            A triple ``(lens_logits, model_logits, input_ids)``. ``lens_logits``
            maps each requested layer to a ``[n_positions, vocab_size]`` tensor;
            ``model_logits`` is the model's actual final-layer logits at the
            same positions (same shape).

        Raises:
            ValueError: If any requested layer is out of range for the model,
                or (with use_jacobian) not in source_layers.
        """
        if layers is None:
            layers = self.source_layers
        out_of_range = sorted(
            layer for layer in set(layers) if not 0 <= layer < model.n_layers
        )
        if out_of_range:
            raise ValueError(
                f"layers {out_of_range} out of range for a "
                f"{model.n_layers}-layer model"
            )
        unknown = set(layers) - set(self.source_layers)
        if use_jacobian and unknown:
            raise ValueError(
                f"layers {sorted(unknown)} not in source_layers; "
                f"fitted layers are {self.source_layers}"
            )
        final_layer = model.n_layers - 1
        record_at = sorted(set(layers) | {final_layer})

        input_ids = model.encode(prompt, max_length=max_seq_len)
        with ActivationRecorder(model.layers, at=record_at) as recorder:
            model.forward(input_ids)
            activations = {
                i: recorder.activations[i].detach() for i in record_at
            }

        def select(layer: int) -> torch.Tensor:
            full = activations[layer][0]
            return (
                full if positions is None else full[list(positions)]
            ).float()

        lens_logits: dict[int, torch.Tensor] = {}
        for layer in layers:
            residual = select(layer)
            if use_jacobian:
                residual = self.transport(residual, layer)
            lens_logits[layer] = model.unembed(residual).float().cpu()

        model_logits = model.unembed(select(final_layer)).float().cpu()
        return lens_logits, model_logits, input_ids


@dataclass
class SliceData:
    """Text-format slice data: top-K token predictions per (position, layer).

    ``layers`` always includes the model's final layer (the actual model
    output) so divergences from lens-transported earlier layers are visible.

    Attributes:
        seq_len: Number of token positions in the slice.
        layers: Layer indices shown (includes final layer).
        prompt: The input prompt text.
        input_ids: Tensor ``[1, seq_len]`` of token IDs.
        token_strs: Decoded strings for each token position.
        top_ids: ``[seq_len, n_layers, top_n]`` top token IDs per cell.
        top_probs: ``[seq_len, n_layers, top_n]`` softmax probabilities.
    """

    seq_len: int
    layers: list[int]
    prompt: str
    input_ids: torch.Tensor
    token_strs: list[str]
    top_ids: torch.Tensor  # [seq_len, n_layers, top_n]
    top_probs: torch.Tensor  # [seq_len, n_layers, top_n]
    top_n: int = field(default=5, init=False)

    def __post_init__(self) -> None:
        self.top_n = self.top_ids.shape[-1]


@torch.no_grad()
def compute_slice(
    model: LensModel,
    lens: JacobianLens,
    prompt: str,
    *,
    top_n: int = 5,
    max_seq_len: int = 512,
) -> SliceData:
    """Compute a position x layer slice of top-K token predictions.

    For each layer in the fitted lens, projects the residual at each position
    through the Jacobian into the final-layer basis, then unembeds to get
    logits and softmax probabilities. Returns the top-N predicted token IDs
    and their probabilities per (position, layer) cell.

    Args:
        model: The model to read out from.
        lens: A fitted JacobianLens.
        prompt: Input text.
        top_n: Top tokens to keep per (position, layer) cell.
        max_seq_len: Truncate the prompt to this many tokens.

    Returns:
        A SliceData instance with arrays indexed ``[seq_len, n_layers, top_n]``.
    """
    final_layer = model.n_layers - 1
    fitted_layers = lens.source_layers
    if final_layer not in fitted_layers:
        layers = sorted([*fitted_layers, final_layer])
    else:
        layers = fitted_layers

    input_ids = model.encode(prompt, max_length=max_seq_len)
    seq_len = input_ids.shape[1]

    tokenizer = getattr(model, "tokenizer", None)
    if tokenizer is not None:
        token_strs = [tokenizer.decode([t]) for t in input_ids[0].tolist()]
    else:
        token_strs = [f"<tok {t}>" for t in input_ids[0].tolist()]

    with ActivationRecorder(model.layers, at=layers) as recorder:
        model.forward(input_ids)
        activations = {layer: recorder.activations[layer].detach() for layer in layers}

    top_ids = torch.zeros(seq_len, len(layers), top_n, dtype=torch.long, device="cpu")
    top_probs = torch.zeros(seq_len, len(layers), top_n, dtype=torch.float32, device="cpu")

    for col, layer in enumerate(layers):
        residual = activations[layer][0].float()
        if layer in lens.jacobians:
            residual = lens.transport(residual, layer)
        logits = model.unembed(residual).float().cpu()
        probs = torch.softmax(logits, dim=-1)
        top = probs.topk(top_n, dim=-1)
        top_ids[:, col] = top.indices.cpu()
        top_probs[:, col] = top.values.cpu()

    return SliceData(
        seq_len=seq_len,
        layers=layers,
        prompt=prompt,
        input_ids=input_ids.cpu(),
        token_strs=token_strs,
        top_ids=top_ids,
        top_probs=top_probs,
    )


def text_slice(slice_data: SliceData, tokenizer: Any = None, n_cols: int = 3) -> str:
    """Render a SliceData as a readable text table.

    For each token position, shows what each layer predicts as the next token.
    The first column shows the actual input token; subsequent columns show the
    top-1 prediction at each layer with its softmax probability.

    Args:
        slice_data: The slice to render.
        tokenizer: Optional tokenizer for decoding predicted token IDs.
        n_cols: Number of layer columns to show (default 3).

    Returns:
        A multi-line string table.
    """
    lines: list[str] = []
    n_layers = len(slice_data.layers)
    step = max(1, n_layers // n_cols)
    display_layers = slice_data.layers[::step]
    if display_layers[-1] != slice_data.layers[-1]:
        display_layers.append(slice_data.layers[-1])

    header = f"{'pos':>4} {'input token':<20}"
    for layer in display_layers:
        header += f"  {'L' + str(layer) + ' top-1':<25}"
    lines.append(header)
    lines.append("-" * len(header))

    for pos in range(slice_data.seq_len):
        tok_str = slice_data.token_strs[pos]
        if len(tok_str) > 18:
            tok_str = tok_str[:15] + "..."
        row = f"{pos:>4} {tok_str:<20}"
        for col_idx, layer in enumerate(display_layers):
            try:
                col = slice_data.layers.index(layer)
                tid = int(slice_data.top_ids[pos, col, 0])
                prob = float(slice_data.top_probs[pos, col, 0])
                if tokenizer is not None:
                    pred_str = tokenizer.decode([tid])
                else:
                    pred_str = f"<{tid}>"
                if len(pred_str) > 14:
                    pred_str = pred_str[:11] + "..."
                row += f"  {pred_str:<16} {prob:.2%}    "
            except (ValueError, IndexError):
                row += f"  {'N/A':<25}"
        lines.append(row)

    lines.append("")
    return "\n".join(lines)


def _demo_jlens() -> None:
    """Run a full jacobian lens demo loading real weights from checkpoint."""
    import argparse

    parser = argparse.ArgumentParser(
        description="TopoGPT3 Jacobian Lens: inspect layer-wise predictions"
    )
    parser.add_argument(
        "--checkpoint", "-c",
        default="checkpoints_topogpt3/last",
        help="checkpoint directory (default: checkpoints_topogpt3/last)",
    )
    parser.add_argument(
        "--prompt", "-p",
        default="def fibonacci(n):\n    ",
        help="prompt to analyze",
    )
    parser.add_argument(
        "--prompts", "-P",
        type=int,
        default=2,
        help="number of auto-generated prompts to fit on (default: 2, use more for better J)",
    )
    parser.add_argument(
        "--dim-batch", "-b",
        type=int,
        default=8,
        help="output dimensions per backward pass (default: 8)",
    )
    parser.add_argument(
        "--max-seq-len",
        type=int,
        default=128,
        help="max prompt length (default: 128)",
    )
    parser.add_argument(
        "--top-n",
        type=int,
        default=5,
        help="top-K predictions per cell (default: 5)",
    )
    parser.add_argument(
        "--layers", "-l",
        type=int,
        nargs="*",
        help="source layers to fit (default: all except final)",
    )
    parser.add_argument(
        "--device", "-d",
        default=None,
        help="device (default: auto)",
    )
    args = parser.parse_args()

    from .lens_model import TopoGPT3LensModel, TopoGPT3LensConfig

    cfg = TopoGPT3LensConfig.probe_checkpoint(args.checkpoint)
    device = args.device or cfg.device
    if device == "cuda" and not torch.cuda.is_available():
        device = "cpu"

    print(f"Loading model from {args.checkpoint} (d_model={cfg.d_model}, n_layers={cfg.n_layers}, device={device})")
    t0 = time.perf_counter()
    model = TopoGPT3LensModel.from_checkpoint(args.checkpoint, device=device)
    print(f"  loaded {sum(p.numel() for p in model._model.parameters()):,} parameters in {time.perf_counter()-t0:.1f}s")

    n_layers = model.n_layers
    source_layers = args.layers or list(range(n_layers - 1))
    target_layer = n_layers - 1

    fit_prompts = [
        "def fibonacci(n):\n    if n <= 1:\n        return n\n    return fibonacci(n-1) + fibonacci(n-2)",
        "def factorial(n):\n    if n <= 1:\n        return 1\n    return n * factorial(n-1)",
        "def is_prime(n):\n    if n < 2:\n        return False\n    for i in range(2, int(n**0.5) + 1):\n        if n % i == 0:\n            return False\n    return True",
        "def quicksort(arr):\n    if len(arr) <= 1:\n        return arr\n    pivot = arr[0]\n    left = [x for x in arr[1:] if x <= pivot]\n    right = [x for x in arr[1:] if x > pivot]\n    return quicksort(left) + [pivot] + quicksort(right)",
    ][:args.prompts]

    print(f"\nFitting Jacobian lens on {len(fit_prompts)} prompts, {len(source_layers)} source layers...")
    t0 = time.perf_counter()
    lens = fit(
        model, fit_prompts,
        source_layers=source_layers,
        target_layer=target_layer,
        dim_batch=args.dim_batch,
        max_seq_len=args.max_seq_len,
    )
    print(f"  fitted in {time.perf_counter()-t0:.1f}s: {lens}")

    print("\nJacobian norms (diagonal dominance indicates reliable transport):")
    print("  layer     ||J||     max_diag   min_diag   ||J - I||")
    print("  " + "-" * 42)
    for layer in source_layers:
        J = lens.jacobians[layer]
        diag = J.diag()
        diff = (J - torch.eye(cfg.d_model, device=J.device)).norm().item()
        print(f"  {layer:>6} {J.norm().item():>10.2f} {diag.max().item():>10.4f} {diag.min().item():>10.4f} {diff:>10.2f}")

    print(f"\nComputing slice for prompt: {args.prompt!r}")
    slice_data = compute_slice(
        model, lens, args.prompt,
        top_n=args.top_n,
        max_seq_len=args.max_seq_len,
    )

    decoder = getattr(model, "tokenizer", None)
    print(text_slice(slice_data, tokenizer=decoder))

    print("\nSummary:")
    print(f"  Fitted on {lens.n_prompts} prompts, {len(source_layers)} layers")
    transport_strs = [f"L{layer}->L{target_layer}" for layer in source_layers]
    print(f"  Layer transport: {transport_strs}")
    print(f"  Prompt: {args.prompt!r} ({slice_data.seq_len} tokens)")
    print("  To explore interactively: from topogpt3.jlens import compute_slice, text_slice")


if __name__ == "__main__":
    _demo_jlens()
