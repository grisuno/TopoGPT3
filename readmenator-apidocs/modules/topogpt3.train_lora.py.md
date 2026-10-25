# `topogpt3.train_lora`

> Source: [topogpt3/train_lora.py:1](../../topogpt3/train_lora.py#L1) | language `py` | coverage 33.3% | [API index](../index.md)

SFT with native LoRA for TopoGPT3.

Freezes quaternion/spectral base, trains only LoRA deltas. DDP + AMP ready.

## Contents

- **Functions:** [`load_base`](#load_base), [`main`](#main)

## Call Graph

Solid arrows stay in this module, dashed arrows leave it.

```mermaid
flowchart LR
    n_topogpt3_train_lora_py__main(["main"])
    n_topogpt3_train_lora_py__load_base(["load_base"])
    n_topogpt3_model_py__TopoGPT2___init__["model.TopoGPT2.__init__"]
    n_topogpt3_model_py__TopoGPT2Config["model.TopoGPT2Config"]
    n_topogpt3_trainer_utils_topo_py__Logger["trainer_utils_topo.Logger"]
    n_topogpt3_lora_py__apply_lora["lora.apply_lora"]
    n_topogpt3_lora_py__freeze_non_lora["lora.freeze_non_lora"]
    n_topogpt3_lora_py__lora_parameters["lora.lora_parameters"]
    n_topogpt3_lora_py__save_lora["lora.save_lora"]
    n_topogpt3_model_py__BPETokenizer___init__["model.BPETokenizer.__init__"]
    n_topogpt3_trainer_utils_topo_py__get_lr["trainer_utils_topo.get_lr"]
    n_topogpt3_trainer_utils_topo_py__init_distributed_mode["trainer_utils_topo.init_distributed_mode"]
    n_topogpt3_trainer_utils_topo_py__is_main_process["trainer_utils_topo.is_main_process"]
    n_topogpt3_trainer_utils_topo_py__setup_seed["trainer_utils_topo.setup_seed"]
    n_topogpt3_train_lora_py__main --> n_topogpt3_train_lora_py__load_base
    n_topogpt3_train_lora_py__load_base -.-> n_topogpt3_model_py__TopoGPT2___init__
    n_topogpt3_train_lora_py__load_base -.-> n_topogpt3_model_py__TopoGPT2Config
    n_topogpt3_train_lora_py__load_base -.-> n_topogpt3_trainer_utils_topo_py__Logger
    n_topogpt3_train_lora_py__main -.-> n_topogpt3_lora_py__apply_lora
    n_topogpt3_train_lora_py__main -.-> n_topogpt3_lora_py__freeze_non_lora
    n_topogpt3_train_lora_py__main -.-> n_topogpt3_lora_py__lora_parameters
    n_topogpt3_train_lora_py__main -.-> n_topogpt3_lora_py__save_lora
    n_topogpt3_train_lora_py__main -.-> n_topogpt3_model_py__BPETokenizer___init__
    n_topogpt3_train_lora_py__main -.-> n_topogpt3_trainer_utils_topo_py__Logger
    n_topogpt3_train_lora_py__main -.-> n_topogpt3_trainer_utils_topo_py__get_lr
    n_topogpt3_train_lora_py__main -.-> n_topogpt3_trainer_utils_topo_py__init_distributed_mode
    n_topogpt3_train_lora_py__main -.-> n_topogpt3_trainer_utils_topo_py__is_main_process
    n_topogpt3_train_lora_py__main -.-> n_topogpt3_trainer_utils_topo_py__setup_seed
```

## Functions

<a id="load_base"></a>

### `load_base`

`function` | [topogpt3/train_lora.py:25](../../topogpt3/train_lora.py#L25)

```python
def load_base(checkpoint: str, device: str)
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `checkpoint` | `str` |  |  |
| `device` | `str` |  |  |

*Calls:* [`TopoGPT2.__init__`](topogpt3.model.py.md#topogpt2-__init__), [`TopoGPT2Config`](topogpt3.model.py.md#topogpt2config), [`Logger`](topogpt3.trainer_utils_topo.py.md#logger)

*Called by:* [`main`](#main)

---

<a id="main"></a>

### `main`

`function` | [topogpt3/train_lora.py:36](../../topogpt3/train_lora.py#L36)

```python
def main()
```

*Calls:* [`apply_lora`](topogpt3.lora.py.md#apply_lora), [`freeze_non_lora`](topogpt3.lora.py.md#freeze_non_lora), [`lora_parameters`](topogpt3.lora.py.md#lora_parameters), [`save_lora`](topogpt3.lora.py.md#save_lora), [`BPETokenizer.__init__`](topogpt3.model.py.md#bpetokenizer-__init__), [`load_base`](#load_base), [`Logger`](topogpt3.trainer_utils_topo.py.md#logger), [`get_lr`](topogpt3.trainer_utils_topo.py.md#get_lr), [`init_distributed_mode`](topogpt3.trainer_utils_topo.py.md#init_distributed_mode), [`is_main_process`](topogpt3.trainer_utils_topo.py.md#is_main_process), [`setup_seed`](topogpt3.trainer_utils_topo.py.md#setup_seed)

---
