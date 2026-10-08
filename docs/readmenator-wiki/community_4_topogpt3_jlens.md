# topogpt3: jlens

*Community 4 | 4 files | cohesion 0.45*

## Definition

This community groups 4 file(s) rooted at `topogpt3` with dominant language py (cohesion 0.45). Central symbols: `ActivationRecorder`, `JacobianLens`, `LensModel`, `SliceData`, `TestConfig`, `TestFit`, `TestFitCheckpoint`, `TestJacobianForPrompt`. Core file: `tests/test_jlens.py` (51 symbols).

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `tests/test_jlens.py` | py | testing | 51 | no |
| `tests/test_lens_model.py` | py | testing | 34 | no |
| `topogpt3/jlens.py` | py | utility | 29 | no |
| `topogpt3/lens_model.py` | py | business_logic | 29 | no |

## Key Symbols

- `TestValidPositionMask` (class, `tests/test_jlens.py:17`) `class TestValidPositionMask` - Feature: valid_position_mask excludes attention-sink and final positions.
- `test_basic_mask` (method, `tests/test_jlens.py:20`) `def test_basic_mask(self)` - Scenario: Correct mask for a standard-length prompt.
- `test_too_short_raises` (method, `tests/test_jlens.py:29`) `def test_too_short_raises(self)` - Scenario: Too-short prompt raises ValueError.
- `test_negative_skip_raises` (method, `tests/test_jlens.py:34`) `def test_negative_skip_raises(self)` - Scenario: Negative skip_first raises ValueError.
- `test_all_positions_valid` (method, `tests/test_jlens.py:39`) `def test_all_positions_valid(self)` - Scenario: skip_first=0 includes all but final position.
- `test_exact_minimum_length` (method, `tests/test_jlens.py:45`) `def test_exact_minimum_length(self)` - Scenario: Exact minimum length (skip_first + 2) works.
- `TestJacobianForPrompt` (class, `tests/test_jlens.py:52`) `class TestJacobianForPrompt` - Feature: jacobian_for_prompt computes J_l for one prompt.
- `model` (method, `tests/test_jlens.py:56`) `def model(self)`
- `test_returns_jacobians_for_source_layers` (method, `tests/test_jlens.py:63`) `def test_returns_jacobians_for_source_layers(self, model)` - Scenario: Returns Jacobians for all requested source layers.
- `test_late_layer_jacobian_close_to_identity` (method, `tests/test_jlens.py:76`) `def test_late_layer_jacobian_close_to_identity(self, model)` - Scenario: J_{n_layers-2} has diag ~= 1 (identity property).
- `test_earlier_layers_further_from_identity` (method, `tests/test_jlens.py:85`) `def test_earlier_layers_further_from_identity(self, model)` - Scenario: Earlier layers compound deviations from identity.
- `test_exact_jacobian_for_last_block` (method, `tests/test_jlens.py:95`) `def test_exact_jacobian_for_last_block(self, model)` - Scenario: J_{n_layers-2} equals I + W_{last} exactly.
- `test_negative_layer_indices` (method, `tests/test_jlens.py:110`) `def test_negative_layer_indices(self, model)` - Scenario: Negative layer indices are normalized correctly.
- `test_out_of_range_layers_rejected` (method, `tests/test_jlens.py:133`) `def test_out_of_range_layers_rejected(self, model)` - Scenario: Out-of-range layers raise ValueError.
- `test_source_below_target_enforced` (method, `tests/test_jlens.py:145`) `def test_source_below_target_enforced(self, model)` - Scenario: source_layers must be below target_layer.
- `test_target_out_of_range_raises` (method, `tests/test_jlens.py:158`) `def test_target_out_of_range_raises(self, model)` - Scenario: target_layer out of range raises ValueError.
- `TestFit` (class, `tests/test_jlens.py:172`) `class TestFit` - Feature: fit() averages Jacobians over multiple prompts.
- `model` (method, `tests/test_jlens.py:176`) `def model(self)`
- `test_fit_returns_lens_with_correct_attributes` (method, `tests/test_jlens.py:183`) `def test_fit_returns_lens_with_correct_attributes(self, model)` - Scenario: fit() returns JacobianLens with correct metadata.
- `test_fit_empty_prompts_raises` (method, `tests/test_jlens.py:191`) `def test_fit_empty_prompts_raises(self, model)` - Scenario: No valid prompts raises ValueError.
- `test_fit_skips_short_prompts` (method, `tests/test_jlens.py:196`) `def test_fit_skips_short_prompts(self, model)` - Scenario: Too-short prompts are skipped.
- `test_fit_with_default_source_layers` (method, `tests/test_jlens.py:202`) `def test_fit_with_default_source_layers(self, model)` - Scenario: Default source_layers covers all layers below target.
- `TestJacobianLens` (class, `tests/test_jlens.py:210`) `class TestJacobianLens` - Feature: JacobianLens saves, loads, applies, and merges.
- `model` (method, `tests/test_jlens.py:214`) `def model(self)`
- `fitted_lens` (method, `tests/test_jlens.py:222`) `def fitted_lens(self, model)`
- `test_save_and_load_round_trip` (method, `tests/test_jlens.py:226`) `def test_save_and_load_round_trip(self, fitted_lens, tmp_path)` - Scenario: save/load preserves jacobians (fp16 tolerance).
- `test_apply_returns_correct_shapes` (method, `tests/test_jlens.py:242`) `def test_apply_returns_correct_shapes(self, fitted_lens, model)` - Scenario: apply() returns correct logit shapes.
- `test_fitted_late_layer_matches_model` (method, `tests/test_jlens.py:254`) `def test_fitted_late_layer_matches_model(self, fitted_lens, model)` - Scenario: Transported late-layer logits match model logits.
- `test_apply_with_explicit_positions` (method, `tests/test_jlens.py:263`) `def test_apply_with_explicit_positions(self, fitted_lens, model)` - Scenario: Explicit positions return correct subset.
- `test_logit_lens_baseline` (method, `tests/test_jlens.py:274`) `def test_logit_lens_baseline(self, fitted_lens, model)` - Scenario: use_jacobian=False returns untransported logits.

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 9
- Cross-boundary resolved imports (EXTRACTED): 8

## Connections

- [EXTRACTED] depends_on community 4 <-> 2 (strength 0.9): Extracted import edge crosses communities: tests/test_lens_model.py imports topogpt3/model.py.
- [EXTRACTED] depends_on community 1 <-> 4 (strength 0.9): Extracted import edge crosses communities: topogpt3/__init__.py imports topogpt3/lens_model.py.
- [EXTRACTED] depends_on community 0 <-> 4 (strength 0.9): Extracted import edge crosses communities: topogpt3/__main__.py imports topogpt3/jlens.py.
- [INFERRED] bridges community 3 <-> 4 (strength 0.5): Inferred cross-community bridge: eval/sandbox_smoke.py reaches tests/test_jlens.py in 5 hops.
- [INFERRED] bridges community 3 <-> 4 (strength 0.5): Inferred cross-community bridge: eval/sandbox_smoke.py reaches tests/test_lens_model.py in 5 hops.

## Risks

- [taint critical] `eval/governor_smoke.py` -> `topogpt3/jlens.py` via `eval` (2 hops)
- [taint critical] `eval/governor_smoke.py` -> `topogpt3/lens_model.py` via `eval` (2 hops)

## Open Questions

- Why do 4 file(s) lack file-level docs (e.g. `tests/test_jlens.py`)? What purpose do they serve?
- What would break if the most connected file in topogpt3: jlens changed?
- Should topogpt3: jlens be split, given cohesion 0.45?

## Sources

- `tests/test_jlens.py`
- `tests/test_lens_model.py`
- `topogpt3/jlens.py`
- `topogpt3/lens_model.py`
