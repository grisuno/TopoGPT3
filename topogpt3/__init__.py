"""TopoGPT3: complex-valued spectral language model for code.

This package bundles:

- ``topogpt3.model``: the base TopoGPT2 architecture (quaternion spectral
  layers, BPE tokenizer, helpers).
- ``topogpt3.train``: the curriculum trainer with Grassmannian / Fisher /
  phase diagnostics.
- ``topogpt3.inference``: a standard autoregressive sampler that loads a
  trained safetensors checkpoint.
- ``topogpt3.inference_hrm``: a hierarchical recursive reasoning sampler
  that reuses the same checkpoint with no extra trained parameters.
- ``topogpt3.lens_model``: the Jacobian-lens model adapter (LensModel
  protocol + TopoGPT3LensModel wrapper).
- ``topogpt3.jlens``: Jacobian lens fitting, application, and the
  ActivationRecorder / JacobianLens infrastructure.

Typical usage from a downstream project::

    from topogpt3 import InferenceSettings, InferencePipeline

    settings = InferenceSettings(
        checkpoint_dir="checkpoints_topogpt3",
        prompt="def fibonacci(",
        max_new_tokens=200,
    )
    InferencePipeline(settings).execute()

Jacobian lens usage::

    from topogpt3.lens_model import TopoGPT3LensModel
    from topogpt3.jlens import fit, JacobianLens

    model = TopoGPT3LensModel.from_checkpoint("checkpoints_topogpt3/last")
    lens = fit(model, prompts, source_layers=[0, 1, 2, 3, 4])
    lens_logits, model_logits, input_ids = lens.apply(model, "def hello(")
"""
from __future__ import annotations

__version__ = "0.1.0"

from .model import (
    BPETokenizer,
    QuaternionSpectralLayer,
    SpectralAutoencoder,
    TopoGPT2,
    TopoGPT2Config,
    set_seed,
    setup_logger,
)
from .train import (
    CheckpointStore,
    CodeCurriculumLoader,
    GrassmannianTracker,
    TopoGPT3Config,
    TopoGPT3Trainer,
    apply_gauss_patch,
)
from .inference import (
    GenerationReport,
    InferencePipeline,
    InferenceSettings,
    SamplingPolicy,
)
from .inference_hrm import (
    GenerationReasoningSummary,
    HRMInferencePipeline,
    HRMInferenceSettings,
    HierarchicalRecursiveReasoner,
    RecursiveReasoningConfig,
)
from .lens_model import (
    LensModel,
    TinyDecoder,
    TopoGPT3LensConfig,
    TopoGPT3LensModel,
)
from .jlens import (
    ActivationRecorder,
    JacobianLens,
    TopoGPT3JLensAppConfig,
    TopoGPT3JLensFitConfig,
    fit,
    jacobian_for_prompt,
    valid_position_mask,
)

__all__ = [
    "__version__",
    "ActivationRecorder",
    "BPETokenizer",
    "CheckpointStore",
    "CodeCurriculumLoader",
    "fit",
    "GenerationReasoningSummary",
    "GenerationReport",
    "GrassmannianTracker",
    "HierarchicalRecursiveReasoner",
    "HRMInferencePipeline",
    "HRMInferenceSettings",
    "InferencePipeline",
    "InferenceSettings",
    "jacobian_for_prompt",
    "JacobianLens",
    "LensModel",
    "QuaternionSpectralLayer",
    "RecursiveReasoningConfig",
    "SamplingPolicy",
    "set_seed",
    "setup_logger",
    "SpectralAutoencoder",
    "TinyDecoder",
    "TopoGPT2",
    "TopoGPT2Config",
    "TopoGPT3Config",
    "TopoGPT3JLensAppConfig",
    "TopoGPT3JLensFitConfig",
    "TopoGPT3LensConfig",
    "TopoGPT3LensModel",
    "TopoGPT3Trainer",
    "apply_gauss_patch",
    "valid_position_mask",
]
