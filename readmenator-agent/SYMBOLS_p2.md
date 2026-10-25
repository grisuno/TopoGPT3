# Symbols (page 2 of 3)
Previous: [SYMBOLS.md](SYMBOLS.md)

| Symbol | Kind | File:Line | Signature |
|--------|------|-----------|-----------|
| `_tool_call_stream_chunks` | function | `topogpt3/api_server.py:1427` | `def _tool_call_stream_chunks(text_stream, allowed_tools, model_name, t0_ms)` |
| `allow` | method | `topogpt3/api_server.py:252` | `def allow(self, key, role)` |
| `chat_completions` | function | `topogpt3/api_server.py:1109` | `def chat_completions(req, request)` |
| `complete` | method | `topogpt3/api_server.py:572` | `def complete(self, prompt)` |
| `complete_candidates` | method | `topogpt3/api_server.py:516` | `def complete_candidates(self, prompt)` |
| `completions` | function | `topogpt3/api_server.py:1004` | `def completions(req, request)` |
| `consume` | method | `topogpt3/api_server.py:227` | `def consume(self, n)` |
| `emit` | function | `topogpt3/api_server.py:1449` | `def emit(delta, finish)` |
| `health` | function | `topogpt3/api_server.py:946` | `def health(request)` |
| `is_banned` | method | `topogpt3/api_server.py:290` | `def is_banned(self, ip)` |
| `lifespan` | function | `topogpt3/api_server.py:806` | `def lifespan(app)` |
| `list_models` | function | `topogpt3/api_server.py:953` | `def list_models(request)` |
| `load_model` | function | `topogpt3/api_server.py:771` | `def load_model(checkpoint, device)` |
| `main` | function | `topogpt3/api_server.py:1546` | `def main()` |
| `record_failure` | method | `topogpt3/api_server.py:278` | `def record_failure(self, ip)` |
| `stream_complete` | method | `topogpt3/api_server.py:601` | `def stream_complete(self, prompt)` |
| `validate` | method | `topogpt3/api_server.py:164` | `def validate(self, raw)` |
| `_fmt_tool_defs` | function | `topogpt3/chat.py:60` | `def _fmt_tool_defs(tools)` |
| `_tool_calls_text` | function | `topogpt3/chat.py:85` | `def _tool_calls_text(tc)` |
| `apply_chat_template` | function | `topogpt3/chat.py:112` | `def apply_chat_template(messages, tools, add_generation_prompt, open_thinking)` |
| `parse_thinking` | function | `topogpt3/chat.py:170` | `def parse_thinking(text)` |
| `parse_tool_calls` | function | `topogpt3/chat.py:160` | `def parse_tool_calls(text)` |
| `post_processing_chat` | function | `topogpt3/chat.py:54` | `def post_processing_chat(prompt, empty_think_ratio)` |
| `pre_processing_chat` | function | `topogpt3/chat.py:43` | `def pre_processing_chat(conversations, add_system_ratio)` |
| `split_reasoning_content` | function | `topogpt3/chat.py:178` | `def split_reasoning_content(text)` |
| `config_dict` | function | `topogpt3/checkpoint_meta.py:129` | `def config_dict(cfg)` |
| `config_from_checkpoint` | function | `topogpt3/checkpoint_meta.py:81` | `def config_from_checkpoint(checkpoint_dir, device, scale)` |
| `probe_checkpoint` | function | `topogpt3/checkpoint_meta.py:35` | `def probe_checkpoint(checkpoint_dir)` |
| `read_state` | function | `topogpt3/checkpoint_meta.py:24` | `def read_state(checkpoint_dir)` |
| `state_summary` | function | `topogpt3/checkpoint_meta.py:120` | `def state_summary(checkpoint_dir)` |
| `_count_unclosed_brackets` | function | `topogpt3/continuation.py:25` | `def _count_unclosed_brackets(text)` |
| `_count_unclosed_fences` | function | `topogpt3/continuation.py:36` | `def _count_unclosed_fences(text)` |
| `extract_tail_for_continuation` | function | `topogpt3/continuation.py:75` | `def extract_tail_for_continuation(text, tail_lines, tail_chars)` |
| `is_response_complete` | function | `topogpt3/continuation.py:45` | `def is_response_complete(text, min_chars)` |
| `split_at_last_newline` | function | `topogpt3/continuation.py:105` | `def split_at_last_newline(text)` |
| `export_hf_stub` | function | `topogpt3/convert.py:38` | `def export_hf_stub(ckpt_dir, out_dir)` |
| `main` | function | `topogpt3/convert.py:49` | `def main()` |
| `merge_base_lora` | function | `topogpt3/convert.py:19` | `def merge_base_lora(base_dir, lora_path, out_dir)` |
| `evaluate` | function | `topogpt3/eval_toolcall.py:91` | `def evaluate(generate_fn)` |
| `run_case` | function | `topogpt3/eval_toolcall.py:36` | `def run_case(generate_fn, prompt, expect_tool, expect_args)` |
| `_iter_pairs` | function | `topogpt3/export_chat.py:65` | `def _iter_pairs(loader, tier, cap)` |
| `_pairs_code_feedback` | function | `topogpt3/export_chat.py:38` | `def _pairs_code_feedback(ex)` |
| `_pairs_codealpaca` | function | `topogpt3/export_chat.py:28` | `def _pairs_codealpaca(ex)` |
| `_pairs_magicoder` | function | `topogpt3/export_chat.py:55` | `def _pairs_magicoder(ex)` |
| `main` | function | `topogpt3/export_chat.py:81` | `def main()` |
| `Profile` | class | `topogpt3/fallback.py:110` | `class Profile` |
| `_extract_code` | function | `topogpt3/fallback.py:300` | `def _extract_code(text)` |
| `_json_valid` | function | `topogpt3/fallback.py:305` | `def _json_valid(text)` |
| `_repetition` | function | `topogpt3/fallback.py:317` | `def _repetition(text, n)` |
| `_valid_target` | function | `topogpt3/fallback.py:250` | `def _valid_target(value)` |
| `models_payload` | function | `topogpt3/fallback.py:227` | `def models_payload(default_checkpoint)` |
| `rank_candidates` | function | `topogpt3/fallback.py:441` | `def rank_candidates(candidates, profile, prompt, allowed_tools)` |
| `resolve_profile` | function | `topogpt3/fallback.py:221` | `def resolve_profile(model)` |
| `score_candidate` | function | `topogpt3/fallback.py:325` | `def score_candidate(text, profile, prompt, allowed_tools)` |
| `select_best` | function | `topogpt3/fallback.py:404` | `def select_best(candidates, profile, prompt, allowed_tools)` |
| `split_response` | function | `topogpt3/fallback.py:435` | `def split_response(text)` |
| `synthesize_tool_call` | function | `topogpt3/fallback.py:456` | `def synthesize_tool_call(profile, prompt)` |
| `tool_calls_payload` | function | `topogpt3/fallback.py:418` | `def tool_calls_payload(text)` |
| `tool_names` | method | `topogpt3/fallback.py:125` | `def tool_names(self)` |
| `validate_tool_call` | function | `topogpt3/fallback.py:256` | `def validate_tool_call(call, allowed)` |
| `CheckpointPaths` | class | `topogpt3/inference.py:236` | `class CheckpointPaths` |
| `CliArgumentParser` | class | `topogpt3/inference.py:678` | `class CliArgumentParser` |
| `GaussPatchApplier` | class | `topogpt3/inference.py:403` | `class GaussPatchApplier` |
| `GenerationEngine` | class | `topogpt3/inference.py:521` | `class GenerationEngine` |
| `GenerationReport` | class | `topogpt3/inference.py:507` | `class GenerationReport` |
| `InferenceLoggerFactory` | class | `topogpt3/inference.py:163` | `class InferenceLoggerFactory` |
| `InferencePipeline` | class | `topogpt3/inference.py:612` | `class InferencePipeline` |
| `InferenceSettings` | class | `topogpt3/inference.py:44` | `class InferenceSettings` |
| `ModelAssembler` | class | `topogpt3/inference.py:422` | `class ModelAssembler` |
| `ResultRenderer` | class | `topogpt3/inference.py:586` | `class ResultRenderer` |
| `SamplingPolicy` | class | `topogpt3/inference.py:487` | `class SamplingPolicy` |
| `ScalePreset` | class | `topogpt3/inference.py:34` | `class ScalePreset` |
| `SecurePathResolver` | class | `topogpt3/inference.py:185` | `class SecurePathResolver` |
| `SeedSynchronizer` | class | `topogpt3/inference.py:461` | `class SeedSynchronizer` |
| `SourceModuleLoader` | class | `topogpt3/inference.py:218` | `class SourceModuleLoader` |
| `TokenizerFactory` | class | `topogpt3/inference.py:390` | `class TokenizerFactory` |
| `TopoGPT2ConfigAligner` | class | `topogpt3/inference.py:331` | `class TopoGPT2ConfigAligner` |
| `WeightShapeProbe` | class | `topogpt3/inference.py:284` | `class WeightShapeProbe` |
| `__init__` | method | `topogpt3/inference.py:221` | `def __init__(self, settings, logger)` |
| `__init__` | method | `topogpt3/inference.py:239` | `def __init__(self, settings)` |
| `__init__` | method | `topogpt3/inference.py:287` | `def __init__(self, settings, logger)` |
| `__init__` | method | `topogpt3/inference.py:334` | `def __init__(self, settings, source_module, logger)` |
| `__init__` | method | `topogpt3/inference.py:393` | `def __init__(self, settings, source_module)` |
| `__init__` | method | `topogpt3/inference.py:406` | `def __init__(self, settings, source_module, logger)` |
| `__init__` | method | `topogpt3/inference.py:425` | `def __init__(self, settings, source_module, logger)` |
| `__init__` | method | `topogpt3/inference.py:464` | `def __init__(self, settings, source_module, logger)` |
| `__init__` | method | `topogpt3/inference.py:524` | `def __init__(self, settings, logger)` |
| `__init__` | method | `topogpt3/inference.py:589` | `def __init__(self, settings, logger)` |
| `__init__` | method | `topogpt3/inference.py:615` | `def __init__(self, settings, logger)` |
| `apply` | method | `topogpt3/inference.py:471` | `def apply(self)` |
| `apply_if_enabled` | method | `topogpt3/inference.py:413` | `def apply_if_enabled(self)` |
| `assemble` | method | `topogpt3/inference.py:432` | `def assemble(self, aligned_cfg, paths)` |
| `assert_ready` | method | `topogpt3/inference.py:266` | `def assert_ready(self)` |
| `build` | method | `topogpt3/inference.py:167` | `def build(settings)` |
| `build` | method | `topogpt3/inference.py:341` | `def build(self, n_kv_heads, vocab_size)` |
| `build` | method | `topogpt3/inference.py:397` | `def build(self)` |
| `build_parser` | method | `topogpt3/inference.py:682` | `def build_parser()` |
| `detect_n_kv_heads` | method | `topogpt3/inference.py:291` | `def detect_n_kv_heads(self, weights_path, d_model, n_heads)` |
| `execute` | method | `topogpt3/inference.py:622` | `def execute(self)` |
| `from_settings` | method | `topogpt3/inference.py:496` | `def from_settings(cls, settings)` |
| `load` | method | `topogpt3/inference.py:225` | `def load(self)` |
| `main` | function | `topogpt3/inference.py:814` | `def main(argv)` |
| `model_file` | method | `topogpt3/inference.py:252` | `def model_file(self)` |
| `parse` | method | `topogpt3/inference.py:791` | `def parse(argv)` |
| `preset` | method | `topogpt3/inference.py:120` | `def preset(self)` |
| `render` | method | `topogpt3/inference.py:593` | `def render(self, report)` |
| `require_existing_file` | method | `topogpt3/inference.py:205` | `def require_existing_file(path, expected_suffix)` |
| `resolve_under` | method | `topogpt3/inference.py:189` | `def resolve_under(root)` |
| `run` | method | `topogpt3/inference.py:529` | `def run(self, model, tokenizer, prompt, policy)` |
| `scale_presets` | method | `topogpt3/inference.py:105` | `def scale_presets()` |
| `slot_dir` | method | `topogpt3/inference.py:248` | `def slot_dir(self)` |
| `state_file` | method | `topogpt3/inference.py:259` | `def state_file(self)` |
| `tokens_per_second` | method | `topogpt3/inference.py:516` | `def tokens_per_second(self, elapsed_floor)` |
| `validate` | method | `topogpt3/inference.py:130` | `def validate(self)` |
| `CheckpointPaths` | class | `topogpt3/inference_hrm.py:416` | `class CheckpointPaths` |
| `CliArgumentParser` | class | `topogpt3/inference_hrm.py:1402` | `class CliArgumentParser` |
| `GaussPatchApplier` | class | `topogpt3/inference_hrm.py:583` | `class GaussPatchApplier` |
| `GenerationReasoningSummary` | class | `topogpt3/inference_hrm.py:704` | `class GenerationReasoningSummary` |
| `GenerationReport` | class | `topogpt3/inference_hrm.py:1066` | `class GenerationReport` |
| `HRMGenerationEngine` | class | `topogpt3/inference_hrm.py:1081` | `class HRMGenerationEngine` |
| `HRMInferencePipeline` | class | `topogpt3/inference_hrm.py:1336` | `class HRMInferencePipeline` |
| `HRMInferenceSettings` | class | `topogpt3/inference_hrm.py:136` | `class HRMInferenceSettings` |
| `HRMLoggerFactory` | class | `topogpt3/inference_hrm.py:343` | `class HRMLoggerFactory` |
| `HierarchicalRecursiveReasoner` | class | `topogpt3/inference_hrm.py:772` | `class HierarchicalRecursiveReasoner` |
| `LatentChangeMetric` | class | `topogpt3/inference_hrm.py:668` | `class LatentChangeMetric` |
| `LogitsSampler` | class | `topogpt3/inference_hrm.py:1010` | `class LogitsSampler` |
| `ModelAssembler` | class | `topogpt3/inference_hrm.py:602` | `class ModelAssembler` |
| `ReasoningIterationStats` | class | `topogpt3/inference_hrm.py:691` | `class ReasoningIterationStats` |
| `RecursiveReasoningConfig` | class | `topogpt3/inference_hrm.py:66` | `class RecursiveReasoningConfig` |
| `ResultRenderer` | class | `topogpt3/inference_hrm.py:1289` | `class ResultRenderer` |
| `SamplingPolicy` | class | `topogpt3/inference_hrm.py:1044` | `class SamplingPolicy` |
| `ScalePreset` | class | `topogpt3/inference_hrm.py:56` | `class ScalePreset` |
| `SecurePathResolver` | class | `topogpt3/inference_hrm.py:365` | `class SecurePathResolver` |
| `SeedSynchronizer` | class | `topogpt3/inference_hrm.py:643` | `class SeedSynchronizer` |
| `SourceModuleLoader` | class | `topogpt3/inference_hrm.py:398` | `class SourceModuleLoader` |
| `SparseHighLevelStateCache` | class | `topogpt3/inference_hrm.py:727` | `class SparseHighLevelStateCache` |
| `TokenizerFactory` | class | `topogpt3/inference_hrm.py:570` | `class TokenizerFactory` |
| `TopoGPT2ConfigAligner` | class | `topogpt3/inference_hrm.py:511` | `class TopoGPT2ConfigAligner` |
| `WeightShapeProbe` | class | `topogpt3/inference_hrm.py:464` | `class WeightShapeProbe` |
| `__init__` | method | `topogpt3/inference_hrm.py:401` | `def __init__(self, settings, logger)` |
| `__init__` | method | `topogpt3/inference_hrm.py:419` | `def __init__(self, settings)` |
| `__init__` | method | `topogpt3/inference_hrm.py:467` | `def __init__(self, settings, logger)` |
| `__init__` | method | `topogpt3/inference_hrm.py:514` | `def __init__(self, settings, source_module, logger)` |
| `__init__` | method | `topogpt3/inference_hrm.py:573` | `def __init__(self, settings, source_module)` |
| `__init__` | method | `topogpt3/inference_hrm.py:586` | `def __init__(self, settings, source_module, logger)` |
| `__init__` | method | `topogpt3/inference_hrm.py:605` | `def __init__(self, settings, source_module, logger)` |
| `__init__` | method | `topogpt3/inference_hrm.py:646` | `def __init__(self, settings, source_module, logger)` |
| `__init__` | method | `topogpt3/inference_hrm.py:671` | `def __init__(self, epsilon_floor)` |
| `__init__` | method | `topogpt3/inference_hrm.py:736` | `def __init__(self, persist_tokens)` |
| `__init__` | method | `topogpt3/inference_hrm.py:813` | `def __init__(self, layers, final_norm, reasoning_config, logger)` |
| `__init__` | method | `topogpt3/inference_hrm.py:1013` | `def __init__(self, logger)` |
| `__init__` | method | `topogpt3/inference_hrm.py:1092` | `def __init__(self, settings, logger)` |
| `__init__` | method | `topogpt3/inference_hrm.py:1292` | `def __init__(self, settings, logger)` |
| `__init__` | method | `topogpt3/inference_hrm.py:1339` | `def __init__(self, settings, logger)` |
| `_encode_prompt` | method | `topogpt3/inference_hrm.py:1097` | `def _encode_prompt(self, model, prompt_ids)` |
| `_full_pass` | method | `topogpt3/inference_hrm.py:841` | `def _full_pass(self, z_in, base_kvs, position_offset)` |
| `_window_pass` | method | `topogpt3/inference_hrm.py:861` | `def _window_pass(self, z_in, base_kvs, window, position_offset)` |
| `absorb` | method | `topogpt3/inference_hrm.py:714` | `def absorb(self, sample)` |
| `apply` | method | `topogpt3/inference_hrm.py:653` | `def apply(self)` |
| `apply_if_enabled` | method | `topogpt3/inference_hrm.py:593` | `def apply_if_enabled(self)` |
| `assemble` | method | `topogpt3/inference_hrm.py:612` | `def assemble(self, aligned_cfg, paths)` |
| `assert_ready` | method | `topogpt3/inference_hrm.py:446` | `def assert_ready(self)` |
| `build` | method | `topogpt3/inference_hrm.py:347` | `def build(settings)` |
| `build` | method | `topogpt3/inference_hrm.py:521` | `def build(self, n_kv_heads, vocab_size)` |
| `build` | method | `topogpt3/inference_hrm.py:577` | `def build(self)` |
| `build_parser` | method | `topogpt3/inference_hrm.py:1406` | `def build_parser()` |
| `commit` | method | `topogpt3/inference_hrm.py:761` | `def commit(self, new_state)` |
| `detect_n_kv_heads` | method | `topogpt3/inference_hrm.py:471` | `def detect_n_kv_heads(self, weights_path, d_model, n_heads)` |
| `execute` | method | `topogpt3/inference_hrm.py:1346` | `def execute(self)` |
| `from_settings` | method | `topogpt3/inference_hrm.py:1054` | `def from_settings(cls, settings)` |
| `get_or_init` | method | `topogpt3/inference_hrm.py:743` | `def get_or_init(self, reference)` |
| `invalidate` | method | `topogpt3/inference_hrm.py:766` | `def invalidate(self)` |
| `load` | method | `topogpt3/inference_hrm.py:405` | `def load(self)` |
| `main` | function | `topogpt3/inference_hrm.py:1657` | `def main(argv)` |
| `model_file` | method | `topogpt3/inference_hrm.py:432` | `def model_file(self)` |
| `num_layers` | method | `topogpt3/inference_hrm.py:837` | `def num_layers(self)` |
| `parse` | method | `topogpt3/inference_hrm.py:1611` | `def parse(argv)` |
| `preset` | method | `topogpt3/inference_hrm.py:234` | `def preset(self)` |
| `reason` | method | `topogpt3/inference_hrm.py:884` | `def reason(self, z_initial, base_kvs, cached_refinement, position_offset)` |
| `relative_change` | method | `topogpt3/inference_hrm.py:676` | `def relative_change(self, current, previous)` |
| `render` | method | `topogpt3/inference_hrm.py:1296` | `def render(self, report)` |
| `require_existing_file` | method | `topogpt3/inference_hrm.py:385` | `def require_existing_file(path, expected_suffix)` |
| `resolve_under` | method | `topogpt3/inference_hrm.py:369` | `def resolve_under(root)` |
| `run` | method | `topogpt3/inference_hrm.py:1128` | `def run(self, model, tokenizer, prompt, policy)` |
| `sample` | method | `topogpt3/inference_hrm.py:1016` | `def sample(self, logits, token_history, temperature, top_k, repetition_penalty)` |
| `scale_presets` | method | `topogpt3/inference_hrm.py:223` | `def scale_presets()` |
| `slot_dir` | method | `topogpt3/inference_hrm.py:428` | `def slot_dir(self)` |
| `state_file` | method | `topogpt3/inference_hrm.py:439` | `def state_file(self)` |
| `tokens_per_second` | method | `topogpt3/inference_hrm.py:1076` | `def tokens_per_second(self, elapsed_floor)` |
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
| `_atomic_save` | function | `topogpt3/jlens.py:283` | `def _atomic_save(obj, path)` |
| `_check_layer_indices` | function | `topogpt3/jlens.py:162` | `def _check_layer_indices(source_layers, target_layer, n_layers)` |
| `_demo_jlens` | function | `topogpt3/jlens.py:842` | `def _demo_jlens()` |
| `_make_hook` | method | `topogpt3/jlens.py:102` | `def _make_hook(self, index)` |
| `apply` | method | `topogpt3/jlens.py:585` | `def apply(self, model, prompt)` |
| `compute_slice` | function | `topogpt3/jlens.py:705` | `def compute_slice(model, lens, prompt)` |
| `fit` | function | `topogpt3/jlens.py:291` | `def fit(model, prompts)` |
| `from_pretrained` | method | `topogpt3/jlens.py:519` | `def from_pretrained(cls, name_or_path)` |
| `hook` | function | `topogpt3/jlens.py:105` | `def hook(module, inputs, output)` |
| `jacobian_for_prompt` | function | `topogpt3/jlens.py:187` | `def jacobian_for_prompt(model, prompt, source_layers)` |
| `load` | method | `topogpt3/jlens.py:504` | `def load(cls, path)` |
| `merge` | method | `topogpt3/jlens.py:543` | `def merge(cls, lenses)` |
| `save` | method | `topogpt3/jlens.py:489` | `def save(self, path)` |
| `select` | function | `topogpt3/jlens.py:646` | `def select(layer)` |
| `text_slice` | function | `topogpt3/jlens.py:789` | `def text_slice(slice_data, tokenizer, n_cols)` |
| `transport` | method | `topogpt3/jlens.py:574` | `def transport(self, residual, layer)` |
| `valid_position_mask` | function | `topogpt3/jlens.py:132` | `def valid_position_mask(seq_len)` |
| `write_checkpoint` | function | `topogpt3/jlens.py:378` | `def write_checkpoint()` |
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
| `_fwd` | function | `topogpt3/lora.py:66` | `def _fwd(x, _o, _l)` |
| `_is_quaternion_sublayer` | function | `topogpt3/lora.py:29` | `def _is_quaternion_sublayer(name)` |
| `apply_lora` | function | `topogpt3/lora.py:54` | `def apply_lora(model, rank, include_mlp)` |
| `forward` | method | `topogpt3/lora.py:25` | `def forward(self, x)` |
| `freeze_non_lora` | function | `topogpt3/lora.py:80` | `def freeze_non_lora(model)` |
| `load_lora` | function | `topogpt3/lora.py:99` | `def load_lora(model, path, device)` |
| `lora_parameters` | function | `topogpt3/lora.py:73` | `def lora_parameters(model)` |
| `lora_targets` | function | `topogpt3/lora.py:34` | `def lora_targets(model, include_mlp)` |
| `merge_lora` | function | `topogpt3/lora.py:110` | `def merge_lora(model, lora_path, save_path)` |
| `save_lora` | function | `topogpt3/lora.py:88` | `def save_lora(model, path)` |
| `BPETokenizer` | class | `topogpt3/model.py:1471` | `class BPETokenizer` |
| `CheckpointManager` | class | `topogpt3/model.py:2766` | `class CheckpointManager` |
| `CurriculumDataset` | class | `topogpt3/model.py:2223` | `class CurriculumDataset(Dataset)` |
| `CurriculumTrainer` | class | `topogpt3/model.py:2587` | `class CurriculumTrainer` |
| `FileManifest` | class | `topogpt3/model.py:1906` | `class FileManifest` |
| `MappedTokenDataset` | class | `topogpt3/model.py:2075` | `class MappedTokenDataset(Dataset)` |
| `MechanisticMetrics` | class | `topogpt3/model.py:3342` | `class MechanisticMetrics` |
| `MemmapTokenizer` | class | `topogpt3/model.py:1975` | `class MemmapTokenizer` |
| `MultiHeadAttention` | class | `topogpt3/model.py:1045` | `class MultiHeadAttention(Module)` |
| `Phase0_KernelOptimizer` | class | `topogpt3/model.py:3587` | `class Phase0_KernelOptimizer` |
| `Phase1_BatchProspector` | class | `topogpt3/model.py:3667` | `class Phase1_BatchProspector` |
| `Phase2_SeedMiner` | class | `topogpt3/model.py:3758` | `class Phase2_SeedMiner` |
| `Phase4_AnnealingRefiner` | class | `topogpt3/model.py:3855` | `class Phase4_AnnealingRefiner` |
| `ProgressiveSeqLenTrainer` | class | `topogpt3/model.py:2292` | `class ProgressiveSeqLenTrainer` |
| `QuantizedEmbedding` | class | `topogpt3/model.py:2518` | `class QuantizedEmbedding(Module)` |
| `QuaternionLinear` | class | `topogpt3/model.py:324` | `class QuaternionLinear(Module)` |
| `QuaternionOps` | class | `topogpt3/model.py:281` | `class QuaternionOps` |
| `QuaternionSpectralLayer` | class | `topogpt3/model.py:375` | `class QuaternionSpectralLayer(Module)` |
| `QuaternionTorusBrain` | class | `topogpt3/model.py:561` | `class QuaternionTorusBrain(Module)` |
| `RMSNorm` | class | `topogpt3/model.py:885` | `class RMSNorm(Module)` |
| `RotaryEmbedding` | class | `topogpt3/model.py:799` | `class RotaryEmbedding(Module)` |
| `SpectralAutoencoder` | class | `topogpt3/model.py:473` | `class SpectralAutoencoder(Module)` |
| `SpeculativeDecoder` | class | `topogpt3/model.py:2394` | `class SpeculativeDecoder` |
| `SwiGLU` | class | `topogpt3/model.py:903` | `class SwiGLU(Module)` |
| `TextFilter` | class | `topogpt3/model.py:2110` | `class TextFilter` |
| `TopoGPT2` | class | `topogpt3/model.py:1222` | `class TopoGPT2(Module)` |
| `TopoGPT2Config` | class | `topogpt3/model.py:59` | `class TopoGPT2Config` |
| `TopoGPT2Layer` | class | `topogpt3/model.py:1164` | `class TopoGPT2Layer(Module)` |
| `TopoGPT2Trainer` | class | `topogpt3/model.py:3005` | `class TopoGPT2Trainer` |
| `TopoMoEBrain` | class | `topogpt3/model.py:932` | `class TopoMoEBrain(Module)` |
| `TopoPhasePipeline` | class | `topogpt3/model.py:4186` | `class TopoPhasePipeline` |
| `TopoPhasePipelineV2` | class | `topogpt3/model.py:4030` | `class TopoPhasePipelineV2` |
| `__getitem__` | method | `topogpt3/model.py:2092` | `def __getitem__(self, idx)` |
| `__getitem__` | method | `topogpt3/model.py:2256` | `def __getitem__(self, idx)` |
| `__init__` | method | `topogpt3/model.py:336` | `def __init__(self, in_features, out_features, bias)` |
| `__init__` | method | `topogpt3/model.py:395` | `def __init__(self, in_q, out_q, grid_h, grid_w, init_scale)` |
| `__init__` | method | `topogpt3/model.py:486` | `def __init__(self, config)` |
| `__init__` | method | `topogpt3/model.py:579` | `def __init__(self, d_model, config)` |
| `__init__` | method | `topogpt3/model.py:811` | `def __init__(self, d_head, max_seq_len, base, yarn_factor, yarn_orig_max)` |
| `__init__` | method | `topogpt3/model.py:888` | `def __init__(self, d_model, eps)` |
| `__init__` | method | `topogpt3/model.py:910` | `def __init__(self, d_model, expansion, dropout)` |
| `__init__` | method | `topogpt3/model.py:947` | `def __init__(self, d_model, config)` |
| `__init__` | method | `topogpt3/model.py:1055` | `def __init__(self, d_model, n_heads, config)` |
| `__init__` | method | `topogpt3/model.py:1173` | `def __init__(self, d_model, n_heads, config)` |
| `__init__` | method | `topogpt3/model.py:1233` | `def __init__(self, config)` |
| `__init__` | method | `topogpt3/model.py:1474` | `def __init__(self, encoding)` |
| `__init__` | method | `topogpt3/model.py:1909` | `def __init__(self, root, cache_dir, logger)` |
| `__init__` | method | `topogpt3/model.py:1985` | `def __init__(self, cache_dir, logger)` |
| `__init__` | method | `topogpt3/model.py:2084` | `def __init__(self, tokens, seq_len)` |
| `__init__` | method | `topogpt3/model.py:2113` | `def __init__(self, config, logger)` |
| `__init__` | method | `topogpt3/model.py:2230` | `def __init__(self, tokens, seq_len, file_tiers, active_tier, logger)` |
| `__init__` | method | `topogpt3/model.py:2303` | `def __init__(self, base_trainer)` |
| `__init__` | method | `topogpt3/model.py:2403` | `def __init__(self, target_model, config, logger)` |
| `__init__` | method | `topogpt3/model.py:2525` | `def __init__(self, embed, mode)` |
| `__init__` | method | `topogpt3/model.py:2595` | `def __init__(self, model, config, tokenizer)` |
| `__init__` | method | `topogpt3/model.py:2791` | `def __init__(self, config, logger)` |
| `__init__` | method | `topogpt3/model.py:3017` | `def __init__(self, model, config, tokenizer)` |
| `__init__` | method | `topogpt3/model.py:3362` | `def __init__(self, config)` |
| `__init__` | method | `topogpt3/model.py:3605` | `def __init__(self, config, logger)` |
| `__init__` | method | `topogpt3/model.py:3683` | `def __init__(self, config, logger)` |
| `__init__` | method | `topogpt3/model.py:3774` | `def __init__(self, config, logger)` |
| `__init__` | method | `topogpt3/model.py:3875` | `def __init__(self, trainer, t0, cooling_rate, stagnation_patience)` |
| `__init__` | method | `topogpt3/model.py:4041` | `def __init__(self, config, train_tokens, val_tokens, tokenizer, logger, curriculum_tiers, progressive_seq)` |
| `__init__` | method | `topogpt3/model.py:4206` | `def __init__(self, config, train_dataset, val_dataset, tokenizer, logger)` |
| `__len__` | method | `topogpt3/model.py:2089` | `def __len__(self)` |
| `__len__` | method | `topogpt3/model.py:2253` | `def __len__(self)` |
| `__post_init__` | method | `topogpt3/model.py:170` | `def __post_init__(self)` |
| `_build_cache` | method | `topogpt3/model.py:847` | `def _build_cache(self, seq_len)` |
| `_build_dataloader` | method | `topogpt3/model.py:2309` | `def _build_dataloader(self, dataset, seq_len, batch_size, is_train)` |
| `_build_dataloader` | method | `topogpt3/model.py:4059` | `def _build_dataloader(self, tokens, seq_len, batch_size, shuffle, tag)` |
| `_build_draft` | method | `topogpt3/model.py:2412` | `def _build_draft(self)` |
| `_build_phases` | method | `topogpt3/model.py:4084` | `def _build_phases(self)` |
| `_build_torus_graph` | method | `topogpt3/model.py:619` | `def _build_torus_graph(self)` |
| `_compute_entropy` | method | `topogpt3/model.py:2127` | `def _compute_entropy(self, text)` |
| `_content_hash` | method | `topogpt3/model.py:2162` | `def _content_hash(self, text)` |
| `_contract` | method | `topogpt3/model.py:422` | `def _contract(self, W, X)` |
| `_cosine_lr` | method | `topogpt3/model.py:2659` | `def _cosine_lr(self)` |
| `_cosine_lr` | method | `topogpt3/model.py:3102` | `def _cosine_lr(self, step_in_session, total_steps_session)` |
| `_current_state` | method | `topogpt3/model.py:2656` | `def _current_state(self)` |
| `_current_state` | method | `topogpt3/model.py:3091` | `def _current_state(self)` |
| `_filter1d` | method | `topogpt3/model.py:520` | `def _filter1d(self, x, kr, ki)` |
| `_forward_impl` | method | `topogpt3/model.py:1182` | `def _forward_impl(self, x, past_kv, position_offset)` |
| `_has_long_lines` | method | `topogpt3/model.py:2142` | `def _has_long_lines(self, text, threshold)` |
| `_init_weights` | method | `topogpt3/model.py:1260` | `def _init_weights(self)` |
| `_kernel` | method | `topogpt3/model.py:419` | `def _kernel(self, c)` |
| `_load_model` | method | `topogpt3/model.py:2843` | `def _load_model(self, model, directory)` |
| `_load_optimizer` | method | `topogpt3/model.py:2879` | `def _load_optimizer(self, optimizer, directory, device)` |
| `_load_state` | method | `topogpt3/model.py:2893` | `def _load_state(self, directory)` |
| `_make_dataloaders` | method | `topogpt3/model.py:4220` | `def _make_dataloaders(self, batch_size)` |
| `_measure_ratio` | method | `topogpt3/model.py:3609` | `def _measure_ratio(self, ratio, sample_batch)` |
| `_message_passing` | method | `topogpt3/model.py:698` | `def _message_passing(self, node_feat)` |
| `_progressive_train` | method | `topogpt3/model.py:2671` | `def _progressive_train(self, train_paths, val_paths, tokenizer, phases, memtok)` |
| `_rotate_half` | method | `topogpt3/model.py:855` | `def _rotate_half(self, x)` |
| `_route` | method | `topogpt3/model.py:970` | `def _route(self, x)` |
| `_sample_text` | method | `topogpt3/model.py:2668` | `def _sample_text(self)` |
| `_sample_text` | method | `topogpt3/model.py:3270` | `def _sample_text(self, tokenizer, prompts, max_new, temperature, top_k)` |
| `_save_model` | method | `topogpt3/model.py:2830` | `def _save_model(self, model, directory)` |
| `_save_optimizer` | method | `topogpt3/model.py:2876` | `def _save_optimizer(self, optimizer, directory)` |
| `_save_state` | method | `topogpt3/model.py:2888` | `def _save_state(self, state, directory)` |
| `_set_lr` | method | `topogpt3/model.py:2662` | `def _set_lr(self)` |
| `_set_lr` | method | `topogpt3/model.py:3110` | `def _set_lr(self, lr)` |
| `_special_token_ratio` | method | `topogpt3/model.py:2149` | `def _special_token_ratio(self, text, tokenizer)` |
| `_tokenize_text_to_memmap` | function | `topogpt3/model.py:2752` | `def _tokenize_text_to_memmap(text, tokenizer, path, max_tokens)` |
| `_torus_soft_assign` | method | `topogpt3/model.py:661` | `def _torus_soft_assign(self, phi1, phi2)` |
| `_update_len` | method | `topogpt3/model.py:2244` | `def _update_len(self)` |
| `amp_dtype` | method | `topogpt3/model.py:2618` | `def amp_dtype(self)` |
| `apply_quantization` | function | `topogpt3/model.py:2558` | `def apply_quantization(model, config)` |
| `best_val_loss` | method | `topogpt3/model.py:2638` | `def best_val_loss(self)` |
| `best_val_loss` | method | `topogpt3/model.py:2642` | `def best_val_loss(self, v)` |
| `build_file_tiers` | function | `topogpt3/model.py:2265` | `def build_file_tiers(paths, short, med)` |
| `cache_tokens` | method | `topogpt3/model.py:2602` | `def cache_tokens(self, key, tokens)` |
| `ckpt_fn` | function | `topogpt3/model.py:1208` | `def ckpt_fn(x_in)` |
| `ckpt_mgr` | method | `topogpt3/model.py:2650` | `def ckpt_mgr(self)` |
| `classify_phase` | method | `topogpt3/model.py:3518` | `def classify_phase(self, delta, kappa, berry)` |
| `completed_epochs` | method | `topogpt3/model.py:2622` | `def completed_epochs(self)` |
| `completed_epochs` | method | `topogpt3/model.py:2626` | `def completed_epochs(self, v)` |
| `compute_all` | method | `topogpt3/model.py:3536` | `def compute_all(self, model, lr, dataloader, compute_kappa)` |
| `compute_alpha` | method | `topogpt3/model.py:3378` | `def compute_alpha(self, delta)` |
| `compute_berry_phase` | method | `topogpt3/model.py:3475` | `def compute_berry_phase(self, model)` |
| `compute_delta` | method | `topogpt3/model.py:3371` | `def compute_delta(self, model)` |
| `compute_kappa` | method | `topogpt3/model.py:3417` | `def compute_kappa(self, model, dataloader, n_batches)` |
| `compute_lc` | method | `topogpt3/model.py:3488` | `def compute_lc(self, model)` |
| `compute_sp` | method | `topogpt3/model.py:3502` | `def compute_sp(self, model)` |
| `compute_t_eff` | method | `topogpt3/model.py:3409` | `def compute_t_eff(self, lr)` |
| `conjugate` | method | `topogpt3/model.py:308` | `def conjugate(q)` |
| `count_params` | method | `topogpt3/model.py:1343` | `def count_params(self)` |
| `decode` | method | `topogpt3/model.py:533` | `def decode(self, z)` |
| `decode` | method | `topogpt3/model.py:1486` | `def decode(self, tokens)` |
| `enable_yarn` | method | `topogpt3/model.py:837` | `def enable_yarn(self, factor, orig_max)` |
| `encode` | method | `topogpt3/model.py:528` | `def encode(self, x)` |
| `encode` | method | `topogpt3/model.py:1483` | `def encode(self, text)` |
| `eot_token` | method | `topogpt3/model.py:1489` | `def eot_token(self)` |
| `evaluate` | method | `topogpt3/model.py:2665` | `def evaluate(self, dataloader)` |
| `evaluate` | method | `topogpt3/model.py:3308` | `def evaluate(self, dataloader)` |
| `filter_file` | method | `topogpt3/model.py:2165` | `def filter_file(self, path, tokenizer)` |
| `format_log` | method | `topogpt3/model.py:3568` | `def format_log(self, m)` |
| `forward` | method | `topogpt3/model.py:352` | `def forward(self, x)` |
| `forward` | method | `topogpt3/model.py:426` | `def forward(self, x)` |
| `forward` | method | `topogpt3/model.py:538` | `def forward(self, x)` |
| `forward` | method | `topogpt3/model.py:735` | `def forward(self, x)` |
| `forward` | method | `topogpt3/model.py:859` | `def forward(self, q, k, seq_len, offset)` |
| `forward` | method | `topogpt3/model.py:893` | `def forward(self, x)` |
| `forward` | method | `topogpt3/model.py:923` | `def forward(self, x)` |
| `forward` | method | `topogpt3/model.py:1018` | `def forward(self, x)` |
| `forward` | method | `topogpt3/model.py:1074` | `def forward(self, x, is_causal, past_kv, position_offset)` |
| `forward` | method | `topogpt3/model.py:1196` | `def forward(self, x, past_kv, position_offset)` |
| `forward` | method | `topogpt3/model.py:1267` | `def forward(self, token_ids, past_kvs, position_offset)` |
| `forward` | method | `topogpt3/model.py:2554` | `def forward(self, indices)` |
| `forward_with_memory` | method | `topogpt3/model.py:1293` | `def forward_with_memory(self, token_ids)` |
| `generate` | method | `topogpt3/model.py:1349` | `def generate(self, token_ids, max_new_tokens, temperature, top_k, repetition_penalty)` |
| `generate` | method | `topogpt3/model.py:2427` | `def generate(self, token_ids, max_new_tokens, temperature, top_k, repetition_penalty)` |
| `generate_with_continuation` | method | `topogpt3/model.py:1409` | `def generate_with_continuation(self, token_ids, tokenizer, max_new_tokens, temperature, top_k, repetition_penalty...` |
| `global_step` | method | `topogpt3/model.py:2630` | `def global_step(self)` |
| `global_step` | method | `topogpt3/model.py:2634` | `def global_step(self, v)` |
| `hamilton_product` | method | `topogpt3/model.py:289` | `def hamilton_product(q1, q2)` |
| `has_checkpoint` | method | `topogpt3/model.py:2996` | `def has_checkpoint(self)` |
| `history` | method | `topogpt3/model.py:2646` | `def history(self)` |
| `load_best` | method | `topogpt3/model.py:2982` | `def load_best(self, model)` |
| `load_latest` | method | `topogpt3/model.py:2955` | `def load_latest(self, model, optimizer)` |
| `main` | function | `topogpt3/model.py:4330` | `def main()` |
| `mine` | method | `topogpt3/model.py:3778` | `def mine(self, seed_start, n_seeds, train_dataset, prospect_steps)` |
| `model` | method | `topogpt3/model.py:2606` | `def model(self)` |
| `normalize` | method | `topogpt3/model.py:304` | `def normalize(q, eps)` |
| `optimize` | method | `topogpt3/model.py:3640` | `def optimize(self, dataloader)` |
| `optimizer` | method | `topogpt3/model.py:2610` | `def optimizer(self)` |
| `patch_config_for_resume` | method | `topogpt3/model.py:2801` | `def patch_config_for_resume(self, cfg)` |
| `process_torus_grid` | method | `topogpt3/model.py:545` | `def process_torus_grid(self, grid)` |
| `prospect` | method | `topogpt3/model.py:3687` | `def prospect(self, candidates, train_dataset, prospect_steps)` |
| `refine` | method | `topogpt3/model.py:3888` | `def refine(self, train_dl, val_dl, refine_epochs)` |
| `report` | method | `topogpt3/model.py:2207` | `def report(self)` |
| `resume` | method | `topogpt3/model.py:2653` | `def resume(self)` |
| `resume` | method | `topogpt3/model.py:3066` | `def resume(self)` |
| `rotate_vector` | method | `topogpt3/model.py:313` | `def rotate_vector(v, q)` |
| `run` | method | `topogpt3/model.py:2324` | `def run(self, train_paths, val_paths, tokenizer, file_tiers, phases)` |
| `run` | method | `topogpt3/model.py:4095` | `def run(self, run_prospect, refine_epochs, resume, prospect_steps, probe_seeds, seed_start)` |
| `run` | method | `topogpt3/model.py:4242` | `def run(self, run_prospect, refine_epochs, resume, prospect_steps, probe_seeds, seed_start)` |
| `run_curriculum` | method | `topogpt3/model.py:2728` | `def run_curriculum(self, train_paths, val_paths, tokenizer, phases)` |
| `save` | method | `topogpt3/model.py:2907` | `def save(self, model, optimizer, state, is_best)` |
| `scaler` | method | `topogpt3/model.py:2614` | `def scaler(self)` |
| `scan` | method | `topogpt3/model.py:1916` | `def scan(self, force)` |
| `set_seed` | function | `topogpt3/model.py:268` | `def set_seed(seed, device)` |
| `set_tier` | method | `topogpt3/model.py:2249` | `def set_tier(self, tier)` |
| `setup_logger` | function | `topogpt3/model.py:256` | `def setup_logger(name, level)` |
| `should_save` | method | `topogpt3/model.py:2904` | `def should_save(self)` |
| `tokenize` | method | `topogpt3/model.py:1990` | `def tokenize(self, file_paths, tokenizer, cache_key, max_tokens, min_chars)` |
| `train` | method | `topogpt3/model.py:2725` | `def train(self, train_dl, val_dl)` |
| `train` | method | `topogpt3/model.py:3114` | `def train(self, train_dl, val_dl)` |
| `update_grad_buffer` | method | `topogpt3/model.py:3383` | `def update_grad_buffer(self, model)` |
| `base_rewards` | function | `topogpt3/rewards.py:25` | `def base_rewards(prompts, completions, reward_fn, device)` |
| `distillation_loss` | function | `topogpt3/rewards.py:122` | `def distillation_loss(student_logits, teacher_logits, mask, labels, alpha, temp)` |
| `dpo_loss_fn` | function | `topogpt3/rewards.py:113` | `def dpo_loss_fn(ref_lp, pol_lp, mask, beta)` |
| `execution_reward` | function | `topogpt3/rewards.py:202` | `def execution_reward(results)` |
| `grpo_advantages` | function | `topogpt3/rewards.py:70` | `def grpo_advantages(rewards, num_generations)` |
| `grpo_loss` | function | `topogpt3/rewards.py:82` | `def grpo_loss(new_logp, old_logp, ref_logp, adv, mask, beta, eps, loss_type, eps_high)` |
| `k3_kl` | function | `topogpt3/rewards.py:77` | `def k3_kl(ref_logp, new_logp)` |
| `logits_to_log_probs` | function | `topogpt3/rewards.py:107` | `def logits_to_log_probs(logits, labels)` |
| `rep_penalty` | function | `topogpt3/rewards.py:17` | `def rep_penalty(text, n, cap)` |
| `spectral_bonus` | function | `topogpt3/rewards.py:55` | `def spectral_bonus(fisher_gap, drift, w_fisher, w_drift)` |
| `tool_call_reward` | function | `topogpt3/rewards.py:151` | `def tool_call_reward(text, allowed_tools, require_tool)` |
| `verifier_reward` | function | `topogpt3/rewards.py:176` | `def verifier_reward(text, mode)` |
| `RolloutEngine` | class | `topogpt3/rollout.py:39` | `class RolloutEngine(ABC)` |
| `RolloutResult` | class | `topogpt3/rollout.py:18` | `class RolloutResult` |
| `TorchRolloutEngine` | class | `topogpt3/rollout.py:50` | `class TorchRolloutEngine(RolloutEngine)` |
| `__init__` | method | `topogpt3/rollout.py:51` | `def __init__(self, policy_model, tokenizer, device, decode)` |
| `compute_per_token_logps` | function | `topogpt3/rollout.py:27` | `def compute_per_token_logps(model, input_ids, n_keep)` |
| `create_rollout_engine` | function | `topogpt3/rollout.py:83` | `def create_rollout_engine(policy_model, tokenizer, device)` |
| `rollout` | method | `topogpt3/rollout.py:41` | `def rollout(self, prompt_ids, num_generations, max_new_tokens, temperature, tokenizer)` |
| `rollout` | method | `topogpt3/rollout.py:57` | `def rollout(self, prompt_ids, num_generations, max_new_tokens, temperature, tokenizer)` |
| `update_policy` | method | `topogpt3/rollout.py:46` | `def update_policy(self, model)` |
| `update_policy` | method | `topogpt3/rollout.py:79` | `def update_policy(self, model)` |
| `GrammarConstraint` | class | `topogpt3/structured_output.py:182` | `class GrammarConstraint` |
| `GrammarSpec` | class | `topogpt3/structured_output.py:32` | `class GrammarSpec` |
| `StructuredOutputError` | class | `topogpt3/structured_output.py:27` | `class StructuredOutputError(ValueError)` |
| `__init__` | method | `topogpt3/structured_output.py:185` | `def __init__(self, xg, compiled, vocab_size)` |
| `_compile` | function | `topogpt3/structured_output.py:162` | `def _compile(spec, compiler)` |
| `_get_compiler` | function | `topogpt3/structured_output.py:139` | `def _get_compiler(tokenizer)` |
| `_import_xgrammar` | function | `topogpt3/structured_output.py:46` | `def _import_xgrammar()` |
| `_new_matcher` | method | `topogpt3/structured_output.py:192` | `def _new_matcher(self)` |
| `_tokenizer_key` | function | `topogpt3/structured_output.py:132` | `def _tokenizer_key(tokenizer)` |
| `accept` | method | `topogpt3/structured_output.py:211` | `def accept(self, token_id)` |
| `apply` | method | `topogpt3/structured_output.py:204` | `def apply(self, logits)` |
| `build_constraint` | function | `topogpt3/structured_output.py:218` | `def build_constraint(tokenizer, spec)` |
| `cache_key` | method | `topogpt3/structured_output.py:36` | `def cache_key(self)` |
| `constraint_from_request` | function | `topogpt3/structured_output.py:240` | `def constraint_from_request(tokenizer, response_format, so_args)` |
| `is_terminated` | method | `topogpt3/structured_output.py:201` | `def is_terminated(self)` |
| `parse_response_format` | function | `topogpt3/structured_output.py:56` | `def parse_response_format(response_format)` |
| `parse_so_args` | function | `topogpt3/structured_output.py:93` | `def parse_so_args(so_args)` |
| `reset` | method | `topogpt3/structured_output.py:197` | `def reset(self)` |
| `ArtifactTokenizer` | class | `topogpt3/tokenizer_tools.py:116` | `class ArtifactTokenizer` |
| `__init__` | method | `topogpt3/tokenizer_tools.py:119` | `def __init__(self)` |
| `audit` | function | `topogpt3/tokenizer_tools.py:27` | `def audit(checkpoint_dir, corpus_files, sample_chars)` |
| `decode` | method | `topogpt3/tokenizer_tools.py:126` | `def decode(self, tokens)` |
| `encode` | method | `topogpt3/tokenizer_tools.py:123` | `def encode(self, text)` |

Next: [SYMBOLS_p3.md](SYMBOLS_p3.md)
