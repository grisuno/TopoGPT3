# Subsystem: eval

## eval/analyze.py
- Layer: utility
- Language: py
- Symbols:
  - `pass_at_k` (function, line 21) `def pass_at_k(n, c, k)`
  - `classify_error` (function, line 32) `def classify_error(msg, candidate_src)`
  - `load_jsonl` (function, line 56) `def load_jsonl(path)`
  - `summarize` (function, line 61) `def summarize(paths)`
  - `main` (function, line 103) `def main()`

## eval/analyze_results.py
- Layer: utility
- Language: py
- Symbols:
  - `load_records` (function, line 26) `def load_records(path)`
  - `summarize` (function, line 31) `def summarize(records)`
  - `show_failures` (function, line 44) `def show_failures(records, task_id)`
  - `main` (function, line 82) `def main()`

## eval/diag_static.py
- Layer: infrastructure
- Language: py
- Symbols:
  - `phase_discretization` (function, line 49) `def phase_discretization(K, n_samples, seed)`
  - `synthetic_winding` (function, line 95) `def synthetic_winding(K, n_windows, window_size)`
  - `static_kappa` (function, line 144) `def static_kappa(K)`
  - `context_length_diagnostic` (function, line 171) `def context_length_diagnostic(model, tracker, device, lengths)`
  - `main` (function, line 248) `def main()`
- Depends on: `topogpt3.c`, `topogpt3/model.py`, `topogpt3/train.py`

## eval/governor.py
- Layer: utility
- Language: py
- Symbols:
  - `TokenStream` (class, line 45) `class TokenStream`
  - `StopReason` (class, line 99) `class StopReason(str, Enum)`
  - `GenerationResult` (class, line 109) `class GenerationResult`
  - `GenerationGovernor` (class, line 134) `class GenerationGovernor`
  - `make_loop_detector` (method, line 285) `def make_loop_detector(window, min_repeats)`
  - `make_timeout_hook` (method, line 314) `def make_timeout_hook(per_token_s)`
  - `__init__` (method, line 56) `def __init__(self)`
  - `put` (method, line 62) `def put(self, tok)`
  - `mark_done` (method, line 67) `def mark_done(self)`
  - `drain` (method, line 72) `def drain(self)`
  - `wait_for_new` (method, line 77) `def wait_for_new(self, timeout)`
  - `is_closed` (method, line 86) `def is_closed(self)`
  - `__len__` (method, line 90) `def __len__(self)`
  - `__post_init__` (method, line 117) `def __post_init__(self)`
  - `__init__` (method, line 156) `def __init__(self, model, ctx, stream, max_new_tokens, temperature, top_k, repetition_penalty, max_seq_len)`
  - `cancel` (method, line 177) `def cancel(self)`
  - `_should_cancel` (method, line 182) `def _should_cancel(self)`
  - `run` (method, line 185) `def run(self, stop_hooks)`
  - `hook` (method, line 292) `def hook(generated)`
  - `hook` (method, line 320) `def hook(generated)`
- Imported by: `eval/governor_smoke.py`

## eval/governor_smoke.py
- Layer: utility
- Language: py
- Symbols:
  - `load_model` (function, line 30) `def load_model()`
  - `test_tokenstream_threadsafety` (function, line 49) `def test_tokenstream_threadsafety()`
  - `test_governor_basic` (function, line 79) `def test_governor_basic()`
  - `test_loop_detector` (function, line 98) `def test_loop_detector()`
  - `test_cancel` (function, line 118) `def test_cancel()`
  - `producer` (function, line 53) `def producer()`
  - `consumer` (function, line 59) `def consumer()`
- Depends on: `eval/governor.py`, `topogpt3.c`

## eval/harness.py
- Layer: utility
- Language: py
- Symbols:
  - `load_humaneval` (function, line 59) `def load_humaneval(cache_dir)`
  - `build_prompt` (function, line 75) `def build_prompt(problem)`
  - `extract_candidate` (function, line 100) `def extract_candidate(prompt, completion)`
  - `run_one_test` (function, line 150) `def run_one_test(problem, candidate_src, timeout)`
  - `run_one_test_sandboxed` (function, line 172) `def run_one_test_sandboxed(problem, candidate_src, timeout, sandbox_cfg)`
  - `make_sampler` (function, line 195) `def make_sampler(mode, settings_kwargs)`
  - `completion_for_problem` (function, line 204) `def completion_for_problem(sampler, prompt)`
  - `ModelLoader` (class, line 217) `class ModelLoader`
  - `evaluate_problem` (method, line 272) `def evaluate_problem(problem, loader, args, sample_idx)`
  - `main` (method, line 315) `def main()`
  - `__init__` (method, line 220) `def __init__(self, ckpt_dir, ckpt_name, device)`
  - `generate` (method, line 246) `def generate(self, prompt, max_new_tokens, temperature, top_k, repetition_penalty)`
- Depends on: `eval/samplers.py`, `eval/sandbox.py`, `topogpt3.c`
- Imported by: `eval/integration_smoke.py`, `eval/noise_sweep.py`, `eval/temp_sweep.py`

## eval/integration_smoke.py
- Layer: utility
- Language: py
- Symbols:
  - `main` (function, line 18) `def main()`
- Depends on: `eval/harness.py`

## eval/noise_analysis.py
- Layer: utility
- Language: py
- Symbols:
  - `_load` (function, line 43) `def _load(p)`
  - `consistency_across_runs` (function, line 47) `def consistency_across_runs(per_run)`
  - `main` (function, line 83) `def main()`

## eval/noise_sweep.py
- Layer: utility
- Language: py
- Symbols:
  - `inject_noise` (function, line 46) `def inject_noise(model, sigma, seed)`
  - `load_model` (function, line 74) `def load_model(ckpt_dir, ckpt_name, device)`
  - `generate_one` (function, line 99) `def generate_one(model, tok, prompt, max_new_tokens, device)`
  - `main` (function, line 117) `def main()`
- Depends on: `eval/harness.py`, `topogpt3.c`, `topogpt3/model.py`
- Imported by: `eval/temp_sweep.py`

## eval/repair.py
- Layer: utility
- Language: py
- Symbols:
  - `_new_loader` (function, line 36) `def _new_loader(ckpt_dir, ckpt_name)`
  - `extract_candidate` (function, line 49) `def extract_candidate(prompt, completion)`
  - `run_test` (function, line 75) `def run_test(problem, candidate_src)`
  - `build_repair_prompt` (function, line 89) `def build_repair_prompt(prompt, candidate, err, entry_point)`
  - `gen` (function, line 104) `def gen(model, tok, text, max_new_tokens, temperature, top_k, rep_penalty)`
  - `main` (function, line 119) `def main()`
- Depends on: `topogpt3.c`

## eval/report.py
- Layer: utility
- Language: py
- Symbols:
  - `pass_at_k` (function, line 25) `def pass_at_k(n, c, k)`
  - `classify_error` (function, line 31) `def classify_error(msg)`
  - `load_jsonl` (function, line 52) `def load_jsonl(p)`
  - `summarize_run` (function, line 56) `def summarize_run(p)`
  - `repair_summary` (function, line 90) `def repair_summary(repair_path, baseline_path)`
  - `main` (function, line 117) `def main()`

## eval/samplers.py
- Layer: utility
- Language: py
- Symbols:
  - `register_sampler` (function, line 36) `def register_sampler(name)`
  - `_is_env_truthy` (function, line 55) `def _is_env_truthy(name)`
  - `_make_standard` (function, line 64) `def _make_standard(settings_kwargs)`
  - `_make_hrm` (function, line 69) `def _make_hrm(settings_kwargs)`
  - `list_samplers` (function, line 86) `def list_samplers()`
  - `build_sampler` (function, line 90) `def build_sampler(mode, settings_kwargs)`
  - `deco` (function, line 42) `def deco(fn)`
- Depends on: `topogpt3.c`
- Imported by: `eval/harness.py`, `eval/harness.py`

## eval/sandbox.py
- Layer: utility
- Language: py
- Symbols:
  - `SandboxConfig` (class, line 53) `class SandboxConfig`
  - `_names_imported` (method, line 100) `def _names_imported(tree)`
  - `_blocked_dunder_access` (method, line 114) `def _blocked_dunder_access(tree, blocked)`
  - `_max_depth` (method, line 123) `def _max_depth(tree)`
  - `check_safety` (method, line 133) `def check_safety(source, cfg)`
  - `_build_worker_src` (method, line 254) `def _build_worker_src(allowed_builtin_names, program_src, blocked_modules)`
  - `safe_exec` (method, line 270) `def safe_exec(program_src, cfg, extra_globals)`
  - `describe_policy` (method, line 373) `def describe_policy(cfg)`
  - `d` (method, line 125) `def d(node, cur)`
- Imported by: `eval/harness.py`, `eval/sandbox_smoke.py`

## eval/sandbox_smoke.py
- Layer: utility
- Language: py
- Symbols:
  - `main` (function, line 15) `def main()`
- Depends on: `eval/sandbox.py`

## eval/smoke.py
- Layer: utility
- Language: py
- Symbols:
  - `run_standard` (function, line 17) `def run_standard()`
  - `run_hrm` (function, line 36) `def run_hrm()`
- Depends on: `topogpt3.c`

## eval/temp_sweep.py
- Layer: utility
- Language: py
- Symbols:
  - `generate_one` (function, line 39) `def generate_one(model, tok, prompt, max_new_tokens, temperature, top_k, device, seed_offset)`
  - `evaluate_problems` (function, line 58) `def evaluate_problems(model, tok, problems, max_new_tokens, temperature, top_k, n_samples, device)`
  - `pass_at_k_unbiased` (function, line 88) `def pass_at_k_unbiased(n, c, k)`
  - `summarize` (function, line 96) `def summarize(results, n_samples)`
  - `main` (function, line 116) `def main()`
- Depends on: `eval/harness.py`, `eval/noise_sweep.py`
