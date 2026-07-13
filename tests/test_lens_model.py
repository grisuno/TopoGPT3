from __future__ import annotations

import pytest
import torch

from topogpt3.lens_model import (
    TopoGPT3LensConfig,
    TopoGPT3LensModel,
    TinyDecoder,
)


class TestTopoGPT3LensConfig:
    """Feature: TopoGPT3LensConfig provides centralized adapter configuration."""

    def test_default_config(self):
        """Scenario: Default config matches small scale preset."""
        cfg = TopoGPT3LensConfig()
        assert cfg.d_model == 256
        assert cfg.n_layers == 6
        assert cfg.n_heads == 8
        assert cfg.vocab_size == 50257
        assert cfg.max_seq_len == 256

    def test_from_topogpt2_config(self):
        """Scenario: Build lens config from TopoGPT2Config."""
        from topogpt3.model import TopoGPT2Config

        model_cfg = TopoGPT2Config(SCALE="medium", DEVICE="cpu")
        lens_cfg = TopoGPT3LensConfig.from_topogpt2_config(model_cfg)
        assert lens_cfg.d_model == 512
        assert lens_cfg.n_layers == 12
        assert lens_cfg.d_model == model_cfg.D_MODEL

    def test_probe_checkpoint_missing_raises(self, tmp_path):
        """Scenario: Missing state.json raises FileNotFoundError."""
        with pytest.raises(FileNotFoundError, match="State file not found"):
            TopoGPT3LensConfig.probe_checkpoint(str(tmp_path))


class TestTinyDecoder:
    """Feature: TinyDecoder provides a minimal test model."""

    def test_default_parameters(self):
        """Scenario: TinyDecoder has correct default shape."""
        model = TinyDecoder()
        assert len(model.layers) == 4
        assert model.config.D_MODEL == 8
        assert model.lm_head.out_features == 32

    def test_forward_output_shape(self):
        """Scenario: Forward pass produces correct logit shape."""
        model = TinyDecoder()
        ids = torch.randint(0, 32, (2, 10))
        logits, aux_loss, kvs = model(ids)
        assert logits.shape == (2, 10, 32)
        assert aux_loss.numel() == 1

    def test_weight_tied(self):
        """Scenario: Embedding and LM head share weights."""
        model = TinyDecoder()
        assert model.lm_head.weight is model.token_embed.weight


class TestTopoGPT3LensModel:
    """Feature: TopoGPT3LensModel wraps a model to implement LensModel protocol."""

    @pytest.fixture
    def raw_model(self):
        model = TinyDecoder()
        model.eval()
        for p in model.parameters():
            p.requires_grad_(False)
        return model

    @pytest.fixture
    def lens_model(self, raw_model):
        return TopoGPT3LensModel(raw_model)

    def test_exposes_protocol_attributes(self, lens_model, raw_model):
        """Scenario: LensModel attributes match underlying model."""
        assert lens_model.n_layers == len(raw_model.layers)
        assert lens_model.d_model == raw_model.config.D_MODEL
        assert lens_model.layers is raw_model.layers
        assert lens_model.tokenizer is None

    def test_encode_text_to_token_ids(self, lens_model):
        """Scenario: encode() returns tensor of shape [1, seq_len]."""
        input_ids = lens_model.encode("hello world", max_length=128)
        assert input_ids.dtype == torch.long
        assert input_ids.dim() == 2
        assert input_ids.shape[0] == 1
        assert 1 < input_ids.shape[1] <= 128

    def test_encode_with_tokenizer(self):
        """Scenario: encode() uses BPETokenizer when available."""
        from topogpt3.model import BPETokenizer

        model = TinyDecoder()
        model.eval()
        tokenizer = BPETokenizer()
        lm = TopoGPT3LensModel(model, tokenizer=tokenizer)
        input_ids = lm.encode("def fibonacci(n):", max_length=64)
        assert input_ids.shape[0] == 1
        assert 1 < input_ids.shape[1] <= 64

    def test_encode_respects_max_length(self, lens_model):
        """Scenario: encode() truncates at max_length."""
        long_text = "hello world " * 200
        input_ids = lens_model.encode(long_text, max_length=16)
        assert input_ids.shape[1] <= 16

    def test_forward_returns_residual_only(self):
        """Scenario: forward() returns hidden states with d_model dim, not vocab.

        The lens model forward should stop before final_norm and lm_head.
        The output should have d_model as last dimension, not vocab_size.
        """
        raw = TinyDecoder(n_layers=4, d_model=8)
        raw.eval()
        lm = TopoGPT3LensModel(raw)
        ids = torch.randint(0, 32, (1, 8))
        with torch.no_grad():
            hidden = lm.forward(ids)
        assert hidden.shape == (1, 8, lm.d_model)
        assert hidden.dtype == torch.float32

    def test_forward_differs_from_full_model(self):
        """Scenario: Residual forward shape differs from full model logits."""
        raw = TinyDecoder(n_layers=4, d_model=8)
        raw.eval()
        lm = TopoGPT3LensModel(raw)
        ids = torch.randint(0, 32, (1, 8))
        with torch.no_grad():
            logits, _, _ = raw(ids)
            hidden = lm.forward(ids)
        assert logits.shape[-1] == 32
        assert hidden.shape[-1] == lm.d_model
        assert logits.shape[-1] != hidden.shape[-1]

    def test_unembed_produces_logits(self, lens_model):
        """Scenario: unembed() maps residual to logits."""
        with torch.no_grad():
            ids = torch.randint(0, 32, (1, 8))
            hidden = lens_model.forward(ids)
            logits = lens_model.unembed(hidden)
        assert logits.shape == (1, 8, 32)
        assert logits.dtype == torch.float32

    def test_forward_plus_unembed_matches_model_logits(self, lens_model, raw_model):
        """Scenario: residual forward + unembed == model forward logits.

        This validates that our split forward matches the original model's
        full forward pass.
        """
        ids = torch.randint(0, 32, (1, 8))
        with torch.no_grad():
            expected_logits, _, _ = raw_model(ids)
            hidden = lens_model.forward(ids)
            actual_logits = lens_model.unembed(hidden)
        torch.testing.assert_close(actual_logits, expected_logits, rtol=1e-5, atol=1e-5)

    def test_autograd_graph_tracks_through_layers(self):
        """Scenario: Gradient flows through residual layers when grads enabled."""
        raw = TinyDecoder(n_layers=4, d_model=8, seed=42)
        lm = TopoGPT3LensModel(raw)
        ids = torch.randint(0, 32, (1, 8))
        hidden = lm.forward(ids)
        loss = hidden.sum()
        loss.backward()
        has_grad = any(
            p.grad is not None and p.grad.abs().sum() > 0
            for p in raw.layers.parameters()
        )
        assert has_grad
        # Cleanup
        for p in raw.parameters():
            p.grad = None

    def test_input_device_property(self, lens_model):
        """Scenario: input_device returns the embedding weight device."""
        device = lens_model.input_device
        assert device == lens_model._model.token_embed.weight.device

    def test_input_device_setter(self, lens_model):
        """Scenario: input_device can be overridden."""
        device = torch.device("cpu")
        lens_model.input_device = device
        assert lens_model.input_device == device

    def test_tokenizer_setter(self, lens_model):
        """Scenario: tokenizer can be set after construction."""
        from types import SimpleNamespace
        fake = SimpleNamespace(decode=lambda x: "test")
        lens_model.tokenizer = fake
        assert lens_model.tokenizer is fake

    def test_from_checkpoint_missing_raises(self):
        """Scenario: from_checkpoint with missing directory raises."""
        with pytest.raises(FileNotFoundError, match="Weights not found"):
            TopoGPT3LensModel.from_checkpoint(
                "/nonexistent/path", device="cpu"
            )

    def test_grad_enabled_deterministic(self, lens_model):
        """Scenario: Multiple forward passes with same input are deterministic."""
        ids = torch.randint(0, 32, (1, 8))
        with torch.no_grad():
            h1 = lens_model.forward(ids)
            h2 = lens_model.forward(ids)
        torch.testing.assert_close(h1, h2)


class TestTopoGPT3LensModelWithRecording:
    """Feature: ActivationRecorder works with TopoGPT3LensModel."""

    @pytest.fixture
    def lens_model(self):
        model = TinyDecoder()
        model.eval()
        for p in model.parameters():
            p.requires_grad_(False)
        return TopoGPT3LensModel(model)

    def test_recorder_captures_layer_outputs(self, lens_model):
        """Scenario: ActivationRecorder captures all requested layer outputs."""
        from topogpt3.jlens import ActivationRecorder

        ids = lens_model.encode("test prompt", max_length=32)
        layers = [0, 1, 2]
        with ActivationRecorder(lens_model.layers, at=layers) as recorder:
            lens_model.forward(ids)
        for layer in layers:
            assert layer in recorder.activations
            assert recorder.activations[layer].shape[0] == 1
            assert recorder.activations[layer].shape[-1] == lens_model.d_model

    def test_recorder_with_start_graph_at(self, lens_model):
        """Scenario: start_graph_at roots the autograd graph."""
        from topogpt3.jlens import ActivationRecorder

        ids = lens_model.encode("test prompt", max_length=32)
        with (
            ActivationRecorder(
                lens_model.layers, at=[0, 2, 3], start_graph_at=0
            ) as recorder,
            torch.enable_grad(),
        ):
            lens_model.forward(ids)
        assert recorder.activations[0].requires_grad is True

    def test_recorder_cleanup_on_exception(self, lens_model):
        """Scenario: Hooks are removed even if construction fails."""
        from topogpt3.jlens import ActivationRecorder

        with pytest.raises(IndexError):
            with ActivationRecorder(lens_model.layers, at=[999]) as recorder:
                pass
        # Should not raise - hooks were cleaned up.
        with ActivationRecorder(lens_model.layers, at=[0]) as recorder:
            pass
        assert 0 not in recorder.activations

    def test_recorder_detach_after_forward(self, lens_model):
        """Scenario: Activations can be detached after recorder exits."""
        from topogpt3.jlens import ActivationRecorder

        ids = lens_model.encode("test prompt", max_length=32)
        with ActivationRecorder(lens_model.layers, at=[0, 1]) as recorder:
            lens_model.forward(ids)
        captured = {
            i: recorder.activations[i].detach() for i in [0, 1]
        }
        for t in captured.values():
            assert t.requires_grad is False


class TestTopoGPT3LensModelEdgeCases:
    """Feature: Edge cases are handled gracefully."""

    def test_empty_sequence(self):
        """Scenario: Empty input produces error or minimal output."""
        model = TinyDecoder()
        model.eval()
        lm = TopoGPT3LensModel(model)
        ids = torch.randint(0, 32, (1, 0))
        with torch.no_grad():
            hidden = lm.forward(ids)
        assert hidden.shape == (1, 0, model.config.D_MODEL)

    def test_single_token(self):
        """Scenario: Single token input works."""
        model = TinyDecoder()
        model.eval()
        lm = TopoGPT3LensModel(model)
        ids = torch.tensor([[5]])
        with torch.no_grad():
            hidden = lm.forward(ids)
        assert hidden.shape == (1, 1, model.config.D_MODEL)
