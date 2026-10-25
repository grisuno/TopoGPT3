# topogpt3: tasks

*Community 2 | 10 files | cohesion 0.51*

## Definition

This community groups 10 file(s) rooted at `topogpt3` with dominant language py (cohesion 0.51). Central symbols: `Profile`, `TestProfiles`, `TestScoring`, `TestSynthesize`, `TestToolCallsPayload`, `TestValidateToolCall`, `_apt_chain_preview`, `_call`. Core file: `tests/test_fallback.py` (23 symbols). Documented purpose: Generic task eval: JSONL cases + safe verifiers.  Case schema (one JSON object per line): {"id": "...", "prompt": "user text", "profile": "topoexploit-apt-chain.

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `eval/tasks.py` | py | utility | 15 | yes |
| `tests/test_eval_tasks.py` | py | testing | 4 | yes |
| `tests/test_fallback.py` | py | testing | 23 | yes |
| `tests/test_heritage.py` | py | testing | 9 | yes |
| `topogpt3/chat.py` | py | utility | 8 | yes |
| `topogpt3/eval_toolcall.py` | py | utility | 2 | yes |
| `topogpt3/fallback.py` | py | utility | 15 | yes |
| `topogpt3/rewards.py` | py | utility | 12 | yes |
| `topogpt3/tools_agent.py` | py | utility | 3 | yes |
| `topogpt3/train_agent.py` | py | utility | 2 | yes |

## Key Symbols

- `_extract_code` (function, `eval/tasks.py:34`) `def _extract_code(text)`
- `_extract_json` (function, `eval/tasks.py:39`) `def _extract_json(text)`
- `verify_tool_call` (function, `eval/tasks.py:50`) `def verify_tool_call(case, completion)`
- `verify_json` (function, `eval/tasks.py:78`) `def verify_json(case, completion)`
- `verify_regex` (function, `eval/tasks.py:90`) `def verify_regex(case, completion)`
- `verify_exact` (function, `eval/tasks.py:97`) `def verify_exact(case, completion)`
- `verify_contains` (function, `eval/tasks.py:105`) `def verify_contains(case, completion)`
- `verify_python_ast` (function, `eval/tasks.py:114`) `def verify_python_ast(case, completion)`
- `load_cases` (function, `eval/tasks.py:133`) `def load_cases(path)`
- `evaluate_case` (function, `eval/tasks.py:145`) `def evaluate_case(case, generate_fn)`
- `evaluate_cases` (function, `eval/tasks.py:174`) `def evaluate_cases(cases, generate_fn, limit)`
- `summary` (function, `eval/tasks.py:187`) `def summary(results)`
- `build_generate_fn` (function, `eval/tasks.py:197`) `def build_generate_fn(ckpt_dir, ckpt_name, device, max_new_tokens)`
- `generate` (function, `eval/tasks.py:221`) `def generate(prompt, profile_name)`
- `main` (function, `eval/tasks.py:251`) `def main()`
- `_gen` (function, `tests/test_eval_tasks.py:16`) `def _gen(prompt, profile_name)`
- `test_apt_chain_cases_full_pass` (function, `tests/test_eval_tasks.py:21`) `def test_apt_chain_cases_full_pass()`
- `test_regex_verifier` (function, `tests/test_eval_tasks.py:30`) `def test_regex_verifier()`
- `test_tool_call_verifier_rejects_wrong_target` (function, `tests/test_eval_tasks.py:36`) `def test_tool_call_verifier_rejects_wrong_target()`
- `_call` (function, `tests/test_fallback.py:19`) `def _call(name, args)`
- `TestProfiles` (class, `tests/test_fallback.py:23`) `class TestProfiles`
- `test_resolve_by_name_and_alias` (method, `tests/test_fallback.py:24`) `def test_resolve_by_name_and_alias(self)`
- `test_unknown_falls_back` (method, `tests/test_fallback.py:29`) `def test_unknown_falls_back(self)`
- `test_apt_chain_tools_registered` (method, `tests/test_fallback.py:32`) `def test_apt_chain_tools_registered(self)`
- `TestValidateToolCall` (class, `tests/test_fallback.py:38`) `class TestValidateToolCall`
- `test_valid_apt_chain` (method, `tests/test_fallback.py:39`) `def test_valid_apt_chain(self)`
- `test_requires_target` (method, `tests/test_fallback.py:48`) `def test_requires_target(self)`
- `test_invalid_chain_name` (method, `tests/test_fallback.py:52`) `def test_invalid_chain_name(self)`
- `test_run_command_forbidden_chars` (method, `tests/test_fallback.py:61`) `def test_run_command_forbidden_chars(self)`
- `test_unknown_tool` (method, `tests/test_fallback.py:67`) `def test_unknown_tool(self)`

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 25
- Cross-boundary resolved imports (EXTRACTED): 27

## Connections

- [EXTRACTED] depends_on community 2 <-> 3 (strength 0.9): Extracted import edge crosses communities: eval/tasks.py imports topogpt3/checkpoint_meta.py.
- [EXTRACTED] depends_on community 2 <-> 0 (strength 0.9): Extracted import edge crosses communities: eval/tasks.py imports topogpt3/model.py.
- [EXTRACTED] depends_on community 2 <-> 1 (strength 0.9): Extracted import edge crosses communities: tests/test_heritage.py imports topogpt3/yarn.py.
- [INFERRED] shares_context community 2 <-> 4 (strength 0.5): Inferred shared context (language py) with no import path between community 2 (topogpt3: tasks) and community 4 (topogpt3: jlens).
- [INFERRED] shares_context community 2 <-> 5 (strength 0.5): Inferred shared context (language py and layer utility) with no import path between community 2 (topogpt3: tasks) and community 5 (root).
- [INFERRED] shares_context community 2 <-> 6 (strength 0.5): Inferred shared context (language py and layer utility) with no import path between community 2 (topogpt3: tasks) and community 6 (orphans).

## Risks

- [taint critical] `eval/governor_smoke.py` -> `topogpt3/eval_toolcall.py` via `eval` (2 hops)
- [taint critical] `eval/governor_smoke.py` -> `topogpt3/chat.py` via `eval` (2 hops)
- [taint critical] `eval/governor_smoke.py` -> `topogpt3/tools_agent.py` via `eval` (2 hops)
- [taint critical] `eval/governor_smoke.py` -> `topogpt3/rewards.py` via `eval` (2 hops)
- [taint critical] `eval/governor_smoke.py` -> `topogpt3/fallback.py` via `eval` (3 hops)

## Open Questions

- What would break if the most connected file in topogpt3: tasks changed?
- Should topogpt3: tasks be split, given cohesion 0.51?

## Sources

- `eval/tasks.py`
- `tests/test_eval_tasks.py`
- `tests/test_fallback.py`
- `tests/test_heritage.py`
- `topogpt3/chat.py`
- `topogpt3/eval_toolcall.py`
- `topogpt3/fallback.py`
- `topogpt3/rewards.py`
- `topogpt3/tools_agent.py`
- `topogpt3/train_agent.py`
