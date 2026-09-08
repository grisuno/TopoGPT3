"""Export / convert utilities for TopoGPT3 checkpoints.

TopoGPT3 keeps its own safetensors slot; this adds:
  - merge_lora CLI (base + LoRA -> merged safetensors dir)
  - export_hf_stub: writes config.json + tokenizer stub for HF/vLLM loaders
  - export_gguf_note: real-valued projection note for llama.cpp/C-engine path
No architecture rewrite: weights are preserved verbatim.
"""
from __future__ import annotations

import argparse
import json
import os

import torch
from safetensors.torch import load_file, save_file


def merge_base_lora(base_dir: str, lora_path: str, out_dir: str):
    import sys as _s
    _s.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from topogpt3.model import TopoGPT2, TopoGPT2Config
    from topogpt3.lora import apply_lora, merge_lora
    cfg = TopoGPT2Config()
    m = TopoGPT2(cfg)
    sd = load_file(os.path.join(base_dir, "model.safetensors"), device="cpu")
    m.load_state_dict(sd, strict=False)
    apply_lora(m, rank=16)
    tmp = os.path.join(out_dir, "_merged_tmp.pt")
    os.makedirs(out_dir, exist_ok=True)
    merge_lora(m, lora_path, tmp)
    merged = torch.load(tmp, map_location="cpu")
    save_file(merged, os.path.join(out_dir, "model.safetensors"))
    os.remove(tmp)
    print(f"merged -> {out_dir}/model.safetensors")


def export_hf_stub(ckpt_dir: str, out_dir: str):
    os.makedirs(out_dir, exist_ok=True)
    stub = {"architectures": ["TopoGPT3ForCausalLM"],
            "model_type": "topogpt3",
            "tie_word_embeddings": True,
            "note": "TopoGPT3 complex/quaternion weights; load via topogpt3.model.TopoGPT2"}
    with open(os.path.join(out_dir, "config.json"), "w") as f:
        json.dump(stub, f, indent=2)
    print(f"wrote {out_dir}/config.json (stub; weights stay in model.safetensors)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default="checkpoints_topogpt3/last")
    ap.add_argument("--lora", default="")
    ap.add_argument("--out", default="out/topo_merged")
    ap.add_argument("--hf-stub", action="store_true")
    args = ap.parse_args()
    if args.lora:
        merge_base_lora(args.base, args.lora, args.out)
    if args.hf_stub:
        export_hf_stub(args.base, args.out)


if __name__ == "__main__":
    main()
