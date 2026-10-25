# `topogpt3.eval_toolcall`

> Source: [topogpt3/eval_toolcall.py:1](../../topogpt3/eval_toolcall.py#L1) | language `py` | coverage 33.3% | [API index](../index.md)

Tool-call evaluation for TopoGPT3 agents.

Runs TOOLS cases through a generate_fn and checks name/args parsing.

## Contents

- **Functions:** [`run_case`](#run_case), [`evaluate`](#evaluate)
- **Constants:** [`CASES`](#cases)

## Call Graph

Solid arrows stay in this module, dashed arrows leave it.

```mermaid
flowchart LR
    n_topogpt3_eval_toolcall_py__evaluate(["evaluate"])
    n_topogpt3_eval_toolcall_py__run_case(["run_case"])
    n_topogpt3_chat_py__apply_chat_template["chat.apply_chat_template"]
    n_topogpt3_chat_py__parse_tool_calls["chat.parse_tool_calls"]
    n_topogpt3_tools_agent_py__execute_tool["tools_agent.execute_tool"]
    n_topogpt3_eval_toolcall_py__evaluate --> n_topogpt3_eval_toolcall_py__run_case
    n_topogpt3_eval_toolcall_py__run_case -.-> n_topogpt3_chat_py__apply_chat_template
    n_topogpt3_eval_toolcall_py__run_case -.-> n_topogpt3_chat_py__parse_tool_calls
    n_topogpt3_eval_toolcall_py__run_case -.-> n_topogpt3_tools_agent_py__execute_tool
```

## Functions

<a id="run_case"></a>

### `run_case`

`function` | [topogpt3/eval_toolcall.py:19](../../topogpt3/eval_toolcall.py#L19)

```python
def run_case(generate_fn, prompt: str, expect_tool: str)
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `generate_fn` |  |  |  |
| `prompt` | `str` |  |  |
| `expect_tool` | `str` |  |  |

*Calls:* [`apply_chat_template`](topogpt3.chat.py.md#apply_chat_template), [`parse_tool_calls`](topogpt3.chat.py.md#parse_tool_calls), [`execute_tool`](topogpt3.tools_agent.py.md#execute_tool)

*Called by:* [`evaluate`](#evaluate)

---

<a id="evaluate"></a>

### `evaluate`

`function` | [topogpt3/eval_toolcall.py:35](../../topogpt3/eval_toolcall.py#L35)

```python
def evaluate(generate_fn)
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `generate_fn` |  |  |  |

*Calls:* [`run_case`](#run_case)

---

## Constants

<a id="cases"></a>

### `CASES`

`constant` | [topogpt3/eval_toolcall.py:11](../../topogpt3/eval_toolcall.py#L11)

```python
CASES
```

---
