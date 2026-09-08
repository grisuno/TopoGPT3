"""Export the real 4-tier curriculum (HF) to chat JSONL for the heritage trainers.

Reuses CodeCurriculumLoader's dataset IDs + fallback chain, but emits
conversations instead of token bins:

  - sft_all.jsonl      tiers 0..2 (instruction -> user/assistant)
  - rlaif_all.jsonl    tiers 0..2 prompts (assistant left open)
  - dpo_all.jsonl      chosen=ground truth, rejected=truncated 50%
                       (weak but honest bootstrap signal; replace with human
                       prefs when available)
  - pretrain_tier3.jsonl  raw code (tier 3 has no instructions)

Usage:
  python -m topogpt3 export-chat --out-dir data/chat --max-per-tier 20000
"""
from __future__ import annotations

import argparse
import json
import logging
import os
import sys
from typing import Any, Dict, Iterator, List

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def _pairs_codealpaca(ex: Dict[str, Any]):
    i = (ex.get("instruction") or "").strip()
    x = (ex.get("input") or "").strip()
    o = (ex.get("output") or "").strip()
    if not i or not o:
        return None
    u = f"{i}\n{x}" if x else i
    return u, o


def _pairs_code_feedback(ex: Dict[str, Any]):
    q = (ex.get("query") or ex.get("question") or ex.get("instruction") or "").strip()
    a = (ex.get("answer") or ex.get("response") or ex.get("output") or "").strip()
    if q and a:
        return q, a
    msgs = ex.get("messages") or ex.get("conversations") or []
    turns = [(m.get("role", "user"), m.get("content", "")) for m in msgs
             if isinstance(m, dict) and m.get("content")]
    if len(turns) >= 2:
        # last assistant turn = target, rest = context
        *ctx, (rl, rc) = turns
        if "assist" in rl:
            u = "\n".join(c for _, c in ctx[-3:]) or "(continue)"
            return u, rc.strip()
    return None


def _pairs_magicoder(ex: Dict[str, Any]):
    p = (ex.get("instruction") or ex.get("problem") or "").strip()
    s = (ex.get("response") or ex.get("solution") or ex.get("output") or "").strip()
    return (p, s) if p and s else None


_PAIR_FN = {"codealpaca": _pairs_codealpaca, "code_feedback": _pairs_code_feedback,
            "magicoder_evol": _pairs_magicoder}


def _iter_pairs(loader, tier: str, cap: int) -> Iterator[tuple]:
    ds = loader._load_hf_with_fallback(tier)
    fn = _PAIR_FN[tier]
    n = 0
    for ex in ds:
        if n >= cap:
            break
        try:
            r = fn(dict(ex))
        except Exception:
            continue
        if r:
            yield r
            n += 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out-dir", default="data/chat")
    ap.add_argument("--max-per-tier", type=int, default=20000)
    ap.add_argument("--tiers", default="0,1,2")
    args = ap.parse_args()

    try:
        import datasets  # noqa: F401
    except ImportError:
        raise SystemExit(
            "export-chat needs HuggingFace 'datasets' (your env lacks it).\n"
            "  pip install datasets   # or: pip install -e \".[train]\"")
    del datasets

    from topogpt3.train import CodeCurriculumLoader, TopoGPT3Config, setup_logger
    from topogpt3.model import BPETokenizer
    logger = setup_logger("export-chat")
    cfg = TopoGPT3Config()
    loader = CodeCurriculumLoader(cfg, BPETokenizer(), logger)
    os.makedirs(args.out_dir, exist_ok=True)

    tier_names = cfg.TIER_NAMES
    wanted = [tier_names[int(i)] for i in args.tiers.split(",")]
    sft = open(os.path.join(args.out_dir, "sft_all.jsonl"), "w", encoding="utf-8")
    rla = open(os.path.join(args.out_dir, "rlaif_all.jsonl"), "w", encoding="utf-8")
    dpo = open(os.path.join(args.out_dir, "dpo_all.jsonl"), "w", encoding="utf-8")
    n_sft = n_rla = n_dpo = 0
    try:
        for tier in wanted:
            if tier not in _PAIR_FN:
                continue
            for u, a in _iter_pairs(loader, tier, args.max_per_tier):
                sft.write(json.dumps({"conversations": [
                    {"role": "user", "content": u},
                    {"role": "assistant", "content": a}]}) + "\n")
                n_sft += 1
                rla.write(json.dumps({"conversations": [
                    {"role": "user", "content": u},
                    {"role": "assistant", "content": ""}]}) + "\n")
                n_rla += 1
                cut = a[:max(32, len(a) // 2)]
                dpo.write(json.dumps({
                    "chosen": [{"role": "user", "content": u},
                               {"role": "assistant", "content": a}],
                    "rejected": [{"role": "user", "content": u},
                                 {"role": "assistant", "content": cut}]}) + "\n")
                n_dpo += 1
            logger.info(f"[{tier}] exported (cap={args.max_per_tier})")
        # tier 3: raw code pretrain text
        if "tiny_the_stack" in tier_names:
            pre = open(os.path.join(args.out_dir, "pretrain_tier3.jsonl"), "w",
                       encoding="utf-8")
            n_pre = 0
            try:
                ds = loader._load_hf_with_fallback("tiny_the_stack")
                fmt = loader._get_formatter("tiny_the_stack")
                for ex in ds:
                    if n_pre >= args.max_per_tier:
                        break
                    try:
                        t = fmt(dict(ex))
                    except Exception:
                        continue
                    if t:
                        pre.write(json.dumps({"text": t}) + "\n")
                        n_pre += 1
            finally:
                pre.close()
            logger.info(f"[tiny_the_stack] pretrain rows={n_pre}")
    finally:
        sft.close()
        rla.close()
        dpo.close()
    logger.info(f"done: sft={n_sft} rlaif={n_rla} dpo={n_dpo} -> {args.out_dir}")


if __name__ == "__main__":
    main()
