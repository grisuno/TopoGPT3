# topogpt3: inference_hrm

*Community 3 | 9 files | cohesion 0.34*

## Definition

This community groups 9 file(s) rooted at `topogpt3` with dominant language py (cohesion 0.34). Central symbols: `ApiKey`, `ArtifactTokenizer`, `AuthState`, `ChatCompletionRequest`, `CheckpointPaths`, `CliArgumentParser`, `CompletionRequest`, `GaussPatchApplier`. Core file: `topogpt3/inference_hrm.py` (76 symbols). Documented purpose: Checkpoint architecture discovery tests..

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `tests/test_checkpoint_meta.py` | py | testing | 4 | yes |
| `tests/test_structured_output.py` | py | testing | 26 | yes |
| `topogpt3/api_server.py` | py | presentation | 63 | yes |
| `topogpt3/checkpoint_meta.py` | py | utility | 5 | yes |
| `topogpt3/continuation.py` | py | utility | 5 | yes |
| `topogpt3/inference.py` | py | utility | 54 | yes |
| `topogpt3/inference_hrm.py` | py | utility | 76 | yes |
| `topogpt3/structured_output.py` | py | utility | 18 | yes |
| `topogpt3/tokenizer_tools.py` | py | utility | 10 | yes |

## Key Symbols

- `test_read_state_missing` (function, `tests/test_checkpoint_meta.py:12`) `def test_read_state_missing(tmp_path)`
- `test_probe_t3_small` (function, `tests/test_checkpoint_meta.py:16`) `def test_probe_t3_small()`
- `test_probe_exploitgym_meta` (function, `tests/test_checkpoint_meta.py:24`) `def test_probe_exploitgym_meta()`
- `test_config_matches_weights` (function, `tests/test_checkpoint_meta.py:31`) `def test_config_matches_weights()`
- `tokenizer` (function, `tests/test_structured_output.py:19`) `def tokenizer()`
- `TestParseResponseFormat` (class, `tests/test_structured_output.py:29`) `class TestParseResponseFormat`
- `test_none_and_text` (method, `tests/test_structured_output.py:30`) `def test_none_and_text(self)`
- `test_json_object` (method, `tests/test_structured_output.py:34`) `def test_json_object(self)`
- `test_json_schema` (method, `tests/test_structured_output.py:39`) `def test_json_schema(self)`
- `test_regex` (method, `tests/test_structured_output.py:48`) `def test_regex(self)`
- `test_grammar` (method, `tests/test_structured_output.py:52`) `def test_grammar(self)`
- `test_invalid_payloads` (method, `tests/test_structured_output.py:65`) `def test_invalid_payloads(self, bad)`
- `TestParseSoArgs` (class, `tests/test_structured_output.py:70`) `class TestParseSoArgs`
- `test_json_string_schema` (method, `tests/test_structured_output.py:71`) `def test_json_string_schema(self)`
- `test_regex` (method, `tests/test_structured_output.py:77`) `def test_regex(self)`
- `test_ebnf` (method, `tests/test_structured_output.py:82`) `def test_ebnf(self)`
- `test_requires_schema` (method, `tests/test_structured_output.py:86`) `def test_requires_schema(self)`
- `test_unknown_schema_type` (method, `tests/test_structured_output.py:90`) `def test_unknown_schema_type(self)`
- `TestGrammarConstraint` (class, `tests/test_structured_output.py:95`) `class TestGrammarConstraint`
- `test_json_schema_accepts_and_terminates` (method, `tests/test_structured_output.py:96`) `def test_json_schema_accepts_and_terminates(self, tokenizer)`
- `test_regex_masks_illegal_first_token` (method, `tests/test_structured_output.py:122`) `def test_regex_masks_illegal_first_token(self, tokenizer)`
- `test_reset_restores_initial_state` (method, `tests/test_structured_output.py:136`) `def test_reset_restores_initial_state(self, tokenizer)`
- `test_invalid_regex_raises` (method, `tests/test_structured_output.py:148`) `def test_invalid_regex_raises(self, tokenizer)`
- `test_constraint_from_request_rejects_both_surfaces` (function, `tests/test_structured_output.py:154`) `def test_constraint_from_request_rejects_both_surfaces(tokenizer)`
- `TestRequestModels` (class, `tests/test_structured_output.py:163`) `class TestRequestModels`
- `test_chat_accepts_seed_and_response_format` (method, `tests/test_structured_output.py:164`) `def test_chat_accepts_seed_and_response_format(self)`
- `test_completion_accepts_so_args` (method, `tests/test_structured_output.py:176`) `def test_completion_accepts_so_args(self)`
- `test_negative_seed_rejected` (method, `tests/test_structured_output.py:185`) `def test_negative_seed_rejected(self)`
- `test_auto_continue_with_constraint_rejected` (function, `tests/test_structured_output.py:195`) `def test_auto_continue_with_constraint_rejected()`
- `test_make_generator_is_reproducible` (function, `tests/test_structured_output.py:211`) `def test_make_generator_is_reproducible()`

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 14
- Cross-boundary resolved imports (EXTRACTED): 24

## Connections

- [EXTRACTED] depends_on community 1 <-> 3 (strength 0.9): Extracted import edge crosses communities: eval/harness.py imports topogpt3/checkpoint_meta.py.
- [EXTRACTED] depends_on community 2 <-> 3 (strength 0.9): Extracted import edge crosses communities: eval/tasks.py imports topogpt3/checkpoint_meta.py.
- [EXTRACTED] depends_on community 3 <-> 0 (strength 0.9): Extracted import edge crosses communities: tests/test_structured_output.py imports topogpt3/model.py.
- [INFERRED] bridges community 1 <-> 3 (strength 0.5): Inferred cross-community bridge: eval/governor.py reaches tests/test_checkpoint_meta.py in 5 hops.
- [INFERRED] bridges community 1 <-> 3 (strength 0.5): Inferred cross-community bridge: eval/governor.py reaches topogpt3/structured_output.py in 5 hops.
- [INFERRED] bridges community 1 <-> 3 (strength 0.5): Inferred cross-community bridge: eval/governor.py reaches topogpt3/tokenizer_tools.py in 5 hops.

## Risks

- [taint critical] `eval/governor_smoke.py` -> `topogpt3/inference_hrm.py` via `eval` (2 hops)
- [taint critical] `eval/governor_smoke.py` -> `topogpt3/inference.py` via `eval` (2 hops)
- [taint critical] `eval/governor_smoke.py` -> `topogpt3/checkpoint_meta.py` via `eval` (3 hops)
- [taint critical] `eval/governor_smoke.py` -> `topogpt3/continuation.py` via `eval` (3 hops)
- [layer strict] `tests/test_structured_output.py` (testing) -> `topogpt3/api_server.py` (presentation)
- [layer strict] `tests/test_structured_output.py` (testing) -> `topogpt3/api_server.py` (presentation)
- [layer strict] `tests/test_structured_output.py` (testing) -> `topogpt3/api_server.py` (presentation)
- [layer strict] `tests/test_structured_output.py` (testing) -> `topogpt3/api_server.py` (presentation)
- [layer strict] `tests/test_structured_output.py` (testing) -> `topogpt3/api_server.py` (presentation)

## Open Questions

- What would break if the most connected file in topogpt3: inference_hrm changed?
- Should topogpt3: inference_hrm be split, given cohesion 0.34?

## Sources

- `tests/test_checkpoint_meta.py`
- `tests/test_structured_output.py`
- `topogpt3/api_server.py`
- `topogpt3/checkpoint_meta.py`
- `topogpt3/continuation.py`
- `topogpt3/inference.py`
- `topogpt3/inference_hrm.py`
- `topogpt3/structured_output.py`
- `topogpt3/tokenizer_tools.py`
