# API (page 2 of 2)
Previous: [API.md](API.md)

## topogpt3/lens_model.py
Depends on: `topogpt3/model.py`
Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/jlens.py`
- `LensModel.encode` (method) `topogpt3/lens_model.py:40` `def encode(self, text)` -- Tokenize ``text`` to ``input_ids`` of shape ``[1, seq_len]`` on the model's input device.
- `LensModel.forward` (method) `topogpt3/lens_model.py:45` `def forward(self, input_ids)` -- Run the residual stack on ``input_ids`` (no LM head).
- `LensModel.unembed` (method) `topogpt3/lens_model.py:52` `def unembed(self, residual)` -- Map a residual-stream tensor ``[..., d_model]`` to logits ``[..., vocab_size]`` (final norm + LM head).
- `TopoGPT3LensConfig.from_topogpt2_config` (method) `topogpt3/lens_model.py:84` `def from_topogpt2_config(cls, cfg)` -- Construct a lens config from a TopoGPT2Config dataclass.
- `TopoGPT3LensConfig.probe_checkpoint` (method) `topogpt3/lens_model.py:104` `def probe_checkpoint(cls, checkpoint_dir)` -- Probe a checkpoint directory and infer lens config from state.json.
- `_TopoGPT3ResidualForward.__init__` (method) `topogpt3/lens_model.py:150` `def __init__(self, model)`
- `_TopoGPT3ResidualForward.forward` (method) `topogpt3/lens_model.py:154` `def forward(self, input_ids)`
- `TopoGPT3LensModel.__init__` (method) `topogpt3/lens_model.py:172` `def __init__(self, model, tokenizer)`
- `TopoGPT3LensModel.n_layers` (method) `topogpt3/lens_model.py:184` `def n_layers(self)`
- `TopoGPT3LensModel.d_model` (method) `topogpt3/lens_model.py:188` `def d_model(self)`
- `TopoGPT3LensModel.layers` (method) `topogpt3/lens_model.py:192` `def layers(self)`
- `TopoGPT3LensModel.tokenizer` (method) `topogpt3/lens_model.py:196` `def tokenizer(self)`
- `TopoGPT3LensModel.tokenizer` (method) `topogpt3/lens_model.py:200` `def tokenizer(self, tok)`
- `TopoGPT3LensModel.input_device` (method) `topogpt3/lens_model.py:204` `def input_device(self)`
- `TopoGPT3LensModel.input_device` (method) `topogpt3/lens_model.py:210` `def input_device(self, device)`
- `TopoGPT3LensModel.encode` (method) `topogpt3/lens_model.py:213` `def encode(self, text)` -- Tokenize text to input_ids of shape ``[1, seq_len]``.
- `TopoGPT3LensModel.forward` (method) `topogpt3/lens_model.py:228` `def forward(self, input_ids)` -- Run the residual stack on ``input_ids``.
- `TopoGPT3LensModel.unembed` (method) `topogpt3/lens_model.py:237` `def unembed(self, residual)` -- Map residual ``[..., d_model]`` to logits ``[..., vocab_size]``.
- `TopoGPT3LensModel.from_checkpoint` (method) `topogpt3/lens_model.py:246` `def from_checkpoint(cls, checkpoint_dir)` -- Build a TopoGPT3LensModel from a checkpoint directory.
- `TinyDecoder.__init__` (method) `topogpt3/lens_model.py:315` `def __init__(self, n_layers, d_model, vocab_size, seed)`
- `TinyDecoder.forward` (method) `topogpt3/lens_model.py:344` `def forward(self, token_ids, past_kvs)`
- `_ResidualBlock.__init__` (method) `topogpt3/lens_model.py:360` `def __init__(self, d_model)`
- `_ResidualBlock.forward` (method) `topogpt3/lens_model.py:366` `def forward(self, x, past_kv)`

## topogpt3/lora.py
Imported by: `tests/test_heritage.py`, `topogpt3/__init__.py`, `topogpt3/convert.py`, `topogpt3/train_lora.py`
- `LoRA.__init__` (method) `topogpt3/lora.py:17` `def __init__(self, in_features, out_features, rank)`
- `LoRA.forward` (method) `topogpt3/lora.py:25` `def forward(self, x)`
- `lora_targets` (function) `topogpt3/lora.py:34` `def lora_targets(model, include_mlp)` -- Yield (name, nn.Linear) candidates.
- `apply_lora` (function) `topogpt3/lora.py:54` `def apply_lora(model, rank, include_mlp)` -- Monkey-patch target linears with additive LoRA.
- `lora_parameters` (function) `topogpt3/lora.py:73` `def lora_parameters(model)`
- `freeze_non_lora` (function) `topogpt3/lora.py:80` `def freeze_non_lora(model)`
- `save_lora` (function) `topogpt3/lora.py:88` `def save_lora(model, path)`
- `load_lora` (function) `topogpt3/lora.py:99` `def load_lora(model, path, device)`
- `merge_lora` (function) `topogpt3/lora.py:110` `def merge_lora(model, lora_path, save_path)` -- Merge LoRA deltas into base weights and save (fp16, no .lora. keys).

## topogpt3/model.py
Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `eval/tasks.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `tests/test_structured_output.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/checkpoint_meta.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`
- `setup_logger` (function) `topogpt3/model.py:256` `def setup_logger(name, level)`
- `set_seed` (function) `topogpt3/model.py:268` `def set_seed(seed, device)`
- `QuaternionOps.hamilton_product` (method) `topogpt3/model.py:289` `def hamilton_product(q1, q2)` -- Producto de Hamilton q1 ⊗ q2.
- `QuaternionOps.normalize` (method) `topogpt3/model.py:304` `def normalize(q, eps)`
- `QuaternionOps.conjugate` (method) `topogpt3/model.py:308` `def conjugate(q)`
- `QuaternionOps.rotate_vector` (method) `topogpt3/model.py:313` `def rotate_vector(v, q)` -- Rota vector 3D v por cuaternión unitario q. v:[...,3] q:[...,4]
- `QuaternionLinear.__init__` (method) `topogpt3/model.py:336` `def __init__(self, in_features, out_features, bias)`
- `QuaternionLinear.forward` (method) `topogpt3/model.py:352` `def forward(self, x)` -- x: [..., in_features] → [..., out_features]
- `QuaternionSpectralLayer.__init__` (method) `topogpt3/model.py:395` `def __init__(self, in_q, out_q, grid_h, grid_w, init_scale)`
- `QuaternionSpectralLayer.forward` (method) `topogpt3/model.py:426` `def forward(self, x)` -- x: [B, 4*in_q, H, W]  (4 canales cuaterniones sobre grid espacial) → [B, 4*out_q, H, W]
- `SpectralAutoencoder.__init__` (method) `topogpt3/model.py:486` `def __init__(self, config)`
- `SpectralAutoencoder.encode` (method) `topogpt3/model.py:528` `def encode(self, x)` -- x: [..., D_MODEL] → latent: [..., D_LAT]
- `SpectralAutoencoder.decode` (method) `topogpt3/model.py:533` `def decode(self, z)` -- z: [..., D_LAT] → recon: [..., D_MODEL]
- `SpectralAutoencoder.forward` (method) `topogpt3/model.py:538` `def forward(self, x)` -- Devuelve (latent, recon_loss)
- `SpectralAutoencoder.process_torus_grid` (method) `topogpt3/model.py:545` `def process_torus_grid(self, grid)` -- Procesa el grid del toro con QuaternionSpectralLayer. grid: [B, 4*D_QUAT, RADIAL, ANGULAR]  →  [B, 4*D_QUAT, RADIAL...
- `QuaternionTorusBrain.__init__` (method) `topogpt3/model.py:579` `def __init__(self, d_model, config)`
- `QuaternionTorusBrain.forward` (method) `topogpt3/model.py:735` `def forward(self, x)` -- x: [B, S, D_MODEL] → output: [B, S, D_MODEL], recon_loss: scalar
- `RotaryEmbedding.__init__` (method) `topogpt3/model.py:811` `def __init__(self, d_head, max_seq_len, base, yarn_factor, yarn_orig_max)`
- `RotaryEmbedding.enable_yarn` (method) `topogpt3/model.py:837` `def enable_yarn(self, factor, orig_max)` -- Enable YaRN extrapolation post-hoc (rebuilds cache in place).
- `RotaryEmbedding.forward` (method) `topogpt3/model.py:859` `def forward(self, q, k, seq_len, offset)` -- q, k: [B, n_heads, S_q/S_k, d_head] offset: posicion inicial (para KV cache: longitud del cache existente) Aplica...
- `RMSNorm.__init__` (method) `topogpt3/model.py:888` `def __init__(self, d_model, eps)`
- `RMSNorm.forward` (method) `topogpt3/model.py:893` `def forward(self, x)`
- `SwiGLU.__init__` (method) `topogpt3/model.py:910` `def __init__(self, d_model, expansion, dropout)`
- `SwiGLU.forward` (method) `topogpt3/model.py:923` `def forward(self, x)`
- `TopoMoEBrain.__init__` (method) `topogpt3/model.py:947` `def __init__(self, d_model, config)`
- `TopoMoEBrain.forward` (method) `topogpt3/model.py:1018` `def forward(self, x)` -- → output: [B, S, D], aux_loss: escalar
- `MultiHeadAttention.__init__` (method) `topogpt3/model.py:1055` `def __init__(self, d_model, n_heads, config)`
- `MultiHeadAttention.forward` (method) `topogpt3/model.py:1074` `def forward(self, x, is_causal, past_kv, position_offset)` -- Args: is_causal: usar mascara causal past_kv:  (K_cache, V_cache) de pasos anteriores o None Returns: out:      [B...
- `TopoGPT2Layer.__init__` (method) `topogpt3/model.py:1173` `def __init__(self, d_model, n_heads, config)`
- `TopoGPT2Layer.forward` (method) `topogpt3/model.py:1196` `def forward(self, x, past_kv, position_offset)` -- Retorna (x_out, aux_loss, kv_cache).
- `ckpt_fn` (function) `topogpt3/model.py:1208` `def ckpt_fn(x_in)`
- `TopoGPT2.__init__` (method) `topogpt3/model.py:1233` `def __init__(self, config)`
- `TopoGPT2.forward` (method) `topogpt3/model.py:1267` `def forward(self, token_ids, past_kvs, position_offset)` -- token_ids: [B, S]  (enteros) past_kvs:  lista de (K, V) por capa, o None para entrenamiento → logits: [B, S...
- `TopoGPT2.forward_with_memory` (method) `topogpt3/model.py:1293` `def forward_with_memory(self, token_ids)` -- Process long sequences with latent memory-token context compression.
- `TopoGPT2.count_params` (method) `topogpt3/model.py:1343` `def count_params(self)`
- `TopoGPT2.generate` (method) `topogpt3/model.py:1349` `def generate(self, token_ids, max_new_tokens, temperature, top_k, repetition_penalty)` -- Autoregressive generation with KV cache and top-k sampling.
- `TopoGPT2.generate_with_continuation` (method) `topogpt3/model.py:1409` `def generate_with_continuation(self, token_ids, tokenizer, max_new_tokens, temperature, top_k, repetition_penalty...`
- `BPETokenizer.__init__` (method) `topogpt3/model.py:1474` `def __init__(self, encoding)`
- `BPETokenizer.encode` (method) `topogpt3/model.py:1483` `def encode(self, text)`
- `BPETokenizer.decode` (method) `topogpt3/model.py:1486` `def decode(self, tokens)`
- `BPETokenizer.eot_token` (method) `topogpt3/model.py:1489` `def eot_token(self)`
- `FileManifest.__init__` (method) `topogpt3/model.py:1909` `def __init__(self, root, cache_dir, logger)`
- `FileManifest.scan` (method) `topogpt3/model.py:1916` `def scan(self, force)` -- Walk directory tree collecting text file paths.
- `MemmapTokenizer.__init__` (method) `topogpt3/model.py:1985` `def __init__(self, cache_dir, logger)`
- `MemmapTokenizer.tokenize` (method) `topogpt3/model.py:1990` `def tokenize(self, file_paths, tokenizer, cache_key, max_tokens, min_chars)` -- Tokenize all files and return a memory-mapped numpy array.
- `MappedTokenDataset.__init__` (method) `topogpt3/model.py:2084` `def __init__(self, tokens, seq_len)`
- `TextFilter.__init__` (method) `topogpt3/model.py:2113` `def __init__(self, config, logger)`
- `TextFilter.filter_file` (method) `topogpt3/model.py:2165` `def filter_file(self, path, tokenizer)` -- Read and evaluate a file.
- `TextFilter.report` (method) `topogpt3/model.py:2207` `def report(self)`
- `CurriculumDataset.__init__` (method) `topogpt3/model.py:2230` `def __init__(self, tokens, seq_len, file_tiers, active_tier, logger)`
- `CurriculumDataset.set_tier` (method) `topogpt3/model.py:2249` `def set_tier(self, tier)`
- `build_file_tiers` (function) `topogpt3/model.py:2265` `def build_file_tiers(paths, short, med)` -- Classify file paths into complexity tiers by line count.
- `ProgressiveSeqLenTrainer.__init__` (method) `topogpt3/model.py:2303` `def __init__(self, base_trainer)`
- `ProgressiveSeqLenTrainer.run` (method) `topogpt3/model.py:2324` `def run(self, train_paths, val_paths, tokenizer, file_tiers, phases)` -- Run training with progressive sequence length across phases.
- `SpeculativeDecoder.__init__` (method) `topogpt3/model.py:2403` `def __init__(self, target_model, config, logger)`
- `SpeculativeDecoder.generate` (method) `topogpt3/model.py:2427` `def generate(self, token_ids, max_new_tokens, temperature, top_k, repetition_penalty)` -- Autoregressive generation via speculative decoding.
- `QuantizedEmbedding.__init__` (method) `topogpt3/model.py:2525` `def __init__(self, embed, mode)`
- `QuantizedEmbedding.forward` (method) `topogpt3/model.py:2554` `def forward(self, indices)`
- `apply_quantization` (function) `topogpt3/model.py:2558` `def apply_quantization(model, config)` -- Quantize embedding and lm_head layers for reduced VRAM usage.
- `CurriculumTrainer.__init__` (method) `topogpt3/model.py:2595` `def __init__(self, model, config, tokenizer)`
- `CurriculumTrainer.cache_tokens` (method) `topogpt3/model.py:2602` `def cache_tokens(self, key, tokens)`
- `CurriculumTrainer.model` (method) `topogpt3/model.py:2606` `def model(self)`
- `CurriculumTrainer.optimizer` (method) `topogpt3/model.py:2610` `def optimizer(self)`
- `CurriculumTrainer.scaler` (method) `topogpt3/model.py:2614` `def scaler(self)`
- `CurriculumTrainer.amp_dtype` (method) `topogpt3/model.py:2618` `def amp_dtype(self)`
- `CurriculumTrainer.completed_epochs` (method) `topogpt3/model.py:2622` `def completed_epochs(self)`
- `CurriculumTrainer.completed_epochs` (method) `topogpt3/model.py:2626` `def completed_epochs(self, v)`
- `CurriculumTrainer.global_step` (method) `topogpt3/model.py:2630` `def global_step(self)`
- `CurriculumTrainer.global_step` (method) `topogpt3/model.py:2634` `def global_step(self, v)`
- `CurriculumTrainer.best_val_loss` (method) `topogpt3/model.py:2638` `def best_val_loss(self)`
- `CurriculumTrainer.best_val_loss` (method) `topogpt3/model.py:2642` `def best_val_loss(self, v)`
- `CurriculumTrainer.history` (method) `topogpt3/model.py:2646` `def history(self)`
- `CurriculumTrainer.ckpt_mgr` (method) `topogpt3/model.py:2650` `def ckpt_mgr(self)`
- `CurriculumTrainer.resume` (method) `topogpt3/model.py:2653` `def resume(self)`
- `CurriculumTrainer.evaluate` (method) `topogpt3/model.py:2665` `def evaluate(self, dataloader)`
- `CurriculumTrainer.train` (method) `topogpt3/model.py:2725` `def train(self, train_dl, val_dl)`
- `CurriculumTrainer.run_curriculum` (method) `topogpt3/model.py:2728` `def run_curriculum(self, train_paths, val_paths, tokenizer, phases)` -- Top-level entry point: curriculum + progressive seq len.
- `CheckpointManager.__init__` (method) `topogpt3/model.py:2791` `def __init__(self, config, logger)`
- `CheckpointManager.patch_config_for_resume` (method) `topogpt3/model.py:2801` `def patch_config_for_resume(self, cfg)` -- Lee el checkpoint 'latest' y ajusta cfg.N_KV_HEADS / cfg.GQA_GROUPS para que coincidan con la arquitectura guardada.
- `CheckpointManager.should_save` (method) `topogpt3/model.py:2904` `def should_save(self)`
- `CheckpointManager.save` (method) `topogpt3/model.py:2907` `def save(self, model, optimizer, state, is_best)` -- Guarda checkpoint completo.
- `CheckpointManager.load_latest` (method) `topogpt3/model.py:2955` `def load_latest(self, model, optimizer)` -- Carga el ultimo checkpoint guardado.
- `CheckpointManager.load_best` (method) `topogpt3/model.py:2982` `def load_best(self, model)` -- Carga el mejor modelo guardado (solo pesos, sin optimizador).
- `CheckpointManager.has_checkpoint` (method) `topogpt3/model.py:2996` `def has_checkpoint(self)`
- `TopoGPT2Trainer.__init__` (method) `topogpt3/model.py:3017` `def __init__(self, model, config, tokenizer)`
- `TopoGPT2Trainer.resume` (method) `topogpt3/model.py:3066` `def resume(self)` -- Carga el ultimo checkpoint disponible.
- `TopoGPT2Trainer.train` (method) `topogpt3/model.py:3114` `def train(self, train_dl, val_dl)` -- Entrena cfg.EPOCHS epocas adicionales a partir de completed_epochs.
- `TopoGPT2Trainer.evaluate` (method) `topogpt3/model.py:3308` `def evaluate(self, dataloader)`
- `MechanisticMetrics.__init__` (method) `topogpt3/model.py:3362` `def __init__(self, config)`
- `MechanisticMetrics.compute_delta` (method) `topogpt3/model.py:3371` `def compute_delta(self, model)`
- `MechanisticMetrics.compute_alpha` (method) `topogpt3/model.py:3378` `def compute_alpha(self, delta)`
- `MechanisticMetrics.update_grad_buffer` (method) `topogpt3/model.py:3383` `def update_grad_buffer(self, model)` -- Captura gradientes de forma segura, ignorando tensores corruptos.
- `MechanisticMetrics.compute_t_eff` (method) `topogpt3/model.py:3409` `def compute_t_eff(self, lr)` -- T_eff = lr/2 * Var(gradiente).
- `MechanisticMetrics.compute_kappa` (method) `topogpt3/model.py:3417` `def compute_kappa(self, model, dataloader, n_batches)` -- κ = λ_max / λ_min de la covarianza del gradiente.
- `MechanisticMetrics.compute_berry_phase` (method) `topogpt3/model.py:3475` `def compute_berry_phase(self, model)` -- Fase de Berry de los kernels espectrales imaginarios.
- `MechanisticMetrics.compute_lc` (method) `topogpt3/model.py:3488` `def compute_lc(self, model)` -- Complejidad local: 1 - similitud coseno promedio entre filas de pesos.
- `MechanisticMetrics.compute_sp` (method) `topogpt3/model.py:3502` `def compute_sp(self, model)` -- Superposicion: correlacion inter-fila promedio (entrelazamiento de features).
- `MechanisticMetrics.classify_phase` (method) `topogpt3/model.py:3518` `def classify_phase(self, delta, kappa, berry)` -- Clasificacion de fase segun Book.md:
- `MechanisticMetrics.compute_all` (method) `topogpt3/model.py:3536` `def compute_all(self, model, lr, dataloader, compute_kappa)` -- Calcula todas las metricas. compute_kappa=True hace pasadas backward adicionales (caro, usar cada N epochs).
- `MechanisticMetrics.format_log` (method) `topogpt3/model.py:3568` `def format_log(self, m)`
- `Phase0_KernelOptimizer.__init__` (method) `topogpt3/model.py:3605` `def __init__(self, config, logger)`
- `Phase0_KernelOptimizer.optimize` (method) `topogpt3/model.py:3640` `def optimize(self, dataloader)` -- Retorna el mejor ratio de inicializacion de kernels espectrales.
- `Phase1_BatchProspector.__init__` (method) `topogpt3/model.py:3683` `def __init__(self, config, logger)`
- `Phase1_BatchProspector.prospect` (method) `topogpt3/model.py:3687` `def prospect(self, candidates, train_dataset, prospect_steps)` -- Retorna el mejor batch size segun delta y T_eff.
- `Phase2_SeedMiner.__init__` (method) `topogpt3/model.py:3774` `def __init__(self, config, logger)`
- `Phase2_SeedMiner.mine` (method) `topogpt3/model.py:3778` `def mine(self, seed_start, n_seeds, train_dataset, prospect_steps)` -- Retorna la semilla con la mejor trayectoria de delta.
- `Phase4_AnnealingRefiner.__init__` (method) `topogpt3/model.py:3875` `def __init__(self, trainer, t0, cooling_rate, stagnation_patience)`
- `Phase4_AnnealingRefiner.refine` (method) `topogpt3/model.py:3888` `def refine(self, train_dl, val_dl, refine_epochs)` -- Ejecuta refine_epochs epocas de recocido simulado.
- `TopoPhasePipelineV2.__init__` (method) `topogpt3/model.py:4041` `def __init__(self, config, train_tokens, val_tokens, tokenizer, logger, curriculum_tiers, progressive_seq)`
- `TopoPhasePipelineV2.run` (method) `topogpt3/model.py:4095` `def run(self, run_prospect, refine_epochs, resume, prospect_steps, probe_seeds, seed_start)`
- `TopoPhasePipeline.__init__` (method) `topogpt3/model.py:4206` `def __init__(self, config, train_dataset, val_dataset, tokenizer, logger)`
- `TopoPhasePipeline.run` (method) `topogpt3/model.py:4242` `def run(self, run_prospect, refine_epochs, resume, prospect_steps, probe_seeds, seed_start)` -- Ejecuta el pipeline completo.
- `main` (function) `topogpt3/model.py:4330` `def main()`

## topogpt3/rewards.py
Depends on: `topogpt3/chat.py`, `topogpt3/fallback.py`
Imported by: `tests/test_heritage.py`, `topogpt3/__init__.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_ppo.py`
- `rep_penalty` (function) `topogpt3/rewards.py:17` `def rep_penalty(text, n, cap)`
- `base_rewards` (function) `topogpt3/rewards.py:25` `def base_rewards(prompts, completions, reward_fn, device)` -- Group-RL reward skeleton: length + thinking + RM - repetition.
- `spectral_bonus` (function) `topogpt3/rewards.py:55` `def spectral_bonus(fisher_gap, drift, w_fisher, w_drift)` -- Small bonus preserving topological identity (0 when stats absent).
- `grpo_advantages` (function) `topogpt3/rewards.py:70` `def grpo_advantages(rewards, num_generations)`
- `k3_kl` (function) `topogpt3/rewards.py:77` `def k3_kl(ref_logp, new_logp)`
- `grpo_loss` (function) `topogpt3/rewards.py:82` `def grpo_loss(new_logp, old_logp, ref_logp, adv, mask, beta, eps, loss_type, eps_high)`
- `logits_to_log_probs` (function) `topogpt3/rewards.py:107` `def logits_to_log_probs(logits, labels)`
- `dpo_loss_fn` (function) `topogpt3/rewards.py:113` `def dpo_loss_fn(ref_lp, pol_lp, mask, beta)`
- `distillation_loss` (function) `topogpt3/rewards.py:122` `def distillation_loss(student_logits, teacher_logits, mask, labels, alpha, temp)` -- White-box distill: CE + T^2*KL on masked response tokens.
- `tool_call_reward` (function) `topogpt3/rewards.py:151` `def tool_call_reward(text, allowed_tools, require_tool)` -- Reward valid tool-call blocks (fallback profiles / apt_chain).
- `verifier_reward` (function) `topogpt3/rewards.py:176` `def verifier_reward(text, mode)` -- Cheap deterministic verifiers: code AST / JSON / regex pass.
- `execution_reward` (function) `topogpt3/rewards.py:202` `def execution_reward(results)` -- Reward sandboxed tool executions: +1 per passed tool result.

## topogpt3/rollout.py
Imported by: `tests/test_heritage.py`, `topogpt3/__init__.py`, `topogpt3/train_grpo.py`, `topogpt3/train_ppo.py`
- `compute_per_token_logps` (function) `topogpt3/rollout.py:27` `def compute_per_token_logps(model, input_ids, n_keep)`
- `RolloutEngine.rollout` (method) `topogpt3/rollout.py:41` `def rollout(self, prompt_ids, num_generations, max_new_tokens, temperature, tokenizer)`
- `RolloutEngine.update_policy` (method) `topogpt3/rollout.py:46` `def update_policy(self, model)`
- `TorchRolloutEngine.__init__` (method) `topogpt3/rollout.py:51` `def __init__(self, policy_model, tokenizer, device, decode)`
- `TorchRolloutEngine.rollout` (method) `topogpt3/rollout.py:57` `def rollout(self, prompt_ids, num_generations, max_new_tokens, temperature, tokenizer)`
- `TorchRolloutEngine.update_policy` (method) `topogpt3/rollout.py:79` `def update_policy(self, model)`
- `create_rollout_engine` (function) `topogpt3/rollout.py:83` `def create_rollout_engine(policy_model, tokenizer, device)`

## topogpt3/structured_output.py
Imported by: `tests/test_structured_output.py`, `topogpt3/api_server.py`
- `GrammarSpec.cache_key` (method) `topogpt3/structured_output.py:36` `def cache_key(self)`
- `parse_response_format` (function) `topogpt3/structured_output.py:56` `def parse_response_format(response_format)` -- Translate an OpenAI ``response_format`` payload into a GrammarSpec.
- `parse_so_args` (function) `topogpt3/structured_output.py:93` `def parse_so_args(so_args)` -- Translate a DeepInfer-style ``so_args`` payload into a GrammarSpec.
- `GrammarConstraint.__init__` (method) `topogpt3/structured_output.py:185` `def __init__(self, xg, compiled, vocab_size)`
- `GrammarConstraint.reset` (method) `topogpt3/structured_output.py:197` `def reset(self)`
- `GrammarConstraint.is_terminated` (method) `topogpt3/structured_output.py:201` `def is_terminated(self)`
- `GrammarConstraint.apply` (method) `topogpt3/structured_output.py:204` `def apply(self, logits)` -- Mask disallowed tokens in ``logits`` with ``-inf`` in place.
- `GrammarConstraint.accept` (method) `topogpt3/structured_output.py:211` `def accept(self, token_id)` -- Feed an emitted token to the matcher.
- `build_constraint` (function) `topogpt3/structured_output.py:218` `def build_constraint(tokenizer, spec)` -- Compile ``spec`` (cached) and return a fresh matcher for one request.
- `constraint_from_request` (function) `topogpt3/structured_output.py:240` `def constraint_from_request(tokenizer, response_format, so_args)` -- Resolve either request surface into a ready-to-use constraint.

## topogpt3/tokenizer_tools.py
Depends on: `topogpt3/checkpoint_meta.py`
- `audit` (function) `topogpt3/tokenizer_tools.py:27` `def audit(checkpoint_dir, corpus_files, sample_chars)` -- Embedding share + chars/token stats for the gpt2 BPE identity.
- `train_code_bpe` (function) `topogpt3/tokenizer_tools.py:76` `def train_code_bpe(corpus_files, out_dir, vocab_size)` -- Train a compact BPE with HF tokenizers (optional dependency).
- `load_tokenizer_artifact` (function) `topogpt3/tokenizer_tools.py:110` `def load_tokenizer_artifact(path)`
- `ArtifactTokenizer.__init__` (method) `topogpt3/tokenizer_tools.py:119` `def __init__(self)`
- `ArtifactTokenizer.encode` (method) `topogpt3/tokenizer_tools.py:123` `def encode(self, text)`
- `ArtifactTokenizer.decode` (method) `topogpt3/tokenizer_tools.py:126` `def decode(self, tokens)`
- `ArtifactTokenizer.eot_token` (method) `topogpt3/tokenizer_tools.py:129` `def eot_token(self)`
- `resize_embeddings` (function) `topogpt3/tokenizer_tools.py:135` `def resize_embeddings(checkpoint_dir, new_vocab, out_dir)` -- Warm-start a checkpoint on a new vocab via longest-prefix byte match.
- `main` (function) `topogpt3/tokenizer_tools.py:183` `def main()`

## topogpt3/tools_agent.py
Depends on: `eval/sandbox.py`, `topogpt3/chat.py`, `topogpt3/fallback.py`
Imported by: `tests/test_heritage.py`, `topogpt3/__init__.py`, `topogpt3/eval_toolcall.py`, `topogpt3/train_agent.py`
- `execute_tool` (function) `topogpt3/tools_agent.py:96` `def execute_tool(name, args)`
- `rollout_multiturn` (function) `topogpt3/tools_agent.py:117` `def rollout_multiturn(generate_fn, tokenizer, messages, tools, max_turns, max_new_tokens, open_thinking)` -- generate_fn(prompt_text)->text.

## topogpt3/train.py
Depends on: `topogpt3/model.py`
Imported by: `eval/diag_static.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/export_chat.py`
- `TopoGPT3Config.build_topogpt2_config` (method) `topogpt3/train.py:170` `def build_topogpt2_config(self, max_seq_len, attn_window)`
- `GrassmannianTracker.__init__` (method) `topogpt3/train.py:217` `def __init__(self, config, logger)`
- `GrassmannianTracker.estimate_fisher_gap` (method) `topogpt3/train.py:313` `def estimate_fisher_gap(self, model, dataloader, vocab_size, r_target)` -- Sigma_F ~= (1/M) sum_m g_m g_m^T  (covarianza muestral de gradientes).
- `GrassmannianTracker.update_holonomy` (method) `topogpt3/train.py:386` `def update_holonomy(self, U_new)` -- Holonomia discreta: T_n = U_n^dagger U_{n+1}  en C^{r x r}  (transporte paralelo discreto) U_Gamma <- T_n * U_Gamma...
- `GrassmannianTracker.conjugation_distance_su2` (method) `topogpt3/train.py:412` `def conjugation_distance_su2(U1, U2)` -- Para U1, U2 en U(1)/U(2):  d_conj(U1, U2) = min_g || U1 - g U2 g^{-1} ||_F.
- `GrassmannianTracker.snapshot` (method) `topogpt3/train.py:445` `def snapshot(self, model, step, dataloader, vocab_size)`
- `GrassmannianTracker.format_log` (method) `topogpt3/train.py:500` `def format_log(self, snap)`
- `GrassmannianTracker.save` (method) `topogpt3/train.py:522` `def save(self, path)`
- `apply_gauss_patch` (function) `topogpt3/train.py:568` `def apply_gauss_patch(logger)` -- Activa la version Gauss de _contract en QuaternionSpectralLayer.
- `EfficiencyMetrics.__init__` (method) `topogpt3/train.py:600` `def __init__(self, model, config, logger, gauss_enabled)`
- `EfficiencyMetrics.measure_throughput` (method) `topogpt3/train.py:619` `def measure_throughput(self, dataloader, vocab_size)` -- Devuelve (tokens_por_segundo, segundos_por_step).
- `EfficiencyMetrics.estimate_flops_per_step` (method) `topogpt3/train.py:651` `def estimate_flops_per_step(self, batch_size, seq_len)` -- Heuristica: 6 * N_no_embed * tokens (forward + backward).
- `EfficiencyMetrics.estimate_bytes_per_step` (method) `topogpt3/train.py:656` `def estimate_bytes_per_step(self, batch_size, seq_len, dtype_bytes)` -- Bandwidth aproximada: lectura de pesos + activaciones por step.
- `EfficiencyMetrics.compute` (method) `topogpt3/train.py:664` `def compute(self, dataloader, vocab_size, val_loss, val_ppl, val_acc, batch_size, seq_len)`
- `EfficiencyMetrics.format_log` (method) `topogpt3/train.py:696` `def format_log(self, m)`
- `CodeCurriculumLoader.__init__` (method) `topogpt3/train.py:729` `def __init__(self, config, tokenizer, logger)`
- `CodeCurriculumLoader.prepare_tier` (method) `topogpt3/train.py:891` `def prepare_tier(self, tier_index, force)`
- `flush` (function) `topogpt3/train.py:922` `def flush(split)`
- `CodeCurriculumLoader.open_memmap` (method) `topogpt3/train.py:986` `def open_memmap(self, tier, split)`
- `BlockTokenDataset.__init__` (method) `topogpt3/train.py:1006` `def __init__(self, tokens, seq_len)`
- `CheckpointStore.__init__` (method) `topogpt3/train.py:1030` `def __init__(self, root, max_keep, logger)`
- `CheckpointStore.save` (method) `topogpt3/train.py:1037` `def save(self, tag, model, optimizer, state)` -- Guarda checkpoint atomico en <root>/last/ sobreescribiendo el anterior.
- `CheckpointStore.load_latest` (method) `topogpt3/train.py:1071` `def load_latest(self, model, optimizer)`
- `CheckpointStore.should_save` (method) `topogpt3/train.py:1095` `def should_save(self, interval_min)`
- `TopoGPT3Trainer.__init__` (method) `topogpt3/train.py:1119` `def __init__(self, config, start_tier)`
- `TopoGPT3Trainer.prepare_all` (method) `topogpt3/train.py:1174` `def prepare_all(self, force)` -- Prepara cada tier; un fallo en uno no detiene los demas.
- `TopoGPT3Trainer.run` (method) `topogpt3/train.py:1449` `def run(self)`
- `parse_args` (function) `topogpt3/train.py:1538` `def parse_args()`
- `main` (function) `topogpt3/train.py:1567` `def main()`

## topogpt3/train_agent.py
Depends on: `topogpt3/chat.py`, `topogpt3/checkpoint_meta.py`, `topogpt3/model.py`, `topogpt3/rewards.py`, `topogpt3/tools_agent.py`, `topogpt3/trainer_utils_topo.py`
Imported by: `topogpt3/__main__.py`
- `agent_reward` (function) `topogpt3/train_agent.py:41` `def agent_reward(text, gt, used_tools, tool_results, allowed_tools, require_tool, verifier)` -- Format + ground-truth + valid tool calls + sandboxed execution.
- `main` (function) `topogpt3/train_agent.py:67` `def main()`

## topogpt3/train_distill.py
Depends on: `topogpt3/checkpoint_meta.py`, `topogpt3/model.py`, `topogpt3/rewards.py`, `topogpt3/trainer_utils_topo.py`
Imported by: `topogpt3/__main__.py`
- `main` (function) `topogpt3/train_distill.py:27` `def main()`

## topogpt3/train_dpo.py
Depends on: `topogpt3/checkpoint_meta.py`, `topogpt3/model.py`, `topogpt3/rewards.py`, `topogpt3/trainer_utils_topo.py`
Imported by: `topogpt3/__main__.py`
- `load_model` (function) `topogpt3/train_dpo.py:31` `def load_model(checkpoint, device)`
- `main` (function) `topogpt3/train_dpo.py:43` `def main()`

## topogpt3/train_grpo.py
Depends on: `topogpt3/checkpoint_meta.py`, `topogpt3/model.py`, `topogpt3/rewards.py`, `topogpt3/rollout.py`, `topogpt3/trainer_utils_topo.py`
Imported by: `topogpt3/__main__.py`
- `main` (function) `topogpt3/train_grpo.py:32` `def main()`

## topogpt3/train_lora.py
Depends on: `topogpt3/checkpoint_meta.py`, `topogpt3/lora.py`, `topogpt3/model.py`, `topogpt3/trainer_utils_topo.py`
Imported by: `topogpt3/__main__.py`
- `load_base` (function) `topogpt3/train_lora.py:32` `def load_base(checkpoint, device)`
- `main` (function) `topogpt3/train_lora.py:46` `def main()`

## topogpt3/train_ppo.py
Depends on: `topogpt3/checkpoint_meta.py`, `topogpt3/model.py`, `topogpt3/rewards.py`, `topogpt3/rollout.py`, `topogpt3/trainer_utils_topo.py`
Imported by: `topogpt3/__main__.py`
- `TopoCritic.__init__` (method) `topogpt3/train_ppo.py:32` `def __init__(self, trunk)`
- `TopoCritic.forward` (method) `topogpt3/train_ppo.py:38` `def forward(self, ids)`
- `main` (function) `topogpt3/train_ppo.py:47` `def main()`

## topogpt3/trainer_utils_topo.py
Imported by: `topogpt3/__init__.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`
- `Logger` (function) `topogpt3/trainer_utils_topo.py:20` `def Logger(content, quiet)`
- `is_main_process` (function) `topogpt3/trainer_utils_topo.py:25` `def is_main_process()`
- `get_lr` (function) `topogpt3/trainer_utils_topo.py:29` `def get_lr(current_step, total_steps, lr)`
- `setup_seed` (function) `topogpt3/trainer_utils_topo.py:34` `def setup_seed(seed)`
- `init_distributed_mode` (function) `topogpt3/trainer_utils_topo.py:43` `def init_distributed_mode()`
- `SkipBatchSampler.__init__` (method) `topogpt3/trainer_utils_topo.py:53` `def __init__(self, sampler, batch_size, skip_batches)`
- `topo_checkpoint` (function) `topogpt3/trainer_utils_topo.py:77` `def topo_checkpoint(save_dir, weight, model, optimizer, scheduler, scaler, epoch, step, wandb, extra)` -- Atomic double-save: fp16 weights + resume state (weights + optim).

## topogpt3/yarn.py
Imported by: `tests/test_heritage.py`, `topogpt3/__init__.py`, `topogpt3/model.py`
- `yarn_scale_inv_freq` (function) `topogpt3/yarn.py:26` `def yarn_scale_inv_freq(inv_freq, d_head, cfg)` -- Apply NTK-by-parts ramp to inv_freq.
- `apply_yarn_to_rope` (function) `topogpt3/yarn.py:50` `def apply_yarn_to_rope(rope_module, cfg)` -- Patch an existing RotaryEmbedding in-place + rebuild cache.

