from __future__ import annotations

import pytest
import torch

from topogpt3.lens_model import TinyDecoder, TopoGPT3LensModel
from topogpt3.jlens import (
    JacobianLens,
    TopoGPT3JLensFitConfig,
    TopoGPT3JLensAppConfig,
    fit,
    jacobian_for_prompt,
    valid_position_mask,
)


class TestValidPositionMask:
    """Feature: valid_position_mask excludes attention-sink and final positions."""

    def test_basic_mask(self):
        """Scenario: Correct mask for a standard-length prompt."""
        mask = valid_position_mask(32, skip_first=4)
        assert mask.dtype == torch.bool
        assert mask[:4].sum() == 0
        assert not mask[-1]
        assert mask[4:-1].all()
        assert mask.sum() == 32 - 4 - 1

    def test_too_short_raises(self):
        """Scenario: Too-short prompt raises ValueError."""
        with pytest.raises(ValueError, match="too short"):
            valid_position_mask(5, skip_first=8)

    def test_negative_skip_raises(self):
        """Scenario: Negative skip_first raises ValueError."""
        with pytest.raises(ValueError, match="skip_first must be >= 0"):
            valid_position_mask(16, skip_first=-1)

    def test_all_positions_valid(self):
        """Scenario: skip_first=0 includes all but final position."""
        mask = valid_position_mask(10, skip_first=0)
        assert mask.sum() == 9
        assert not mask[-1]

    def test_exact_minimum_length(self):
        """Scenario: Exact minimum length (skip_first + 2) works."""
        mask = valid_position_mask(18, skip_first=16)
        assert mask.sum() == 1
        assert mask[16]


class TestJacobianForPrompt:
    """Feature: jacobian_for_prompt computes J_l for one prompt."""

    @pytest.fixture
    def model(self):
        raw = TinyDecoder(n_layers=4, d_model=8)
        raw.eval()
        for p in raw.parameters():
            p.requires_grad_(False)
        return TopoGPT3LensModel(raw)

    def test_returns_jacobians_for_source_layers(self, model):
        """Scenario: Returns Jacobians for all requested source layers."""
        prompt = "the quick brown fox " * 4
        jacobians, seq_len, n_valid = jacobian_for_prompt(
            model, prompt, source_layers=[0, 1, 2], dim_batch=4, max_seq_len=64
        )
        assert set(jacobians) == {0, 1, 2}
        for J in jacobians.values():
            assert J.shape == (8, 8)
            assert J.dtype == torch.float32
        assert n_valid > 0
        assert seq_len > n_valid

    def test_late_layer_jacobian_close_to_identity(self, model):
        """Scenario: J_{n_layers-2} has diag ~= 1 (identity property)."""
        prompt = "the quick brown fox " * 4
        jacobians, _, _ = jacobian_for_prompt(
            model, prompt, source_layers=[0, 1, 2], dim_batch=4, max_seq_len=64
        )
        diag_late = jacobians[2].diag()
        assert (diag_late - 1.0).abs().max() < 0.2

    def test_earlier_layers_further_from_identity(self, model):
        """Scenario: Earlier layers compound deviations from identity."""
        prompt = "the quick brown fox " * 4
        jacobians, _, _ = jacobian_for_prompt(
            model, prompt, source_layers=[0, 1, 2], dim_batch=4, max_seq_len=64
        )
        assert (
            jacobians[0] - torch.eye(8)
        ).norm() > (jacobians[2] - torch.eye(8)).norm()

    def test_exact_jacobian_for_last_block(self, model):
        """Scenario: J_{n_layers-2} equals I + W_{last} exactly.

        For TinyDecoder with block = h + 0.1*W*h, J_{n_layers-2} = I + W.
        """
        prompt = "the quick brown fox " * 4
        jacobians, _, _ = jacobian_for_prompt(
            model, prompt, source_layers=[0, 1, 2], dim_batch=4, max_seq_len=64
        )
        expected_J2 = (
            torch.eye(8)
            + model._model.layers[3].linear.weight.detach()
        )
        torch.testing.assert_close(jacobians[2], expected_J2, rtol=0, atol=1e-5)

    def test_negative_layer_indices(self, model):
        """Scenario: Negative layer indices are normalized correctly."""
        prompt = "the quick brown fox " * 4
        jac_neg, _, _ = jacobian_for_prompt(
            model,
            prompt,
            source_layers=[-4, -3],
            target_layer=-1,
            dim_batch=4,
            max_seq_len=64,
        )
        jac_pos, _, _ = jacobian_for_prompt(
            model,
            prompt,
            source_layers=[0, 1],
            target_layer=3,
            dim_batch=4,
            max_seq_len=64,
        )
        assert set(jac_neg) == {0, 1}
        for layer in (0, 1):
            torch.testing.assert_close(jac_neg[layer], jac_pos[layer])

    def test_out_of_range_layers_rejected(self, model):
        """Scenario: Out-of-range layers raise ValueError."""
        prompt = "the quick brown fox " * 4
        with pytest.raises(ValueError, match="out of range"):
            jacobian_for_prompt(
                model,
                prompt,
                source_layers=[0, 7],
                dim_batch=4,
                max_seq_len=64,
            )

    def test_source_below_target_enforced(self, model):
        """Scenario: source_layers must be below target_layer."""
        prompt = "the quick brown fox " * 4
        with pytest.raises(ValueError, match="must all be < target_layer"):
            jacobian_for_prompt(
                model,
                prompt,
                source_layers=[-1],
                target_layer=3,
                dim_batch=4,
                max_seq_len=64,
            )

    def test_target_out_of_range_raises(self, model):
        """Scenario: target_layer out of range raises ValueError."""
        prompt = "the quick brown fox " * 4
        with pytest.raises(ValueError, match="target_layer"):
            jacobian_for_prompt(
                model,
                prompt,
                source_layers=[0],
                target_layer=9,
                dim_batch=4,
                max_seq_len=64,
            )


class TestFit:
    """Feature: fit() averages Jacobians over multiple prompts."""

    @pytest.fixture
    def model(self):
        raw = TinyDecoder(n_layers=4, d_model=8)
        raw.eval()
        for p in raw.parameters():
            p.requires_grad_(False)
        return TopoGPT3LensModel(raw)

    def test_fit_returns_lens_with_correct_attributes(self, model):
        """Scenario: fit() returns JacobianLens with correct metadata."""
        prompts = ["abcdefghij " * 5, "klmnopqrst " * 5]
        lens = fit(model, prompts, source_layers=[0, 1, 2], dim_batch=4, max_seq_len=64)
        assert lens.n_prompts == 2
        assert lens.source_layers == [0, 1, 2]
        assert lens.d_model == 8

    def test_fit_empty_prompts_raises(self, model):
        """Scenario: No valid prompts raises ValueError."""
        with pytest.raises(ValueError, match="no prompts"):
            fit(model, [], source_layers=[0], dim_batch=4, max_seq_len=64)

    def test_fit_skips_short_prompts(self, model):
        """Scenario: Too-short prompts are skipped."""
        prompts = ["short", "abcdefghij " * 5]
        lens = fit(model, prompts, source_layers=[0], dim_batch=4, max_seq_len=64)
        assert lens.n_prompts == 1

    def test_fit_with_default_source_layers(self, model):
        """Scenario: Default source_layers covers all layers below target."""
        prompts = ["abcdefghij " * 5]
        lens = fit(model, prompts, dim_batch=4, max_seq_len=64)
        assert lens.source_layers == [0, 1, 2]
        assert len(lens.source_layers) == model.n_layers - 1


class TestJacobianLens:
    """Feature: JacobianLens saves, loads, applies, and merges."""

    @pytest.fixture
    def model(self):
        raw = TinyDecoder(n_layers=4, d_model=8)
        raw.eval()
        for p in raw.parameters():
            p.requires_grad_(False)
        return TopoGPT3LensModel(raw)

    @pytest.fixture
    def fitted_lens(self, model):
        prompts = ["abcdefghij " * 5, "klmnopqrst " * 5]
        return fit(model, prompts, source_layers=[0, 1, 2], dim_batch=4, max_seq_len=64)

    def test_save_and_load_round_trip(self, fitted_lens, tmp_path):
        """Scenario: save/load preserves jacobians (fp16 tolerance)."""
        path = tmp_path / "lens.pt"
        fitted_lens.save(str(path))
        reloaded = JacobianLens.load(str(path))
        assert reloaded.source_layers == [0, 1, 2]
        assert reloaded.n_prompts == 2
        assert reloaded.d_model == 8
        for layer in [0, 1, 2]:
            torch.testing.assert_close(
                reloaded.jacobians[layer],
                fitted_lens.jacobians[layer],
                rtol=0,
                atol=2e-3,
            )

    def test_apply_returns_correct_shapes(self, fitted_lens, model):
        """Scenario: apply() returns correct logit shapes."""
        lens_logits, model_logits, input_ids = fitted_lens.apply(
            model, "the quick brown fox jumps", layers=[0, 2]
        )
        assert set(lens_logits) == {0, 2}
        vocab_size = model._model.lm_head.out_features
        seq_len = input_ids.shape[1]
        assert model_logits.shape == (seq_len, vocab_size)
        for tensor in lens_logits.values():
            assert tensor.shape == (seq_len, vocab_size)

    def test_fitted_late_layer_matches_model(self, fitted_lens, model):
        """Scenario: Transported late-layer logits match model logits."""
        lens_logits, model_logits, _ = fitted_lens.apply(
            model, "the quick brown fox jumps", layers=[0, 2]
        )
        torch.testing.assert_close(
            lens_logits[2], model_logits, rtol=0, atol=1e-2
        )

    def test_apply_with_explicit_positions(self, fitted_lens, model):
        """Scenario: Explicit positions return correct subset."""
        lens_logits, model_logits, _ = fitted_lens.apply(
            model, "the quick brown fox jumps", layers=[0, 2], positions=[0, -1]
        )
        assert set(lens_logits) == {0, 2}
        vocab_size = model._model.lm_head.out_features
        assert model_logits.shape == (2, vocab_size)
        for layer in [0, 2]:
            assert lens_logits[layer].shape == (2, vocab_size)

    def test_logit_lens_baseline(self, fitted_lens, model):
        """Scenario: use_jacobian=False returns untransported logits."""
        baseline, _, _ = fitted_lens.apply(
            model, "hello world test", layers=[1], positions=[-1], use_jacobian=False
        )
        assert baseline[1].shape == (1, model._model.lm_head.out_features)

    def test_unfitted_layer_rejected(self, fitted_lens, model):
        """Scenario: Unfitted layer raises ValueError."""
        with pytest.raises(ValueError, match="not in source_layers"):
            fitted_lens.apply(model, "x" * 30, layers=[3])

    def test_out_of_range_layer_rejected(self, fitted_lens, model):
        """Scenario: Out-of-range layer raises ValueError."""
        with pytest.raises(ValueError, match="out of range"):
            fitted_lens.apply(model, "x" * 30, layers=[99], use_jacobian=False)

    def test_merge_weighted_mean(self):
        """Scenario: merge() computes n_prompts-weighted mean."""
        d_model = 4
        lens_a = JacobianLens(
            jacobians={
                0: torch.full((d_model, d_model), 1.0),
                1: torch.full((d_model, d_model), 2.0),
            },
            n_prompts=2,
            d_model=d_model,
        )
        lens_b = JacobianLens(
            jacobians={
                0: torch.full((d_model, d_model), 4.0),
                1: torch.full((d_model, d_model), 8.0),
            },
            n_prompts=6,
            d_model=d_model,
        )
        merged = JacobianLens.merge([lens_a, lens_b])
        assert merged.n_prompts == 8
        torch.testing.assert_close(
            merged.jacobians[0], torch.full((d_model, d_model), 3.25)
        )
        torch.testing.assert_close(
            merged.jacobians[1], torch.full((d_model, d_model), 6.5)
        )

    def test_merge_mismatch_raises(self):
        """Scenario: Mismatched lenses raise ValueError."""
        a = JacobianLens(jacobians={0: torch.eye(4)}, n_prompts=1, d_model=4)
        b = JacobianLens(jacobians={1: torch.eye(4)}, n_prompts=1, d_model=4)
        with pytest.raises(ValueError, match="disagree"):
            JacobianLens.merge([a, b])

    def test_merge_empty_raises(self):
        """Scenario: Empty merge raises ValueError."""
        with pytest.raises(ValueError, match="at least one"):
            JacobianLens.merge([])

    def test_transport_produces_correct_shape(self, fitted_lens):
        """Scenario: transport() maps residual to final-layer basis."""
        residual = torch.randn(8, fitted_lens.d_model)
        transported = fitted_lens.transport(residual, layer=2)
        assert transported.shape == residual.shape

    def test_load_invalid_file_raises(self, tmp_path):
        """Scenario: Loading non-lens file raises ValueError."""
        path = tmp_path / "not_lens.pt"
        torch.save({"not_J": "data"}, path)
        with pytest.raises(ValueError, match="not a JacobianLens file"):
            JacobianLens.load(str(path))

    def test_from_pretrained_local_file(self, fitted_lens, tmp_path):
        """Scenario: from_pretrained resolves a local file."""
        path = tmp_path / "lens.pt"
        fitted_lens.save(str(path))
        reloaded = JacobianLens.from_pretrained(str(path))
        assert reloaded.n_prompts == 2

    def test_from_pretrained_local_directory(self, fitted_lens, tmp_path):
        """Scenario: from_pretrained resolves a local directory."""
        one_dir = tmp_path / "one"
        one_dir.mkdir()
        fitted_lens.save(str(one_dir / "lens.pt"))
        reloaded = JacobianLens.from_pretrained(str(one_dir))
        assert reloaded.n_prompts == 2

    def test_repr(self, fitted_lens):
        """Scenario: repr contains key metadata."""
        text = repr(fitted_lens)
        assert "d_model=8" in text
        assert "n_prompts=2" in text
        assert "source_layers" in text


class TestFitCheckpoint:
    """Feature: fit() with checkpoint resume works correctly."""

    @pytest.fixture
    def model(self):
        raw = TinyDecoder(n_layers=4, d_model=8)
        raw.eval()
        for p in raw.parameters():
            p.requires_grad_(False)
        return TopoGPT3LensModel(raw)

    def test_checkpoint_resume_produces_same_result(self, model, tmp_path):
        """Scenario: Resumed fit matches fresh fit."""
        prompts = [
            "abcdefghij " * 5,
            "klmnopqrst " * 5,
            "uvwxyzabcd " * 5,
        ]
        checkpoint = str(tmp_path / "ckpt.pt")
        full = fit(
            model,
            prompts,
            source_layers=[0, 2],
            dim_batch=4,
            max_seq_len=64,
            checkpoint_path=checkpoint,
        )
        resumed = fit(
            model,
            prompts,
            source_layers=[0, 2],
            dim_batch=4,
            max_seq_len=64,
            checkpoint_path=checkpoint,
        )
        assert resumed.n_prompts == full.n_prompts == 3
        for layer in [0, 2]:
            torch.testing.assert_close(
                resumed.jacobians[layer], full.jacobians[layer]
            )

    def test_resume_after_skip_no_double_count(self, model, tmp_path):
        """Scenario: Resume after a skipped prompt does not double-count.

        Regression: a skipped prompt must not desync success-count from
        list-position.
        """
        long_a = "abcdefghij " * 5
        short = "x"
        long_b = "klmnopqrst " * 5
        prompts = [long_a, short, long_b]
        checkpoint = str(tmp_path / "ckpt.pt")
        reference = fit(
            model,
            prompts,
            source_layers=[0, 2],
            dim_batch=4,
            max_seq_len=64,
        )
        assert reference.n_prompts == 2

        fit(
            model,
            prompts,
            source_layers=[0, 2],
            dim_batch=4,
            max_seq_len=64,
            checkpoint_path=checkpoint,
        )
        resumed = fit(
            model,
            prompts,
            source_layers=[0, 2],
            dim_batch=4,
            max_seq_len=64,
            checkpoint_path=checkpoint,
        )
        assert resumed.n_prompts == 2
        for layer in [0, 2]:
            torch.testing.assert_close(
                resumed.jacobians[layer], reference.jacobians[layer]
            )

    def test_checkpoint_mismatch_raises(self, model, tmp_path):
        """Scenario: Mismatched checkpoint settings raise ValueError."""
        prompts = ["abcdefghij " * 5]
        checkpoint = str(tmp_path / "ckpt.pt")
        fit(
            model,
            prompts,
            source_layers=[0, 1],
            dim_batch=4,
            max_seq_len=64,
            checkpoint_path=checkpoint,
        )
        with pytest.raises(ValueError, match="source_layers"):
            fit(
                model,
                prompts,
                source_layers=[0, 2],
                dim_batch=4,
                max_seq_len=64,
                checkpoint_path=checkpoint,
            )


class TestConfig:
    """Feature: Config classes centralize all tunable parameters."""

    def test_fit_config_defaults(self):
        """Scenario: Default fit config has sensible defaults."""
        cfg = TopoGPT3JLensFitConfig()
        assert cfg.dim_batch == 8
        assert cfg.max_seq_len == 128
        assert cfg.skip_first == 16
        assert cfg.resume is True
        assert cfg.source_layers is None

    def test_app_config_defaults(self):
        """Scenario: Default app config has sensible defaults."""
        cfg = TopoGPT3JLensAppConfig()
        assert cfg.max_seq_len == 512
        assert cfg.use_jacobian is True
        assert cfg.layers is None
        assert cfg.positions is None


class TestTopoGPT3JLensAppConfig:
    """Feature: Application config controls readout behavior."""

    def test_default_config(self):
        """Scenario: Default app config uses all positions."""
        cfg = TopoGPT3JLensAppConfig()
        assert cfg.use_jacobian is True
        assert cfg.max_seq_len == 512
        assert cfg.layers is None
        assert cfg.positions is None

    def test_custom_config(self):
        """Scenario: Custom app config overrides specific layers."""
        cfg = TopoGPT3JLensAppConfig(
            layers=(0, 2, 4),
            positions=(0, -1),
            max_seq_len=256,
            use_jacobian=False,
        )
        assert cfg.layers == (0, 2, 4)
        assert cfg.positions == (0, -1)
        assert cfg.max_seq_len == 256
        assert cfg.use_jacobian is False
