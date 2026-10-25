# `convert_weights_minios`

> Source: [convert_weights_minios.py:1](../../convert_weights_minios.py#L1) | language `py` | coverage 50.0% | [API index](../index.md)

Convert TopoGPT3 safetensors weights to float16 binary for MiniOS.

Produces a compact weight file (~47MB vs 94MB float32) that fits on MiniFS.
The C engine loads float16 and converts to float32 on the fly.

Usage:
    python convert_weights_minios.py -i checkpoint.safetensors -o topogpt3.fp16

Binary format (TG16):
    4 bytes: magic "TG16"
    4 bytes: version (2)
    4 bytes: number of tensors
    For each tensor:
        4 bytes: name length
        N bytes: name (UTF-8)
        4 bytes: ndim
        4 bytes × ndim: dimensions
        2 bytes × total_elements: float16 data (little-endian IEEE 754)

## Contents

- **Functions:** [`main`](#main)
- **Constants:** [`WEIGHT_ORDER`](#weight_order)

## Functions

<a id="main"></a>

### `main`

`function` | [convert_weights_minios.py:85](../../convert_weights_minios.py#L85)

```python
def main()
```

---

## Constants

<a id="weight_order"></a>

### `WEIGHT_ORDER`

`constant` | [convert_weights_minios.py:34](../../convert_weights_minios.py#L34)

```python
WEIGHT_ORDER = ['token_embed.weight']
```

---
