# Symbols

| Symbol | Kind | File:Line | Signature |
|--------|------|-----------|-----------|
| `_build_parser` | function | `app.py:121` | `def _build_parser()` |
| `main` | function | `app.py:159` | `def main(argv)` |
| `run_inference` | function | `app.py:46` | `def run_inference(prompt, checkpoint_dir, checkpoint_name, max_new_tokens, temperature, top_k, repetition_penalty, devic` |
| `run_inference_hrm` | function | `app.py:71` | `def run_inference_hrm(prompt, checkpoint_dir, checkpoint_name, max_new_tokens, temperature, top_k, repetition_penalty, h` |
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
| `run_hrm_inference` | function | `gradio_app.py:95` | `def run_hrm_inference(prompt, max_new_tokens, temperature, top_k, repetition_penalty, high_level_iters, low_level_iters,` |
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
| `READ_TENSOR` | function | `topogpt3.c:1326` | `READ_TENSOR(W.token_embed, VOCAB_SIZE * D_MODEL);` |
| `READ_TENSOR16` | macro | `topogpt3.c:1480` | `#define READ_TENSOR16(dest, count)` |
| `READ_TENSOR16` | function | `topogpt3.c:1501` | `READ_TENSOR16(W.token_embed, VOCAB_SIZE * D_MODEL);` |
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
| `VOCAB_SIZE` | macro | `topogpt3.c:64` | `#define VOCAB_SIZE` |
| `apply_repetition_penalty` | function | `topogpt3.c:1215` | `static void apply_repetition_penalty(float *logits, int n, const int *tokens,
                   ...` |
| `apply_temperature` | function | `topogpt3.c:1209` | `static void apply_temperature(float *logits, int n, float temp)` |
| `apply_top_k` | function | `topogpt3.c:1228` | `static void apply_top_k(float *logits, int n, int k)` |
| `attention_forward` | function | `topogpt3.c:977` | `static void attention_forward(const float *x, float *out, int layer_idx, int pos, int total_kv_co...` |
| `build_torus_graph` | function | `topogpt3.c:295` | `static void build_torus_graph(void)` |
| `cmul` | function | `topogpt3.c:664` | `static void cmul(float ar, float ai, float cr, float di, float *rr, float *ri)` |
| `decode_token` | function | `topogpt3.c:1613` | `static void decode_token(int tid)` |
| `decode_token_tiktoken` | function | `topogpt3.c:1652` | `static void decode_token_tiktoken(int tid)` |
| `fclose` | function | `topogpt3.c:37` | `extern int fclose(FILE *);` |
| `fflush` | function | `topogpt3.c:42` | `extern int fflush(FILE *);` |
| `fft_radix2` | function | `topogpt3.c:508` | `fft_radix2(real, imag, n);` |
| `filter1d` | function | `topogpt3.c:536` | `static void filter1d(const float *x, const float *kr, const float *ki,
                      floa...` |
| `fopen` | function | `topogpt3.c:36` | `extern FILE *fopen(const char *, const char *);` |
| `forward` | function | `topogpt3.c:1127` | `static void forward(const int *token_ids, int seq_len, float *logits_out)` |
| `fprintf` | function | `topogpt3.c:29` | `extern int fprintf(FILE *, const char *, ...);` |
| `fputc` | function | `topogpt3.c:34` | `extern int fputc(int, FILE *);` |
| `fputs` | function | `topogpt3.c:35` | `extern int fputs(const char *, FILE *);` |
| `fread` | function | `topogpt3.c:38` | `extern unsigned long fread(void *, unsigned long, unsigned long, FILE *);` |
| `free` | function | `topogpt3.c:48` | `extern void free(void *);` |
| `fseek` | function | `topogpt3.c:40` | `extern int fseek(FILE *, long, int);` |
| `ftell` | function | `topogpt3.c:41` | `extern long ftell(FILE *);` |
| `fwrite` | function | `topogpt3.c:39` | `extern unsigned long fwrite(const void *, unsigned long, unsigned long, FILE *);` |
| `gelu` | function | `topogpt3.c:399` | `static void gelu(float *x, int n)` |
| `generate` | function | `topogpt3.c:1724` | `static void generate(const char *prompt, int max_new_tokens, float temperature,
                 ...` |
| `generate_tokens` | function | `topogpt3.c:1660` | `static void generate_tokens(int *prompt_tokens, int n_prompt, int max_new_tokens,
               ...` |
| `ifft2d` | function | `topogpt3.c:579` | `static void ifft2d(float *data_r, float *data_i, int h, int w)` |
| `ifft_radix2` | function | `topogpt3.c:504` | `static void ifft_radix2(float *real, float *imag, int n)` |
| `interactive_mode` | function | `topogpt3.c:1735` | `static void interactive_mode(void)` |
| `irfft` | function | `topogpt3.c:522` | `static void irfft(const float *Xr, const float *Xi, float *x, int n)` |
| `irfft2d` | function | `topogpt3.c:629` | `static void irfft2d(const float *in_r, const float *in_i, float *out,
                     int h,...` |
| `load_token_file` | function | `topogpt3.c:1629` | `static int load_token_file(const char *path, int *out_ids, int max_ids)` |
| `load_vocab` | function | `topogpt3.c:254` | `static void load_vocab(const char *path)` |
| `load_weights` | function | `topogpt3.c:1281` | `static int load_weights(const char *path)` |
| `load_weights_auto` | function | `topogpt3.c:1583` | `static int load_weights_auto(const char *path)` |
| `load_weights_fp16` | function | `topogpt3.c:1451` | `static int load_weights_fp16(const char *path)` |
| `main` | function | `topogpt3.c:1884` | `int main(int argc, char **argv)` |
| `malloc` | function | `topogpt3.c:47` | `extern void *malloc(unsigned long);` |
| `matvec` | function | `topogpt3.c:358` | `static void matvec(const float *W, const float *x, float *y, int rows, int cols)` |
| `matvec_bias` | function | `topogpt3.c:369` | `static void matvec_bias(const float *W, const float *b, const float *x, float *y,
               ...` |
| `memcpy` | function | `topogpt3.c:49` | `extern void *memcpy(void *, const void *, unsigned long);` |
| `memset` | function | `topogpt3.c:50` | `extern void *memset(void *, int, unsigned long);` |
| `message_passing` | function | `topogpt3.c:842` | `static void message_passing(const float *node_feat, float *out,
                             cons...` |
| `moe_forward` | function | `topogpt3.c:1077` | `static void moe_forward(const float *x, float *out, const LayerWeights *lw)` |
| `precompute_rope` | function | `topogpt3.c:326` | `static void precompute_rope(void)` |
| `print_help` | function | `topogpt3.c:1849` | `static void print_help(void)` |
| `printf` | function | `topogpt3.c:28` | `extern int printf(const char *, ...);` |
| `process_torus_grid` | function | `topogpt3.c:799` | `static void process_torus_grid(const float *grid, float *out, const LayerWeights *lw)` |
| `putchar` | function | `topogpt3.c:33` | `extern int putchar(int);` |
| `puts` | function | `topogpt3.c:32` | `extern int puts(const char *);` |
| `quat_hamilton` | function | `topogpt3.c:439` | `static void quat_hamilton(const float *a, const float *b, float *c)` |
| `quat_linear` | function | `topogpt3.c:448` | `static void quat_linear(const float *Ww, const float *Wx, const float *Wy, const float *Wz,
     ...` |
| `quat_normalize` | function | `topogpt3.c:434` | `static void quat_normalize(float *q)` |
| `quat_spectral_layer_2d` | function | `topogpt3.c:694` | `static void quat_spectral_layer_2d(
    const float *x, float *y,
    const float *kr_w, const fl...` |
| `rfft` | function | `topogpt3.c:513` | `static void rfft(const float *x, float *Xr, float *Xi, int n)` |
| `rfft2d_real` | function | `topogpt3.c:602` | `static void rfft2d_real(const float *data, float *out_r, float *out_i,
                         i...` |
| `rmsnorm` | function | `topogpt3.c:381` | `static void rmsnorm(const float *x, const float *w, float *y, int d)` |
| `sample` | function | `topogpt3.c:1247` | `static int sample(const float *logits, int n)` |
| `silu` | function | `topogpt3.c:409` | `static void silu(float *x, int n)` |
| `snprintf` | function | `topogpt3.c:31` | `extern int snprintf(char *, unsigned long, const char *, ...);` |
| `softmax` | function | `topogpt3.c:390` | `static void softmax(float *x, int n)` |
| `spectral_ae_decode` | function | `topogpt3.c:792` | `static void spectral_ae_decode(const float *z, float *x, const LayerWeights *lw)` |
| `spectral_ae_encode` | function | `topogpt3.c:784` | `static void spectral_ae_encode(const float *x, float *z, const LayerWeights *lw)` |
| `spectral_contract` | function | `topogpt3.c:670` | `static void spectral_contract(const float *Wr, const float *Wi,
                               co...` |
| `sprintf` | function | `topogpt3.c:30` | `extern int sprintf(char *, const char *, ...);` |
| `stderr` | variable | `topogpt3.c:27` | `extern FILE *stderr;` |
| `stdin` | variable | `topogpt3.c:25` | `extern FILE *stdin;` |
| `stdout` | variable | `topogpt3.c:26` | `extern FILE *stdout;` |
| `strcmp` | function | `topogpt3.c:51` | `extern int strcmp(const char *, const char *);` |
| `strlen` | function | `topogpt3.c:53` | `extern unsigned long strlen(const char *);` |
| `strncmp` | function | `topogpt3.c:52` | `extern int strncmp(const char *, const char *, unsigned long);` |
| `strstr` | function | `topogpt3.c:54` | `extern char *strstr(const char *, const char *);` |
| `swiglu` | function | `topogpt3.c:417` | `static void swiglu(const float *gate_w, const float *up_w, const float *down_w,
                 ...` |
| `tg_cos` | function | `topogpt3.c:143` | `static float tg_cos(float x)` |
| `tg_exp` | function | `topogpt3.c:113` | `static float tg_exp(float x)` |
| `tg_fabs` | function | `topogpt3.c:147` | `static float tg_fabs(float x)` |
| `tg_fmax` | function | `topogpt3.c:163` | `static float tg_fmax(float a, float b)` |
| `tg_fmin` | function | `topogpt3.c:167` | `static float tg_fmin(float a, float b)` |
| `tg_log` | function | `topogpt3.c:151` | `static float tg_log(float x)` |
| `tg_sin` | function | `topogpt3.c:134` | `static float tg_sin(float x)` |
| `tg_tanh` | function | `topogpt3.c:127` | `static float tg_tanh(float x)` |
| `time_now_ms` | function | `topogpt3.c:1600` | `static double time_now_ms(void)` |
| `tokenize_string` | function | `topogpt3.c:1194` | `static int tokenize_string(const char *text, int *tokens, int max_tokens)` |
| `torus_brain_forward` | function | `topogpt3.c:887` | `static void torus_brain_forward(const float *x, float *out, float *recon_loss,
                  ...` |
| `torus_soft_assign` | function | `topogpt3.c:820` | `static void torus_soft_assign(const float *phi1, const float *phi2,
                             ...` |
| `volatile` | function | `topogpt3.c:1605` | `__asm__ volatile ("rdtsc" : "=a"(lo), "=d"(hi));` |
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
| `_stream_chat` | method | `topogpt3/api_server.py:895` | `def _stream_chat(t0_ms, prompt, max_tokens, temperature, top_k, repetition_penalty, stop, auto_continue, max_continuatio` |
| `_stream_completion` | method | `topogpt3/api_server.py:860` | `def _stream_completion(prompt, max_tokens, temperature, top_k, repetition_penalty, stop, auto_continue, max_continuation` |
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
| `GenerationReasoningSummary` | class | `topogpt3/inference_hrm.py:661` | `class GenerationReasoningSummary` |
| `GenerationReport` | class | `topogpt3/inference_hrm.py:985` | `class GenerationReport` |
| `HRMGenerationEngine` | class | `topogpt3/inference_hrm.py:1000` | `class HRMGenerationEngine` |
| `HRMInferencePipeline` | class | `topogpt3/inference_hrm.py:1230` | `class HRMInferencePipeline` |
| `HRMInferenceSettings` | class | `topogpt3/inference_hrm.py:134` | `class HRMInferenceSettings` |
| `HRMLoggerFactory` | class | `topogpt3/inference_hrm.py:343` | `class HRMLoggerFactory` |
| `HierarchicalRecursiveReasoner` | class | `topogpt3/inference_hrm.py:727` | `class HierarchicalRecursiveReasoner` |
| `LatentChangeMetric` | class | `topogpt3/inference_hrm.py:624` | `class LatentChangeMetric` |
| `LogitsSampler` | class | `topogpt3/inference_hrm.py:935` | `class LogitsSampler` |
| `ModelAssembler` | class | `topogpt3/inference_hrm.py:564` | `class ModelAssembler` |
| `ReasoningIterationStats` | class | `topogpt3/inference_hrm.py:648` | `class ReasoningIterationStats` |
| `RecursiveReasoningConfig` | class | `topogpt3/inference_hrm.py:64` | `class RecursiveReasoningConfig` |
| `ResultRenderer` | class | `topogpt3/inference_hrm.py:1189` | `class ResultRenderer` |
| `SamplingPolicy` | class | `topogpt3/inference_hrm.py:963` | `class SamplingPolicy` |
| `ScalePreset` | class | `topogpt3/inference_hrm.py:54` | `class ScalePreset` |
| `SecurePathResolver` | class | `topogpt3/inference_hrm.py:363` | `class SecurePathResolver` |
| `SeedSynchronizer` | class | `topogpt3/inference_hrm.py:601` | `class SeedSynchronizer` |
| `SourceModuleLoader` | class | `topogpt3/inference_hrm.py:397` | `class SourceModuleLoader` |
| `SparseHighLevelStateCache` | class | `topogpt3/inference_hrm.py:684` | `class SparseHighLevelStateCache` |
| `TokenizerFactory` | class | `topogpt3/inference_hrm.py:533` | `class TokenizerFactory` |
| `TopoGPT2ConfigAligner` | class | `topogpt3/inference_hrm.py:502` | `class TopoGPT2ConfigAligner` |
| `WeightShapeProbe` | class | `topogpt3/inference_hrm.py:459` | `class WeightShapeProbe` |
| `__init__` | method | `topogpt3/inference_hrm.py:400` | `def __init__(self, settings, logger)` |
| `__init__` | method | `topogpt3/inference_hrm.py:416` | `def __init__(self, settings)` |
| `__init__` | method | `topogpt3/inference_hrm.py:462` | `def __init__(self, settings, logger)` |
| `__init__` | method | `topogpt3/inference_hrm.py:505` | `def __init__(self, settings, source_module, logger)` |
| `__init__` | method | `topogpt3/inference_hrm.py:536` | `def __init__(self, settings, source_module)` |
| `__init__` | method | `topogpt3/inference_hrm.py:549` | `def __init__(self, settings, source_module, logger)` |
| `__init__` | method | `topogpt3/inference_hrm.py:567` | `def __init__(self, settings, source_module, logger)` |
| `__init__` | method | `topogpt3/inference_hrm.py:604` | `def __init__(self, settings, source_module, logger)` |
| `__init__` | method | `topogpt3/inference_hrm.py:627` | `def __init__(self, epsilon_floor)` |
| `__init__` | method | `topogpt3/inference_hrm.py:693` | `def __init__(self, persist_tokens)` |
| `__init__` | method | `topogpt3/inference_hrm.py:768` | `def __init__(self, layers, final_norm, reasoning_config, logger)` |
| `__init__` | method | `topogpt3/inference_hrm.py:938` | `def __init__(self, logger)` |
| `__init__` | method | `topogpt3/inference_hrm.py:1011` | `def __init__(self, settings, logger)` |
| `__init__` | method | `topogpt3/inference_hrm.py:1192` | `def __init__(self, settings, logger)` |
| `__init__` | method | `topogpt3/inference_hrm.py:1233` | `def __init__(self, settings, logger)` |
| `_encode_prompt` | method | `topogpt3/inference_hrm.py:1016` | `def _encode_prompt(self, model, prompt_ids)` |
| `_full_pass` | method | `topogpt3/inference_hrm.py:793` | `def _full_pass(self, z_in, base_kvs)` |
| `_window_pass` | method | `topogpt3/inference_hrm.py:808` | `def _window_pass(self, z_in, base_kvs, window)` |
| `absorb` | method | `topogpt3/inference_hrm.py:671` | `def absorb(self, sample)` |
| `apply` | method | `topogpt3/inference_hrm.py:610` | `def apply(self)` |
| `apply_if_enabled` | method | `topogpt3/inference_hrm.py:555` | `def apply_if_enabled(self)` |
| `assemble` | method | `topogpt3/inference_hrm.py:573` | `def assemble(self, aligned_cfg, paths)` |
| `assert_ready` | method | `topogpt3/inference_hrm.py:440` | `def assert_ready(self)` |
| `build` | method | `topogpt3/inference_hrm.py:347` | `def build(settings)` |
| `build` | method | `topogpt3/inference_hrm.py:511` | `def build(self, n_kv_heads, vocab_size)` |
| `build` | method | `topogpt3/inference_hrm.py:540` | `def build(self)` |
| `build_parser` | method | `topogpt3/inference_hrm.py:1287` | `def build_parser()` |
| `commit` | method | `topogpt3/inference_hrm.py:716` | `def commit(self, new_state)` |
| `detect_n_kv_heads` | method | `topogpt3/inference_hrm.py:466` | `def detect_n_kv_heads(self, weights_path, d_model, n_heads)` |
| `execute` | method | `topogpt3/inference_hrm.py:1239` | `def execute(self)` |
| `from_settings` | method | `topogpt3/inference_hrm.py:973` | `def from_settings(cls, settings)` |
| `get_or_init` | method | `topogpt3/inference_hrm.py:700` | `def get_or_init(self, reference)` |
| `invalidate` | method | `topogpt3/inference_hrm.py:721` | `def invalidate(self)` |
| `load` | method | `topogpt3/inference_hrm.py:404` | `def load(self)` |
| `main` | method | `topogpt3/inference_hrm.py:1494` | `def main(argv)` |
| `model_file` | method | `topogpt3/inference_hrm.py:428` | `def model_file(self)` |
| `num_layers` | method | `topogpt3/inference_hrm.py:789` | `def num_layers(self)` |
| `parse` | method | `topogpt3/inference_hrm.py:1448` | `def parse(argv)` |
| `preset` | method | `topogpt3/inference_hrm.py:234` | `def preset(self)` |
| `reason` | method | `topogpt3/inference_hrm.py:827` | `def reason(self, z_initial, base_kvs, cached_refinement)` |
| `relative_change` | method | `topogpt3/inference_hrm.py:632` | `def relative_change(self, current, previous)` |
| `render` | method | `topogpt3/inference_hrm.py:1196` | `def render(self, report)` |
| `require_existing_file` | method | `topogpt3/inference_hrm.py:383` | `def require_existing_file(path, expected_suffix)` |
| `resolve_under` | method | `topogpt3/inference_hrm.py:367` | `def resolve_under(root)` |
| `run` | method | `topogpt3/inference_hrm.py:1048` | `def run(self, model, tokenizer, prompt, policy)` |
| `sample` | method | `topogpt3/inference_hrm.py:941` | `def sample(self, logits, token_history, temperature, top_k, repetition_penalty)` |
| `scale_presets` | method | `topogpt3/inference_hrm.py:221` | `def scale_presets()` |
| `slot_dir` | method | `topogpt3/inference_hrm.py:424` | `def slot_dir(self)` |
| `state_file` | method | `topogpt3/inference_hrm.py:434` | `def state_file(self)` |
| `tokens_per_second` | method | `topogpt3/inference_hrm.py:995` | `def tokens_per_second(self, elapsed_floor)` |
| `validate` | method | `topogpt3/inference_hrm.py:244` | `def validate(self)` |
| `ActivationRecorder` | class | `topogpt3/jlens.py:69` | `class ActivationRecorder` |
| `JacobianLens` | class | `topogpt3/jlens.py:459` | `class JacobianLens` |
| `SliceData` | class | `topogpt3/jlens.py:664` | `class SliceData` |
| `TopoGPT3JLensAppConfig` | class | `topogpt3/jlens.py:56` | `class TopoGPT3JLensAppConfig` |
| `TopoGPT3JLensFitConfig` | class | `topogpt3/jlens.py:37` | `class TopoGPT3JLensFitConfig` |
| `__enter__` | method | `topogpt3/jlens.py:113` | `def __enter__(self)` |
| `__exit__` | method | `topogpt3/jlens.py:126` | `def __exit__(self)` |
| `__init__` | method | `topogpt3/jlens.py:87` | `def __init__(self, blocks, at)` |
| `__init__` | method | `topogpt3/jlens.py:470` | `def __init__(self, jacobians)` |
| `__post_init__` | method | `topogpt3/jlens.py:692` | `def __post_init__(self)` |
| `__repr__` | method | `topogpt3/jlens.py:482` | `def __repr__(self)` |
| `_atomic_save` | method | `topogpt3/jlens.py:283` | `def _atomic_save(obj, path)` |
| `_check_layer_indices` | method | `topogpt3/jlens.py:162` | `def _check_layer_indices(source_layers, target_layer, n_layers)` |
| `_demo_jlens` | method | `topogpt3/jlens.py:842` | `def _demo_jlens()` |
| `_make_hook` | method | `topogpt3/jlens.py:102` | `def _make_hook(self, index)` |
| `apply` | method | `topogpt3/jlens.py:585` | `def apply(self, model, prompt)` |
| `compute_slice` | method | `topogpt3/jlens.py:705` | `def compute_slice(model, lens, prompt)` |
| `fit` | method | `topogpt3/jlens.py:291` | `def fit(model, prompts)` |
| `from_pretrained` | method | `topogpt3/jlens.py:519` | `def from_pretrained(cls, name_or_path)` |
| `hook` | method | `topogpt3/jlens.py:105` | `def hook(module, inputs, output)` |
| `jacobian_for_prompt` | method | `topogpt3/jlens.py:187` | `def jacobian_for_prompt(model, prompt, source_layers)` |
| `load` | method | `topogpt3/jlens.py:504` | `def load(cls, path)` |
| `merge` | method | `topogpt3/jlens.py:543` | `def merge(cls, lenses)` |
| `save` | method | `topogpt3/jlens.py:489` | `def save(self, path)` |
| `select` | method | `topogpt3/jlens.py:646` | `def select(layer)` |
| `text_slice` | method | `topogpt3/jlens.py:789` | `def text_slice(slice_data, tokenizer, n_cols)` |
| `transport` | method | `topogpt3/jlens.py:574` | `def transport(self, residual, layer)` |
| `valid_position_mask` | method | `topogpt3/jlens.py:132` | `def valid_position_mask(seq_len)` |
| `write_checkpoint` | method | `topogpt3/jlens.py:378` | `def write_checkpoint()` |
| `LensModel` | class | `topogpt3/lens_model.py:23` | `class LensModel(Protocol)` |
| `TinyDecoder` | class | `topogpt3/lens_model.py:306` | `class TinyDecoder(Module)` |
| `TopoGPT3LensConfig` | class | `topogpt3/lens_model.py:59` | `class TopoGPT3LensConfig` |
| `TopoGPT3LensModel` | class | `topogpt3/lens_model.py:161` | `class TopoGPT3LensModel(Module)` |
| `_ResidualBlock` | class | `topogpt3/lens_model.py:359` | `class _ResidualBlock(Module)` |
| `_TopoGPT3ResidualForward` | class | `topogpt3/lens_model.py:142` | `class _TopoGPT3ResidualForward(Module)` |
| `__init__` | method | `topogpt3/lens_model.py:150` | `def __init__(self, model)` |
| `__init__` | method | `topogpt3/lens_model.py:172` | `def __init__(self, model, tokenizer)` |
| `__init__` | method | `topogpt3/lens_model.py:315` | `def __init__(self, n_layers, d_model, vocab_size, seed)` |
| `__init__` | method | `topogpt3/lens_model.py:360` | `def __init__(self, d_model)` |
| `d_model` | method | `topogpt3/lens_model.py:188` | `def d_model(self)` |
| `encode` | method | `topogpt3/lens_model.py:40` | `def encode(self, text)` |
| `encode` | method | `topogpt3/lens_model.py:213` | `def encode(self, text)` |
| `forward` | method | `topogpt3/lens_model.py:45` | `def forward(self, input_ids)` |
| `forward` | method | `topogpt3/lens_model.py:154` | `def forward(self, input_ids)` |
| `forward` | method | `topogpt3/lens_model.py:228` | `def forward(self, input_ids)` |
| `forward` | method | `topogpt3/lens_model.py:344` | `def forward(self, token_ids, past_kvs)` |
| `forward` | method | `topogpt3/lens_model.py:366` | `def forward(self, x, past_kv)` |
| `from_checkpoint` | method | `topogpt3/lens_model.py:246` | `def from_checkpoint(cls, checkpoint_dir)` |
| `from_topogpt2_config` | method | `topogpt3/lens_model.py:84` | `def from_topogpt2_config(cls, cfg)` |
| `input_device` | method | `topogpt3/lens_model.py:204` | `def input_device(self)` |
| `input_device` | method | `topogpt3/lens_model.py:210` | `def input_device(self, device)` |
| `layers` | method | `topogpt3/lens_model.py:192` | `def layers(self)` |
| `n_layers` | method | `topogpt3/lens_model.py:184` | `def n_layers(self)` |
| `probe_checkpoint` | method | `topogpt3/lens_model.py:104` | `def probe_checkpoint(cls, checkpoint_dir)` |
| `tokenizer` | method | `topogpt3/lens_model.py:196` | `def tokenizer(self)` |
| `tokenizer` | method | `topogpt3/lens_model.py:200` | `def tokenizer(self, tok)` |
| `unembed` | method | `topogpt3/lens_model.py:52` | `def unembed(self, residual)` |
| `unembed` | method | `topogpt3/lens_model.py:237` | `def unembed(self, residual)` |
| `LoRA` | class | `topogpt3/lora.py:16` | `class LoRA(Module)` |
| `__init__` | method | `topogpt3/lora.py:17` | `def __init__(self, in_features, out_features, rank)` |
| `_fwd` | method | `topogpt3/lora.py:66` | `def _fwd(x, _o, _l)` |
| `_is_quaternion_sublayer` | method | `topogpt3/lora.py:29` | `def _is_quaternion_sublayer(name)` |
| `apply_lora` | method | `topogpt3/lora.py:54` | `def apply_lora(model, rank, include_mlp)` |
| `forward` | method | `topogpt3/lora.py:25` | `def forward(self, x)` |
| `freeze_non_lora` | method | `topogpt3/lora.py:80` | `def freeze_non_lora(model)` |
| `load_lora` | method | `topogpt3/lora.py:99` | `def load_lora(model, path, device)` |
| `lora_parameters` | method | `topogpt3/lora.py:73` | `def lora_parameters(model)` |
| `lora_targets` | method | `topogpt3/lora.py:34` | `def lora_targets(model, include_mlp)` |
| `merge_lora` | method | `topogpt3/lora.py:110` | `def merge_lora(model, lora_path, save_path)` |
| `save_lora` | method | `topogpt3/lora.py:88` | `def save_lora(model, path)` |
| `BPETokenizer` | class | `topogpt3/model.py:1279` | `class BPETokenizer` |
| `CheckpointManager` | class | `topogpt3/model.py:2174` | `class CheckpointManager` |
| `CurriculumDataset` | class | `topogpt3/model.py:1699` | `class CurriculumDataset(Dataset)` |
| `CurriculumTrainer` | class | `topogpt3/model.py:2022` | `class CurriculumTrainer` |
| `FileManifest` | class | `topogpt3/model.py:1405` | `class FileManifest` |
| `MappedTokenDataset` | class | `topogpt3/model.py:1561` | `class MappedTokenDataset(Dataset)` |
| `MechanisticMetrics` | class | `topogpt3/model.py:2700` | `class MechanisticMetrics` |
| `MemmapTokenizer` | class | `topogpt3/model.py:1472` | `class MemmapTokenizer` |
| `MultiHeadAttention` | class | `topogpt3/model.py:911` | `class MultiHeadAttention(Module)` |
| `Phase0_KernelOptimizer` | class | `topogpt3/model.py:2937` | `class Phase0_KernelOptimizer` |
| `Phase1_BatchProspector` | class | `topogpt3/model.py:3012` | `class Phase1_BatchProspector` |
| `Phase2_SeedMiner` | class | `topogpt3/model.py:3095` | `class Phase2_SeedMiner` |
| `Phase4_AnnealingRefiner` | class | `topogpt3/model.py:3177` | `class Phase4_AnnealingRefiner` |
| `ProgressiveSeqLenTrainer` | class | `topogpt3/model.py:1763` | `class ProgressiveSeqLenTrainer` |
| `QuantizedEmbedding` | class | `topogpt3/model.py:1954` | `class QuantizedEmbedding(Module)` |
| `QuaternionLinear` | class | `topogpt3/model.py:253` | `class QuaternionLinear(Module)` |
| `QuaternionOps` | class | `topogpt3/model.py:214` | `class QuaternionOps` |
| `QuaternionSpectralLayer` | class | `topogpt3/model.py:298` | `class QuaternionSpectralLayer(Module)` |
| `QuaternionTorusBrain` | class | `topogpt3/model.py:468` | `class QuaternionTorusBrain(Module)` |
| `RMSNorm` | class | `topogpt3/model.py:760` | `class RMSNorm(Module)` |
| `RotaryEmbedding` | class | `topogpt3/model.py:685` | `class RotaryEmbedding(Module)` |
| `SpectralAutoencoder` | class | `topogpt3/model.py:385` | `class SpectralAutoencoder(Module)` |
| `SpeculativeDecoder` | class | `topogpt3/model.py:1839` | `class SpeculativeDecoder` |
| `SwiGLU` | class | `topogpt3/model.py:777` | `class SwiGLU(Module)` |
| `TextFilter` | class | `topogpt3/model.py:1595` | `class TextFilter` |
| `TopoGPT2` | class | `topogpt3/model.py:1062` | `class TopoGPT2(Module)` |
| `TopoGPT2Config` | class | `topogpt3/model.py:56` | `class TopoGPT2Config` |
| `TopoGPT2Layer` | class | `topogpt3/model.py:1015` | `class TopoGPT2Layer(Module)` |
| `TopoGPT2Trainer` | class | `topogpt3/model.py:2407` | `class TopoGPT2Trainer` |
| `TopoMoEBrain` | class | `topogpt3/model.py:806` | `class TopoMoEBrain(Module)` |
| `TopoPhasePipeline` | class | `topogpt3/model.py:3467` | `class TopoPhasePipeline` |
| `TopoPhasePipelineV2` | class | `topogpt3/model.py:3338` | `class TopoPhasePipelineV2` |
| `__getitem__` | method | `topogpt3/model.py:1578` | `def __getitem__(self, idx)` |
| `__getitem__` | method | `topogpt3/model.py:1729` | `def __getitem__(self, idx)` |
| `__init__` | method | `topogpt3/model.py:265` | `def __init__(self, in_features, out_features, bias)` |
| `__init__` | method | `topogpt3/model.py:318` | `def __init__(self, in_q, out_q, grid_h, grid_w, init_scale)` |
| `__init__` | method | `topogpt3/model.py:398` | `def __init__(self, config)` |
| `__init__` | method | `topogpt3/model.py:486` | `def __init__(self, d_model, config)` |
| `__init__` | method | `topogpt3/model.py:697` | `def __init__(self, d_head, max_seq_len, base, yarn_factor, yarn_orig_max)` |
| `__init__` | method | `topogpt3/model.py:763` | `def __init__(self, d_model, eps)` |
| `__init__` | method | `topogpt3/model.py:784` | `def __init__(self, d_model, expansion, dropout)` |
| `__init__` | method | `topogpt3/model.py:821` | `def __init__(self, d_model, config)` |
| `__init__` | method | `topogpt3/model.py:921` | `def __init__(self, d_model, n_heads, config)` |
| `__init__` | method | `topogpt3/model.py:1024` | `def __init__(self, d_model, n_heads, config)` |
| `__init__` | method | `topogpt3/model.py:1073` | `def __init__(self, config)` |
| `__init__` | method | `topogpt3/model.py:1282` | `def __init__(self, encoding)` |
| `__init__` | method | `topogpt3/model.py:1408` | `def __init__(self, root, cache_dir, logger)` |
| `__init__` | method | `topogpt3/model.py:1482` | `def __init__(self, cache_dir, logger)` |
| `__init__` | method | `topogpt3/model.py:1570` | `def __init__(self, tokens, seq_len)` |
| `__init__` | method | `topogpt3/model.py:1598` | `def __init__(self, config, logger)` |
| `__init__` | method | `topogpt3/model.py:1706` | `def __init__(self, tokens, seq_len, file_tiers, active_tier, logger)` |
| `__init__` | method | `topogpt3/model.py:1774` | `def __init__(self, base_trainer)` |
| `__init__` | method | `topogpt3/model.py:1848` | `def __init__(self, target_model, config, logger)` |
| `__init__` | method | `topogpt3/model.py:1961` | `def __init__(self, embed, mode)` |
| `__init__` | method | `topogpt3/model.py:2030` | `def __init__(self, model, config, tokenizer)` |
| `__init__` | method | `topogpt3/model.py:2199` | `def __init__(self, config, logger)` |
| `__init__` | method | `topogpt3/model.py:2419` | `def __init__(self, model, config, tokenizer)` |
| `__init__` | method | `topogpt3/model.py:2720` | `def __init__(self, config)` |
| `__init__` | method | `topogpt3/model.py:2955` | `def __init__(self, config, logger)` |
| `__init__` | method | `topogpt3/model.py:3028` | `def __init__(self, config, logger)` |
| `__init__` | method | `topogpt3/model.py:3111` | `def __init__(self, config, logger)` |
| `__init__` | method | `topogpt3/model.py:3197` | `def __init__(self, trainer, t0, cooling_rate, stagnation_patience)` |
| `__init__` | method | `topogpt3/model.py:3349` | `def __init__(self, config, train_tokens, val_tokens, tokenizer, logger, curriculum_tiers, progressive_seq)` |
| `__init__` | method | `topogpt3/model.py:3487` | `def __init__(self, config, train_dataset, val_dataset, tokenizer, logger)` |
| `__len__` | method | `topogpt3/model.py:1575` | `def __len__(self)` |
| `__len__` | method | `topogpt3/model.py:1726` | `def __len__(self)` |
| `__post_init__` | method | `topogpt3/model.py:161` | `def __post_init__(self)` |
| `_build_cache` | method | `topogpt3/model.py:724` | `def _build_cache(self, seq_len)` |
| `_build_dataloader` | method | `topogpt3/model.py:1780` | `def _build_dataloader(self, dataset, seq_len, batch_size, is_train)` |
| `_build_dataloader` | method | `topogpt3/model.py:3362` | `def _build_dataloader(self, tokens, seq_len, batch_size, shuffle, tag)` |
| `_build_draft` | method | `topogpt3/model.py:1856` | `def _build_draft(self)` |
| `_build_phases` | method | `topogpt3/model.py:3376` | `def _build_phases(self)` |
| `_build_torus_graph` | method | `topogpt3/model.py:526` | `def _build_torus_graph(self)` |
| `_compute_entropy` | method | `topogpt3/model.py:1607` | `def _compute_entropy(self, text)` |
| `_content_hash` | method | `topogpt3/model.py:1642` | `def _content_hash(self, text)` |
| `_contract` | method | `topogpt3/model.py:340` | `def _contract(self, W, X)` |
| `_cosine_lr` | method | `topogpt3/model.py:2094` | `def _cosine_lr(self)` |
| `_cosine_lr` | method | `topogpt3/model.py:2490` | `def _cosine_lr(self, step_in_session, total_steps_session)` |
| `_current_state` | method | `topogpt3/model.py:2091` | `def _current_state(self)` |
| `_current_state` | method | `topogpt3/model.py:2479` | `def _current_state(self)` |
| `_filter1d` | method | `topogpt3/model.py:430` | `def _filter1d(self, x, kr, ki)` |
| `_forward_impl` | method | `topogpt3/model.py:1033` | `def _forward_impl(self, x, past_kv)` |
| `_has_long_lines` | method | `topogpt3/model.py:1621` | `def _has_long_lines(self, text, threshold)` |
| `_init_weights` | method | `topogpt3/model.py:1098` | `def _init_weights(self)` |
| `_kernel` | method | `topogpt3/model.py:337` | `def _kernel(self, c)` |
| `_load_model` | method | `topogpt3/model.py:2251` | `def _load_model(self, model, directory)` |
| `_load_optimizer` | method | `topogpt3/model.py:2285` | `def _load_optimizer(self, optimizer, directory, device)` |
| `_load_state` | method | `topogpt3/model.py:2299` | `def _load_state(self, directory)` |
| `_make_dataloaders` | method | `topogpt3/model.py:3497` | `def _make_dataloaders(self, batch_size)` |
| `_measure_ratio` | method | `topogpt3/model.py:2959` | `def _measure_ratio(self, ratio, sample_batch)` |
| `_message_passing` | method | `topogpt3/model.py:587` | `def _message_passing(self, node_feat)` |
| `_progressive_train` | method | `topogpt3/model.py:2106` | `def _progressive_train(self, train_paths, val_paths, tokenizer, phases, memtok)` |
| `_rotate_half` | method | `topogpt3/model.py:732` | `def _rotate_half(self, x)` |
| `_route` | method | `topogpt3/model.py:842` | `def _route(self, x)` |
| `_sample_text` | method | `topogpt3/model.py:2103` | `def _sample_text(self)` |
| `_sample_text` | method | `topogpt3/model.py:2638` | `def _sample_text(self, tokenizer, prompts, max_new, temperature, top_k)` |
| `_save_model` | method | `topogpt3/model.py:2238` | `def _save_model(self, model, directory)` |
| `_save_optimizer` | method | `topogpt3/model.py:2282` | `def _save_optimizer(self, optimizer, directory)` |
| `_save_state` | method | `topogpt3/model.py:2294` | `def _save_state(self, state, directory)` |
| `_set_lr` | method | `topogpt3/model.py:2097` | `def _set_lr(self)` |
| `_set_lr` | method | `topogpt3/model.py:2498` | `def _set_lr(self, lr)` |
| `_special_token_ratio` | method | `topogpt3/model.py:1628` | `def _special_token_ratio(self, text, tokenizer)` |
| `_tokenize_text_to_memmap` | method | `topogpt3/model.py:2162` | `def _tokenize_text_to_memmap(text, tokenizer, path, max_tokens)` |
| `_torus_soft_assign` | method | `topogpt3/model.py:560` | `def _torus_soft_assign(self, phi1, phi2)` |
| `_update_len` | method | `topogpt3/model.py:1716` | `def _update_len(self)` |
| `amp_dtype` | method | `topogpt3/model.py:2053` | `def amp_dtype(self)` |
| `apply_quantization` | method | `topogpt3/model.py:1994` | `def apply_quantization(model, config)` |
| `best_val_loss` | method | `topogpt3/model.py:2073` | `def best_val_loss(self)` |
| `best_val_loss` | method | `topogpt3/model.py:2077` | `def best_val_loss(self, v)` |
| `build_file_tiers` | method | `topogpt3/model.py:1737` | `def build_file_tiers(paths, short, med)` |
| `cache_tokens` | method | `topogpt3/model.py:2037` | `def cache_tokens(self, key, tokens)` |
| `ckpt_fn` | method | `topogpt3/model.py:1050` | `def ckpt_fn(x_in)` |
| `ckpt_mgr` | method | `topogpt3/model.py:2085` | `def ckpt_mgr(self)` |
| `classify_phase` | method | `topogpt3/model.py:2875` | `def classify_phase(self, delta, kappa, berry)` |
| `completed_epochs` | method | `topogpt3/model.py:2057` | `def completed_epochs(self)` |
| `completed_epochs` | method | `topogpt3/model.py:2061` | `def completed_epochs(self, v)` |
| `compute_all` | method | `topogpt3/model.py:2894` | `def compute_all(self, model, lr, dataloader, compute_kappa)` |
| `compute_alpha` | method | `topogpt3/model.py:2735` | `def compute_alpha(self, delta)` |
| `compute_berry_phase` | method | `topogpt3/model.py:2832` | `def compute_berry_phase(self, model)` |
| `compute_delta` | method | `topogpt3/model.py:2728` | `def compute_delta(self, model)` |
| `compute_kappa` | method | `topogpt3/model.py:2774` | `def compute_kappa(self, model, dataloader, n_batches)` |
| `compute_lc` | method | `topogpt3/model.py:2845` | `def compute_lc(self, model)` |
| `compute_sp` | method | `topogpt3/model.py:2859` | `def compute_sp(self, model)` |
| `compute_t_eff` | method | `topogpt3/model.py:2766` | `def compute_t_eff(self, lr)` |
| `conjugate` | method | `topogpt3/model.py:238` | `def conjugate(q)` |
| `count_params` | method | `topogpt3/model.py:1178` | `def count_params(self)` |
| `decode` | method | `topogpt3/model.py:441` | `def decode(self, z)` |
| `decode` | method | `topogpt3/model.py:1293` | `def decode(self, tokens)` |
| `enable_yarn` | method | `topogpt3/model.py:716` | `def enable_yarn(self, factor, orig_max)` |
| `encode` | method | `topogpt3/model.py:436` | `def encode(self, x)` |
| `encode` | method | `topogpt3/model.py:1290` | `def encode(self, text)` |
| `eot_token` | method | `topogpt3/model.py:1296` | `def eot_token(self)` |
| `evaluate` | method | `topogpt3/model.py:2100` | `def evaluate(self, dataloader)` |
| `evaluate` | method | `topogpt3/model.py:2670` | `def evaluate(self, dataloader)` |
| `filter_file` | method | `topogpt3/model.py:1645` | `def filter_file(self, path, tokenizer)` |
| `format_log` | method | `topogpt3/model.py:2919` | `def format_log(self, m)` |
| `forward` | method | `topogpt3/model.py:281` | `def forward(self, x)` |
| `forward` | method | `topogpt3/model.py:344` | `def forward(self, x)` |
| `forward` | method | `topogpt3/model.py:446` | `def forward(self, x)` |
| `forward` | method | `topogpt3/model.py:624` | `def forward(self, x)` |
| `forward` | method | `topogpt3/model.py:736` | `def forward(self, q, k, seq_len, offset)` |
| `forward` | method | `topogpt3/model.py:768` | `def forward(self, x)` |
| `forward` | method | `topogpt3/model.py:798` | `def forward(self, x)` |
| `forward` | method | `topogpt3/model.py:884` | `def forward(self, x)` |
| `forward` | method | `topogpt3/model.py:940` | `def forward(self, x, is_causal, past_kv)` |
| `forward` | method | `topogpt3/model.py:1042` | `def forward(self, x, past_kv)` |
| `forward` | method | `topogpt3/model.py:1105` | `def forward(self, token_ids, past_kvs)` |
| `forward` | method | `topogpt3/model.py:1990` | `def forward(self, indices)` |
| `forward_with_memory` | method | `topogpt3/model.py:1128` | `def forward_with_memory(self, token_ids)` |
| `generate` | method | `topogpt3/model.py:1184` | `def generate(self, token_ids, max_new_tokens, temperature, top_k, repetition_penalty)` |
| `generate` | method | `topogpt3/model.py:1870` | `def generate(self, token_ids, max_new_tokens, temperature, top_k, repetition_penalty)` |
| `generate_with_continuation` | method | `topogpt3/model.py:1235` | `def generate_with_continuation(self, token_ids, tokenizer, max_new_tokens, temperature, top_k, repetition_penalty, max_c` |
| `global_step` | method | `topogpt3/model.py:2065` | `def global_step(self)` |
| `global_step` | method | `topogpt3/model.py:2069` | `def global_step(self, v)` |
| `hamilton_product` | method | `topogpt3/model.py:222` | `def hamilton_product(q1, q2)` |
| `has_checkpoint` | method | `topogpt3/model.py:2397` | `def has_checkpoint(self)` |
| `history` | method | `topogpt3/model.py:2081` | `def history(self)` |
| `load_best` | method | `topogpt3/model.py:2385` | `def load_best(self, model)` |
| `load_latest` | method | `topogpt3/model.py:2358` | `def load_latest(self, model, optimizer)` |
| `main` | method | `topogpt3/model.py:3589` | `def main()` |
| `mine` | method | `topogpt3/model.py:3115` | `def mine(self, seed_start, n_seeds, train_dataset, prospect_steps)` |
| `model` | method | `topogpt3/model.py:2041` | `def model(self)` |
| `normalize` | method | `topogpt3/model.py:234` | `def normalize(q, eps)` |
| `optimize` | method | `topogpt3/model.py:2988` | `def optimize(self, dataloader)` |
| `optimizer` | method | `topogpt3/model.py:2045` | `def optimizer(self)` |
| `patch_config_for_resume` | method | `topogpt3/model.py:2209` | `def patch_config_for_resume(self, cfg)` |
| `process_torus_grid` | method | `topogpt3/model.py:453` | `def process_torus_grid(self, grid)` |
| `prospect` | method | `topogpt3/model.py:3032` | `def prospect(self, candidates, train_dataset, prospect_steps)` |
| `refine` | method | `topogpt3/model.py:3206` | `def refine(self, train_dl, val_dl, refine_epochs)` |
| `report` | method | `topogpt3/model.py:1685` | `def report(self)` |
| `resume` | method | `topogpt3/model.py:2088` | `def resume(self)` |
| `resume` | method | `topogpt3/model.py:2454` | `def resume(self)` |
| `rotate_vector` | method | `topogpt3/model.py:243` | `def rotate_vector(v, q)` |
| `run` | method | `topogpt3/model.py:1790` | `def run(self, train_paths, val_paths, tokenizer, file_tiers, phases)` |
| `run` | method | `topogpt3/model.py:3385` | `def run(self, run_prospect, refine_epochs, resume, prospect_steps, probe_seeds, seed_start)` |
| `run` | method | `topogpt3/model.py:3509` | `def run(self, run_prospect, refine_epochs, resume, prospect_steps, probe_seeds, seed_start)` |
| `run_curriculum` | method | `topogpt3/model.py:2148` | `def run_curriculum(self, train_paths, val_paths, tokenizer, phases)` |
| `save` | method | `topogpt3/model.py:2313` | `def save(self, model, optimizer, state, is_best)` |
| `scaler` | method | `topogpt3/model.py:2049` | `def scaler(self)` |
| `scan` | method | `topogpt3/model.py:1415` | `def scan(self, force)` |
| `set_seed` | method | `topogpt3/model.py:202` | `def set_seed(seed, device)` |
| `set_tier` | method | `topogpt3/model.py:1722` | `def set_tier(self, tier)` |
| `setup_logger` | method | `topogpt3/model.py:192` | `def setup_logger(name, level)` |
| `should_save` | method | `topogpt3/model.py:2310` | `def should_save(self)` |
| `tokenize` | method | `topogpt3/model.py:1487` | `def tokenize(self, file_paths, tokenizer, cache_key, max_tokens, min_chars)` |
| `train` | method | `topogpt3/model.py:2145` | `def train(self, train_dl, val_dl)` |
| `train` | method | `topogpt3/model.py:2502` | `def train(self, train_dl, val_dl)` |
| `update_grad_buffer` | method | `topogpt3/model.py:2740` | `def update_grad_buffer(self, model)` |
| `base_rewards` | function | `topogpt3/rewards.py:25` | `def base_rewards(prompts, completions, reward_fn, device)` |
| `distillation_loss` | function | `topogpt3/rewards.py:108` | `def distillation_loss(student_logits, teacher_logits, mask, labels, alpha, temp)` |
| `dpo_loss_fn` | function | `topogpt3/rewards.py:99` | `def dpo_loss_fn(ref_lp, pol_lp, mask, beta)` |
| `grpo_advantages` | function | `topogpt3/rewards.py:67` | `def grpo_advantages(rewards, num_generations)` |
| `grpo_loss` | function | `topogpt3/rewards.py:79` | `def grpo_loss(new_logp, old_logp, ref_logp, adv, mask, beta, eps, loss_type, eps_high)` |
| `k3_kl` | function | `topogpt3/rewards.py:74` | `def k3_kl(ref_logp, new_logp)` |
| `logits_to_log_probs` | function | `topogpt3/rewards.py:94` | `def logits_to_log_probs(logits, labels)` |
| `rep_penalty` | function | `topogpt3/rewards.py:17` | `def rep_penalty(text, n, cap)` |
| `spectral_bonus` | function | `topogpt3/rewards.py:55` | `def spectral_bonus(fisher_gap, drift, w_fisher, w_drift)` |
| `RolloutEngine` | class | `topogpt3/rollout.py:39` | `class RolloutEngine(ABC)` |
| `RolloutResult` | class | `topogpt3/rollout.py:18` | `class RolloutResult` |
| `TorchRolloutEngine` | class | `topogpt3/rollout.py:50` | `class TorchRolloutEngine(RolloutEngine)` |
| `__init__` | method | `topogpt3/rollout.py:51` | `def __init__(self, policy_model, tokenizer, device, decode)` |
| `compute_per_token_logps` | method | `topogpt3/rollout.py:27` | `def compute_per_token_logps(model, input_ids, n_keep)` |
| `create_rollout_engine` | method | `topogpt3/rollout.py:83` | `def create_rollout_engine(policy_model, tokenizer, device)` |
| `rollout` | method | `topogpt3/rollout.py:41` | `def rollout(self, prompt_ids, num_generations, max_new_tokens, temperature, tokenizer)` |
| `rollout` | method | `topogpt3/rollout.py:57` | `def rollout(self, prompt_ids, num_generations, max_new_tokens, temperature, tokenizer)` |
| `update_policy` | method | `topogpt3/rollout.py:46` | `def update_policy(self, model)` |
| `update_policy` | method | `topogpt3/rollout.py:79` | `def update_policy(self, model)` |
| `execute_tool` | function | `topogpt3/tools_agent.py:59` | `def execute_tool(name, args)` |
| `rollout_multiturn` | function | `topogpt3/tools_agent.py:80` | `def rollout_multiturn(generate_fn, tokenizer, messages, tools, max_turns, max_new_tokens, open_thinking)` |
| `BlockTokenDataset` | class | `topogpt3/train.py:1000` | `class BlockTokenDataset(Dataset)` |
| `CheckpointStore` | class | `topogpt3/train.py:1027` | `class CheckpointStore` |
| `CodeCurriculumLoader` | class | `topogpt3/train.py:713` | `class CodeCurriculumLoader` |
| `EfficiencyMetrics` | class | `topogpt3/train.py:585` | `class EfficiencyMetrics` |
| `GrassmannianTracker` | class | `topogpt3/train.py:197` | `class GrassmannianTracker` |
| `TopoGPT3Config` | class | `topogpt3/train.py:83` | `class TopoGPT3Config` |
| `TopoGPT3Trainer` | class | `topogpt3/train.py:1103` | `class TopoGPT3Trainer` |
| `__getitem__` | method | `topogpt3/train.py:1014` | `def __getitem__(self, idx)` |
| `__init__` | method | `topogpt3/train.py:217` | `def __init__(self, config, logger)` |
| `__init__` | method | `topogpt3/train.py:600` | `def __init__(self, model, config, logger, gauss_enabled)` |
| `__init__` | method | `topogpt3/train.py:729` | `def __init__(self, config, tokenizer, logger)` |
| `__init__` | method | `topogpt3/train.py:1006` | `def __init__(self, tokens, seq_len)` |
| `__init__` | method | `topogpt3/train.py:1030` | `def __init__(self, root, max_keep, logger)` |
| `__init__` | method | `topogpt3/train.py:1119` | `def __init__(self, config, start_tier)` |
| `__len__` | method | `topogpt3/train.py:1011` | `def __len__(self)` |
| `_accumulate_winding` | method | `topogpt3/train.py:429` | `def _accumulate_winding(self, U_new)` |
| `_already_prepared` | method | `topogpt3/train.py:828` | `def _already_prepared(self, tier)` |
| `_build_loaders` | method | `topogpt3/train.py:1190` | `def _build_loaders(self, tier_index)` |
| `_cosine_lr` | method | `topogpt3/train.py:1222` | `def _cosine_lr(self, step, total_steps)` |
| `_dominant_subspace` | method | `topogpt3/train.py:277` | `def _dominant_subspace(self, K)` |
| `_elbow_rank` | method | `topogpt3/train.py:268` | `def _elbow_rank(self, sigmas)` |
| `_embed_params` | method | `topogpt3/train.py:611` | `def _embed_params(model)` |
| `_eval_combined_holdout` | method | `topogpt3/train.py:1506` | `def _eval_combined_holdout(self)` |
| `_evaluate` | method | `topogpt3/train.py:1398` | `def _evaluate(self, dl)` |
| `_flatten_grads` | method | `topogpt3/train.py:295` | `def _flatten_grads(model, max_per_tensor)` |
| `_format_code_feedback` | method | `topogpt3/train.py:757` | `def _format_code_feedback(ex)` |
| `_format_codealpaca` | method | `topogpt3/train.py:746` | `def _format_codealpaca(ex)` |
| `_format_magicoder` | method | `topogpt3/train.py:777` | `def _format_magicoder(ex)` |
| `_format_tiny_stack` | method | `topogpt3/train.py:785` | `def _format_tiny_stack(ex)` |
| `_gauss_complex_contract` | method | `topogpt3/train.py:532` | `def _gauss_complex_contract(self, W, X)` |
| `_get_formatter` | method | `topogpt3/train.py:797` | `def _get_formatter(cls, tier)` |
| `_load_hf_with_fallback` | method | `topogpt3/train.py:858` | `def _load_hf_with_fallback(self, tier)` |
| `_manifest_path` | method | `topogpt3/train.py:825` | `def _manifest_path(self, tier)` |
| `_project_unitary` | method | `topogpt3/train.py:381` | `def _project_unitary(M)` |
| `_set_lr` | method | `topogpt3/train.py:1229` | `def _set_lr(self, lr)` |
| `_stack_spectral_kernels` | method | `topogpt3/train.py:231` | `def _stack_spectral_kernels(model)` |
| `_state_dict` | method | `topogpt3/train.py:1436` | `def _state_dict(self)` |
| `_tier_paths` | method | `topogpt3/train.py:819` | `def _tier_paths(self, tier)` |
| `_train_one_tier` | method | `topogpt3/train.py:1237` | `def _train_one_tier(self, tier_index)` |
| `apply_gauss_patch` | method | `topogpt3/train.py:568` | `def apply_gauss_patch(logger)` |
| `build_topogpt2_config` | method | `topogpt3/train.py:170` | `def build_topogpt2_config(self, max_seq_len, attn_window)` |
| `compute` | method | `topogpt3/train.py:664` | `def compute(self, dataloader, vocab_size, val_loss, val_ppl, val_acc, batch_size, seq_len)` |
| `conjugation_distance_su2` | method | `topogpt3/train.py:412` | `def conjugation_distance_su2(U1, U2)` |
| `estimate_bytes_per_step` | method | `topogpt3/train.py:656` | `def estimate_bytes_per_step(self, batch_size, seq_len, dtype_bytes)` |
| `estimate_fisher_gap` | method | `topogpt3/train.py:313` | `def estimate_fisher_gap(self, model, dataloader, vocab_size, r_target)` |
| `estimate_flops_per_step` | method | `topogpt3/train.py:651` | `def estimate_flops_per_step(self, batch_size, seq_len)` |
| `flush` | method | `topogpt3/train.py:922` | `def flush(split)` |
| `format_log` | method | `topogpt3/train.py:500` | `def format_log(self, snap)` |
| `format_log` | method | `topogpt3/train.py:696` | `def format_log(self, m)` |
| `load_latest` | method | `topogpt3/train.py:1071` | `def load_latest(self, model, optimizer)` |
| `main` | method | `topogpt3/train.py:1567` | `def main()` |
| `measure_throughput` | method | `topogpt3/train.py:619` | `def measure_throughput(self, dataloader, vocab_size)` |
| `open_memmap` | method | `topogpt3/train.py:986` | `def open_memmap(self, tier, split)` |
| `parse_args` | method | `topogpt3/train.py:1538` | `def parse_args()` |
| `prepare_all` | method | `topogpt3/train.py:1174` | `def prepare_all(self, force)` |
| `prepare_tier` | method | `topogpt3/train.py:891` | `def prepare_tier(self, tier_index, force)` |
| `run` | method | `topogpt3/train.py:1449` | `def run(self)` |
| `save` | method | `topogpt3/train.py:522` | `def save(self, path)` |
| `save` | method | `topogpt3/train.py:1037` | `def save(self, tag, model, optimizer, state)` |
| `should_save` | method | `topogpt3/train.py:1095` | `def should_save(self, interval_min)` |
| `snapshot` | method | `topogpt3/train.py:445` | `def snapshot(self, model, step, dataloader, vocab_size)` |
| `update_holonomy` | method | `topogpt3/train.py:386` | `def update_holonomy(self, U_new)` |
| `agent_reward` | function | `topogpt3/train_agent.py:31` | `def agent_reward(text, gt, used_tools)` |
| `main` | function | `topogpt3/train_agent.py:43` | `def main()` |
| `main` | function | `topogpt3/train_distill.py:24` | `def main()` |
| `load_model` | function | `topogpt3/train_dpo.py:24` | `def load_model(checkpoint, device)` |
| `main` | function | `topogpt3/train_dpo.py:33` | `def main()` |
| `_gather` | function | `topogpt3/train_grpo.py:88` | `def _gather(lg, _plen, _R, _comp)` |
| `main` | function | `topogpt3/train_grpo.py:29` | `def main()` |
| `load_base` | function | `topogpt3/train_lora.py:25` | `def load_base(checkpoint, device)` |
| `main` | function | `topogpt3/train_lora.py:36` | `def main()` |
| `TopoCritic` | class | `topogpt3/train_ppo.py:29` | `class TopoCritic(Module)` |
| `__init__` | method | `topogpt3/train_ppo.py:30` | `def __init__(self, trunk)` |
| `forward` | method | `topogpt3/train_ppo.py:36` | `def forward(self, ids)` |
| `main` | method | `topogpt3/train_ppo.py:45` | `def main()` |
| `Logger` | function | `topogpt3/trainer_utils_topo.py:20` | `def Logger(content, quiet)` |
| `SkipBatchSampler` | class | `topogpt3/trainer_utils_topo.py:52` | `class SkipBatchSampler(Sampler)` |
| `__init__` | method | `topogpt3/trainer_utils_topo.py:53` | `def __init__(self, sampler, batch_size, skip_batches)` |
| `__iter__` | method | `topogpt3/trainer_utils_topo.py:58` | `def __iter__(self)` |
| `__len__` | method | `topogpt3/trainer_utils_topo.py:72` | `def __len__(self)` |
| `get_lr` | function | `topogpt3/trainer_utils_topo.py:29` | `def get_lr(current_step, total_steps, lr)` |
| `init_distributed_mode` | function | `topogpt3/trainer_utils_topo.py:43` | `def init_distributed_mode()` |
| `is_main_process` | function | `topogpt3/trainer_utils_topo.py:25` | `def is_main_process()` |
| `setup_seed` | function | `topogpt3/trainer_utils_topo.py:34` | `def setup_seed(seed)` |
| `topo_checkpoint` | method | `topogpt3/trainer_utils_topo.py:77` | `def topo_checkpoint(save_dir, weight, model, optimizer, scheduler, scaler, epoch, step, wandb, extra)` |
| `YaRNConfig` | class | `topogpt3/yarn.py:18` | `class YaRNConfig` |
| `apply_yarn_to_rope` | method | `topogpt3/yarn.py:50` | `def apply_yarn_to_rope(rope_module, cfg)` |
| `yarn_scale_inv_freq` | method | `topogpt3/yarn.py:26` | `def yarn_scale_inv_freq(inv_freq, d_head, cfg)` |
