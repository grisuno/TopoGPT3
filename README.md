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
- Sliding window attention (`ATTN_WINDOW`) with configurable window size to control KV-cache memory footprint in long sequences. Set to 0 for full attention or a positive integer for local attention with O(W * S) complexity.
- Latent memory tokens (`N_MEMORY_TOKENS`) for fixed-size context compression across long sequence segments.
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

### Context-length diagnostic

A static analysis mode evaluates Fisher gap and phase discretization as a function of input sequence length. This helps detect phase collapse -- the degrading of long-range coherence when distant tokens suffer destructive interference in the complex-valued attention space:

```
python eval/diag_static.py --context-diagnostic
```

Output is a JSON record at `eval/runs/diag_static_<timestamp>.jsonl` containing Fisher gap, kappa, delta (phase discretization), and leading singular values for each tested context length. A `phase_collapse_at_ctx` field signals whether delta drops below 0.01 at any context length, indicating that phase wrapping or destructive interference may be impeding long-range dependencies.

## Topo J-Lens

The Jacobian lens transports intermediate residual-stream activations into
the final-layer logit space using the per-layer average input-output
Jacobian ``J_l``, letting you inspect what the model "thinks" at each
layer before it reaches the output. Based on the
[jacobian-lens](https://github.com/anthropics/jacobian-lens) library
(Anthropic, Apache 2.0).

### Quick demo (CLI)

```
python -m topogpt3 jlens \
    --checkpoint checkpoints_topogpt3/last \
    --prompts 4 \
    --prompt "def fibonacci(n):\n    "
```

This loads the checkpoint, fits ``J_l`` on 4 auto-generated code prompts,
prints Jacobian norm diagnostics, and renders a `text_slice` table
showing the top-1 prediction at select layers for every token position.
The table now includes **decoded token strings** (actual words, not raw
token IDs) for every prediction cell.

### Python API

```python
from topogpt3.lens_model import TopoGPT3LensModel
from topogpt3.jlens import fit, compute_slice, text_slice

model = TopoGPT3LensModel.from_checkpoint("checkpoints_topogpt3/last")

prompts = [
    "def fibonacci(n):\n    if n <= 1:\n        return n\n",
    "def factorial(n):\n    if n <= 1:\n        return 1\n",
]
lens = fit(model, prompts, source_layers=[0, 1, 2, 3, 4], dim_batch=8)

slice_data = compute_slice(model, lens, "def hello(", top_n=5)
print(text_slice(slice_data))

# slice_data.top_token_strs[pos][layer][k] contains the decoded word
# at layer column `layer`, position `pos`, rank `k` (0-indexed).
print(slice_data.top_token_strs[0][2][0])  # L2 top-1 at position 0
```

The ``SliceData`` object also exposes ``top_ids``, ``top_probs``,
``token_strs``, and ``layers`` for custom visualisation.

Run the lens test suite:

```bash
pytest tests/test_lens_model.py tests/test_jlens.py -v --tb=short
```

## Pi Agent Harness

The TopoGPT3 API server exposes an **OpenAI-compatible HTTP interface**
so any coding agent that speaks the OpenAI API can drive your local model.
This includes [Pi](https://github.com/earendil-works/pi),
[Aider](https://aider.chat), [Continue](https://continue.dev), and the
Codex CLI.

### Architecture

```
+-------------+     Bearer token      +------------------+
| Pi / Aider  | --- HTTP/JSON ------->| TopoGPT3 API     |
| (any agent) | <-- SSE streaming --- | Server :8800     |
+-------------+                       | FastAPI+uvicorn  |
                                      | TopoGPT2 backend |
                                      +------------------+
```

### Security model

The server is **hardened against red-team attacks** and ships with:

- **Authentication**: ``Authorization: Bearer <key>`` header.
  Keys are loaded from the ``TOPOGPT3_API_KEYS`` env var or ``--keys``.
  Admin keys (``admin:`` prefix) get higher rate limits. Constant-time
  comparison prevents timing attacks on the key.

- **Rate limiting**: token-bucket per IP (10 req/s) and per API key
  (10 req/s user, 50 req/s admin). Brute-force triggers an IP ban after
  10 failed auth attempts within an hour.

- **Input hardening**: Pydantic strict schemas enforce max prompt length
  (4096 tokens), max messages (200), max output (4096 tokens), and
  parameter bounds. Body size is capped at 256 KB.

- **Security headers**: ``X-Content-Type-Options``, ``X-Frame-Options``,
  ``X-XSS-Protection``, ``Content-Security-Policy``, and ``Cache-Control``
  on every response. ``Server`` header is suppressed. CORS is deny-all
  by default with an environment-variable allowlist.

- **Audit logging**: structured JSON log lines for every request (no
  secrets ever logged).

### Installing the API server

```bash
pip install -e ".[api]"
```

### Starting the server

```bash
export TOPOGPT3_API_KEYS="sk-my-secret-key-12345,admin:sk-admin-key-67890"

python -m topogpt3 api_server \
    --checkpoint checkpoints_topogpt3/last \
    --port 8800 \
    --host 127.0.0.1
```

Endpoints:

| Method | Path                    | Auth  | Description           |
|--------|-------------------------|-------|-----------------------|
| POST   | `/v1/completions`       | Bearer| Text completions      |
| POST   | `/v1/chat/completions`  | Bearer| Chat completions      |
| GET    | `/v1/models`            | Bearer| List available models |
| GET    | `/health`               | open  | Liveness check        |

### Configuring Pi

Pi discovers models through `~/.pi/agent/models.json`. Create it with the TopoGPT3 provider pointing at your local API server:

```bash
make pi-setup
```

This writes a `models.json` that declares the `topogpt3` provider with the OpenAI-compatible completions API. Alternatively, create the file manually:

```json
{
  "providers": {
    "topogpt3": {
      "baseUrl": "http://127.0.0.1:8800/v1",
      "api": "openai-completions",
      "apiKey": "$TOPOGPT3_API_KEY",
      "compat": {
        "supportsDeveloperRole": false,
        "supportsReasoningEffort": false
      },
      "models": [
        {
          "id": "topogpt3",
          "name": "TopoGPT3 (Local)",
          "reasoning": false,
          "input": ["text"],
          "contextWindow": 512,
          "maxTokens": 512,
          "cost": { "input": 0, "output": 0, "cacheRead": 0, "cacheWrite": 0 }
        }
      ]
    }
  }
}
```

Then run Pi with:

```bash
TOPOGPT3_API_KEY="sk-local" make pi-run
```

The Makefile passes a minimal system prompt to conserve the limited context window.

### Configuring other agents

```bash
# Aider
export OPENAI_API_BASE="http://localhost:8800/v1"
export OPENAI_API_KEY="sk-my-secret-key-12345"
aider --model openai/topogpt3

# Continue (VS Code extension)
# Set "apiBase" to "http://localhost:8800/v1" in config.json

# Codex CLI
export CODEX_API_BASE="http://localhost:8800/v1"
export CODEX_API_KEY="sk-my-secret-key-12345"
```

### API usage (curl)

```bash
# Completions
curl -s http://localhost:8800/v1/completions \
  -H "Authorization: Bearer sk-my-secret-key-12345" \
  -H "Content-Type: application/json" \
  -d '{"prompt":"def fibonacci(n):\n    ","max_tokens":64,"temperature":0.7}'

# Chat completions
curl -s http://localhost:8800/v1/chat/completions \
  -H "Authorization: Bearer sk-my-secret-key-12345" \
  -H "Content-Type: application/json" \
  -d '{
    "messages":[
      {"role":"system","content":"You write Python."},
      {"role":"user","content":"Write a fibonacci function."}
    ],
    "max_tokens":128
  }'

# Streaming chat
curl -s http://localhost:8800/v1/chat/completions \
  -H "Authorization: Bearer sk-my-secret-key-12345" \
  -H "Content-Type: application/json" \
  -d '{"messages":[{"role":"user","content":"fibonacci"}],"stream":true}'
```

## Inference

Two engines share the same checkpoint:

- `topogpt3.inference`: standard sampler. Loads weights from safetensors, aligns the architecture configuration against the stored tensors, and performs autoregressive generation with top-k filtering and a repetition penalty.
- `topogpt3.inference_hrm`: hierarchical recursive reasoning sampler. Adds no new trainable parameters. The pretrained transformer layers are reused as the step function of a low-level and high-level latent refinement loop, with a short persistence window across emitted tokens. Halting is governed by the empirical stabilization of the latent state.

HRM is intended to study iterative latent transport at inference time. At the current training stage it preserves syntactic coherence and formatting but does not yield large qualitative improvements in algorithmic correctness; the diagnostics remain stable while high-level convergence events are rare.

### Auto-continuation

When the model hits the end-of-text token (EOS) before producing a structurally complete response, the engine can feed the last incomplete lines back as a continuation prefix and resume generation. This is controlled by the `--auto-continue` flag, with `--max-continuations` (default 3) setting the upper bound on continuation rounds.

Detection heuristics check for unclosed code fences (` ``` `), unclosed brackets/parentheses, trailing punctuation like `,` or `:`, and a minimum character threshold.

```bash
python -m topogpt3.inference --auto-continue --max-new 512 --prompt "def main("
```

### Thinking mode (HRM)

`--thinking` enables a deeper reasoning configuration in the HRM engine. When active, the hierarchical reasoner increases its high-level iterations to 4 and low-level iterations to 8 per emitted token, trading latency for deeper iterative latent refinement. Combines naturally with auto-continuation:

```bash
python -m topogpt3.inference_hrm --thinking --auto-continue --max-new 512
```

## C Inference Engine

A standalone C implementation of the TopoGPT3 forward pass, compilable as a
static Linux ELF or as a bare-metal MiniOS program. It loads the same
safetensors-derived weight files as the Python engine and produces identical
output, running 60-70% faster than Python on the same hardware.

### Features

- Full transformer forward pass: GQA attention with RoPE, sliding window,
  RMSNorm, SwiGLU MoE with top-2 routing, quaternion torus spectral layers.
- Hand-rolled math (sqrt, exp, tanh, sin, cos, log) -- no libm dependency
  in standalone mode.
- In-place radix-2 FFT and 2D FFT for torus spectral layers.
- Weight loading from flat binary files (float32 `TG3W` or float16 `TG16`).
- Token decoding via GPT-2 BPE vocabulary file (`vocab.bin`) or a fallback
  byte-level encoder.
- Three operating modes: headless (`-p`), interactive (`-i`), and
  file-based (`-f`).
- Pre-tokenized binary input (`-T`).
- tok/s timing display via `rdtsc`.

### Building (Linux host)

```bash
# Convert weights to flat binary (float32, 94 MB)
python convert_weights.py -i checkpoints_topogpt3/last/model.safetensors \
    -o topogpt3.weights

# Or convert to float16 (47 MB, for MiniOS)
python convert_weights_minios.py -i checkpoints_topogpt3/last/model.safetensors \
    -o topogpt3.fp16

# Generate vocabulary file
# (encode_tokens.py generates tokens.bin for pre-tokenized input;
#  vocab.bin is generated separately and distributed with the project)

# Compile
gcc -static -no-pie -O2 -o topogpt3.elf topogpt3.c -lm
```

### Command-line options

```
TopoGPT3 - Quaternion Topological Transformer Inference

Usage:
  topogpt3 -h                      Show help
  topogpt3 -p "prompt" [options]   Generate text (headless)
  topogpt3 -i [options]            Interactive mode
  topogpt3 -f file.txt [options]   Read prompt from file
  topogpt3 -T tokens.bin           Read pre-tokenized binary IDs

Options:
  -w FILE    Weight file (default: topogpt3.weights)
  -v FILE    Vocabulary file (default: vocab.bin)
  -n NUM     Max new tokens (default: 256)
  -t NUM     Temperature (default: 0.3)
  -k NUM     Top-k (default: 50)
  -r NUM     Repetition penalty (default: 1.1)
```

### Usage examples

Headless generation:

```bash
./topogpt3.elf -w topogpt3.weights -v vocab.bin \
    -p "def fibonacci(n):" -n 100 -t 0.2
```

Interactive mode:

```bash
./topogpt3.elf -w topogpt3.weights -v vocab.bin -i
```

Inside the interactive session:

```
TopoGPT3 Inference Engine
Model: small (d=256, heads=8, layers=6, kv=2)
Loading weights from: topogpt3.weights
Loaded vocab: 50257 tokens (321428 bytes)
Loading 380 tensors (v1)...
  Layer 0 loaded
  ...
Weights loaded successfully.
Ready.

interactive mode. /help for commands.
> def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

> /temp 0.1
Temperature set to 0.10

> /topk 20
Top-k set to 20

> /status
Model: small (d=256, heads=8, layers=6, kv=2, experts=4, topk=2)
Context: 32 tokens
Parameters: temp=0.10 topk=20 rep=1.10 max=256

> /quit
```

Interactive mode commands:

```
/help      Show commands
/quit      Exit
/clear     Clear prompt buffer
/temp N    Set temperature
/topk N    Set top-k
/rep N     Set repetition penalty
/newtokens N  Set max new tokens
/status    Show current settings
```

Reading a prompt from a file:

```bash
./topogpt3.elf -w topogpt3.weights -v vocab.bin -f prompt.txt -n 200
```

Using pre-tokenized binary input:

```bash
# On the host: tokenize text to binary IDs
python encode_tokens.py -t checkpoints_topogpt3/last -p "def hello():" \
    -o tokens.bin

# Run inference from binary token IDs
./topogpt3.elf -w topogpt3.weights -v vocab.bin -T tokens.bin -n 50
```

### Building for MiniOS

TopoGPT3 runs as a ring-3 Linux ELF inside MiniOS, exactly like Lua,
MicroPython, and DOOM. The float16 weight format keeps the filesystem
footprint under 50 MB.

```bash
cd /path/to/miniOS

# Build the binary
make progs/bin/topogpt3.elf

# Rebuild the MiniFS image (includes topogpt3.elf, weights, vocab)
make minifs.bin

# Rebuild the full disk image
make os.img

# Run in QEMU
make run
```

Inside MiniOS, the program is launched from the shell:

```
miniOS> topogpt3 -w topogpt3.fp16 -v vocab.bin -p "def fibonacci(n):" -n 30

TopoGPT3 Inference Engine
Model: small (d=256, heads=8, layers=6, kv=2)
Loading weights from: topogpt3.fp16
Loaded vocab: 50257 tokens (321428 bytes)
Loading 380 tensors (fp16 v2)...
  Layer 0 loaded
  ...
Weights loaded successfully (fp16).
Ready.

Prompt: 17 tokens
---

        return n

---
Generated 12 tokens in 15.03s (0.80 tok/s)
```

The 0.80 tok/s figure reflects QEMU software emulation without KVM.
With KVM acceleration, performance matches the Linux host (17-29 tok/s).

Interactive mode also works inside MiniOS:

```
miniOS> topogpt3 -w topogpt3.fp16 -v vocab.bin -i

interactive mode. /help for commands.
> def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

> /quit
```

### Weight formats

The engine supports two binary weight formats, auto-detected at load time:

| Format | Magic | Precision | Size   | Description                    |
|--------|-------|-----------|--------|--------------------------------|
| TG3W   | TG3W  | float32   | 94 MB  | Full-precision, Linux host use |
| TG16   | TG16  | float16   | 47 MB  | Half-precision, MiniOS use     |

Convert between formats:

```bash
# float32 (default)
python convert_weights.py -i checkpoints_topogpt3/last/model.safetensors \
    -o topogpt3.weights

# float16 (for MiniOS)
python convert_weights_minios.py -i checkpoints_topogpt3/last/model.safetensors \
    -o topogpt3.fp16
```

### Files on MiniFS

When built for MiniOS, the following files are placed on the MiniFS
filesystem:

| File            | Size     | Description                          |
|-----------------|----------|--------------------------------------|
| topogpt3.elf    | 841 KB   | Static Linux ELF binary              |
| topogpt3.fp16   | 47 MB    | Float16 model weights                |
| vocab.bin       | 422 KB   | GPT-2 BPE vocabulary (50257 tokens)  |

### Performance

Measured on the prompt `def fibonacci(n):` with 30 new tokens, temperature
0.3, top-k 50:

| Platform                    | Speed       |
|-----------------------------|-------------|
| Linux host (KVM)            | 17-29 tok/s |
| Linux host (no KVM)         | 8-12 tok/s  |
| MiniOS QEMU (no KVM)        | 0.80 tok/s  |
| MiniOS QEMU (with KVM)      | 17-29 tok/s |

## Repository layout

```
.
├── topogpt3/                  pip-installable package
│   ├── __init__.py            public API re-exports
│   ├── model.py               base TopoGPT2 architecture, tokenizer, helpers
│   ├── train.py               curriculum trainer + Grassmannian diagnostics
│   ├── inference.py           standard autoregressive sampler
│   ├── inference_hrm.py       hierarchical recursive reasoning sampler
│   ├── continuation.py        auto-continuation engine (detect + resume truncated output)
│   ├── lens_model.py          Jacobian-lens model adapter (LensModel protocol)
│   ├── jlens.py               Jacobian lens fitting + application pipeline
│   └── api_server.py          OpenAI-compatible HTTP API server (hardened)
├── tests/                     BDD test suite
│   ├── test_lens_model.py     adapter contract tests
│   └── test_jlens.py          fitting + application contract tests
├── eval/                      HumanEval benchmark harness
│   ├── harness.py             evaluation pipeline
│   ├── samplers.py            sampler registry (standard / HRM)
│   ├── sandbox.py             sandboxed test executor
│   ├── analysis.py            pass@k / metrics reporting
│   └── diag_static.py         static checkpoint diagnostics (kappa, delta, winding, context-length)
├── topogpt3.c                 standalone C inference engine (~2000 lines)
├── convert_weights.py         safetensors to float32 binary converter
├── convert_weights_minios.py  safetensors to float16 binary converter (MiniOS)
├── encode_tokens.py           GPT-2 BPE tokenizer to binary IDs
├── vocab.bin                  GPT-2 BPE vocabulary (50257 tokens, 422 KB)
├── topogpt3.weights           float32 weights (94 MB, generated)
├── topogpt3.fp16              float16 weights (47 MB, generated)
├── topogpt3.elf               static Linux ELF binary (generated)
├── app.py                     example entry point for downstream projects
├── Makefile                   convenience targets for all common commands
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

Extra dependencies:

```
pip install -e ".[train]"   # datasets, huggingface-hub
pip install -e ".[lens]"    # huggingface-hub
pip install -e ".[api]"     # fastapi, uvicorn (for the agent harness)
pip install -e ".[dev]"     # pytest, ruff
```

Or install everything at once:

```
pip install -e ".[train,lens,api,dev]"
```

Once published, the package will be installable directly from PyPI or GitHub:

```
pip install topogpt3
pip install git+https://github.com/grisuno/TopoGPT3
```

The install registers these console scripts:

| Command              | Description                                     |
|----------------------|-------------------------------------------------|
| `topogpt3-train`     | Full curriculum trainer CLI                      |
| `topogpt3-infer`     | Standard autoregressive sampler CLI              |
| `topogpt3-infer-hrm` | Hierarchical recursive reasoning sampler CLI     |
| `topogpt3-jlens`     | Jacobian lens demo (fit + slice + text table)   |
| `topogpt3-api`       | OpenAI-compatible API server (agent harness)     |

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

Inference with auto-continuation:

```
topogpt3-infer --auto-continue --max-new 512 --prompt "def main("
```

Hierarchical recursive inference:

```
topogpt3-infer-hrm --prompt "def fibonacci(" \
    --hrm-h-iters 2 --hrm-l-iters 3 --hrm-l-window 2 --max-new 200
```

HRM thinking mode with auto-continuation:

```
topogpt3-infer-hrm --thinking --auto-continue --max-new 512 --prompt "def main("
```

Jacobian lens visualization:

```
topogpt3-jlens --checkpoint checkpoints_topogpt3/last \
    --prompts 4 --prompt "def fibonacci(n):\n    "
```

Start the API server for Pi / Aider / Continue:

```
export TOPOGPT3_API_KEYS="sk-my-secret-key-12345"
topogpt3-api --checkpoint checkpoints_topogpt3/last --port 8800
```

The same entry points are reachable as modules (useful before installation):

```
python -m topogpt3.train --help
python -m topogpt3.inference --help
python -m topogpt3.inference_hrm --help
python -m topogpt3.jlens --help
python -m topogpt3 api_server --help
python app.py --mode infer --prompt "def main(" --max-new 64
```

Or through the unified dispatcher:

```
python -m topogpt3 infer --auto-continue --max-new 512
python -m topogpt3 infer-hrm --thinking --auto-continue
python -m topogpt3 train
python -m topogpt3 api
```

### Makefile

A `Makefile` at the repo root wraps every common task. Run `make help`
to see all targets.

```
make install           pip install -e ".[train,lens,api,dev]"
make test              run full test suite
make lint              ruff check + format
make train             full curriculum training
make infer             standard inference (prompt=def fibonacci)
make infer-continue    inference with auto-continuation
make infer-hrm         HRM inference
make infer-think       HRM thinking mode with auto-continuation
make jlens             Jacobian lens demo (fit 4 prompts)
make api               start API server on port 8800 (no auth)
make api-auth          start API server with authentication
make eval              HumanEval benchmark (all 164 problems)
make eval-sample       HumanEval single problem
make pi                clone, build, and configure Pi agent
make pi-setup          write TopoGPT3 provider config to ~/.pi/agent/models.json
make pi-run            launch Pi pointed at local TopoGPT3 API
make c-convert         convert weights to float32 binary
make c-vocab           generate vocab.bin
make c-tokenize        tokenize text to binary IDs
make c-build           compile C inference engine
make c-run             run C engine (headless, prompt=def fibonacci)
make c-run-i           run C engine (interactive mode)
make c-all             convert + build + run
make clean             remove __pycache__ and .pyc files
```

## Checkpoint compatibility

The model is always built with the maximum sequence length across all curriculum tiers, so positional embeddings keep a fixed shape regardless of which tier is used as the entry point. Existing safetensors weights load without shape mismatch when restarting at a different tier.

As of the 2026-08 sliding window update, the RoPE (Rotary Position Embedding) caches are stored as non-persistent buffers under the names `_cos_cache` and `_sin_cache`. Checkpoints from earlier versions that contain `cos_cache` and `sin_cache` are safely ignored during loading with `strict=False`. The caches are recomputed to match the current `MAX_SEQ_LEN` configuration at model instantiation time. Memory tokens (`memory_tokens`) are a new parameter introduced alongside the latent compression feature; missing this key in older checkpoints is harmless and produces a warning during load.

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


---
### Topo Journey
If you are interested in this project, explore the architecture evolution:
- [TopoBrain](https://github.com/grisuno/TopoBrain): Topo applied to neural networks.
- [ReadMenator](https://github.com/grisuno/ReadMenator): Knowledge graph generator without LLMs.
- [TopoGPT2](https://github.com/grisuno/TopoGPT2): Previous evolution of the model.
