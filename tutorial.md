# Tutorial

A step-by-step guide to using TopoGPT3 from installation to custom training.

Project URL: [https://github.com/grisuno/TopoGPT3](https://github.com/grisuno/TopoGPT3)

---

## Table of Contents

1. [Installation](#installation)
2. [Your First Inference](#your-first-inference)
3. [Understanding the Output](#understanding-the-output)
4. [Using HRM Inference](#using-hrm-inference)
5. [Preparing Training Data](#preparing-training-data)
6. [Training from Scratch](#training-from-scratch)
7. [Resuming Training](#resuming-training)
8. [Evaluating on Holdout](#evaluating-on-holdout)
9. [Customizing the Model Scale](#customizing-the-model-scale)
10. [Interpreting Training Diagnostics](#interpreting-training-diagnostics)
11. [Using the Python API](#using-the-python-api)
12. [Generating Synthetic Data](#generating-synthetic-data)
13. [Next Steps](#next-steps)

---

## Installation

### Clone and Install

```bash
git clone https://github.com/grisuno/TopoGPT3.git
cd TopoGPT3
python3 -m venv env
source env/bin/activate
pip install -e ".[train]"
```

### Verify Installation

```bash
python -c "from topogpt3 import __version__; print(__version__)"
```

Expected output: `0.1.0`

### Download a Checkpoint

Checkpoints are hosted on Hugging Face:

```bash
mkdir -p checkpoints_topogpt3/last
# Download model.safetensors and state.json from:
# https://huggingface.co/grisiscomeback/TopoGPT3/tree/main/checkpoints_topogpt3/last
```

---

## Your First Inference

### Command Line

```bash
topogpt3-infer --prompt "def fibonacci(n):\n    """Return the nth Fibonacci number."""\n" --max-new 100
```

### Python Script

Create `first_inference.py`:

```python
from topogpt3 import InferenceSettings, InferencePipeline

settings = InferenceSettings(
    checkpoint_dir="checkpoints_topogpt3",
    checkpoint_name="last",
    prompt="def fibonacci(n):\n",
    max_new_tokens=100,
    temperature=0.3,
)
report = InferencePipeline(settings).execute()
print(report.output)
```

Run it:

```bash
python first_inference.py
```

---

## Understanding the Output

The `GenerationReport` object contains:

- `output`: the generated text string
- `tokens_generated`: count of new tokens produced
- `time_seconds`: generation wall time

You can inspect these fields for benchmarking:

```python
print(f"Generated {report.tokens_generated} tokens in {report.time_seconds:.2f}s")
```

---

## Using HRM Inference

HRM adds iterative latent refinement to standard decoding.

### CLI

```bash
topogpt3-infer-hrm \
    --prompt "def factorial(n):\n" \
    --max-new 100 \
    --hrm-h-iters 2 \
    --hrm-l-iters 3 \
    --hrm-l-window 2
```

### Python

```python
from topogpt3 import (
    HRMInferencePipeline,
    HRMInferenceSettings,
    RecursiveReasoningConfig,
)

settings = HRMInferenceSettings(
    prompt="def factorial(n):\n",
    checkpoint_dir="checkpoints_topogpt3",
    max_new_tokens=100,
    reasoning=RecursiveReasoningConfig(
        max_high_level_iters=2,
        max_low_level_iters=3,
        low_level_window=2,
    ),
)
report = HRMInferencePipeline(settings).execute()
print(report.output)
```

HRM is slower than standard inference but provides diagnostics on latent refinement dynamics.

---

## Preparing Training Data

Before training, download and tokenize the four curriculum datasets:

```bash
topogpt3-train --prepare-data
```

This creates cached tokenized datasets in the `data/` directory. It only needs to be run once.

---

## Training from Scratch

### CLI

```bash
topogpt3-train --train --scale small
```

### Python

```python
from topogpt3 import TopoGPT3Config, TopoGPT3Trainer

config = TopoGPT3Config(SCALE="small")
trainer = TopoGPT3Trainer(config)
trainer.prepare_all()
trainer.run()
```

Training proceeds automatically through the four tiers. Checkpoints are saved to `checkpoints_topogpt3/last/`.

---

## Resuming Training

To resume from a specific tier (for example, tier 2):

```bash
topogpt3-train --train --start-tier 2
```

The trainer loads the latest checkpoint and continues from the requested tier, even if the state file marks it as completed.

---

## Evaluating on Holdout

After training, evaluate generalization on the combined holdout set:

```bash
topogpt3-train --eval-holdout
```

This reports holdout loss, accuracy, and perplexity without updating model weights.

---

## Customizing the Model Scale

The `SCALE` parameter controls model size. Options are `micro`, `small`, `medium`, and `gpt2`.

```python
from topogpt3 import TopoGPT3Config

config = TopoGPT3Config(SCALE="micro")   # smallest, for CPU
config = TopoGPT3Config(SCALE="small")   # default, ~24.5M parameters
config = TopoGPT3Config(SCALE="medium")  # larger, more VRAM
config = TopoGPT3Config(SCALE="gpt2")    # GPT-2 reference dimensions
```

If you run out of memory, switch to `micro`.

---

## Interpreting Training Diagnostics

During training, the console prints metrics like:

```
[step 1000] loss: 2.168 | acc: 60.08% | rank: 16 | W: 0.55 | Delta_F: 1.347e-3
```

What these mean:

- **loss / acc**: standard language modeling metrics.
- **rank**: dominant subspace dimension (stable at 16 is good).
- **W**: net angular drift. Bounded values suggest coherent phase evolution.
- **Delta_F**: Fisher spectral gap. Positive values indicate a stable functional subspace.

These diagnostics are observational, not rigorous invariants. Use them to understand optimization structure beyond scalar loss.

---

## Using the Python API in Your Own Project

After `pip install -e .`, import the public API:

```python
from topogpt3 import (
    InferenceSettings,
    InferencePipeline,
    HRMInferenceSettings,
    HRMInferencePipeline,
    RecursiveReasoningConfig,
    TopoGPT3Config,
    TopoGPT3Trainer,
)
```

`app.py` at the repository root is a complete, runnable example that wires all three modes (standard inference, HRM inference, training) behind a single CLI. Copy it into your own project and adapt.

---

## Generating Synthetic Data

TopoGPT3 includes `synthetic_dataset.py`, which turns source files into instruction-tuning data using an external LLM.

### Example with Groq

```bash
export GROQ_API_KEY="your-key"
python synthetic_dataset.py \
    --provider groq \
    --model llama-3.3-70b-versatile \
    --paths-file my_files.txt \
    --output data/synthetic.jsonl
```

### Example with OpenRouter (Claude)

```bash
export OPENROUTER_API_KEY="your-key"
python synthetic_dataset.py \
    --provider openrouter \
    --model anthropic/claude-3.5-sonnet \
    --paths-file my_files.txt \
    --output data/synthetic_claude.jsonl
```

The script supports SHA256 deduplication, resumable progress via a manifest, and threaded batch processing.

---

## Next Steps

- Explore the [Command Cheatsheet](cheatsheet.md) for quick reference.
- Read [Essential Concepts](essentials.md) to understand the theory.
- Review the [Technical Paper](topogpt3.md) for full experimental results.
- See [Comparison](comparison.md) to understand how TopoGPT3 fits in the landscape of small models.

---

**License**: GPL v3 | **Author**: grisun0
