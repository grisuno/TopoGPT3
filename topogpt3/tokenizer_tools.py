"""Tokenizer efficiency toolkit.

Three utilities for the GPT-2 BPE situation of TopoGPT3/TopoExploit:

1. ``audit()`` -- measures how much of the parameter budget goes to the
   shared embedding table and chars/token on a corpus.
2. ``train_code_bpe()`` -- trains a smaller code-aware BPE (HF ``tokenizers``
   optional dependency) and writes a tokenizer artifact.
3. ``resize_embeddings()`` -- maps an old-vocab checkpoint into a new vocab
   (longest-prefix match on token bytes) so retraining starts warm.

Retraining from scratch is required for any vocab change; these utilities
only prepare it.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from collections.abc import Iterable
from pathlib import Path
from typing import Any


def audit(
    checkpoint_dir: str,
    corpus_files: Iterable[str] | None = None,
    sample_chars: int = 200_000,
) -> dict[str, Any]:
    """Embedding share + chars/token stats for the gpt2 BPE identity."""
    from safetensors import safe_open

    path = Path(checkpoint_dir) / "model.safetensors"
    total_params = 0
    embed_params = 0
    with safe_open(str(path), framework="pt", device="cpu") as handle:
        for key in list(handle.keys()):
            tensor = handle.get_tensor(key)
            n = int(tensor.numel())
            total_params += n
            if key == "token_embed.weight":
                embed_params = n
    result = {
        "checkpoint": checkpoint_dir,
        "total_params": total_params,
        "embed_params": embed_params,
        "embed_share": round(embed_params / total_params, 4) if total_params else 0.0,
    }

    files = list(corpus_files or [])
    if files:
        try:
            import tiktoken

            enc = tiktoken.get_encoding("gpt2")
        except Exception:  # noqa: BLE001 - audit is best-effort
            enc = None
        if enc is not None:
            chars = 0
            tokens = 0
            for file in files:
                try:
                    text = Path(file).read_text(errors="ignore")[:sample_chars]
                except OSError:
                    continue
                chars += len(text)
                tokens += len(enc.encode(text))
            if chars:
                result["corpus_files"] = len(files)
                result["chars_per_token"] = round(chars / max(1, tokens), 3)
    return result


def train_code_bpe(
    corpus_files: list[str], out_dir: str, vocab_size: int = 16_000
) -> dict[str, Any]:
    """Train a compact BPE with HF tokenizers (optional dependency)."""
    try:
        from tokenizers import Tokenizer, pre_tokenizers, trainers
        from tokenizers.models import BPE
    except ImportError:
        raise SystemExit(
            "train_code_bpe requires 'tokenizers': pip install 'topogpt3[tokenizers]'"
        )

    files = [f for f in corpus_files if Path(f).is_file()]
    if not files:
        raise SystemExit(f"no corpus files found among {corpus_files}")

    tokenizer = Tokenizer(BPE(unk_token=None))
    tokenizer.pre_tokenizer = pre_tokenizers.ByteLevel(add_prefix_space=False)
    trainer = trainers.BpeTrainer(
        vocab_size=vocab_size,
        special_tokens=["<|pad|>", "<|eos|>", "<|bos|>", "<|user|>", "<|assistant|>"],
        show_progress=False,
    )
    tokenizer.train(files, trainer)
    out_path = Path(out_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    tokenizer.save(str(out_path / "tokenizer.json"))
    return {
        "out_dir": str(out_path),
        "vocab_size": tokenizer.get_vocab_size(),
        "files": files,
    }


def load_tokenizer_artifact(path: str | Path):
    from tokenizers import Tokenizer

    tokenizer = Tokenizer.from_file(str(Path(path) / "tokenizer.json"))
    eot = tokenizer.token_to_id("<|eos|>")

    class ArtifactTokenizer:
        """Drop-in for BPETokenizer consumers (encode/decode/vocab_size)."""

        def __init__(self) -> None:
            self.vocab_size = tokenizer.get_vocab_size()
            self.enc = None

        def encode(self, text: str) -> list[int]:
            return tokenizer.encode(text, add_special_tokens=False).ids

        def decode(self, tokens: Iterable[int]) -> str:
            return tokenizer.decode(list(tokens), skip_special_tokens=True)

        def eot_token(self) -> int:
            return int(eot)

    return ArtifactTokenizer()


def resize_embeddings(
    checkpoint_dir: str, new_vocab: list[bytes], out_dir: str
) -> dict[str, Any]:
    """Warm-start a checkpoint on a new vocab via longest-prefix byte match."""
    import torch
    from safetensors.torch import load_file, save_file

    from topogpt3.checkpoint_meta import config_from_checkpoint

    try:
        import tiktoken

        enc = tiktoken.get_encoding("gpt2")
        old_bytes = [enc.decode_single_token_bytes(i) for i in range(enc.n_vocab)]
    except Exception as exc:  # noqa: BLE001 - clear abort path
        raise SystemExit(f"tiktoken required to rebuild token bytes: {exc}")

    cfg, _meta = config_from_checkpoint(checkpoint_dir, device="cpu")
    sd = load_file(str(Path(checkpoint_dir) / "model.safetensors"), device="cpu")
    old_embed = sd["token_embed.weight"]

    new_embed = torch.empty(len(new_vocab), old_embed.shape[1])
    torch.nn.init.normal_(new_embed, mean=0.0, std=0.02)
    for index, token in enumerate(new_vocab):
        best_len, best_i = -1, 0
        for old_i, old_tok in enumerate(old_bytes):
            length = len(os.path.commonprefix([old_tok, token]))
            if length > best_len:
                best_len, best_i = length, old_i
        new_embed[index] = old_embed[best_i]

    sd["token_embed.weight"] = new_embed
    sd["lm_head.weight"] = new_embed  # tied storage is materialized on load

    out_path = Path(out_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    save_file(sd, str(out_path / "model.safetensors"))
    cfg.VOCAB_SIZE = len(new_vocab)
    (out_path / "state.json").write_text(
        json.dumps({"SCALE": cfg.SCALE, "VOCAB_SIZE": cfg.VOCAB_SIZE})
    )
    return {
        "out_dir": str(out_path),
        "old_vocab": int(old_embed.shape[0]),
        "new_vocab": len(new_vocab),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Tokenizer efficiency toolkit")
    parser.add_argument(
        "--audit",
        nargs="?",
        const="checkpoints_topogpt3",
        default=None,
        help="audit a checkpoint",
    )
    parser.add_argument(
        "--corpus", nargs="*", default=[], help="corpus files for audit/train-bpe"
    )
    parser.add_argument(
        "--train-bpe",
        nargs="*",
        default=None,
        help="train a compact BPE on the given corpus files",
    )
    parser.add_argument("--vocab-size", type=int, default=16_000)
    parser.add_argument("--out-dir", default="tokenizer_out")
    args = parser.parse_args()

    if args.train_bpe is not None:
        print(json.dumps(train_code_bpe(args.train_bpe, args.out_dir, args.vocab_size)))
        return 0
    if args.audit is not None:
        print(json.dumps(audit(args.audit, args.corpus)))
        return 0
    parser.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
