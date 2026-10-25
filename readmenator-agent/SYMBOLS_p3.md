# Symbols (page 3 of 3)
Previous: [SYMBOLS_p2.md](SYMBOLS_p2.md)

| Symbol | Kind | File:Line | Signature |
|--------|------|-----------|-----------|
| `eot_token` | method | `topogpt3/tokenizer_tools.py:129` | `def eot_token(self)` |
| `load_tokenizer_artifact` | function | `topogpt3/tokenizer_tools.py:110` | `def load_tokenizer_artifact(path)` |
| `main` | function | `topogpt3/tokenizer_tools.py:183` | `def main()` |
| `resize_embeddings` | function | `topogpt3/tokenizer_tools.py:135` | `def resize_embeddings(checkpoint_dir, new_vocab, out_dir)` |
| `train_code_bpe` | function | `topogpt3/tokenizer_tools.py:76` | `def train_code_bpe(corpus_files, out_dir, vocab_size)` |
| `_apt_chain_preview` | function | `topogpt3/tools_agent.py:55` | `def _apt_chain_preview(args)` |
| `execute_tool` | function | `topogpt3/tools_agent.py:96` | `def execute_tool(name, args)` |
| `rollout_multiturn` | function | `topogpt3/tools_agent.py:117` | `def rollout_multiturn(generate_fn, tokenizer, messages, tools, max_turns, max_new_tokens, open_thinking)` |
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
| `_gauss_complex_contract` | function | `topogpt3/train.py:532` | `def _gauss_complex_contract(self, W, X)` |
| `_get_formatter` | method | `topogpt3/train.py:797` | `def _get_formatter(cls, tier)` |
| `_load_hf_with_fallback` | method | `topogpt3/train.py:858` | `def _load_hf_with_fallback(self, tier)` |
| `_manifest_path` | method | `topogpt3/train.py:825` | `def _manifest_path(self, tier)` |
| `_project_unitary` | method | `topogpt3/train.py:381` | `def _project_unitary(M)` |
| `_set_lr` | method | `topogpt3/train.py:1229` | `def _set_lr(self, lr)` |
| `_stack_spectral_kernels` | method | `topogpt3/train.py:231` | `def _stack_spectral_kernels(model)` |
| `_state_dict` | method | `topogpt3/train.py:1436` | `def _state_dict(self)` |
| `_tier_paths` | method | `topogpt3/train.py:819` | `def _tier_paths(self, tier)` |
| `_train_one_tier` | method | `topogpt3/train.py:1237` | `def _train_one_tier(self, tier_index)` |
| `apply_gauss_patch` | function | `topogpt3/train.py:568` | `def apply_gauss_patch(logger)` |
| `build_topogpt2_config` | method | `topogpt3/train.py:170` | `def build_topogpt2_config(self, max_seq_len, attn_window)` |
| `compute` | method | `topogpt3/train.py:664` | `def compute(self, dataloader, vocab_size, val_loss, val_ppl, val_acc, batch_size, seq_len)` |
| `conjugation_distance_su2` | method | `topogpt3/train.py:412` | `def conjugation_distance_su2(U1, U2)` |
| `estimate_bytes_per_step` | method | `topogpt3/train.py:656` | `def estimate_bytes_per_step(self, batch_size, seq_len, dtype_bytes)` |
| `estimate_fisher_gap` | method | `topogpt3/train.py:313` | `def estimate_fisher_gap(self, model, dataloader, vocab_size, r_target)` |
| `estimate_flops_per_step` | method | `topogpt3/train.py:651` | `def estimate_flops_per_step(self, batch_size, seq_len)` |
| `flush` | function | `topogpt3/train.py:922` | `def flush(split)` |
| `format_log` | method | `topogpt3/train.py:500` | `def format_log(self, snap)` |
| `format_log` | method | `topogpt3/train.py:696` | `def format_log(self, m)` |
| `load_latest` | method | `topogpt3/train.py:1071` | `def load_latest(self, model, optimizer)` |
| `main` | function | `topogpt3/train.py:1567` | `def main()` |
| `measure_throughput` | method | `topogpt3/train.py:619` | `def measure_throughput(self, dataloader, vocab_size)` |
| `open_memmap` | method | `topogpt3/train.py:986` | `def open_memmap(self, tier, split)` |
| `parse_args` | function | `topogpt3/train.py:1538` | `def parse_args()` |
| `prepare_all` | method | `topogpt3/train.py:1174` | `def prepare_all(self, force)` |
| `prepare_tier` | method | `topogpt3/train.py:891` | `def prepare_tier(self, tier_index, force)` |
| `run` | method | `topogpt3/train.py:1449` | `def run(self)` |
| `save` | method | `topogpt3/train.py:522` | `def save(self, path)` |
| `save` | method | `topogpt3/train.py:1037` | `def save(self, tag, model, optimizer, state)` |
| `should_save` | method | `topogpt3/train.py:1095` | `def should_save(self, interval_min)` |
| `snapshot` | method | `topogpt3/train.py:445` | `def snapshot(self, model, step, dataloader, vocab_size)` |
| `update_holonomy` | method | `topogpt3/train.py:386` | `def update_holonomy(self, U_new)` |
| `agent_reward` | function | `topogpt3/train_agent.py:41` | `def agent_reward(text, gt, used_tools, tool_results, allowed_tools, require_tool, verifier)` |
| `main` | function | `topogpt3/train_agent.py:67` | `def main()` |
| `main` | function | `topogpt3/train_distill.py:27` | `def main()` |
| `load_model` | function | `topogpt3/train_dpo.py:31` | `def load_model(checkpoint, device)` |
| `main` | function | `topogpt3/train_dpo.py:43` | `def main()` |
| `_gather` | function | `topogpt3/train_grpo.py:105` | `def _gather(lg, _plen, _R, _comp)` |
| `main` | function | `topogpt3/train_grpo.py:32` | `def main()` |
| `load_base` | function | `topogpt3/train_lora.py:32` | `def load_base(checkpoint, device)` |
| `main` | function | `topogpt3/train_lora.py:46` | `def main()` |
| `TopoCritic` | class | `topogpt3/train_ppo.py:31` | `class TopoCritic(Module)` |
| `__init__` | method | `topogpt3/train_ppo.py:32` | `def __init__(self, trunk)` |
| `forward` | method | `topogpt3/train_ppo.py:38` | `def forward(self, ids)` |
| `main` | function | `topogpt3/train_ppo.py:47` | `def main()` |
| `Logger` | function | `topogpt3/trainer_utils_topo.py:20` | `def Logger(content, quiet)` |
| `SkipBatchSampler` | class | `topogpt3/trainer_utils_topo.py:52` | `class SkipBatchSampler(Sampler)` |
| `__init__` | method | `topogpt3/trainer_utils_topo.py:53` | `def __init__(self, sampler, batch_size, skip_batches)` |
| `__iter__` | method | `topogpt3/trainer_utils_topo.py:58` | `def __iter__(self)` |
| `__len__` | method | `topogpt3/trainer_utils_topo.py:72` | `def __len__(self)` |
| `get_lr` | function | `topogpt3/trainer_utils_topo.py:29` | `def get_lr(current_step, total_steps, lr)` |
| `init_distributed_mode` | function | `topogpt3/trainer_utils_topo.py:43` | `def init_distributed_mode()` |
| `is_main_process` | function | `topogpt3/trainer_utils_topo.py:25` | `def is_main_process()` |
| `setup_seed` | function | `topogpt3/trainer_utils_topo.py:34` | `def setup_seed(seed)` |
| `topo_checkpoint` | function | `topogpt3/trainer_utils_topo.py:77` | `def topo_checkpoint(save_dir, weight, model, optimizer, scheduler, scaler, epoch, step, wandb, extra)` |
| `YaRNConfig` | class | `topogpt3/yarn.py:18` | `class YaRNConfig` |
| `apply_yarn_to_rope` | function | `topogpt3/yarn.py:50` | `def apply_yarn_to_rope(rope_module, cfg)` |
| `yarn_scale_inv_freq` | function | `topogpt3/yarn.py:26` | `def yarn_scale_inv_freq(inv_freq, d_head, cfg)` |

