#!/usr/bin/env python3
"""
TopoGPT3 Weight Converter: safetensors -> flat float32 binary.

Usage:
    python convert_weights.py [--input model.safetensors] [--output topogpt3.weights]

Output format:
    Header: "TG3W" + uint32 version(1) + uint32 n_tensors
    For each tensor: uint32 name_len + char[name_len] + uint32 ndim + uint32 dims[ndim] + float32[data]

The C inference engine loads this file sequentially.
"""
import struct
import sys
import argparse
from pathlib import Path

try:
    from safetensors import safe_open
except ImportError:
    print("Error: safetensors not installed. pip install safetensors", file=sys.stderr)
    sys.exit(1)


# Weight loading order for the C inference engine
WEIGHT_ORDER = [
    "token_embed.weight",
]

for i in range(6):
    WEIGHT_ORDER += [
        f"layers.{i}.norm1.weight",
        f"layers.{i}.norm2.weight",
        f"layers.{i}.attn.q_proj.weight",
        f"layers.{i}.attn.k_proj.weight",
        f"layers.{i}.attn.v_proj.weight",
        f"layers.{i}.attn.o_proj.weight",
        f"layers.{i}.attn.temperature",
        # Spectral autoencoder 1D kernels
        f"layers.{i}.topo_brain.shared_expert.spectral_ae.enc_kr",
        f"layers.{i}.topo_brain.shared_expert.spectral_ae.enc_ki",
        f"layers.{i}.topo_brain.shared_expert.spectral_ae.dec_kr",
        f"layers.{i}.topo_brain.shared_expert.spectral_ae.dec_ki",
        # Spectral autoencoder quaternion projections
        f"layers.{i}.topo_brain.shared_expert.spectral_ae.enc_proj.Ww.weight",
        f"layers.{i}.topo_brain.shared_expert.spectral_ae.enc_proj.Wx.weight",
        f"layers.{i}.topo_brain.shared_expert.spectral_ae.enc_proj.Wy.weight",
        f"layers.{i}.topo_brain.shared_expert.spectral_ae.enc_proj.Wz.weight",
        f"layers.{i}.topo_brain.shared_expert.spectral_ae.dec_proj.Ww.weight",
        f"layers.{i}.topo_brain.shared_expert.spectral_ae.dec_proj.Wx.weight",
        f"layers.{i}.topo_brain.shared_expert.spectral_ae.dec_proj.Wy.weight",
        f"layers.{i}.topo_brain.shared_expert.spectral_ae.dec_proj.Wz.weight",
        # Spectral 2D layers (2 layers, 8 kernels each)
        *[
            f"layers.{i}.topo_brain.shared_expert.spectral_ae.torus_spectral.{j}.kr_{c}"
            for j in range(2) for c in ("w", "x", "y", "z")
        ],
        *[
            f"layers.{i}.topo_brain.shared_expert.spectral_ae.torus_spectral.{j}.ki_{c}"
            for j in range(2) for c in ("w", "x", "y", "z")
        ],
        # Torus projection
        f"layers.{i}.topo_brain.shared_expert.torus_proj.0.Ww.weight",
        f"layers.{i}.topo_brain.shared_expert.torus_proj.0.Wx.weight",
        f"layers.{i}.topo_brain.shared_expert.torus_proj.0.Wy.weight",
        f"layers.{i}.topo_brain.shared_expert.torus_proj.0.Wz.weight",
        f"layers.{i}.topo_brain.shared_expert.torus_proj.2.weight",
        # Node and edge embeddings
        f"layers.{i}.topo_brain.shared_expert.node_embed",
        f"layers.{i}.topo_brain.shared_expert.edge_quat",
        # Message passing network
        f"layers.{i}.topo_brain.shared_expert.node_net.Ww.weight",
        f"layers.{i}.topo_brain.shared_expert.node_net.Wx.weight",
        f"layers.{i}.topo_brain.shared_expert.node_net.Wy.weight",
        f"layers.{i}.topo_brain.shared_expert.node_net.Wz.weight",
        # Readout
        f"layers.{i}.topo_brain.shared_expert.readout.0.weight",
        f"layers.{i}.topo_brain.shared_expert.readout.0.bias",
        f"layers.{i}.topo_brain.shared_expert.readout.2.weight",
        f"layers.{i}.topo_brain.shared_expert.readout.2.bias",
        # MoE experts (4 experts, 3 weight matrices each)
        *[
            f"layers.{i}.topo_brain.experts.{e}.gate_proj.weight"
            for e in range(4)
        ],
        *[
            f"layers.{i}.topo_brain.experts.{e}.up_proj.weight"
            for e in range(4)
        ],
        *[
            f"layers.{i}.topo_brain.experts.{e}.down_proj.weight"
            for e in range(4)
        ],
        # MoE router
        f"layers.{i}.topo_brain.router.weight",
    ]

WEIGHT_ORDER.append("final_norm.weight")


def convert(input_path: str, output_path: str):
    print(f"Loading safetensors: {input_path}")
    st = safe_open(input_path, framework="pt", device="cpu")

    all_keys = set(st.keys())
    ordered_keys = [k for k in WEIGHT_ORDER if k in all_keys]
    missing = [k for k in WEIGHT_ORDER if k not in all_keys]
    extra = [k for k in all_keys if k not in WEIGHT_ORDER]

    if missing:
        print(f"Warning: {len(missing)} expected keys missing from checkpoint:")
        for k in missing[:10]:
            print(f"  - {k}")
        if len(missing) > 10:
            print(f"  ... and {len(missing) - 10} more")

    if extra:
        print(f"Info: {len(extra)} extra keys in checkpoint (not loaded):")
        for k in extra[:10]:
            print(f"  + {k}")

    total_params = 0
    tensors = []
    for key in ordered_keys:
        t = st.get_tensor(key)
        # Convert to float32
        t = t.float()
        data = t.numpy().tobytes()
        n_elements = t.numel()
        total_params += n_elements
        tensors.append((key, t.shape, data))
        print(f"  {key}: {list(t.shape)} ({n_elements:,} params, {len(data)} bytes)")

    print(f"\nTotal parameters: {total_params:,}")
    print(f"Total size: {total_params * 4:,} bytes ({total_params * 4 / 1024 / 1024:.1f} MB)")

    # Write binary file
    print(f"\nWriting: {output_path}")
    with open(output_path, "wb") as f:
        # Header: magic + version + n_tensors
        f.write(b"TG3W")
        f.write(struct.pack("<I", 1))  # version
        f.write(struct.pack("<I", len(tensors)))

        for key, shape, data in tensors:
            key_bytes = key.encode("utf-8")
            f.write(struct.pack("<I", len(key_bytes)))
            f.write(key_bytes)
            f.write(struct.pack("<I", len(shape)))
            for dim in shape:
                f.write(struct.pack("<I", dim))
            f.write(data)

    out_size = Path(output_path).stat().st_size
    print(f"Written {out_size:,} bytes ({out_size / 1024 / 1024:.1f} MB)")
    print("Done.")


def main():
    parser = argparse.ArgumentParser(description="Convert TopoGPT3 safetensors to binary weights")
    parser.add_argument("--input", "-i", default="checkpoints_topogpt3/last/model.safetensors",
                        help="Input safetensors file")
    parser.add_argument("--output", "-o", default="topogpt3.weights",
                        help="Output binary weights file")
    args = parser.parse_args()
    convert(args.input, args.output)


if __name__ == "__main__":
    main()
