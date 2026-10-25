# `topogpt3.train_ppo`

> Source: [topogpt3/train_ppo.py:1](../../topogpt3/train_ppo.py#L1) | language `py` | coverage 20.0% | [API index](../index.md)

PPO for TopoGPT3.

Critic = frozen TopoGPT2 trunk + fresh Linear value head (quaternion trunk
untouched by value gradients except through shared trunk).
GAE + clipped actor + clipped value + k3 KL to ref.

## Contents

- **Classes:** [`TopoCritic`](#topocritic)
- **Functions:** [`main`](#main)

## Type Diagram

```mermaid
classDiagram
    direction LR
    class TopoCritic
    TopoCritic : __init__()
    TopoCritic : forward()
```

## Call Graph

Solid arrows stay in this module, dashed arrows leave it.

```mermaid
flowchart LR
    n_topogpt3_train_ppo_py__main(["main"])
    n_topogpt3_train_ppo_py__TopoCritic___init__(["TopoCritic.__init__"])
    n_topogpt3_model_py__BPETokenizer___init__["model.BPETokenizer.__init__"]
    n_topogpt3_model_py__BPETokenizer_decode["model.BPETokenizer.decode"]
    n_topogpt3_model_py__BPETokenizer_encode["model.BPETokenizer.encode"]
    n_topogpt3_model_py__TopoGPT2___init__["model.TopoGPT2.__init__"]
    n_topogpt3_model_py__TopoGPT2Config["model.TopoGPT2Config"]
    n_topogpt3_rewards_py__base_rewards["rewards.base_rewards"]
    n_topogpt3_rewards_py__k3_kl["rewards.k3_kl"]
    n_topogpt3_rollout_py__create_rollout_engine["rollout.create_rollout_engine"]
    n_topogpt3_trainer_utils_topo_py__Logger["trainer_utils_topo.Logger"]
    n_topogpt3_trainer_utils_topo_py__is_main_process["trainer_utils_topo.is_main_process"]
    n_topogpt3_trainer_utils_topo_py__setup_seed["trainer_utils_topo.setup_seed"]
    n_topogpt3_train_ppo_py__main --> n_topogpt3_train_ppo_py__TopoCritic___init__
    n_topogpt3_train_ppo_py__main -.-> n_topogpt3_model_py__BPETokenizer___init__
    n_topogpt3_train_ppo_py__main -.-> n_topogpt3_model_py__BPETokenizer_decode
    n_topogpt3_train_ppo_py__main -.-> n_topogpt3_model_py__BPETokenizer_encode
    n_topogpt3_train_ppo_py__main -.-> n_topogpt3_model_py__TopoGPT2___init__
    n_topogpt3_train_ppo_py__main -.-> n_topogpt3_model_py__TopoGPT2Config
    n_topogpt3_train_ppo_py__main -.-> n_topogpt3_rewards_py__base_rewards
    n_topogpt3_train_ppo_py__main -.-> n_topogpt3_rewards_py__k3_kl
    n_topogpt3_train_ppo_py__main -.-> n_topogpt3_rollout_py__create_rollout_engine
    n_topogpt3_train_ppo_py__main -.-> n_topogpt3_trainer_utils_topo_py__Logger
    n_topogpt3_train_ppo_py__main -.-> n_topogpt3_trainer_utils_topo_py__is_main_process
    n_topogpt3_train_ppo_py__main -.-> n_topogpt3_trainer_utils_topo_py__setup_seed
```

## Classes

<a id="topocritic"></a>

### `TopoCritic`

`class` | [topogpt3/train_ppo.py:29](../../topogpt3/train_ppo.py#L29)

```python
class TopoCritic(nn.Module)
```

Bases: `nn.Module`

**Members**

| Member | Kind | Summary |
|---|---|---|
| [`__init__`](#topocritic-__init__) | constructor |  |
| [`forward`](#topocritic-forward) | method |  |

<a id="topocritic-__init__"></a>

#### `TopoCritic.__init__`

`constructor` | [topogpt3/train_ppo.py:30](../../topogpt3/train_ppo.py#L30)

```python
def __init__(self, trunk: TopoGPT2)
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `trunk` | `TopoGPT2` |  |  |

*Called by:* [`main`](#main)

<a id="topocritic-forward"></a>

#### `TopoCritic.forward`

`method` | [topogpt3/train_ppo.py:36](../../topogpt3/train_ppo.py#L36)

```python
def forward(self, ids)
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `ids` |  |  |  |

---

## Functions

<a id="main"></a>

### `main`

`function` | [topogpt3/train_ppo.py:45](../../topogpt3/train_ppo.py#L45)

```python
def main()
```

*Calls:* [`BPETokenizer.__init__`](topogpt3.model.py.md#bpetokenizer-__init__), [`BPETokenizer.decode`](topogpt3.model.py.md#bpetokenizer-decode), [`BPETokenizer.encode`](topogpt3.model.py.md#bpetokenizer-encode), [`TopoGPT2.__init__`](topogpt3.model.py.md#topogpt2-__init__), [`TopoGPT2Config`](topogpt3.model.py.md#topogpt2config), [`base_rewards`](topogpt3.rewards.py.md#base_rewards), [`k3_kl`](topogpt3.rewards.py.md#k3_kl), [`create_rollout_engine`](topogpt3.rollout.py.md#create_rollout_engine), [`TopoCritic.__init__`](#topocritic-__init__), [`Logger`](topogpt3.trainer_utils_topo.py.md#logger), [`is_main_process`](topogpt3.trainer_utils_topo.py.md#is_main_process), [`setup_seed`](topogpt3.trainer_utils_topo.py.md#setup_seed)

---
