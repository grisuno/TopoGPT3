# eval

*Community 1 | 11 files | cohesion 0.43*

## Definition

This community groups 11 file(s) rooted at `eval` with dominant language py (cohesion 0.43). Central symbols: `CheckpointPaths`, `CliArgumentParser`, `GaussPatchApplier`, `GenerationEngine`, `GenerationGovernor`, `GenerationReport`, `GenerationResult`, `InferenceLoggerFactory`. Core file: `topogpt3/inference.py` (54 symbols). Documented purpose: Streaming + governance for autoregressive generation.  Two classes that fix two real problems with the existing `topogpt3.inference` pipeline:  - `TokenStream` .

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `eval/governor.py` | py | utility | 20 | yes |
| `eval/governor_smoke.py` | py | utility | 7 | yes |
| `eval/harness.py` | py | utility | 12 | yes |
| `eval/integration_smoke.py` | py | utility | 1 | yes |
| `eval/noise_sweep.py` | py | utility | 4 | yes |
| `eval/repair.py` | py | utility | 6 | yes |
| `eval/samplers.py` | py | utility | 7 | yes |
| `eval/smoke.py` | py | utility | 2 | yes |
| `eval/temp_sweep.py` | py | utility | 5 | yes |
| `topogpt3/__init__.py` | py | utility | 0 | yes |
| `topogpt3/inference.py` | py | utility | 54 | yes |

## Key Symbols

- `TokenStream` (class, `eval/governor.py:45`) `class TokenStream` - Thread-safe single-producer / single-consumer queue of token IDs.
- `__init__` (method, `eval/governor.py:56`) `def __init__(self)`
- `put` (method, `eval/governor.py:62`) `def put(self, tok)`
- `mark_done` (method, `eval/governor.py:67`) `def mark_done(self)`
- `drain` (method, `eval/governor.py:72`) `def drain(self)` - Return all tokens emitted so far, atomic snapshot.
- `wait_for_new` (method, `eval/governor.py:77`) `def wait_for_new(self, timeout)` - Block up to `timeout` seconds for a new token. Returns True
- `is_closed` (method, `eval/governor.py:86`) `def is_closed(self)`
- `__len__` (method, `eval/governor.py:90`) `def __len__(self)`
- `StopReason` (class, `eval/governor.py:99`) `class StopReason(str, Enum)`
- `GenerationResult` (class, `eval/governor.py:109`) `class GenerationResult` - Outcome of a governed generation.
- `__post_init__` (method, `eval/governor.py:117`) `def __post_init__(self)`
- `GenerationGovernor` (class, `eval/governor.py:134`) `class GenerationGovernor` - Run a model's autoregressive generation loop with optional stop
- `__init__` (method, `eval/governor.py:156`) `def __init__(self, model, ctx, stream, max_new_tokens, temperature, top_k, repet`
- `cancel` (method, `eval/governor.py:177`) `def cancel(self)` - Asynchronously stop the generation. Safe to call from any
- `_should_cancel` (method, `eval/governor.py:182`) `def _should_cancel(self)`
- `run` (method, `eval/governor.py:185`) `def run(self, stop_hooks)` - Execute the generation loop. Returns when the model emits
- `make_loop_detector` (method, `eval/governor.py:285`) `def make_loop_detector(window, min_repeats)` - Return True if the last `window` tokens contain a sub-sequence
- `hook` (method, `eval/governor.py:292`) `def hook(generated)`
- `make_timeout_hook` (method, `eval/governor.py:314`) `def make_timeout_hook(per_token_s)` - Return True if the per-token wall time exceeds `per_token_s`.
- `hook` (method, `eval/governor.py:320`) `def hook(generated)`
- `load_model` (function, `eval/governor_smoke.py:30`) `def load_model()`
- `test_tokenstream_threadsafety` (function, `eval/governor_smoke.py:49`) `def test_tokenstream_threadsafety()`
- `producer` (function, `eval/governor_smoke.py:53`) `def producer()`
- `consumer` (function, `eval/governor_smoke.py:59`) `def consumer()`
- `test_governor_basic` (function, `eval/governor_smoke.py:79`) `def test_governor_basic()`
- `test_loop_detector` (function, `eval/governor_smoke.py:98`) `def test_loop_detector()`
- `test_cancel` (function, `eval/governor_smoke.py:118`) `def test_cancel()`
- `load_humaneval` (function, `eval/harness.py:59`) `def load_humaneval(cache_dir)`
- `build_prompt` (function, `eval/harness.py:75`) `def build_prompt(problem)` - Return the exact prompt text fed to the model.
- `extract_candidate` (function, `eval/harness.py:100`) `def extract_candidate(prompt, completion)` - Combine prompt + completion into a single Python source string.

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 14
- Cross-boundary resolved imports (EXTRACTED): 17

## Connections

- [EXTRACTED] depends_on community 2 <-> 1 (strength 0.9): Extracted import edge crosses communities: eval/diag_static.py imports topogpt3/__init__.py.
- [EXTRACTED] depends_on community 1 <-> 3 (strength 0.9): Extracted import edge crosses communities: eval/harness.py imports eval/sandbox.py.
- [EXTRACTED] depends_on community 1 <-> 4 (strength 0.9): Extracted import edge crosses communities: topogpt3/__init__.py imports topogpt3/lens_model.py.
- [EXTRACTED] depends_on community 1 <-> 0 (strength 0.9): Extracted import edge crosses communities: topogpt3/__init__.py imports topogpt3/lora.py.
- [INFERRED] bridges community 1 <-> 3 (strength 0.5): Inferred cross-community bridge: eval/governor.py reaches eval/sandbox_smoke.py in 5 hops.
- [INFERRED] shares_context community 1 <-> 5 (strength 0.5): Inferred shared context (language py and layer utility) with no import path between community 1 (eval) and community 5 (root).
- [INFERRED] shares_context community 1 <-> 6 (strength 0.5): Inferred shared context (language py and layer utility) with no import path between community 1 (eval) and community 6 (orphans).

## Risks

- [taint critical] `eval/governor_smoke.py` -> `eval/governor_smoke.py` via `eval` (0 hops)
- [taint critical] `eval/governor_smoke.py` -> `eval/governor.py` via `eval` (1 hops)
- [taint critical] `eval/governor_smoke.py` -> `topogpt3/__init__.py` via `eval` (1 hops)
- [taint critical] `eval/governor_smoke.py` -> `topogpt3/rewards.py` via `eval` (2 hops)
- [taint critical] `eval/governor_smoke.py` -> `topogpt3/trainer_utils_topo.py` via `eval` (2 hops)
- [taint critical] `eval/governor_smoke.py` -> `topogpt3/lora.py` via `eval` (2 hops)
- [taint critical] `eval/governor_smoke.py` -> `topogpt3/model.py` via `eval` (2 hops)
- [taint critical] `eval/governor_smoke.py` -> `topogpt3/inference_hrm.py` via `eval` (2 hops)
- [taint critical] `eval/governor_smoke.py` -> `topogpt3/train.py` via `eval` (2 hops)
- [taint critical] `eval/governor_smoke.py` -> `topogpt3/jlens.py` via `eval` (2 hops)
- [taint critical] `eval/governor_smoke.py` -> `topogpt3/tools_agent.py` via `eval` (2 hops)
- [taint critical] `eval/governor_smoke.py` -> `topogpt3/eval_toolcall.py` via `eval` (2 hops)
- [taint critical] `eval/governor_smoke.py` -> `topogpt3/lens_model.py` via `eval` (2 hops)
- [taint critical] `eval/governor_smoke.py` -> `topogpt3/chat.py` via `eval` (2 hops)
- [taint critical] `eval/governor_smoke.py` -> `topogpt3/yarn.py` via `eval` (2 hops)

## Open Questions

- Is the dangerous import `eval` in `eval/governor_smoke.py` still required, or can it be isolated?
- What would break if the most connected file in eval changed?
- Should eval be split, given cohesion 0.43?

## Sources

- `eval/governor.py`
- `eval/governor_smoke.py`
- `eval/harness.py`
- `eval/integration_smoke.py`
- `eval/noise_sweep.py`
- `eval/repair.py`
- `eval/samplers.py`
- `eval/smoke.py`
- `eval/temp_sweep.py`
- `topogpt3/__init__.py`
- `topogpt3/inference.py`
