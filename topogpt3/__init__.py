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

Typical usage from a downstream project::

    from topogpt3 import InferenceSettings, InferencePipeline

    settings = InferenceSettings(
        checkpoint_dir="checkpoints_topogpt3",
        prompt="def fibonacci(",
        max_new_tokens=200,
    )
    InferencePipeline(settings).execute()
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

__all__ = [
    "__version__",
    "BPETokenizer",
    "QuaternionSpectralLayer",
    "SpectralAutoencoder",
    "TopoGPT2",
    "TopoGPT2Config",
    "set_seed",
    "setup_logger",
    "CheckpointStore",
    "CodeCurriculumLoader",
    "GrassmannianTracker",
    "TopoGPT3Config",
    "TopoGPT3Trainer",
    "apply_gauss_patch",
    "GenerationReport",
    "InferencePipeline",
    "InferenceSettings",
    "SamplingPolicy",
    "GenerationReasoningSummary",
    "HRMInferencePipeline",
    "HRMInferenceSettings",
    "HierarchicalRecursiveReasoner",
    "RecursiveReasoningConfig",
]
