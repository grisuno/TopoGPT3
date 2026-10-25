# `topogpt3.train_dpo`

> Source: [topogpt3/train_dpo.py:1](../../topogpt3/train_dpo.py#L1) | language `py` | coverage 33.3% | [API index](../index.md)

DPO for TopoGPT3.

Policy + frozen ref share TopoGPT2 quaternion/spectral weights; only preference direction is learned.

## Contents

- **Functions:** [`load_model`](#load_model), [`main`](#main)

## Call Graph

Solid arrows stay in this module, dashed arrows leave it.

```mermaid
flowchart LR
    n_topogpt3_train_dpo_py__main(["main"])
    n_topogpt3_train_dpo_py__load_model(["load_model"])
    n_topogpt3_checkpoint_meta_py__config_from_checkpoint["checkpoint_meta.config_from_checkpoint"]
    n_topogpt3_model_py__TopoGPT2___init__["model.TopoGPT2.__init__"]
    n_topogpt3_model_py__TopoGPT2Config["model.TopoGPT2Config"]
    n_topogpt3_model_py__BPETokenizer___init__["model.BPETokenizer.__init__"]
    n_topogpt3_model_py__CurriculumTrainer_model["model.CurriculumTrainer.model"]
    n_topogpt3_rewards_py__dpo_loss_fn["rewards.dpo_loss_fn"]
    n_topogpt3_rewards_py__logits_to_log_probs["rewards.logits_to_log_probs"]
    n_topogpt3_trainer_utils_topo_py__Logger["trainer_utils_topo.Logger"]
    n_topogpt3_trainer_utils_topo_py__get_lr["trainer_utils_topo.get_lr"]
    n_topogpt3_trainer_utils_topo_py__init_distributed_mode["trainer_utils_topo.init_distributed_mode"]
    n_topogpt3_trainer_utils_topo_py__is_main_process["trainer_utils_topo.is_main_process"]
    n_topogpt3_trainer_utils_topo_py__setup_seed["trainer_utils_topo.setup_seed"]
    n_topogpt3_trainer_utils_topo_py__topo_checkpoint["trainer_utils_topo.topo_checkpoint"]
    n_topogpt3_train_dpo_py__main --> n_topogpt3_train_dpo_py__load_model
    n_topogpt3_train_dpo_py__load_model -.-> n_topogpt3_checkpoint_meta_py__config_from_checkpoint
    n_topogpt3_train_dpo_py__load_model -.-> n_topogpt3_model_py__TopoGPT2___init__
    n_topogpt3_train_dpo_py__load_model -.-> n_topogpt3_model_py__TopoGPT2Config
    n_topogpt3_train_dpo_py__main -.-> n_topogpt3_model_py__BPETokenizer___init__
    n_topogpt3_train_dpo_py__main -.-> n_topogpt3_model_py__CurriculumTrainer_model
    n_topogpt3_train_dpo_py__main -.-> n_topogpt3_rewards_py__dpo_loss_fn
    n_topogpt3_train_dpo_py__main -.-> n_topogpt3_rewards_py__logits_to_log_probs
    n_topogpt3_train_dpo_py__main -.-> n_topogpt3_trainer_utils_topo_py__Logger
    n_topogpt3_train_dpo_py__main -.-> n_topogpt3_trainer_utils_topo_py__get_lr
    n_topogpt3_train_dpo_py__main -.-> n_topogpt3_trainer_utils_topo_py__init_distributed_mode
    n_topogpt3_train_dpo_py__main -.-> n_topogpt3_trainer_utils_topo_py__is_main_process
    n_topogpt3_train_dpo_py__main -.-> n_topogpt3_trainer_utils_topo_py__setup_seed
    n_topogpt3_train_dpo_py__main -.-> n_topogpt3_trainer_utils_topo_py__topo_checkpoint
```

## Functions

<a id="load_model"></a>

### `load_model`

`function` | [topogpt3/train_dpo.py:31](../../topogpt3/train_dpo.py#L31)

```python
def load_model(checkpoint, device)
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `checkpoint` |  |  |  |
| `device` |  |  |  |

*Calls:* [`config_from_checkpoint`](topogpt3.checkpoint_meta.py.md#config_from_checkpoint), [`TopoGPT2.__init__`](topogpt3.model.py.md#topogpt2-__init__), [`TopoGPT2Config`](topogpt3.model.py.md#topogpt2config)

*Called by:* [`main`](#main)

---

<a id="main"></a>

### `main`

`function` | [topogpt3/train_dpo.py:43](../../topogpt3/train_dpo.py#L43)

```python
def main()
```

*Calls:* [`BPETokenizer.__init__`](topogpt3.model.py.md#bpetokenizer-__init__), [`CurriculumTrainer.model`](topogpt3.model.py.md#curriculumtrainer-model), [`dpo_loss_fn`](topogpt3.rewards.py.md#dpo_loss_fn), [`logits_to_log_probs`](topogpt3.rewards.py.md#logits_to_log_probs), [`load_model`](#load_model), [`Logger`](topogpt3.trainer_utils_topo.py.md#logger), [`get_lr`](topogpt3.trainer_utils_topo.py.md#get_lr), [`init_distributed_mode`](topogpt3.trainer_utils_topo.py.md#init_distributed_mode), [`is_main_process`](topogpt3.trainer_utils_topo.py.md#is_main_process), [`setup_seed`](topogpt3.trainer_utils_topo.py.md#setup_seed), [`topo_checkpoint`](topogpt3.trainer_utils_topo.py.md#topo_checkpoint)

---
