# API (page 2 of 2)
Previous: [API.md](API.md)

## topogpt3/model.py
Depends on: `synthetic_dataset.py`, `topogpt3/continuation.py`, `topogpt3/yarn.py`
Imported by: `eval/diag_static.py`, `eval/noise_sweep.py`, `tests/test_heritage.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`
- `TopoGPT2Config.setup_logger` (method) `topogpt3/model.py:192` `def setup_logger(name, level)`
- `TopoGPT2Config.set_seed` (method) `topogpt3/model.py:202` `def set_seed(seed, device)`
- `QuaternionOps.hamilton_product` (method) `topogpt3/model.py:222` `def hamilton_product(q1, q2)` -- Producto de Hamilton q1 ⊗ q2.
- `QuaternionOps.normalize` (method) `topogpt3/model.py:234` `def normalize(q, eps)`
- `QuaternionOps.conjugate` (method) `topogpt3/model.py:238` `def conjugate(q)`
- `QuaternionOps.rotate_vector` (method) `topogpt3/model.py:243` `def rotate_vector(v, q)` -- Rota vector 3D v por cuaternión unitario q. v:[...,3] q:[...,4]
- `QuaternionLinear.__init__` (method) `topogpt3/model.py:265` `def __init__(self, in_features, out_features, bias)`
- `QuaternionLinear.forward` (method) `topogpt3/model.py:281` `def forward(self, x)` -- x: [..., in_features] → [..., out_features]
- `QuaternionSpectralLayer.__init__` (method) `topogpt3/model.py:318` `def __init__(self, in_q, out_q, grid_h, grid_w, init_scale)`
- `QuaternionSpectralLayer.forward` (method) `topogpt3/model.py:344` `def forward(self, x)` -- x: [B, 4*in_q, H, W]  (4 canales cuaterniones sobre grid espacial) → [B, 4*out_q, H, W]
- `SpectralAutoencoder.__init__` (method) `topogpt3/model.py:398` `def __init__(self, config)`
- `SpectralAutoencoder.encode` (method) `topogpt3/model.py:436` `def encode(self, x)` -- x: [..., D_MODEL] → latent: [..., D_LAT]
- `SpectralAutoencoder.decode` (method) `topogpt3/model.py:441` `def decode(self, z)` -- z: [..., D_LAT] → recon: [..., D_MODEL]
- `SpectralAutoencoder.forward` (method) `topogpt3/model.py:446` `def forward(self, x)` -- Devuelve (latent, recon_loss)
- `SpectralAutoencoder.process_torus_grid` (method) `topogpt3/model.py:453` `def process_torus_grid(self, grid)` -- Procesa el grid del toro con QuaternionSpectralLayer. grid: [B, 4*D_QUAT, RADIAL, ANGULAR]  →  [B, 4*D_QUAT, RADIAL...
- `QuaternionTorusBrain.__init__` (method) `topogpt3/model.py:486` `def __init__(self, d_model, config)`
- `QuaternionTorusBrain.forward` (method) `topogpt3/model.py:624` `def forward(self, x)` -- x: [B, S, D_MODEL] → output: [B, S, D_MODEL], recon_loss: scalar
- `RotaryEmbedding.__init__` (method) `topogpt3/model.py:697` `def __init__(self, d_head, max_seq_len, base, yarn_factor, yarn_orig_max)`
- `RotaryEmbedding.enable_yarn` (method) `topogpt3/model.py:716` `def enable_yarn(self, factor, orig_max)` -- Enable YaRN extrapolation post-hoc (rebuilds cache in place).
- `RotaryEmbedding.forward` (method) `topogpt3/model.py:736` `def forward(self, q, k, seq_len, offset)` -- q, k: [B, n_heads, S_q/S_k, d_head] offset: posicion inicial (para KV cache: longitud del cache existente) Aplica...
- `RMSNorm.__init__` (method) `topogpt3/model.py:763` `def __init__(self, d_model, eps)`
- `RMSNorm.forward` (method) `topogpt3/model.py:768` `def forward(self, x)`
- `SwiGLU.__init__` (method) `topogpt3/model.py:784` `def __init__(self, d_model, expansion, dropout)`
- `SwiGLU.forward` (method) `topogpt3/model.py:798` `def forward(self, x)`
- `TopoMoEBrain.__init__` (method) `topogpt3/model.py:821` `def __init__(self, d_model, config)`
- `TopoMoEBrain.forward` (method) `topogpt3/model.py:884` `def forward(self, x)` -- → output: [B, S, D], aux_loss: escalar
- `MultiHeadAttention.__init__` (method) `topogpt3/model.py:921` `def __init__(self, d_model, n_heads, config)`
- `MultiHeadAttention.forward` (method) `topogpt3/model.py:940` `def forward(self, x, is_causal, past_kv)` -- Args: is_causal: usar mascara causal past_kv:  (K_cache, V_cache) de pasos anteriores o None Returns: out:      [B...
- `TopoGPT2Layer.__init__` (method) `topogpt3/model.py:1024` `def __init__(self, d_model, n_heads, config)`
- `TopoGPT2Layer.forward` (method) `topogpt3/model.py:1042` `def forward(self, x, past_kv)` -- Retorna (x_out, aux_loss, kv_cache).
- `TopoGPT2Layer.ckpt_fn` (method) `topogpt3/model.py:1050` `def ckpt_fn(x_in)`
- `TopoGPT2.__init__` (method) `topogpt3/model.py:1073` `def __init__(self, config)`
- `TopoGPT2.forward` (method) `topogpt3/model.py:1105` `def forward(self, token_ids, past_kvs)` -- token_ids: [B, S]  (enteros) past_kvs:  lista de (K, V) por capa, o None para entrenamiento → logits: [B, S...
- `TopoGPT2.forward_with_memory` (method) `topogpt3/model.py:1128` `def forward_with_memory(self, token_ids)` -- Process long sequences with latent memory-token context compression.
- `TopoGPT2.count_params` (method) `topogpt3/model.py:1178` `def count_params(self)`
- `TopoGPT2.generate` (method) `topogpt3/model.py:1184` `def generate(self, token_ids, max_new_tokens, temperature, top_k, repetition_penalty)` -- Autoregressive generation with KV cache and top-k sampling.
- `TopoGPT2.generate_with_continuation` (method) `topogpt3/model.py:1235` `def generate_with_continuation(self, token_ids, tokenizer, max_new_tokens, temperature, top_k, repetition_penalty...`
- `BPETokenizer.__init__` (method) `topogpt3/model.py:1282` `def __init__(self, encoding)`
- `BPETokenizer.encode` (method) `topogpt3/model.py:1290` `def encode(self, text)`
- `BPETokenizer.decode` (method) `topogpt3/model.py:1293` `def decode(self, tokens)`
- `BPETokenizer.eot_token` (method) `topogpt3/model.py:1296` `def eot_token(self)`
- `FileManifest.__init__` (method) `topogpt3/model.py:1408` `def __init__(self, root, cache_dir, logger)`
- `FileManifest.scan` (method) `topogpt3/model.py:1415` `def scan(self, force)` -- Walk directory tree collecting text file paths.
- `MemmapTokenizer.__init__` (method) `topogpt3/model.py:1482` `def __init__(self, cache_dir, logger)`
- `MemmapTokenizer.tokenize` (method) `topogpt3/model.py:1487` `def tokenize(self, file_paths, tokenizer, cache_key, max_tokens, min_chars)` -- Tokenize all files and return a memory-mapped numpy array.
- `MappedTokenDataset.__init__` (method) `topogpt3/model.py:1570` `def __init__(self, tokens, seq_len)`
- `TextFilter.__init__` (method) `topogpt3/model.py:1598` `def __init__(self, config, logger)`
- `TextFilter.filter_file` (method) `topogpt3/model.py:1645` `def filter_file(self, path, tokenizer)` -- Read and evaluate a file.
- `TextFilter.report` (method) `topogpt3/model.py:1685` `def report(self)`
- `CurriculumDataset.__init__` (method) `topogpt3/model.py:1706` `def __init__(self, tokens, seq_len, file_tiers, active_tier, logger)`
- `CurriculumDataset.set_tier` (method) `topogpt3/model.py:1722` `def set_tier(self, tier)`
- `CurriculumDataset.build_file_tiers` (method) `topogpt3/model.py:1737` `def build_file_tiers(paths, short, med)` -- Classify file paths into complexity tiers by line count.
- `ProgressiveSeqLenTrainer.__init__` (method) `topogpt3/model.py:1774` `def __init__(self, base_trainer)`
- `ProgressiveSeqLenTrainer.run` (method) `topogpt3/model.py:1790` `def run(self, train_paths, val_paths, tokenizer, file_tiers, phases)` -- Run training with progressive sequence length across phases.
- `SpeculativeDecoder.__init__` (method) `topogpt3/model.py:1848` `def __init__(self, target_model, config, logger)`
- `SpeculativeDecoder.generate` (method) `topogpt3/model.py:1870` `def generate(self, token_ids, max_new_tokens, temperature, top_k, repetition_penalty)` -- Autoregressive generation via speculative decoding.
- `QuantizedEmbedding.__init__` (method) `topogpt3/model.py:1961` `def __init__(self, embed, mode)`
- `QuantizedEmbedding.forward` (method) `topogpt3/model.py:1990` `def forward(self, indices)`
- `QuantizedEmbedding.apply_quantization` (method) `topogpt3/model.py:1994` `def apply_quantization(model, config)` -- Quantize embedding and lm_head layers for reduced VRAM usage.
- `CurriculumTrainer.__init__` (method) `topogpt3/model.py:2030` `def __init__(self, model, config, tokenizer)`
- `CurriculumTrainer.cache_tokens` (method) `topogpt3/model.py:2037` `def cache_tokens(self, key, tokens)`
- `CurriculumTrainer.model` (method) `topogpt3/model.py:2041` `def model(self)`
- `CurriculumTrainer.optimizer` (method) `topogpt3/model.py:2045` `def optimizer(self)`
- `CurriculumTrainer.scaler` (method) `topogpt3/model.py:2049` `def scaler(self)`
- `CurriculumTrainer.amp_dtype` (method) `topogpt3/model.py:2053` `def amp_dtype(self)`
- `CurriculumTrainer.completed_epochs` (method) `topogpt3/model.py:2057` `def completed_epochs(self)`
- `CurriculumTrainer.completed_epochs` (method) `topogpt3/model.py:2061` `def completed_epochs(self, v)`
- `CurriculumTrainer.global_step` (method) `topogpt3/model.py:2065` `def global_step(self)`
- `CurriculumTrainer.global_step` (method) `topogpt3/model.py:2069` `def global_step(self, v)`
- `CurriculumTrainer.best_val_loss` (method) `topogpt3/model.py:2073` `def best_val_loss(self)`
- `CurriculumTrainer.best_val_loss` (method) `topogpt3/model.py:2077` `def best_val_loss(self, v)`
- `CurriculumTrainer.history` (method) `topogpt3/model.py:2081` `def history(self)`
- `CurriculumTrainer.ckpt_mgr` (method) `topogpt3/model.py:2085` `def ckpt_mgr(self)`
- `CurriculumTrainer.resume` (method) `topogpt3/model.py:2088` `def resume(self)`
- `CurriculumTrainer.evaluate` (method) `topogpt3/model.py:2100` `def evaluate(self, dataloader)`
- `CurriculumTrainer.train` (method) `topogpt3/model.py:2145` `def train(self, train_dl, val_dl)`
- `CurriculumTrainer.run_curriculum` (method) `topogpt3/model.py:2148` `def run_curriculum(self, train_paths, val_paths, tokenizer, phases)` -- Top-level entry point: curriculum + progressive seq len.
- `CheckpointManager.__init__` (method) `topogpt3/model.py:2199` `def __init__(self, config, logger)`
- `CheckpointManager.patch_config_for_resume` (method) `topogpt3/model.py:2209` `def patch_config_for_resume(self, cfg)` -- Lee el checkpoint 'latest' y ajusta cfg.N_KV_HEADS / cfg.GQA_GROUPS para que coincidan con la arquitectura guardada.
- `CheckpointManager.should_save` (method) `topogpt3/model.py:2310` `def should_save(self)`
- `CheckpointManager.save` (method) `topogpt3/model.py:2313` `def save(self, model, optimizer, state, is_best)` -- Guarda checkpoint completo.
- `CheckpointManager.load_latest` (method) `topogpt3/model.py:2358` `def load_latest(self, model, optimizer)` -- Carga el ultimo checkpoint guardado.
- `CheckpointManager.load_best` (method) `topogpt3/model.py:2385` `def load_best(self, model)` -- Carga el mejor modelo guardado (solo pesos, sin optimizador).
- `CheckpointManager.has_checkpoint` (method) `topogpt3/model.py:2397` `def has_checkpoint(self)`
- `TopoGPT2Trainer.__init__` (method) `topogpt3/model.py:2419` `def __init__(self, model, config, tokenizer)`
- `TopoGPT2Trainer.resume` (method) `topogpt3/model.py:2454` `def resume(self)` -- Carga el ultimo checkpoint disponible.
- `TopoGPT2Trainer.train` (method) `topogpt3/model.py:2502` `def train(self, train_dl, val_dl)` -- Entrena cfg.EPOCHS epocas adicionales a partir de completed_epochs.
- `TopoGPT2Trainer.evaluate` (method) `topogpt3/model.py:2670` `def evaluate(self, dataloader)`
- `MechanisticMetrics.__init__` (method) `topogpt3/model.py:2720` `def __init__(self, config)`
- `MechanisticMetrics.compute_delta` (method) `topogpt3/model.py:2728` `def compute_delta(self, model)`
- `MechanisticMetrics.compute_alpha` (method) `topogpt3/model.py:2735` `def compute_alpha(self, delta)`
- `MechanisticMetrics.update_grad_buffer` (method) `topogpt3/model.py:2740` `def update_grad_buffer(self, model)` -- Captura gradientes de forma segura, ignorando tensores corruptos.
- `MechanisticMetrics.compute_t_eff` (method) `topogpt3/model.py:2766` `def compute_t_eff(self, lr)` -- T_eff = lr/2 * Var(gradiente).
- `MechanisticMetrics.compute_kappa` (method) `topogpt3/model.py:2774` `def compute_kappa(self, model, dataloader, n_batches)` -- κ = λ_max / λ_min de la covarianza del gradiente.
- `MechanisticMetrics.compute_berry_phase` (method) `topogpt3/model.py:2832` `def compute_berry_phase(self, model)` -- Fase de Berry de los kernels espectrales imaginarios.
- `MechanisticMetrics.compute_lc` (method) `topogpt3/model.py:2845` `def compute_lc(self, model)` -- Complejidad local: 1 - similitud coseno promedio entre filas de pesos.
- `MechanisticMetrics.compute_sp` (method) `topogpt3/model.py:2859` `def compute_sp(self, model)` -- Superposicion: correlacion inter-fila promedio (entrelazamiento de features).
- `MechanisticMetrics.classify_phase` (method) `topogpt3/model.py:2875` `def classify_phase(self, delta, kappa, berry)` -- Clasificacion de fase segun Book.md:
- `MechanisticMetrics.compute_all` (method) `topogpt3/model.py:2894` `def compute_all(self, model, lr, dataloader, compute_kappa)` -- Calcula todas las metricas. compute_kappa=True hace pasadas backward adicionales (caro, usar cada N epochs).
- `MechanisticMetrics.format_log` (method) `topogpt3/model.py:2919` `def format_log(self, m)`
- `Phase0_KernelOptimizer.__init__` (method) `topogpt3/model.py:2955` `def __init__(self, config, logger)`
- `Phase0_KernelOptimizer.optimize` (method) `topogpt3/model.py:2988` `def optimize(self, dataloader)` -- Retorna el mejor ratio de inicializacion de kernels espectrales.
- `Phase1_BatchProspector.__init__` (method) `topogpt3/model.py:3028` `def __init__(self, config, logger)`
- `Phase1_BatchProspector.prospect` (method) `topogpt3/model.py:3032` `def prospect(self, candidates, train_dataset, prospect_steps)` -- Retorna el mejor batch size segun delta y T_eff.
- `Phase2_SeedMiner.__init__` (method) `topogpt3/model.py:3111` `def __init__(self, config, logger)`
- `Phase2_SeedMiner.mine` (method) `topogpt3/model.py:3115` `def mine(self, seed_start, n_seeds, train_dataset, prospect_steps)` -- Retorna la semilla con la mejor trayectoria de delta.
- `Phase4_AnnealingRefiner.__init__` (method) `topogpt3/model.py:3197` `def __init__(self, trainer, t0, cooling_rate, stagnation_patience)`
- `Phase4_AnnealingRefiner.refine` (method) `topogpt3/model.py:3206` `def refine(self, train_dl, val_dl, refine_epochs)` -- Ejecuta refine_epochs epocas de recocido simulado.
- `TopoPhasePipelineV2.__init__` (method) `topogpt3/model.py:3349` `def __init__(self, config, train_tokens, val_tokens, tokenizer, logger, curriculum_tiers, progressive_seq)`
- `TopoPhasePipelineV2.run` (method) `topogpt3/model.py:3385` `def run(self, run_prospect, refine_epochs, resume, prospect_steps, probe_seeds, seed_start)`
- `TopoPhasePipeline.__init__` (method) `topogpt3/model.py:3487` `def __init__(self, config, train_dataset, val_dataset, tokenizer, logger)`
- `TopoPhasePipeline.run` (method) `topogpt3/model.py:3509` `def run(self, run_prospect, refine_epochs, resume, prospect_steps, probe_seeds, seed_start)` -- Ejecuta el pipeline completo.
- `TopoPhasePipeline.main` (method) `topogpt3/model.py:3589` `def main()`

## topogpt3/rewards.py
Imported by: `tests/test_heritage.py`, `topogpt3/__init__.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_ppo.py`
- `rep_penalty` (function) `topogpt3/rewards.py:17` `def rep_penalty(text, n, cap)`
- `base_rewards` (function) `topogpt3/rewards.py:25` `def base_rewards(prompts, completions, reward_fn, device)` -- Group-RL reward skeleton: length + thinking + RM - repetition.
- `spectral_bonus` (function) `topogpt3/rewards.py:55` `def spectral_bonus(fisher_gap, drift, w_fisher, w_drift)` -- Small bonus preserving topological identity (0 when stats absent).
- `grpo_advantages` (function) `topogpt3/rewards.py:67` `def grpo_advantages(rewards, num_generations)`
- `k3_kl` (function) `topogpt3/rewards.py:74` `def k3_kl(ref_logp, new_logp)`
- `grpo_loss` (function) `topogpt3/rewards.py:79` `def grpo_loss(new_logp, old_logp, ref_logp, adv, mask, beta, eps, loss_type, eps_high)`
- `logits_to_log_probs` (function) `topogpt3/rewards.py:94` `def logits_to_log_probs(logits, labels)`
- `dpo_loss_fn` (function) `topogpt3/rewards.py:99` `def dpo_loss_fn(ref_lp, pol_lp, mask, beta)`
- `distillation_loss` (function) `topogpt3/rewards.py:108` `def distillation_loss(student_logits, teacher_logits, mask, labels, alpha, temp)` -- White-box distill: CE + T^2*KL on masked response tokens.

## topogpt3/rollout.py
Imported by: `tests/test_heritage.py`, `topogpt3/__init__.py`, `topogpt3/train_grpo.py`, `topogpt3/train_ppo.py`
- `RolloutResult.compute_per_token_logps` (method) `topogpt3/rollout.py:27` `def compute_per_token_logps(model, input_ids, n_keep)`
- `RolloutEngine.rollout` (method) `topogpt3/rollout.py:41` `def rollout(self, prompt_ids, num_generations, max_new_tokens, temperature, tokenizer)`
- `RolloutEngine.update_policy` (method) `topogpt3/rollout.py:46` `def update_policy(self, model)`
- `TorchRolloutEngine.__init__` (method) `topogpt3/rollout.py:51` `def __init__(self, policy_model, tokenizer, device, decode)`
- `TorchRolloutEngine.rollout` (method) `topogpt3/rollout.py:57` `def rollout(self, prompt_ids, num_generations, max_new_tokens, temperature, tokenizer)`
- `TorchRolloutEngine.update_policy` (method) `topogpt3/rollout.py:79` `def update_policy(self, model)`
- `TorchRolloutEngine.create_rollout_engine` (method) `topogpt3/rollout.py:83` `def create_rollout_engine(policy_model, tokenizer, device)`

## topogpt3/tools_agent.py
Depends on: `eval/sandbox.py`, `topogpt3/chat.py`
Imported by: `tests/test_heritage.py`, `topogpt3/__init__.py`, `topogpt3/eval_toolcall.py`, `topogpt3/train_agent.py`
- `execute_tool` (function) `topogpt3/tools_agent.py:59` `def execute_tool(name, args)`
- `rollout_multiturn` (function) `topogpt3/tools_agent.py:80` `def rollout_multiturn(generate_fn, tokenizer, messages, tools, max_turns, max_new_tokens, open_thinking)` -- generate_fn(prompt_text)->text.

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
- `GrassmannianTracker.apply_gauss_patch` (method) `topogpt3/train.py:568` `def apply_gauss_patch(logger)` -- Activa la version Gauss de _contract en QuaternionSpectralLayer.
- `EfficiencyMetrics.__init__` (method) `topogpt3/train.py:600` `def __init__(self, model, config, logger, gauss_enabled)`
- `EfficiencyMetrics.measure_throughput` (method) `topogpt3/train.py:619` `def measure_throughput(self, dataloader, vocab_size)` -- Devuelve (tokens_por_segundo, segundos_por_step).
- `EfficiencyMetrics.estimate_flops_per_step` (method) `topogpt3/train.py:651` `def estimate_flops_per_step(self, batch_size, seq_len)` -- Heuristica: 6 * N_no_embed * tokens (forward + backward).
- `EfficiencyMetrics.estimate_bytes_per_step` (method) `topogpt3/train.py:656` `def estimate_bytes_per_step(self, batch_size, seq_len, dtype_bytes)` -- Bandwidth aproximada: lectura de pesos + activaciones por step.
- `EfficiencyMetrics.compute` (method) `topogpt3/train.py:664` `def compute(self, dataloader, vocab_size, val_loss, val_ppl, val_acc, batch_size, seq_len)`
- `EfficiencyMetrics.format_log` (method) `topogpt3/train.py:696` `def format_log(self, m)`
- `CodeCurriculumLoader.__init__` (method) `topogpt3/train.py:729` `def __init__(self, config, tokenizer, logger)`
- `CodeCurriculumLoader.prepare_tier` (method) `topogpt3/train.py:891` `def prepare_tier(self, tier_index, force)`
- `CodeCurriculumLoader.flush` (method) `topogpt3/train.py:922` `def flush(split)`
- `CodeCurriculumLoader.open_memmap` (method) `topogpt3/train.py:986` `def open_memmap(self, tier, split)`
- `BlockTokenDataset.__init__` (method) `topogpt3/train.py:1006` `def __init__(self, tokens, seq_len)`
- `CheckpointStore.__init__` (method) `topogpt3/train.py:1030` `def __init__(self, root, max_keep, logger)`
- `CheckpointStore.save` (method) `topogpt3/train.py:1037` `def save(self, tag, model, optimizer, state)` -- Guarda checkpoint atomico en <root>/last/ sobreescribiendo el anterior.
- `CheckpointStore.load_latest` (method) `topogpt3/train.py:1071` `def load_latest(self, model, optimizer)`
- `CheckpointStore.should_save` (method) `topogpt3/train.py:1095` `def should_save(self, interval_min)`
- `TopoGPT3Trainer.__init__` (method) `topogpt3/train.py:1119` `def __init__(self, config, start_tier)`
- `TopoGPT3Trainer.prepare_all` (method) `topogpt3/train.py:1174` `def prepare_all(self, force)` -- Prepara cada tier; un fallo en uno no detiene los demas.
- `TopoGPT3Trainer.run` (method) `topogpt3/train.py:1449` `def run(self)`
- `TopoGPT3Trainer.parse_args` (method) `topogpt3/train.py:1538` `def parse_args()`
- `TopoGPT3Trainer.main` (method) `topogpt3/train.py:1567` `def main()`

## topogpt3/train_agent.py
Depends on: `topogpt3/chat.py`, `topogpt3/model.py`, `topogpt3/rewards.py`, `topogpt3/tools_agent.py`, `topogpt3/trainer_utils_topo.py`
Imported by: `topogpt3/__main__.py`
- `agent_reward` (function) `topogpt3/train_agent.py:31` `def agent_reward(text, gt, used_tools)`
- `main` (function) `topogpt3/train_agent.py:43` `def main()`

## topogpt3/train_distill.py
Depends on: `topogpt3/model.py`, `topogpt3/rewards.py`, `topogpt3/trainer_utils_topo.py`
Imported by: `topogpt3/__main__.py`
- `main` (function) `topogpt3/train_distill.py:24` `def main()`

## topogpt3/train_dpo.py
Depends on: `topogpt3/model.py`, `topogpt3/rewards.py`, `topogpt3/trainer_utils_topo.py`
Imported by: `topogpt3/__main__.py`
- `load_model` (function) `topogpt3/train_dpo.py:24` `def load_model(checkpoint, device)`
- `main` (function) `topogpt3/train_dpo.py:33` `def main()`

## topogpt3/train_grpo.py
Depends on: `topogpt3/model.py`, `topogpt3/rewards.py`, `topogpt3/rollout.py`, `topogpt3/trainer_utils_topo.py`
Imported by: `topogpt3/__main__.py`
- `main` (function) `topogpt3/train_grpo.py:29` `def main()`

## topogpt3/train_lora.py
Depends on: `topogpt3/lora.py`, `topogpt3/model.py`, `topogpt3/trainer_utils_topo.py`
Imported by: `topogpt3/__main__.py`
- `load_base` (function) `topogpt3/train_lora.py:25` `def load_base(checkpoint, device)`
- `main` (function) `topogpt3/train_lora.py:36` `def main()`

## topogpt3/train_ppo.py
Depends on: `topogpt3/model.py`, `topogpt3/rewards.py`, `topogpt3/rollout.py`, `topogpt3/trainer_utils_topo.py`
Imported by: `topogpt3/__main__.py`
- `TopoCritic.__init__` (method) `topogpt3/train_ppo.py:30` `def __init__(self, trunk)`
- `TopoCritic.forward` (method) `topogpt3/train_ppo.py:36` `def forward(self, ids)`
- `TopoCritic.main` (method) `topogpt3/train_ppo.py:45` `def main()`

## topogpt3/trainer_utils_topo.py
Imported by: `topogpt3/__init__.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`
- `Logger` (function) `topogpt3/trainer_utils_topo.py:20` `def Logger(content, quiet)`
- `is_main_process` (function) `topogpt3/trainer_utils_topo.py:25` `def is_main_process()`
- `get_lr` (function) `topogpt3/trainer_utils_topo.py:29` `def get_lr(current_step, total_steps, lr)`
- `setup_seed` (function) `topogpt3/trainer_utils_topo.py:34` `def setup_seed(seed)`
- `init_distributed_mode` (function) `topogpt3/trainer_utils_topo.py:43` `def init_distributed_mode()`
- `SkipBatchSampler.__init__` (method) `topogpt3/trainer_utils_topo.py:53` `def __init__(self, sampler, batch_size, skip_batches)`
- `SkipBatchSampler.topo_checkpoint` (method) `topogpt3/trainer_utils_topo.py:77` `def topo_checkpoint(save_dir, weight, model, optimizer, scheduler, scaler, epoch, step, wandb, extra)` -- Atomic double-save: fp16 weights + resume state (weights + optim).

## topogpt3/yarn.py
Imported by: `tests/test_heritage.py`, `topogpt3/__init__.py`, `topogpt3/model.py`
- `YaRNConfig.yarn_scale_inv_freq` (method) `topogpt3/yarn.py:26` `def yarn_scale_inv_freq(inv_freq, d_head, cfg)` -- Apply NTK-by-parts ramp to inv_freq.
- `YaRNConfig.apply_yarn_to_rope` (method) `topogpt3/yarn.py:50` `def apply_yarn_to_rope(rope_module, cfg)` -- Patch an existing RotaryEmbedding in-place + rebuild cache.

