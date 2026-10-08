# topogpt3: model

*Community 2 | 8 files | cohesion 0.32*

## Definition

This community groups 8 file(s) rooted at `topogpt3` with dominant language py (cohesion 0.32). Central symbols: `ApiKey`, `AuthState`, `BPETokenizer`, `BlockTokenDataset`, `ChatCompletionRequest`, `CheckpointManager`, `CheckpointPaths`, `CheckpointStore`. Core file: `topogpt3/model.py` (188 symbols). Documented purpose: Diagnostico estatico de un checkpoint TopoGPT3 congelado.  Calcula sobre los pesos espectrales congelados (sin reentrenar):  kappa_F   = sigma_max / sigma_min  .

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `eval/diag_static.py` | py | utility | 5 | yes |
| `synthetic_dataset.py` | py | data_access | 35 | yes |
| `topogpt3/api_server.py` | py | presentation | 46 | yes |
| `topogpt3/continuation.py` | py | utility | 5 | yes |
| `topogpt3/export_chat.py` | py | utility | 5 | yes |
| `topogpt3/inference_hrm.py` | py | utility | 76 | yes |
| `topogpt3/model.py` | py | business_logic | 188 | yes |
| `topogpt3/train.py` | py | utility | 62 | yes |

## Key Symbols

- `phase_discretization` (function, `eval/diag_static.py:49`) `def phase_discretization(K, n_samples, seed)` - Muestrea n_samples overlaps aleatorios <u_i \| u_j> sobre los vectores
- `synthetic_winding` (function, `eval/diag_static.py:95`) `def synthetic_winding(K, n_windows, window_size)` - Como el checkpoint es estatico, no hay trayectoria temporal.
- `static_kappa` (function, `eval/diag_static.py:144`) `def static_kappa(K)`
- `context_length_diagnostic` (function, `eval/diag_static.py:171`) `def context_length_diagnostic(model, tracker, device, lengths)`
- `main` (function, `eval/diag_static.py:248`) `def main()`
- `LLMBackend` (class, `synthetic_dataset.py:61`) `class LLMBackend` - Abstract LLM backend. Subclass for each provider.
- `generate` (method, `synthetic_dataset.py:64`) `def generate(self, prompt)`
- `name` (method, `synthetic_dataset.py:67`) `def name(self)`
- `GroqBackend` (class, `synthetic_dataset.py:71`) `class GroqBackend(LLMBackend)` - Groq API backend using requests.
- `__init__` (method, `synthetic_dataset.py:78`) `def __init__(self, model, api_key, max_tokens, temperature, timeout)`
- `name` (method, `synthetic_dataset.py:95`) `def name(self)`
- `generate` (method, `synthetic_dataset.py:98`) `def generate(self, prompt)`
- `OpenRouterBackend` (class, `synthetic_dataset.py:121`) `class OpenRouterBackend(LLMBackend)` - OpenRouter unified API backend.
- `__init__` (method, `synthetic_dataset.py:132`) `def __init__(self, model, api_key, max_tokens, temperature, timeout)`
- `name` (method, `synthetic_dataset.py:151`) `def name(self)`
- `generate` (method, `synthetic_dataset.py:154`) `def generate(self, prompt)`
- `OllamaBackend` (class, `synthetic_dataset.py:177`) `class OllamaBackend(LLMBackend)` - Ollama local inference backend.
- `__init__` (method, `synthetic_dataset.py:184`) `def __init__(self, model, host, max_tokens, temperature, timeout)`
- `name` (method, `synthetic_dataset.py:198`) `def name(self)`
- `generate` (method, `synthetic_dataset.py:201`) `def generate(self, prompt)`
- `build_backend` (method, `synthetic_dataset.py:227`) `def build_backend(provider, model)` - Factory for LLM backends.
- `validate_sample` (method, `synthetic_dataset.py:330`) `def validate_sample(sample)` - Validate that a generated sample meets quality bar.
- `ProcessedManifest` (class, `synthetic_dataset.py:364`) `class ProcessedManifest` - Tracks processed files for resumability.
- `load` (method, `synthetic_dataset.py:374`) `def load(path)`
- `save` (method, `synthetic_dataset.py:387`) `def save(self, path)`
- `SyntheticDatasetGenerator` (class, `synthetic_dataset.py:399`) `class SyntheticDatasetGenerator` - Generates synthetic instruction-tuning data from source files.
- `__init__` (method, `synthetic_dataset.py:418`) `def __init__(self, backend, output_path, manifest_path, logger, max_workers, max`
- `_jsonl_writer` (method, `synthetic_dataset.py:447`) `def _jsonl_writer(self)` - Background thread that drains the queue and writes JSONL lines.
- `_enqueue_sample` (method, `synthetic_dataset.py:465`) `def _enqueue_sample(self, sample)`
- `_flush_writer` (method, `synthetic_dataset.py:468`) `def _flush_writer(self)`

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 10
- Cross-boundary resolved imports (EXTRACTED): 25

## Connections

- [EXTRACTED] depends_on community 2 <-> 1 (strength 0.9): Extracted import edge crosses communities: eval/diag_static.py imports topogpt3/__init__.py.
- [EXTRACTED] depends_on community 3 <-> 2 (strength 0.9): Extracted import edge crosses communities: tests/test_heritage.py imports topogpt3/model.py.
- [EXTRACTED] depends_on community 4 <-> 2 (strength 0.9): Extracted import edge crosses communities: tests/test_lens_model.py imports topogpt3/model.py.
- [EXTRACTED] depends_on community 0 <-> 2 (strength 0.9): Extracted import edge crosses communities: topogpt3/__main__.py imports topogpt3/api_server.py.
- [INFERRED] bridges community 3 <-> 2 (strength 0.5): Inferred cross-community bridge: eval/sandbox_smoke.py reaches synthetic_dataset.py in 5 hops.
- [INFERRED] bridges community 3 <-> 2 (strength 0.5): Inferred cross-community bridge: eval/sandbox_smoke.py reaches topogpt3/continuation.py in 5 hops.
- [INFERRED] shares_context community 2 <-> 5 (strength 0.5): Inferred shared context (language py and layer utility) with no import path between community 2 (topogpt3: model) and community 5 (root).
- [INFERRED] shares_context community 2 <-> 6 (strength 0.5): Inferred shared context (language py and layer utility) with no import path between community 2 (topogpt3: model) and community 6 (orphans).

## Risks

- [taint critical] `eval/governor_smoke.py` -> `topogpt3/model.py` via `eval` (2 hops)
- [taint critical] `eval/governor_smoke.py` -> `topogpt3/inference_hrm.py` via `eval` (2 hops)
- [taint critical] `eval/governor_smoke.py` -> `topogpt3/train.py` via `eval` (2 hops)
- [taint critical] `eval/governor_smoke.py` -> `topogpt3/continuation.py` via `eval` (3 hops)
- [taint critical] `eval/governor_smoke.py` -> `synthetic_dataset.py` via `eval` (3 hops)
- [dataflow UNCHECKED_ALLOC] `topogpt3/export_chat.py:105` `main` `sft`: Result of allocator stored in `sft` is never checked against NULL.
- [dataflow UNCHECKED_ALLOC] `topogpt3/export_chat.py:106` `main` `rla`: Result of allocator stored in `rla` is never checked against NULL.
- [dataflow UNCHECKED_ALLOC] `topogpt3/export_chat.py:107` `main` `dpo`: Result of allocator stored in `dpo` is never checked against NULL.
- [dataflow UNCHECKED_ALLOC] `topogpt3/export_chat.py:132` `main` `pre`: Result of allocator stored in `pre` is never checked against NULL.

## Open Questions

- What would break if the most connected file in topogpt3: model changed?
- Should topogpt3: model be split, given cohesion 0.32?

## Sources

- `eval/diag_static.py`
- `synthetic_dataset.py`
- `topogpt3/api_server.py`
- `topogpt3/continuation.py`
- `topogpt3/export_chat.py`
- `topogpt3/inference_hrm.py`
- `topogpt3/model.py`
- `topogpt3/train.py`
