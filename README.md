# TopoGPT3

A 24.5M parameter complex-valued autoregressive language model for code, instrumented with spectral and geometric diagnostics over training dynamics.

This repository contains the model definition, the curriculum trainer, and two inference engines: a standard sampler and a hierarchical recursive reasoning sampler (HRM) that requires no extra trained parameters.

The work is documented in detail in `topogpt3.md`.

## Documentation

- [Quick Start](quickstart.md) — Get running in under five minutes.
- [Tutorial](tutorial.md) — Step-by-step guide from installation to custom training.
- [Essential Concepts](essentials.md) — Core ideas behind complex-valued spectral operators, Grassmannian diagnostics, and HRM.
- [Command Cheatsheet](cheatsheet.md) — Quick reference for CLI commands and Python API.
- [Comparison](comparison.md) — How TopoGPT3 relates to similar small-scale and code-focused models.
- [Claude Integration Guide](claude.md) — Using TopoGPT3 with Anthropic models and hybrid pipelines.
- [Technical Paper](topogpt3.md) — Full experimental write-up and results.

## Motivation

Most code language models scale through size. TopoGPT3 explores the opposite direction: whether better representations can let a much smaller model learn programming structure efficiently. Source code carries strong internal structure (recursion, composition, scope, repeated motifs), and complex-valued parameters may encode phase relationships that capture this structure more compactly than real-valued weights of equal count.

## Checkpoints

[https://huggingface.co/grisiscomeback/TopoGPT3/tree/main/checkpoints_topogpt3/last](https://huggingface.co/grisiscomeback/TopoGPT3/tree/main/checkpoints_topogpt3/last)

## Architecture summary

- Autoregressive transformer with complex-valued spectral operators.
- Quaternion-inspired layers for parameter efficiency.
- A Gauss-style optimization for complex multiplication: three real multiplications per contraction instead of four.
- Approximately 24.5M parameters at the default `small` scale.

The base architecture lives in `topogpt3/model.py`. The curriculum trainer and the Grassmannian / Fisher / phase diagnostics live in `topogpt3/train.py`.

## Training pipeline

Training proceeds through a four-tier curriculum, from short instructions to real multilingual code:

1. CodeAlpaca
2. Code Feedback (filtered instruction)
3. Magicoder Evol Instruct
4. Tiny subset of The Stack

Each tier maintains disjoint train, validation and holdout splits. The holdout is never used during training; it is reserved to measure true generalization at the end of each tier and at the end of the full pipeline.

Mixed precision is used on a single GPU. Checkpoints are written atomically to `checkpoints_topogpt3/last/` as safetensors plus an optimizer file and a JSON state. Older `step_*` directories are still loadable for backwards compatibility.

## Optimization diagnostics

At regular intervals the trainer extracts the kernel tensor, performs a truncated SVD on the leading 16 modes, normalizes them, and records:

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

The dominant kernels do not grow only in magnitude; their evolution shows persistent directional structure in phase space. Angular drift statistics stay bounded and accumulate coherently rather than diffusing like an unconstrained random walk. This is treated as an empirical observation, not as evidence of a formal topological invariant.

## Topo J-Lens

```python
❯  python3 -m topogpt3.jlens
Loading model from checkpoints_topogpt3/last (d_model=256, n_layers=6, device=cpu)
  loaded 24,457,622 parameters in 0.6s

Fitting Jacobian lens on 2 prompts, 5 source layers...
  fitted in 27.3s: JacobianLens(d_model=256, n_prompts=2, source_layers=[0..4] (5 layers))

Jacobian norms (diagonal dominance indicates reliable transport):
  layer     ||J||     max_diag   min_diag   ||J - I||
  ------------------------------------------
       0      22.20     1.0924     0.3867      17.21
       1      20.38     1.1276     0.5782      13.53
       2      18.56     1.0943     0.6139      10.14
       3      17.99     1.1119     0.6583       7.61
       4      17.00     1.0679     0.9422       4.89

Computing slice for prompt: 'def fibonacci(n):\n    '
 pos input token           L0 top-1                   L2 top-1                   L4 top-1                   L5 top-1                 
-------------------------------------------------------------------------------------------------------------------------------------
   0 def                   def              3.39%      def              0.09%       find            2.78%       find            7.23%    
   1  fib                  on               12.40%      on               63.49%      on               92.08%      on               95.33%    
   2 on                    on               84.84%      acci             21.03%      acci             93.29%      acci             99.62%    
   3 acci                  acci             35.38%      (                39.68%      (                94.84%      (                88.46%    
   4 (                     ):               2.45%      n                65.24%      n                82.16%      n                91.28%    
   5 n                     n                30.93%      umbers           16.97%      ):               97.23%      ):               97.46%    
   6 ):                    ):               64.79%      ):               78.69%      
                92.09%      
                80.98%    
   7 
                      super           0.13%                       31.64%                       75.16%                       95.50%    
   8                                        38.25%                       84.25%                       56.59%                       81.16%    
   9                                        46.50%                       49.94%                       97.22%                       98.47%    
  10                                        58.45%       """             49.04%       if              41.36%       if              48.04%    
  11                                        57.73%                       31.70%                       74.12%                       64.06%    


Summary:
  Fitted on 2 prompts, 5 layers
  Layer transport: ['L0->L5', 'L1->L5', 'L2->L5', 'L3->L5', 'L4->L5']
  Prompt: 'def fibonacci(n):\n    ' (12 tokens)
  To explore interactively: from topogpt3.jlens import compute_slice, text_slice

```

## Inference

Two engines share the same checkpoint:

- `topogpt3.inference`: standard sampler. Loads weights from safetensors, aligns the architecture configuration against the stored tensors, and performs autoregressive generation with top-k filtering and a repetition penalty.
- `topogpt3.inference_hrm`: hierarchical recursive reasoning sampler. Adds no new trainable parameters. The pretrained transformer layers are reused as the step function of a low-level and high-level latent refinement loop, with a short persistence window across emitted tokens. Halting is governed by the empirical stabilization of the latent state.

HRM is intended to study iterative latent transport at inference time. At the current training stage it preserves syntactic coherence and formatting but does not yield large qualitative improvements in algorithmic correctness; the diagnostics remain stable while high-level convergence events are rare.

## Repository layout

```
.
├── topogpt3/                  pip-installable package
│   ├── __init__.py            public API re-exports
│   ├── model.py               base TopoGPT2 architecture, tokenizer, helpers
│   ├── train.py               curriculum trainer + Grassmannian diagnostics
│   ├── inference.py           standard autoregressive sampler
│   ├── inference_hrm.py       hierarchical recursive reasoning sampler
│   ├── lens_model.py          Jacobian-lens model adapter (LensModel protocol)
│   └── jlens.py               Jacobian lens fitting + application pipeline
├── tests/                     BDD test suite
│   ├── test_lens_model.py     adapter contract tests
│   └── test_jlens.py          fitting + application contract tests
├── app.py                     example entry point for downstream projects
├── pyproject.toml             package metadata, dependencies, console scripts
├── README.md                  this file
├── topogpt3.md                full paper write-up
├── quickstart.md              five-minute getting started guide
├── tutorial.md                step-by-step usage tutorial
├── essentials.md              core concepts explained
├── cheatsheet.md              command and API quick reference
├── comparison.md              comparison with similar models
├── claude.md                  integration guide for Claude and Anthropic
├── synthetic_dataset.py       optional synthetic dataset helper
├── docs/                      HTML documentation and assets
└── workflows/                 GitHub Actions workflows
```

## Requirements

- Python 3.10 or newer
- PyTorch with CUDA recommended (CPU works for small scales)
- `safetensors`
- `tiktoken` (BPE tokenizer)
- `numpy`
- `datasets` and `huggingface-hub` for data preparation (optional extra `[train]`)

## Installation

From a checkout of this repository:

```
pip install -e .
```

For dataset preparation, install the training extra:

```
pip install -e ".[train]"
```

Once published, the package will be installable directly from PyPI or GitHub:

```
pip install topogpt3
pip install git+https://github.com/grisuno/TopoGPT3
```

The install registers three console scripts:

- `topogpt3-train` — full curriculum trainer CLI
- `topogpt3-infer` — standard autoregressive sampler CLI
- `topogpt3-infer-hrm` — hierarchical recursive reasoning sampler CLI

## Using the package from your own code

The simplest pattern is to import the public API from `topogpt3` and build the settings object that matches the use case:

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

### Jacobian Lens

Read out intermediate residual activations in the final-layer basis using the average input-output Jacobian. Based on the [jacobian-lens](https://github.com/anthropics/jacobian-lens) library (Anthropic, Apache 2.0).

```python
from topogpt3.lens_model import TopoGPT3LensModel
from topogpt3.jlens import fit, JacobianLens

model = TopoGPT3LensModel.from_checkpoint("checkpoints_topogpt3/last")

prompts = [
    "def fibonacci(n):\n    if n <= 1:\n        return n\n",
    "def factorial(n):\n    if n <= 1:\n        return 1\n",
]

lens = fit(model, prompts, source_layers=[0, 1, 2, 3, 4], dim_batch=8, max_seq_len=128)

lens_logits, model_logits, input_ids = lens.apply(
    model, "def hello(", layers=[0, 2, 4], use_jacobian=True
)
```

Run the test suite (no GPU required):

```bash
pytest tests/test_lens_model.py tests/test_jlens.py -v --tb=short
```

`app.py` at the repository root is a complete, runnable example that wires both inference modes plus the trainer behind a tiny `--mode` CLI. It is intended to be copied into downstream projects and adapted.

## Command-line usage

After `pip install -e .`:

Prepare datasets (downloads and tokenizes the four tiers into local cache):

```
topogpt3-train --prepare-data
```

Run the full curriculum:

```
topogpt3-train --train
```

Start from a specific tier and re-train from there (the `--start-tier` flag is honored even if the tier is already marked completed in the checkpoint state):

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

The same entry points are reachable as modules (useful before installation):

```
python -m topogpt3.train --help
python -m topogpt3.inference --help
python -m topogpt3.inference_hrm --help
python app.py --mode infer --prompt "def main(" --max-new 64
```

## Checkpoint compatibility

The model is always built with the maximum sequence length across all curriculum tiers, so positional embeddings keep a fixed shape regardless of which tier is used as the entry point. Existing safetensors weights load without shape mismatch when restarting at a different tier.

## Limitations

This is an exploratory small-scale study. The model is only 24.5M parameters and is trained on a limited curriculum. The phase and angular drift measurements are diagnostics, not rigorous mathematical invariants. A real-valued control of the same parameter count, broader benchmarks, and longer training are needed before drawing stronger conclusions.

Early generations show syntactic continuity and local semantic consistency. Algorithmic correctness remains limited at this scale and training duration.

## Related work

A 25M-parameter Transformer implementation designed to study language acquisition as a condensed matter phenomenon. Unlike traditional LLMs, TopoGPT-2 is engineered to reach a Topological Insulator state a phase where grammatical and logical invariants are protected by a spectral gap. Using the Tiny Stories corpus

- [https://github.com/grisuno/TopoGPT2](https://github.com/grisuno/TopoGPT2)

## Citation

If you build on this work, please cite:

- [https://doi.org/10.5281/zenodo.20388757](https://doi.org/10.5281/zenodo.20388757)

```
grisuno, "TopoGPT3: Exploring Complex-Valued Representations in Small
Code Models", May 2026.
```

## License

AGPL v3.
