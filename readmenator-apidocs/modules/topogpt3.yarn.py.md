# `topogpt3.yarn`

> Source: [topogpt3/yarn.py:1](../../topogpt3/yarn.py#L1) | language `py` | coverage 75.0% | [API index](../index.md)

YaRN RoPE extrapolation for TopoGPT3.

Preserves the quaternionic/spectral identity: only rescales the rotary
frequencies (NTK-by-parts ramp), never touches Quaternion/Torus/MoE layers.

Reference: NTK-by-parts frequency ramp with
  factor=16, orig_max=2048, beta_fast=32, beta_slow=1.

## Contents

- **Classes:** [`YaRNConfig`](#yarnconfig)
- **Functions:** [`yarn_scale_inv_freq`](#yarn_scale_inv_freq), [`apply_yarn_to_rope`](#apply_yarn_to_rope)

## Call Graph

Solid arrows stay in this module, dashed arrows leave it.

```mermaid
flowchart LR
    n_topogpt3_yarn_py__apply_yarn_to_rope(["apply_yarn_to_rope"])
    n_topogpt3_yarn_py__yarn_scale_inv_freq(["yarn_scale_inv_freq"])
    n_topogpt3_yarn_py__apply_yarn_to_rope --> n_topogpt3_yarn_py__yarn_scale_inv_freq
```

## Classes

<a id="yarnconfig"></a>

### `YaRNConfig`

`class` `dataclass` | [topogpt3/yarn.py:18](../../topogpt3/yarn.py#L18)

Decorators: `@dataclass`

```python
class YaRNConfig
```

**Attributes**

| Name | Type | Default | Description |
|---|---|---|---|
| [`factor`](#yarnconfig-factor) | `float` | `16.0` |  |
| [`orig_max`](#yarnconfig-orig_max) | `int` | `2048` |  |
| [`beta_fast`](#yarnconfig-beta_fast) | `float` | `32.0` |  |
| [`beta_slow`](#yarnconfig-beta_slow) | `float` | `1.0` |  |
| [`enabled`](#yarnconfig-enabled) | `bool` | `False` |  |

---

## Functions

<a id="yarn_scale_inv_freq"></a>

### `yarn_scale_inv_freq`

`function` | [topogpt3/yarn.py:26](../../topogpt3/yarn.py#L26)

```python
def yarn_scale_inv_freq(inv_freq: torch.Tensor, d_head: int, cfg: YaRNConfig) -> torch.Tensor
```

Apply NTK-by-parts ramp to inv_freq.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `inv_freq` | `torch.Tensor` |  |  |
| `d_head` | `int` |  |  |
| `cfg` | `YaRNConfig` |  |  |

**Returns:** `torch.Tensor`

*Called by:* [`apply_yarn_to_rope`](#apply_yarn_to_rope)

---

<a id="apply_yarn_to_rope"></a>

### `apply_yarn_to_rope`

`function` | [topogpt3/yarn.py:50](../../topogpt3/yarn.py#L50)

```python
def apply_yarn_to_rope(rope_module, cfg: YaRNConfig) -> None
```

Patch an existing RotaryEmbedding in-place + rebuild cache.

rope_module: instance of topogpt3.model.RotaryEmbedding

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `rope_module` |  |  |  |
| `cfg` | `YaRNConfig` |  |  |

*Calls:* [`yarn_scale_inv_freq`](#yarn_scale_inv_freq)

*Called by:* [`RotaryEmbedding.enable_yarn`](topogpt3.model.py.md#rotaryembedding-enable_yarn)

---
