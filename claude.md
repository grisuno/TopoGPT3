# TopoGPT3 Project Contracts

## Jacobian Lens Contracts (topogpt3/lens_model.py + topogpt3/jlens.py)

Two self-contained contracts implement the Jacobian lens (Anthropic, Apache 2.0) for TopoGPT3.

### Contract A: `topogpt3/lens_model.py` -- Model Adapter

Wraps a TopoGPT2 model into the `LensModel` protocol for use with `ActivationRecorder`, `fit()`, and `JacobianLens.apply()`.

**Classes:**
- `LensModel` (Protocol) -- duck-typed interface: `n_layers`, `d_model`, `layers`, `encode()`, `forward()`, `unembed()`
- `TopoGPT3LensConfig` -- frozen dataclass; all adapter tunables centralized here
- `TopoGPT3LensModel` (nn.Module) -- wraps TopoGPT2; `forward()` runs residual blocks only (no final_norm, no LM head); `unembed()` applies final_norm + lm_head separately
- `TinyDecoder` -- 4-layer CPU test model (d_model=8, vocab=32) for TDD without GPU

**Key design decisions:**
- `forward()` stops before `final_norm` so `ActivationRecorder` hooks capture raw residuals
- `from_checkpoint()` classmethod probes state.json, loads safetensors, configures model in eval mode with `requires_grad_(False)`
- No `transformers` dependency needed; implements `LensModel` directly
- All paths parameterized; no absolute paths or hardcoded values

### Contract B: `topogpt3/jlens.py` -- Fitting + Application

Vendored core from jlens (Apache 2.0, Anthropic PBC) adapted for TopoGPT3.

**Classes:**
- `ActivationRecorder` -- context manager; registers forward hooks on `model.layers`, captures residual activations, `start_graph_at` roots autograd graph
- `JacobianLens` -- stores per-layer `J_l [d_model x d_model]` matrices; `apply()`, `transport()`, `save()`, `load()`, `merge()`, `from_pretrained()`
- `TopoGPT3JLensFitConfig` -- frozen dataclass; all fitting tunables centralized
- `TopoGPT3JLensAppConfig` -- frozen dataclass; all application tunables centralized

**Functions:**
- `valid_position_mask(seq_len, skip_first)` -- boolean mask excluding attention-sink and final positions
- `jacobian_for_prompt(model, prompt, source_layers, ...)` -- one forward + ceil(d_model/dim_batch) backward passes
- `fit(model, prompts, ...)` -- running mean over prompts; supports checkpoint resume with atomic save

### Security and Tech Debt Remediation (Boy Scout)

| Fix | Location | Change |
|-----|----------|--------|
| `weights_only=False` -> `True` | model.py:2136 | Prevent pickle deserialization attack |
| Missing `weights_only=True` | train.py:1083 | Same hardening |
| Hardcoded user home path | model.py:135 | `CORPUS_ROOT` defaulted to `./src` |
| `generated.extend` bug | model.py:1786 | Removed incorrect assignment that overwrote list |
| Empty requirements.txt | root | Removed (deps in pyproject.toml) |

### Methodology: SDD + TDD + BDD

1. **SDD (Spec-Driven Development)**: Contracts defined first (lens_model.py + jlens.py) with all config centralized in frozen dataclasses
2. **TDD (Test-Driven Development)**: Tests written covering every public API surface: 40+ scenarios in `tests/test_lens_model.py` and `tests/test_jlens.py`
3. **BDD (Behavior-Driven Development)**: Feature/Scenario/Given/When/Then structure in test docstrings
4. **Boy Scout Rule**: Security fixes (pickle deserialization) and tech debt remediation performed before adding new code

### Testing

```
pytest tests/test_lens_model.py -v --tb=short
pytest tests/test_jlens.py -v --tb=short
```

### Jacobian lens usage

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

---

## Using TopoGPT3 with Claude and Anthropic Models

This guide covers how to integrate TopoGPT3 with Claude, Anthropic APIs, and broader AI workflows.

Project URL: [https://github.com/grisuno/TopoGPT3](https://github.com/grisuno/TopoGPT3)

---

## Overview

TopoGPT3 is a compact, complex-valued language model for code. While it runs independently, it pairs well with Claude and other large models in hybrid pipelines:

- **Claude as orchestrator**: Use Claude to plan, decompose tasks, and validate outputs.
- **TopoGPT3 as local inference engine**: Use TopoGPT3 for fast, private, on-device code generation and completion.
- **Synthetic data generation**: Use Claude (or other LLMs) to create training data for TopoGPT3 via `synthetic_dataset.py`.

## Synthetic Data Generation with Claude

The `synthetic_dataset.py` script supports OpenRouter, which provides access to Claude models.

### Setup

1. Obtain an OpenRouter API key.
2. Set the environment variable:

```bash
export OPENROUTER_API_KEY="your-key-here"
```

3. Run the generator with a Claude model:

```bash
python synthetic_dataset.py \
    --provider openrouter \
    --model anthropic/claude-3.5-sonnet \
    --paths-file my_source_files.txt \
    --output data/synthetic_claude.jsonl
```

### Supported Claude Models via OpenRouter

- `anthropic/claude-3.5-sonnet`
- `anthropic/claude-3-opus`
- `anthropic/claude-3-haiku`

## Hybrid Pipeline Example

A typical workflow combining Claude and TopoGPT3:

```python
# Step 1: Use Claude to generate a high-level plan
claude_plan = call_claude_api(
    "Write a Python module that implements a LRU cache with thread safety."
)

# Step 2: Use TopoGPT3 for fast local completion or refinement
from topogpt3 import InferenceSettings, InferencePipeline

settings = InferenceSettings(
    checkpoint_dir="checkpoints_topogpt3",
    prompt=f"# LRU cache with thread safety\n{claude_plan}\n\ndef ",
    max_new_tokens=300,
)
report = InferencePipeline(settings).execute()
local_code = report.output

# Step 3: Use Claude to review and test the generated code
review = call_claude_api(
    f"Review this Python code for correctness and add unit tests:\n\n{local_code}"
)
```

## Prompt Engineering Tips for Hybrid Use

When passing Claude outputs into TopoGPT3:

- Keep prompts focused on a single function or class.
- Include type hints and docstrings in the prompt to steer style.
- Use `def` or `class` prefixes to trigger code completion behavior.
- Set temperature low (`0.2` to `0.3`) for deterministic completions.

## Using Claude to Improve TopoGPT3

You can use Claude to:

1. **Analyze diagnostics**: Feed training diagnostics (Fisher gap, phase drift, singular values) to Claude for interpretation and suggestions.
2. **Generate curriculum data**: Ask Claude to create instruction-response pairs for weak areas identified during evaluation.
3. **Refine HRM configurations**: Ask Claude to suggest `RecursiveReasoningConfig` parameters based on the task complexity.

## Anthropic API Integration in synthetic_dataset.py

The script uses the OpenRouter backend to reach Claude. If you prefer direct Anthropic API access, extend the `LLMBackend` class:

```python
class AnthropicBackend(LLMBackend):
    def __init__(self, model="claude-3-5-sonnet-20241022", api_key=None):
        import anthropic
        self.client = anthropic.Anthropic(api_key=api_key or os.environ.get("ANTHROPIC_API_KEY"))
        self.model = model

    def generate(self, prompt: str, **kwargs) -> str:
        message = self.client.messages.create(
            model=self.model,
            max_tokens=kwargs.get("max_tokens", 4096),
            messages=[{"role": "user", "content": prompt}],
        )
        return message.content[0].text
```

Register it in `build_backend` and use `--provider anthropic`.

## Privacy Considerations

- TopoGPT3 runs entirely locally after installation; no data leaves your machine during inference.
- Claude API calls send data to Anthropic servers; use them only for data generation or orchestration, not for sensitive code.

## Further Reading

- [Quick Start](quickstart.md)
- [Tutorial](tutorial.md)
- [Essential Concepts](essentials.md)

---

**License**: GPL v3 | **Author**: grisun0
