# Cheatsheet

Quick reference for TopoGPT3 commands, APIs, and configuration options.

Project URL: [https://github.com/grisuno/TopoGPT3](https://github.com/grisuno/TopoGPT3)

---

## CLI Commands

### Training

| Command | Description |
|---------|-------------|
| `topogpt3-train --train` | Run the full four-tier curriculum |
| `topogpt3-train --prepare-data` | Download and tokenize all datasets |
| `topogpt3-train --train --start-tier 2` | Start training from tier 2 |
| `topogpt3-train --eval-holdout` | Evaluate on the combined holdout set |

### Standard Inference

| Command | Description |
|---------|-------------|
| `topogpt3-infer --prompt "def fib(" --max-new 200` | Generate 200 tokens |
| `topogpt3-infer --prompt "..." --temp 0.5 --top-k 40` | Custom temperature and top-k |
| `topogpt3-infer --prompt "..." --rep-penalty 1.2` | Increase repetition penalty |

### Hierarchical Recursive Reasoning (HRM)

| Command | Description |
|---------|-------------|
| `topogpt3-infer-hrm --prompt "def fib(" --max-new 200` | HRM with defaults |
| `topogpt3-infer-hrm --prompt "..." --hrm-h-iters 3 --hrm-l-iters 5` | More refinement iterations |
| `topogpt3-infer-hrm --prompt "..." --hrm-l-window 4` | Larger low-level window |

### Module Entry Points (before installation)

```bash
python -m topogpt3.train --help
python -m topogpt3.inference --help
python -m topogpt3.inference_hrm --help
```

### app.py Entry Point

```bash
python app.py --mode infer --prompt "def main(" --max-new 64
python app.py --mode infer-hrm --prompt "def main(" --max-new 64
python app.py --mode train --scale small
```

## Python API

### Standard Inference

```python
from topogpt3 import InferenceSettings, InferencePipeline

settings = InferenceSettings(
    checkpoint_dir="checkpoints_topogpt3",
    checkpoint_name="last",
    prompt="def fibonacci(n):\n",
    max_new_tokens=200,
    temperature=0.3,
    top_k=50,
    repetition_penalty=1.1,
)
report = InferencePipeline(settings).execute()
print(report.output)
```

### HRM Inference

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

### Training (programmatic)

```python
from topogpt3 import TopoGPT3Config, TopoGPT3Trainer

config = TopoGPT3Config(SCALE="small")
trainer = TopoGPT3Trainer(config)
trainer.prepare_all()   # download and tokenize datasets
trainer.run()           # start training
```

## Model Scales

| Scale | Parameters | Use case |
|-------|-----------|----------|
| `micro` | Smallest | CPU testing, memory-constrained environments |
| `small` | ~24.5M | Default, balanced for single-GPU training |
| `medium` | Larger | More capacity, requires more VRAM |
| `gpt2` | Matches GPT-2 | Reference baseline scale |

## Curriculum Tiers

| Tier | Dataset | Purpose |
|------|---------|---------|
| 1 | CodeAlpaca | Short instructions, basic patterns |
| 2 | Code Feedback (filtered) | Instruction refinement |
| 3 | Magicoder Evol Instruct | Complex instructions |
| 4 | Tiny subset of The Stack | Real multilingual code |

## File Locations

| Asset | Default Path |
|-------|--------------|
| Checkpoints | `checkpoints_topogpt3/last/` |
| Tokenized data cache | `data/` |
| Logs | Written to stdout/stderr by default |

## Common Flags

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--prompt` | string | `def fibonacci(n):\n` | Input prompt for inference |
| `--max-new` | int | 200 | Maximum tokens to generate |
| `--temp` | float | 0.3 | Sampling temperature |
| `--top-k` | int | 50 | Top-k filtering |
| `--rep-penalty` | float | 1.1 | Repetition penalty |
| `--device` | string | auto | `cuda` or `cpu` |
| `--scale` | string | `small` | Model scale |
| `--start-tier` | int | None | Resume from a specific curriculum tier |
| `--ckpt-dir` | string | `checkpoints_topogpt3` | Checkpoint directory |
| `--ckpt-name` | string | `last` | Checkpoint slot name |

## Environment Variables

| Variable | Used by | Purpose |
|----------|---------|---------|
| `GROQ_API_KEY` | `synthetic_dataset.py` | Groq API backend |
| `OPENROUTER_API_KEY` | `synthetic_dataset.py` | OpenRouter API backend |
| `OLLAMA_HOST` | `synthetic_dataset.py` | Ollama server host |

---

**License**: GPL v3 | **Author**: grisun0
