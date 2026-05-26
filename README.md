# TopoGPT3

A 24.5M parameter complex-valued autoregressive language model for code,
instrumented with spectral and geometric diagnostics over training dynamics.

This repository contains the model definition, the curriculum trainer, and
two inference engines: a standard sampler and a hierarchical recursive
reasoning sampler (HRM) that requires no extra trained parameters.

The work is documented in detail in `topogpt3.md`.

## Motivation

Most code language models scale through size. TopoGPT3 explores the
opposite direction: whether better representations can let a much smaller
model learn programming structure efficiently. Source code carries strong
internal structure (recursion, composition, scope, repeated motifs), and
complex-valued parameters may encode phase relationships that capture this
structure more compactly than real-valued weights of equal count.

## Architecture summary

- Autoregressive transformer with complex-valued spectral operators.
- Quaternion-inspired layers for parameter efficiency.
- A Gauss-style optimization for complex multiplication: three real
  multiplications per contraction instead of four.
- Approximately 24.5M parameters at the default `small` scale.

The base architecture lives in `topogpt3/model.py`. The curriculum trainer
and the Grassmannian / Fisher / phase diagnostics live in
`topogpt3/train.py`.

## Training pipeline

Training proceeds through a four-tier curriculum, from short instructions
to real multilingual code:

1. CodeAlpaca
2. Code Feedback (filtered instruction)
3. Magicoder Evol Instruct
4. Tiny subset of The Stack

Each tier maintains disjoint train, validation and holdout splits. The
holdout is never used during training; it is reserved to measure true
generalization at the end of each tier and at the end of the full pipeline.

Mixed precision is used on a single GPU. Checkpoints are written
atomically to `checkpoints_topogpt3/last/` as safetensors plus an
optimizer file and a JSON state. Older `step_*` directories are still
loadable for backwards compatibility.

## Optimization diagnostics

At regular intervals the trainer extracts the kernel tensor, performs a
truncated SVD on the leading 16 modes, normalizes them, and records:

- accumulated phase between consecutive normalized dominant kernels,
- net angular drift `W` (a winding-like proxy),
- empirical Fisher spectral gap `Delta_F = lambda_r - lambda_{r+1}`,
- dominant rank `r` from an elbow rule on the singular values.

Reported results from the first tier (CodeAlpaca, two epochs):

- training loss: 2.168
- training accuracy: 60.08 percent
- validation loss: 2.199
- validation accuracy: 60.12 percent
- validation perplexity: 9.02
- holdout perplexity: 9.07
- dominant rank: stable at `r = 16`
- leading singular values: about `[2.383, 2.246]`
- Fisher gap `Delta_F`: about `1.347e-3`
- maximum observed `|W|`: about `0.55`

The dominant kernels do not grow only in magnitude; their evolution shows
persistent directional structure in phase space. Angular drift statistics
stay bounded and accumulate coherently rather than diffusing like an
unconstrained random walk. This is treated as an empirical observation,
not as evidence of a formal topological invariant.

## Inference

Two engines share the same checkpoint:

- `topogpt3.inference`: standard sampler. Loads weights from safetensors,
  aligns the architecture configuration against the stored tensors, and
  performs autoregressive generation with top-k filtering and a
  repetition penalty.
- `topogpt3.inference_hrm`: hierarchical recursive reasoning sampler.
  Adds no new trainable parameters. The pretrained transformer layers
  are reused as the step function of a low-level and high-level latent
  refinement loop, with a short persistence window across emitted
  tokens. Halting is governed by the empirical stabilization of the
  latent state.

HRM is intended to study iterative latent transport at inference time.
At the current training stage it preserves syntactic coherence and
formatting but does not yield large qualitative improvements in
algorithmic correctness; the diagnostics remain stable while
high-level convergence events are rare.

## Repository layout

```
.
├── topogpt3/                  pip-installable package
│   ├── __init__.py            public API re-exports
│   ├── model.py               base TopoGPT2 architecture, tokenizer, helpers
│   ├── train.py               curriculum trainer + Grassmannian diagnostics
│   ├── inference.py           standard autoregressive sampler
│   └── inference_hrm.py       hierarchical recursive reasoning sampler
├── app.py                     example entry point for downstream projects
├── pyproject.toml             package metadata, dependencies, console scripts
├── README.md                  this file
├── topogpt3.md                full paper write-up
└── synthetic_dataset.py       optional synthetic dataset helper
```

## Requirements

- Python 3.10 or newer
- PyTorch with CUDA recommended (CPU works for small scales)
- `safetensors`
- `tiktoken` (BPE tokenizer)
- `numpy`
- `datasets` and `huggingface-hub` for data preparation (optional extra
  `[train]`)

## Installation

From a checkout of this repository:

```
pip install -e .
```

For dataset preparation, install the training extra:

```
pip install -e ".[train]"
```

Once published, the package will be installable directly from PyPI or
GitHub:

```
pip install topogpt3
pip install git+https://github.com/grisuno/TopoGPT3
```

The install registers three console scripts:

- `topogpt3-train` — full curriculum trainer CLI
- `topogpt3-infer` — standard autoregressive sampler CLI
- `topogpt3-infer-hrm` — hierarchical recursive reasoning sampler CLI

## Using the package from your own code

The simplest pattern is to import the public API from `topogpt3` and
build the settings object that matches the use case:

```python
from topogpt3 import InferenceSettings, InferencePipeline

settings = InferenceSettings(
    checkpoint_dir="checkpoints_topogpt3",
    checkpoint_name="last",
    prompt="def fibonacci(n):\n",
    max_new_tokens=200,
)
report = InferencePipeline(settings).execute()
print(report.output)
```

For hierarchical recursive inference:

```python
from topogpt3 import (
    HRMInferencePipeline,
    HRMInferenceSettings,
    RecursiveReasoningConfig,
)

settings = HRMInferenceSettings(
    prompt="def fibonacci(n):\n",
    reasoning=RecursiveReasoningConfig(
        max_high_level_iters=2,
        max_low_level_iters=3,
        low_level_window=2,
    ),
)
report = HRMInferencePipeline(settings).execute()
print(report.output)
```

`app.py` at the repository root is a complete, runnable example that
wires both inference modes plus the trainer behind a tiny `--mode` CLI.
It is intended to be copied into downstream projects and adapted.

## Command-line usage

After `pip install -e .`:

Prepare datasets (downloads and tokenizes the four tiers into local
cache):

```
topogpt3-train --prepare-data
```

Run the full curriculum:

```
topogpt3-train --train
```

Start from a specific tier and re-train from there (the `--start-tier`
flag is honored even if the tier is already marked completed in the
checkpoint state):

```
topogpt3-train --train --start-tier 2
```

Evaluate on the combined holdout:

```
topogpt3-train --eval-holdout
```

Standard inference from the latest checkpoint:

```
topogpt3-infer --prompt "def fibonacci(" --max-new 200
```

Hierarchical recursive inference:

```
topogpt3-infer-hrm --prompt "def fibonacci(" \
    --hrm-h-iters 2 --hrm-l-iters 3 --hrm-l-window 2 --max-new 200
```

The same entry points are reachable as modules (useful before
installation):

```
python -m topogpt3.train --help
python -m topogpt3.inference --help
python -m topogpt3.inference_hrm --help
python app.py --mode infer --prompt "def main(" --max-new 64
```

## Checkpoint compatibility

The model is always built with the maximum sequence length across all
curriculum tiers, so positional embeddings keep a fixed shape regardless
of which tier is used as the entry point. Existing safetensors weights
load without shape mismatch when restarting at a different tier.

## Limitations

This is an exploratory small-scale study. The model is only 24.5M
parameters and is trained on a limited curriculum. The phase and angular
drift measurements are diagnostics, not rigorous mathematical invariants.
A real-valued control of the same parameter count, broader benchmarks,
and longer training are needed before drawing stronger conclusions.

Early generations show syntactic continuity and local semantic
consistency. Algorithmic correctness remains limited at this scale and
training duration.

## Citation

If you build on this work, please cite:

```
grisuno, "TopoGPT3: Exploring Complex-Valued Representations in Small
Code Models", May 2026.
```

## License

GPL v3.
