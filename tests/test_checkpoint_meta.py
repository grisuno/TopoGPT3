"""Checkpoint architecture discovery tests."""

import pytest

from topogpt3.checkpoint_meta import (
    config_from_checkpoint,
    probe_checkpoint,
    read_state,
)


def test_read_state_missing(tmp_path):
    assert read_state(tmp_path) == {}


def test_probe_t3_small():
    cfg, meta = config_from_checkpoint("checkpoints_topogpt3/last", device="cpu")
    assert meta["scale"] == "small"
    assert cfg.D_MODEL == 256 and cfg.N_LAYERS == 6
    assert cfg.N_KV_HEADS == 2
    assert cfg.MAX_SEQ_LEN == 512


def test_probe_exploitgym_meta():
    pytest.importorskip("safetensors")
    meta = probe_checkpoint("checkpoints_topogpt3/last")
    assert meta["vocab_size"] == 50257
    assert meta["d_model"] == 256


def test_config_matches_weights():
    cfg, meta = config_from_checkpoint("checkpoints_topogpt3/last", device="cpu")
    assert cfg.D_MODEL == meta["d_model"]
    assert cfg.N_LAYERS == meta["n_layers"]
