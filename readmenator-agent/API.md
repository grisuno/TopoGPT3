# API

## app.py

### run_inference `def run_inference(prompt, checkpoint_dir, checkpoint_name, max_new_tokens, temperature, top_k, repetition_penalty, device)`
- Defined: `app.py:46`
- Doc: Run the standard sampler and return the generated completion text.
- Depends on: `topogpt3/__init__.py`

### run_inference_hrm `def run_inference_hrm(prompt, checkpoint_dir, checkpoint_name, max_new_tokens, temperature, top_k, repetition_penalty, high_level_iters, low_level_iters, low_level_window, device)`
- Defined: `app.py:71`
- Doc: Run the hierarchical recursive sampler and return the completion.
- Depends on: `topogpt3/__init__.py`

### run_training `def run_training(scale, start_tier, device, prepare_data)`
- Defined: `app.py:105`
- Doc: Run the full TopoGPT3 curriculum trainer.
- Depends on: `topogpt3/__init__.py`

### _build_parser `def _build_parser()`
- Defined: `app.py:121`
- Doc: Build the top-level CLI for this entry point script.
- Depends on: `topogpt3/__init__.py`

### main `def main(argv)`
- Defined: `app.py:159`
- Doc: Entry point invoked when the file is executed as a script.
- Depends on: `topogpt3/__init__.py`

## convert_weights.py

### convert `def convert(input_path, output_path)`
- Defined: `convert_weights.py:102`

### main `def main()`
- Defined: `convert_weights.py:160`

## convert_weights_minios.py

### main `def main()`
- Defined: `convert_weights_minios.py:85`

## encode_tokens.py

### main `def main()`
- Defined: `encode_tokens.py:19`

## eval/analyze.py

### pass_at_k `def pass_at_k(n, c, k)`
- Defined: `eval/analyze.py:21`
- Doc: Unbiased estimator from the HumanEval paper.

### classify_error `def classify_error(msg, candidate_src)`
- Defined: `eval/analyze.py:32`
- Doc: Heuristic single-label error classifier.

### load_jsonl `def load_jsonl(path)`
- Defined: `eval/analyze.py:56`

### summarize `def summarize(paths)`
- Defined: `eval/analyze.py:61`

### main `def main()`
- Defined: `eval/analyze.py:103`

## eval/analyze_results.py

### load_records `def load_records(path)`
- Defined: `eval/analyze_results.py:26`

### summarize `def summarize(records)`
- Defined: `eval/analyze_results.py:31`

### show_failures `def show_failures(records, task_id)`
- Defined: `eval/analyze_results.py:44`

### main `def main()`
- Defined: `eval/analyze_results.py:82`

## eval/diag_static.py

### phase_discretization `def phase_discretization(K, n_samples, seed)`
- Defined: `eval/diag_static.py:49`
- Doc: Muestrea n_samples overlaps aleatorios <u_i | u_j> sobre los vectores
- Depends on: `topogpt3.c`, `topogpt3/model.py`, `topogpt3/train.py`

### synthetic_winding `def synthetic_winding(K, n_windows, window_size)`
- Defined: `eval/diag_static.py:95`
- Doc: Como el checkpoint es estatico, no hay trayectoria temporal.
- Depends on: `topogpt3.c`, `topogpt3/model.py`, `topogpt3/train.py`

### static_kappa `def static_kappa(K)`
- Defined: `eval/diag_static.py:144`
- Depends on: `topogpt3.c`, `topogpt3/model.py`, `topogpt3/train.py`

### context_length_diagnostic `def context_length_diagnostic(model, tracker, device, lengths)`
- Defined: `eval/diag_static.py:171`
- Depends on: `topogpt3.c`, `topogpt3/model.py`, `topogpt3/train.py`

### main `def main()`
- Defined: `eval/diag_static.py:248`
- Depends on: `topogpt3.c`, `topogpt3/model.py`, `topogpt3/train.py`

## eval/governor.py

### make_loop_detector `def make_loop_detector(window, min_repeats)`
- Defined: `eval/governor.py:285`
- Doc: Return True if the last `window` tokens contain a sub-sequence
- Imported by: `eval/governor_smoke.py`

### make_timeout_hook `def make_timeout_hook(per_token_s)`
- Defined: `eval/governor.py:314`
- Doc: Return True if the per-token wall time exceeds `per_token_s`.
- Imported by: `eval/governor_smoke.py`

### __init__ `def __init__(self)`
- Defined: `eval/governor.py:56`
- Imported by: `eval/governor_smoke.py`

### put `def put(self, tok)`
- Defined: `eval/governor.py:62`
- Imported by: `eval/governor_smoke.py`

### mark_done `def mark_done(self)`
- Defined: `eval/governor.py:67`
- Imported by: `eval/governor_smoke.py`

### drain `def drain(self)`
- Defined: `eval/governor.py:72`
- Doc: Return all tokens emitted so far, atomic snapshot.
- Imported by: `eval/governor_smoke.py`

### wait_for_new `def wait_for_new(self, timeout)`
- Defined: `eval/governor.py:77`
- Doc: Block up to `timeout` seconds for a new token. Returns True
- Imported by: `eval/governor_smoke.py`

### is_closed `def is_closed(self)`
- Defined: `eval/governor.py:86`
- Imported by: `eval/governor_smoke.py`

### __len__ `def __len__(self)`
- Defined: `eval/governor.py:90`
- Imported by: `eval/governor_smoke.py`

### __post_init__ `def __post_init__(self)`
- Defined: `eval/governor.py:117`
- Imported by: `eval/governor_smoke.py`

### __init__ `def __init__(self, model, ctx, stream, max_new_tokens, temperature, top_k, repetition_penalty, max_seq_len)`
- Defined: `eval/governor.py:156`
- Imported by: `eval/governor_smoke.py`

### cancel `def cancel(self)`
- Defined: `eval/governor.py:177`
- Doc: Asynchronously stop the generation. Safe to call from any
- Imported by: `eval/governor_smoke.py`

### _should_cancel `def _should_cancel(self)`
- Defined: `eval/governor.py:182`
- Imported by: `eval/governor_smoke.py`

### run `def run(self, stop_hooks)`
- Defined: `eval/governor.py:185`
- Doc: Execute the generation loop. Returns when the model emits
- Imported by: `eval/governor_smoke.py`

### hook `def hook(generated)`
- Defined: `eval/governor.py:292`
- Imported by: `eval/governor_smoke.py`

### hook `def hook(generated)`
- Defined: `eval/governor.py:320`
- Imported by: `eval/governor_smoke.py`

## eval/governor_smoke.py

### load_model `def load_model()`
- Defined: `eval/governor_smoke.py:30`
- Depends on: `eval/governor.py`, `topogpt3.c`

### test_tokenstream_threadsafety `def test_tokenstream_threadsafety()`
- Defined: `eval/governor_smoke.py:49`
- Depends on: `eval/governor.py`, `topogpt3.c`

### test_governor_basic `def test_governor_basic()`
- Defined: `eval/governor_smoke.py:79`
- Depends on: `eval/governor.py`, `topogpt3.c`

### test_loop_detector `def test_loop_detector()`
- Defined: `eval/governor_smoke.py:98`
- Depends on: `eval/governor.py`, `topogpt3.c`

### test_cancel `def test_cancel()`
- Defined: `eval/governor_smoke.py:118`
- Depends on: `eval/governor.py`, `topogpt3.c`

### producer `def producer()`
- Defined: `eval/governor_smoke.py:53`
- Depends on: `eval/governor.py`, `topogpt3.c`

### consumer `def consumer()`
- Defined: `eval/governor_smoke.py:59`
- Depends on: `eval/governor.py`, `topogpt3.c`

## eval/harness.py

### load_humaneval `def load_humaneval(cache_dir)`
- Defined: `eval/harness.py:59`
- Depends on: `eval/samplers.py`, `eval/sandbox.py`, `topogpt3.c`
- Imported by: `eval/integration_smoke.py`, `eval/noise_sweep.py`, `eval/temp_sweep.py`

### build_prompt `def build_prompt(problem)`
- Defined: `eval/harness.py:75`
- Doc: Return the exact prompt text fed to the model.
- Depends on: `eval/samplers.py`, `eval/sandbox.py`, `topogpt3.c`
- Imported by: `eval/integration_smoke.py`, `eval/noise_sweep.py`, `eval/temp_sweep.py`

### extract_candidate `def extract_candidate(prompt, completion)`
- Defined: `eval/harness.py:100`
- Doc: Combine prompt + completion into a single Python source string.
- Depends on: `eval/samplers.py`, `eval/sandbox.py`, `topogpt3.c`
- Imported by: `eval/integration_smoke.py`, `eval/noise_sweep.py`, `eval/temp_sweep.py`

### run_one_test `def run_one_test(problem, candidate_src, timeout)`
- Defined: `eval/harness.py:150`
- Doc: Execute the candidate against the hidden test.
- Depends on: `eval/samplers.py`, `eval/sandbox.py`, `topogpt3.c`
- Imported by: `eval/integration_smoke.py`, `eval/noise_sweep.py`, `eval/temp_sweep.py`

### run_one_test_sandboxed `def run_one_test_sandboxed(problem, candidate_src, timeout, sandbox_cfg)`
- Defined: `eval/harness.py:172`
- Doc: Sandboxed variant of `run_one_test`. Runs the candidate in a
- Depends on: `eval/samplers.py`, `eval/sandbox.py`, `topogpt3.c`
- Imported by: `eval/integration_smoke.py`, `eval/noise_sweep.py`, `eval/temp_sweep.py`

### make_sampler `def make_sampler(mode, settings_kwargs)`
- Defined: `eval/harness.py:195`
- Doc: Backwards-compatible shim. The real implementation lives in
- Depends on: `eval/samplers.py`, `eval/sandbox.py`, `topogpt3.c`
- Imported by: `eval/integration_smoke.py`, `eval/noise_sweep.py`, `eval/temp_sweep.py`

### completion_for_problem `def completion_for_problem(sampler, prompt)`
- Defined: `eval/harness.py:204`
- Doc: Run a single completion and return (raw_output_text, metrics_dict).
- Depends on: `eval/samplers.py`, `eval/sandbox.py`, `topogpt3.c`
- Imported by: `eval/integration_smoke.py`, `eval/noise_sweep.py`, `eval/temp_sweep.py`

### evaluate_problem `def evaluate_problem(problem, loader, args, sample_idx)`
- Defined: `eval/harness.py:272`
- Depends on: `eval/samplers.py`, `eval/sandbox.py`, `topogpt3.c`
- Imported by: `eval/integration_smoke.py`, `eval/noise_sweep.py`, `eval/temp_sweep.py`

### main `def main()`
- Defined: `eval/harness.py:315`
- Depends on: `eval/samplers.py`, `eval/sandbox.py`, `topogpt3.c`
- Imported by: `eval/integration_smoke.py`, `eval/noise_sweep.py`, `eval/temp_sweep.py`

### __init__ `def __init__(self, ckpt_dir, ckpt_name, device)`
- Defined: `eval/harness.py:220`
- Depends on: `eval/samplers.py`, `eval/sandbox.py`, `topogpt3.c`
- Imported by: `eval/integration_smoke.py`, `eval/noise_sweep.py`, `eval/temp_sweep.py`

### generate `def generate(self, prompt, max_new_tokens, temperature, top_k, repetition_penalty)`
- Defined: `eval/harness.py:246`
- Depends on: `eval/samplers.py`, `eval/sandbox.py`, `topogpt3.c`
- Imported by: `eval/integration_smoke.py`, `eval/noise_sweep.py`, `eval/temp_sweep.py`

## eval/integration_smoke.py

### main `def main()`
- Defined: `eval/integration_smoke.py:18`
- Depends on: `eval/harness.py`

## eval/noise_analysis.py

### _load `def _load(p)`
- Defined: `eval/noise_analysis.py:43`

### consistency_across_runs `def consistency_across_runs(per_run)`
- Defined: `eval/noise_analysis.py:47`
- Doc: Para cada problema, mira si pasa consistentemente a traves de los

### main `def main()`
- Defined: `eval/noise_analysis.py:83`

## eval/noise_sweep.py

### inject_noise `def inject_noise(model, sigma, seed)`
- Defined: `eval/noise_sweep.py:46`
- Doc: Anade N(0, sigma) a TODOS los kernels espectrales (kr_*, ki_*).
- Depends on: `eval/harness.py`, `topogpt3.c`, `topogpt3/model.py`
- Imported by: `eval/temp_sweep.py`

### load_model `def load_model(ckpt_dir, ckpt_name, device)`
- Defined: `eval/noise_sweep.py:74`
- Doc: Reconstruye TopoGPT2 alineado con el checkpoint, sin acceso a
- Depends on: `eval/harness.py`, `topogpt3.c`, `topogpt3/model.py`
- Imported by: `eval/temp_sweep.py`

### generate_one `def generate_one(model, tok, prompt, max_new_tokens, device)`
- Defined: `eval/noise_sweep.py:99`
- Depends on: `eval/harness.py`, `topogpt3.c`, `topogpt3/model.py`
- Imported by: `eval/temp_sweep.py`

### main `def main()`
- Defined: `eval/noise_sweep.py:117`
- Depends on: `eval/harness.py`, `topogpt3.c`, `topogpt3/model.py`
- Imported by: `eval/temp_sweep.py`

## eval/repair.py

### _new_loader `def _new_loader(ckpt_dir, ckpt_name)`
- Defined: `eval/repair.py:36`
- Depends on: `topogpt3.c`

### extract_candidate `def extract_candidate(prompt, completion)`
- Defined: `eval/repair.py:49`
- Depends on: `topogpt3.c`

### run_test `def run_test(problem, candidate_src)`
- Defined: `eval/repair.py:75`
- Depends on: `topogpt3.c`

### build_repair_prompt `def build_repair_prompt(prompt, candidate, err, entry_point)`
- Defined: `eval/repair.py:89`
- Depends on: `topogpt3.c`

### gen `def gen(model, tok, text, max_new_tokens, temperature, top_k, rep_penalty)`
- Defined: `eval/repair.py:104`
- Depends on: `topogpt3.c`

### main `def main()`
- Defined: `eval/repair.py:119`
- Depends on: `topogpt3.c`

## eval/report.py

### pass_at_k `def pass_at_k(n, c, k)`
- Defined: `eval/report.py:25`

### classify_error `def classify_error(msg)`
- Defined: `eval/report.py:31`

### load_jsonl `def load_jsonl(p)`
- Defined: `eval/report.py:52`

### summarize_run `def summarize_run(p)`
- Defined: `eval/report.py:56`

### repair_summary `def repair_summary(repair_path, baseline_path)`
- Defined: `eval/report.py:90`

### main `def main()`
- Defined: `eval/report.py:117`

## eval/samplers.py

### register_sampler `def register_sampler(name)`
- Defined: `eval/samplers.py:36`
- Doc: Decorator. Register a factory under `name`. If `enabled_env` is set,
- Depends on: `topogpt3.c`
- Imported by: `eval/harness.py`, `eval/harness.py`

### _is_env_truthy `def _is_env_truthy(name)`
- Defined: `eval/samplers.py:55`
- Depends on: `topogpt3.c`
- Imported by: `eval/harness.py`, `eval/harness.py`

### _make_standard `def _make_standard(settings_kwargs)`
- Defined: `eval/samplers.py:64`
- Depends on: `topogpt3.c`
- Imported by: `eval/harness.py`, `eval/harness.py`

### _make_hrm `def _make_hrm(settings_kwargs)`
- Defined: `eval/samplers.py:69`
- Depends on: `topogpt3.c`
- Imported by: `eval/harness.py`, `eval/harness.py`

### list_samplers `def list_samplers()`
- Defined: `eval/samplers.py:86`
- Depends on: `topogpt3.c`
- Imported by: `eval/harness.py`, `eval/harness.py`

### build_sampler `def build_sampler(mode, settings_kwargs)`
- Defined: `eval/samplers.py:90`
- Doc: Construct a sampler. Drop-in replacement for the old
- Depends on: `topogpt3.c`
- Imported by: `eval/harness.py`, `eval/harness.py`

### deco `def deco(fn)`
- Defined: `eval/samplers.py:42`
- Depends on: `topogpt3.c`
- Imported by: `eval/harness.py`, `eval/harness.py`

## eval/sandbox.py

### _names_imported `def _names_imported(tree)`
- Defined: `eval/sandbox.py:100`
- Doc: Return the set of top-level names brought into scope by imports.
- Imported by: `eval/harness.py`, `eval/sandbox_smoke.py`

### _blocked_dunder_access `def _blocked_dunder_access(tree, blocked)`
- Defined: `eval/sandbox.py:114`
- Doc: Find Attribute nodes whose attr is in `blocked`. Returns attr names found.
- Imported by: `eval/harness.py`, `eval/sandbox_smoke.py`

### _max_depth `def _max_depth(tree)`
- Defined: `eval/sandbox.py:123`
- Doc: Compute max nesting depth of the AST. Catches obfuscated huge trees.
- Imported by: `eval/harness.py`, `eval/sandbox_smoke.py`

### check_safety `def check_safety(source, cfg)`
- Defined: `eval/sandbox.py:133`
- Doc: Return (ok, reason). `reason` is "" when ok, else a human-readable
- Imported by: `eval/harness.py`, `eval/sandbox_smoke.py`

### _build_worker_src `def _build_worker_src(allowed_builtin_names, program_src, blocked_modules)`
- Defined: `eval/sandbox.py:254`
- Imported by: `eval/harness.py`, `eval/sandbox_smoke.py`

### safe_exec `def safe_exec(program_src, cfg, extra_globals)`
- Defined: `eval/sandbox.py:270`
- Doc: Execute `program_src` in a sandboxed child process. Returns the same
- Imported by: `eval/harness.py`, `eval/sandbox_smoke.py`

### describe_policy `def describe_policy(cfg)`
- Defined: `eval/sandbox.py:373`
- Imported by: `eval/harness.py`, `eval/sandbox_smoke.py`

### d `def d(node, cur)`
- Defined: `eval/sandbox.py:125`
- Imported by: `eval/harness.py`, `eval/sandbox_smoke.py`

## eval/sandbox_smoke.py

### main `def main()`
- Defined: `eval/sandbox_smoke.py:15`
- Depends on: `eval/sandbox.py`

## eval/smoke.py

### run_standard `def run_standard()`
- Defined: `eval/smoke.py:17`
- Depends on: `topogpt3.c`

### run_hrm `def run_hrm()`
- Defined: `eval/smoke.py:36`
- Depends on: `topogpt3.c`

## eval/temp_sweep.py

### generate_one `def generate_one(model, tok, prompt, max_new_tokens, temperature, top_k, device, seed_offset)`
- Defined: `eval/temp_sweep.py:39`
- Depends on: `eval/harness.py`, `eval/noise_sweep.py`

### evaluate_problems `def evaluate_problems(model, tok, problems, max_new_tokens, temperature, top_k, n_samples, device)`
- Defined: `eval/temp_sweep.py:58`
- Depends on: `eval/harness.py`, `eval/noise_sweep.py`

### pass_at_k_unbiased `def pass_at_k_unbiased(n, c, k)`
- Defined: `eval/temp_sweep.py:88`
- Depends on: `eval/harness.py`, `eval/noise_sweep.py`

### summarize `def summarize(results, n_samples)`
- Defined: `eval/temp_sweep.py:96`
- Depends on: `eval/harness.py`, `eval/noise_sweep.py`

### main `def main()`
- Defined: `eval/temp_sweep.py:116`
- Depends on: `eval/harness.py`, `eval/noise_sweep.py`

## gradio_app.py

### ensure_checkpoint `def ensure_checkpoint()`
- Defined: `gradio_app.py:35`
- Doc: Return the path to the checkpoint directory, downloading if needed.
- Depends on: `topogpt3/__init__.py`

### run_standard_inference `def run_standard_inference(prompt, max_new_tokens, temperature, top_k, repetition_penalty, auto_continue)`
- Defined: `gradio_app.py:59`
- Doc: Run standard autoregressive inference.
- Depends on: `topogpt3/__init__.py`

### run_hrm_inference `def run_hrm_inference(prompt, max_new_tokens, temperature, top_k, repetition_penalty, high_level_iters, low_level_iters, low_level_window, thinking, auto_continue)`
- Defined: `gradio_app.py:95`
- Doc: Run hierarchical recursive reasoning inference.
- Depends on: `topogpt3/__init__.py`

### build_ui `def build_ui()`
- Defined: `gradio_app.py:144`
- Doc: Construct the Gradio Blocks interface.
- Depends on: `topogpt3/__init__.py`

## synthetic_dataset.py

### build_backend `def build_backend(provider, model)`
- Defined: `synthetic_dataset.py:227`
- Doc: Factory for LLM backends.
- Imported by: `topogpt3/model.py`

### validate_sample `def validate_sample(sample)`
- Defined: `synthetic_dataset.py:330`
- Doc: Validate that a generated sample meets quality bar.
- Imported by: `topogpt3/model.py`

### build_logger `def build_logger(level)`
- Defined: `synthetic_dataset.py:614`
- Imported by: `topogpt3/model.py`

### parse_args `def parse_args()`
- Defined: `synthetic_dataset.py:625`
- Imported by: `topogpt3/model.py`

### load_paths `def load_paths(paths_arg, paths_file, max_files)`
- Defined: `synthetic_dataset.py:652`
- Doc: Load file paths from CLI args or file.
- Imported by: `topogpt3/model.py`

### main `def main()`
- Defined: `synthetic_dataset.py:667`
- Imported by: `topogpt3/model.py`

### generate `def generate(self, prompt)`
- Defined: `synthetic_dataset.py:64`
- Imported by: `topogpt3/model.py`

### name `def name(self)`
- Defined: `synthetic_dataset.py:67`
- Imported by: `topogpt3/model.py`

### __init__ `def __init__(self, model, api_key, max_tokens, temperature, timeout)`
- Defined: `synthetic_dataset.py:78`
- Imported by: `topogpt3/model.py`

### name `def name(self)`
- Defined: `synthetic_dataset.py:95`
- Imported by: `topogpt3/model.py`

### generate `def generate(self, prompt)`
- Defined: `synthetic_dataset.py:98`
- Imported by: `topogpt3/model.py`

### __init__ `def __init__(self, model, api_key, max_tokens, temperature, timeout)`
- Defined: `synthetic_dataset.py:132`
- Imported by: `topogpt3/model.py`

### name `def name(self)`
- Defined: `synthetic_dataset.py:151`
- Imported by: `topogpt3/model.py`

### generate `def generate(self, prompt)`
- Defined: `synthetic_dataset.py:154`
- Imported by: `topogpt3/model.py`

### __init__ `def __init__(self, model, host, max_tokens, temperature, timeout)`
- Defined: `synthetic_dataset.py:184`
- Imported by: `topogpt3/model.py`

### name `def name(self)`
- Defined: `synthetic_dataset.py:198`
- Imported by: `topogpt3/model.py`

### generate `def generate(self, prompt)`
- Defined: `synthetic_dataset.py:201`
- Imported by: `topogpt3/model.py`

### load `def load(path)`
- Defined: `synthetic_dataset.py:374`
- Imported by: `topogpt3/model.py`

### save `def save(self, path)`
- Defined: `synthetic_dataset.py:387`
- Imported by: `topogpt3/model.py`

### __init__ `def __init__(self, backend, output_path, manifest_path, logger, max_workers, max_file_chars)`
- Defined: `synthetic_dataset.py:418`
- Imported by: `topogpt3/model.py`

### _jsonl_writer `def _jsonl_writer(self)`
- Defined: `synthetic_dataset.py:447`
- Doc: Background thread that drains the queue and writes JSONL lines.
- Imported by: `topogpt3/model.py`

### _enqueue_sample `def _enqueue_sample(self, sample)`
- Defined: `synthetic_dataset.py:465`
- Imported by: `topogpt3/model.py`

### _flush_writer `def _flush_writer(self)`
- Defined: `synthetic_dataset.py:468`
- Imported by: `topogpt3/model.py`

### _read_file `def _read_file(self, path)`
- Defined: `synthetic_dataset.py:477`
- Doc: Read file content and detect language. Truncate if needed.
- Imported by: `topogpt3/model.py`

### _build_prompt `def _build_prompt(self, content, lang)`
- Defined: `synthetic_dataset.py:490`
- Imported by: `topogpt3/model.py`

### _generate_sample `def _generate_sample(self, content, lang)`
- Defined: `synthetic_dataset.py:496`
- Doc: Call LLM with retry logic.
- Imported by: `topogpt3/model.py`

### process_file `def process_file(self, path)`
- Defined: `synthetic_dataset.py:533`
- Doc: Process a single file. Returns True if a sample was written.
- Imported by: `topogpt3/model.py`

### process_batch `def process_batch(self, paths)`
- Defined: `synthetic_dataset.py:568`
- Doc: Process a batch of files in parallel using thread pool.
- Imported by: `topogpt3/model.py`

### finish `def finish(self)`
- Defined: `synthetic_dataset.py:590`
- Doc: Signal end of processing and flush writer.
- Imported by: `topogpt3/model.py`

## tests/test_jlens.py

### test_basic_mask `def test_basic_mask(self)`
- Defined: `tests/test_jlens.py:20`
- Doc: Scenario: Correct mask for a standard-length prompt.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_too_short_raises `def test_too_short_raises(self)`
- Defined: `tests/test_jlens.py:29`
- Doc: Scenario: Too-short prompt raises ValueError.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_negative_skip_raises `def test_negative_skip_raises(self)`
- Defined: `tests/test_jlens.py:34`
- Doc: Scenario: Negative skip_first raises ValueError.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_all_positions_valid `def test_all_positions_valid(self)`
- Defined: `tests/test_jlens.py:39`
- Doc: Scenario: skip_first=0 includes all but final position.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_exact_minimum_length `def test_exact_minimum_length(self)`
- Defined: `tests/test_jlens.py:45`
- Doc: Scenario: Exact minimum length (skip_first + 2) works.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### model `def model(self)`
- Defined: `tests/test_jlens.py:56`
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_returns_jacobians_for_source_layers `def test_returns_jacobians_for_source_layers(self, model)`
- Defined: `tests/test_jlens.py:63`
- Doc: Scenario: Returns Jacobians for all requested source layers.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_late_layer_jacobian_close_to_identity `def test_late_layer_jacobian_close_to_identity(self, model)`
- Defined: `tests/test_jlens.py:76`
- Doc: Scenario: J_{n_layers-2} has diag ~= 1 (identity property).
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_earlier_layers_further_from_identity `def test_earlier_layers_further_from_identity(self, model)`
- Defined: `tests/test_jlens.py:85`
- Doc: Scenario: Earlier layers compound deviations from identity.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_exact_jacobian_for_last_block `def test_exact_jacobian_for_last_block(self, model)`
- Defined: `tests/test_jlens.py:95`
- Doc: Scenario: J_{n_layers-2} equals I + W_{last} exactly.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_negative_layer_indices `def test_negative_layer_indices(self, model)`
- Defined: `tests/test_jlens.py:110`
- Doc: Scenario: Negative layer indices are normalized correctly.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_out_of_range_layers_rejected `def test_out_of_range_layers_rejected(self, model)`
- Defined: `tests/test_jlens.py:133`
- Doc: Scenario: Out-of-range layers raise ValueError.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_source_below_target_enforced `def test_source_below_target_enforced(self, model)`
- Defined: `tests/test_jlens.py:145`
- Doc: Scenario: source_layers must be below target_layer.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_target_out_of_range_raises `def test_target_out_of_range_raises(self, model)`
- Defined: `tests/test_jlens.py:158`
- Doc: Scenario: target_layer out of range raises ValueError.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### model `def model(self)`
- Defined: `tests/test_jlens.py:176`
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_fit_returns_lens_with_correct_attributes `def test_fit_returns_lens_with_correct_attributes(self, model)`
- Defined: `tests/test_jlens.py:183`
- Doc: Scenario: fit() returns JacobianLens with correct metadata.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_fit_empty_prompts_raises `def test_fit_empty_prompts_raises(self, model)`
- Defined: `tests/test_jlens.py:191`
- Doc: Scenario: No valid prompts raises ValueError.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_fit_skips_short_prompts `def test_fit_skips_short_prompts(self, model)`
- Defined: `tests/test_jlens.py:196`
- Doc: Scenario: Too-short prompts are skipped.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_fit_with_default_source_layers `def test_fit_with_default_source_layers(self, model)`
- Defined: `tests/test_jlens.py:202`
- Doc: Scenario: Default source_layers covers all layers below target.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### model `def model(self)`
- Defined: `tests/test_jlens.py:214`
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### fitted_lens `def fitted_lens(self, model)`
- Defined: `tests/test_jlens.py:222`
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_save_and_load_round_trip `def test_save_and_load_round_trip(self, fitted_lens, tmp_path)`
- Defined: `tests/test_jlens.py:226`
- Doc: Scenario: save/load preserves jacobians (fp16 tolerance).
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_apply_returns_correct_shapes `def test_apply_returns_correct_shapes(self, fitted_lens, model)`
- Defined: `tests/test_jlens.py:242`
- Doc: Scenario: apply() returns correct logit shapes.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_fitted_late_layer_matches_model `def test_fitted_late_layer_matches_model(self, fitted_lens, model)`
- Defined: `tests/test_jlens.py:254`
- Doc: Scenario: Transported late-layer logits match model logits.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_apply_with_explicit_positions `def test_apply_with_explicit_positions(self, fitted_lens, model)`
- Defined: `tests/test_jlens.py:263`
- Doc: Scenario: Explicit positions return correct subset.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_logit_lens_baseline `def test_logit_lens_baseline(self, fitted_lens, model)`
- Defined: `tests/test_jlens.py:274`
- Doc: Scenario: use_jacobian=False returns untransported logits.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_unfitted_layer_rejected `def test_unfitted_layer_rejected(self, fitted_lens, model)`
- Defined: `tests/test_jlens.py:281`
- Doc: Scenario: Unfitted layer raises ValueError.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_out_of_range_layer_rejected `def test_out_of_range_layer_rejected(self, fitted_lens, model)`
- Defined: `tests/test_jlens.py:286`
- Doc: Scenario: Out-of-range layer raises ValueError.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_merge_weighted_mean `def test_merge_weighted_mean(self)`
- Defined: `tests/test_jlens.py:291`
- Doc: Scenario: merge() computes n_prompts-weighted mean.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_merge_mismatch_raises `def test_merge_mismatch_raises(self)`
- Defined: `tests/test_jlens.py:319`
- Doc: Scenario: Mismatched lenses raise ValueError.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_merge_empty_raises `def test_merge_empty_raises(self)`
- Defined: `tests/test_jlens.py:326`
- Doc: Scenario: Empty merge raises ValueError.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_transport_produces_correct_shape `def test_transport_produces_correct_shape(self, fitted_lens)`
- Defined: `tests/test_jlens.py:331`
- Doc: Scenario: transport() maps residual to final-layer basis.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_load_invalid_file_raises `def test_load_invalid_file_raises(self, tmp_path)`
- Defined: `tests/test_jlens.py:337`
- Doc: Scenario: Loading non-lens file raises ValueError.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_from_pretrained_local_file `def test_from_pretrained_local_file(self, fitted_lens, tmp_path)`
- Defined: `tests/test_jlens.py:344`
- Doc: Scenario: from_pretrained resolves a local file.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_from_pretrained_local_directory `def test_from_pretrained_local_directory(self, fitted_lens, tmp_path)`
- Defined: `tests/test_jlens.py:351`
- Doc: Scenario: from_pretrained resolves a local directory.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_repr `def test_repr(self, fitted_lens)`
- Defined: `tests/test_jlens.py:359`
- Doc: Scenario: repr contains key metadata.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### model `def model(self)`
- Defined: `tests/test_jlens.py:371`
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_checkpoint_resume_produces_same_result `def test_checkpoint_resume_produces_same_result(self, model, tmp_path)`
- Defined: `tests/test_jlens.py:378`
- Doc: Scenario: Resumed fit matches fresh fit.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_resume_after_skip_no_double_count `def test_resume_after_skip_no_double_count(self, model, tmp_path)`
- Defined: `tests/test_jlens.py:408`
- Doc: Scenario: Resume after a skipped prompt does not double-count.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_checkpoint_mismatch_raises `def test_checkpoint_mismatch_raises(self, model, tmp_path)`
- Defined: `tests/test_jlens.py:450`
- Doc: Scenario: Mismatched checkpoint settings raise ValueError.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_fit_config_defaults `def test_fit_config_defaults(self)`
- Defined: `tests/test_jlens.py:476`
- Doc: Scenario: Default fit config has sensible defaults.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_app_config_defaults `def test_app_config_defaults(self)`
- Defined: `tests/test_jlens.py:485`
- Doc: Scenario: Default app config has sensible defaults.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_default_config `def test_default_config(self)`
- Defined: `tests/test_jlens.py:497`
- Doc: Scenario: Default app config uses all positions.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

### test_custom_config `def test_custom_config(self)`
- Defined: `tests/test_jlens.py:505`
- Doc: Scenario: Custom app config overrides specific layers.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`

## tests/test_lens_model.py

### test_default_config `def test_default_config(self)`
- Defined: `tests/test_lens_model.py:16`
- Doc: Scenario: Default config matches small scale preset.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`, `topogpt3/model.py`

### test_from_topogpt2_config `def test_from_topogpt2_config(self)`
- Defined: `tests/test_lens_model.py:25`
- Doc: Scenario: Build lens config from TopoGPT2Config.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`, `topogpt3/model.py`

### test_probe_checkpoint_missing_raises `def test_probe_checkpoint_missing_raises(self, tmp_path)`
- Defined: `tests/test_lens_model.py:35`
- Doc: Scenario: Missing state.json raises FileNotFoundError.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`, `topogpt3/model.py`

### test_default_parameters `def test_default_parameters(self)`
- Defined: `tests/test_lens_model.py:44`
- Doc: Scenario: TinyDecoder has correct default shape.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`, `topogpt3/model.py`

### test_forward_output_shape `def test_forward_output_shape(self)`
- Defined: `tests/test_lens_model.py:51`
- Doc: Scenario: Forward pass produces correct logit shape.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`, `topogpt3/model.py`

### test_weight_tied `def test_weight_tied(self)`
- Defined: `tests/test_lens_model.py:59`
- Doc: Scenario: Embedding and LM head share weights.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`, `topogpt3/model.py`

### raw_model `def raw_model(self)`
- Defined: `tests/test_lens_model.py:69`
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`, `topogpt3/model.py`

### lens_model `def lens_model(self, raw_model)`
- Defined: `tests/test_lens_model.py:77`
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`, `topogpt3/model.py`

### test_exposes_protocol_attributes `def test_exposes_protocol_attributes(self, lens_model, raw_model)`
- Defined: `tests/test_lens_model.py:80`
- Doc: Scenario: LensModel attributes match underlying model.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`, `topogpt3/model.py`

### test_encode_text_to_token_ids `def test_encode_text_to_token_ids(self, lens_model)`
- Defined: `tests/test_lens_model.py:87`
- Doc: Scenario: encode() returns tensor of shape [1, seq_len].
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`, `topogpt3/model.py`

### test_encode_with_tokenizer `def test_encode_with_tokenizer(self)`
- Defined: `tests/test_lens_model.py:95`
- Doc: Scenario: encode() uses BPETokenizer when available.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`, `topogpt3/model.py`

### test_encode_respects_max_length `def test_encode_respects_max_length(self, lens_model)`
- Defined: `tests/test_lens_model.py:107`
- Doc: Scenario: encode() truncates at max_length.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`, `topogpt3/model.py`

### test_forward_returns_residual_only `def test_forward_returns_residual_only(self)`
- Defined: `tests/test_lens_model.py:113`
- Doc: Scenario: forward() returns hidden states with d_model dim, not vocab.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`, `topogpt3/model.py`

### test_forward_differs_from_full_model `def test_forward_differs_from_full_model(self)`
- Defined: `tests/test_lens_model.py:128`
- Doc: Scenario: Residual forward shape differs from full model logits.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`, `topogpt3/model.py`

### test_unembed_produces_logits `def test_unembed_produces_logits(self, lens_model)`
- Defined: `tests/test_lens_model.py:141`
- Doc: Scenario: unembed() maps residual to logits.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`, `topogpt3/model.py`

### test_forward_plus_unembed_matches_model_logits `def test_forward_plus_unembed_matches_model_logits(self, lens_model, raw_model)`
- Defined: `tests/test_lens_model.py:150`
- Doc: Scenario: residual forward + unembed == model forward logits.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`, `topogpt3/model.py`

### test_autograd_graph_tracks_through_layers `def test_autograd_graph_tracks_through_layers(self)`
- Defined: `tests/test_lens_model.py:163`
- Doc: Scenario: Gradient flows through residual layers when grads enabled.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`, `topogpt3/model.py`

### test_input_device_property `def test_input_device_property(self, lens_model)`
- Defined: `tests/test_lens_model.py:180`
- Doc: Scenario: input_device returns the embedding weight device.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`, `topogpt3/model.py`

### test_input_device_setter `def test_input_device_setter(self, lens_model)`
- Defined: `tests/test_lens_model.py:185`
- Doc: Scenario: input_device can be overridden.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`, `topogpt3/model.py`

### test_tokenizer_setter `def test_tokenizer_setter(self, lens_model)`
- Defined: `tests/test_lens_model.py:191`
- Doc: Scenario: tokenizer can be set after construction.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`, `topogpt3/model.py`

### test_from_checkpoint_missing_raises `def test_from_checkpoint_missing_raises(self)`
- Defined: `tests/test_lens_model.py:198`
- Doc: Scenario: from_checkpoint with missing directory raises.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`, `topogpt3/model.py`

### test_grad_enabled_deterministic `def test_grad_enabled_deterministic(self, lens_model)`
- Defined: `tests/test_lens_model.py:205`
- Doc: Scenario: Multiple forward passes with same input are deterministic.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`, `topogpt3/model.py`

### lens_model `def lens_model(self)`
- Defined: `tests/test_lens_model.py:218`
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`, `topogpt3/model.py`

### test_recorder_captures_layer_outputs `def test_recorder_captures_layer_outputs(self, lens_model)`
- Defined: `tests/test_lens_model.py:225`
- Doc: Scenario: ActivationRecorder captures all requested layer outputs.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`, `topogpt3/model.py`

### test_recorder_with_start_graph_at `def test_recorder_with_start_graph_at(self, lens_model)`
- Defined: `tests/test_lens_model.py:238`
- Doc: Scenario: start_graph_at roots the autograd graph.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`, `topogpt3/model.py`

### test_recorder_cleanup_on_exception `def test_recorder_cleanup_on_exception(self, lens_model)`
- Defined: `tests/test_lens_model.py:252`
- Doc: Scenario: Hooks are removed even if construction fails.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`, `topogpt3/model.py`

### test_recorder_detach_after_forward `def test_recorder_detach_after_forward(self, lens_model)`
- Defined: `tests/test_lens_model.py:264`
- Doc: Scenario: Activations can be detached after recorder exits.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`, `topogpt3/model.py`

### test_empty_sequence `def test_empty_sequence(self)`
- Defined: `tests/test_lens_model.py:281`
- Doc: Scenario: Empty input produces error or minimal output.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`, `topogpt3/model.py`

### test_single_token `def test_single_token(self)`
- Defined: `tests/test_lens_model.py:291`
- Doc: Scenario: Single token input works.
- Depends on: `topogpt3/jlens.py`, `topogpt3/lens_model.py`, `topogpt3/model.py`

## topogpt3.c

### tg_exp `static float tg_exp(float x)`
- Defined: `topogpt3.c:113`
- Imported by: `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`

### tg_tanh `static float tg_tanh(float x)`
- Defined: `topogpt3.c:127`
- Imported by: `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`

### tg_sin `static float tg_sin(float x)`
- Defined: `topogpt3.c:134`
- Imported by: `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`

### tg_cos `static float tg_cos(float x)`
- Defined: `topogpt3.c:143`
- Imported by: `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`

### tg_fabs `static float tg_fabs(float x)`
- Defined: `topogpt3.c:147`
- Imported by: `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`

### tg_log `static float tg_log(float x)`
- Defined: `topogpt3.c:151`
- Imported by: `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`

### tg_fmax `static float tg_fmax(float a, float b)`
- Defined: `topogpt3.c:163`
- Imported by: `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`

### tg_fmin `static float tg_fmin(float a, float b)`
- Defined: `topogpt3.c:167`
- Imported by: `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`

### load_vocab `static void load_vocab(const char *path)`
- Defined: `topogpt3.c:254`
- Imported by: `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`

### build_torus_graph `static void build_torus_graph(void)`
- Defined: `topogpt3.c:295`
- Doc: ====================================================================== SECTION 4: TORUS GRAPH BUILDER * ================
- Imported by: `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`

### precompute_rope `static void precompute_rope(void)`
- Defined: `topogpt3.c:326`
- Doc: ====================================================================== SECTION 5: ROPE PRECOMPUTATION * ================
- Imported by: `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`

### matvec `static void matvec(const float *W, const float *x, float *y, int rows, int cols)`
- Defined: `topogpt3.c:358`
- Doc: ====================================================================== SECTION 6: MATRIX OPERATIONS * ==================
- Imported by: `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`

### matvec_bias `static void matvec_bias(const float *W, const float *b, const float *x, float *y,
               ...`
- Defined: `topogpt3.c:369`
- Imported by: `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`

### rmsnorm `static void rmsnorm(const float *x, const float *w, float *y, int d)`
- Defined: `topogpt3.c:381`
- Imported by: `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`

### softmax `static void softmax(float *x, int n)`
- Defined: `topogpt3.c:390`
- Imported by: `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`

### gelu `static void gelu(float *x, int n)`
- Defined: `topogpt3.c:399`
- Imported by: `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`

### silu `static void silu(float *x, int n)`
- Defined: `topogpt3.c:409`
- Imported by: `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`

### swiglu `static void swiglu(const float *gate_w, const float *up_w, const float *down_w,
                 ...`
- Defined: `topogpt3.c:417`
- Imported by: `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`

### quat_normalize `static void quat_normalize(float *q)`
- Defined: `topogpt3.c:434`
- Doc: ====================================================================== SECTION 7: QUATERNION OPERATIONS * ==============
- Imported by: `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`

### quat_hamilton `static void quat_hamilton(const float *a, const float *b, float *c)`
- Defined: `topogpt3.c:439`
- Imported by: `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`

### quat_linear `static void quat_linear(const float *Ww, const float *Wx, const float *Wy, const float *Wz,
     ...`
- Defined: `topogpt3.c:448`
- Doc: static void quat_normalize(float *q) { float n = tg_sqrt(q[0]*q[0] + q[1]*q[1] + q[2]*q[2] + q[3]*q[3]); if (n > 1e-8f) 
- Imported by: `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`

### ifft_radix2 `static void ifft_radix2(float *real, float *imag, int n)`
- Defined: `topogpt3.c:504`
- Imported by: `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`

### rfft `static void rfft(const float *x, float *Xr, float *Xi, int n)`
- Defined: `topogpt3.c:513`
- Doc: cur_r = nr; } } } } static void ifft_radix2(float *real, float *imag, int n) { int i; for (i = 0; i < n; i++) imag[i] = 
- Imported by: `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`

### irfft `static void irfft(const float *Xr, const float *Xi, float *x, int n)`
- Defined: `topogpt3.c:522`
- Doc: fft_radix2(real, imag, n); for (i = 0; i < n; i++) { real[i] /= (float)n; imag[i] = -imag[i] / (float)n; } } /* Real FFT
- Imported by: `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`

### filter1d `static void filter1d(const float *x, const float *kr, const float *ki,
                      floa...`
- Defined: `topogpt3.c:536`
- Doc: ====================================================================== SECTION 9: SPECTRAL 1D FILTER * =================
- Imported by: `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`

### ifft2d `static void ifft2d(float *data_r, float *data_i, int h, int w)`
- Defined: `topogpt3.c:579`
- Imported by: `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`

### rfft2d_real `static void rfft2d_real(const float *data, float *out_r, float *out_i,
                         i...`
- Defined: `topogpt3.c:602`
- Doc: ifft_radix2(row_re, row_im, w); for (c = 0; c < w; c++) { re[r*w+c] = row_re[c]; im[r*w+c] = row_im[c]; } } /* IFFT colu
- Imported by: `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`

### irfft2d `static void irfft2d(const float *in_r, const float *in_i, float *out,
                     int h,...`
- Defined: `topogpt3.c:629`
- Doc: for (r = 0; r < h; r++) { col_re[r] = re[r*w+c]; col_im[r] = im[r*w+c]; } fft_radix2(col_re, col_im, h); for (r = 0; r <
- Imported by: `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`

### cmul `static void cmul(float ar, float ai, float cr, float di, float *rr, float *ri)`
- Defined: `topogpt3.c:664`
- Doc: ====================================================================== SECTION 11: QUATERNION SPECTRAL LAYER 2D * ======
- Imported by: `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`

### spectral_contract `static void spectral_contract(const float *Wr, const float *Wi,
                               co...`
- Defined: `topogpt3.c:670`
- Doc: ====================================================================== SECTION 11: QUATERNION SPECTRAL LAYER 2D * ======
- Imported by: `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`

### quat_spectral_layer_2d `static void quat_spectral_layer_2d(
    const float *x, float *y,
    const float *kr_w, const fl...`
- Defined: `topogpt3.c:694`
- Imported by: `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`

### spectral_ae_encode `static void spectral_ae_encode(const float *x, float *z, const LayerWeights *lw)`
- Defined: `topogpt3.c:784`
- Doc: ====================================================================== SECTION 12: SPECTRAL AUTOENCODER FORWARD * ======
- Imported by: `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`

### spectral_ae_decode `static void spectral_ae_decode(const float *z, float *x, const LayerWeights *lw)`
- Defined: `topogpt3.c:792`
- Imported by: `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`

### process_torus_grid `static void process_torus_grid(const float *grid, float *out, const LayerWeights *lw)`
- Defined: `topogpt3.c:799`
- Imported by: `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`

### torus_soft_assign `static void torus_soft_assign(const float *phi1, const float *phi2,
                             ...`
- Defined: `topogpt3.c:820`
- Doc: ====================================================================== SECTION 13: TORUS BRAIN FORWARD * ===============
- Imported by: `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`

### message_passing `static void message_passing(const float *node_feat, float *out,
                             cons...`
- Defined: `topogpt3.c:842`
- Imported by: `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`

### torus_brain_forward `static void torus_brain_forward(const float *x, float *out, float *recon_loss,
                  ...`
- Defined: `topogpt3.c:887`
- Imported by: `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`

### attention_forward `static void attention_forward(const float *x, float *out, int layer_idx, int pos, int total_kv_co...`
- Defined: `topogpt3.c:977`
- Doc: ====================================================================== SECTION 14: ATTENTION FORWARD * =================
- Imported by: `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`

### moe_forward `static void moe_forward(const float *x, float *out, const LayerWeights *lw)`
- Defined: `topogpt3.c:1077`
- Doc: ====================================================================== SECTION 15: MoE ROUTING * =======================
- Imported by: `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`

### forward `static void forward(const int *token_ids, int seq_len, float *logits_out)`
- Defined: `topogpt3.c:1127`
- Doc: ====================================================================== SECTION 16: FULL MODEL FORWARD  Processes tokens 
- Imported by: `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`

### tokenize_string `static int tokenize_string(const char *text, int *tokens, int max_tokens)`
- Defined: `topogpt3.c:1194`
- Imported by: `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`

### apply_temperature `static void apply_temperature(float *logits, int n, float temp)`
- Defined: `topogpt3.c:1209`
- Doc: ====================================================================== SECTION 18: SAMPLING * ==========================
- Imported by: `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`

### apply_repetition_penalty `static void apply_repetition_penalty(float *logits, int n, const int *tokens,
                   ...`
- Defined: `topogpt3.c:1215`
- Imported by: `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`

### apply_top_k `static void apply_top_k(float *logits, int n, int k)`
- Defined: `topogpt3.c:1228`
- Imported by: `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`

### sample `static int sample(const float *logits, int n)`
- Defined: `topogpt3.c:1247`
- Imported by: `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`

### load_weights `static int load_weights(const char *path)`
- Defined: `topogpt3.c:1281`
- Doc: ====================================================================== SECTION 19: WEIGHT LOADER  Reads the binary file 
- Imported by: `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`

### load_weights_fp16 `static int load_weights_fp16(const char *path)`
- Defined: `topogpt3.c:1451`
- Imported by: `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`

### load_weights_auto `static int load_weights_auto(const char *path)`
- Defined: `topogpt3.c:1583`
- Doc: printf("  Layer %d loaded\n", i); } READ_TENSOR16(W.final_norm, D_MODEL); #undef SKIP_TENSOR16 #undef READ_TENSOR16 fclo
- Imported by: `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`

### time_now_ms `static double time_now_ms(void)`
- Defined: `topogpt3.c:1600`
- Doc: ====================================================================== SECTION 20: TIMING * ============================
- Imported by: `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`

### decode_token `static void decode_token(int tid)`
- Defined: `topogpt3.c:1613`
- Doc: ====================================================================== SECTION 21: GENERATION * ========================
- Imported by: `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`

### load_token_file `static int load_token_file(const char *path, int *out_ids, int max_ids)`
- Defined: `topogpt3.c:1629`
- Doc: if (tid < 256) { /* Map GPT-2 byte-level encoding back to original byte int n = tid; if (n < 94) n += 33; else if (n < 1
- Imported by: `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`

### decode_token_tiktoken `static void decode_token_tiktoken(int tid)`
- Defined: `topogpt3.c:1652`
- Doc: if (fread(&n, 4, 1, f) != 1) { fclose(f); return 0; } if (n > (unsigned)max_ids) n = max_ids; int count = (int)n; int i;
- Imported by: `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`

### generate_tokens `static void generate_tokens(int *prompt_tokens, int n_prompt, int max_new_tokens,
               ...`
- Defined: `topogpt3.c:1660`
- Imported by: `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`

### generate `static void generate(const char *prompt, int max_new_tokens, float temperature,
                 ...`
- Defined: `topogpt3.c:1724`
- Imported by: `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`

### interactive_mode `static void interactive_mode(void)`
- Defined: `topogpt3.c:1735`
- Doc: ====================================================================== SECTION 22: INTERACTIVE MODE * ==================
- Imported by: `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`

### print_help `static void print_help(void)`
- Defined: `topogpt3.c:1849`
- Doc: ====================================================================== SECTION 23: HELP AND MAIN * =====================
- Imported by: `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`

### main `int main(int argc, char **argv)`
- Defined: `topogpt3.c:1884`
- Imported by: `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`

## topogpt3/__main__.py

### main `def main()`
- Defined: `topogpt3/__main__.py:6`
- Doc: TopoGPT3 entry point. Delegates to subcommands.
- Depends on: `topogpt3/api_server.py`, `topogpt3/inference.py`, `topogpt3/inference_hrm.py`, `topogpt3/jlens.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

## topogpt3/api_server.py

### _setup_logging `def _setup_logging(verbose)`
- Defined: `topogpt3/api_server.py:116`
- Depends on: `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### _parse_keys `def _parse_keys(raw)`
- Defined: `topogpt3/api_server.py:164`
- Doc: Accept ``key1,admin:key2,key3``. The ``admin:`` prefix marks an
- Depends on: `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### _sha256 `def _sha256(raw)`
- Defined: `topogpt3/api_server.py:192`
- Depends on: `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### _sanitize_stop `def _sanitize_stop(stop)`
- Defined: `topogpt3/api_server.py:281`
- Depends on: `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### _resolve_device `def _resolve_device(device)`
- Defined: `topogpt3/api_server.py:499`
- Depends on: `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### _probe_n_kv `def _probe_n_kv(checkpoint_dir)`
- Defined: `topogpt3/api_server.py:505`
- Depends on: `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### load_model `def load_model(checkpoint, device)`
- Defined: `topogpt3/api_server.py:513`
- Depends on: `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### lifespan `def lifespan(app)`
- Defined: `topogpt3/api_server.py:534`
- Depends on: `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### _security_middleware `def _security_middleware(request, call_next)`
- Defined: `topogpt3/api_server.py:574`
- Doc: Global middleware: rate-limit, IP-ban, security headers, audit log.
- Depends on: `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### _real_ip `def _real_ip(request)`
- Defined: `topogpt3/api_server.py:602`
- Doc: Best-effort real client IP. We trust no proxy headers by default.
- Depends on: `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### _json_error `def _json_error(status, detail)`
- Defined: `topogpt3/api_server.py:613`
- Depends on: `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### _authenticate `def _authenticate(request)`
- Defined: `topogpt3/api_server.py:625`
- Doc: FastAPI dependency: extract & validate Bearer token.
- Depends on: `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### _check_rate_limit `def _check_rate_limit(api_key, request)`
- Defined: `topogpt3/api_server.py:643`
- Doc: Rate limit per-key (with admin exemption / higher limit).
- Depends on: `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### health `def health(request)`
- Defined: `topogpt3/api_server.py:661`
- Depends on: `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### list_models `def list_models(request)`
- Defined: `topogpt3/api_server.py:668`
- Depends on: `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### completions `def completions(req, request)`
- Defined: `topogpt3/api_server.py:685`
- Depends on: `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### chat_completions `def chat_completions(req, request)`
- Defined: `topogpt3/api_server.py:741`
- Depends on: `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### _check_model `def _check_model()`
- Defined: `topogpt3/api_server.py:799`
- Depends on: `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### _short_id `def _short_id()`
- Defined: `topogpt3/api_server.py:804`
- Depends on: `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### _build_chat_prompt `def _build_chat_prompt(messages)`
- Defined: `topogpt3/api_server.py:808`
- Depends on: `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### _extract_text `def _extract_text(content)`
- Defined: `topogpt3/api_server.py:815`
- Depends on: `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### _stream_completion `def _stream_completion(prompt, max_tokens, temperature, top_k, repetition_penalty, stop, auto_continue, max_continuations)`
- Defined: `topogpt3/api_server.py:829`
- Depends on: `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### _stream_chat `def _stream_chat(t0_ms, prompt, max_tokens, temperature, top_k, repetition_penalty, stop, auto_continue, max_continuations)`
- Defined: `topogpt3/api_server.py:864`
- Depends on: `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### main `def main()`
- Defined: `topogpt3/api_server.py:902`
- Depends on: `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### validate `def validate(self, raw)`
- Defined: `topogpt3/api_server.py:148`
- Depends on: `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### consume `def consume(self, n)`
- Defined: `topogpt3/api_server.py:208`
- Depends on: `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### __init__ `def __init__(self, user_rps, admin_rps, capacity)`
- Defined: `topogpt3/api_server.py:220`
- Depends on: `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### _cleanup `def _cleanup(self)`
- Defined: `topogpt3/api_server.py:227`
- Depends on: `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### allow `def allow(self, key, role)`
- Defined: `topogpt3/api_server.py:233`
- Depends on: `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### __init__ `def __init__(self, max_failures, window)`
- Defined: `topogpt3/api_server.py:251`
- Depends on: `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### record_failure `def record_failure(self, ip)`
- Defined: `topogpt3/api_server.py:257`
- Depends on: `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### is_banned `def is_banned(self, ip)`
- Defined: `topogpt3/api_server.py:265`
- Depends on: `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### _normalize_stop `def _normalize_stop(cls, v)`
- Defined: `topogpt3/api_server.py:306`
- Depends on: `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### _normalize_stop `def _normalize_stop(cls, v)`
- Defined: `topogpt3/api_server.py:331`
- Depends on: `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### complete `def complete(self, prompt)`
- Defined: `topogpt3/api_server.py:348`
- Depends on: `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### stream_complete `def stream_complete(self, prompt)`
- Defined: `topogpt3/api_server.py:393`
- Depends on: `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

### _is_eos `def _is_eos(self, token_id)`
- Defined: `topogpt3/api_server.py:482`
- Depends on: `topogpt3/continuation.py`, `topogpt3/model.py`
- Imported by: `topogpt3/__main__.py`

## topogpt3/continuation.py

### _count_unclosed_brackets `def _count_unclosed_brackets(text)`
- Defined: `topogpt3/continuation.py:25`
- Imported by: `topogpt3/api_server.py`, `topogpt3/inference_hrm.py`, `topogpt3/model.py`

### _count_unclosed_fences `def _count_unclosed_fences(text)`
- Defined: `topogpt3/continuation.py:36`
- Imported by: `topogpt3/api_server.py`, `topogpt3/inference_hrm.py`, `topogpt3/model.py`

### is_response_complete `def is_response_complete(text, min_chars)`
- Defined: `topogpt3/continuation.py:45`
- Doc: Heuristic to decide whether a model response looks finished.
- Imported by: `topogpt3/api_server.py`, `topogpt3/inference_hrm.py`, `topogpt3/model.py`

### extract_tail_for_continuation `def extract_tail_for_continuation(text, tail_lines, tail_chars)`
- Defined: `topogpt3/continuation.py:75`
- Doc: Return the last N lines (or up to tail_chars) of `text` as a
- Imported by: `topogpt3/api_server.py`, `topogpt3/inference_hrm.py`, `topogpt3/model.py`

### split_at_last_newline `def split_at_last_newline(text)`
- Defined: `topogpt3/continuation.py:105`
- Doc: Split `text` at the last newline.
- Imported by: `topogpt3/api_server.py`, `topogpt3/inference_hrm.py`, `topogpt3/model.py`

## topogpt3/inference.py

### main `def main(argv)`
- Defined: `topogpt3/inference.py:721`
- Doc: CLI entry point. Returns a process exit code.
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### scale_presets `def scale_presets()`
- Defined: `topogpt3/inference.py:103`
- Doc: Return the architecture preset table indexed by scale name.
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### preset `def preset(self)`
- Defined: `topogpt3/inference.py:116`
- Doc: Return the resolved preset for the configured model scale.
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### validate `def validate(self)`
- Defined: `topogpt3/inference.py:126`
- Doc: Raise ValueError if any setting falls outside its safety bounds.
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### build `def build(settings)`
- Defined: `topogpt3/inference.py:162`
- Doc: Return a configured Logger with a single deduplicated stdout handler.
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### resolve_under `def resolve_under(root)`
- Defined: `topogpt3/inference.py:182`
- Doc: Join `parts` under `root` and return the canonical resolved path.
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### require_existing_file `def require_existing_file(path, expected_suffix)`
- Defined: `topogpt3/inference.py:198`
- Doc: Validate `path` points to an existing regular file with the expected suffix.
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __init__ `def __init__(self, settings, logger)`
- Defined: `topogpt3/inference.py:215`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### load `def load(self)`
- Defined: `topogpt3/inference.py:219`
- Doc: Return the topogpt3.train module which re-exports model symbols.
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __init__ `def __init__(self, settings)`
- Defined: `topogpt3/inference.py:231`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### slot_dir `def slot_dir(self)`
- Defined: `topogpt3/inference.py:239`
- Doc: Directory holding the active checkpoint slot.
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### model_file `def model_file(self)`
- Defined: `topogpt3/inference.py:243`
- Doc: Resolved path to the safetensors weights file inside the slot.
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### state_file `def state_file(self)`
- Defined: `topogpt3/inference.py:249`
- Doc: Resolved path to the JSON training-state file inside the slot.
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### assert_ready `def assert_ready(self)`
- Defined: `topogpt3/inference.py:255`
- Doc: Verify weights exist and the on-disk size lies within safety bounds.
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __init__ `def __init__(self, settings, logger)`
- Defined: `topogpt3/inference.py:277`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### detect_n_kv_heads `def detect_n_kv_heads(self, weights_path, d_model, n_heads)`
- Defined: `topogpt3/inference.py:281`
- Doc: Recover N_KV_HEADS used at training by inspecting the k_proj shape.
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __init__ `def __init__(self, settings, source_module, logger)`
- Defined: `topogpt3/inference.py:321`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### build `def build(self, n_kv_heads, vocab_size)`
- Defined: `topogpt3/inference.py:327`
- Doc: Return a TopoGPT2Config dataclass ready to instantiate the model.
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __init__ `def __init__(self, settings, source_module)`
- Defined: `topogpt3/inference.py:352`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### build `def build(self)`
- Defined: `topogpt3/inference.py:356`
- Doc: Return an instance of BPETokenizer bound to the configured encoding.
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __init__ `def __init__(self, settings, source_module, logger)`
- Defined: `topogpt3/inference.py:365`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### apply_if_enabled `def apply_if_enabled(self)`
- Defined: `topogpt3/inference.py:371`
- Doc: Patch QuaternionSpectralLayer to use the 3-multiply Gauss contract.
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __init__ `def __init__(self, settings, source_module, logger)`
- Defined: `topogpt3/inference.py:383`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### assemble `def assemble(self, aligned_cfg, paths)`
- Defined: `topogpt3/inference.py:389`
- Doc: Build the TopoGPT2 graph, load weights into it, and return it in eval mode.
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __init__ `def __init__(self, settings, source_module, logger)`
- Defined: `topogpt3/inference.py:420`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### apply `def apply(self)`
- Defined: `topogpt3/inference.py:426`
- Doc: Seed all relevant RNGs using the model package helper when available.
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### from_settings `def from_settings(cls, settings)`
- Defined: `topogpt3/inference.py:450`
- Doc: Construct a SamplingPolicy from inference settings.
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### tokens_per_second `def tokens_per_second(self, elapsed_floor)`
- Defined: `topogpt3/inference.py:470`
- Doc: Return throughput in tokens/sec, clamped to avoid divide-by-zero.
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __init__ `def __init__(self, settings, logger)`
- Defined: `topogpt3/inference.py:478`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### run `def run(self, model, tokenizer, prompt, policy)`
- Defined: `topogpt3/inference.py:483`
- Doc: Generate a completion for `prompt` and return a GenerationReport.
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __init__ `def __init__(self, settings, logger)`
- Defined: `topogpt3/inference.py:536`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### render `def render(self, report)`
- Defined: `topogpt3/inference.py:540`
- Doc: Emit a banner with prompt and completion, plus a throughput log line.
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __init__ `def __init__(self, settings, logger)`
- Defined: `topogpt3/inference.py:565`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### execute `def execute(self)`
- Defined: `topogpt3/inference.py:571`
- Doc: Run the full inference pipeline end-to-end and return the report.
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### build_parser `def build_parser()`
- Defined: `topogpt3/inference.py:619`
- Doc: Return the configured argparse.ArgumentParser.
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### parse `def parse(argv)`
- Defined: `topogpt3/inference.py:698`
- Doc: Parse `argv` (or sys.argv) and return a populated InferenceSettings.
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

## topogpt3/inference_hrm.py

### main `def main(argv)`
- Defined: `topogpt3/inference_hrm.py:1494`
- Doc: CLI entry point. Returns a process exit code.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### scale_presets `def scale_presets()`
- Defined: `topogpt3/inference_hrm.py:221`
- Doc: Return the architecture preset table indexed by scale name.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### preset `def preset(self)`
- Defined: `topogpt3/inference_hrm.py:234`
- Doc: Return the resolved preset for the configured model scale.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### validate `def validate(self)`
- Defined: `topogpt3/inference_hrm.py:244`
- Doc: Raise ValueError if any setting falls outside its safety bounds.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### build `def build(settings)`
- Defined: `topogpt3/inference_hrm.py:347`
- Doc: Return a configured Logger with a single deduplicated stdout handler.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### resolve_under `def resolve_under(root)`
- Defined: `topogpt3/inference_hrm.py:367`
- Doc: Join parts under root and return the canonical resolved path.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### require_existing_file `def require_existing_file(path, expected_suffix)`
- Defined: `topogpt3/inference_hrm.py:383`
- Doc: Validate path points to an existing regular file with the expected suffix.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __init__ `def __init__(self, settings, logger)`
- Defined: `topogpt3/inference_hrm.py:400`
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### load `def load(self)`
- Defined: `topogpt3/inference_hrm.py:404`
- Doc: Return the topogpt3.train module which re-exports model symbols.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __init__ `def __init__(self, settings)`
- Defined: `topogpt3/inference_hrm.py:416`
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### slot_dir `def slot_dir(self)`
- Defined: `topogpt3/inference_hrm.py:424`
- Doc: Directory holding the active checkpoint slot.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### model_file `def model_file(self)`
- Defined: `topogpt3/inference_hrm.py:428`
- Doc: Resolved path to the safetensors weights file inside the slot.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### state_file `def state_file(self)`
- Defined: `topogpt3/inference_hrm.py:434`
- Doc: Resolved path to the JSON training-state file inside the slot.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### assert_ready `def assert_ready(self)`
- Defined: `topogpt3/inference_hrm.py:440`
- Doc: Verify weights exist and the on-disk size lies within safety bounds.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __init__ `def __init__(self, settings, logger)`
- Defined: `topogpt3/inference_hrm.py:462`
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### detect_n_kv_heads `def detect_n_kv_heads(self, weights_path, d_model, n_heads)`
- Defined: `topogpt3/inference_hrm.py:466`
- Doc: Recover N_KV_HEADS used at training by inspecting the k_proj shape.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __init__ `def __init__(self, settings, source_module, logger)`
- Defined: `topogpt3/inference_hrm.py:505`
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### build `def build(self, n_kv_heads, vocab_size)`
- Defined: `topogpt3/inference_hrm.py:511`
- Doc: Return a TopoGPT2Config dataclass ready to instantiate the model.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __init__ `def __init__(self, settings, source_module)`
- Defined: `topogpt3/inference_hrm.py:536`
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### build `def build(self)`
- Defined: `topogpt3/inference_hrm.py:540`
- Doc: Return an instance of BPETokenizer bound to the configured encoding.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __init__ `def __init__(self, settings, source_module, logger)`
- Defined: `topogpt3/inference_hrm.py:549`
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### apply_if_enabled `def apply_if_enabled(self)`
- Defined: `topogpt3/inference_hrm.py:555`
- Doc: Patch QuaternionSpectralLayer to use the 3-multiply Gauss contract.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __init__ `def __init__(self, settings, source_module, logger)`
- Defined: `topogpt3/inference_hrm.py:567`
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### assemble `def assemble(self, aligned_cfg, paths)`
- Defined: `topogpt3/inference_hrm.py:573`
- Doc: Build the TopoGPT2 graph, load weights into it, and return it in eval mode.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __init__ `def __init__(self, settings, source_module, logger)`
- Defined: `topogpt3/inference_hrm.py:604`
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### apply `def apply(self)`
- Defined: `topogpt3/inference_hrm.py:610`
- Doc: Seed all relevant RNGs using the model package helper when available.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __init__ `def __init__(self, epsilon_floor)`
- Defined: `topogpt3/inference_hrm.py:627`
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### relative_change `def relative_change(self, current, previous)`
- Defined: `topogpt3/inference_hrm.py:632`
- Doc: Return ||current - previous|| / max(||previous||, epsilon_floor).
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### absorb `def absorb(self, sample)`
- Defined: `topogpt3/inference_hrm.py:671`
- Doc: Fold a per-token sample into the running totals.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __init__ `def __init__(self, persist_tokens)`
- Defined: `topogpt3/inference_hrm.py:693`
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### get_or_init `def get_or_init(self, reference)`
- Defined: `topogpt3/inference_hrm.py:700`
- Doc: Return the cached high-level state or a zeroed one when stale.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### commit `def commit(self, new_state)`
- Defined: `topogpt3/inference_hrm.py:716`
- Doc: Store a fresh high-level state and increment the cache age.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### invalidate `def invalidate(self)`
- Defined: `topogpt3/inference_hrm.py:721`
- Doc: Drop any cached state and reset the age counter.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __init__ `def __init__(self, layers, final_norm, reasoning_config, logger)`
- Defined: `topogpt3/inference_hrm.py:768`
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### num_layers `def num_layers(self)`
- Defined: `topogpt3/inference_hrm.py:789`
- Doc: Return the number of trained transformer layers.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### _full_pass `def _full_pass(self, z_in, base_kvs)`
- Defined: `topogpt3/inference_hrm.py:793`
- Doc: Forward z_in through every layer using base_kvs as immutable prefix cache.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### _window_pass `def _window_pass(self, z_in, base_kvs, window)`
- Defined: `topogpt3/inference_hrm.py:808`
- Doc: Forward z_in through the trailing `window` layers only.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### reason `def reason(self, z_initial, base_kvs, cached_refinement)`
- Defined: `topogpt3/inference_hrm.py:827`
- Doc: Run hierarchical recursive thinking for a single emission step.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __init__ `def __init__(self, logger)`
- Defined: `topogpt3/inference_hrm.py:938`
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### sample `def sample(self, logits, token_history, temperature, top_k, repetition_penalty)`
- Defined: `topogpt3/inference_hrm.py:941`
- Doc: Return a sampled token id tensor of shape [B, 1] from raw logits [B, V].
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### from_settings `def from_settings(cls, settings)`
- Defined: `topogpt3/inference_hrm.py:973`
- Doc: Construct a SamplingPolicy from inference settings.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### tokens_per_second `def tokens_per_second(self, elapsed_floor)`
- Defined: `topogpt3/inference_hrm.py:995`
- Doc: Return throughput in tokens/sec, clamped to avoid divide-by-zero.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __init__ `def __init__(self, settings, logger)`
- Defined: `topogpt3/inference_hrm.py:1011`
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### _encode_prompt `def _encode_prompt(self, model, prompt_ids)`
- Defined: `topogpt3/inference_hrm.py:1016`
- Doc: Run the prompt through the full stack once, returning the final
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### run `def run(self, model, tokenizer, prompt, policy)`
- Defined: `topogpt3/inference_hrm.py:1048`
- Doc: Generate a completion for prompt and return a GenerationReport.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __init__ `def __init__(self, settings, logger)`
- Defined: `topogpt3/inference_hrm.py:1192`
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### render `def render(self, report)`
- Defined: `topogpt3/inference_hrm.py:1196`
- Doc: Emit a banner with prompt, completion, throughput and reasoning stats.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __init__ `def __init__(self, settings, logger)`
- Defined: `topogpt3/inference_hrm.py:1233`
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### execute `def execute(self)`
- Defined: `topogpt3/inference_hrm.py:1239`
- Doc: Run the full inference pipeline end-to-end and return the report.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### build_parser `def build_parser()`
- Defined: `topogpt3/inference_hrm.py:1287`
- Doc: Return the configured argparse.ArgumentParser.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

### parse `def parse(argv)`
- Defined: `topogpt3/inference_hrm.py:1448`
- Doc: Parse argv (or sys.argv) and return a populated HRMInferenceSettings.
- Depends on: `topogpt3/continuation.py`
- Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`

## topogpt3/jlens.py

### valid_position_mask `def valid_position_mask(seq_len)`
- Defined: `topogpt3/jlens.py:132`
- Doc: Boolean mask over sequence positions to include in the Jacobian average.
- Depends on: `topogpt3/lens_model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### _check_layer_indices `def _check_layer_indices(source_layers, target_layer, n_layers)`
- Defined: `topogpt3/jlens.py:162`
- Doc: Resolve None/negative layer indices, bounds-check, enforce source < target.
- Depends on: `topogpt3/lens_model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### jacobian_for_prompt `def jacobian_for_prompt(model, prompt, source_layers)`
- Defined: `topogpt3/jlens.py:187`
- Doc: Compute the per-layer Jacobian estimator ``J_l`` for one prompt.
- Depends on: `topogpt3/lens_model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### _atomic_save `def _atomic_save(obj, path)`
- Defined: `topogpt3/jlens.py:283`
- Doc: ``torch.save`` to a temp file then ``os.replace`` so a crash never
- Depends on: `topogpt3/lens_model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### fit `def fit(model, prompts)`
- Defined: `topogpt3/jlens.py:291`
- Doc: Fit ``J_l`` over a list of prompts and return a JacobianLens.
- Depends on: `topogpt3/lens_model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### compute_slice `def compute_slice(model, lens, prompt)`
- Defined: `topogpt3/jlens.py:705`
- Doc: Compute a position x layer slice of top-K token predictions.
- Depends on: `topogpt3/lens_model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### text_slice `def text_slice(slice_data, tokenizer, n_cols)`
- Defined: `topogpt3/jlens.py:789`
- Doc: Render a SliceData as a readable text table showing decoded words.
- Depends on: `topogpt3/lens_model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### _demo_jlens `def _demo_jlens()`
- Defined: `topogpt3/jlens.py:842`
- Doc: Run a full jacobian lens demo loading real weights from checkpoint.
- Depends on: `topogpt3/lens_model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __init__ `def __init__(self, blocks, at)`
- Defined: `topogpt3/jlens.py:87`
- Depends on: `topogpt3/lens_model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### _make_hook `def _make_hook(self, index)`
- Defined: `topogpt3/jlens.py:102`
- Depends on: `topogpt3/lens_model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __enter__ `def __enter__(self)`
- Defined: `topogpt3/jlens.py:113`
- Depends on: `topogpt3/lens_model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __exit__ `def __exit__(self)`
- Defined: `topogpt3/jlens.py:126`
- Depends on: `topogpt3/lens_model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### write_checkpoint `def write_checkpoint()`
- Defined: `topogpt3/jlens.py:378`
- Depends on: `topogpt3/lens_model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __init__ `def __init__(self, jacobians)`
- Defined: `topogpt3/jlens.py:470`
- Depends on: `topogpt3/lens_model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __repr__ `def __repr__(self)`
- Defined: `topogpt3/jlens.py:482`
- Depends on: `topogpt3/lens_model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### save `def save(self, path)`
- Defined: `topogpt3/jlens.py:489`
- Doc: Save to ``path``. Jacobians are stored as ``dtype`` (default fp16).
- Depends on: `topogpt3/lens_model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### load `def load(cls, path)`
- Defined: `topogpt3/jlens.py:504`
- Doc: Load a lens previously written by ``save``.
- Depends on: `topogpt3/lens_model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### from_pretrained `def from_pretrained(cls, name_or_path)`
- Defined: `topogpt3/jlens.py:519`
- Doc: Load a lens from a local file, a local directory, or a HuggingFace
- Depends on: `topogpt3/lens_model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### merge `def merge(cls, lenses)`
- Defined: `topogpt3/jlens.py:543`
- Doc: Combine lenses fitted on disjoint prompt subsets into one
- Depends on: `topogpt3/lens_model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### transport `def transport(self, residual, layer)`
- Defined: `topogpt3/jlens.py:574`
- Doc: Map a residual at ``layer`` into the final-layer basis: ``J_l @ h``.
- Depends on: `topogpt3/lens_model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### apply `def apply(self, model, prompt)`
- Defined: `topogpt3/jlens.py:585`
- Doc: Run ``model`` on ``prompt`` and return lens logits at ``positions``.
- Depends on: `topogpt3/lens_model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __post_init__ `def __post_init__(self)`
- Defined: `topogpt3/jlens.py:692`
- Depends on: `topogpt3/lens_model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### hook `def hook(module, inputs, output)`
- Defined: `topogpt3/jlens.py:105`
- Depends on: `topogpt3/lens_model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### select `def select(layer)`
- Defined: `topogpt3/jlens.py:646`
- Depends on: `topogpt3/lens_model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

## topogpt3/lens_model.py

### encode `def encode(self, text)`
- Defined: `topogpt3/lens_model.py:40`
- Doc: Tokenize ``text`` to ``input_ids`` of shape ``[1, seq_len]`` on the
- Depends on: `topogpt3/model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/jlens.py`, `topogpt3/jlens.py`

### forward `def forward(self, input_ids)`
- Defined: `topogpt3/lens_model.py:45`
- Doc: Run the residual stack on ``input_ids`` (no LM head). Must build an
- Depends on: `topogpt3/model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/jlens.py`, `topogpt3/jlens.py`

### unembed `def unembed(self, residual)`
- Defined: `topogpt3/lens_model.py:52`
- Doc: Map a residual-stream tensor ``[..., d_model]`` to logits
- Depends on: `topogpt3/model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/jlens.py`, `topogpt3/jlens.py`

### from_topogpt2_config `def from_topogpt2_config(cls, cfg)`
- Defined: `topogpt3/lens_model.py:84`
- Doc: Construct a lens config from a TopoGPT2Config dataclass.
- Depends on: `topogpt3/model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/jlens.py`, `topogpt3/jlens.py`

### probe_checkpoint `def probe_checkpoint(cls, checkpoint_dir)`
- Defined: `topogpt3/lens_model.py:104`
- Doc: Probe a checkpoint directory and infer lens config from state.json.
- Depends on: `topogpt3/model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/jlens.py`, `topogpt3/jlens.py`

### __init__ `def __init__(self, model)`
- Defined: `topogpt3/lens_model.py:150`
- Depends on: `topogpt3/model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/jlens.py`, `topogpt3/jlens.py`

### forward `def forward(self, input_ids)`
- Defined: `topogpt3/lens_model.py:154`
- Depends on: `topogpt3/model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/jlens.py`, `topogpt3/jlens.py`

### __init__ `def __init__(self, model, tokenizer)`
- Defined: `topogpt3/lens_model.py:172`
- Depends on: `topogpt3/model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/jlens.py`, `topogpt3/jlens.py`

### n_layers `def n_layers(self)`
- Defined: `topogpt3/lens_model.py:184`
- Depends on: `topogpt3/model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/jlens.py`, `topogpt3/jlens.py`

### d_model `def d_model(self)`
- Defined: `topogpt3/lens_model.py:188`
- Depends on: `topogpt3/model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/jlens.py`, `topogpt3/jlens.py`

### layers `def layers(self)`
- Defined: `topogpt3/lens_model.py:192`
- Depends on: `topogpt3/model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/jlens.py`, `topogpt3/jlens.py`

### tokenizer `def tokenizer(self)`
- Defined: `topogpt3/lens_model.py:196`
- Depends on: `topogpt3/model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/jlens.py`, `topogpt3/jlens.py`

### tokenizer `def tokenizer(self, tok)`
- Defined: `topogpt3/lens_model.py:200`
- Depends on: `topogpt3/model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/jlens.py`, `topogpt3/jlens.py`

### input_device `def input_device(self)`
- Defined: `topogpt3/lens_model.py:204`
- Depends on: `topogpt3/model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/jlens.py`, `topogpt3/jlens.py`

### input_device `def input_device(self, device)`
- Defined: `topogpt3/lens_model.py:210`
- Depends on: `topogpt3/model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/jlens.py`, `topogpt3/jlens.py`

### encode `def encode(self, text)`
- Defined: `topogpt3/lens_model.py:213`
- Doc: Tokenize text to input_ids of shape ``[1, seq_len]``.
- Depends on: `topogpt3/model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/jlens.py`, `topogpt3/jlens.py`

### forward `def forward(self, input_ids)`
- Defined: `topogpt3/lens_model.py:228`
- Doc: Run the residual stack on ``input_ids``.
- Depends on: `topogpt3/model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/jlens.py`, `topogpt3/jlens.py`

### unembed `def unembed(self, residual)`
- Defined: `topogpt3/lens_model.py:237`
- Doc: Map residual ``[..., d_model]`` to logits ``[..., vocab_size]``.
- Depends on: `topogpt3/model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/jlens.py`, `topogpt3/jlens.py`

### from_checkpoint `def from_checkpoint(cls, checkpoint_dir)`
- Defined: `topogpt3/lens_model.py:246`
- Doc: Build a TopoGPT3LensModel from a checkpoint directory.
- Depends on: `topogpt3/model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/jlens.py`, `topogpt3/jlens.py`

### __init__ `def __init__(self, n_layers, d_model, vocab_size, seed)`
- Defined: `topogpt3/lens_model.py:315`
- Depends on: `topogpt3/model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/jlens.py`, `topogpt3/jlens.py`

### forward `def forward(self, token_ids, past_kvs)`
- Defined: `topogpt3/lens_model.py:344`
- Depends on: `topogpt3/model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/jlens.py`, `topogpt3/jlens.py`

### __init__ `def __init__(self, d_model)`
- Defined: `topogpt3/lens_model.py:360`
- Depends on: `topogpt3/model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/jlens.py`, `topogpt3/jlens.py`

### forward `def forward(self, x, past_kv)`
- Defined: `topogpt3/lens_model.py:366`
- Depends on: `topogpt3/model.py`
- Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/jlens.py`, `topogpt3/jlens.py`

## topogpt3/model.py

### setup_logger `def setup_logger(name, level)`
- Defined: `topogpt3/model.py:192`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### set_seed `def set_seed(seed, device)`
- Defined: `topogpt3/model.py:202`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### build_file_tiers `def build_file_tiers(paths, short, med)`
- Defined: `topogpt3/model.py:1716`
- Doc: Classify file paths into complexity tiers by line count.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### apply_quantization `def apply_quantization(model, config)`
- Defined: `topogpt3/model.py:1973`
- Doc: Quantize embedding and lm_head layers for reduced VRAM usage.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### _tokenize_text_to_memmap `def _tokenize_text_to_memmap(text, tokenizer, path, max_tokens)`
- Defined: `topogpt3/model.py:2141`
- Doc: Tokenize a single text string and write tokens to disk as raw int64.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### main `def main()`
- Defined: `topogpt3/model.py:3568`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### __post_init__ `def __post_init__(self)`
- Defined: `topogpt3/model.py:161`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### hamilton_product `def hamilton_product(q1, q2)`
- Defined: `topogpt3/model.py:222`
- Doc: Producto de Hamilton q1 ⊗ q2. Ambos [..., 4].
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### normalize `def normalize(q, eps)`
- Defined: `topogpt3/model.py:234`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### conjugate `def conjugate(q)`
- Defined: `topogpt3/model.py:238`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### rotate_vector `def rotate_vector(v, q)`
- Defined: `topogpt3/model.py:243`
- Doc: Rota vector 3D v por cuaternión unitario q. v:[...,3] q:[...,4]
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### __init__ `def __init__(self, in_features, out_features, bias)`
- Defined: `topogpt3/model.py:265`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### forward `def forward(self, x)`
- Defined: `topogpt3/model.py:281`
- Doc: x: [..., in_features] → [..., out_features]
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### __init__ `def __init__(self, in_q, out_q, grid_h, grid_w, init_scale)`
- Defined: `topogpt3/model.py:318`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### _kernel `def _kernel(self, c)`
- Defined: `topogpt3/model.py:337`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### _contract `def _contract(self, W, X)`
- Defined: `topogpt3/model.py:340`
- Doc: Suma sobre canales in_q: Y[b,o,h,w] = Σ_i W[i,o,h,w]·X[b,i,h,w]
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### forward `def forward(self, x)`
- Defined: `topogpt3/model.py:344`
- Doc: x: [B, 4*in_q, H, W]  (4 canales cuaterniones sobre grid espacial)
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### __init__ `def __init__(self, config)`
- Defined: `topogpt3/model.py:398`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### _filter1d `def _filter1d(self, x, kr, ki)`
- Defined: `topogpt3/model.py:430`
- Doc: Filtro espectral 1D: x[..., D] → filtrado[..., D]
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### encode `def encode(self, x)`
- Defined: `topogpt3/model.py:436`
- Doc: x: [..., D_MODEL] → latent: [..., D_LAT]
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### decode `def decode(self, z)`
- Defined: `topogpt3/model.py:441`
- Doc: z: [..., D_LAT] → recon: [..., D_MODEL]
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### forward `def forward(self, x)`
- Defined: `topogpt3/model.py:446`
- Doc: Devuelve (latent, recon_loss)
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### process_torus_grid `def process_torus_grid(self, grid)`
- Defined: `topogpt3/model.py:453`
- Doc: Procesa el grid del toro con QuaternionSpectralLayer.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### __init__ `def __init__(self, d_model, config)`
- Defined: `topogpt3/model.py:486`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### _build_torus_graph `def _build_torus_graph(self)`
- Defined: `topogpt3/model.py:526`
- Doc: Construye las aristas del grafo toro 2×4.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### _torus_soft_assign `def _torus_soft_assign(self, phi1, phi2)`
- Defined: `topogpt3/model.py:560`
- Doc: Asignación blanda de tokens a los 8 nodos del toro via distancia circular.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### _message_passing `def _message_passing(self, node_feat)`
- Defined: `topogpt3/model.py:587`
- Doc: Message-passing VECTORIZADO con rotaciones cuaterniones.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### forward `def forward(self, x)`
- Defined: `topogpt3/model.py:624`
- Doc: x: [B, S, D_MODEL]
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### __init__ `def __init__(self, d_head, max_seq_len, base)`
- Defined: `topogpt3/model.py:697`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### _build_cache `def _build_cache(self, seq_len)`
- Defined: `topogpt3/model.py:703`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### _rotate_half `def _rotate_half(self, x)`
- Defined: `topogpt3/model.py:711`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### forward `def forward(self, q, k, seq_len, offset)`
- Defined: `topogpt3/model.py:715`
- Doc: q, k: [B, n_heads, S_q/S_k, d_head]
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### __init__ `def __init__(self, d_model, eps)`
- Defined: `topogpt3/model.py:742`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### forward `def forward(self, x)`
- Defined: `topogpt3/model.py:747`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### __init__ `def __init__(self, d_model, expansion, dropout)`
- Defined: `topogpt3/model.py:763`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### forward `def forward(self, x)`
- Defined: `topogpt3/model.py:777`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### __init__ `def __init__(self, d_model, config)`
- Defined: `topogpt3/model.py:800`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### _route `def _route(self, x)`
- Defined: `topogpt3/model.py:821`
- Doc: x: [N, D] donde N = B*S (tokens aplanados)
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### forward `def forward(self, x)`
- Defined: `topogpt3/model.py:863`
- Doc: x: [B, S, D]
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### __init__ `def __init__(self, d_model, n_heads, config)`
- Defined: `topogpt3/model.py:900`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### forward `def forward(self, x, is_causal, past_kv)`
- Defined: `topogpt3/model.py:919`
- Doc: Args:
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### __init__ `def __init__(self, d_model, n_heads, config)`
- Defined: `topogpt3/model.py:1003`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### _forward_impl `def _forward_impl(self, x, past_kv)`
- Defined: `topogpt3/model.py:1012`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### forward `def forward(self, x, past_kv)`
- Defined: `topogpt3/model.py:1021`
- Doc: Retorna (x_out, aux_loss, kv_cache).
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### __init__ `def __init__(self, config)`
- Defined: `topogpt3/model.py:1052`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### _init_weights `def _init_weights(self)`
- Defined: `topogpt3/model.py:1077`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### forward `def forward(self, token_ids, past_kvs)`
- Defined: `topogpt3/model.py:1084`
- Doc: token_ids: [B, S]  (enteros)
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### forward_with_memory `def forward_with_memory(self, token_ids)`
- Defined: `topogpt3/model.py:1107`
- Doc: Process long sequences with latent memory-token context compression.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### count_params `def count_params(self)`
- Defined: `topogpt3/model.py:1157`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### generate `def generate(self, token_ids, max_new_tokens, temperature, top_k, repetition_penalty)`
- Defined: `topogpt3/model.py:1163`
- Doc: Autoregressive generation with KV cache and top-k sampling.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### generate_with_continuation `def generate_with_continuation(self, token_ids, tokenizer, max_new_tokens, temperature, top_k, repetition_penalty, max_continuations, tail_lines)`
- Defined: `topogpt3/model.py:1214`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### __init__ `def __init__(self, encoding)`
- Defined: `topogpt3/model.py:1261`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### encode `def encode(self, text)`
- Defined: `topogpt3/model.py:1269`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### decode `def decode(self, tokens)`
- Defined: `topogpt3/model.py:1272`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### eot_token `def eot_token(self)`
- Defined: `topogpt3/model.py:1275`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### __init__ `def __init__(self, root, cache_dir, logger)`
- Defined: `topogpt3/model.py:1387`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### scan `def scan(self, force)`
- Defined: `topogpt3/model.py:1394`
- Doc: Walk directory tree collecting text file paths. Cached to disk.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### __init__ `def __init__(self, cache_dir, logger)`
- Defined: `topogpt3/model.py:1461`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### tokenize `def tokenize(self, file_paths, tokenizer, cache_key, max_tokens, min_chars)`
- Defined: `topogpt3/model.py:1466`
- Doc: Tokenize all files and return a memory-mapped numpy array.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### __init__ `def __init__(self, tokens, seq_len)`
- Defined: `topogpt3/model.py:1549`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### __len__ `def __len__(self)`
- Defined: `topogpt3/model.py:1554`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### __getitem__ `def __getitem__(self, idx)`
- Defined: `topogpt3/model.py:1557`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### __init__ `def __init__(self, config, logger)`
- Defined: `topogpt3/model.py:1577`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### _compute_entropy `def _compute_entropy(self, text)`
- Defined: `topogpt3/model.py:1586`
- Doc: Shannon entropy of byte frequencies (bits per byte).
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### _has_long_lines `def _has_long_lines(self, text, threshold)`
- Defined: `topogpt3/model.py:1600`
- Doc: Return True if any line exceeds threshold characters.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### _special_token_ratio `def _special_token_ratio(self, text, tokenizer)`
- Defined: `topogpt3/model.py:1607`
- Doc: Fraction of tokens that are pure whitespace or indentation-only.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### _content_hash `def _content_hash(self, text)`
- Defined: `topogpt3/model.py:1621`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### filter_file `def filter_file(self, path, tokenizer)`
- Defined: `topogpt3/model.py:1624`
- Doc: Read and evaluate a file. Returns text if passed, None if filtered.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### report `def report(self)`
- Defined: `topogpt3/model.py:1664`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### __init__ `def __init__(self, tokens, seq_len, file_tiers, active_tier, logger)`
- Defined: `topogpt3/model.py:1685`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### _update_len `def _update_len(self)`
- Defined: `topogpt3/model.py:1695`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### set_tier `def set_tier(self, tier)`
- Defined: `topogpt3/model.py:1701`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### __len__ `def __len__(self)`
- Defined: `topogpt3/model.py:1705`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### __getitem__ `def __getitem__(self, idx)`
- Defined: `topogpt3/model.py:1708`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### __init__ `def __init__(self, base_trainer)`
- Defined: `topogpt3/model.py:1753`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### _build_dataloader `def _build_dataloader(self, dataset, seq_len, batch_size, is_train)`
- Defined: `topogpt3/model.py:1759`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### run `def run(self, train_paths, val_paths, tokenizer, file_tiers, phases)`
- Defined: `topogpt3/model.py:1769`
- Doc: Run training with progressive sequence length across phases.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### __init__ `def __init__(self, target_model, config, logger)`
- Defined: `topogpt3/model.py:1827`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### _build_draft `def _build_draft(self)`
- Defined: `topogpt3/model.py:1835`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### generate `def generate(self, token_ids, max_new_tokens, temperature, top_k, repetition_penalty)`
- Defined: `topogpt3/model.py:1849`
- Doc: Autoregressive generation via speculative decoding.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### __init__ `def __init__(self, embed, mode)`
- Defined: `topogpt3/model.py:1940`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### forward `def forward(self, indices)`
- Defined: `topogpt3/model.py:1969`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### __init__ `def __init__(self, model, config, tokenizer)`
- Defined: `topogpt3/model.py:2009`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### cache_tokens `def cache_tokens(self, key, tokens)`
- Defined: `topogpt3/model.py:2016`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### model `def model(self)`
- Defined: `topogpt3/model.py:2020`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### optimizer `def optimizer(self)`
- Defined: `topogpt3/model.py:2024`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### scaler `def scaler(self)`
- Defined: `topogpt3/model.py:2028`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### amp_dtype `def amp_dtype(self)`
- Defined: `topogpt3/model.py:2032`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### completed_epochs `def completed_epochs(self)`
- Defined: `topogpt3/model.py:2036`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### completed_epochs `def completed_epochs(self, v)`
- Defined: `topogpt3/model.py:2040`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### global_step `def global_step(self)`
- Defined: `topogpt3/model.py:2044`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### global_step `def global_step(self, v)`
- Defined: `topogpt3/model.py:2048`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### best_val_loss `def best_val_loss(self)`
- Defined: `topogpt3/model.py:2052`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### best_val_loss `def best_val_loss(self, v)`
- Defined: `topogpt3/model.py:2056`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### history `def history(self)`
- Defined: `topogpt3/model.py:2060`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### ckpt_mgr `def ckpt_mgr(self)`
- Defined: `topogpt3/model.py:2064`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### resume `def resume(self)`
- Defined: `topogpt3/model.py:2067`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### _current_state `def _current_state(self)`
- Defined: `topogpt3/model.py:2070`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### _cosine_lr `def _cosine_lr(self)`
- Defined: `topogpt3/model.py:2073`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### _set_lr `def _set_lr(self)`
- Defined: `topogpt3/model.py:2076`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### evaluate `def evaluate(self, dataloader)`
- Defined: `topogpt3/model.py:2079`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### _sample_text `def _sample_text(self)`
- Defined: `topogpt3/model.py:2082`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### _progressive_train `def _progressive_train(self, train_paths, val_paths, tokenizer, phases, memtok)`
- Defined: `topogpt3/model.py:2085`
- Doc: Training loop with progressive sequence length across phases.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### train `def train(self, train_dl, val_dl)`
- Defined: `topogpt3/model.py:2124`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### run_curriculum `def run_curriculum(self, train_paths, val_paths, tokenizer, phases)`
- Defined: `topogpt3/model.py:2127`
- Doc: Top-level entry point: curriculum + progressive seq len.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### __init__ `def __init__(self, config, logger)`
- Defined: `topogpt3/model.py:2178`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### patch_config_for_resume `def patch_config_for_resume(self, cfg)`
- Defined: `topogpt3/model.py:2188`
- Doc: Lee el checkpoint 'latest' y ajusta cfg.N_KV_HEADS / cfg.GQA_GROUPS
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### _save_model `def _save_model(self, model, directory)`
- Defined: `topogpt3/model.py:2217`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### _load_model `def _load_model(self, model, directory)`
- Defined: `topogpt3/model.py:2230`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### _save_optimizer `def _save_optimizer(self, optimizer, directory)`
- Defined: `topogpt3/model.py:2261`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### _load_optimizer `def _load_optimizer(self, optimizer, directory, device)`
- Defined: `topogpt3/model.py:2264`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### _save_state `def _save_state(self, state, directory)`
- Defined: `topogpt3/model.py:2273`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### _load_state `def _load_state(self, directory)`
- Defined: `topogpt3/model.py:2278`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### should_save `def should_save(self)`
- Defined: `topogpt3/model.py:2289`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### save `def save(self, model, optimizer, state, is_best)`
- Defined: `topogpt3/model.py:2292`
- Doc: Guarda checkpoint completo.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### load_latest `def load_latest(self, model, optimizer)`
- Defined: `topogpt3/model.py:2337`
- Doc: Carga el ultimo checkpoint guardado.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### load_best `def load_best(self, model)`
- Defined: `topogpt3/model.py:2364`
- Doc: Carga el mejor modelo guardado (solo pesos, sin optimizador).
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### has_checkpoint `def has_checkpoint(self)`
- Defined: `topogpt3/model.py:2376`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### __init__ `def __init__(self, model, config, tokenizer)`
- Defined: `topogpt3/model.py:2398`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### resume `def resume(self)`
- Defined: `topogpt3/model.py:2433`
- Doc: Carga el ultimo checkpoint disponible.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### _current_state `def _current_state(self)`
- Defined: `topogpt3/model.py:2458`
- Doc: Construye el dict de estado para persistir en state.json.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### _cosine_lr `def _cosine_lr(self, step_in_session, total_steps_session)`
- Defined: `topogpt3/model.py:2469`
- Doc: Cosine decay con warmup. El schedule es relativo a la sesion actual.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### _set_lr `def _set_lr(self, lr)`
- Defined: `topogpt3/model.py:2477`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### train `def train(self, train_dl, val_dl)`
- Defined: `topogpt3/model.py:2481`
- Doc: Entrena cfg.EPOCHS epocas adicionales a partir de completed_epochs.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### _sample_text `def _sample_text(self, tokenizer, prompts, max_new, temperature, top_k)`
- Defined: `topogpt3/model.py:2617`
- Doc: Genera una muestra de texto al final de cada epoch para monitorear
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### evaluate `def evaluate(self, dataloader)`
- Defined: `topogpt3/model.py:2649`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### __init__ `def __init__(self, config)`
- Defined: `topogpt3/model.py:2699`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### compute_delta `def compute_delta(self, model)`
- Defined: `topogpt3/model.py:2707`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### compute_alpha `def compute_alpha(self, delta)`
- Defined: `topogpt3/model.py:2714`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### update_grad_buffer `def update_grad_buffer(self, model)`
- Defined: `topogpt3/model.py:2719`
- Doc: Captura gradientes de forma segura, ignorando tensores corruptos.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### compute_t_eff `def compute_t_eff(self, lr)`
- Defined: `topogpt3/model.py:2745`
- Doc: T_eff = lr/2 * Var(gradiente). Temperatura termodinamica efectiva.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### compute_kappa `def compute_kappa(self, model, dataloader, n_batches)`
- Defined: `topogpt3/model.py:2753`
- Doc: κ = λ_max / λ_min de la covarianza del gradiente.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### compute_berry_phase `def compute_berry_phase(self, model)`
- Defined: `topogpt3/model.py:2811`
- Doc: Fase de Berry de los kernels espectrales imaginarios.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### compute_lc `def compute_lc(self, model)`
- Defined: `topogpt3/model.py:2824`
- Doc: Complejidad local: 1 - similitud coseno promedio entre filas de pesos.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### compute_sp `def compute_sp(self, model)`
- Defined: `topogpt3/model.py:2838`
- Doc: Superposicion: correlacion inter-fila promedio (entrelazamiento de features).
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### classify_phase `def classify_phase(self, delta, kappa, berry)`
- Defined: `topogpt3/model.py:2854`
- Doc: Clasificacion de fase segun Book.md:
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### compute_all `def compute_all(self, model, lr, dataloader, compute_kappa)`
- Defined: `topogpt3/model.py:2873`
- Doc: Calcula todas las metricas.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### format_log `def format_log(self, m)`
- Defined: `topogpt3/model.py:2898`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### __init__ `def __init__(self, config, logger)`
- Defined: `topogpt3/model.py:2934`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### _measure_ratio `def _measure_ratio(self, ratio, sample_batch)`
- Defined: `topogpt3/model.py:2938`
- Doc: Mide la coherencia espectral para un ratio dado.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### optimize `def optimize(self, dataloader)`
- Defined: `topogpt3/model.py:2967`
- Doc: Retorna el mejor ratio de inicializacion de kernels espectrales.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### __init__ `def __init__(self, config, logger)`
- Defined: `topogpt3/model.py:3007`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### prospect `def prospect(self, candidates, train_dataset, prospect_steps)`
- Defined: `topogpt3/model.py:3011`
- Doc: Retorna el mejor batch size segun delta y T_eff.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### __init__ `def __init__(self, config, logger)`
- Defined: `topogpt3/model.py:3090`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### mine `def mine(self, seed_start, n_seeds, train_dataset, prospect_steps)`
- Defined: `topogpt3/model.py:3094`
- Doc: Retorna la semilla con la mejor trayectoria de delta.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### __init__ `def __init__(self, trainer, t0, cooling_rate, stagnation_patience)`
- Defined: `topogpt3/model.py:3176`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### refine `def refine(self, train_dl, val_dl, refine_epochs)`
- Defined: `topogpt3/model.py:3185`
- Doc: Ejecuta refine_epochs epocas de recocido simulado.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### __init__ `def __init__(self, config, train_tokens, val_tokens, tokenizer, logger, curriculum_tiers, progressive_seq)`
- Defined: `topogpt3/model.py:3328`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### _build_dataloader `def _build_dataloader(self, tokens, seq_len, batch_size, shuffle, tag)`
- Defined: `topogpt3/model.py:3341`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### _build_phases `def _build_phases(self)`
- Defined: `topogpt3/model.py:3355`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### run `def run(self, run_prospect, refine_epochs, resume, prospect_steps, probe_seeds, seed_start)`
- Defined: `topogpt3/model.py:3364`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### __init__ `def __init__(self, config, train_dataset, val_dataset, tokenizer, logger)`
- Defined: `topogpt3/model.py:3466`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### _make_dataloaders `def _make_dataloaders(self, batch_size)`
- Defined: `topogpt3/model.py:3476`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### run `def run(self, run_prospect, refine_epochs, resume, prospect_steps, probe_seeds, seed_start)`
- Defined: `topogpt3/model.py:3488`
- Doc: Ejecuta el pipeline completo.
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

### ckpt_fn `def ckpt_fn(x_in)`
- Defined: `topogpt3/model.py:1029`
- Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`
- Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_lens_model.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/lens_model.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`

## topogpt3/train.py

### _gauss_complex_contract `def _gauss_complex_contract(self, W, X)`
- Defined: `topogpt3/train.py:532`
- Doc: Sustituye QuaternionSpectralLayer._contract usando el truco de Gauss.
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### apply_gauss_patch `def apply_gauss_patch(logger)`
- Defined: `topogpt3/train.py:568`
- Doc: Activa la version Gauss de _contract en QuaternionSpectralLayer.
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### parse_args `def parse_args()`
- Defined: `topogpt3/train.py:1538`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### main `def main()`
- Defined: `topogpt3/train.py:1567`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### build_topogpt2_config `def build_topogpt2_config(self, max_seq_len, attn_window)`
- Defined: `topogpt3/train.py:170`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __init__ `def __init__(self, config, logger)`
- Defined: `topogpt3/train.py:217`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### _stack_spectral_kernels `def _stack_spectral_kernels(model)`
- Defined: `topogpt3/train.py:231`
- Doc: Devuelve K(theta) en C^{N_f x N_c}:
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### _elbow_rank `def _elbow_rank(self, sigmas)`
- Defined: `topogpt3/train.py:268`
- Doc: Punto donde el valor singular cae por debajo de elbow_ratio * sigma_max.
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### _dominant_subspace `def _dominant_subspace(self, K)`
- Defined: `topogpt3/train.py:277`
- Doc: SVD compacta y truncada.
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### _flatten_grads `def _flatten_grads(model, max_per_tensor)`
- Defined: `topogpt3/train.py:295`
- Doc: Concatena un sub-sample de gradientes para mantener costo acotado.
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### estimate_fisher_gap `def estimate_fisher_gap(self, model, dataloader, vocab_size, r_target)`
- Defined: `topogpt3/train.py:313`
- Doc: Sigma_F ~= (1/M) sum_m g_m g_m^T  (covarianza muestral de gradientes).
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### _project_unitary `def _project_unitary(M)`
- Defined: `topogpt3/train.py:381`
- Doc: Proyeccion a U(r) por descomposicion polar (M ~= U H -> retorna U).
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### update_holonomy `def update_holonomy(self, U_new)`
- Defined: `topogpt3/train.py:386`
- Doc: Holonomia discreta:
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### conjugation_distance_su2 `def conjugation_distance_su2(U1, U2)`
- Defined: `topogpt3/train.py:412`
- Doc: Para U1, U2 en U(1)/U(2):  d_conj(U1, U2) = min_g || U1 - g U2 g^{-1} ||_F.
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### _accumulate_winding `def _accumulate_winding(self, U_new)`
- Defined: `topogpt3/train.py:429`
- Doc: W += (1/2pi) * arg det <U_prev | U_new>  acumulado sobre la trayectoria.
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### snapshot `def snapshot(self, model, step, dataloader, vocab_size)`
- Defined: `topogpt3/train.py:445`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### format_log `def format_log(self, snap)`
- Defined: `topogpt3/train.py:500`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### save `def save(self, path)`
- Defined: `topogpt3/train.py:522`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __init__ `def __init__(self, model, config, logger, gauss_enabled)`
- Defined: `topogpt3/train.py:600`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### _embed_params `def _embed_params(model)`
- Defined: `topogpt3/train.py:611`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### measure_throughput `def measure_throughput(self, dataloader, vocab_size)`
- Defined: `topogpt3/train.py:619`
- Doc: Devuelve (tokens_por_segundo, segundos_por_step).
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### estimate_flops_per_step `def estimate_flops_per_step(self, batch_size, seq_len)`
- Defined: `topogpt3/train.py:651`
- Doc: Heuristica: 6 * N_no_embed * tokens (forward + backward).
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### estimate_bytes_per_step `def estimate_bytes_per_step(self, batch_size, seq_len, dtype_bytes)`
- Defined: `topogpt3/train.py:656`
- Doc: Bandwidth aproximada: lectura de pesos + activaciones por step.
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### compute `def compute(self, dataloader, vocab_size, val_loss, val_ppl, val_acc, batch_size, seq_len)`
- Defined: `topogpt3/train.py:664`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### format_log `def format_log(self, m)`
- Defined: `topogpt3/train.py:696`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __init__ `def __init__(self, config, tokenizer, logger)`
- Defined: `topogpt3/train.py:729`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### _format_codealpaca `def _format_codealpaca(ex)`
- Defined: `topogpt3/train.py:746`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### _format_code_feedback `def _format_code_feedback(ex)`
- Defined: `topogpt3/train.py:757`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### _format_magicoder `def _format_magicoder(ex)`
- Defined: `topogpt3/train.py:777`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### _format_tiny_stack `def _format_tiny_stack(ex)`
- Defined: `topogpt3/train.py:785`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### _get_formatter `def _get_formatter(cls, tier)`
- Defined: `topogpt3/train.py:797`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### _tier_paths `def _tier_paths(self, tier)`
- Defined: `topogpt3/train.py:819`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### _manifest_path `def _manifest_path(self, tier)`
- Defined: `topogpt3/train.py:825`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### _already_prepared `def _already_prepared(self, tier)`
- Defined: `topogpt3/train.py:828`
- Doc: True solo si los 3 splits existen, son no-vacios y el manifest concuerda.
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### _load_hf_with_fallback `def _load_hf_with_fallback(self, tier)`
- Defined: `topogpt3/train.py:858`
- Doc: Carga el dataset HF; para tiny_the_stack prueba una cadena de fallbacks
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### prepare_tier `def prepare_tier(self, tier_index, force)`
- Defined: `topogpt3/train.py:891`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### open_memmap `def open_memmap(self, tier, split)`
- Defined: `topogpt3/train.py:986`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __init__ `def __init__(self, tokens, seq_len)`
- Defined: `topogpt3/train.py:1006`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __len__ `def __len__(self)`
- Defined: `topogpt3/train.py:1011`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __getitem__ `def __getitem__(self, idx)`
- Defined: `topogpt3/train.py:1014`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __init__ `def __init__(self, root, max_keep, logger)`
- Defined: `topogpt3/train.py:1030`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### save `def save(self, tag, model, optimizer, state)`
- Defined: `topogpt3/train.py:1037`
- Doc: Guarda checkpoint atomico en <root>/last/ sobreescribiendo el anterior.
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### load_latest `def load_latest(self, model, optimizer)`
- Defined: `topogpt3/train.py:1071`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### should_save `def should_save(self, interval_min)`
- Defined: `topogpt3/train.py:1095`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### __init__ `def __init__(self, config, start_tier)`
- Defined: `topogpt3/train.py:1119`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### prepare_all `def prepare_all(self, force)`
- Defined: `topogpt3/train.py:1174`
- Doc: Prepara cada tier; un fallo en uno no detiene los demas.
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### _build_loaders `def _build_loaders(self, tier_index)`
- Defined: `topogpt3/train.py:1190`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### _cosine_lr `def _cosine_lr(self, step, total_steps)`
- Defined: `topogpt3/train.py:1222`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### _set_lr `def _set_lr(self, lr)`
- Defined: `topogpt3/train.py:1229`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### _train_one_tier `def _train_one_tier(self, tier_index)`
- Defined: `topogpt3/train.py:1237`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### _evaluate `def _evaluate(self, dl)`
- Defined: `topogpt3/train.py:1398`
- Doc: Devuelve (avg_loss, perplexity, token_accuracy).
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### _state_dict `def _state_dict(self)`
- Defined: `topogpt3/train.py:1436`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### run `def run(self)`
- Defined: `topogpt3/train.py:1449`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### _eval_combined_holdout `def _eval_combined_holdout(self)`
- Defined: `topogpt3/train.py:1506`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`

### flush `def flush(split)`
- Defined: `topogpt3/train.py:922`
- Depends on: `topogpt3/model.py`
- Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`
