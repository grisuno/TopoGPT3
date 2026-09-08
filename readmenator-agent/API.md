# API

## app.py

### run_inference (function) `def run_inference(prompt, checkpoint_dir, checkpoint_name, max_new_tokens, temperature, top_k, repetition_penalty, device)`
- Defined: `app.py:46`
- Doc: Run the standard sampler and return the generated completion text.
- Depends on: `topogpt3.c`

### run_inference_hrm (function) `def run_inference_hrm(prompt, checkpoint_dir, checkpoint_name, max_new_tokens, temperature, top_k, repetition_penalty, high_level_iters, low_level_iters, low_level_window, device)`
- Defined: `app.py:71`
- Doc: Run the hierarchical recursive sampler and return the completion.
- Depends on: `topogpt3.c`

### run_training (function) `def run_training(scale, start_tier, device, prepare_data)`
- Defined: `app.py:105`
- Doc: Run the full TopoGPT3 curriculum trainer.
- Depends on: `topogpt3.c`

### _build_parser (function) `def _build_parser()`
- Defined: `app.py:121`
- Doc: Build the top-level CLI for this entry point script.
- Depends on: `topogpt3.c`

### main (function) `def main(argv)`
- Defined: `app.py:159`
- Doc: Entry point invoked when the file is executed as a script.
- Depends on: `topogpt3.c`

## convert_weights.py

### convert (function) `def convert(input_path, output_path)`
- Defined: `convert_weights.py:102`

### main (function) `def main()`
- Defined: `convert_weights.py:160`

## convert_weights_minios.py

### main (function) `def main()`
- Defined: `convert_weights_minios.py:85`

## encode_tokens.py

### main (function) `def main()`
- Defined: `encode_tokens.py:19`

## eval/analyze.py

### pass_at_k (function) `def pass_at_k(n, c, k)`
- Defined: `eval/analyze.py:21`
- Doc: Unbiased estimator from the HumanEval paper.

### classify_error (function) `def classify_error(msg, candidate_src)`
- Defined: `eval/analyze.py:32`
- Doc: Heuristic single-label error classifier.

### load_jsonl (function) `def load_jsonl(path)`
- Defined: `eval/analyze.py:56`

### summarize (function) `def summarize(paths)`
- Defined: `eval/analyze.py:61`

### main (function) `def main()`
- Defined: `eval/analyze.py:103`

## eval/analyze_results.py

### load_records (function) `def load_records(path)`
- Defined: `eval/analyze_results.py:26`

### summarize (function) `def summarize(records)`
- Defined: `eval/analyze_results.py:31`

### show_failures (function) `def show_failures(records, task_id)`
- Defined: `eval/analyze_results.py:44`

### main (function) `def main()`
- Defined: `eval/analyze_results.py:82`

## eval/diag_static.py

### phase_discretization (function) `def phase_discretization(K, n_samples, seed)`
- Defined: `eval/diag_static.py:49`
- Doc: Muestrea n_samples overlaps aleatorios <u_i | u_j> sobre los vectores
- Depends on: `topogpt3.c`, `topogpt3/model.py`, `topogpt3/train.py`

### synthetic_winding (function) `def synthetic_winding(K, n_windows, window_size)`
- Defined: `eval/diag_static.py:95`
- Doc: Como el checkpoint es estatico, no hay trayectoria temporal.
- Depends on: `topogpt3.c`, `topogpt3/model.py`, `topogpt3/train.py`

### static_kappa (function) `def static_kappa(K)`
- Defined: `eval/diag_static.py:144`
- Depends on: `topogpt3.c`, `topogpt3/model.py`, `topogpt3/train.py`

### context_length_diagnostic (function) `def context_length_diagnostic(model, tracker, device, lengths)`
- Defined: `eval/diag_static.py:171`
- Depends on: `topogpt3.c`, `topogpt3/model.py`, `topogpt3/train.py`

### main (function) `def main()`
- Defined: `eval/diag_static.py:248`
- Depends on: `topogpt3.c`, `topogpt3/model.py`, `topogpt3/train.py`

## eval/governor.py

### make_loop_detector (method) `def make_loop_detector(window, min_repeats)`
- Defined: `eval/governor.py:285`
- Doc: Return True if the last `window` tokens contain a sub-sequence
- Imported by: `eval/governor_smoke.py`

### make_timeout_hook (method) `def make_timeout_hook(per_token_s)`
- Defined: `eval/governor.py:314`
- Doc: Return True if the per-token wall time exceeds `per_token_s`.
- Imported by: `eval/governor_smoke.py`

### __init__ (method) `def __init__(self)`
- Defined: `eval/governor.py:56`
- Imported by: `eval/governor_smoke.py`

### put (method) `def put(self, tok)`
- Defined: `eval/governor.py:62`
- Imported by: `eval/governor_smoke.py`

### mark_done (method) `def mark_done(self)`
- Defined: `eval/governor.py:67`
- Imported by: `eval/governor_smoke.py`

### drain (method) `def drain(self)`
- Defined: `eval/governor.py:72`
- Doc: Return all tokens emitted so far, atomic snapshot.
- Imported by: `eval/governor_smoke.py`

### wait_for_new (method) `def wait_for_new(self, timeout)`
- Defined: `eval/governor.py:77`
- Doc: Block up to `timeout` seconds for a new token. Returns True
- Imported by: `eval/governor_smoke.py`

### is_closed (method) `def is_closed(self)`
- Defined: `eval/governor.py:86`
- Imported by: `eval/governor_smoke.py`

### __len__ (method) `def __len__(self)`
- Defined: `eval/governor.py:90`
- Imported by: `eval/governor_smoke.py`

### __post_init__ (method) `def __post_init__(self)`
- Defined: `eval/governor.py:117`
- Imported by: `eval/governor_smoke.py`

### __init__ (method) `def __init__(self, model, ctx, stream, max_new_tokens, temperature, top_k, repetition_penalty, max_seq_len)`
- Defined: `eval/governor.py:156`
- Imported by: `eval/governor_smoke.py`

### cancel (method) `def cancel(self)`
- Defined: `eval/governor.py:177`
- Doc: Asynchronously stop the generation. Safe to call from any
- Imported by: `eval/governor_smoke.py`

### _should_cancel (method) `def _should_cancel(self)`
- Defined: `eval/governor.py:182`
- Imported by: `eval/governor_smoke.py`

### run (method) `def run(self, stop_hooks)`
- Defined: `eval/governor.py:185`
- Doc: Execute the generation loop. Returns when the model emits
- Imported by: `eval/governor_smoke.py`

### hook (method) `def hook(generated)`
- Defined: `eval/governor.py:292`
- Imported by: `eval/governor_smoke.py`

### hook (method) `def hook(generated)`
- Defined: `eval/governor.py:320`
- Imported by: `eval/governor_smoke.py`

## eval/governor_smoke.py

### load_model (function) `def load_model()`
- Defined: `eval/governor_smoke.py:30`
- Depends on: `eval/governor.py`, `topogpt3.c`

### test_tokenstream_threadsafety (function) `def test_tokenstream_threadsafety()`
- Defined: `eval/governor_smoke.py:49`
- Depends on: `eval/governor.py`, `topogpt3.c`

### test_governor_basic (function) `def test_governor_basic()`
- Defined: `eval/governor_smoke.py:79`
- Depends on: `eval/governor.py`, `topogpt3.c`

### test_loop_detector (function) `def test_loop_detector()`
- Defined: `eval/governor_smoke.py:98`
- Depends on: `eval/governor.py`, `topogpt3.c`

### test_cancel (function) `def test_cancel()`
- Defined: `eval/governor_smoke.py:118`
- Depends on: `eval/governor.py`, `topogpt3.c`

### producer (function) `def producer()`
- Defined: `eval/governor_smoke.py:53`
- Depends on: `eval/governor.py`, `topogpt3.c`

### consumer (function) `def consumer()`
- Defined: `eval/governor_smoke.py:59`
- Depends on: `eval/governor.py`, `topogpt3.c`

## eval/harness.py

### load_humaneval (function) `def load_humaneval(cache_dir)`
- Defined: `eval/harness.py:59`
- Depends on: `eval/samplers.py`, `eval/sandbox.py`, `topogpt3.c`
- Imported by: `eval/integration_smoke.py`, `eval/noise_sweep.py`, `eval/temp_sweep.py`

### build_prompt (function) `def build_prompt(problem)`
- Defined: `eval/harness.py:75`
- Doc: Return the exact prompt text fed to the model.
- Depends on: `eval/samplers.py`, `eval/sandbox.py`, `topogpt3.c`
- Imported by: `eval/integration_smoke.py`, `eval/noise_sweep.py`, `eval/temp_sweep.py`

### extract_candidate (function) `def extract_candidate(prompt, completion)`
- Defined: `eval/harness.py:100`
- Doc: Combine prompt + completion into a single Python source string.
- Depends on: `eval/samplers.py`, `eval/sandbox.py`, `topogpt3.c`
- Imported by: `eval/integration_smoke.py`, `eval/noise_sweep.py`, `eval/temp_sweep.py`

### run_one_test (function) `def run_one_test(problem, candidate_src, timeout)`
- Defined: `eval/harness.py:150`
- Doc: Execute the candidate against the hidden test.
- Depends on: `eval/samplers.py`, `eval/sandbox.py`, `topogpt3.c`
- Imported by: `eval/integration_smoke.py`, `eval/noise_sweep.py`, `eval/temp_sweep.py`

### run_one_test_sandboxed (function) `def run_one_test_sandboxed(problem, candidate_src, timeout, sandbox_cfg)`
- Defined: `eval/harness.py:172`
- Doc: Sandboxed variant of `run_one_test`. Runs the candidate in a
- Depends on: `eval/samplers.py`, `eval/sandbox.py`, `topogpt3.c`
- Imported by: `eval/integration_smoke.py`, `eval/noise_sweep.py`, `eval/temp_sweep.py`

### make_sampler (function) `def make_sampler(mode, settings_kwargs)`
- Defined: `eval/harness.py:195`
- Doc: Backwards-compatible shim. The real implementation lives in
- Depends on: `eval/samplers.py`, `eval/sandbox.py`, `topogpt3.c`
- Imported by: `eval/integration_smoke.py`, `eval/noise_sweep.py`, `eval/temp_sweep.py`

### completion_for_problem (function) `def completion_for_problem(sampler, prompt)`
- Defined: `eval/harness.py:204`
- Doc: Run a single completion and return (raw_output_text, metrics_dict).
- Depends on: `eval/samplers.py`, `eval/sandbox.py`, `topogpt3.c`
- Imported by: `eval/integration_smoke.py`, `eval/noise_sweep.py`, `eval/temp_sweep.py`

### evaluate_problem (method) `def evaluate_problem(problem, loader, args, sample_idx)`
- Defined: `eval/harness.py:272`
- Depends on: `eval/samplers.py`, `eval/sandbox.py`, `topogpt3.c`
- Imported by: `eval/integration_smoke.py`, `eval/noise_sweep.py`, `eval/temp_sweep.py`

### main (method) `def main()`
- Defined: `eval/harness.py:315`
- Depends on: `eval/samplers.py`, `eval/sandbox.py`, `topogpt3.c`
- Imported by: `eval/integration_smoke.py`, `eval/noise_sweep.py`, `eval/temp_sweep.py`

### __init__ (method) `def __init__(self, ckpt_dir, ckpt_name, device)`
- Defined: `eval/harness.py:220`
- Depends on: `eval/samplers.py`, `eval/sandbox.py`, `topogpt3.c`
- Imported by: `eval/integration_smoke.py`, `eval/noise_sweep.py`, `eval/temp_sweep.py`

### generate (method) `def generate(self, prompt, max_new_tokens, temperature, top_k, repetition_penalty)`
- Defined: `eval/harness.py:246`
- Depends on: `eval/samplers.py`, `eval/sandbox.py`, `topogpt3.c`
- Imported by: `eval/integration_smoke.py`, `eval/noise_sweep.py`, `eval/temp_sweep.py`

## eval/integration_smoke.py

### main (function) `def main()`
- Defined: `eval/integration_smoke.py:18`
- Depends on: `eval/harness.py`

## eval/noise_analysis.py

### _load (function) `def _load(p)`
- Defined: `eval/noise_analysis.py:43`

### consistency_across_runs (function) `def consistency_across_runs(per_run)`
- Defined: `eval/noise_analysis.py:47`
- Doc: Para cada problema, mira si pasa consistentemente a traves de los

### main (function) `def main()`
- Defined: `eval/noise_analysis.py:83`

## eval/noise_sweep.py

### inject_noise (function) `def inject_noise(model, sigma, seed)`
- Defined: `eval/noise_sweep.py:46`
- Doc: Anade N(0, sigma) a TODOS los kernels espectrales (kr_*, ki_*).
- Depends on: `eval/harness.py`, `topogpt3.c`, `topogpt3/model.py`
- Imported by: `eval/temp_sweep.py`

### load_model (function) `def load_model(ckpt_dir, ckpt_name, device)`
- Defined: `eval/noise_sweep.py:74`
- Doc: Reconstruye TopoGPT2 alineado con el checkpoint, sin acceso a
- Depends on: `eval/harness.py`, `topogpt3.c`, `topogpt3/model.py`
- Imported by: `eval/temp_sweep.py`

### generate_one (function) `def generate_one(model, tok, prompt, max_new_tokens, device)`
- Defined: `eval/noise_sweep.py:99`
- Depends on: `eval/harness.py`, `topogpt3.c`, `topogpt3/model.py`
- Imported by: `eval/temp_sweep.py`

### main (function) `def main()`
- Defined: `eval/noise_sweep.py:117`
- Depends on: `eval/harness.py`, `topogpt3.c`, `topogpt3/model.py`
- Imported by: `eval/temp_sweep.py`

## eval/repair.py

### _new_loader (function) `def _new_loader(ckpt_dir, ckpt_name)`
- Defined: `eval/repair.py:36`
- Depends on: `topogpt3.c`

### extract_candidate (function) `def extract_candidate(prompt, completion)`
- Defined: `eval/repair.py:49`
- Depends on: `topogpt3.c`

### run_test (function) `def run_test(problem, candidate_src)`
- Defined: `eval/repair.py:75`
- Depends on: `topogpt3.c`

### build_repair_prompt (function) `def build_repair_prompt(prompt, candidate, err, entry_point)`
- Defined: `eval/repair.py:89`
- Depends on: `topogpt3.c`

### gen (function) `def gen(model, tok, text, max_new_tokens, temperature, top_k, rep_penalty)`
- Defined: `eval/repair.py:104`
- Depends on: `topogpt3.c`

### main (function) `def main()`
- Defined: `eval/repair.py:119`
- Depends on: `topogpt3.c`

## eval/report.py

### pass_at_k (function) `def pass_at_k(n, c, k)`
- Defined: `eval/report.py:25`

### classify_error (function) `def classify_error(msg)`
- Defined: `eval/report.py:31`

### load_jsonl (function) `def load_jsonl(p)`
- Defined: `eval/report.py:52`

### summarize_run (function) `def summarize_run(p)`
- Defined: `eval/report.py:56`

### repair_summary (function) `def repair_summary(repair_path, baseline_path)`
- Defined: `eval/report.py:90`

### main (function) `def main()`
- Defined: `eval/report.py:117`

## eval/samplers.py

### register_sampler (function) `def register_sampler(name)`
- Defined: `eval/samplers.py:36`
- Doc: Decorator. Register a factory under `name`. If `enabled_env` is set,
- Depends on: `topogpt3.c`
- Imported by: `eval/harness.py`, `eval/harness.py`

### _is_env_truthy (function) `def _is_env_truthy(name)`
- Defined: `eval/samplers.py:55`
- Depends on: `topogpt3.c`
- Imported by: `eval/harness.py`, `eval/harness.py`

### _make_standard (function) `def _make_standard(settings_kwargs)`
- Defined: `eval/samplers.py:64`
- Depends on: `topogpt3.c`
- Imported by: `eval/harness.py`, `eval/harness.py`

### _make_hrm (function) `def _make_hrm(settings_kwargs)`
- Defined: `eval/samplers.py:69`
- Depends on: `topogpt3.c`
- Imported by: `eval/harness.py`, `eval/harness.py`

### list_samplers (function) `def list_samplers()`
- Defined: `eval/samplers.py:86`
- Depends on: `topogpt3.c`
- Imported by: `eval/harness.py`, `eval/harness.py`

### build_sampler (function) `def build_sampler(mode, settings_kwargs)`
- Defined: `eval/samplers.py:90`
- Doc: Construct a sampler. Drop-in replacement for the old
- Depends on: `topogpt3.c`
- Imported by: `eval/harness.py`, `eval/harness.py`

### deco (function) `def deco(fn)`
- Defined: `eval/samplers.py:42`
- Depends on: `topogpt3.c`
- Imported by: `eval/harness.py`, `eval/harness.py`

## eval/sandbox.py

### _names_imported (method) `def _names_imported(tree)`
- Defined: `eval/sandbox.py:100`
- Doc: Return the set of top-level names brought into scope by imports.
- Imported by: `eval/harness.py`, `eval/sandbox_smoke.py`, `topogpt3/tools_agent.py`

### _blocked_dunder_access (method) `def _blocked_dunder_access(tree, blocked)`
- Defined: `eval/sandbox.py:114`
- Doc: Find Attribute nodes whose attr is in `blocked`. Returns attr names found.
- Imported by: `eval/harness.py`, `eval/sandbox_smoke.py`, `topogpt3/tools_agent.py`

### _max_depth (method) `def _max_depth(tree)`
- Defined: `eval/sandbox.py:123`
- Doc: Compute max nesting depth of the AST. Catches obfuscated huge trees.
- Imported by: `eval/harness.py`, `eval/sandbox_smoke.py`, `topogpt3/tools_agent.py`

### check_safety (method) `def check_safety(source, cfg)`
- Defined: `eval/sandbox.py:133`
- Doc: Return (ok, reason). `reason` is "" when ok, else a human-readable
- Imported by: `eval/harness.py`, `eval/sandbox_smoke.py`, `topogpt3/tools_agent.py`

### _build_worker_src (method) `def _build_worker_src(allowed_builtin_names, program_src, blocked_modules)`
- Defined: `eval/sandbox.py:254`
- Imported by: `eval/harness.py`, `eval/sandbox_smoke.py`, `topogpt3/tools_agent.py`

### safe_exec (method) `def safe_exec(program_src, cfg, extra_globals)`
- Defined: `eval/sandbox.py:270`
- Doc: Execute `program_src` in a sandboxed child process. Returns the same
- Imported by: `eval/harness.py`, `eval/sandbox_smoke.py`, `topogpt3/tools_agent.py`

### describe_policy (method) `def describe_policy(cfg)`
- Defined: `eval/sandbox.py:373`
- Imported by: `eval/harness.py`, `eval/sandbox_smoke.py`, `topogpt3/tools_agent.py`

### d (method) `def d(node, cur)`
- Defined: `eval/sandbox.py:125`
- Imported by: `eval/harness.py`, `eval/sandbox_smoke.py`, `topogpt3/tools_agent.py`

## eval/sandbox_smoke.py

### main (function) `def main()`
- Defined: `eval/sandbox_smoke.py:15`
- Depends on: `eval/sandbox.py`

## eval/smoke.py

### run_standard (function) `def run_standard()`
- Defined: `eval/smoke.py:17`
- Depends on: `topogpt3.c`

### run_hrm (function) `def run_hrm()`
- Defined: `eval/smoke.py:36`
- Depends on: `topogpt3.c`

## eval/temp_sweep.py

### generate_one (function) `def generate_one(model, tok, prompt, max_new_tokens, temperature, top_k, device, seed_offset)`
- Defined: `eval/temp_sweep.py:39`
- Depends on: `eval/harness.py`, `eval/noise_sweep.py`

### evaluate_problems (function) `def evaluate_problems(model, tok, problems, max_new_tokens, temperature, top_k, n_samples, device)`
- Defined: `eval/temp_sweep.py:58`
- Depends on: `eval/harness.py`, `eval/noise_sweep.py`

### pass_at_k_unbiased (function) `def pass_at_k_unbiased(n, c, k)`
- Defined: `eval/temp_sweep.py:88`
- Depends on: `eval/harness.py`, `eval/noise_sweep.py`

### summarize (function) `def summarize(results, n_samples)`
- Defined: `eval/temp_sweep.py:96`
- Depends on: `eval/harness.py`, `eval/noise_sweep.py`

### main (function) `def main()`
- Defined: `eval/temp_sweep.py:116`
- Depends on: `eval/harness.py`, `eval/noise_sweep.py`

## gradio_app.py

### ensure_checkpoint (function) `def ensure_checkpoint()`
- Defined: `gradio_app.py:35`
- Doc: Return the path to the checkpoint directory, downloading if needed.
- Depends on: `topogpt3.c`

### run_standard_inference (function) `def run_standard_inference(prompt, max_new_tokens, temperature, top_k, repetition_penalty, auto_continue)`
- Defined: `gradio_app.py:59`
- Doc: Run standard autoregressive inference.
- Depends on: `topogpt3.c`

### run_hrm_inference (function) `def run_hrm_inference(prompt, max_new_tokens, temperature, top_k, repetition_penalty, high_level_iters, low_level_iters, low_level_window, thinking, auto_continue)`
- Defined: `gradio_app.py:95`
- Doc: Run hierarchical recursive reasoning inference.
- Depends on: `topogpt3.c`

### build_ui (function) `def build_ui()`
- Defined: `gradio_app.py:144`
- Doc: Construct the Gradio Blocks interface.
- Depends on: `topogpt3.c`

## synthetic_dataset.py

### build_backend (method) `def build_backend(provider, model)`
- Defined: `synthetic_dataset.py:227`
- Doc: Factory for LLM backends.
- Imported by: `topogpt3/model.py`

### validate_sample (method) `def validate_sample(sample)`
- Defined: `synthetic_dataset.py:330`
- Doc: Validate that a generated sample meets quality bar.
- Imported by: `topogpt3/model.py`

### build_logger (method) `def build_logger(level)`
- Defined: `synthetic_dataset.py:614`
- Imported by: `topogpt3/model.py`

### parse_args (method) `def parse_args()`
- Defined: `synthetic_dataset.py:625`
- Imported by: `topogpt3/model.py`

### load_paths (method) `def load_paths(paths_arg, paths_file, max_files)`
- Defined: `synthetic_dataset.py:652`
- Doc: Load file paths from CLI args or file.
- Imported by: `topogpt3/model.py`

### main (method) `def main()`
- Defined: `synthetic_dataset.py:667`
- Imported by: `topogpt3/model.py`

### generate (method) `def generate(self, prompt)`
- Defined: `synthetic_dataset.py:64`
- Imported by: `topogpt3/model.py`

### name (method) `def name(self)`
- Defined: `synthetic_dataset.py:67`
- Imported by: `topogpt3/model.py`

### __init__ (method) `def __init__(self, model, api_key, max_tokens, temperature, timeout)`
- Defined: `synthetic_dataset.py:78`
- Imported by: `topogpt3/model.py`

### name (method) `def name(self)`
- Defined: `synthetic_dataset.py:95`
- Imported by: `topogpt3/model.py`

### generate (method) `def generate(self, prompt)`
- Defined: `synthetic_dataset.py:98`
- Imported by: `topogpt3/model.py`

### __init__ (method) `def __init__(self, model, api_key, max_tokens, temperature, timeout)`
- Defined: `synthetic_dataset.py:132`
- Imported by: `topogpt3/model.py`

### name (method) `def name(self)`
- Defined: `synthetic_dataset.py:151`
- Imported by: `topogpt3/model.py`

### generate (method) `def generate(self, prompt)`
- Defined: `synthetic_dataset.py:154`
- Imported by: `topogpt3/model.py`

### __init__ (method) `def __init__(self, model, host, max_tokens, temperature, timeout)`
- Defined: `synthetic_dataset.py:184`
- Imported by: `topogpt3/model.py`

### name (method) `def name(self)`
- Defined: `synthetic_dataset.py:198`
- Imported by: `topogpt3/model.py`

### generate (method) `def generate(self, prompt)`
- Defined: `synthetic_dataset.py:201`
- Imported by: `topogpt3/model.py`

### load (method) `def load(path)`
- Defined: `synthetic_dataset.py:374`
- Imported by: `topogpt3/model.py`

### save (method) `def save(self, path)`
- Defined: `synthetic_dataset.py:387`
- Imported by: `topogpt3/model.py`

### __init__ (method) `def __init__(self, backend, output_path, manifest_path, logger, max_workers, max_file_chars)`
- Defined: `synthetic_dataset.py:418`
- Imported by: `topogpt3/model.py`

### _jsonl_writer (method) `def _jsonl_writer(self)`
- Defined: `synthetic_dataset.py:447`
- Doc: Background thread that drains the queue and writes JSONL lines.
- Imported by: `topogpt3/model.py`

### _enqueue_sample (method) `def _enqueue_sample(self, sample)`
- Defined: `synthetic_dataset.py:465`
- Imported by: `topogpt3/model.py`

### _flush_writer (method) `def _flush_writer(self)`
- Defined: `synthetic_dataset.py:468`
- Imported by: `topogpt3/model.py`

### _read_file (method) `def _read_file(self, path)`
- Defined: `synthetic_dataset.py:477`
- Doc: Read file content and detect language. Truncate if needed.
- Imported by: `topogpt3/model.py`

### _build_prompt (method) `def _build_prompt(self, content, lang)`
- Defined: `synthetic_dataset.py:490`
- Imported by: `topogpt3/model.py`

### _generate_sample (method) `def _generate_sample(self, content, lang)`
- Defined: `synthetic_dataset.py:496`
- Doc: Call LLM with retry logic.
- Imported by: `topogpt3/model.py`

### process_file (method) `def process_file(self, path)`
- Defined: `synthetic_dataset.py:533`
- Doc: Process a single file. Returns True if a sample was written.
- Imported by: `topogpt3/model.py`

### process_batch (method) `def process_batch(self, paths)`
- Defined: `synthetic_dataset.py:568`
- Doc: Process a batch of files in parallel using thread pool.
- Imported by: `topogpt3/model.py`

### finish (method) `def finish(self)`
- Defined: `synthetic_dataset.py:590`
- Doc: Signal end of processing and flush writer.
- Imported by: `topogpt3/model.py`

## tests/test_heritage.py

### _micro (function) `def _micro()`
- Defined: `tests/test_heritage.py:18`
- Depends on: `topogpt3/chat.py`, `topogpt3/eval_toolcall.py`, `topogpt3/lora.py`, `topogpt3/model.py`, `topogpt3/rewards.py`, `topogpt3/rollout.py`, `topogpt3/tools_agent.py`, `topogpt3/yarn.py`

### test_chat_template_tools_think (function) `def test_chat_template_tools_think()`
- Defined: `tests/test_heritage.py:24`
- Depends on: `topogpt3/chat.py`, `topogpt3/eval_toolcall.py`, `topogpt3/lora.py`, `topogpt3/model.py`, `topogpt3/rewards.py`, `topogpt3/rollout.py`, `topogpt3/tools_agent.py`, `topogpt3/yarn.py`

### test_yarn_changes_freqs_only (function) `def test_yarn_changes_freqs_only()`
- Defined: `tests/test_heritage.py:37`
- Depends on: `topogpt3/chat.py`, `topogpt3/eval_toolcall.py`, `topogpt3/lora.py`, `topogpt3/model.py`, `topogpt3/rewards.py`, `topogpt3/rollout.py`, `topogpt3/tools_agent.py`, `topogpt3/yarn.py`

### test_lora_zero_init_and_quaternion_targets (function) `def test_lora_zero_init_and_quaternion_targets()`
- Defined: `tests/test_heritage.py:47`
- Depends on: `topogpt3/chat.py`, `topogpt3/eval_toolcall.py`, `topogpt3/lora.py`, `topogpt3/model.py`, `topogpt3/rewards.py`, `topogpt3/rollout.py`, `topogpt3/tools_agent.py`, `topogpt3/yarn.py`

### test_lora_save_load (function) `def test_lora_save_load(tmp_path)`
- Defined: `tests/test_heritage.py:64`
- Depends on: `topogpt3/chat.py`, `topogpt3/eval_toolcall.py`, `topogpt3/lora.py`, `topogpt3/model.py`, `topogpt3/rewards.py`, `topogpt3/rollout.py`, `topogpt3/tools_agent.py`, `topogpt3/yarn.py`

### test_dpo_grpo_losses_finite (function) `def test_dpo_grpo_losses_finite()`
- Defined: `tests/test_heritage.py:76`
- Depends on: `topogpt3/chat.py`, `topogpt3/eval_toolcall.py`, `topogpt3/lora.py`, `topogpt3/model.py`, `topogpt3/rewards.py`, `topogpt3/rollout.py`, `topogpt3/tools_agent.py`, `topogpt3/yarn.py`

### test_distill_loss_finite (function) `def test_distill_loss_finite()`
- Defined: `tests/test_heritage.py:96`
- Depends on: `topogpt3/chat.py`, `topogpt3/eval_toolcall.py`, `topogpt3/lora.py`, `topogpt3/model.py`, `topogpt3/rewards.py`, `topogpt3/rollout.py`, `topogpt3/tools_agent.py`, `topogpt3/yarn.py`

### test_rollout_engine_micro (function) `def test_rollout_engine_micro()`
- Defined: `tests/test_heritage.py:106`
- Depends on: `topogpt3/chat.py`, `topogpt3/eval_toolcall.py`, `topogpt3/lora.py`, `topogpt3/model.py`, `topogpt3/rewards.py`, `topogpt3/rollout.py`, `topogpt3/tools_agent.py`, `topogpt3/yarn.py`

### test_tools_and_eval (function) `def test_tools_and_eval()`
- Defined: `tests/test_heritage.py:123`
- Depends on: `topogpt3/chat.py`, `topogpt3/eval_toolcall.py`, `topogpt3/lora.py`, `topogpt3/model.py`, `topogpt3/rewards.py`, `topogpt3/rollout.py`, `topogpt3/tools_agent.py`, `topogpt3/yarn.py`

## tests/test_jlens.py

### test_basic_mask (method) `def test_basic_mask(self)`
- Defined: `tests/test_jlens.py:20`
- Doc: Scenario: Correct mask for a standard-length prompt.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_too_short_raises (method) `def test_too_short_raises(self)`
- Defined: `tests/test_jlens.py:29`
- Doc: Scenario: Too-short prompt raises ValueError.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_negative_skip_raises (method) `def test_negative_skip_raises(self)`
- Defined: `tests/test_jlens.py:34`
- Doc: Scenario: Negative skip_first raises ValueError.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_all_positions_valid (method) `def test_all_positions_valid(self)`
- Defined: `tests/test_jlens.py:39`
- Doc: Scenario: skip_first=0 includes all but final position.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_exact_minimum_length (method) `def test_exact_minimum_length(self)`
- Defined: `tests/test_jlens.py:45`
- Doc: Scenario: Exact minimum length (skip_first + 2) works.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### model (method) `def model(self)`
- Defined: `tests/test_jlens.py:56`
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_returns_jacobians_for_source_layers (method) `def test_returns_jacobians_for_source_layers(self, model)`
- Defined: `tests/test_jlens.py:63`
- Doc: Scenario: Returns Jacobians for all requested source layers.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_late_layer_jacobian_close_to_identity (method) `def test_late_layer_jacobian_close_to_identity(self, model)`
- Defined: `tests/test_jlens.py:76`
- Doc: Scenario: J_{n_layers-2} has diag ~= 1 (identity property).
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_earlier_layers_further_from_identity (method) `def test_earlier_layers_further_from_identity(self, model)`
- Defined: `tests/test_jlens.py:85`
- Doc: Scenario: Earlier layers compound deviations from identity.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_exact_jacobian_for_last_block (method) `def test_exact_jacobian_for_last_block(self, model)`
- Defined: `tests/test_jlens.py:95`
- Doc: Scenario: J_{n_layers-2} equals I + W_{last} exactly.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_negative_layer_indices (method) `def test_negative_layer_indices(self, model)`
- Defined: `tests/test_jlens.py:110`
- Doc: Scenario: Negative layer indices are normalized correctly.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_out_of_range_layers_rejected (method) `def test_out_of_range_layers_rejected(self, model)`
- Defined: `tests/test_jlens.py:133`
- Doc: Scenario: Out-of-range layers raise ValueError.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_source_below_target_enforced (method) `def test_source_below_target_enforced(self, model)`
- Defined: `tests/test_jlens.py:145`
- Doc: Scenario: source_layers must be below target_layer.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_target_out_of_range_raises (method) `def test_target_out_of_range_raises(self, model)`
- Defined: `tests/test_jlens.py:158`
- Doc: Scenario: target_layer out of range raises ValueError.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### model (method) `def model(self)`
- Defined: `tests/test_jlens.py:176`
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_fit_returns_lens_with_correct_attributes (method) `def test_fit_returns_lens_with_correct_attributes(self, model)`
- Defined: `tests/test_jlens.py:183`
- Doc: Scenario: fit() returns JacobianLens with correct metadata.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_fit_empty_prompts_raises (method) `def test_fit_empty_prompts_raises(self, model)`
- Defined: `tests/test_jlens.py:191`
- Doc: Scenario: No valid prompts raises ValueError.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_fit_skips_short_prompts (method) `def test_fit_skips_short_prompts(self, model)`
- Defined: `tests/test_jlens.py:196`
- Doc: Scenario: Too-short prompts are skipped.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_fit_with_default_source_layers (method) `def test_fit_with_default_source_layers(self, model)`
- Defined: `tests/test_jlens.py:202`
- Doc: Scenario: Default source_layers covers all layers below target.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### model (method) `def model(self)`
- Defined: `tests/test_jlens.py:214`
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### fitted_lens (method) `def fitted_lens(self, model)`
- Defined: `tests/test_jlens.py:222`
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_save_and_load_round_trip (method) `def test_save_and_load_round_trip(self, fitted_lens, tmp_path)`
- Defined: `tests/test_jlens.py:226`
- Doc: Scenario: save/load preserves jacobians (fp16 tolerance).
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_apply_returns_correct_shapes (method) `def test_apply_returns_correct_shapes(self, fitted_lens, model)`
- Defined: `tests/test_jlens.py:242`
- Doc: Scenario: apply() returns correct logit shapes.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_fitted_late_layer_matches_model (method) `def test_fitted_late_layer_matches_model(self, fitted_lens, model)`
- Defined: `tests/test_jlens.py:254`
- Doc: Scenario: Transported late-layer logits match model logits.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_apply_with_explicit_positions (method) `def test_apply_with_explicit_positions(self, fitted_lens, model)`
- Defined: `tests/test_jlens.py:263`
- Doc: Scenario: Explicit positions return correct subset.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_logit_lens_baseline (method) `def test_logit_lens_baseline(self, fitted_lens, model)`
- Defined: `tests/test_jlens.py:274`
- Doc: Scenario: use_jacobian=False returns untransported logits.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_unfitted_layer_rejected (method) `def test_unfitted_layer_rejected(self, fitted_lens, model)`
- Defined: `tests/test_jlens.py:281`
- Doc: Scenario: Unfitted layer raises ValueError.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_out_of_range_layer_rejected (method) `def test_out_of_range_layer_rejected(self, fitted_lens, model)`
- Defined: `tests/test_jlens.py:286`
- Doc: Scenario: Out-of-range layer raises ValueError.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_merge_weighted_mean (method) `def test_merge_weighted_mean(self)`
- Defined: `tests/test_jlens.py:291`
- Doc: Scenario: merge() computes n_prompts-weighted mean.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_merge_mismatch_raises (method) `def test_merge_mismatch_raises(self)`
- Defined: `tests/test_jlens.py:319`
- Doc: Scenario: Mismatched lenses raise ValueError.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_merge_empty_raises (method) `def test_merge_empty_raises(self)`
- Defined: `tests/test_jlens.py:326`
- Doc: Scenario: Empty merge raises ValueError.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_transport_produces_correct_shape (method) `def test_transport_produces_correct_shape(self, fitted_lens)`
- Defined: `tests/test_jlens.py:331`
- Doc: Scenario: transport() maps residual to final-layer basis.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_load_invalid_file_raises (method) `def test_load_invalid_file_raises(self, tmp_path)`
- Defined: `tests/test_jlens.py:337`
- Doc: Scenario: Loading non-lens file raises ValueError.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_from_pretrained_local_file (method) `def test_from_pretrained_local_file(self, fitted_lens, tmp_path)`
- Defined: `tests/test_jlens.py:344`
- Doc: Scenario: from_pretrained resolves a local file.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_from_pretrained_local_directory (method) `def test_from_pretrained_local_directory(self, fitted_lens, tmp_path)`
- Defined: `tests/test_jlens.py:351`
- Doc: Scenario: from_pretrained resolves a local directory.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_repr (method) `def test_repr(self, fitted_lens)`
- Defined: `tests/test_jlens.py:359`
- Doc: Scenario: repr contains key metadata.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### model (method) `def model(self)`
- Defined: `tests/test_jlens.py:371`
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_checkpoint_resume_produces_same_result (method) `def test_checkpoint_resume_produces_same_result(self, model, tmp_path)`
- Defined: `tests/test_jlens.py:378`
- Doc: Scenario: Resumed fit matches fresh fit.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_resume_after_skip_no_double_count (method) `def test_resume_after_skip_no_double_count(self, model, tmp_path)`
- Defined: `tests/test_jlens.py:408`
- Doc: Scenario: Resume after a skipped prompt does not double-count.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_checkpoint_mismatch_raises (method) `def test_checkpoint_mismatch_raises(self, model, tmp_path)`
- Defined: `tests/test_jlens.py:450`
- Doc: Scenario: Mismatched checkpoint settings raise ValueError.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_fit_config_defaults (method) `def test_fit_config_defaults(self)`
- Defined: `tests/test_jlens.py:476`
- Doc: Scenario: Default fit config has sensible defaults.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_app_config_defaults (method) `def test_app_config_defaults(self)`
- Defined: `tests/test_jlens.py:485`
- Doc: Scenario: Default app config has sensible defaults.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_default_config (method) `def test_default_config(self)`
- Defined: `tests/test_jlens.py:497`
- Doc: Scenario: Default app config uses all positions.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_custom_config (method) `def test_custom_config(self)`
- Defined: `tests/test_jlens.py:505`
- Doc: Scenario: Custom app config overrides specific layers.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

## tests/test_lens_model.py

### test_default_config (method) `def test_default_config(self)`
- Defined: `tests/test_lens_model.py:16`
- Doc: Scenario: Default config matches small scale preset.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`, `topogpt3/model.py`

### test_from_topogpt2_config (method) `def test_from_topogpt2_config(self)`
- Defined: `tests/test_lens_model.py:25`
- Doc: Scenario: Build lens config from TopoGPT2Config.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`, `topogpt3/model.py`

### test_probe_checkpoint_missing_raises (method) `def test_probe_checkpoint_missing_raises(self, tmp_path)`
- Defined: `tests/test_lens_model.py:35`
- Doc: Scenario: Missing state.json raises FileNotFoundError.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`, `topogpt3/model.py`

### test_default_parameters (method) `def test_default_parameters(self)`
- Defined: `tests/test_lens_model.py:44`
- Doc: Scenario: TinyDecoder has correct default shape.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`, `topogpt3/model.py`

### test_forward_output_shape (method) `def test_forward_output_shape(self)`
- Defined: `tests/test_lens_model.py:51`
- Doc: Scenario: Forward pass produces correct logit shape.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`, `topogpt3/model.py`

### test_weight_tied (method) `def test_weight_tied(self)`
- Defined: `tests/test_lens_model.py:59`
- Doc: Scenario: Embedding and LM head share weights.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`, `topogpt3/model.py`

### raw_model (method) `def raw_model(self)`
- Defined: `tests/test_lens_model.py:69`
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`, `topogpt3/model.py`

### lens_model (method) `def lens_model(self, raw_model)`
- Defined: `tests/test_lens_model.py:77`
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`, `topogpt3/model.py`

### test_exposes_protocol_attributes (method) `def test_exposes_protocol_attributes(self, lens_model, raw_model)`
- Defined: `tests/test_lens_model.py:80`
- Doc: Scenario: LensModel attributes match underlying model.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`, `topogpt3/model.py`

### test_encode_text_to_token_ids (method) `def test_encode_text_to_token_ids(self, lens_model)`
- Defined: `tests/test_lens_model.py:87`
- Doc: Scenario: encode() returns tensor of shape [1, seq_len].
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`, `topogpt3/model.py`

### test_encode_with_tokenizer (method) `def test_encode_with_tokenizer(self)`
- Defined: `tests/test_lens_model.py:95`
- Doc: Scenario: encode() uses BPETokenizer when available.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`, `topogpt3/model.py`

### test_encode_respects_max_length (method) `def test_encode_respects_max_length(self, lens_model)`
- Defined: `tests/test_lens_model.py:107`
- Doc: Scenario: encode() truncates at max_length.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`, `topogpt3/model.py`

### test_forward_returns_residual_only (method) `def test_forward_returns_residual_only(self)`
- Defined: `tests/test_lens_model.py:113`
- Doc: Scenario: forward() returns hidden states with d_model dim, not vocab.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`, `topogpt3/model.py`

### test_forward_differs_from_full_model (method) `def test_forward_differs_from_full_model(self)`
- Defined: `tests/test_lens_model.py:128`
- Doc: Scenario: Residual forward shape differs from full model logits.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`, `topogpt3/model.py`

### test_unembed_produces_logits (method) `def test_unembed_produces_logits(self, lens_model)`
- Defined: `tests/test_lens_model.py:141`
- Doc: Scenario: unembed() maps residual to logits.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`, `topogpt3/model.py`

### test_forward_plus_unembed_matches_model_logits (method) `def test_forward_plus_unembed_matches_model_logits(self, lens_model, raw_model)`
- Defined: `tests/test_lens_model.py:150`
- Doc: Scenario: residual forward + unembed == model forward logits.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`, `topogpt3/model.py`

### test_autograd_graph_tracks_through_layers (method) `def test_autograd_graph_tracks_through_layers(self)`
- Defined: `tests/test_lens_model.py:163`
- Doc: Scenario: Gradient flows through residual layers when grads enabled.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`, `topogpt3/model.py`

### test_input_device_property (method) `def test_input_device_property(self, lens_model)`
- Defined: `tests/test_lens_model.py:180`
- Doc: Scenario: input_device returns the embedding weight device.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`, `topogpt3/model.py`

### test_input_device_setter (method) `def test_input_device_setter(self, lens_model)`
- Defined: `tests/test_lens_model.py:185`
- Doc: Scenario: input_device can be overridden.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`, `topogpt3/model.py`

### test_tokenizer_setter (method) `def test_tokenizer_setter(self, lens_model)`
- Defined: `tests/test_lens_model.py:191`
- Doc: Scenario: tokenizer can be set after construction.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`, `topogpt3/model.py`

### test_from_checkpoint_missing_raises (method) `def test_from_checkpoint_missing_raises(self)`
- Defined: `tests/test_lens_model.py:198`
- Doc: Scenario: from_checkpoint with missing directory raises.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`, `topogpt3/model.py`

### test_grad_enabled_deterministic (method) `def test_grad_enabled_deterministic(self, lens_model)`
- Defined: `tests/test_lens_model.py:205`
- Doc: Scenario: Multiple forward passes with same input are deterministic.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`, `topogpt3/model.py`

### lens_model (method) `def lens_model(self)`
- Defined: `tests/test_lens_model.py:218`
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`, `topogpt3/model.py`

### test_recorder_captures_layer_outputs (method) `def test_recorder_captures_layer_outputs(self, lens_model)`
- Defined: `tests/test_lens_model.py:225`
- Doc: Scenario: ActivationRecorder captures all requested layer outputs.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`, `topogpt3/model.py`

### test_recorder_with_start_graph_at (method) `def test_recorder_with_start_graph_at(self, lens_model)`
- Defined: `tests/test_lens_model.py:238`
- Doc: Scenario: start_graph_at roots the autograd graph.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`, `topogpt3/model.py`

### test_recorder_cleanup_on_exception (method) `def test_recorder_cleanup_on_exception(self, lens_model)`
- Defined: `tests/test_lens_model.py:252`
- Doc: Scenario: Hooks are removed even if construction fails.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`, `topogpt3/model.py`

### test_recorder_detach_after_forward (method) `def test_recorder_detach_after_forward(self, lens_model)`
- Defined: `tests/test_lens_model.py:264`
- Doc: Scenario: Activations can be detached after recorder exits.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`, `topogpt3/model.py`

### test_empty_sequence (method) `def test_empty_sequence(self)`
- Defined: `tests/test_lens_model.py:281`
- Doc: Scenario: Empty input produces error or minimal output.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`, `topogpt3/model.py`

### test_single_token (method) `def test_single_token(self)`
- Defined: `tests/test_lens_model.py:291`
- Doc: Scenario: Single token input works.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`, `topogpt3/model.py`

## topogpt3.c

### tg_exp (function) `static float tg_exp(float x)`
- Defined: `topogpt3.c:113`
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### tg_tanh (function) `static float tg_tanh(float x)`
- Defined: `topogpt3.c:127`
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### tg_sin (function) `static float tg_sin(float x)`
- Defined: `topogpt3.c:134`
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### tg_cos (function) `static float tg_cos(float x)`
- Defined: `topogpt3.c:143`
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### tg_fabs (function) `static float tg_fabs(float x)`
- Defined: `topogpt3.c:147`
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### tg_log (function) `static float tg_log(float x)`
- Defined: `topogpt3.c:151`
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### tg_fmax (function) `static float tg_fmax(float a, float b)`
- Defined: `topogpt3.c:163`
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### tg_fmin (function) `static float tg_fmin(float a, float b)`
- Defined: `topogpt3.c:167`
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### load_vocab (function) `static void load_vocab(const char *path)`
- Defined: `topogpt3.c:254`
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### build_torus_graph (function) `static void build_torus_graph(void)`
- Defined: `topogpt3.c:295`
- Doc: ====================================================================== SECTION 4: TORUS GRAPH BUILDER * ================
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### precompute_rope (function) `static void precompute_rope(void)`
- Defined: `topogpt3.c:326`
- Doc: ====================================================================== SECTION 5: ROPE PRECOMPUTATION * ================
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### matvec (function) `static void matvec(const float *W, const float *x, float *y, int rows, int cols)`
- Defined: `topogpt3.c:358`
- Doc: ====================================================================== SECTION 6: MATRIX OPERATIONS * ==================
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### matvec_bias (function) `static void matvec_bias(const float *W, const float *b, const float *x, float *y,
               ...`
- Defined: `topogpt3.c:369`
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### rmsnorm (function) `static void rmsnorm(const float *x, const float *w, float *y, int d)`
- Defined: `topogpt3.c:381`
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### softmax (function) `static void softmax(float *x, int n)`
- Defined: `topogpt3.c:390`
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### gelu (function) `static void gelu(float *x, int n)`
- Defined: `topogpt3.c:399`
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### silu (function) `static void silu(float *x, int n)`
- Defined: `topogpt3.c:409`
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### swiglu (function) `static void swiglu(const float *gate_w, const float *up_w, const float *down_w,
                 ...`
- Defined: `topogpt3.c:417`
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### quat_normalize (function) `static void quat_normalize(float *q)`
- Defined: `topogpt3.c:434`
- Doc: ====================================================================== SECTION 7: QUATERNION OPERATIONS * ==============
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### quat_hamilton (function) `static void quat_hamilton(const float *a, const float *b, float *c)`
- Defined: `topogpt3.c:439`
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### quat_linear (function) `static void quat_linear(const float *Ww, const float *Wx, const float *Wy, const float *Wz,
     ...`
- Defined: `topogpt3.c:448`
- Doc: static void quat_normalize(float *q) { float n = tg_sqrt(q[0]*q[0] + q[1]*q[1] + q[2]*q[2] + q[3]*q[3]); if (n > 1e-8f) 
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### ifft_radix2 (function) `static void ifft_radix2(float *real, float *imag, int n)`
- Defined: `topogpt3.c:504`
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### rfft (function) `static void rfft(const float *x, float *Xr, float *Xi, int n)`
- Defined: `topogpt3.c:513`
- Doc: cur_r = nr; } } } } static void ifft_radix2(float *real, float *imag, int n) { int i; for (i = 0; i < n; i++) imag[i] = 
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### irfft (function) `static void irfft(const float *Xr, const float *Xi, float *x, int n)`
- Defined: `topogpt3.c:522`
- Doc: fft_radix2(real, imag, n); for (i = 0; i < n; i++) { real[i] /= (float)n; imag[i] = -imag[i] / (float)n; } } /* Real FFT
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### filter1d (function) `static void filter1d(const float *x, const float *kr, const float *ki,
                      floa...`
- Defined: `topogpt3.c:536`
- Doc: ====================================================================== SECTION 9: SPECTRAL 1D FILTER * =================
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### ifft2d (function) `static void ifft2d(float *data_r, float *data_i, int h, int w)`
- Defined: `topogpt3.c:579`
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### rfft2d_real (function) `static void rfft2d_real(const float *data, float *out_r, float *out_i,
                         i...`
- Defined: `topogpt3.c:602`
- Doc: ifft_radix2(row_re, row_im, w); for (c = 0; c < w; c++) { re[r*w+c] = row_re[c]; im[r*w+c] = row_im[c]; } } /* IFFT colu
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### irfft2d (function) `static void irfft2d(const float *in_r, const float *in_i, float *out,
                     int h,...`
- Defined: `topogpt3.c:629`
- Doc: for (r = 0; r < h; r++) { col_re[r] = re[r*w+c]; col_im[r] = im[r*w+c]; } fft_radix2(col_re, col_im, h); for (r = 0; r <
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### cmul (function) `static void cmul(float ar, float ai, float cr, float di, float *rr, float *ri)`
- Defined: `topogpt3.c:664`
- Doc: ====================================================================== SECTION 11: QUATERNION SPECTRAL LAYER 2D * ======
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### spectral_contract (function) `static void spectral_contract(const float *Wr, const float *Wi,
                               co...`
- Defined: `topogpt3.c:670`
- Doc: ====================================================================== SECTION 11: QUATERNION SPECTRAL LAYER 2D * ======
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### quat_spectral_layer_2d (function) `static void quat_spectral_layer_2d(
    const float *x, float *y,
    const float *kr_w, const fl...`
- Defined: `topogpt3.c:694`
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### spectral_ae_encode (function) `static void spectral_ae_encode(const float *x, float *z, const LayerWeights *lw)`
- Defined: `topogpt3.c:784`
- Doc: ====================================================================== SECTION 12: SPECTRAL AUTOENCODER FORWARD * ======
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### spectral_ae_decode (function) `static void spectral_ae_decode(const float *z, float *x, const LayerWeights *lw)`
- Defined: `topogpt3.c:792`
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### process_torus_grid (function) `static void process_torus_grid(const float *grid, float *out, const LayerWeights *lw)`
- Defined: `topogpt3.c:799`
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### torus_soft_assign (function) `static void torus_soft_assign(const float *phi1, const float *phi2,
                             ...`
- Defined: `topogpt3.c:820`
- Doc: ====================================================================== SECTION 13: TORUS BRAIN FORWARD * ===============
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### message_passing (function) `static void message_passing(const float *node_feat, float *out,
                             cons...`
- Defined: `topogpt3.c:842`
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### torus_brain_forward (function) `static void torus_brain_forward(const float *x, float *out, float *recon_loss,
                  ...`
- Defined: `topogpt3.c:887`
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### attention_forward (function) `static void attention_forward(const float *x, float *out, int layer_idx, int pos, int total_kv_co...`
- Defined: `topogpt3.c:977`
- Doc: ====================================================================== SECTION 14: ATTENTION FORWARD * =================
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### moe_forward (function) `static void moe_forward(const float *x, float *out, const LayerWeights *lw)`
- Defined: `topogpt3.c:1077`
- Doc: ====================================================================== SECTION 15: MoE ROUTING * =======================
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### forward (function) `static void forward(const int *token_ids, int seq_len, float *logits_out)`
- Defined: `topogpt3.c:1127`
- Doc: ====================================================================== SECTION 16: FULL MODEL FORWARD  Processes tokens 
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### tokenize_string (function) `static int tokenize_string(const char *text, int *tokens, int max_tokens)`
- Defined: `topogpt3.c:1194`
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### apply_temperature (function) `static void apply_temperature(float *logits, int n, float temp)`
- Defined: `topogpt3.c:1209`
- Doc: ====================================================================== SECTION 18: SAMPLING * ==========================
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### apply_repetition_penalty (function) `static void apply_repetition_penalty(float *logits, int n, const int *tokens,
                   ...`
- Defined: `topogpt3.c:1215`
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### apply_top_k (function) `static void apply_top_k(float *logits, int n, int k)`
- Defined: `topogpt3.c:1228`
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### sample (function) `static int sample(const float *logits, int n)`
- Defined: `topogpt3.c:1247`
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### load_weights (function) `static int load_weights(const char *path)`
- Defined: `topogpt3.c:1281`
- Doc: ====================================================================== SECTION 19: WEIGHT LOADER  Reads the binary file 
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### load_weights_fp16 (function) `static int load_weights_fp16(const char *path)`
- Defined: `topogpt3.c:1451`
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### load_weights_auto (function) `static int load_weights_auto(const char *path)`
- Defined: `topogpt3.c:1583`
- Doc: printf("  Layer %d loaded\n", i); } READ_TENSOR16(W.final_norm, D_MODEL); #undef SKIP_TENSOR16 #undef READ_TENSOR16 fclo
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### time_now_ms (function) `static double time_now_ms(void)`
- Defined: `topogpt3.c:1600`
- Doc: ====================================================================== SECTION 20: TIMING * ============================
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### decode_token (function) `static void decode_token(int tid)`
- Defined: `topogpt3.c:1613`
- Doc: ====================================================================== SECTION 21: GENERATION * ========================
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### load_token_file (function) `static int load_token_file(const char *path, int *out_ids, int max_ids)`
- Defined: `topogpt3.c:1629`
- Doc: if (tid < 256) { /* Map GPT-2 byte-level encoding back to original byte int n = tid; if (n < 94) n += 33; else if (n < 1
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### decode_token_tiktoken (function) `static void decode_token_tiktoken(int tid)`
- Defined: `topogpt3.c:1652`
- Doc: if (fread(&n, 4, 1, f) != 1) { fclose(f); return 0; } if (n > (unsigned)max_ids) n = max_ids; int count = (int)n; int i;
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### generate_tokens (function) `static void generate_tokens(int *prompt_tokens, int n_prompt, int max_new_tokens,
               ...`
- Defined: `topogpt3.c:1660`
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### generate (function) `static void generate(const char *prompt, int max_new_tokens, float temperature,
                 ...`
- Defined: `topogpt3.c:1724`
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### interactive_mode (function) `static void interactive_mode(void)`
- Defined: `topogpt3.c:1735`
- Doc: ====================================================================== SECTION 22: INTERACTIVE MODE * ==================
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### print_help (function) `static void print_help(void)`
- Defined: `topogpt3.c:1849`
- Doc: ====================================================================== SECTION 23: HELP AND MAIN * =====================
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### main (function) `int main(int argc, char **argv)`
- Defined: `topogpt3.c:1884`
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### printf (function) `extern int printf(const char *, ...);`
- Defined: `topogpt3.c:28`
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### fprintf (function) `extern int fprintf(FILE *, const char *, ...);`
- Defined: `topogpt3.c:29`
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### sprintf (function) `extern int sprintf(char *, const char *, ...);`
- Defined: `topogpt3.c:30`
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### snprintf (function) `extern int snprintf(char *, unsigned long, const char *, ...);`
- Defined: `topogpt3.c:31`
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### puts (function) `extern int puts(const char *);`
- Defined: `topogpt3.c:32`
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### putchar (function) `extern int putchar(int);`
- Defined: `topogpt3.c:33`
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### fputc (function) `extern int fputc(int, FILE *);`
- Defined: `topogpt3.c:34`
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### fputs (function) `extern int fputs(const char *, FILE *);`
- Defined: `topogpt3.c:35`
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### fopen (function) `extern FILE *fopen(const char *, const char *);`
- Defined: `topogpt3.c:36`
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### fclose (function) `extern int fclose(FILE *);`
- Defined: `topogpt3.c:37`
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### fread (function) `extern unsigned long fread(void *, unsigned long, unsigned long, FILE *);`
- Defined: `topogpt3.c:38`
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### fwrite (function) `extern unsigned long fwrite(const void *, unsigned long, unsigned long, FILE *);`
- Defined: `topogpt3.c:39`
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### fseek (function) `extern int fseek(FILE *, long, int);`
- Defined: `topogpt3.c:40`
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### ftell (function) `extern long ftell(FILE *);`
- Defined: `topogpt3.c:41`
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### fflush (function) `extern int fflush(FILE *);`
- Defined: `topogpt3.c:42`
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### malloc (function) `extern void *malloc(unsigned long);`
- Defined: `topogpt3.c:47`
- Doc: define NULL ((void*)0) define SEEK_SET 0 define SEEK_CUR 1 define SEEK_END 2
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### free (function) `extern void free(void *);`
- Defined: `topogpt3.c:48`
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### memcpy (function) `extern void *memcpy(void *, const void *, unsigned long);`
- Defined: `topogpt3.c:49`
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### memset (function) `extern void *memset(void *, int, unsigned long);`
- Defined: `topogpt3.c:50`
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### strcmp (function) `extern int strcmp(const char *, const char *);`
- Defined: `topogpt3.c:51`
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### strncmp (function) `extern int strncmp(const char *, const char *, unsigned long);`
- Defined: `topogpt3.c:52`
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### strlen (function) `extern unsigned long strlen(const char *);`
- Defined: `topogpt3.c:53`
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### strstr (function) `extern char *strstr(const char *, const char *);`
- Defined: `topogpt3.c:54`
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### fft_radix2 (function) `fft_radix2(real, imag, n);`
- Defined: `topogpt3.c:508`
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### READ_TENSOR (function) `READ_TENSOR(W.token_embed, VOCAB_SIZE * D_MODEL);`
- Defined: `topogpt3.c:1326`
- Doc: if (fread(&nl, 4, 1, f) != 1) { fclose(f); return -1; } \ if (fseek(f, nl, SEEK_CUR) != 0) { fclose(f); return -1; } \ i
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### READ_TENSOR16 (function) `READ_TENSOR16(W.token_embed, VOCAB_SIZE * D_MODEL);`
- Defined: `topogpt3.c:1501`
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

### volatile (function) `__asm__ volatile ("rdtsc" : "=a"(lo), "=d"(hi));`
- Defined: `topogpt3.c:1605`
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`

## topogpt3/__main__.py

### main (function) `def main()`
- Defined: `topogpt3/__main__.py:6`
- Doc: TopoGPT3 entry point. Delegates to subcommands.
- Depends on: `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/inference.py`, `topogpt3/inference_hrm.py`, `topogpt3/jlens.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

## topogpt3/api_server.py

### _setup_logging (function) `def _setup_logging(verbose)`
- Defined: `topogpt3/api_server.py:116`
- Depends on: `topogpt3/chat.py`, `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### _parse_keys (method) `def _parse_keys(raw)`
- Defined: `topogpt3/api_server.py:164`
- Doc: Accept ``key1,admin:key2,key3``. The ``admin:`` prefix marks an
- Depends on: `topogpt3/chat.py`, `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### _sha256 (method) `def _sha256(raw)`
- Defined: `topogpt3/api_server.py:192`
- Depends on: `topogpt3/chat.py`, `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### _sanitize_stop (method) `def _sanitize_stop(stop)`
- Defined: `topogpt3/api_server.py:281`
- Depends on: `topogpt3/chat.py`, `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### _resolve_device (method) `def _resolve_device(device)`
- Defined: `topogpt3/api_server.py:502`
- Depends on: `topogpt3/chat.py`, `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### _probe_n_kv (method) `def _probe_n_kv(checkpoint_dir)`
- Defined: `topogpt3/api_server.py:508`
- Depends on: `topogpt3/chat.py`, `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### load_model (method) `def load_model(checkpoint, device)`
- Defined: `topogpt3/api_server.py:516`
- Depends on: `topogpt3/chat.py`, `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### lifespan (method) `def lifespan(app)`
- Defined: `topogpt3/api_server.py:537`
- Depends on: `topogpt3/chat.py`, `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### _security_middleware (method) `def _security_middleware(request, call_next)`
- Defined: `topogpt3/api_server.py:577`
- Doc: Global middleware: rate-limit, IP-ban, security headers, audit log.
- Depends on: `topogpt3/chat.py`, `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### _real_ip (method) `def _real_ip(request)`
- Defined: `topogpt3/api_server.py:605`
- Doc: Best-effort real client IP. We trust no proxy headers by default.
- Depends on: `topogpt3/chat.py`, `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### _json_error (method) `def _json_error(status, detail)`
- Defined: `topogpt3/api_server.py:616`
- Depends on: `topogpt3/chat.py`, `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### _authenticate (method) `def _authenticate(request)`
- Defined: `topogpt3/api_server.py:628`
- Doc: FastAPI dependency: extract & validate Bearer token.
- Depends on: `topogpt3/chat.py`, `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### _check_rate_limit (method) `def _check_rate_limit(api_key, request)`
- Defined: `topogpt3/api_server.py:646`
- Doc: Rate limit per-key (with admin exemption / higher limit).
- Depends on: `topogpt3/chat.py`, `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### health (method) `def health(request)`
- Defined: `topogpt3/api_server.py:664`
- Depends on: `topogpt3/chat.py`, `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### list_models (method) `def list_models(request)`
- Defined: `topogpt3/api_server.py:671`
- Depends on: `topogpt3/chat.py`, `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### completions (method) `def completions(req, request)`
- Defined: `topogpt3/api_server.py:688`
- Depends on: `topogpt3/chat.py`, `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### chat_completions (method) `def chat_completions(req, request)`
- Defined: `topogpt3/api_server.py:744`
- Depends on: `topogpt3/chat.py`, `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### _check_model (method) `def _check_model()`
- Defined: `topogpt3/api_server.py:818`
- Depends on: `topogpt3/chat.py`, `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### _short_id (method) `def _short_id()`
- Defined: `topogpt3/api_server.py:823`
- Depends on: `topogpt3/chat.py`, `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### _build_chat_prompt (method) `def _build_chat_prompt(messages)`
- Defined: `topogpt3/api_server.py:827`
- Depends on: `topogpt3/chat.py`, `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### _extract_text (method) `def _extract_text(content)`
- Defined: `topogpt3/api_server.py:846`
- Depends on: `topogpt3/chat.py`, `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### _stream_completion (method) `def _stream_completion(prompt, max_tokens, temperature, top_k, repetition_penalty, stop, auto_continue, max_continuations)`
- Defined: `topogpt3/api_server.py:860`
- Depends on: `topogpt3/chat.py`, `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### _stream_chat (method) `def _stream_chat(t0_ms, prompt, max_tokens, temperature, top_k, repetition_penalty, stop, auto_continue, max_continuations)`
- Defined: `topogpt3/api_server.py:895`
- Depends on: `topogpt3/chat.py`, `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### main (method) `def main()`
- Defined: `topogpt3/api_server.py:933`
- Depends on: `topogpt3/chat.py`, `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### validate (method) `def validate(self, raw)`
- Defined: `topogpt3/api_server.py:148`
- Depends on: `topogpt3/chat.py`, `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### consume (method) `def consume(self, n)`
- Defined: `topogpt3/api_server.py:208`
- Depends on: `topogpt3/chat.py`, `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### __init__ (method) `def __init__(self, user_rps, admin_rps, capacity)`
- Defined: `topogpt3/api_server.py:220`
- Depends on: `topogpt3/chat.py`, `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### _cleanup (method) `def _cleanup(self)`
- Defined: `topogpt3/api_server.py:227`
- Depends on: `topogpt3/chat.py`, `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### allow (method) `def allow(self, key, role)`
- Defined: `topogpt3/api_server.py:233`
- Depends on: `topogpt3/chat.py`, `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### __init__ (method) `def __init__(self, max_failures, window)`
- Defined: `topogpt3/api_server.py:251`
- Depends on: `topogpt3/chat.py`, `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### record_failure (method) `def record_failure(self, ip)`
- Defined: `topogpt3/api_server.py:257`
- Depends on: `topogpt3/chat.py`, `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### is_banned (method) `def is_banned(self, ip)`
- Defined: `topogpt3/api_server.py:265`
- Depends on: `topogpt3/chat.py`, `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### _normalize_stop (method) `def _normalize_stop(cls, v)`
- Defined: `topogpt3/api_server.py:306`
- Depends on: `topogpt3/chat.py`, `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### _normalize_stop (method) `def _normalize_stop(cls, v)`
- Defined: `topogpt3/api_server.py:334`
- Depends on: `topogpt3/chat.py`, `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### complete (method) `def complete(self, prompt)`
- Defined: `topogpt3/api_server.py:351`
- Depends on: `topogpt3/chat.py`, `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### stream_complete (method) `def stream_complete(self, prompt)`
- Defined: `topogpt3/api_server.py:396`
- Depends on: `topogpt3/chat.py`, `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### _is_eos (method) `def _is_eos(self, token_id)`
- Defined: `topogpt3/api_server.py:485`
- Depends on: `topogpt3/chat.py`, `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

## topogpt3/chat.py

### pre_processing_chat (function) `def pre_processing_chat(conversations, add_system_ratio)`
- Defined: `topogpt3/chat.py:43`
- Doc: Randomly prepend a system prompt (skip when tools present).
- Imported by: `tests/test_heritage.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/api_server.py`, `topogpt3/eval_toolcall.py`, `topogpt3/eval_toolcall.py`, `topogpt3/tools_agent.py`, `topogpt3/tools_agent.py`, `topogpt3/train_agent.py`

### post_processing_chat (function) `def post_processing_chat(prompt, empty_think_ratio)`
- Defined: `topogpt3/chat.py:54`
- Imported by: `tests/test_heritage.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/api_server.py`, `topogpt3/eval_toolcall.py`, `topogpt3/eval_toolcall.py`, `topogpt3/tools_agent.py`, `topogpt3/tools_agent.py`, `topogpt3/train_agent.py`

### _fmt_tool_defs (function) `def _fmt_tool_defs(tools)`
- Defined: `topogpt3/chat.py:60`
- Imported by: `tests/test_heritage.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/api_server.py`, `topogpt3/eval_toolcall.py`, `topogpt3/eval_toolcall.py`, `topogpt3/tools_agent.py`, `topogpt3/tools_agent.py`, `topogpt3/train_agent.py`

### apply_chat_template (function) `def apply_chat_template(messages, tools, add_generation_prompt, open_thinking)`
- Defined: `topogpt3/chat.py:71`
- Doc: Render messages with tool definitions, thinking and tool-call blocks.
- Imported by: `tests/test_heritage.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/api_server.py`, `topogpt3/eval_toolcall.py`, `topogpt3/eval_toolcall.py`, `topogpt3/tools_agent.py`, `topogpt3/tools_agent.py`, `topogpt3/train_agent.py`

### parse_tool_calls (function) `def parse_tool_calls(text)`
- Defined: `topogpt3/chat.py:116`
- Imported by: `tests/test_heritage.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/api_server.py`, `topogpt3/eval_toolcall.py`, `topogpt3/eval_toolcall.py`, `topogpt3/tools_agent.py`, `topogpt3/tools_agent.py`, `topogpt3/train_agent.py`

### parse_thinking (function) `def parse_thinking(text)`
- Defined: `topogpt3/chat.py:126`
- Imported by: `tests/test_heritage.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/api_server.py`, `topogpt3/eval_toolcall.py`, `topogpt3/eval_toolcall.py`, `topogpt3/tools_agent.py`, `topogpt3/tools_agent.py`, `topogpt3/train_agent.py`

### split_reasoning_content (function) `def split_reasoning_content(text)`
- Defined: `topogpt3/chat.py:134`
- Doc: Split generated text into reasoning_content / content / tool_calls (API).
- Imported by: `tests/test_heritage.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/api_server.py`, `topogpt3/eval_toolcall.py`, `topogpt3/eval_toolcall.py`, `topogpt3/tools_agent.py`, `topogpt3/tools_agent.py`, `topogpt3/train_agent.py`

## topogpt3/continuation.py

### _count_unclosed_brackets (function) `def _count_unclosed_brackets(text)`
- Defined: `topogpt3/continuation.py:25`
- Imported by: `topogpt3/api_server.py`, `topogpt3/inference_hrm.py`, `topogpt3/model.py`

### _count_unclosed_fences (function) `def _count_unclosed_fences(text)`
- Defined: `topogpt3/continuation.py:36`
- Imported by: `topogpt3/api_server.py`, `topogpt3/inference_hrm.py`, `topogpt3/model.py`

### is_response_complete (function) `def is_response_complete(text, min_chars)`
- Defined: `topogpt3/continuation.py:45`
- Doc: Heuristic to decide whether a model response looks finished.
- Imported by: `topogpt3/api_server.py`, `topogpt3/inference_hrm.py`, `topogpt3/model.py`

### extract_tail_for_continuation (function) `def extract_tail_for_continuation(text, tail_lines, tail_chars)`
- Defined: `topogpt3/continuation.py:75`
- Doc: Return the last N lines (or up to tail_chars) of `text` as a
- Imported by: `topogpt3/api_server.py`, `topogpt3/inference_hrm.py`, `topogpt3/model.py`

### split_at_last_newline (function) `def split_at_last_newline(text)`
- Defined: `topogpt3/continuation.py:105`
- Doc: Split `text` at the last newline.
- Imported by: `topogpt3/api_server.py`, `topogpt3/inference_hrm.py`, `topogpt3/model.py`

## topogpt3/convert.py

### merge_base_lora (function) `def merge_base_lora(base_dir, lora_path, out_dir)`
- Defined: `topogpt3/convert.py:19`
- Depends on: `topogpt3/lora.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### export_hf_stub (function) `def export_hf_stub(ckpt_dir, out_dir)`
- Defined: `topogpt3/convert.py:38`
- Depends on: `topogpt3/lora.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### main (function) `def main()`
- Defined: `topogpt3/convert.py:49`
- Depends on: `topogpt3/lora.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

## topogpt3/eval_toolcall.py

### run_case (function) `def run_case(generate_fn, prompt, expect_tool)`
- Defined: `topogpt3/eval_toolcall.py:19`
- Depends on: `topogpt3/chat.py`, `topogpt3/tools_agent.py`
- Imported by: `tests/test_heritage.py`, `topogpt3/__init__.py`

### evaluate (function) `def evaluate(generate_fn)`
- Defined: `topogpt3/eval_toolcall.py:35`
- Depends on: `topogpt3/chat.py`, `topogpt3/tools_agent.py`
- Imported by: `tests/test_heritage.py`, `topogpt3/__init__.py`

## topogpt3/export_chat.py

### _pairs_codealpaca (function) `def _pairs_codealpaca(ex)`
- Defined: `topogpt3/export_chat.py:28`
- Depends on: `topogpt3/model.py`, `topogpt3/train.py`
- Imported by: `topogpt3/__main__.py`

### _pairs_code_feedback (function) `def _pairs_code_feedback(ex)`
- Defined: `topogpt3/export_chat.py:38`
- Depends on: `topogpt3/model.py`, `topogpt3/train.py`
- Imported by: `topogpt3/__main__.py`

### _pairs_magicoder (function) `def _pairs_magicoder(ex)`
- Defined: `topogpt3/export_chat.py:55`
- Depends on: `topogpt3/model.py`, `topogpt3/train.py`
- Imported by: `topogpt3/__main__.py`

### _iter_pairs (function) `def _iter_pairs(loader, tier, cap)`
- Defined: `topogpt3/export_chat.py:65`
- Depends on: `topogpt3/model.py`, `topogpt3/train.py`
- Imported by: `topogpt3/__main__.py`

### main (function) `def main()`
- Defined: `topogpt3/export_chat.py:81`
- Depends on: `topogpt3/model.py`, `topogpt3/train.py`
- Imported by: `topogpt3/__main__.py`

## topogpt3/inference.py

### main (method) `def main(argv)`
- Defined: `topogpt3/inference.py:721`
- Doc: CLI entry point. Returns a process exit code.
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### scale_presets (method) `def scale_presets()`
- Defined: `topogpt3/inference.py:103`
- Doc: Return the architecture preset table indexed by scale name.
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### preset (method) `def preset(self)`
- Defined: `topogpt3/inference.py:116`
- Doc: Return the resolved preset for the configured model scale.
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### validate (method) `def validate(self)`
- Defined: `topogpt3/inference.py:126`
- Doc: Raise ValueError if any setting falls outside its safety bounds.
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### build (method) `def build(settings)`
- Defined: `topogpt3/inference.py:162`
- Doc: Return a configured Logger with a single deduplicated stdout handler.
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### resolve_under (method) `def resolve_under(root)`
- Defined: `topogpt3/inference.py:182`
- Doc: Join `parts` under `root` and return the canonical resolved path.
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### require_existing_file (method) `def require_existing_file(path, expected_suffix)`
- Defined: `topogpt3/inference.py:198`
- Doc: Validate `path` points to an existing regular file with the expected suffix.
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __init__ (method) `def __init__(self, settings, logger)`
- Defined: `topogpt3/inference.py:215`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### load (method) `def load(self)`
- Defined: `topogpt3/inference.py:219`
- Doc: Return the topogpt3.train module which re-exports model symbols.
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __init__ (method) `def __init__(self, settings)`
- Defined: `topogpt3/inference.py:231`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### slot_dir (method) `def slot_dir(self)`
- Defined: `topogpt3/inference.py:239`
- Doc: Directory holding the active checkpoint slot.
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### model_file (method) `def model_file(self)`
- Defined: `topogpt3/inference.py:243`
- Doc: Resolved path to the safetensors weights file inside the slot.
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### state_file (method) `def state_file(self)`
- Defined: `topogpt3/inference.py:249`
- Doc: Resolved path to the JSON training-state file inside the slot.
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### assert_ready (method) `def assert_ready(self)`
- Defined: `topogpt3/inference.py:255`
- Doc: Verify weights exist and the on-disk size lies within safety bounds.
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __init__ (method) `def __init__(self, settings, logger)`
- Defined: `topogpt3/inference.py:277`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### detect_n_kv_heads (method) `def detect_n_kv_heads(self, weights_path, d_model, n_heads)`
- Defined: `topogpt3/inference.py:281`
- Doc: Recover N_KV_HEADS used at training by inspecting the k_proj shape.
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __init__ (method) `def __init__(self, settings, source_module, logger)`
- Defined: `topogpt3/inference.py:321`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### build (method) `def build(self, n_kv_heads, vocab_size)`
- Defined: `topogpt3/inference.py:327`
- Doc: Return a TopoGPT2Config dataclass ready to instantiate the model.
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __init__ (method) `def __init__(self, settings, source_module)`
- Defined: `topogpt3/inference.py:352`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### build (method) `def build(self)`
- Defined: `topogpt3/inference.py:356`
- Doc: Return an instance of BPETokenizer bound to the configured encoding.
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __init__ (method) `def __init__(self, settings, source_module, logger)`
- Defined: `topogpt3/inference.py:365`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### apply_if_enabled (method) `def apply_if_enabled(self)`
- Defined: `topogpt3/inference.py:371`
- Doc: Patch QuaternionSpectralLayer to use the 3-multiply Gauss contract.
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __init__ (method) `def __init__(self, settings, source_module, logger)`
- Defined: `topogpt3/inference.py:383`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### assemble (method) `def assemble(self, aligned_cfg, paths)`
- Defined: `topogpt3/inference.py:389`
- Doc: Build the TopoGPT2 graph, load weights into it, and return it in eval mode.
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __init__ (method) `def __init__(self, settings, source_module, logger)`
- Defined: `topogpt3/inference.py:420`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### apply (method) `def apply(self)`
- Defined: `topogpt3/inference.py:426`
- Doc: Seed all relevant RNGs using the model package helper when available.
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### from_settings (method) `def from_settings(cls, settings)`
- Defined: `topogpt3/inference.py:450`
- Doc: Construct a SamplingPolicy from inference settings.
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### tokens_per_second (method) `def tokens_per_second(self, elapsed_floor)`
- Defined: `topogpt3/inference.py:470`
- Doc: Return throughput in tokens/sec, clamped to avoid divide-by-zero.
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __init__ (method) `def __init__(self, settings, logger)`
- Defined: `topogpt3/inference.py:478`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### run (method) `def run(self, model, tokenizer, prompt, policy)`
- Defined: `topogpt3/inference.py:483`
- Doc: Generate a completion for `prompt` and return a GenerationReport.
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __init__ (method) `def __init__(self, settings, logger)`
- Defined: `topogpt3/inference.py:536`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### render (method) `def render(self, report)`
- Defined: `topogpt3/inference.py:540`
- Doc: Emit a banner with prompt and completion, plus a throughput log line.
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __init__ (method) `def __init__(self, settings, logger)`
- Defined: `topogpt3/inference.py:565`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### execute (method) `def execute(self)`
- Defined: `topogpt3/inference.py:571`
- Doc: Run the full inference pipeline end-to-end and return the report.
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### build_parser (method) `def build_parser()`
- Defined: `topogpt3/inference.py:619`
- Doc: Return the configured argparse.ArgumentParser.
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### parse (method) `def parse(argv)`
- Defined: `topogpt3/inference.py:698`
- Doc: Parse `argv` (or sys.argv) and return a populated InferenceSettings.
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

## topogpt3/inference_hrm.py

### main (method) `def main(argv)`
- Defined: `topogpt3/inference_hrm.py:1494`
- Doc: CLI entry point. Returns a process exit code.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### scale_presets (method) `def scale_presets()`
- Defined: `topogpt3/inference_hrm.py:221`
- Doc: Return the architecture preset table indexed by scale name.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### preset (method) `def preset(self)`
- Defined: `topogpt3/inference_hrm.py:234`
- Doc: Return the resolved preset for the configured model scale.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### validate (method) `def validate(self)`
- Defined: `topogpt3/inference_hrm.py:244`
- Doc: Raise ValueError if any setting falls outside its safety bounds.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### build (method) `def build(settings)`
- Defined: `topogpt3/inference_hrm.py:347`
- Doc: Return a configured Logger with a single deduplicated stdout handler.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### resolve_under (method) `def resolve_under(root)`
- Defined: `topogpt3/inference_hrm.py:367`
- Doc: Join parts under root and return the canonical resolved path.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### require_existing_file (method) `def require_existing_file(path, expected_suffix)`
- Defined: `topogpt3/inference_hrm.py:383`
- Doc: Validate path points to an existing regular file with the expected suffix.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __init__ (method) `def __init__(self, settings, logger)`
- Defined: `topogpt3/inference_hrm.py:400`
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### load (method) `def load(self)`
- Defined: `topogpt3/inference_hrm.py:404`
- Doc: Return the topogpt3.train module which re-exports model symbols.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __init__ (method) `def __init__(self, settings)`
- Defined: `topogpt3/inference_hrm.py:416`
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### slot_dir (method) `def slot_dir(self)`
- Defined: `topogpt3/inference_hrm.py:424`
- Doc: Directory holding the active checkpoint slot.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### model_file (method) `def model_file(self)`
- Defined: `topogpt3/inference_hrm.py:428`
- Doc: Resolved path to the safetensors weights file inside the slot.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### state_file (method) `def state_file(self)`
- Defined: `topogpt3/inference_hrm.py:434`
- Doc: Resolved path to the JSON training-state file inside the slot.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### assert_ready (method) `def assert_ready(self)`
- Defined: `topogpt3/inference_hrm.py:440`
- Doc: Verify weights exist and the on-disk size lies within safety bounds.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __init__ (method) `def __init__(self, settings, logger)`
- Defined: `topogpt3/inference_hrm.py:462`
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### detect_n_kv_heads (method) `def detect_n_kv_heads(self, weights_path, d_model, n_heads)`
- Defined: `topogpt3/inference_hrm.py:466`
- Doc: Recover N_KV_HEADS used at training by inspecting the k_proj shape.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __init__ (method) `def __init__(self, settings, source_module, logger)`
- Defined: `topogpt3/inference_hrm.py:505`
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### build (method) `def build(self, n_kv_heads, vocab_size)`
- Defined: `topogpt3/inference_hrm.py:511`
- Doc: Return a TopoGPT2Config dataclass ready to instantiate the model.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __init__ (method) `def __init__(self, settings, source_module)`
- Defined: `topogpt3/inference_hrm.py:536`
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### build (method) `def build(self)`
- Defined: `topogpt3/inference_hrm.py:540`
- Doc: Return an instance of BPETokenizer bound to the configured encoding.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __init__ (method) `def __init__(self, settings, source_module, logger)`
- Defined: `topogpt3/inference_hrm.py:549`
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### apply_if_enabled (method) `def apply_if_enabled(self)`
- Defined: `topogpt3/inference_hrm.py:555`
- Doc: Patch QuaternionSpectralLayer to use the 3-multiply Gauss contract.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __init__ (method) `def __init__(self, settings, source_module, logger)`
- Defined: `topogpt3/inference_hrm.py:567`
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### assemble (method) `def assemble(self, aligned_cfg, paths)`
- Defined: `topogpt3/inference_hrm.py:573`
- Doc: Build the TopoGPT2 graph, load weights into it, and return it in eval mode.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __init__ (method) `def __init__(self, settings, source_module, logger)`
- Defined: `topogpt3/inference_hrm.py:604`
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### apply (method) `def apply(self)`
- Defined: `topogpt3/inference_hrm.py:610`
- Doc: Seed all relevant RNGs using the model package helper when available.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __init__ (method) `def __init__(self, epsilon_floor)`
- Defined: `topogpt3/inference_hrm.py:627`
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### relative_change (method) `def relative_change(self, current, previous)`
- Defined: `topogpt3/inference_hrm.py:632`
- Doc: Return ||current - previous|| / max(||previous||, epsilon_floor).
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### absorb (method) `def absorb(self, sample)`
- Defined: `topogpt3/inference_hrm.py:671`
- Doc: Fold a per-token sample into the running totals.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __init__ (method) `def __init__(self, persist_tokens)`
- Defined: `topogpt3/inference_hrm.py:693`
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### get_or_init (method) `def get_or_init(self, reference)`
- Defined: `topogpt3/inference_hrm.py:700`
- Doc: Return the cached high-level state or a zeroed one when stale.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### commit (method) `def commit(self, new_state)`
- Defined: `topogpt3/inference_hrm.py:716`
- Doc: Store a fresh high-level state and increment the cache age.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### invalidate (method) `def invalidate(self)`
- Defined: `topogpt3/inference_hrm.py:721`
- Doc: Drop any cached state and reset the age counter.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __init__ (method) `def __init__(self, layers, final_norm, reasoning_config, logger)`
- Defined: `topogpt3/inference_hrm.py:768`
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### num_layers (method) `def num_layers(self)`
- Defined: `topogpt3/inference_hrm.py:789`
- Doc: Return the number of trained transformer layers.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### _full_pass (method) `def _full_pass(self, z_in, base_kvs)`
- Defined: `topogpt3/inference_hrm.py:793`
- Doc: Forward z_in through every layer using base_kvs as immutable prefix cache.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### _window_pass (method) `def _window_pass(self, z_in, base_kvs, window)`
- Defined: `topogpt3/inference_hrm.py:808`
- Doc: Forward z_in through the trailing `window` layers only.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### reason (method) `def reason(self, z_initial, base_kvs, cached_refinement)`
- Defined: `topogpt3/inference_hrm.py:827`
- Doc: Run hierarchical recursive thinking for a single emission step.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __init__ (method) `def __init__(self, logger)`
- Defined: `topogpt3/inference_hrm.py:938`
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### sample (method) `def sample(self, logits, token_history, temperature, top_k, repetition_penalty)`
- Defined: `topogpt3/inference_hrm.py:941`
- Doc: Return a sampled token id tensor of shape [B, 1] from raw logits [B, V].
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### from_settings (method) `def from_settings(cls, settings)`
- Defined: `topogpt3/inference_hrm.py:973`
- Doc: Construct a SamplingPolicy from inference settings.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### tokens_per_second (method) `def tokens_per_second(self, elapsed_floor)`
- Defined: `topogpt3/inference_hrm.py:995`
- Doc: Return throughput in tokens/sec, clamped to avoid divide-by-zero.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __init__ (method) `def __init__(self, settings, logger)`
- Defined: `topogpt3/inference_hrm.py:1011`
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### _encode_prompt (method) `def _encode_prompt(self, model, prompt_ids)`
- Defined: `topogpt3/inference_hrm.py:1016`
- Doc: Run the prompt through the full stack once, returning the final
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### run (method) `def run(self, model, tokenizer, prompt, policy)`
- Defined: `topogpt3/inference_hrm.py:1048`
- Doc: Generate a completion for prompt and return a GenerationReport.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __init__ (method) `def __init__(self, settings, logger)`
- Defined: `topogpt3/inference_hrm.py:1192`
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### render (method) `def render(self, report)`
- Defined: `topogpt3/inference_hrm.py:1196`
- Doc: Emit a banner with prompt, completion, throughput and reasoning stats.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __init__ (method) `def __init__(self, settings, logger)`
- Defined: `topogpt3/inference_hrm.py:1233`
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### execute (method) `def execute(self)`
- Defined: `topogpt3/inference_hrm.py:1239`
- Doc: Run the full inference pipeline end-to-end and return the report.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### build_parser (method) `def build_parser()`
- Defined: `topogpt3/inference_hrm.py:1287`
- Doc: Return the configured argparse.ArgumentParser.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### parse (method) `def parse(argv)`
- Defined: `topogpt3/inference_hrm.py:1448`
- Doc: Parse argv (or sys.argv) and return a populated HRMInferenceSettings.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

## topogpt3/jlens.py

### valid_position_mask (method) `def valid_position_mask(seq_len)`
- Defined: `topogpt3/jlens.py:132`
- Doc: Boolean mask over sequence positions to include in the Jacobian average.
- Depends on: `topogpt3/lens_model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### _check_layer_indices (method) `def _check_layer_indices(source_layers, target_layer, n_layers)`
- Defined: `topogpt3/jlens.py:162`
- Doc: Resolve None/negative layer indices, bounds-check, enforce source < target.
- Depends on: `topogpt3/lens_model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### jacobian_for_prompt (method) `def jacobian_for_prompt(model, prompt, source_layers)`
- Defined: `topogpt3/jlens.py:187`
- Doc: Compute the per-layer Jacobian estimator ``J_l`` for one prompt.
- Depends on: `topogpt3/lens_model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### _atomic_save (method) `def _atomic_save(obj, path)`
- Defined: `topogpt3/jlens.py:283`
- Doc: ``torch.save`` to a temp file then ``os.replace`` so a crash never
- Depends on: `topogpt3/lens_model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### fit (method) `def fit(model, prompts)`
- Defined: `topogpt3/jlens.py:291`
- Doc: Fit ``J_l`` over a list of prompts and return a JacobianLens.
- Depends on: `topogpt3/lens_model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### compute_slice (method) `def compute_slice(model, lens, prompt)`
- Defined: `topogpt3/jlens.py:705`
- Doc: Compute a position x layer slice of top-K token predictions.
- Depends on: `topogpt3/lens_model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### text_slice (method) `def text_slice(slice_data, tokenizer, n_cols)`
- Defined: `topogpt3/jlens.py:789`
- Doc: Render a SliceData as a readable text table showing decoded words.
- Depends on: `topogpt3/lens_model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### _demo_jlens (method) `def _demo_jlens()`
- Defined: `topogpt3/jlens.py:842`
- Doc: Run a full jacobian lens demo loading real weights from checkpoint.
- Depends on: `topogpt3/lens_model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __init__ (method) `def __init__(self, blocks, at)`
- Defined: `topogpt3/jlens.py:87`
- Depends on: `topogpt3/lens_model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### _make_hook (method) `def _make_hook(self, index)`
- Defined: `topogpt3/jlens.py:102`
- Depends on: `topogpt3/lens_model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __enter__ (method) `def __enter__(self)`
- Defined: `topogpt3/jlens.py:113`
- Depends on: `topogpt3/lens_model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __exit__ (method) `def __exit__(self)`
- Defined: `topogpt3/jlens.py:126`
- Depends on: `topogpt3/lens_model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### write_checkpoint (method) `def write_checkpoint()`
- Defined: `topogpt3/jlens.py:378`
- Depends on: `topogpt3/lens_model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __init__ (method) `def __init__(self, jacobians)`
- Defined: `topogpt3/jlens.py:470`
- Depends on: `topogpt3/lens_model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __repr__ (method) `def __repr__(self)`
- Defined: `topogpt3/jlens.py:482`
- Depends on: `topogpt3/lens_model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### save (method) `def save(self, path)`
- Defined: `topogpt3/jlens.py:489`
- Doc: Save to ``path``. Jacobians are stored as ``dtype`` (default fp16).
- Depends on: `topogpt3/lens_model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### load (method) `def load(cls, path)`
- Defined: `topogpt3/jlens.py:504`
- Doc: Load a lens previously written by ``save``.
- Depends on: `topogpt3/lens_model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### from_pretrained (method) `def from_pretrained(cls, name_or_path)`
- Defined: `topogpt3/jlens.py:519`
- Doc: Load a lens from a local file, a local directory, or a HuggingFace
- Depends on: `topogpt3/lens_model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### merge (method) `def merge(cls, lenses)`
- Defined: `topogpt3/jlens.py:543`
- Doc: Combine lenses fitted on disjoint prompt subsets into one
- Depends on: `topogpt3/lens_model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### transport (method) `def transport(self, residual, layer)`
- Defined: `topogpt3/jlens.py:574`
- Doc: Map a residual at ``layer`` into the final-layer basis: ``J_l @ h``.
- Depends on: `topogpt3/lens_model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### apply (method) `def apply(self, model, prompt)`
- Defined: `topogpt3/jlens.py:585`
- Doc: Run ``model`` on ``prompt`` and return lens logits at ``positions``.
- Depends on: `topogpt3/lens_model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __post_init__ (method) `def __post_init__(self)`
- Defined: `topogpt3/jlens.py:692`
- Depends on: `topogpt3/lens_model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### hook (method) `def hook(module, inputs, output)`
- Defined: `topogpt3/jlens.py:105`
- Depends on: `topogpt3/lens_model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### select (method) `def select(layer)`
- Defined: `topogpt3/jlens.py:646`
- Depends on: `topogpt3/lens_model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

## topogpt3/lens_model.py

### encode (method) `def encode(self, text)`
- Defined: `topogpt3/lens_model.py:40`
- Doc: Tokenize ``text`` to ``input_ids`` of shape ``[1, seq_len]`` on the
- Depends on: `topogpt3/model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/jlens.py`, `topogpt3/jlens.py`

### forward (method) `def forward(self, input_ids)`
- Defined: `topogpt3/lens_model.py:45`
- Doc: Run the residual stack on ``input_ids`` (no LM head). Must build an
- Depends on: `topogpt3/model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/jlens.py`, `topogpt3/jlens.py`

### unembed (method) `def unembed(self, residual)`
- Defined: `topogpt3/lens_model.py:52`
- Doc: Map a residual-stream tensor ``[..., d_model]`` to logits
- Depends on: `topogpt3/model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/jlens.py`, `topogpt3/jlens.py`

### from_topogpt2_config (method) `def from_topogpt2_config(cls, cfg)`
- Defined: `topogpt3/lens_model.py:84`
- Doc: Construct a lens config from a TopoGPT2Config dataclass.
- Depends on: `topogpt3/model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/jlens.py`, `topogpt3/jlens.py`

### probe_checkpoint (method) `def probe_checkpoint(cls, checkpoint_dir)`
- Defined: `topogpt3/lens_model.py:104`
- Doc: Probe a checkpoint directory and infer lens config from state.json.
- Depends on: `topogpt3/model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/jlens.py`, `topogpt3/jlens.py`

### __init__ (method) `def __init__(self, model)`
- Defined: `topogpt3/lens_model.py:150`
- Depends on: `topogpt3/model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/jlens.py`, `topogpt3/jlens.py`

### forward (method) `def forward(self, input_ids)`
- Defined: `topogpt3/lens_model.py:154`
- Depends on: `topogpt3/model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/jlens.py`, `topogpt3/jlens.py`

### __init__ (method) `def __init__(self, model, tokenizer)`
- Defined: `topogpt3/lens_model.py:172`
- Depends on: `topogpt3/model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/jlens.py`, `topogpt3/jlens.py`

### n_layers (method) `def n_layers(self)`
- Defined: `topogpt3/lens_model.py:184`
- Depends on: `topogpt3/model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/jlens.py`, `topogpt3/jlens.py`

### d_model (method) `def d_model(self)`
- Defined: `topogpt3/lens_model.py:188`
- Depends on: `topogpt3/model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/jlens.py`, `topogpt3/jlens.py`

### layers (method) `def layers(self)`
- Defined: `topogpt3/lens_model.py:192`
- Depends on: `topogpt3/model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/jlens.py`, `topogpt3/jlens.py`

### tokenizer (method) `def tokenizer(self)`
- Defined: `topogpt3/lens_model.py:196`
- Depends on: `topogpt3/model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/jlens.py`, `topogpt3/jlens.py`

### tokenizer (method) `def tokenizer(self, tok)`
- Defined: `topogpt3/lens_model.py:200`
- Depends on: `topogpt3/model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/jlens.py`, `topogpt3/jlens.py`

### input_device (method) `def input_device(self)`
- Defined: `topogpt3/lens_model.py:204`
- Depends on: `topogpt3/model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/jlens.py`, `topogpt3/jlens.py`

### input_device (method) `def input_device(self, device)`
- Defined: `topogpt3/lens_model.py:210`
- Depends on: `topogpt3/model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/jlens.py`, `topogpt3/jlens.py`

### encode (method) `def encode(self, text)`
- Defined: `topogpt3/lens_model.py:213`
- Doc: Tokenize text to input_ids of shape ``[1, seq_len]``.
- Depends on: `topogpt3/model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/jlens.py`, `topogpt3/jlens.py`

### forward (method) `def forward(self, input_ids)`
- Defined: `topogpt3/lens_model.py:228`
- Doc: Run the residual stack on ``input_ids``.
- Depends on: `topogpt3/model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/jlens.py`, `topogpt3/jlens.py`

### unembed (method) `def unembed(self, residual)`
- Defined: `topogpt3/lens_model.py:237`
- Doc: Map residual ``[..., d_model]`` to logits ``[..., vocab_size]``.
- Depends on: `topogpt3/model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/jlens.py`, `topogpt3/jlens.py`

### from_checkpoint (method) `def from_checkpoint(cls, checkpoint_dir)`
- Defined: `topogpt3/lens_model.py:246`
- Doc: Build a TopoGPT3LensModel from a checkpoint directory.
- Depends on: `topogpt3/model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/jlens.py`, `topogpt3/jlens.py`

### __init__ (method) `def __init__(self, n_layers, d_model, vocab_size, seed)`
- Defined: `topogpt3/lens_model.py:315`
- Depends on: `topogpt3/model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/jlens.py`, `topogpt3/jlens.py`

### forward (method) `def forward(self, token_ids, past_kvs)`
- Defined: `topogpt3/lens_model.py:344`
- Depends on: `topogpt3/model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/jlens.py`, `topogpt3/jlens.py`

### __init__ (method) `def __init__(self, d_model)`
- Defined: `topogpt3/lens_model.py:360`
- Depends on: `topogpt3/model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/jlens.py`, `topogpt3/jlens.py`

### forward (method) `def forward(self, x, past_kv)`
- Defined: `topogpt3/lens_model.py:366`
- Depends on: `topogpt3/model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/jlens.py`, `topogpt3/jlens.py`

## topogpt3/lora.py

### _is_quaternion_sublayer (method) `def _is_quaternion_sublayer(name)`
- Defined: `topogpt3/lora.py:29`
- Imported by: `tests/test_heritage.py`, `topogpt3/__init__.py`, `topogpt3/convert.py`, `topogpt3/train_lora.py`

### lora_targets (method) `def lora_targets(model, include_mlp)`
- Defined: `topogpt3/lora.py:34`
- Doc: Yield (name, nn.Linear) candidates.
- Imported by: `tests/test_heritage.py`, `topogpt3/__init__.py`, `topogpt3/convert.py`, `topogpt3/train_lora.py`

### apply_lora (method) `def apply_lora(model, rank, include_mlp)`
- Defined: `topogpt3/lora.py:54`
- Doc: Monkey-patch target linears with additive LoRA. Returns patched names.
- Imported by: `tests/test_heritage.py`, `topogpt3/__init__.py`, `topogpt3/convert.py`, `topogpt3/train_lora.py`

### lora_parameters (method) `def lora_parameters(model)`
- Defined: `topogpt3/lora.py:73`
- Imported by: `tests/test_heritage.py`, `topogpt3/__init__.py`, `topogpt3/convert.py`, `topogpt3/train_lora.py`

### freeze_non_lora (method) `def freeze_non_lora(model)`
- Defined: `topogpt3/lora.py:80`
- Imported by: `tests/test_heritage.py`, `topogpt3/__init__.py`, `topogpt3/convert.py`, `topogpt3/train_lora.py`

### save_lora (method) `def save_lora(model, path)`
- Defined: `topogpt3/lora.py:88`
- Imported by: `tests/test_heritage.py`, `topogpt3/__init__.py`, `topogpt3/convert.py`, `topogpt3/train_lora.py`

### load_lora (method) `def load_lora(model, path, device)`
- Defined: `topogpt3/lora.py:99`
- Imported by: `tests/test_heritage.py`, `topogpt3/__init__.py`, `topogpt3/convert.py`, `topogpt3/train_lora.py`

### merge_lora (method) `def merge_lora(model, lora_path, save_path)`
- Defined: `topogpt3/lora.py:110`
- Doc: Merge LoRA deltas into base weights and save (fp16, no .lora. keys).
- Imported by: `tests/test_heritage.py`, `topogpt3/__init__.py`, `topogpt3/convert.py`, `topogpt3/train_lora.py`

### __init__ (method) `def __init__(self, in_features, out_features, rank)`
- Defined: `topogpt3/lora.py:17`
- Imported by: `tests/test_heritage.py`, `topogpt3/__init__.py`, `topogpt3/convert.py`, `topogpt3/train_lora.py`

### forward (method) `def forward(self, x)`
- Defined: `topogpt3/lora.py:25`
- Imported by: `tests/test_heritage.py`, `topogpt3/__init__.py`, `topogpt3/convert.py`, `topogpt3/train_lora.py`

### _fwd (method) `def _fwd(x, _o, _l)`
- Defined: `topogpt3/lora.py:66`
- Imported by: `tests/test_heritage.py`, `topogpt3/__init__.py`, `topogpt3/convert.py`, `topogpt3/train_lora.py`

## topogpt3/model.py

### setup_logger (method) `def setup_logger(name, level)`
- Defined: `topogpt3/model.py:192`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### set_seed (method) `def set_seed(seed, device)`
- Defined: `topogpt3/model.py:202`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### build_file_tiers (method) `def build_file_tiers(paths, short, med)`
- Defined: `topogpt3/model.py:1737`
- Doc: Classify file paths into complexity tiers by line count.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### apply_quantization (method) `def apply_quantization(model, config)`
- Defined: `topogpt3/model.py:1994`
- Doc: Quantize embedding and lm_head layers for reduced VRAM usage.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### _tokenize_text_to_memmap (method) `def _tokenize_text_to_memmap(text, tokenizer, path, max_tokens)`
- Defined: `topogpt3/model.py:2162`
- Doc: Tokenize a single text string and write tokens to disk as raw int64.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### main (method) `def main()`
- Defined: `topogpt3/model.py:3589`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### __post_init__ (method) `def __post_init__(self)`
- Defined: `topogpt3/model.py:161`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### hamilton_product (method) `def hamilton_product(q1, q2)`
- Defined: `topogpt3/model.py:222`
- Doc: Producto de Hamilton q1 ⊗ q2. Ambos [..., 4].
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### normalize (method) `def normalize(q, eps)`
- Defined: `topogpt3/model.py:234`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### conjugate (method) `def conjugate(q)`
- Defined: `topogpt3/model.py:238`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### rotate_vector (method) `def rotate_vector(v, q)`
- Defined: `topogpt3/model.py:243`
- Doc: Rota vector 3D v por cuaternión unitario q. v:[...,3] q:[...,4]
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### __init__ (method) `def __init__(self, in_features, out_features, bias)`
- Defined: `topogpt3/model.py:265`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### forward (method) `def forward(self, x)`
- Defined: `topogpt3/model.py:281`
- Doc: x: [..., in_features] → [..., out_features]
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### __init__ (method) `def __init__(self, in_q, out_q, grid_h, grid_w, init_scale)`
- Defined: `topogpt3/model.py:318`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### _kernel (method) `def _kernel(self, c)`
- Defined: `topogpt3/model.py:337`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### _contract (method) `def _contract(self, W, X)`
- Defined: `topogpt3/model.py:340`
- Doc: Suma sobre canales in_q: Y[b,o,h,w] = Σ_i W[i,o,h,w]·X[b,i,h,w]
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### forward (method) `def forward(self, x)`
- Defined: `topogpt3/model.py:344`
- Doc: x: [B, 4*in_q, H, W]  (4 canales cuaterniones sobre grid espacial)
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### __init__ (method) `def __init__(self, config)`
- Defined: `topogpt3/model.py:398`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### _filter1d (method) `def _filter1d(self, x, kr, ki)`
- Defined: `topogpt3/model.py:430`
- Doc: Filtro espectral 1D: x[..., D] → filtrado[..., D]
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### encode (method) `def encode(self, x)`
- Defined: `topogpt3/model.py:436`
- Doc: x: [..., D_MODEL] → latent: [..., D_LAT]
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### decode (method) `def decode(self, z)`
- Defined: `topogpt3/model.py:441`
- Doc: z: [..., D_LAT] → recon: [..., D_MODEL]
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### forward (method) `def forward(self, x)`
- Defined: `topogpt3/model.py:446`
- Doc: Devuelve (latent, recon_loss)
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### process_torus_grid (method) `def process_torus_grid(self, grid)`
- Defined: `topogpt3/model.py:453`
- Doc: Procesa el grid del toro con QuaternionSpectralLayer.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### __init__ (method) `def __init__(self, d_model, config)`
- Defined: `topogpt3/model.py:486`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### _build_torus_graph (method) `def _build_torus_graph(self)`
- Defined: `topogpt3/model.py:526`
- Doc: Construye las aristas del grafo toro 2×4.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### _torus_soft_assign (method) `def _torus_soft_assign(self, phi1, phi2)`
- Defined: `topogpt3/model.py:560`
- Doc: Asignación blanda de tokens a los 8 nodos del toro via distancia circular.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### _message_passing (method) `def _message_passing(self, node_feat)`
- Defined: `topogpt3/model.py:587`
- Doc: Message-passing VECTORIZADO con rotaciones cuaterniones.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### forward (method) `def forward(self, x)`
- Defined: `topogpt3/model.py:624`
- Doc: x: [B, S, D_MODEL]
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### __init__ (method) `def __init__(self, d_head, max_seq_len, base, yarn_factor, yarn_orig_max)`
- Defined: `topogpt3/model.py:697`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### enable_yarn (method) `def enable_yarn(self, factor, orig_max)`
- Defined: `topogpt3/model.py:716`
- Doc: Enable YaRN extrapolation post-hoc (rebuilds cache in place).
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### _build_cache (method) `def _build_cache(self, seq_len)`
- Defined: `topogpt3/model.py:724`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### _rotate_half (method) `def _rotate_half(self, x)`
- Defined: `topogpt3/model.py:732`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### forward (method) `def forward(self, q, k, seq_len, offset)`
- Defined: `topogpt3/model.py:736`
- Doc: q, k: [B, n_heads, S_q/S_k, d_head]
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### __init__ (method) `def __init__(self, d_model, eps)`
- Defined: `topogpt3/model.py:763`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### forward (method) `def forward(self, x)`
- Defined: `topogpt3/model.py:768`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### __init__ (method) `def __init__(self, d_model, expansion, dropout)`
- Defined: `topogpt3/model.py:784`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### forward (method) `def forward(self, x)`
- Defined: `topogpt3/model.py:798`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### __init__ (method) `def __init__(self, d_model, config)`
- Defined: `topogpt3/model.py:821`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### _route (method) `def _route(self, x)`
- Defined: `topogpt3/model.py:842`
- Doc: x: [N, D] donde N = B*S (tokens aplanados)
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### forward (method) `def forward(self, x)`
- Defined: `topogpt3/model.py:884`
- Doc: x: [B, S, D]
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### __init__ (method) `def __init__(self, d_model, n_heads, config)`
- Defined: `topogpt3/model.py:921`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### forward (method) `def forward(self, x, is_causal, past_kv)`
- Defined: `topogpt3/model.py:940`
- Doc: Args:
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### __init__ (method) `def __init__(self, d_model, n_heads, config)`
- Defined: `topogpt3/model.py:1024`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### _forward_impl (method) `def _forward_impl(self, x, past_kv)`
- Defined: `topogpt3/model.py:1033`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### forward (method) `def forward(self, x, past_kv)`
- Defined: `topogpt3/model.py:1042`
- Doc: Retorna (x_out, aux_loss, kv_cache).
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### __init__ (method) `def __init__(self, config)`
- Defined: `topogpt3/model.py:1073`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### _init_weights (method) `def _init_weights(self)`
- Defined: `topogpt3/model.py:1098`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### forward (method) `def forward(self, token_ids, past_kvs)`
- Defined: `topogpt3/model.py:1105`
- Doc: token_ids: [B, S]  (enteros)
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### forward_with_memory (method) `def forward_with_memory(self, token_ids)`
- Defined: `topogpt3/model.py:1128`
- Doc: Process long sequences with latent memory-token context compression.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### count_params (method) `def count_params(self)`
- Defined: `topogpt3/model.py:1178`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### generate (method) `def generate(self, token_ids, max_new_tokens, temperature, top_k, repetition_penalty)`
- Defined: `topogpt3/model.py:1184`
- Doc: Autoregressive generation with KV cache and top-k sampling.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### generate_with_continuation (method) `def generate_with_continuation(self, token_ids, tokenizer, max_new_tokens, temperature, top_k, repetition_penalty, max_continuations, tail_lines)`
- Defined: `topogpt3/model.py:1235`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### __init__ (method) `def __init__(self, encoding)`
- Defined: `topogpt3/model.py:1282`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### encode (method) `def encode(self, text)`
- Defined: `topogpt3/model.py:1290`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### decode (method) `def decode(self, tokens)`
- Defined: `topogpt3/model.py:1293`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### eot_token (method) `def eot_token(self)`
- Defined: `topogpt3/model.py:1296`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### __init__ (method) `def __init__(self, root, cache_dir, logger)`
- Defined: `topogpt3/model.py:1408`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### scan (method) `def scan(self, force)`
- Defined: `topogpt3/model.py:1415`
- Doc: Walk directory tree collecting text file paths. Cached to disk.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### __init__ (method) `def __init__(self, cache_dir, logger)`
- Defined: `topogpt3/model.py:1482`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### tokenize (method) `def tokenize(self, file_paths, tokenizer, cache_key, max_tokens, min_chars)`
- Defined: `topogpt3/model.py:1487`
- Doc: Tokenize all files and return a memory-mapped numpy array.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### __init__ (method) `def __init__(self, tokens, seq_len)`
- Defined: `topogpt3/model.py:1570`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### __len__ (method) `def __len__(self)`
- Defined: `topogpt3/model.py:1575`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### __getitem__ (method) `def __getitem__(self, idx)`
- Defined: `topogpt3/model.py:1578`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### __init__ (method) `def __init__(self, config, logger)`
- Defined: `topogpt3/model.py:1598`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### _compute_entropy (method) `def _compute_entropy(self, text)`
- Defined: `topogpt3/model.py:1607`
- Doc: Shannon entropy of byte frequencies (bits per byte).
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### _has_long_lines (method) `def _has_long_lines(self, text, threshold)`
- Defined: `topogpt3/model.py:1621`
- Doc: Return True if any line exceeds threshold characters.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### _special_token_ratio (method) `def _special_token_ratio(self, text, tokenizer)`
- Defined: `topogpt3/model.py:1628`
- Doc: Fraction of tokens that are pure whitespace or indentation-only.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### _content_hash (method) `def _content_hash(self, text)`
- Defined: `topogpt3/model.py:1642`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### filter_file (method) `def filter_file(self, path, tokenizer)`
- Defined: `topogpt3/model.py:1645`
- Doc: Read and evaluate a file. Returns text if passed, None if filtered.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### report (method) `def report(self)`
- Defined: `topogpt3/model.py:1685`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### __init__ (method) `def __init__(self, tokens, seq_len, file_tiers, active_tier, logger)`
- Defined: `topogpt3/model.py:1706`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### _update_len (method) `def _update_len(self)`
- Defined: `topogpt3/model.py:1716`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### set_tier (method) `def set_tier(self, tier)`
- Defined: `topogpt3/model.py:1722`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### __len__ (method) `def __len__(self)`
- Defined: `topogpt3/model.py:1726`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### __getitem__ (method) `def __getitem__(self, idx)`
- Defined: `topogpt3/model.py:1729`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### __init__ (method) `def __init__(self, base_trainer)`
- Defined: `topogpt3/model.py:1774`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### _build_dataloader (method) `def _build_dataloader(self, dataset, seq_len, batch_size, is_train)`
- Defined: `topogpt3/model.py:1780`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### run (method) `def run(self, train_paths, val_paths, tokenizer, file_tiers, phases)`
- Defined: `topogpt3/model.py:1790`
- Doc: Run training with progressive sequence length across phases.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### __init__ (method) `def __init__(self, target_model, config, logger)`
- Defined: `topogpt3/model.py:1848`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### _build_draft (method) `def _build_draft(self)`
- Defined: `topogpt3/model.py:1856`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### generate (method) `def generate(self, token_ids, max_new_tokens, temperature, top_k, repetition_penalty)`
- Defined: `topogpt3/model.py:1870`
- Doc: Autoregressive generation via speculative decoding.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### __init__ (method) `def __init__(self, embed, mode)`
- Defined: `topogpt3/model.py:1961`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### forward (method) `def forward(self, indices)`
- Defined: `topogpt3/model.py:1990`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### __init__ (method) `def __init__(self, model, config, tokenizer)`
- Defined: `topogpt3/model.py:2030`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### cache_tokens (method) `def cache_tokens(self, key, tokens)`
- Defined: `topogpt3/model.py:2037`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### model (method) `def model(self)`
- Defined: `topogpt3/model.py:2041`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### optimizer (method) `def optimizer(self)`
- Defined: `topogpt3/model.py:2045`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### scaler (method) `def scaler(self)`
- Defined: `topogpt3/model.py:2049`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### amp_dtype (method) `def amp_dtype(self)`
- Defined: `topogpt3/model.py:2053`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### completed_epochs (method) `def completed_epochs(self)`
- Defined: `topogpt3/model.py:2057`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### completed_epochs (method) `def completed_epochs(self, v)`
- Defined: `topogpt3/model.py:2061`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### global_step (method) `def global_step(self)`
- Defined: `topogpt3/model.py:2065`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### global_step (method) `def global_step(self, v)`
- Defined: `topogpt3/model.py:2069`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### best_val_loss (method) `def best_val_loss(self)`
- Defined: `topogpt3/model.py:2073`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### best_val_loss (method) `def best_val_loss(self, v)`
- Defined: `topogpt3/model.py:2077`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### history (method) `def history(self)`
- Defined: `topogpt3/model.py:2081`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### ckpt_mgr (method) `def ckpt_mgr(self)`
- Defined: `topogpt3/model.py:2085`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### resume (method) `def resume(self)`
- Defined: `topogpt3/model.py:2088`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### _current_state (method) `def _current_state(self)`
- Defined: `topogpt3/model.py:2091`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### _cosine_lr (method) `def _cosine_lr(self)`
- Defined: `topogpt3/model.py:2094`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### _set_lr (method) `def _set_lr(self)`
- Defined: `topogpt3/model.py:2097`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### evaluate (method) `def evaluate(self, dataloader)`
- Defined: `topogpt3/model.py:2100`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### _sample_text (method) `def _sample_text(self)`
- Defined: `topogpt3/model.py:2103`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### _progressive_train (method) `def _progressive_train(self, train_paths, val_paths, tokenizer, phases, memtok)`
- Defined: `topogpt3/model.py:2106`
- Doc: Training loop with progressive sequence length across phases.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### train (method) `def train(self, train_dl, val_dl)`
- Defined: `topogpt3/model.py:2145`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### run_curriculum (method) `def run_curriculum(self, train_paths, val_paths, tokenizer, phases)`
- Defined: `topogpt3/model.py:2148`
- Doc: Top-level entry point: curriculum + progressive seq len.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### __init__ (method) `def __init__(self, config, logger)`
- Defined: `topogpt3/model.py:2199`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### patch_config_for_resume (method) `def patch_config_for_resume(self, cfg)`
- Defined: `topogpt3/model.py:2209`
- Doc: Lee el checkpoint 'latest' y ajusta cfg.N_KV_HEADS / cfg.GQA_GROUPS
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### _save_model (method) `def _save_model(self, model, directory)`
- Defined: `topogpt3/model.py:2238`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### _load_model (method) `def _load_model(self, model, directory)`
- Defined: `topogpt3/model.py:2251`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### _save_optimizer (method) `def _save_optimizer(self, optimizer, directory)`
- Defined: `topogpt3/model.py:2282`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### _load_optimizer (method) `def _load_optimizer(self, optimizer, directory, device)`
- Defined: `topogpt3/model.py:2285`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### _save_state (method) `def _save_state(self, state, directory)`
- Defined: `topogpt3/model.py:2294`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### _load_state (method) `def _load_state(self, directory)`
- Defined: `topogpt3/model.py:2299`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### should_save (method) `def should_save(self)`
- Defined: `topogpt3/model.py:2310`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### save (method) `def save(self, model, optimizer, state, is_best)`
- Defined: `topogpt3/model.py:2313`
- Doc: Guarda checkpoint completo.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### load_latest (method) `def load_latest(self, model, optimizer)`
- Defined: `topogpt3/model.py:2358`
- Doc: Carga el ultimo checkpoint guardado.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### load_best (method) `def load_best(self, model)`
- Defined: `topogpt3/model.py:2385`
- Doc: Carga el mejor modelo guardado (solo pesos, sin optimizador).
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### has_checkpoint (method) `def has_checkpoint(self)`
- Defined: `topogpt3/model.py:2397`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### __init__ (method) `def __init__(self, model, config, tokenizer)`
- Defined: `topogpt3/model.py:2419`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### resume (method) `def resume(self)`
- Defined: `topogpt3/model.py:2454`
- Doc: Carga el ultimo checkpoint disponible.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### _current_state (method) `def _current_state(self)`
- Defined: `topogpt3/model.py:2479`
- Doc: Construye el dict de estado para persistir en state.json.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### _cosine_lr (method) `def _cosine_lr(self, step_in_session, total_steps_session)`
- Defined: `topogpt3/model.py:2490`
- Doc: Cosine decay con warmup. El schedule es relativo a la sesion actual.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### _set_lr (method) `def _set_lr(self, lr)`
- Defined: `topogpt3/model.py:2498`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### train (method) `def train(self, train_dl, val_dl)`
- Defined: `topogpt3/model.py:2502`
- Doc: Entrena cfg.EPOCHS epocas adicionales a partir de completed_epochs.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### _sample_text (method) `def _sample_text(self, tokenizer, prompts, max_new, temperature, top_k)`
- Defined: `topogpt3/model.py:2638`
- Doc: Genera una muestra de texto al final de cada epoch para monitorear
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### evaluate (method) `def evaluate(self, dataloader)`
- Defined: `topogpt3/model.py:2670`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### __init__ (method) `def __init__(self, config)`
- Defined: `topogpt3/model.py:2720`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### compute_delta (method) `def compute_delta(self, model)`
- Defined: `topogpt3/model.py:2728`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### compute_alpha (method) `def compute_alpha(self, delta)`
- Defined: `topogpt3/model.py:2735`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### update_grad_buffer (method) `def update_grad_buffer(self, model)`
- Defined: `topogpt3/model.py:2740`
- Doc: Captura gradientes de forma segura, ignorando tensores corruptos.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### compute_t_eff (method) `def compute_t_eff(self, lr)`
- Defined: `topogpt3/model.py:2766`
- Doc: T_eff = lr/2 * Var(gradiente). Temperatura termodinamica efectiva.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### compute_kappa (method) `def compute_kappa(self, model, dataloader, n_batches)`
- Defined: `topogpt3/model.py:2774`
- Doc: κ = λ_max / λ_min de la covarianza del gradiente.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### compute_berry_phase (method) `def compute_berry_phase(self, model)`
- Defined: `topogpt3/model.py:2832`
- Doc: Fase de Berry de los kernels espectrales imaginarios.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### compute_lc (method) `def compute_lc(self, model)`
- Defined: `topogpt3/model.py:2845`
- Doc: Complejidad local: 1 - similitud coseno promedio entre filas de pesos.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### compute_sp (method) `def compute_sp(self, model)`
- Defined: `topogpt3/model.py:2859`
- Doc: Superposicion: correlacion inter-fila promedio (entrelazamiento de features).
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### classify_phase (method) `def classify_phase(self, delta, kappa, berry)`
- Defined: `topogpt3/model.py:2875`
- Doc: Clasificacion de fase segun Book.md:
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### compute_all (method) `def compute_all(self, model, lr, dataloader, compute_kappa)`
- Defined: `topogpt3/model.py:2894`
- Doc: Calcula todas las metricas.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### format_log (method) `def format_log(self, m)`
- Defined: `topogpt3/model.py:2919`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### __init__ (method) `def __init__(self, config, logger)`
- Defined: `topogpt3/model.py:2955`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### _measure_ratio (method) `def _measure_ratio(self, ratio, sample_batch)`
- Defined: `topogpt3/model.py:2959`
- Doc: Mide la coherencia espectral para un ratio dado.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### optimize (method) `def optimize(self, dataloader)`
- Defined: `topogpt3/model.py:2988`
- Doc: Retorna el mejor ratio de inicializacion de kernels espectrales.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### __init__ (method) `def __init__(self, config, logger)`
- Defined: `topogpt3/model.py:3028`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### prospect (method) `def prospect(self, candidates, train_dataset, prospect_steps)`
- Defined: `topogpt3/model.py:3032`
- Doc: Retorna el mejor batch size segun delta y T_eff.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### __init__ (method) `def __init__(self, config, logger)`
- Defined: `topogpt3/model.py:3111`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### mine (method) `def mine(self, seed_start, n_seeds, train_dataset, prospect_steps)`
- Defined: `topogpt3/model.py:3115`
- Doc: Retorna la semilla con la mejor trayectoria de delta.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### __init__ (method) `def __init__(self, trainer, t0, cooling_rate, stagnation_patience)`
- Defined: `topogpt3/model.py:3197`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### refine (method) `def refine(self, train_dl, val_dl, refine_epochs)`
- Defined: `topogpt3/model.py:3206`
- Doc: Ejecuta refine_epochs epocas de recocido simulado.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### __init__ (method) `def __init__(self, config, train_tokens, val_tokens, tokenizer, logger, curriculum_tiers, progressive_seq)`
- Defined: `topogpt3/model.py:3349`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### _build_dataloader (method) `def _build_dataloader(self, tokens, seq_len, batch_size, shuffle, tag)`
- Defined: `topogpt3/model.py:3362`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### _build_phases (method) `def _build_phases(self)`
- Defined: `topogpt3/model.py:3376`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### run (method) `def run(self, run_prospect, refine_epochs, resume, prospect_steps, probe_seeds, seed_start)`
- Defined: `topogpt3/model.py:3385`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### __init__ (method) `def __init__(self, config, train_dataset, val_dataset, tokenizer, logger)`
- Defined: `topogpt3/model.py:3487`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### _make_dataloaders (method) `def _make_dataloaders(self, batch_size)`
- Defined: `topogpt3/model.py:3497`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### run (method) `def run(self, run_prospect, refine_epochs, resume, prospect_steps, probe_seeds, seed_start)`
- Defined: `topogpt3/model.py:3509`
- Doc: Ejecuta el pipeline completo.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### ckpt_fn (method) `def ckpt_fn(x_in)`
- Defined: `topogpt3/model.py:1050`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

## topogpt3/rewards.py

### rep_penalty (function) `def rep_penalty(text, n, cap)`
- Defined: `topogpt3/rewards.py:17`
- Imported by: `tests/test_heritage.py`, `topogpt3/__init__.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_ppo.py`

### base_rewards (function) `def base_rewards(prompts, completions, reward_fn, device)`
- Defined: `topogpt3/rewards.py:25`
- Doc: Group-RL reward skeleton: length + thinking + RM - repetition.
- Imported by: `tests/test_heritage.py`, `topogpt3/__init__.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_ppo.py`

### spectral_bonus (function) `def spectral_bonus(fisher_gap, drift, w_fisher, w_drift)`
- Defined: `topogpt3/rewards.py:55`
- Doc: Small bonus preserving topological identity (0 when stats absent).
- Imported by: `tests/test_heritage.py`, `topogpt3/__init__.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_ppo.py`

### grpo_advantages (function) `def grpo_advantages(rewards, num_generations)`
- Defined: `topogpt3/rewards.py:67`
- Imported by: `tests/test_heritage.py`, `topogpt3/__init__.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_ppo.py`

### k3_kl (function) `def k3_kl(ref_logp, new_logp)`
- Defined: `topogpt3/rewards.py:74`
- Imported by: `tests/test_heritage.py`, `topogpt3/__init__.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_ppo.py`

### grpo_loss (function) `def grpo_loss(new_logp, old_logp, ref_logp, adv, mask, beta, eps, loss_type, eps_high)`
- Defined: `topogpt3/rewards.py:79`
- Imported by: `tests/test_heritage.py`, `topogpt3/__init__.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_ppo.py`

### logits_to_log_probs (function) `def logits_to_log_probs(logits, labels)`
- Defined: `topogpt3/rewards.py:94`
- Imported by: `tests/test_heritage.py`, `topogpt3/__init__.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_ppo.py`

### dpo_loss_fn (function) `def dpo_loss_fn(ref_lp, pol_lp, mask, beta)`
- Defined: `topogpt3/rewards.py:99`
- Imported by: `tests/test_heritage.py`, `topogpt3/__init__.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_ppo.py`

### distillation_loss (function) `def distillation_loss(student_logits, teacher_logits, mask, labels, alpha, temp)`
- Defined: `topogpt3/rewards.py:108`
- Doc: White-box distill: CE + T^2*KL on masked response tokens.
- Imported by: `tests/test_heritage.py`, `topogpt3/__init__.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_ppo.py`

## topogpt3/rollout.py

### compute_per_token_logps (method) `def compute_per_token_logps(model, input_ids, n_keep)`
- Defined: `topogpt3/rollout.py:27`
- Imported by: `tests/test_heritage.py`, `topogpt3/__init__.py`, `topogpt3/train_grpo.py`, `topogpt3/train_ppo.py`

### create_rollout_engine (method) `def create_rollout_engine(policy_model, tokenizer, device)`
- Defined: `topogpt3/rollout.py:83`
- Imported by: `tests/test_heritage.py`, `topogpt3/__init__.py`, `topogpt3/train_grpo.py`, `topogpt3/train_ppo.py`

### rollout (method) `def rollout(self, prompt_ids, num_generations, max_new_tokens, temperature, tokenizer)`
- Defined: `topogpt3/rollout.py:41`
- Imported by: `tests/test_heritage.py`, `topogpt3/__init__.py`, `topogpt3/train_grpo.py`, `topogpt3/train_ppo.py`

### update_policy (method) `def update_policy(self, model)`
- Defined: `topogpt3/rollout.py:46`
- Imported by: `tests/test_heritage.py`, `topogpt3/__init__.py`, `topogpt3/train_grpo.py`, `topogpt3/train_ppo.py`

### __init__ (method) `def __init__(self, policy_model, tokenizer, device, decode)`
- Defined: `topogpt3/rollout.py:51`
- Imported by: `tests/test_heritage.py`, `topogpt3/__init__.py`, `topogpt3/train_grpo.py`, `topogpt3/train_ppo.py`

### rollout (method) `def rollout(self, prompt_ids, num_generations, max_new_tokens, temperature, tokenizer)`
- Defined: `topogpt3/rollout.py:57`
- Imported by: `tests/test_heritage.py`, `topogpt3/__init__.py`, `topogpt3/train_grpo.py`, `topogpt3/train_ppo.py`

### update_policy (method) `def update_policy(self, model)`
- Defined: `topogpt3/rollout.py:79`
- Imported by: `tests/test_heritage.py`, `topogpt3/__init__.py`, `topogpt3/train_grpo.py`, `topogpt3/train_ppo.py`

## topogpt3/tools_agent.py

### execute_tool (function) `def execute_tool(name, args)`
- Defined: `topogpt3/tools_agent.py:59`
- Depends on: `eval/sandbox.py`, `topogpt3/chat.py`
- Imported by: `tests/test_heritage.py`, `topogpt3/__init__.py`, `topogpt3/eval_toolcall.py`, `topogpt3/train_agent.py`

### rollout_multiturn (function) `def rollout_multiturn(generate_fn, tokenizer, messages, tools, max_turns, max_new_tokens, open_thinking)`
- Defined: `topogpt3/tools_agent.py:80`
- Doc: generate_fn(prompt_text)->text. Returns (full_text, tool_trace).
- Depends on: `eval/sandbox.py`, `topogpt3/chat.py`
- Imported by: `tests/test_heritage.py`, `topogpt3/__init__.py`, `topogpt3/eval_toolcall.py`, `topogpt3/train_agent.py`

## topogpt3/train.py

### _gauss_complex_contract (method) `def _gauss_complex_contract(self, W, X)`
- Defined: `topogpt3/train.py:532`
- Doc: Sustituye QuaternionSpectralLayer._contract usando el truco de Gauss.
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/export_chat.py`

### apply_gauss_patch (method) `def apply_gauss_patch(logger)`
- Defined: `topogpt3/train.py:568`
- Doc: Activa la version Gauss de _contract en QuaternionSpectralLayer.
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/export_chat.py`

### parse_args (method) `def parse_args()`
- Defined: `topogpt3/train.py:1538`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/export_chat.py`

### main (method) `def main()`
- Defined: `topogpt3/train.py:1567`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/export_chat.py`

### build_topogpt2_config (method) `def build_topogpt2_config(self, max_seq_len, attn_window)`
- Defined: `topogpt3/train.py:170`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/export_chat.py`

### __init__ (method) `def __init__(self, config, logger)`
- Defined: `topogpt3/train.py:217`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/export_chat.py`

### _stack_spectral_kernels (method) `def _stack_spectral_kernels(model)`
- Defined: `topogpt3/train.py:231`
- Doc: Devuelve K(theta) en C^{N_f x N_c}:
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/export_chat.py`

### _elbow_rank (method) `def _elbow_rank(self, sigmas)`
- Defined: `topogpt3/train.py:268`
- Doc: Punto donde el valor singular cae por debajo de elbow_ratio * sigma_max.
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/export_chat.py`

### _dominant_subspace (method) `def _dominant_subspace(self, K)`
- Defined: `topogpt3/train.py:277`
- Doc: SVD compacta y truncada.
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/export_chat.py`

### _flatten_grads (method) `def _flatten_grads(model, max_per_tensor)`
- Defined: `topogpt3/train.py:295`
- Doc: Concatena un sub-sample de gradientes para mantener costo acotado.
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/export_chat.py`

### estimate_fisher_gap (method) `def estimate_fisher_gap(self, model, dataloader, vocab_size, r_target)`
- Defined: `topogpt3/train.py:313`
- Doc: Sigma_F ~= (1/M) sum_m g_m g_m^T  (covarianza muestral de gradientes).
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/export_chat.py`

### _project_unitary (method) `def _project_unitary(M)`
- Defined: `topogpt3/train.py:381`
- Doc: Proyeccion a U(r) por descomposicion polar (M ~= U H -> retorna U).
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/export_chat.py`

### update_holonomy (method) `def update_holonomy(self, U_new)`
- Defined: `topogpt3/train.py:386`
- Doc: Holonomia discreta:
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/export_chat.py`

### conjugation_distance_su2 (method) `def conjugation_distance_su2(U1, U2)`
- Defined: `topogpt3/train.py:412`
- Doc: Para U1, U2 en U(1)/U(2):  d_conj(U1, U2) = min_g || U1 - g U2 g^{-1} ||_F.
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/export_chat.py`

### _accumulate_winding (method) `def _accumulate_winding(self, U_new)`
- Defined: `topogpt3/train.py:429`
- Doc: W += (1/2pi) * arg det <U_prev | U_new>  acumulado sobre la trayectoria.
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/export_chat.py`

### snapshot (method) `def snapshot(self, model, step, dataloader, vocab_size)`
- Defined: `topogpt3/train.py:445`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/export_chat.py`

### format_log (method) `def format_log(self, snap)`
- Defined: `topogpt3/train.py:500`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/export_chat.py`

### save (method) `def save(self, path)`
- Defined: `topogpt3/train.py:522`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/export_chat.py`

### __init__ (method) `def __init__(self, model, config, logger, gauss_enabled)`
- Defined: `topogpt3/train.py:600`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/export_chat.py`

### _embed_params (method) `def _embed_params(model)`
- Defined: `topogpt3/train.py:611`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/export_chat.py`

### measure_throughput (method) `def measure_throughput(self, dataloader, vocab_size)`
- Defined: `topogpt3/train.py:619`
- Doc: Devuelve (tokens_por_segundo, segundos_por_step).
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/export_chat.py`

### estimate_flops_per_step (method) `def estimate_flops_per_step(self, batch_size, seq_len)`
- Defined: `topogpt3/train.py:651`
- Doc: Heuristica: 6 * N_no_embed * tokens (forward + backward).
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/export_chat.py`

### estimate_bytes_per_step (method) `def estimate_bytes_per_step(self, batch_size, seq_len, dtype_bytes)`
- Defined: `topogpt3/train.py:656`
- Doc: Bandwidth aproximada: lectura de pesos + activaciones por step.
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/export_chat.py`

### compute (method) `def compute(self, dataloader, vocab_size, val_loss, val_ppl, val_acc, batch_size, seq_len)`
- Defined: `topogpt3/train.py:664`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/export_chat.py`

### format_log (method) `def format_log(self, m)`
- Defined: `topogpt3/train.py:696`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/export_chat.py`

### __init__ (method) `def __init__(self, config, tokenizer, logger)`
- Defined: `topogpt3/train.py:729`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/export_chat.py`

### _format_codealpaca (method) `def _format_codealpaca(ex)`
- Defined: `topogpt3/train.py:746`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/export_chat.py`

### _format_code_feedback (method) `def _format_code_feedback(ex)`
- Defined: `topogpt3/train.py:757`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/export_chat.py`

### _format_magicoder (method) `def _format_magicoder(ex)`
- Defined: `topogpt3/train.py:777`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/export_chat.py`

### _format_tiny_stack (method) `def _format_tiny_stack(ex)`
- Defined: `topogpt3/train.py:785`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/export_chat.py`

### _get_formatter (method) `def _get_formatter(cls, tier)`
- Defined: `topogpt3/train.py:797`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/export_chat.py`

### _tier_paths (method) `def _tier_paths(self, tier)`
- Defined: `topogpt3/train.py:819`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/export_chat.py`

### _manifest_path (method) `def _manifest_path(self, tier)`
- Defined: `topogpt3/train.py:825`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/export_chat.py`

### _already_prepared (method) `def _already_prepared(self, tier)`
- Defined: `topogpt3/train.py:828`
- Doc: True solo si los 3 splits existen, son no-vacios y el manifest concuerda.
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/export_chat.py`

### _load_hf_with_fallback (method) `def _load_hf_with_fallback(self, tier)`
- Defined: `topogpt3/train.py:858`
- Doc: Carga el dataset HF; para tiny_the_stack prueba una cadena de fallbacks
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/export_chat.py`

### prepare_tier (method) `def prepare_tier(self, tier_index, force)`
- Defined: `topogpt3/train.py:891`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/export_chat.py`

### open_memmap (method) `def open_memmap(self, tier, split)`
- Defined: `topogpt3/train.py:986`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/export_chat.py`

### __init__ (method) `def __init__(self, tokens, seq_len)`
- Defined: `topogpt3/train.py:1006`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/export_chat.py`

### __len__ (method) `def __len__(self)`
- Defined: `topogpt3/train.py:1011`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/export_chat.py`

### __getitem__ (method) `def __getitem__(self, idx)`
- Defined: `topogpt3/train.py:1014`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/export_chat.py`

### __init__ (method) `def __init__(self, root, max_keep, logger)`
- Defined: `topogpt3/train.py:1030`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/export_chat.py`

### save (method) `def save(self, tag, model, optimizer, state)`
- Defined: `topogpt3/train.py:1037`
- Doc: Guarda checkpoint atomico en <root>/last/ sobreescribiendo el anterior.
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/export_chat.py`

### load_latest (method) `def load_latest(self, model, optimizer)`
- Defined: `topogpt3/train.py:1071`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/export_chat.py`

### should_save (method) `def should_save(self, interval_min)`
- Defined: `topogpt3/train.py:1095`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/export_chat.py`

### __init__ (method) `def __init__(self, config, start_tier)`
- Defined: `topogpt3/train.py:1119`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/export_chat.py`

### prepare_all (method) `def prepare_all(self, force)`
- Defined: `topogpt3/train.py:1174`
- Doc: Prepara cada tier; un fallo en uno no detiene los demas.
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/export_chat.py`

### _build_loaders (method) `def _build_loaders(self, tier_index)`
- Defined: `topogpt3/train.py:1190`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/export_chat.py`

### _cosine_lr (method) `def _cosine_lr(self, step, total_steps)`
- Defined: `topogpt3/train.py:1222`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/export_chat.py`

### _set_lr (method) `def _set_lr(self, lr)`
- Defined: `topogpt3/train.py:1229`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/export_chat.py`

### _train_one_tier (method) `def _train_one_tier(self, tier_index)`
- Defined: `topogpt3/train.py:1237`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/export_chat.py`

### _evaluate (method) `def _evaluate(self, dl)`
- Defined: `topogpt3/train.py:1398`
- Doc: Devuelve (avg_loss, perplexity, token_accuracy).
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/export_chat.py`

### _state_dict (method) `def _state_dict(self)`
- Defined: `topogpt3/train.py:1436`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/export_chat.py`

### run (method) `def run(self)`
- Defined: `topogpt3/train.py:1449`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/export_chat.py`

### _eval_combined_holdout (method) `def _eval_combined_holdout(self)`
- Defined: `topogpt3/train.py:1506`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/export_chat.py`

### flush (method) `def flush(split)`
- Defined: `topogpt3/train.py:922`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/export_chat.py`

## topogpt3/train_agent.py

### agent_reward (function) `def agent_reward(text, gt, used_tools)`
- Defined: `topogpt3/train_agent.py:31`
- Depends on: `topogpt3/chat.py`, `topogpt3/model.py`, `topogpt3/rewards.py`, `topogpt3/tools_agent.py`, `topogpt3/trainer_utils_topo.py`
- Imported by: `topogpt3/__main__.py`

### main (function) `def main()`
- Defined: `topogpt3/train_agent.py:43`
- Depends on: `topogpt3/chat.py`, `topogpt3/model.py`, `topogpt3/rewards.py`, `topogpt3/tools_agent.py`, `topogpt3/trainer_utils_topo.py`
- Imported by: `topogpt3/__main__.py`

## topogpt3/train_distill.py

### main (function) `def main()`
- Defined: `topogpt3/train_distill.py:24`
- Depends on: `topogpt3/model.py`, `topogpt3/rewards.py`, `topogpt3/trainer_utils_topo.py`
- Imported by: `topogpt3/__main__.py`

## topogpt3/train_dpo.py

### load_model (function) `def load_model(checkpoint, device)`
- Defined: `topogpt3/train_dpo.py:24`
- Depends on: `topogpt3/model.py`, `topogpt3/rewards.py`, `topogpt3/trainer_utils_topo.py`
- Imported by: `topogpt3/__main__.py`

### main (function) `def main()`
- Defined: `topogpt3/train_dpo.py:33`
- Depends on: `topogpt3/model.py`, `topogpt3/rewards.py`, `topogpt3/trainer_utils_topo.py`
- Imported by: `topogpt3/__main__.py`

## topogpt3/train_grpo.py

### main (function) `def main()`
- Defined: `topogpt3/train_grpo.py:29`
- Depends on: `topogpt3/model.py`, `topogpt3/rewards.py`, `topogpt3/rollout.py`, `topogpt3/trainer_utils_topo.py`
- Imported by: `topogpt3/__main__.py`

### _gather (function) `def _gather(lg, _plen, _R, _comp)`
- Defined: `topogpt3/train_grpo.py:88`
- Depends on: `topogpt3/model.py`, `topogpt3/rewards.py`, `topogpt3/rollout.py`, `topogpt3/trainer_utils_topo.py`
- Imported by: `topogpt3/__main__.py`

## topogpt3/train_lora.py

### load_base (function) `def load_base(checkpoint, device)`
- Defined: `topogpt3/train_lora.py:25`
- Depends on: `topogpt3/lora.py`, `topogpt3/model.py`, `topogpt3/trainer_utils_topo.py`
- Imported by: `topogpt3/__main__.py`

### main (function) `def main()`
- Defined: `topogpt3/train_lora.py:36`
- Depends on: `topogpt3/lora.py`, `topogpt3/model.py`, `topogpt3/trainer_utils_topo.py`
- Imported by: `topogpt3/__main__.py`

## topogpt3/train_ppo.py

### main (method) `def main()`
- Defined: `topogpt3/train_ppo.py:45`
- Depends on: `topogpt3/model.py`, `topogpt3/rewards.py`, `topogpt3/rollout.py`, `topogpt3/trainer_utils_topo.py`
- Imported by: `topogpt3/__main__.py`

### __init__ (method) `def __init__(self, trunk)`
- Defined: `topogpt3/train_ppo.py:30`
- Depends on: `topogpt3/model.py`, `topogpt3/rewards.py`, `topogpt3/rollout.py`, `topogpt3/trainer_utils_topo.py`
- Imported by: `topogpt3/__main__.py`

### forward (method) `def forward(self, ids)`
- Defined: `topogpt3/train_ppo.py:36`
- Depends on: `topogpt3/model.py`, `topogpt3/rewards.py`, `topogpt3/rollout.py`, `topogpt3/trainer_utils_topo.py`
- Imported by: `topogpt3/__main__.py`

## topogpt3/trainer_utils_topo.py

### Logger (function) `def Logger(content, quiet)`
- Defined: `topogpt3/trainer_utils_topo.py:20`
- Imported by: `topogpt3/__init__.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### is_main_process (function) `def is_main_process()`
- Defined: `topogpt3/trainer_utils_topo.py:25`
- Imported by: `topogpt3/__init__.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### get_lr (function) `def get_lr(current_step, total_steps, lr)`
- Defined: `topogpt3/trainer_utils_topo.py:29`
- Imported by: `topogpt3/__init__.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### setup_seed (function) `def setup_seed(seed)`
- Defined: `topogpt3/trainer_utils_topo.py:34`
- Imported by: `topogpt3/__init__.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### init_distributed_mode (function) `def init_distributed_mode()`
- Defined: `topogpt3/trainer_utils_topo.py:43`
- Imported by: `topogpt3/__init__.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### topo_checkpoint (method) `def topo_checkpoint(save_dir, weight, model, optimizer, scheduler, scaler, epoch, step, wandb, extra)`
- Defined: `topogpt3/trainer_utils_topo.py:77`
- Doc: Atomic double-save: fp16 weights + resume state (weights + optim).
- Imported by: `topogpt3/__init__.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### __init__ (method) `def __init__(self, sampler, batch_size, skip_batches)`
- Defined: `topogpt3/trainer_utils_topo.py:53`
- Imported by: `topogpt3/__init__.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### __iter__ (method) `def __iter__(self)`
- Defined: `topogpt3/trainer_utils_topo.py:58`
- Imported by: `topogpt3/__init__.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

### __len__ (method) `def __len__(self)`
- Defined: `topogpt3/trainer_utils_topo.py:72`
- Imported by: `topogpt3/__init__.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`

## topogpt3/yarn.py

### yarn_scale_inv_freq (method) `def yarn_scale_inv_freq(inv_freq, d_head, cfg)`
- Defined: `topogpt3/yarn.py:26`
- Doc: Apply NTK-by-parts ramp to inv_freq.
- Imported by: `tests/test_heritage.py`, `topogpt3/__init__.py`, `topogpt3/model.py`

### apply_yarn_to_rope (method) `def apply_yarn_to_rope(rope_module, cfg)`
- Defined: `topogpt3/yarn.py:50`
- Doc: Patch an existing RotaryEmbedding in-place + rebuild cache.
- Imported by: `tests/test_heritage.py`, `topogpt3/__init__.py`, `topogpt3/model.py`
