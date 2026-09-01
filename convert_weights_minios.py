#!/usr/bin/env python3
"""Convert TopoGPT3 safetensors weights to float16 binary for MiniOS.

Produces a compact weight file (~47MB vs 94MB float32) that fits on MiniFS.
The C engine loads float16 and converts to float32 on the fly.

Usage:
    python convert_weights_minios.py -i checkpoint.safetensors -o topogpt3.fp16

Binary format (TG16):
    4 bytes: magic "TG16"
    4 bytes: version (2)
    4 bytes: number of tensors
    For each tensor:
        4 bytes: name length
        N bytes: name (UTF-8)
        4 bytes: ndim
        4 bytes × ndim: dimensions
        2 bytes × total_elements: float16 data (little-endian IEEE 754)
"""

import argparse
import struct
import numpy as np
import sys

try:
    from safetensors import safe_open
except ImportError:
    print("Error: safetensors not installed. pip install safetensors", file=sys.stderr)
    sys.exit(1)

# Same weight ordering as convert_weights.py
WEIGHT_ORDER = ["token_embed.weight"]

for i in range(6):
    WEIGHT_ORDER += [
        f"layers.{i}.norm1.weight",
        f"layers.{i}.norm2.weight",
        f"layers.{i}.attn.q_proj.weight",
        f"layers.{i}.attn.k_proj.weight",
        f"layers.{i}.attn.v_proj.weight",
        f"layers.{i}.attn.o_proj.weight",
        f"layers.{i}.attn.temperature",
        f"layers.{i}.topo_brain.shared_expert.spectral_ae.enc_kr",
        f"layers.{i}.topo_brain.shared_expert.spectral_ae.enc_ki",
        f"layers.{i}.topo_brain.shared_expert.spectral_ae.dec_kr",
        f"layers.{i}.topo_brain.shared_expert.spectral_ae.dec_ki",
        f"layers.{i}.topo_brain.shared_expert.spectral_ae.enc_proj.Ww.weight",
        f"layers.{i}.topo_brain.shared_expert.spectral_ae.enc_proj.Wx.weight",
        f"layers.{i}.topo_brain.shared_expert.spectral_ae.enc_proj.Wy.weight",
        f"layers.{i}.topo_brain.shared_expert.spectral_ae.enc_proj.Wz.weight",
        f"layers.{i}.topo_brain.shared_expert.spectral_ae.dec_proj.Ww.weight",
        f"layers.{i}.topo_brain.shared_expert.spectral_ae.dec_proj.Wx.weight",
        f"layers.{i}.topo_brain.shared_expert.spectral_ae.dec_proj.Wy.weight",
        f"layers.{i}.topo_brain.shared_expert.spectral_ae.dec_proj.Wz.weight",
        *[f"layers.{i}.topo_brain.shared_expert.spectral_ae.torus_spectral.{j}.kr_{c}"
          for j in range(2) for c in ("w", "x", "y", "z")],
        *[f"layers.{i}.topo_brain.shared_expert.spectral_ae.torus_spectral.{j}.ki_{c}"
          for j in range(2) for c in ("w", "x", "y", "z")],
        f"layers.{i}.topo_brain.shared_expert.torus_proj.0.Ww.weight",
        f"layers.{i}.topo_brain.shared_expert.torus_proj.0.Wx.weight",
        f"layers.{i}.topo_brain.shared_expert.torus_proj.0.Wy.weight",
        f"layers.{i}.topo_brain.shared_expert.torus_proj.0.Wz.weight",
        f"layers.{i}.topo_brain.shared_expert.torus_proj.2.weight",
        f"layers.{i}.topo_brain.shared_expert.node_embed",
        f"layers.{i}.topo_brain.shared_expert.edge_quat",
        f"layers.{i}.topo_brain.shared_expert.node_net.Ww.weight",
        f"layers.{i}.topo_brain.shared_expert.node_net.Wx.weight",
        f"layers.{i}.topo_brain.shared_expert.node_net.Wy.weight",
        f"layers.{i}.topo_brain.shared_expert.node_net.Wz.weight",
        f"layers.{i}.topo_brain.shared_expert.readout.0.weight",
        f"layers.{i}.topo_brain.shared_expert.readout.0.bias",
        f"layers.{i}.topo_brain.shared_expert.readout.2.weight",
        f"layers.{i}.topo_brain.shared_expert.readout.2.bias",
        *[f"layers.{i}.topo_brain.experts.{e}.gate_proj.weight" for e in range(4)],
        *[f"layers.{i}.topo_brain.experts.{e}.up_proj.weight" for e in range(4)],
        *[f"layers.{i}.topo_brain.experts.{e}.down_proj.weight" for e in range(4)],
        f"layers.{i}.topo_brain.router.weight",
    ]

WEIGHT_ORDER.append("final_norm.weight")


def main():
    parser = argparse.ArgumentParser(description='Convert weights to float16 for MiniOS')
    parser.add_argument('-i', '--input', required=True, help='Input safetensors file')
    parser.add_argument('-o', '--output', default='topogpt3.fp16', help='Output float16 binary')
    args = parser.parse_args()

    with safe_open(args.input, framework='numpy') as f:
        all_keys = set(f.keys())
        ordered_keys = [k for k in WEIGHT_ORDER if k in all_keys]
        missing = [k for k in WEIGHT_ORDER if k not in all_keys]

        if missing:
            print(f"Warning: {len(missing)} expected keys missing:")
            for k in missing[:10]:
                print(f"  - {k}")

        print(f"Converting {len(ordered_keys)} tensors to float16...")

        with open(args.output, 'wb') as out:
            out.write(b'TG16')
            out.write(struct.pack('<I', 2))
            out.write(struct.pack('<I', len(ordered_keys)))

            for name in ordered_keys:
                t = f.get_tensor(name).astype(np.float32)
                name_bytes = name.encode('utf-8')
                out.write(struct.pack('<I', len(name_bytes)))
                out.write(name_bytes)
                ndim = len(t.shape)
                out.write(struct.pack('<I', ndim))
                for d in t.shape:
                    out.write(struct.pack('<I', d))
                t16 = t.astype(np.float16)
                out.write(t16.tobytes())

    import os
    size = os.path.getsize(args.output)
    print(f"Written {args.output}: {size:,} bytes ({size/1024/1024:.1f} MB)")


if __name__ == '__main__':
    main()
