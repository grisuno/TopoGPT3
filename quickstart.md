# Quick Start

Get started with TopoGPT3 in under five minutes.

Project URL: [https://github.com/grisuno/TopoGPT3](https://github.com/grisuno/TopoGPT3)

---

## Prerequisites

- Python 3.10 or newer
- Git
- (Recommended) NVIDIA GPU with CUDA for training

## Installation (30 seconds)

```bash
# 1. Clone the repository
git clone https://github.com/grisuno/TopoGPT3.git
cd TopoGPT3

# 2. Create a virtual environment
python3 -m venv env
source env/bin/activate

# 3. Install the package
pip install -e .
```

For training (additional data dependencies):

```bash
pip install -e ".[train]"
```

## Quick Inference (1 minute)

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

Or from the command line:

```bash
topogpt3-infer --prompt "def fibonacci(" --max-new 200
```

## Download Checkpoints

Checkpoints are available on Hugging Face:

[https://huggingface.co/grisiscomeback/TopoGPT3/tree/main/checkpoints_topogpt3/last](https://huggingface.co/grisiscomeback/TopoGPT3/tree/main/checkpoints_topogpt3/last)

## Available CLI Commands

| Command | Description |
|---------|-------------|
| `topogpt3-train --train` | Train the model with the full curriculum |
| `topogpt3-infer` | Standard autoregressive inference |
| `topogpt3-infer-hrm` | Hierarchical recursive reasoning inference (HRM) |

## Complete Example with app.py

```bash
# Standard inference
python app.py --mode infer --prompt "def main(" --max-new 64

# HRM inference
python app.py --mode infer-hrm --prompt "def main(" --max-new 64

# Training
python app.py --mode train --scale small
```

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `ModuleNotFoundError` | Make sure the virtual environment is active and the package is installed with `pip install -e .` |
| Out of memory | Reduce the model size with `--scale micro` |
| No CUDA | The model works on CPU, but it will be slower |

## Next Steps

- [Full Tutorial](tutorial.md)
- [Command Cheatsheet](cheatsheet.md)
- [Essential Concepts](essentials.md)
- [Technical Paper](topogpt3.md)

---

**License**: GPL v3 | **Author**: grisun0
