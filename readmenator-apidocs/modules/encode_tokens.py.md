# `encode_tokens`

> Source: [encode_tokens.py:1](../../encode_tokens.py#L1) | language `py` | coverage 50.0% | [API index](../index.md)

Tokenize text using GPT-2 BPE and output binary token IDs.

Usage:
    python tokenize.py "text to tokenize" -o tokens.bin
    echo "text" | python tokenize.py - -o tokens.bin
    python tokenize.py -f input.txt -o tokens.bin

The binary format is:
    4 bytes: magic "TKID"
    4 bytes: number of tokens (uint32 LE)
    N * 4 bytes: token IDs (int32 LE)

## Contents

- **Functions:** [`main`](#main)

## Functions

<a id="main"></a>

### `main`

`function` | [encode_tokens.py:19](../../encode_tokens.py#L19)

```python
def main()
```

---
