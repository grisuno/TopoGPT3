"""JSONL chat datasets (SFT / DPO / RLAIF / Agent) for TopoGPT3.

Assistant-only loss masking over multi-turn chats; tokenizes with
TopoGPT3's BPETokenizer (tiktoken) + topogpt3.chat template. Identity safe:
no tokenizer change, no architecture change; only (input_ids, labels, mask).
"""
from __future__ import annotations

import json
import os
from typing import Any, Dict, List

import torch
from torch.utils.data import Dataset

from .chat import BOS, EOS, apply_chat_template, pre_processing_chat


class _JSONLLoader:
    @staticmethod
    def load(path: str) -> List[Dict[str, Any]]:
        if not os.path.exists(path):
            raise FileNotFoundError(
                f"dataset not found: {path}\n"
                f"  - quick smoke files: data/sft_toolcall.jsonl, data/dpo.jsonl, "
                f"data/rlaif.jsonl, data/agent_rl.jsonl\n"
                f"  - real curriculum data: python -m topogpt3 export-chat "
                f"--out-dir data/chat (needs: pip install datasets)")
        rows = []
        with open(path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    rows.append(json.loads(line))
        if not rows:
            raise ValueError(f"dataset is empty: {path}")
        return rows


class _TokAdapter:
    """Wrap BPETokenizer (encode/decode list[int]) with a small encode API."""

    def __init__(self, tok, max_length: int):
        self.tok = tok
        self.max_length = max_length
        # Encode markers once for masking
        self.bos_ids = tok.encode(f"{BOS}assistant\n")
        self.eos_ids = tok.encode(f"{EOS}\n")
        try:
            self.eot = tok.eot_token()
        except Exception:
            self.eot = None

    def encode(self, text: str) -> List[int]:
        ids = self.tok.encode(text)
        return ids[: self.max_length]


def _assistant_mask(input_ids: List[int], bos_ids: List[int],
                    eos_ids: List[int]) -> List[int]:
    labels = [-100] * len(input_ids)
    if not bos_ids:
        return labels
    i = 0
    while i < len(input_ids):
        if input_ids[i:i + len(bos_ids)] == bos_ids:
            start = i + len(bos_ids)
            end = start
            while end < len(input_ids):
                if eos_ids and input_ids[end:end + len(eos_ids)] == eos_ids:
                    break
                end += 1
            stop = min(end + len(eos_ids), len(input_ids)) if eos_ids else end
            for j in range(start, stop):
                labels[j] = input_ids[j]
            i = stop
        else:
            i += 1
    return labels


class SFTDatasetJSONL(Dataset):
    """Expects {"conversations": [{role, content, ...}]} per line."""

    def __init__(self, path: str, tokenizer, max_length: int = 1024):
        self.rows = _JSONLLoader.load(path)
        self.ad = _TokAdapter(tokenizer, max_length)
        self.max_length = max_length

    def __len__(self):
        return len(self.rows)

    def __getitem__(self, idx):
        convs = pre_processing_chat(self.rows[idx]["conversations"])
        tools = None
        msgs = []
        for m in convs:
            m = dict(m)
            if m.get("role") == "system" and m.get("tools"):
                import json as _j
                tools = _j.loads(m["tools"]) if isinstance(m["tools"], str) else m["tools"]
            if isinstance(m.get("tool_calls"), str):
                import json as _j
                try:
                    m["tool_calls"] = _j.loads(m["tool_calls"])
                except Exception:
                    pass
            msgs.append(m)
        prompt = apply_chat_template(msgs, tools=tools)
        ids = self.ad.encode(prompt)
        pad = 0
        if len(ids) < self.max_length:
            ids = ids + [pad] * (self.max_length - len(ids))
        labels = _assistant_mask(ids, self.ad.bos_ids, self.ad.eos_ids)
        return torch.tensor(ids, dtype=torch.long), torch.tensor(labels, dtype=torch.long)


class DPODatasetJSONL(Dataset):
    """Expects {"chosen": [...], "rejected": [...]} per line."""

    def __init__(self, path: str, tokenizer, max_length: int = 1024):
        self.rows = _JSONLLoader.load(path)
        self.ad = _TokAdapter(tokenizer, max_length)
        self.max_length = max_length

    def __len__(self):
        return len(self.rows)

    def _encode(self, convs):
        # NOTE: y keeps RAW token ids (never -100) for gather-safe indexing;
        # the mask alone decides which positions count. -100 in y would crash
        # torch.gather (CUDA device-side assert).
        prompt = apply_chat_template([dict(m) for m in convs])
        ids = self.ad.encode(prompt)
        pad = 0
        if len(ids) < self.max_length:
            ids = ids + [pad] * (self.max_length - len(ids))
        labels = _assistant_mask(ids, self.ad.bos_ids, self.ad.eos_ids)
        mask = [1 if l != -100 else 0 for l in labels]
        return ids, ids, mask

    def __getitem__(self, idx):
        r = self.rows[idx]
        xc, yc, mc = self._encode(r["chosen"])
        xr, yr, mr = self._encode(r["rejected"])
        return {"x_chosen": torch.tensor(xc), "y_chosen": torch.tensor(yc),
                "mask_chosen": torch.tensor(mc, dtype=torch.float),
                "x_rejected": torch.tensor(xr), "y_rejected": torch.tensor(yr),
                "mask_rejected": torch.tensor(mr, dtype=torch.float)}


class RLAIFDatasetJSONL(Dataset):
    """Prompt-only: keeps conversations[:-1], leaves last assistant open."""

    def __init__(self, path: str, tokenizer, max_length: int = 1024,
                 thinking_ratio: float = 0.9):
        self.rows = _JSONLLoader.load(path)
        self.tok = tokenizer
        self.max_length = max_length
        self.thinking_ratio = thinking_ratio

    def __len__(self):
        return len(self.rows)

    def __getitem__(self, idx):
        import random as _r
        r = self.rows[idx]
        convs = r.get("conversations", r.get("chosen", []))
        msgs = [dict(m) for m in convs[:-1]] if convs else []
        open_th = _r.random() < self.thinking_ratio
        prompt = apply_chat_template(msgs, add_generation_prompt=True,
                                     open_thinking=open_th)
        return {"prompt": prompt}


class AgentRLDatasetJSONL(Dataset):
    def __init__(self, path: str, tokenizer, max_length: int = 1024):
        self.rows = _JSONLLoader.load(path)

    def __len__(self):
        return len(self.rows)

    def __getitem__(self, idx):
        r = self.rows[idx]
        convs = r.get("conversations", [])
        tools = r.get("tools")
        gt = r.get("gt", r.get("ground_truth", ""))
        msgs = [dict(m) for m in convs[:-1]] if convs else []
        return {"messages": msgs, "tools": tools, "gt": gt,
                "prompt": apply_chat_template(msgs, tools=tools,
                                              add_generation_prompt=True)}
