# `topogpt3.rewards`

> Source: [topogpt3/rewards.py:1](../../topogpt3/rewards.py#L1) | language `py` | coverage 40.0% | [API index](../index.md)

Reward + advantage + loss helpers for TopoGPT3 group-RL.

Adds an *optional* spectral-coherence bonus unique to TopoGPT3 identity:
rewards answers whose generation kept Fisher gap healthy / drift bounded
(when diagnostics are supplied). Defaults to 0 so the base reward
is reproduced exactly when no geometry stats are passed.

## Contents

- **Functions:** [`rep_penalty`](#rep_penalty), [`base_rewards`](#base_rewards), [`spectral_bonus`](#spectral_bonus), [`grpo_advantages`](#grpo_advantages), [`k3_kl`](#k3_kl), [`grpo_loss`](#grpo_loss), [`logits_to_log_probs`](#logits_to_log_probs), [`dpo_loss_fn`](#dpo_loss_fn), [`distillation_loss`](#distillation_loss)

## Call Graph

Solid arrows stay in this module, dashed arrows leave it.

```mermaid
flowchart LR
    n_topogpt3_rewards_py__base_rewards(["base_rewards"])
    n_topogpt3_rewards_py__rep_penalty(["rep_penalty"])
    n_topogpt3_rewards_py__grpo_loss(["grpo_loss"])
    n_topogpt3_rewards_py__k3_kl(["k3_kl"])
    n_topogpt3_rewards_py__base_rewards --> n_topogpt3_rewards_py__rep_penalty
    n_topogpt3_rewards_py__grpo_loss --> n_topogpt3_rewards_py__k3_kl
```

## Functions

<a id="rep_penalty"></a>

### `rep_penalty`

`function` | [topogpt3/rewards.py:17](../../topogpt3/rewards.py#L17)

```python
def rep_penalty(text: str, n: int = 3, cap: float = 0.5) -> float
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `text` | `str` |  |  |
| `n` | `int` | `3` |  |
| `cap` | `float` | `0.5` |  |

**Returns:** `float`

*Called by:* [`base_rewards`](#base_rewards), [`agent_reward`](topogpt3.train_agent.py.md#agent_reward)

---

<a id="base_rewards"></a>

### `base_rewards`

`function` | [topogpt3/rewards.py:25](../../topogpt3/rewards.py#L25)

```python
def base_rewards(prompts, completions, reward_fn=None, device='cpu')
```

Group-RL reward skeleton: length + thinking + RM - repetition.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `prompts` |  |  |  |
| `completions` |  |  |  |
| `reward_fn` |  | `None` |  |
| `device` |  | `'cpu'` |  |

*Calls:* [`rep_penalty`](#rep_penalty)

*Called by:* [`main`](topogpt3.train_grpo.py.md#main), [`main`](topogpt3.train_ppo.py.md#main)

---

<a id="spectral_bonus"></a>

### `spectral_bonus`

`function` | [topogpt3/rewards.py:55](../../topogpt3/rewards.py#L55)

```python
def spectral_bonus(fisher_gap: Optional[float] = None, drift: Optional[float] = None, w_fisher: float = 0.05, w_drift: float = 0.05) -> float
```

Small bonus preserving topological identity (0 when stats absent).

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `fisher_gap` | `Optional[float]` | `None` |  |
| `drift` | `Optional[float]` | `None` |  |
| `w_fisher` | `float` | `0.05` |  |
| `w_drift` | `float` | `0.05` |  |

**Returns:** `float`

---

<a id="grpo_advantages"></a>

### `grpo_advantages`

`function` | [topogpt3/rewards.py:67](../../topogpt3/rewards.py#L67)

```python
def grpo_advantages(rewards: torch.Tensor, num_generations: int)
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `rewards` | `torch.Tensor` |  |  |
| `num_generations` | `int` |  |  |

*Called by:* [`main`](topogpt3.train_agent.py.md#main), [`main`](topogpt3.train_grpo.py.md#main)

---

<a id="k3_kl"></a>

### `k3_kl`

`function` | [topogpt3/rewards.py:74](../../topogpt3/rewards.py#L74)

```python
def k3_kl(ref_logp: torch.Tensor, new_logp: torch.Tensor)
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `ref_logp` | `torch.Tensor` |  |  |
| `new_logp` | `torch.Tensor` |  |  |

*Called by:* [`grpo_loss`](#grpo_loss), [`main`](topogpt3.train_ppo.py.md#main)

---

<a id="grpo_loss"></a>

### `grpo_loss`

`function` | [topogpt3/rewards.py:79](../../topogpt3/rewards.py#L79)

```python
def grpo_loss(new_logp, old_logp, ref_logp, adv, mask, beta=0.1, eps=0.2, loss_type='cispo', eps_high=5.0)
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `new_logp` |  |  |  |
| `old_logp` |  |  |  |
| `ref_logp` |  |  |  |
| `adv` |  |  |  |
| `mask` |  |  |  |
| `beta` |  | `0.1` |  |
| `eps` |  | `0.2` |  |
| `loss_type` |  | `'cispo'` |  |
| `eps_high` |  | `5.0` |  |

*Calls:* [`k3_kl`](#k3_kl)

*Called by:* [`main`](topogpt3.train_agent.py.md#main), [`main`](topogpt3.train_grpo.py.md#main)

---

<a id="logits_to_log_probs"></a>

### `logits_to_log_probs`

`function` | [topogpt3/rewards.py:94](../../topogpt3/rewards.py#L94)

```python
def logits_to_log_probs(logits: torch.Tensor, labels: torch.Tensor)
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `logits` | `torch.Tensor` |  |  |
| `labels` | `torch.Tensor` |  |  |

*Called by:* [`main`](topogpt3.train_dpo.py.md#main)

---

<a id="dpo_loss_fn"></a>

### `dpo_loss_fn`

`function` | [topogpt3/rewards.py:99](../../topogpt3/rewards.py#L99)

```python
def dpo_loss_fn(ref_lp, pol_lp, mask, beta=0.15)
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `ref_lp` |  |  |  |
| `pol_lp` |  |  |  |
| `mask` |  |  |  |
| `beta` |  | `0.15` |  |

*Called by:* [`main`](topogpt3.train_dpo.py.md#main)

---

<a id="distillation_loss"></a>

### `distillation_loss`

`function` | [topogpt3/rewards.py:108](../../topogpt3/rewards.py#L108)

```python
def distillation_loss(student_logits, teacher_logits, mask, labels=None, alpha: float = 0.5, temp: float = 1.5)
```

White-box distill: CE + T^2*KL on masked response tokens.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `student_logits` |  |  |  |
| `teacher_logits` |  |  |  |
| `mask` |  |  |  |
| `labels` |  | `None` |  |
| `alpha` | `float` | `0.5` |  |
| `temp` | `float` | `1.5` |  |

*Called by:* [`main`](topogpt3.train_distill.py.md#main)

---
