# Symbols (page 1 of 2)
Pages: [SYMBOLS.md](SYMBOLS.md), [SYMBOLS_p2.md](SYMBOLS_p2.md)

| Symbol | Kind | File:Line | Signature |
|--------|------|-----------|-----------|
| `_build_parser` | function | `app.py:121` | `def _build_parser()` |
| `main` | function | `app.py:159` | `def main(argv)` |
| `run_inference` | function | `app.py:46` | `def run_inference(prompt, checkpoint_dir, checkpoint_name, max_new_tokens, temperature, top_k, repetition_penalty...` |
| `run_inference_hrm` | function | `app.py:71` | `def run_inference_hrm(prompt, checkpoint_dir, checkpoint_name, max_new_tokens, temperature, top_k...` |
| `run_training` | function | `app.py:105` | `def run_training(scale, start_tier, device, prepare_data)` |
| `convert` | function | `convert_weights.py:102` | `def convert(input_path, output_path)` |
| `main` | function | `convert_weights.py:160` | `def main()` |
| `main` | function | `convert_weights_minios.py:85` | `def main()` |
| `main` | function | `encode_tokens.py:19` | `def main()` |
| `classify_error` | function | `eval/analyze.py:32` | `def classify_error(msg, candidate_src)` |
| `load_jsonl` | function | `eval/analyze.py:56` | `def load_jsonl(path)` |
| `main` | function | `eval/analyze.py:103` | `def main()` |
| `pass_at_k` | function | `eval/analyze.py:21` | `def pass_at_k(n, c, k)` |
| `summarize` | function | `eval/analyze.py:61` | `def summarize(paths)` |
| `load_records` | function | `eval/analyze_results.py:26` | `def load_records(path)` |
| `main` | function | `eval/analyze_results.py:82` | `def main()` |
| `show_failures` | function | `eval/analyze_results.py:44` | `def show_failures(records, task_id)` |
| `summarize` | function | `eval/analyze_results.py:31` | `def summarize(records)` |
| `context_length_diagnostic` | function | `eval/diag_static.py:171` | `def context_length_diagnostic(model, tracker, device, lengths)` |
| `main` | function | `eval/diag_static.py:248` | `def main()` |
| `phase_discretization` | function | `eval/diag_static.py:49` | `def phase_discretization(K, n_samples, seed)` |
| `static_kappa` | function | `eval/diag_static.py:144` | `def static_kappa(K)` |
| `synthetic_winding` | function | `eval/diag_static.py:95` | `def synthetic_winding(K, n_windows, window_size)` |
| `GenerationGovernor` | class | `eval/governor.py:134` | `class GenerationGovernor` |
| `GenerationResult` | class | `eval/governor.py:109` | `class GenerationResult` |
| `StopReason` | class | `eval/governor.py:99` | `class StopReason(str, Enum)` |
| `TokenStream` | class | `eval/governor.py:45` | `class TokenStream` |
| `__init__` | method | `eval/governor.py:56` | `def __init__(self)` |
| `__init__` | method | `eval/governor.py:156` | `def __init__(self, model, ctx, stream, max_new_tokens, temperature, top_k, repetition_penalty, max_seq_len)` |
| `__len__` | method | `eval/governor.py:90` | `def __len__(self)` |
| `__post_init__` | method | `eval/governor.py:117` | `def __post_init__(self)` |
| `_should_cancel` | method | `eval/governor.py:182` | `def _should_cancel(self)` |
| `cancel` | method | `eval/governor.py:177` | `def cancel(self)` |
| `drain` | method | `eval/governor.py:72` | `def drain(self)` |
| `hook` | method | `eval/governor.py:292` | `def hook(generated)` |
| `hook` | method | `eval/governor.py:320` | `def hook(generated)` |
| `is_closed` | method | `eval/governor.py:86` | `def is_closed(self)` |
| `make_loop_detector` | method | `eval/governor.py:285` | `def make_loop_detector(window, min_repeats)` |
| `make_timeout_hook` | method | `eval/governor.py:314` | `def make_timeout_hook(per_token_s)` |
| `mark_done` | method | `eval/governor.py:67` | `def mark_done(self)` |
| `put` | method | `eval/governor.py:62` | `def put(self, tok)` |
| `run` | method | `eval/governor.py:185` | `def run(self, stop_hooks)` |
| `wait_for_new` | method | `eval/governor.py:77` | `def wait_for_new(self, timeout)` |
| `consumer` | function | `eval/governor_smoke.py:59` | `def consumer()` |
| `load_model` | function | `eval/governor_smoke.py:30` | `def load_model()` |
| `producer` | function | `eval/governor_smoke.py:53` | `def producer()` |
| `test_cancel` | function | `eval/governor_smoke.py:118` | `def test_cancel()` |
| `test_governor_basic` | function | `eval/governor_smoke.py:79` | `def test_governor_basic()` |
| `test_loop_detector` | function | `eval/governor_smoke.py:98` | `def test_loop_detector()` |
| `test_tokenstream_threadsafety` | function | `eval/governor_smoke.py:49` | `def test_tokenstream_threadsafety()` |
| `ModelLoader` | class | `eval/harness.py:217` | `class ModelLoader` |
| `__init__` | method | `eval/harness.py:220` | `def __init__(self, ckpt_dir, ckpt_name, device)` |
| `build_prompt` | function | `eval/harness.py:75` | `def build_prompt(problem)` |
| `completion_for_problem` | function | `eval/harness.py:204` | `def completion_for_problem(sampler, prompt)` |
| `evaluate_problem` | method | `eval/harness.py:272` | `def evaluate_problem(problem, loader, args, sample_idx)` |
| `extract_candidate` | function | `eval/harness.py:100` | `def extract_candidate(prompt, completion)` |
| `generate` | method | `eval/harness.py:246` | `def generate(self, prompt, max_new_tokens, temperature, top_k, repetition_penalty)` |
| `load_humaneval` | function | `eval/harness.py:59` | `def load_humaneval(cache_dir)` |
| `main` | method | `eval/harness.py:315` | `def main()` |
| `make_sampler` | function | `eval/harness.py:195` | `def make_sampler(mode, settings_kwargs)` |
| `run_one_test` | function | `eval/harness.py:150` | `def run_one_test(problem, candidate_src, timeout)` |
| `run_one_test_sandboxed` | function | `eval/harness.py:172` | `def run_one_test_sandboxed(problem, candidate_src, timeout, sandbox_cfg)` |
| `main` | function | `eval/integration_smoke.py:18` | `def main()` |
| `_load` | function | `eval/noise_analysis.py:43` | `def _load(p)` |
| `consistency_across_runs` | function | `eval/noise_analysis.py:47` | `def consistency_across_runs(per_run)` |
| `main` | function | `eval/noise_analysis.py:83` | `def main()` |
| `generate_one` | function | `eval/noise_sweep.py:99` | `def generate_one(model, tok, prompt, max_new_tokens, device)` |
| `inject_noise` | function | `eval/noise_sweep.py:46` | `def inject_noise(model, sigma, seed)` |
| `load_model` | function | `eval/noise_sweep.py:74` | `def load_model(ckpt_dir, ckpt_name, device)` |
| `main` | function | `eval/noise_sweep.py:117` | `def main()` |
| `_new_loader` | function | `eval/repair.py:36` | `def _new_loader(ckpt_dir, ckpt_name)` |
| `build_repair_prompt` | function | `eval/repair.py:89` | `def build_repair_prompt(prompt, candidate, err, entry_point)` |
| `extract_candidate` | function | `eval/repair.py:49` | `def extract_candidate(prompt, completion)` |
| `gen` | function | `eval/repair.py:104` | `def gen(model, tok, text, max_new_tokens, temperature, top_k, rep_penalty)` |
| `main` | function | `eval/repair.py:119` | `def main()` |
| `run_test` | function | `eval/repair.py:75` | `def run_test(problem, candidate_src)` |
| `classify_error` | function | `eval/report.py:31` | `def classify_error(msg)` |
| `load_jsonl` | function | `eval/report.py:52` | `def load_jsonl(p)` |
| `main` | function | `eval/report.py:117` | `def main()` |
| `pass_at_k` | function | `eval/report.py:25` | `def pass_at_k(n, c, k)` |
| `repair_summary` | function | `eval/report.py:90` | `def repair_summary(repair_path, baseline_path)` |
| `summarize_run` | function | `eval/report.py:56` | `def summarize_run(p)` |
| `_is_env_truthy` | function | `eval/samplers.py:55` | `def _is_env_truthy(name)` |
| `_make_hrm` | function | `eval/samplers.py:69` | `def _make_hrm(settings_kwargs)` |
| `_make_standard` | function | `eval/samplers.py:64` | `def _make_standard(settings_kwargs)` |
| `build_sampler` | function | `eval/samplers.py:90` | `def build_sampler(mode, settings_kwargs)` |
| `deco` | function | `eval/samplers.py:42` | `def deco(fn)` |
| `list_samplers` | function | `eval/samplers.py:86` | `def list_samplers()` |
| `register_sampler` | function | `eval/samplers.py:36` | `def register_sampler(name)` |
| `SandboxConfig` | class | `eval/sandbox.py:53` | `class SandboxConfig` |
| `_blocked_dunder_access` | method | `eval/sandbox.py:114` | `def _blocked_dunder_access(tree, blocked)` |
| `_build_worker_src` | method | `eval/sandbox.py:254` | `def _build_worker_src(allowed_builtin_names, program_src, blocked_modules)` |
| `_max_depth` | method | `eval/sandbox.py:123` | `def _max_depth(tree)` |
| `_names_imported` | method | `eval/sandbox.py:100` | `def _names_imported(tree)` |
| `check_safety` | method | `eval/sandbox.py:133` | `def check_safety(source, cfg)` |
| `d` | method | `eval/sandbox.py:125` | `def d(node, cur)` |
| `describe_policy` | method | `eval/sandbox.py:373` | `def describe_policy(cfg)` |
| `safe_exec` | method | `eval/sandbox.py:270` | `def safe_exec(program_src, cfg, extra_globals)` |
| `main` | function | `eval/sandbox_smoke.py:15` | `def main()` |
| `run_hrm` | function | `eval/smoke.py:36` | `def run_hrm()` |
| `run_standard` | function | `eval/smoke.py:17` | `def run_standard()` |
| `evaluate_problems` | function | `eval/temp_sweep.py:58` | `def evaluate_problems(model, tok, problems, max_new_tokens, temperature, top_k, n_samples, device)` |
| `generate_one` | function | `eval/temp_sweep.py:39` | `def generate_one(model, tok, prompt, max_new_tokens, temperature, top_k, device, seed_offset)` |
| `main` | function | `eval/temp_sweep.py:116` | `def main()` |
| `pass_at_k_unbiased` | function | `eval/temp_sweep.py:88` | `def pass_at_k_unbiased(n, c, k)` |
| `summarize` | function | `eval/temp_sweep.py:96` | `def summarize(results, n_samples)` |
| `build_ui` | function | `gradio_app.py:144` | `def build_ui()` |
| `ensure_checkpoint` | function | `gradio_app.py:35` | `def ensure_checkpoint()` |
| `run_hrm_inference` | function | `gradio_app.py:95` | `def run_hrm_inference(prompt, max_new_tokens, temperature, top_k, repetition_penalty, high_level_iters...` |
| `run_standard_inference` | function | `gradio_app.py:59` | `def run_standard_inference(prompt, max_new_tokens, temperature, top_k, repetition_penalty, auto_continue)` |
| `GroqBackend` | class | `synthetic_dataset.py:71` | `class GroqBackend(LLMBackend)` |
| `LLMBackend` | class | `synthetic_dataset.py:61` | `class LLMBackend` |
| `OllamaBackend` | class | `synthetic_dataset.py:177` | `class OllamaBackend(LLMBackend)` |
| `OpenRouterBackend` | class | `synthetic_dataset.py:121` | `class OpenRouterBackend(LLMBackend)` |
| `ProcessedManifest` | class | `synthetic_dataset.py:364` | `class ProcessedManifest` |
| `SyntheticDatasetGenerator` | class | `synthetic_dataset.py:399` | `class SyntheticDatasetGenerator` |
| `__init__` | method | `synthetic_dataset.py:78` | `def __init__(self, model, api_key, max_tokens, temperature, timeout)` |
| `__init__` | method | `synthetic_dataset.py:132` | `def __init__(self, model, api_key, max_tokens, temperature, timeout)` |
| `__init__` | method | `synthetic_dataset.py:184` | `def __init__(self, model, host, max_tokens, temperature, timeout)` |
| `__init__` | method | `synthetic_dataset.py:418` | `def __init__(self, backend, output_path, manifest_path, logger, max_workers, max_file_chars)` |
| `_build_prompt` | method | `synthetic_dataset.py:490` | `def _build_prompt(self, content, lang)` |
| `_enqueue_sample` | method | `synthetic_dataset.py:465` | `def _enqueue_sample(self, sample)` |
| `_flush_writer` | method | `synthetic_dataset.py:468` | `def _flush_writer(self)` |
| `_generate_sample` | method | `synthetic_dataset.py:496` | `def _generate_sample(self, content, lang)` |
| `_jsonl_writer` | method | `synthetic_dataset.py:447` | `def _jsonl_writer(self)` |
| `_read_file` | method | `synthetic_dataset.py:477` | `def _read_file(self, path)` |
| `build_backend` | method | `synthetic_dataset.py:227` | `def build_backend(provider, model)` |
| `build_logger` | method | `synthetic_dataset.py:614` | `def build_logger(level)` |
| `finish` | method | `synthetic_dataset.py:590` | `def finish(self)` |
| `generate` | method | `synthetic_dataset.py:64` | `def generate(self, prompt)` |
| `generate` | method | `synthetic_dataset.py:98` | `def generate(self, prompt)` |
| `generate` | method | `synthetic_dataset.py:154` | `def generate(self, prompt)` |
| `generate` | method | `synthetic_dataset.py:201` | `def generate(self, prompt)` |
| `load` | method | `synthetic_dataset.py:374` | `def load(path)` |
| `load_paths` | method | `synthetic_dataset.py:652` | `def load_paths(paths_arg, paths_file, max_files)` |
| `main` | method | `synthetic_dataset.py:667` | `def main()` |
| `name` | method | `synthetic_dataset.py:67` | `def name(self)` |
| `name` | method | `synthetic_dataset.py:95` | `def name(self)` |
| `name` | method | `synthetic_dataset.py:151` | `def name(self)` |
| `name` | method | `synthetic_dataset.py:198` | `def name(self)` |
| `parse_args` | method | `synthetic_dataset.py:625` | `def parse_args()` |
| `process_batch` | method | `synthetic_dataset.py:568` | `def process_batch(self, paths)` |
| `process_file` | method | `synthetic_dataset.py:533` | `def process_file(self, path)` |
| `save` | method | `synthetic_dataset.py:387` | `def save(self, path)` |
| `validate_sample` | method | `synthetic_dataset.py:330` | `def validate_sample(sample)` |
| `_micro` | function | `tests/test_heritage.py:18` | `def _micro()` |
| `test_chat_template_tools_think` | function | `tests/test_heritage.py:24` | `def test_chat_template_tools_think()` |
| `test_distill_loss_finite` | function | `tests/test_heritage.py:96` | `def test_distill_loss_finite()` |
| `test_dpo_grpo_losses_finite` | function | `tests/test_heritage.py:76` | `def test_dpo_grpo_losses_finite()` |
| `test_lora_save_load` | function | `tests/test_heritage.py:64` | `def test_lora_save_load(tmp_path)` |
| `test_lora_zero_init_and_quaternion_targets` | function | `tests/test_heritage.py:47` | `def test_lora_zero_init_and_quaternion_targets()` |
| `test_rollout_engine_micro` | function | `tests/test_heritage.py:106` | `def test_rollout_engine_micro()` |
| `test_tools_and_eval` | function | `tests/test_heritage.py:123` | `def test_tools_and_eval()` |
| `test_yarn_changes_freqs_only` | function | `tests/test_heritage.py:37` | `def test_yarn_changes_freqs_only()` |
| `TestConfig` | class | `tests/test_jlens.py:473` | `class TestConfig` |
| `TestFit` | class | `tests/test_jlens.py:172` | `class TestFit` |
| `TestFitCheckpoint` | class | `tests/test_jlens.py:367` | `class TestFitCheckpoint` |
| `TestJacobianForPrompt` | class | `tests/test_jlens.py:52` | `class TestJacobianForPrompt` |
| `TestJacobianLens` | class | `tests/test_jlens.py:210` | `class TestJacobianLens` |
| `TestTopoGPT3JLensAppConfig` | class | `tests/test_jlens.py:494` | `class TestTopoGPT3JLensAppConfig` |
| `TestValidPositionMask` | class | `tests/test_jlens.py:17` | `class TestValidPositionMask` |
| `fitted_lens` | method | `tests/test_jlens.py:222` | `def fitted_lens(self, model)` |
| `model` | method | `tests/test_jlens.py:56` | `def model(self)` |
| `model` | method | `tests/test_jlens.py:176` | `def model(self)` |
| `model` | method | `tests/test_jlens.py:214` | `def model(self)` |
| `model` | method | `tests/test_jlens.py:371` | `def model(self)` |
| `test_all_positions_valid` | method | `tests/test_jlens.py:39` | `def test_all_positions_valid(self)` |
| `test_app_config_defaults` | method | `tests/test_jlens.py:485` | `def test_app_config_defaults(self)` |
| `test_apply_returns_correct_shapes` | method | `tests/test_jlens.py:242` | `def test_apply_returns_correct_shapes(self, fitted_lens, model)` |
| `test_apply_with_explicit_positions` | method | `tests/test_jlens.py:263` | `def test_apply_with_explicit_positions(self, fitted_lens, model)` |
| `test_basic_mask` | method | `tests/test_jlens.py:20` | `def test_basic_mask(self)` |
| `test_checkpoint_mismatch_raises` | method | `tests/test_jlens.py:450` | `def test_checkpoint_mismatch_raises(self, model, tmp_path)` |
| `test_checkpoint_resume_produces_same_result` | method | `tests/test_jlens.py:378` | `def test_checkpoint_resume_produces_same_result(self, model, tmp_path)` |
| `test_custom_config` | method | `tests/test_jlens.py:505` | `def test_custom_config(self)` |
| `test_default_config` | method | `tests/test_jlens.py:497` | `def test_default_config(self)` |
| `test_earlier_layers_further_from_identity` | method | `tests/test_jlens.py:85` | `def test_earlier_layers_further_from_identity(self, model)` |
| `test_exact_jacobian_for_last_block` | method | `tests/test_jlens.py:95` | `def test_exact_jacobian_for_last_block(self, model)` |
| `test_exact_minimum_length` | method | `tests/test_jlens.py:45` | `def test_exact_minimum_length(self)` |
| `test_fit_config_defaults` | method | `tests/test_jlens.py:476` | `def test_fit_config_defaults(self)` |
| `test_fit_empty_prompts_raises` | method | `tests/test_jlens.py:191` | `def test_fit_empty_prompts_raises(self, model)` |
| `test_fit_returns_lens_with_correct_attributes` | method | `tests/test_jlens.py:183` | `def test_fit_returns_lens_with_correct_attributes(self, model)` |
| `test_fit_skips_short_prompts` | method | `tests/test_jlens.py:196` | `def test_fit_skips_short_prompts(self, model)` |
| `test_fit_with_default_source_layers` | method | `tests/test_jlens.py:202` | `def test_fit_with_default_source_layers(self, model)` |
| `test_fitted_late_layer_matches_model` | method | `tests/test_jlens.py:254` | `def test_fitted_late_layer_matches_model(self, fitted_lens, model)` |
| `test_from_pretrained_local_directory` | method | `tests/test_jlens.py:351` | `def test_from_pretrained_local_directory(self, fitted_lens, tmp_path)` |
| `test_from_pretrained_local_file` | method | `tests/test_jlens.py:344` | `def test_from_pretrained_local_file(self, fitted_lens, tmp_path)` |
| `test_late_layer_jacobian_close_to_identity` | method | `tests/test_jlens.py:76` | `def test_late_layer_jacobian_close_to_identity(self, model)` |
| `test_load_invalid_file_raises` | method | `tests/test_jlens.py:337` | `def test_load_invalid_file_raises(self, tmp_path)` |
| `test_logit_lens_baseline` | method | `tests/test_jlens.py:274` | `def test_logit_lens_baseline(self, fitted_lens, model)` |
| `test_merge_empty_raises` | method | `tests/test_jlens.py:326` | `def test_merge_empty_raises(self)` |
| `test_merge_mismatch_raises` | method | `tests/test_jlens.py:319` | `def test_merge_mismatch_raises(self)` |
| `test_merge_weighted_mean` | method | `tests/test_jlens.py:291` | `def test_merge_weighted_mean(self)` |
| `test_negative_layer_indices` | method | `tests/test_jlens.py:110` | `def test_negative_layer_indices(self, model)` |
| `test_negative_skip_raises` | method | `tests/test_jlens.py:34` | `def test_negative_skip_raises(self)` |
| `test_out_of_range_layer_rejected` | method | `tests/test_jlens.py:286` | `def test_out_of_range_layer_rejected(self, fitted_lens, model)` |
| `test_out_of_range_layers_rejected` | method | `tests/test_jlens.py:133` | `def test_out_of_range_layers_rejected(self, model)` |
| `test_repr` | method | `tests/test_jlens.py:359` | `def test_repr(self, fitted_lens)` |
| `test_resume_after_skip_no_double_count` | method | `tests/test_jlens.py:408` | `def test_resume_after_skip_no_double_count(self, model, tmp_path)` |
| `test_returns_jacobians_for_source_layers` | method | `tests/test_jlens.py:63` | `def test_returns_jacobians_for_source_layers(self, model)` |
| `test_save_and_load_round_trip` | method | `tests/test_jlens.py:226` | `def test_save_and_load_round_trip(self, fitted_lens, tmp_path)` |
| `test_source_below_target_enforced` | method | `tests/test_jlens.py:145` | `def test_source_below_target_enforced(self, model)` |
| `test_target_out_of_range_raises` | method | `tests/test_jlens.py:158` | `def test_target_out_of_range_raises(self, model)` |
| `test_too_short_raises` | method | `tests/test_jlens.py:29` | `def test_too_short_raises(self)` |
| `test_transport_produces_correct_shape` | method | `tests/test_jlens.py:331` | `def test_transport_produces_correct_shape(self, fitted_lens)` |
| `test_unfitted_layer_rejected` | method | `tests/test_jlens.py:281` | `def test_unfitted_layer_rejected(self, fitted_lens, model)` |
| `TestTinyDecoder` | class | `tests/test_lens_model.py:41` | `class TestTinyDecoder` |
| `TestTopoGPT3LensConfig` | class | `tests/test_lens_model.py:13` | `class TestTopoGPT3LensConfig` |
| `TestTopoGPT3LensModel` | class | `tests/test_lens_model.py:65` | `class TestTopoGPT3LensModel` |
| `TestTopoGPT3LensModelEdgeCases` | class | `tests/test_lens_model.py:278` | `class TestTopoGPT3LensModelEdgeCases` |
| `TestTopoGPT3LensModelWithRecording` | class | `tests/test_lens_model.py:214` | `class TestTopoGPT3LensModelWithRecording` |
| `lens_model` | method | `tests/test_lens_model.py:77` | `def lens_model(self, raw_model)` |
| `lens_model` | method | `tests/test_lens_model.py:218` | `def lens_model(self)` |
| `raw_model` | method | `tests/test_lens_model.py:69` | `def raw_model(self)` |
| `test_autograd_graph_tracks_through_layers` | method | `tests/test_lens_model.py:163` | `def test_autograd_graph_tracks_through_layers(self)` |
| `test_default_config` | method | `tests/test_lens_model.py:16` | `def test_default_config(self)` |
| `test_default_parameters` | method | `tests/test_lens_model.py:44` | `def test_default_parameters(self)` |
| `test_empty_sequence` | method | `tests/test_lens_model.py:281` | `def test_empty_sequence(self)` |
| `test_encode_respects_max_length` | method | `tests/test_lens_model.py:107` | `def test_encode_respects_max_length(self, lens_model)` |
| `test_encode_text_to_token_ids` | method | `tests/test_lens_model.py:87` | `def test_encode_text_to_token_ids(self, lens_model)` |
| `test_encode_with_tokenizer` | method | `tests/test_lens_model.py:95` | `def test_encode_with_tokenizer(self)` |
| `test_exposes_protocol_attributes` | method | `tests/test_lens_model.py:80` | `def test_exposes_protocol_attributes(self, lens_model, raw_model)` |
| `test_forward_differs_from_full_model` | method | `tests/test_lens_model.py:128` | `def test_forward_differs_from_full_model(self)` |
| `test_forward_output_shape` | method | `tests/test_lens_model.py:51` | `def test_forward_output_shape(self)` |
| `test_forward_plus_unembed_matches_model_logits` | method | `tests/test_lens_model.py:150` | `def test_forward_plus_unembed_matches_model_logits(self, lens_model, raw_model)` |
| `test_forward_returns_residual_only` | method | `tests/test_lens_model.py:113` | `def test_forward_returns_residual_only(self)` |
| `test_from_checkpoint_missing_raises` | method | `tests/test_lens_model.py:198` | `def test_from_checkpoint_missing_raises(self)` |
| `test_from_topogpt2_config` | method | `tests/test_lens_model.py:25` | `def test_from_topogpt2_config(self)` |
| `test_grad_enabled_deterministic` | method | `tests/test_lens_model.py:205` | `def test_grad_enabled_deterministic(self, lens_model)` |
| `test_input_device_property` | method | `tests/test_lens_model.py:180` | `def test_input_device_property(self, lens_model)` |
| `test_input_device_setter` | method | `tests/test_lens_model.py:185` | `def test_input_device_setter(self, lens_model)` |
| `test_probe_checkpoint_missing_raises` | method | `tests/test_lens_model.py:35` | `def test_probe_checkpoint_missing_raises(self, tmp_path)` |
| `test_recorder_captures_layer_outputs` | method | `tests/test_lens_model.py:225` | `def test_recorder_captures_layer_outputs(self, lens_model)` |
| `test_recorder_cleanup_on_exception` | method | `tests/test_lens_model.py:252` | `def test_recorder_cleanup_on_exception(self, lens_model)` |
| `test_recorder_detach_after_forward` | method | `tests/test_lens_model.py:264` | `def test_recorder_detach_after_forward(self, lens_model)` |
| `test_recorder_with_start_graph_at` | method | `tests/test_lens_model.py:238` | `def test_recorder_with_start_graph_at(self, lens_model)` |
| `test_single_token` | method | `tests/test_lens_model.py:291` | `def test_single_token(self)` |
| `test_tokenizer_setter` | method | `tests/test_lens_model.py:191` | `def test_tokenizer_setter(self, lens_model)` |
| `test_unembed_produces_logits` | method | `tests/test_lens_model.py:141` | `def test_unembed_produces_logits(self, lens_model)` |
| `test_weight_tied` | method | `tests/test_lens_model.py:59` | `def test_weight_tied(self)` |
| `D_HEAD` | macro | `topogpt3.c:70` | `#define D_HEAD` |
| `D_LAT_Q` | macro | `topogpt3.c:82` | `#define D_LAT_Q` |
| `D_MODEL` | macro | `topogpt3.c:66` | `#define D_MODEL` |
| `D_QUAT` | macro | `topogpt3.c:71` | `#define D_QUAT` |
| `EMBED_INNER` | macro | `topogpt3.c:90` | `#define EMBED_INNER` |
| `EOS_TOKEN` | macro | `topogpt3.c:89` | `#define EOS_TOKEN` |
| `EPS_RMS` | macro | `topogpt3.c:92` | `#define EPS_RMS` |
| `EXPERT_INNER` | macro | `topogpt3.c:87` | `#define EXPERT_INNER` |
| `FILE` | struct | `topogpt3.c:24` | `` |
| `FREQ_W` | macro | `topogpt3.c:85` | `#define FREQ_W` |
| `GQA_GROUPS` | macro | `topogpt3.c:69` | `#define GQA_GROUPS` |
| `LayerWeights` | struct | `topogpt3.c:176` | `` |
| `MAX_LINE` | macro | `topogpt3.c:96` | `#define MAX_LINE` |
| `MAX_PROMPT_LEN` | macro | `topogpt3.c:95` | `#define MAX_PROMPT_LEN` |
| `MAX_SEQ_LEN` | macro | `topogpt3.c:73` | `#define MAX_SEQ_LEN` |
| `MAX_TOKENS` | macro | `topogpt3.c:94` | `#define MAX_TOKENS` |
| `MOE_TOP_K` | macro | `topogpt3.c:75` | `#define MOE_TOP_K` |
| `ModelWeights` | struct | `topogpt3.c:224` | `` |
| `NULL` | macro | `topogpt3.c:43` | `#define NULL` |
| `N_ANGULAR` | macro | `topogpt3.c:78` | `#define N_ANGULAR` |
| `N_EDGES` | macro | `topogpt3.c:80` | `#define N_EDGES` |
| `N_EDGE_TYPES` | macro | `topogpt3.c:79` | `#define N_EDGE_TYPES` |
| `N_EXPERTS` | macro | `topogpt3.c:74` | `#define N_EXPERTS` |
| `N_HEADS` | macro | `topogpt3.c:67` | `#define N_HEADS` |
| `N_KV_HEADS` | macro | `topogpt3.c:68` | `#define N_KV_HEADS` |
| `N_LAYERS` | macro | `topogpt3.c:72` | `#define N_LAYERS` |
| `N_NODES` | macro | `topogpt3.c:76` | `#define N_NODES` |
| `N_RADIAL` | macro | `topogpt3.c:77` | `#define N_RADIAL` |
| `N_SPECTRAL_LAYERS` | macro | `topogpt3.c:86` | `#define N_SPECTRAL_LAYERS` |
| `PI` | macro | `topogpt3.c:91` | `#define PI` |
| `READOUT_INNER` | macro | `topogpt3.c:88` | `#define READOUT_INNER` |
| `READ_TENSOR` | macro | `topogpt3.c:1310` | `#define READ_TENSOR(dest, count)` |
| `READ_TENSOR16` | macro | `topogpt3.c:1480` | `#define READ_TENSOR16(dest, count)` |
| `SEEK_CUR` | macro | `topogpt3.c:45` | `#define SEEK_CUR` |
| `SEEK_END` | macro | `topogpt3.c:46` | `#define SEEK_END` |
| `SEEK_SET` | macro | `topogpt3.c:44` | `#define SEEK_SET` |
| `SKIP_TENSOR` | macro | `topogpt3.c:1300` | `#define SKIP_TENSOR()` |
| `SKIP_TENSOR16` | macro | `topogpt3.c:1470` | `#define SKIP_TENSOR16()` |
| `SPECTRAL_LATENT_DIM` | macro | `topogpt3.c:81` | `#define SPECTRAL_LATENT_DIM` |
| `TOK_TAB_SIZE` | macro | `topogpt3.c:97` | `#define TOK_TAB_SIZE` |
| `TOK_VOCAB_SIZE` | macro | `topogpt3.c:98` | `#define TOK_VOCAB_SIZE` |
| `TORUS_GRID_H` | macro | `topogpt3.c:83` | `#define TORUS_GRID_H` |
| `TORUS_GRID_W` | macro | `topogpt3.c:84` | `#define TORUS_GRID_W` |
| `TORUS_TEMP` | macro | `topogpt3.c:93` | `#define TORUS_TEMP` |
| `VOCAB_SIZE` | macro | `topogpt3.c:65` | `#define VOCAB_SIZE` |
| `apply_repetition_penalty` | function | `topogpt3.c:1216` | `static void apply_repetition_penalty(float *logits, int n, const int *tokens,                    ...` |
| `apply_temperature` | function | `topogpt3.c:1210` | `static void apply_temperature(float *logits, int n, float temp)` |
| `apply_top_k` | function | `topogpt3.c:1229` | `static void apply_top_k(float *logits, int n, int k)` |
| `attention_forward` | function | `topogpt3.c:978` | `static void attention_forward(const float *x, float *out, int layer_idx, int pos, int total_kv_co...` |
| `build_torus_graph` | function | `topogpt3.c:296` | `static void build_torus_graph(void)` |
| `cmul` | function | `topogpt3.c:664` | `static void cmul(float ar, float ai, float cr, float di, float *rr, float *ri)` |
| `decode_token` | function | `topogpt3.c:1614` | `static void decode_token(int tid)` |
| `decode_token_tiktoken` | function | `topogpt3.c:1652` | `static void decode_token_tiktoken(int tid)` |
| `fclose` | function | `topogpt3.c:37` | `extern int fclose(FILE *);` |
| `fflush` | function | `topogpt3.c:42` | `extern int fflush(FILE *);` |
| `filter1d` | function | `topogpt3.c:537` | `static void filter1d(const float *x, const float *kr, const float *ki,                       floa...` |
| `fopen` | function | `topogpt3.c:36` | `extern FILE *fopen(const char *, const char *);` |
| `forward` | function | `topogpt3.c:1128` | `static void forward(const int *token_ids, int seq_len, float *logits_out)` |
| `fprintf` | function | `topogpt3.c:29` | `extern int fprintf(FILE *, const char *, ...);` |
| `fputc` | function | `topogpt3.c:34` | `extern int fputc(int, FILE *);` |
| `fputs` | function | `topogpt3.c:35` | `extern int fputs(const char *, FILE *);` |
| `fread` | function | `topogpt3.c:38` | `extern unsigned long fread(void *, unsigned long, unsigned long, FILE *);` |
| `free` | function | `topogpt3.c:48` | `extern void free(void *);` |
| `fseek` | function | `topogpt3.c:40` | `extern int fseek(FILE *, long, int);` |
| `ftell` | function | `topogpt3.c:41` | `extern long ftell(FILE *);` |
| `fwrite` | function | `topogpt3.c:39` | `extern unsigned long fwrite(const void *, unsigned long, unsigned long, FILE *);` |
| `gelu` | function | `topogpt3.c:400` | `static void gelu(float *x, int n)` |
| `generate` | function | `topogpt3.c:1725` | `static void generate(const char *prompt, int max_new_tokens, float temperature,                  ...` |
| `generate_tokens` | function | `topogpt3.c:1661` | `static void generate_tokens(int *prompt_tokens, int n_prompt, int max_new_tokens,                ...` |
| `ifft2d` | function | `topogpt3.c:580` | `static void ifft2d(float *data_r, float *data_i, int h, int w)` |
| `ifft_radix2` | function | `topogpt3.c:505` | `static void ifft_radix2(float *real, float *imag, int n)` |
| `interactive_mode` | function | `topogpt3.c:1736` | `static void interactive_mode(void)` |
| `irfft` | function | `topogpt3.c:522` | `static void irfft(const float *Xr, const float *Xi, float *x, int n)` |
| `irfft2d` | function | `topogpt3.c:629` | `static void irfft2d(const float *in_r, const float *in_i, float *out,                      int h,...` |
| `load_token_file` | function | `topogpt3.c:1629` | `static int load_token_file(const char *path, int *out_ids, int max_ids)` |
| `load_vocab` | function | `topogpt3.c:255` | `static void load_vocab(const char *path)` |
| `load_weights` | function | `topogpt3.c:1282` | `static int load_weights(const char *path)` |
| `load_weights_auto` | function | `topogpt3.c:1583` | `static int load_weights_auto(const char *path)` |
| `load_weights_fp16` | function | `topogpt3.c:1452` | `static int load_weights_fp16(const char *path)` |
| `main` | function | `topogpt3.c:1885` | `int main(int argc, char **argv)` |
| `malloc` | function | `topogpt3.c:47` | `extern void *malloc(unsigned long);` |
| `matvec` | function | `topogpt3.c:359` | `static void matvec(const float *W, const float *x, float *y, int rows, int cols)` |
| `matvec_bias` | function | `topogpt3.c:370` | `static void matvec_bias(const float *W, const float *b, const float *x, float *y,                ...` |
| `memcpy` | function | `topogpt3.c:49` | `extern void *memcpy(void *, const void *, unsigned long);` |
| `memset` | function | `topogpt3.c:50` | `extern void *memset(void *, int, unsigned long);` |
| `message_passing` | function | `topogpt3.c:843` | `static void message_passing(const float *node_feat, float *out,                              cons...` |
| `moe_forward` | function | `topogpt3.c:1078` | `static void moe_forward(const float *x, float *out, const LayerWeights *lw)` |
| `precompute_rope` | function | `topogpt3.c:327` | `static void precompute_rope(void)` |
| `print_help` | function | `topogpt3.c:1850` | `static void print_help(void)` |
| `printf` | function | `topogpt3.c:28` | `extern int printf(const char *, ...);` |
| `process_torus_grid` | function | `topogpt3.c:800` | `static void process_torus_grid(const float *grid, float *out, const LayerWeights *lw)` |
| `putchar` | function | `topogpt3.c:33` | `extern int putchar(int);` |
| `puts` | function | `topogpt3.c:32` | `extern int puts(const char *);` |
| `quat_hamilton` | function | `topogpt3.c:440` | `static void quat_hamilton(const float *a, const float *b, float *c)` |
| `quat_linear` | function | `topogpt3.c:448` | `static void quat_linear(const float *Ww, const float *Wx, const float *Wy, const float *Wz,      ...` |
| `quat_normalize` | function | `topogpt3.c:435` | `static void quat_normalize(float *q)` |
| `quat_spectral_layer_2d` | function | `topogpt3.c:695` | `static void quat_spectral_layer_2d(     const float *x, float *y,     const float *kr_w, const fl...` |
| `rfft` | function | `topogpt3.c:513` | `static void rfft(const float *x, float *Xr, float *Xi, int n)` |
| `rfft2d_real` | function | `topogpt3.c:602` | `static void rfft2d_real(const float *data, float *out_r, float *out_i,                          i...` |
| `rmsnorm` | function | `topogpt3.c:382` | `static void rmsnorm(const float *x, const float *w, float *y, int d)` |
| `sample` | function | `topogpt3.c:1248` | `static int sample(const float *logits, int n)` |
| `silu` | function | `topogpt3.c:410` | `static void silu(float *x, int n)` |
| `snprintf` | function | `topogpt3.c:31` | `extern int snprintf(char *, unsigned long, const char *, ...);` |
| `softmax` | function | `topogpt3.c:391` | `static void softmax(float *x, int n)` |
| `spectral_ae_decode` | function | `topogpt3.c:793` | `static void spectral_ae_decode(const float *z, float *x, const LayerWeights *lw)` |
| `spectral_ae_encode` | function | `topogpt3.c:785` | `static void spectral_ae_encode(const float *x, float *z, const LayerWeights *lw)` |
| `spectral_contract` | function | `topogpt3.c:670` | `static void spectral_contract(const float *Wr, const float *Wi,                                co...` |
| `sprintf` | function | `topogpt3.c:30` | `extern int sprintf(char *, const char *, ...);` |
| `stderr` | variable | `topogpt3.c:27` | `extern FILE *stderr;` |
| `stdin` | variable | `topogpt3.c:25` | `extern FILE *stdin;` |
| `stdout` | variable | `topogpt3.c:26` | `extern FILE *stdout;` |
| `strcmp` | function | `topogpt3.c:51` | `extern int strcmp(const char *, const char *);` |
| `strlen` | function | `topogpt3.c:53` | `extern unsigned long strlen(const char *);` |
| `strncmp` | function | `topogpt3.c:52` | `extern int strncmp(const char *, const char *, unsigned long);` |
| `strstr` | function | `topogpt3.c:54` | `extern char *strstr(const char *, const char *);` |
| `swiglu` | function | `topogpt3.c:418` | `static void swiglu(const float *gate_w, const float *up_w, const float *down_w,                  ...` |
| `tg_cos` | function | `topogpt3.c:144` | `static float tg_cos(float x)` |
| `tg_exp` | function | `topogpt3.c:114` | `static float tg_exp(float x)` |
| `tg_fabs` | function | `topogpt3.c:148` | `static float tg_fabs(float x)` |
| `tg_fmax` | function | `topogpt3.c:164` | `static float tg_fmax(float a, float b)` |
| `tg_fmin` | function | `topogpt3.c:168` | `static float tg_fmin(float a, float b)` |
| `tg_log` | function | `topogpt3.c:152` | `static float tg_log(float x)` |
| `tg_sin` | function | `topogpt3.c:135` | `static float tg_sin(float x)` |
| `tg_tanh` | function | `topogpt3.c:128` | `static float tg_tanh(float x)` |
| `time_now_ms` | function | `topogpt3.c:1600` | `static double time_now_ms(void)` |
| `tokenize_string` | function | `topogpt3.c:1195` | `static int tokenize_string(const char *text, int *tokens, int max_tokens)` |
| `torus_brain_forward` | function | `topogpt3.c:888` | `static void torus_brain_forward(const float *x, float *out, float *recon_loss,                   ...` |
| `torus_soft_assign` | function | `topogpt3.c:821` | `static void torus_soft_assign(const float *phi1, const float *phi2,                              ...` |
| `main` | function | `topogpt3/__main__.py:6` | `def main()` |
| `ApiKey` | class | `topogpt3/api_server.py:137` | `class ApiKey` |
| `AuthState` | class | `topogpt3/api_server.py:143` | `class AuthState` |
| `ChatCompletionRequest` | class | `topogpt3/api_server.py:316` | `class ChatCompletionRequest(BaseModel)` |
| `CompletionRequest` | class | `topogpt3/api_server.py:291` | `class CompletionRequest(BaseModel)` |
| `IpBanner` | class | `topogpt3/api_server.py:250` | `class IpBanner` |
| `Message` | class | `topogpt3/api_server.py:310` | `class Message(BaseModel)` |
| `RateLimiter` | class | `topogpt3/api_server.py:219` | `class RateLimiter` |
| `ServerModel` | class | `topogpt3/api_server.py:344` | `class ServerModel` |
| `TokenBucket` | class | `topogpt3/api_server.py:202` | `class TokenBucket` |
| `__init__` | method | `topogpt3/api_server.py:220` | `def __init__(self, user_rps, admin_rps, capacity)` |
| `__init__` | method | `topogpt3/api_server.py:251` | `def __init__(self, max_failures, window)` |
| `_authenticate` | method | `topogpt3/api_server.py:628` | `def _authenticate(request)` |
| `_build_chat_prompt` | method | `topogpt3/api_server.py:827` | `def _build_chat_prompt(messages)` |
| `_check_model` | method | `topogpt3/api_server.py:818` | `def _check_model()` |
| `_check_rate_limit` | method | `topogpt3/api_server.py:646` | `def _check_rate_limit(api_key, request)` |
| `_cleanup` | method | `topogpt3/api_server.py:227` | `def _cleanup(self)` |
| `_extract_text` | method | `topogpt3/api_server.py:846` | `def _extract_text(content)` |
| `_is_eos` | method | `topogpt3/api_server.py:485` | `def _is_eos(self, token_id)` |
| `_json_error` | method | `topogpt3/api_server.py:616` | `def _json_error(status, detail)` |
| `_normalize_stop` | method | `topogpt3/api_server.py:306` | `def _normalize_stop(cls, v)` |
| `_normalize_stop` | method | `topogpt3/api_server.py:334` | `def _normalize_stop(cls, v)` |
| `_parse_keys` | method | `topogpt3/api_server.py:164` | `def _parse_keys(raw)` |
| `_probe_n_kv` | method | `topogpt3/api_server.py:508` | `def _probe_n_kv(checkpoint_dir)` |
| `_real_ip` | method | `topogpt3/api_server.py:605` | `def _real_ip(request)` |
| `_resolve_device` | method | `topogpt3/api_server.py:502` | `def _resolve_device(device)` |
| `_sanitize_stop` | method | `topogpt3/api_server.py:281` | `def _sanitize_stop(stop)` |
| `_security_middleware` | method | `topogpt3/api_server.py:577` | `def _security_middleware(request, call_next)` |
| `_setup_logging` | function | `topogpt3/api_server.py:116` | `def _setup_logging(verbose)` |
| `_sha256` | method | `topogpt3/api_server.py:192` | `def _sha256(raw)` |
| `_short_id` | method | `topogpt3/api_server.py:823` | `def _short_id()` |
| `_stream_chat` | method | `topogpt3/api_server.py:895` | `def _stream_chat(t0_ms, prompt, max_tokens, temperature, top_k, repetition_penalty, stop, auto_continue...` |
| `_stream_completion` | method | `topogpt3/api_server.py:860` | `def _stream_completion(prompt, max_tokens, temperature, top_k, repetition_penalty, stop, auto_continue...` |
| `allow` | method | `topogpt3/api_server.py:233` | `def allow(self, key, role)` |
| `chat_completions` | method | `topogpt3/api_server.py:744` | `def chat_completions(req, request)` |
| `complete` | method | `topogpt3/api_server.py:351` | `def complete(self, prompt)` |
| `completions` | method | `topogpt3/api_server.py:688` | `def completions(req, request)` |
| `consume` | method | `topogpt3/api_server.py:208` | `def consume(self, n)` |
| `health` | method | `topogpt3/api_server.py:664` | `def health(request)` |
| `is_banned` | method | `topogpt3/api_server.py:265` | `def is_banned(self, ip)` |
| `lifespan` | method | `topogpt3/api_server.py:537` | `def lifespan(app)` |
| `list_models` | method | `topogpt3/api_server.py:671` | `def list_models(request)` |
| `load_model` | method | `topogpt3/api_server.py:516` | `def load_model(checkpoint, device)` |
| `main` | method | `topogpt3/api_server.py:933` | `def main()` |
| `record_failure` | method | `topogpt3/api_server.py:257` | `def record_failure(self, ip)` |
| `stream_complete` | method | `topogpt3/api_server.py:396` | `def stream_complete(self, prompt)` |
| `validate` | method | `topogpt3/api_server.py:148` | `def validate(self, raw)` |
| `_fmt_tool_defs` | function | `topogpt3/chat.py:60` | `def _fmt_tool_defs(tools)` |
| `apply_chat_template` | function | `topogpt3/chat.py:71` | `def apply_chat_template(messages, tools, add_generation_prompt, open_thinking)` |
| `parse_thinking` | function | `topogpt3/chat.py:126` | `def parse_thinking(text)` |
| `parse_tool_calls` | function | `topogpt3/chat.py:116` | `def parse_tool_calls(text)` |
| `post_processing_chat` | function | `topogpt3/chat.py:54` | `def post_processing_chat(prompt, empty_think_ratio)` |
| `pre_processing_chat` | function | `topogpt3/chat.py:43` | `def pre_processing_chat(conversations, add_system_ratio)` |
| `split_reasoning_content` | function | `topogpt3/chat.py:134` | `def split_reasoning_content(text)` |
| `_count_unclosed_brackets` | function | `topogpt3/continuation.py:25` | `def _count_unclosed_brackets(text)` |
| `_count_unclosed_fences` | function | `topogpt3/continuation.py:36` | `def _count_unclosed_fences(text)` |
| `extract_tail_for_continuation` | function | `topogpt3/continuation.py:75` | `def extract_tail_for_continuation(text, tail_lines, tail_chars)` |
| `is_response_complete` | function | `topogpt3/continuation.py:45` | `def is_response_complete(text, min_chars)` |
| `split_at_last_newline` | function | `topogpt3/continuation.py:105` | `def split_at_last_newline(text)` |
| `export_hf_stub` | function | `topogpt3/convert.py:38` | `def export_hf_stub(ckpt_dir, out_dir)` |
| `main` | function | `topogpt3/convert.py:49` | `def main()` |
| `merge_base_lora` | function | `topogpt3/convert.py:19` | `def merge_base_lora(base_dir, lora_path, out_dir)` |
| `evaluate` | function | `topogpt3/eval_toolcall.py:35` | `def evaluate(generate_fn)` |
| `run_case` | function | `topogpt3/eval_toolcall.py:19` | `def run_case(generate_fn, prompt, expect_tool)` |
| `_iter_pairs` | function | `topogpt3/export_chat.py:65` | `def _iter_pairs(loader, tier, cap)` |
| `_pairs_code_feedback` | function | `topogpt3/export_chat.py:38` | `def _pairs_code_feedback(ex)` |
| `_pairs_codealpaca` | function | `topogpt3/export_chat.py:28` | `def _pairs_codealpaca(ex)` |
| `_pairs_magicoder` | function | `topogpt3/export_chat.py:55` | `def _pairs_magicoder(ex)` |
| `main` | function | `topogpt3/export_chat.py:81` | `def main()` |
| `CheckpointPaths` | class | `topogpt3/inference.py:228` | `class CheckpointPaths` |
| `CliArgumentParser` | class | `topogpt3/inference.py:615` | `class CliArgumentParser` |
| `GaussPatchApplier` | class | `topogpt3/inference.py:362` | `class GaussPatchApplier` |
| `GenerationEngine` | class | `topogpt3/inference.py:475` | `class GenerationEngine` |
| `GenerationReport` | class | `topogpt3/inference.py:461` | `class GenerationReport` |
| `InferenceLoggerFactory` | class | `topogpt3/inference.py:158` | `class InferenceLoggerFactory` |
| `InferencePipeline` | class | `topogpt3/inference.py:562` | `class InferencePipeline` |
| `InferenceSettings` | class | `topogpt3/inference.py:42` | `class InferenceSettings` |
| `ModelAssembler` | class | `topogpt3/inference.py:380` | `class ModelAssembler` |
| `ResultRenderer` | class | `topogpt3/inference.py:533` | `class ResultRenderer` |
| `SamplingPolicy` | class | `topogpt3/inference.py:441` | `class SamplingPolicy` |
| `ScalePreset` | class | `topogpt3/inference.py:32` | `class ScalePreset` |
| `SecurePathResolver` | class | `topogpt3/inference.py:178` | `class SecurePathResolver` |
| `SeedSynchronizer` | class | `topogpt3/inference.py:417` | `class SeedSynchronizer` |
| `SourceModuleLoader` | class | `topogpt3/inference.py:212` | `class SourceModuleLoader` |
| `TokenizerFactory` | class | `topogpt3/inference.py:349` | `class TokenizerFactory` |
| `TopoGPT2ConfigAligner` | class | `topogpt3/inference.py:318` | `class TopoGPT2ConfigAligner` |
| `WeightShapeProbe` | class | `topogpt3/inference.py:274` | `class WeightShapeProbe` |
| `__init__` | method | `topogpt3/inference.py:215` | `def __init__(self, settings, logger)` |
| `__init__` | method | `topogpt3/inference.py:231` | `def __init__(self, settings)` |
| `__init__` | method | `topogpt3/inference.py:277` | `def __init__(self, settings, logger)` |
| `__init__` | method | `topogpt3/inference.py:321` | `def __init__(self, settings, source_module, logger)` |
| `__init__` | method | `topogpt3/inference.py:352` | `def __init__(self, settings, source_module)` |
| `__init__` | method | `topogpt3/inference.py:365` | `def __init__(self, settings, source_module, logger)` |
| `__init__` | method | `topogpt3/inference.py:383` | `def __init__(self, settings, source_module, logger)` |
| `__init__` | method | `topogpt3/inference.py:420` | `def __init__(self, settings, source_module, logger)` |
| `__init__` | method | `topogpt3/inference.py:478` | `def __init__(self, settings, logger)` |
| `__init__` | method | `topogpt3/inference.py:536` | `def __init__(self, settings, logger)` |
| `__init__` | method | `topogpt3/inference.py:565` | `def __init__(self, settings, logger)` |
| `apply` | method | `topogpt3/inference.py:426` | `def apply(self)` |
| `apply_if_enabled` | method | `topogpt3/inference.py:371` | `def apply_if_enabled(self)` |
| `assemble` | method | `topogpt3/inference.py:389` | `def assemble(self, aligned_cfg, paths)` |
| `assert_ready` | method | `topogpt3/inference.py:255` | `def assert_ready(self)` |
| `build` | method | `topogpt3/inference.py:162` | `def build(settings)` |
| `build` | method | `topogpt3/inference.py:327` | `def build(self, n_kv_heads, vocab_size)` |
| `build` | method | `topogpt3/inference.py:356` | `def build(self)` |
| `build_parser` | method | `topogpt3/inference.py:619` | `def build_parser()` |
| `detect_n_kv_heads` | method | `topogpt3/inference.py:281` | `def detect_n_kv_heads(self, weights_path, d_model, n_heads)` |
| `execute` | method | `topogpt3/inference.py:571` | `def execute(self)` |
| `from_settings` | method | `topogpt3/inference.py:450` | `def from_settings(cls, settings)` |
| `load` | method | `topogpt3/inference.py:219` | `def load(self)` |
| `main` | method | `topogpt3/inference.py:721` | `def main(argv)` |
| `model_file` | method | `topogpt3/inference.py:243` | `def model_file(self)` |
| `parse` | method | `topogpt3/inference.py:698` | `def parse(argv)` |
| `preset` | method | `topogpt3/inference.py:116` | `def preset(self)` |
| `render` | method | `topogpt3/inference.py:540` | `def render(self, report)` |
| `require_existing_file` | method | `topogpt3/inference.py:198` | `def require_existing_file(path, expected_suffix)` |
| `resolve_under` | method | `topogpt3/inference.py:182` | `def resolve_under(root)` |
| `run` | method | `topogpt3/inference.py:483` | `def run(self, model, tokenizer, prompt, policy)` |
| `scale_presets` | method | `topogpt3/inference.py:103` | `def scale_presets()` |
| `slot_dir` | method | `topogpt3/inference.py:239` | `def slot_dir(self)` |
| `state_file` | method | `topogpt3/inference.py:249` | `def state_file(self)` |
| `tokens_per_second` | method | `topogpt3/inference.py:470` | `def tokens_per_second(self, elapsed_floor)` |
| `validate` | method | `topogpt3/inference.py:126` | `def validate(self)` |
| `CheckpointPaths` | class | `topogpt3/inference_hrm.py:413` | `class CheckpointPaths` |
| `CliArgumentParser` | class | `topogpt3/inference_hrm.py:1283` | `class CliArgumentParser` |
| `GaussPatchApplier` | class | `topogpt3/inference_hrm.py:546` | `class GaussPatchApplier` |

Next: [SYMBOLS_p2.md](SYMBOLS_p2.md)
