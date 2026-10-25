# `topogpt3.continuation`

> Source: [topogpt3/continuation.py:1](../../topogpt3/continuation.py#L1) | language `py` | coverage 100.0% | [API index](../index.md)

Auto-continuation engine: detects truncated responses and feeds the last incomplete lines back so the model can resume where it left off.

Used by both the standard inference pipeline and the HRM "thinking" mode.

## Contents

- **Functions:** [`is_response_complete`](#is_response_complete), [`extract_tail_for_continuation`](#extract_tail_for_continuation), [`split_at_last_newline`](#split_at_last_newline)

## Functions

<a id="is_response_complete"></a>

### `is_response_complete`

`function` | [topogpt3/continuation.py:45](../../topogpt3/continuation.py#L45)

```python
def is_response_complete(text: str, min_chars: int = 10) -> bool
```

Heuristic to decide whether a model response looks finished.

Returns True when the response seems naturally complete (no need to
continue), False when it appears truncated and continuation may help.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `text` | `str` |  |  |
| `min_chars` | `int` | `10` |  |

**Returns:** `bool`

*Called by:* [`ServerModel.stream_complete`](topogpt3.api_server.py.md#servermodel-stream_complete), [`HRMGenerationEngine.run`](topogpt3.inference_hrm.py.md#hrmgenerationengine-run), [`TopoGPT2.generate_with_continuation`](topogpt3.model.py.md#topogpt2-generate_with_continuation)

---

<a id="extract_tail_for_continuation"></a>

### `extract_tail_for_continuation`

`function` | [topogpt3/continuation.py:75](../../topogpt3/continuation.py#L75)

```python
def extract_tail_for_continuation(text: str, tail_lines: int = 2, tail_chars: int = 512) -> str
```

Return the last N lines (or up to tail_chars) of `text` as a continuation prefix to feed back into the model.

The returned string can be prepended as context for the model's next
generation call so it continues naturally from that point.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `text` | `str` |  |  |
| `tail_lines` | `int` | `2` |  |
| `tail_chars` | `int` | `512` |  |

**Returns:** `str`

*Called by:* [`ServerModel.stream_complete`](topogpt3.api_server.py.md#servermodel-stream_complete), [`HRMGenerationEngine.run`](topogpt3.inference_hrm.py.md#hrmgenerationengine-run), [`TopoGPT2.generate_with_continuation`](topogpt3.model.py.md#topogpt2-generate_with_continuation)

---

<a id="split_at_last_newline"></a>

### `split_at_last_newline`

`function` | [topogpt3/continuation.py:105](../../topogpt3/continuation.py#L105)

```python
def split_at_last_newline(text: str) -> Tuple[str, str]
```

Split `text` at the last newline.

Returns (prefix_without_last_line, last_line).
Useful for discarding a trailing incomplete line before continuation.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `text` | `str` |  |  |

**Returns:** `Tuple[str, str]`

---
