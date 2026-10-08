# topogpt3: lora

*Community 0 | 12 files | cohesion 0.49*

## Definition

This community groups 12 file(s) rooted at `topogpt3` with dominant language py (cohesion 0.49). Central symbols: `LoRA`, `Logger`, `RolloutEngine`, `RolloutResult`, `SkipBatchSampler`, `TopoCritic`, `TorchRolloutEngine`, `__init__`. Core file: `topogpt3/lora.py` (12 symbols). Documented purpose: Export / convert utilities for TopoGPT3 checkpoints.  TopoGPT3 keeps its own safetensors slot; this adds: - merge_lora CLI (base + LoRA -> merged safetensors di.

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `topogpt3/__main__.py` | py | utility | 1 | no |
| `topogpt3/convert.py` | py | utility | 3 | yes |
| `topogpt3/lora.py` | py | utility | 12 | yes |
| `topogpt3/rewards.py` | py | utility | 9 | yes |
| `topogpt3/rollout.py` | py | utility | 10 | yes |
| `topogpt3/train_agent.py` | py | utility | 2 | yes |
| `topogpt3/train_distill.py` | py | utility | 1 | yes |
| `topogpt3/train_dpo.py` | py | utility | 2 | yes |
| `topogpt3/train_grpo.py` | py | utility | 2 | yes |
| `topogpt3/train_lora.py` | py | utility | 2 | yes |
| `topogpt3/train_ppo.py` | py | utility | 4 | yes |
| `topogpt3/trainer_utils_topo.py` | py | utility | 10 | yes |

## Key Symbols

- `main` (function, `topogpt3/__main__.py:6`) `def main()` - TopoGPT3 entry point. Delegates to subcommands.
- `merge_base_lora` (function, `topogpt3/convert.py:19`) `def merge_base_lora(base_dir, lora_path, out_dir)`
- `export_hf_stub` (function, `topogpt3/convert.py:38`) `def export_hf_stub(ckpt_dir, out_dir)`
- `main` (function, `topogpt3/convert.py:49`) `def main()`
- `LoRA` (class, `topogpt3/lora.py:16`) `class LoRA(Module)`
- `__init__` (method, `topogpt3/lora.py:17`) `def __init__(self, in_features, out_features, rank)`
- `forward` (method, `topogpt3/lora.py:25`) `def forward(self, x)`
- `_is_quaternion_sublayer` (method, `topogpt3/lora.py:29`) `def _is_quaternion_sublayer(name)`
- `lora_targets` (method, `topogpt3/lora.py:34`) `def lora_targets(model, include_mlp)` - Yield (name, nn.Linear) candidates.
- `apply_lora` (method, `topogpt3/lora.py:54`) `def apply_lora(model, rank, include_mlp)` - Monkey-patch target linears with additive LoRA. Returns patched names.
- `_fwd` (method, `topogpt3/lora.py:66`) `def _fwd(x, _o, _l)`
- `lora_parameters` (method, `topogpt3/lora.py:73`) `def lora_parameters(model)`
- `freeze_non_lora` (method, `topogpt3/lora.py:80`) `def freeze_non_lora(model)`
- `save_lora` (method, `topogpt3/lora.py:88`) `def save_lora(model, path)`
- `load_lora` (method, `topogpt3/lora.py:99`) `def load_lora(model, path, device)`
- `merge_lora` (method, `topogpt3/lora.py:110`) `def merge_lora(model, lora_path, save_path)` - Merge LoRA deltas into base weights and save (fp16, no .lora. keys).
- `rep_penalty` (function, `topogpt3/rewards.py:17`) `def rep_penalty(text, n, cap)`
- `base_rewards` (function, `topogpt3/rewards.py:25`) `def base_rewards(prompts, completions, reward_fn, device)` - Group-RL reward skeleton: length + thinking + RM - repetition.
- `spectral_bonus` (function, `topogpt3/rewards.py:55`) `def spectral_bonus(fisher_gap, drift, w_fisher, w_drift)` - Small bonus preserving topological identity (0 when stats absent).
- `grpo_advantages` (function, `topogpt3/rewards.py:67`) `def grpo_advantages(rewards, num_generations)`
- `k3_kl` (function, `topogpt3/rewards.py:74`) `def k3_kl(ref_logp, new_logp)`
- `grpo_loss` (function, `topogpt3/rewards.py:79`) `def grpo_loss(new_logp, old_logp, ref_logp, adv, mask, beta, eps, loss_type, eps`
- `logits_to_log_probs` (function, `topogpt3/rewards.py:94`) `def logits_to_log_probs(logits, labels)`
- `dpo_loss_fn` (function, `topogpt3/rewards.py:99`) `def dpo_loss_fn(ref_lp, pol_lp, mask, beta)`
- `distillation_loss` (function, `topogpt3/rewards.py:108`) `def distillation_loss(student_logits, teacher_logits, mask, labels, alpha, temp)` - White-box distill: CE + T^2*KL on masked response tokens.
- `RolloutResult` (class, `topogpt3/rollout.py:18`) `class RolloutResult`
- `compute_per_token_logps` (method, `topogpt3/rollout.py:27`) `def compute_per_token_logps(model, input_ids, n_keep)`
- `RolloutEngine` (class, `topogpt3/rollout.py:39`) `class RolloutEngine(ABC)`
- `rollout` (method, `topogpt3/rollout.py:41`) `def rollout(self, prompt_ids, num_generations, max_new_tokens, temperature, toke`
- `update_policy` (method, `topogpt3/rollout.py:46`) `def update_policy(self, model)`

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 22
- Cross-boundary resolved imports (EXTRACTED): 23

## Connections

- [EXTRACTED] depends_on community 3 <-> 0 (strength 0.9): Extracted import edge crosses communities: tests/test_heritage.py imports topogpt3/lora.py.
- [EXTRACTED] depends_on community 1 <-> 0 (strength 0.9): Extracted import edge crosses communities: topogpt3/__init__.py imports topogpt3/lora.py.
- [EXTRACTED] depends_on community 0 <-> 4 (strength 0.9): Extracted import edge crosses communities: topogpt3/__main__.py imports topogpt3/jlens.py.
- [EXTRACTED] depends_on community 0 <-> 2 (strength 0.9): Extracted import edge crosses communities: topogpt3/__main__.py imports topogpt3/api_server.py.
- [INFERRED] shares_context community 0 <-> 5 (strength 0.5): Inferred shared context (language py and layer utility) with no import path between community 0 (topogpt3: lora) and community 5 (root).
- [INFERRED] shares_context community 0 <-> 6 (strength 0.5): Inferred shared context (language py and layer utility) with no import path between community 0 (topogpt3: lora) and community 6 (orphans).

## Risks

- [taint critical] `eval/governor_smoke.py` -> `topogpt3/rewards.py` via `eval` (2 hops)
- [taint critical] `eval/governor_smoke.py` -> `topogpt3/trainer_utils_topo.py` via `eval` (2 hops)
- [taint critical] `eval/governor_smoke.py` -> `topogpt3/lora.py` via `eval` (2 hops)
- [taint critical] `eval/governor_smoke.py` -> `topogpt3/rollout.py` via `eval` (2 hops)

## Open Questions

- Why do 1 file(s) lack file-level docs (e.g. `topogpt3/__main__.py`)? What purpose do they serve?
- What would break if the most connected file in topogpt3: lora changed?
- Should topogpt3: lora be split, given cohesion 0.49?

## Sources

- `topogpt3/__main__.py`
- `topogpt3/convert.py`
- `topogpt3/lora.py`
- `topogpt3/rewards.py`
- `topogpt3/rollout.py`
- `topogpt3/train_agent.py`
- `topogpt3/train_distill.py`
- `topogpt3/train_dpo.py`
- `topogpt3/train_grpo.py`
- `topogpt3/train_lora.py`
- `topogpt3/train_ppo.py`
- `topogpt3/trainer_utils_topo.py`
