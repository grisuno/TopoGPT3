# topogpt3: sandbox

*Community 3 | 7 files | cohesion 0.41*

## Definition

This community groups 7 file(s) rooted at `topogpt3` with dominant language py (cohesion 0.41). Central symbols: `SandboxConfig`, `YaRNConfig`, `_blocked_dunder_access`, `_build_worker_src`, `_fmt_tool_defs`, `_max_depth`, `_micro`, `_names_imported`. Core file: `eval/sandbox.py` (9 symbols). Documented purpose: Sandbox for executing model-generated code during HumanEval evaluation.  This module replaces the bare `exec()` call in `eval/harness.py:run_one_test` with a de.

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `eval/sandbox.py` | py | utility | 9 | yes |
| `eval/sandbox_smoke.py` | py | utility | 1 | yes |
| `tests/test_heritage.py` | py | testing | 9 | yes |
| `topogpt3/chat.py` | py | utility | 7 | yes |
| `topogpt3/eval_toolcall.py` | py | utility | 2 | yes |
| `topogpt3/tools_agent.py` | py | utility | 2 | yes |
| `topogpt3/yarn.py` | py | utility | 3 | yes |

## Key Symbols

- `SandboxConfig` (class, `eval/sandbox.py:53`) `class SandboxConfig` - One knob per defence layer. Defaults match HumanEval-style eval.
- `_names_imported` (method, `eval/sandbox.py:100`) `def _names_imported(tree)` - Return the set of top-level names brought into scope by imports.
- `_blocked_dunder_access` (method, `eval/sandbox.py:114`) `def _blocked_dunder_access(tree, blocked)` - Find Attribute nodes whose attr is in `blocked`. Returns attr names found.
- `_max_depth` (method, `eval/sandbox.py:123`) `def _max_depth(tree)` - Compute max nesting depth of the AST. Catches obfuscated huge trees.
- `d` (method, `eval/sandbox.py:125`) `def d(node, cur)`
- `check_safety` (method, `eval/sandbox.py:133`) `def check_safety(source, cfg)` - Return (ok, reason). `reason` is "" when ok, else a human-readable
- `_build_worker_src` (method, `eval/sandbox.py:254`) `def _build_worker_src(allowed_builtin_names, program_src, blocked_modules)`
- `safe_exec` (method, `eval/sandbox.py:270`) `def safe_exec(program_src, cfg, extra_globals)` - Execute `program_src` in a sandboxed child process. Returns the same
- `describe_policy` (method, `eval/sandbox.py:373`) `def describe_policy(cfg)`
- `main` (function, `eval/sandbox_smoke.py:15`) `def main()`
- `_micro` (function, `tests/test_heritage.py:18`) `def _micro()`
- `test_chat_template_tools_think` (function, `tests/test_heritage.py:24`) `def test_chat_template_tools_think()`
- `test_yarn_changes_freqs_only` (function, `tests/test_heritage.py:37`) `def test_yarn_changes_freqs_only()`
- `test_lora_zero_init_and_quaternion_targets` (function, `tests/test_heritage.py:47`) `def test_lora_zero_init_and_quaternion_targets()`
- `test_lora_save_load` (function, `tests/test_heritage.py:64`) `def test_lora_save_load(tmp_path)`
- `test_dpo_grpo_losses_finite` (function, `tests/test_heritage.py:76`) `def test_dpo_grpo_losses_finite()`
- `test_distill_loss_finite` (function, `tests/test_heritage.py:96`) `def test_distill_loss_finite()`
- `test_rollout_engine_micro` (function, `tests/test_heritage.py:106`) `def test_rollout_engine_micro()`
- `test_tools_and_eval` (function, `tests/test_heritage.py:123`) `def test_tools_and_eval()`
- `pre_processing_chat` (function, `topogpt3/chat.py:43`) `def pre_processing_chat(conversations, add_system_ratio)` - Randomly prepend a system prompt (skip when tools present).
- `post_processing_chat` (function, `topogpt3/chat.py:54`) `def post_processing_chat(prompt, empty_think_ratio)`
- `_fmt_tool_defs` (function, `topogpt3/chat.py:60`) `def _fmt_tool_defs(tools)`
- `apply_chat_template` (function, `topogpt3/chat.py:71`) `def apply_chat_template(messages, tools, add_generation_prompt, open_thinking)` - Render messages with tool definitions, thinking and tool-call blocks.
- `parse_tool_calls` (function, `topogpt3/chat.py:116`) `def parse_tool_calls(text)`
- `parse_thinking` (function, `topogpt3/chat.py:126`) `def parse_thinking(text)`
- `split_reasoning_content` (function, `topogpt3/chat.py:134`) `def split_reasoning_content(text)` - Split generated text into reasoning_content / content / tool_calls (API).
- `run_case` (function, `topogpt3/eval_toolcall.py:19`) `def run_case(generate_fn, prompt, expect_tool)`
- `evaluate` (function, `topogpt3/eval_toolcall.py:35`) `def evaluate(generate_fn)`
- `execute_tool` (function, `topogpt3/tools_agent.py:59`) `def execute_tool(name, args)`
- `rollout_multiturn` (function, `topogpt3/tools_agent.py:80`) `def rollout_multiturn(generate_fn, tokenizer, messages, tools, max_turns, max_ne` - generate_fn(prompt_text)->text. Returns (full_text, tool_trace).

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 11
- Cross-boundary resolved imports (EXTRACTED): 15

## Connections

- [EXTRACTED] depends_on community 1 <-> 3 (strength 0.9): Extracted import edge crosses communities: eval/harness.py imports eval/sandbox.py.
- [EXTRACTED] depends_on community 3 <-> 0 (strength 0.9): Extracted import edge crosses communities: tests/test_heritage.py imports topogpt3/lora.py.
- [EXTRACTED] depends_on community 3 <-> 2 (strength 0.9): Extracted import edge crosses communities: tests/test_heritage.py imports topogpt3/model.py.
- [INFERRED] bridges community 1 <-> 3 (strength 0.5): Inferred cross-community bridge: eval/governor.py reaches eval/sandbox_smoke.py in 5 hops.
- [INFERRED] bridges community 3 <-> 2 (strength 0.5): Inferred cross-community bridge: eval/sandbox_smoke.py reaches synthetic_dataset.py in 5 hops.
- [INFERRED] bridges community 3 <-> 4 (strength 0.5): Inferred cross-community bridge: eval/sandbox_smoke.py reaches tests/test_jlens.py in 5 hops.
- [INFERRED] bridges community 3 <-> 4 (strength 0.5): Inferred cross-community bridge: eval/sandbox_smoke.py reaches tests/test_lens_model.py in 5 hops.
- [INFERRED] bridges community 3 <-> 2 (strength 0.5): Inferred cross-community bridge: eval/sandbox_smoke.py reaches topogpt3/continuation.py in 5 hops.

## Risks

- [taint critical] `eval/governor_smoke.py` -> `topogpt3/tools_agent.py` via `eval` (2 hops)
- [taint critical] `eval/governor_smoke.py` -> `topogpt3/eval_toolcall.py` via `eval` (2 hops)
- [taint critical] `eval/governor_smoke.py` -> `topogpt3/chat.py` via `eval` (2 hops)
- [taint critical] `eval/governor_smoke.py` -> `topogpt3/yarn.py` via `eval` (2 hops)
- [taint critical] `eval/governor_smoke.py` -> `eval/sandbox.py` via `eval` (3 hops)

## Open Questions

- What would break if the most connected file in topogpt3: sandbox changed?
- Should topogpt3: sandbox be split, given cohesion 0.41?

## Sources

- `eval/sandbox.py`
- `eval/sandbox_smoke.py`
- `tests/test_heritage.py`
- `topogpt3/chat.py`
- `topogpt3/eval_toolcall.py`
- `topogpt3/tools_agent.py`
- `topogpt3/yarn.py`
