# `topogpt3.train_agent`

> Source: [topogpt3/train_agent.py:1](../../topogpt3/train_agent.py#L1) | language `py` | coverage 33.3% | [API index](../index.md)

Agentic RL for TopoGPT3 (multi-turn Tool-Use).

Rollout: prompt -> generate -> parse <tool_call> -> execute (run_python
sandbox + mock tools) -> append <tool_response> -> repeat (max_turns=3).
Reward: tool use + completion - repetition.
Loss: same GRPO/CISPO as train_grpo (no Critic -> quaternion-safe).
Observations (tool outputs) are masked out of the policy loss.

## Contents

- **Functions:** [`agent_reward`](#agent_reward), [`main`](#main)

## Call Graph

Solid arrows stay in this module, dashed arrows leave it.

```mermaid
flowchart LR
    n_topogpt3_train_agent_py__main(["main"])
    n_topogpt3_train_agent_py__agent_reward(["agent_reward"])
    n_topogpt3_rewards_py__rep_penalty["rewards.rep_penalty"]
    n_topogpt3_chat_py__apply_chat_template["chat.apply_chat_template"]
    n_topogpt3_chat_py__parse_tool_calls["chat.parse_tool_calls"]
    n_topogpt3_model_py__BPETokenizer___init__["model.BPETokenizer.__init__"]
    n_topogpt3_model_py__BPETokenizer_decode["model.BPETokenizer.decode"]
    n_topogpt3_model_py__BPETokenizer_encode["model.BPETokenizer.encode"]
    n_topogpt3_model_py__CurriculumTrainer_model["model.CurriculumTrainer.model"]
    n_topogpt3_model_py__TopoGPT2___init__["model.TopoGPT2.__init__"]
    n_topogpt3_model_py__TopoGPT2_generate["model.TopoGPT2.generate"]
    n_topogpt3_model_py__TopoGPT2Config["model.TopoGPT2Config"]
    n_topogpt3_rewards_py__grpo_advantages["rewards.grpo_advantages"]
    n_topogpt3_rewards_py__grpo_loss["rewards.grpo_loss"]
    n_topogpt3_tools_agent_py__execute_tool["tools_agent.execute_tool"]
    n_topogpt3_trainer_utils_topo_py__Logger["trainer_utils_topo.Logger"]
    n_topogpt3_trainer_utils_topo_py__is_main_process["trainer_utils_topo.is_main_process"]
    n_topogpt3_trainer_utils_topo_py__setup_seed["trainer_utils_topo.setup_seed"]
    n_topogpt3_train_agent_py__main --> n_topogpt3_train_agent_py__agent_reward
    n_topogpt3_train_agent_py__agent_reward -.-> n_topogpt3_rewards_py__rep_penalty
    n_topogpt3_train_agent_py__main -.-> n_topogpt3_chat_py__apply_chat_template
    n_topogpt3_train_agent_py__main -.-> n_topogpt3_chat_py__parse_tool_calls
    n_topogpt3_train_agent_py__main -.-> n_topogpt3_model_py__BPETokenizer___init__
    n_topogpt3_train_agent_py__main -.-> n_topogpt3_model_py__BPETokenizer_decode
    n_topogpt3_train_agent_py__main -.-> n_topogpt3_model_py__BPETokenizer_encode
    n_topogpt3_train_agent_py__main -.-> n_topogpt3_model_py__CurriculumTrainer_model
    n_topogpt3_train_agent_py__main -.-> n_topogpt3_model_py__TopoGPT2___init__
    n_topogpt3_train_agent_py__main -.-> n_topogpt3_model_py__TopoGPT2_generate
    n_topogpt3_train_agent_py__main -.-> n_topogpt3_model_py__TopoGPT2Config
    n_topogpt3_train_agent_py__main -.-> n_topogpt3_rewards_py__grpo_advantages
    n_topogpt3_train_agent_py__main -.-> n_topogpt3_rewards_py__grpo_loss
    n_topogpt3_train_agent_py__main -.-> n_topogpt3_tools_agent_py__execute_tool
    n_topogpt3_train_agent_py__main -.-> n_topogpt3_trainer_utils_topo_py__Logger
    n_topogpt3_train_agent_py__main -.-> n_topogpt3_trainer_utils_topo_py__is_main_process
    n_topogpt3_train_agent_py__main -.-> n_topogpt3_trainer_utils_topo_py__setup_seed
```

## Functions

<a id="agent_reward"></a>

### `agent_reward`

`function` | [topogpt3/train_agent.py:31](../../topogpt3/train_agent.py#L31)

```python
def agent_reward(text: str, gt: str, used_tools: bool) -> float
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `text` | `str` |  |  |
| `gt` | `str` |  |  |
| `used_tools` | `bool` |  |  |

**Returns:** `float`

*Calls:* [`rep_penalty`](topogpt3.rewards.py.md#rep_penalty)

*Called by:* [`main`](#main)

---

<a id="main"></a>

### `main`

`function` | [topogpt3/train_agent.py:43](../../topogpt3/train_agent.py#L43)

```python
def main()
```

*Calls:* [`apply_chat_template`](topogpt3.chat.py.md#apply_chat_template), [`parse_tool_calls`](topogpt3.chat.py.md#parse_tool_calls), [`BPETokenizer.__init__`](topogpt3.model.py.md#bpetokenizer-__init__), [`BPETokenizer.decode`](topogpt3.model.py.md#bpetokenizer-decode), [`BPETokenizer.encode`](topogpt3.model.py.md#bpetokenizer-encode), [`CurriculumTrainer.model`](topogpt3.model.py.md#curriculumtrainer-model), [`TopoGPT2.__init__`](topogpt3.model.py.md#topogpt2-__init__), [`TopoGPT2.generate`](topogpt3.model.py.md#topogpt2-generate), [`TopoGPT2Config`](topogpt3.model.py.md#topogpt2config), [`grpo_advantages`](topogpt3.rewards.py.md#grpo_advantages), [`grpo_loss`](topogpt3.rewards.py.md#grpo_loss), [`execute_tool`](topogpt3.tools_agent.py.md#execute_tool) and 4 more

---
