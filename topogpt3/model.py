#!/usr/bin/env python3
"""
TopoGPT2: Quaternion-Enhanced Topological Transformer Language Model

Author: Gris Iscomeback
Email: grisiscomeback@gmail.com
License: GPL v3

Mejoras sobre topogpt.py:
- Álgebra de cuaterniones completa (QuaternionLinear, QuaternionSpectralLayer)
  con producto de Hamilton en el dominio de frecuencia para capturar la
  espectrografía de los datos con kernels reales e imaginarios cruzados.
- SpectralAutoencoder: encoder/decoder espectral que comprime y reconstruye
  las representaciones en el dominio de frecuencia.
- QuaternionTorusBrain VECTORIZADA (sin bucles sobre seq_len): proyección
  geométrica sobre el toro con asignación blanda usando distancias circulares,
  message-passing con rotaciones de cuaterniones.
- 8 nodos (RADIAL=2 × ANGULAR=4), 4 ángulos, 2 radiales (spec del usuario).
- Rotary Position Embeddings (RoPE).
- Flash-attention (scaled_dot_product_attention de PyTorch 2.0+).
- RMSNorm en lugar de LayerNorm (estilo LLaMA).
- Tokenizador BPE via tiktoken (vocab GPT-2, 50k tokens).
- Descargador de corpus: TinyStories, WikiText-103, raw file.
- Entrenamiento con AMP (mixed precision) + acumulación de gradientes.
- Presets de escala: micro, small, medium, gpt2.
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.checkpoint import checkpoint as grad_ckpt
from safetensors.torch import save_file as st_save, load_file as st_load
import numpy as np
import math
import os
import sys
import time
from pathlib import Path
import json
import hashlib
import logging
import warnings
import argparse
from datetime import datetime
from typing import Dict, Tuple, Optional, List, Any, Union
from dataclasses import dataclass, asdict
from collections import deque

warnings.filterwarnings('ignore')

# ============================================================================
# CONFIGURACIÓN
# ============================================================================

@dataclass
class TopoGPT2Config:
    """Configuración completa para TopoGPT2."""

    # --- Dispositivo ---
    DEVICE: str = 'cuda' if torch.cuda.is_available() else 'cpu'
    RANDOM_SEED: int = 42
    USE_AMP: bool = True

    # --- Escala del modelo: 'micro' | 'small' | 'medium' | 'gpt2' | 'custom' ---
    SCALE: str = 'small'

    # --- Vocabulario (GPT-2 BPE via tiktoken) ---
    VOCAB_SIZE: int = 50257
    MAX_SEQ_LEN: int = 512

    # --- Arquitectura (sobrescritos por SCALE salvo SCALE='custom') ---
    D_MODEL: int = 256   # debe ser divisible por 4 (cuaterniones) y N_HEADS
    N_HEADS: int = 8
    N_KV_HEADS: int = 0  # GQA: cabezas K/V (0 = N_HEADS//4, -1 = MHA completo)
    N_LAYERS: int = 6
    DROPOUT: float = 0.1

    # --- MoE (Mixture of Experts) ---
    MOE_ENABLED: bool = True          # activar MoE en cada capa
    N_EXPERTS: int = 4                # expertos SwiGLU por capa
    MOE_TOP_K: int = 2                # expertos activos por token (sparse)
    MOE_AUX_LOSS_WEIGHT: float = 0.01 # load-balancing loss

    # --- Topología del toro (spec usuario: 8 nodos = 4 ang × 2 rad) ---
    TORUS_GRID_SIZE: int = 8       # Grid para SpectralLayer (8×8 FFT2)
    TORUS_RADIAL_BINS: int = 2     # 2 niveles radiales
    TORUS_ANGULAR_BINS: int = 4    # 4 ángulos (= 4 nodos por anillo)
    # Total nodos en el grafo toro: 2 × 4 = 8

    # --- Espectral / Autoencoder ---
    SPECTRAL_LATENT_RATIO: float = 0.5   # latent_dim = D_MODEL * ratio
    SPECTRAL_KERNEL_INIT_SCALE: float = 0.02
    NUM_SPECTRAL_LAYERS: int = 2
    AE_RECON_WEIGHT: float = 0.01        # peso de la pérdida de reconstrucción

    # --- Training ---
    BATCH_SIZE: int = 4                  # reduced to fit 6GB VRAM
    GRAD_ACCUM_STEPS: int = 8            # effective batch = 32
    LEARNING_RATE: float = 3e-4
    WEIGHT_DECAY: float = 0.1
    EPOCHS: int = 10
    WARMUP_RATIO: float = 0.05
    GRADIENT_CLIP_NORM: float = 1.0
    GRADIENT_CHECKPOINTING: bool = True  # trades compute for memory

    # --- Curriculum Learning ---
    CURRICULUM_ENABLED: bool = True
    CURRICULUM_SHORT_LINES: int = 50     # tier 1: short files
    CURRICULUM_MED_LINES: int = 300      # tier 2: medium files

    # --- Sliding Window Attention ---
    ATTN_WINDOW: int = 0                # 0 = full attention; N = sliding window of N tokens

    # --- Latent Memory Tokens (context compression) ---
    N_MEMORY_TOKENS: int = 0            # number of learnable memory tokens for context compression
    MEMORY_SEGMENT_LEN: int = 0         # segment length for memory-token processing (0 = disabled)

    # --- Progressive Sequence Length ---
    PROGRESSIVE_SEQ: bool = True        # warm up with shorter sequences
    PROGRESSIVE_SEQ_STEPS: Tuple[int, int, int] = (128, 256, 512)  # len per phase
    PROGRESSIVE_SEQ_EPOCHS: Tuple[int, int, int] = (3, 3, 4)        # epochs per phase

    # --- Text Quality Filters ---
    FILTER_MAX_LINE_LEN: int = 500       # files with lines >500 chars are suspicious
    FILTER_ENTROPY_MIN: float = 3.5      # below this = repetitive / auto-generated
    FILTER_ENTROPY_MAX: float = 6.5      # above this = binary / encrypted
    FILTER_SPECIAL_TOKEN_RATIO_MAX: float = 0.25  # max fraction of whitespace-only tokens
    FILTER_ENABLE_DEDUP: bool = True     # skip files with identical content hash

    # --- Quantization for inference (6GB VRAM) ---
    QUANTIZE_EMBEDDINGS: bool = True     # int8 on embed + lm_head
    QUANTIZE_FFN: bool = False          # int4 on FFN weights (experimental)
    QUANT_EMBED_BITS: int = 8

    # --- Speculative Decoding ---
    SPEC_DECODE_ENABLED: bool = False
    SPEC_DECODE_DRAFT_SCALE: str = 'micro'  # draft model scale (4x smaller)
    SPEC_DECODE_K: int = 5              # draft tokens per speculation step

    # --- Corpus ---
    CORPUS: str = 'directory'            # 'directory' | 'file'
    CORPUS_ROOT: str = './src'
    CORPUS_FILE: str = ''                # Path if CORPUS='file'
    CORPUS_MIN_FILE_CHARS: int = 30      # minimum chars to include a file
    DATA_DIR: str = 'data_topogpt2'
    MAX_TRAIN_TOKENS: int = 500_000_000  # max tokens per epoch (0 = unlimited)

    # --- Checkpoints ---
    CHECKPOINT_DIR: str = 'checkpoints_topogpt2'
    CHECKPOINT_INTERVAL_MINUTES: int = 10
    MAX_CHECKPOINTS: int = 5

    # --- Logging ---
    LOG_INTERVAL_STEPS: int = 100
    EVAL_INTERVAL_STEPS: int = 500
    LOG_LEVEL: str = 'INFO'

    # --- Temperatura termodinámica (heredada) ---
    T_INIT: float = 1.0

    def __post_init__(self):
        presets = {
            'micro':  dict(D_MODEL=64,  N_HEADS=4,  N_LAYERS=2,  MAX_SEQ_LEN=256,  ATTN_WINDOW=64, N_MEMORY_TOKENS=16, MEMORY_SEGMENT_LEN=64),
            'small':  dict(D_MODEL=256, N_HEADS=8,  N_LAYERS=6,  MAX_SEQ_LEN=512,  ATTN_WINDOW=128, N_MEMORY_TOKENS=32, MEMORY_SEGMENT_LEN=128),
            'medium': dict(D_MODEL=512, N_HEADS=8,  N_LAYERS=12, MAX_SEQ_LEN=1024, ATTN_WINDOW=256, N_MEMORY_TOKENS=64, MEMORY_SEGMENT_LEN=256),
            'gpt2':   dict(D_MODEL=768, N_HEADS=12, N_LAYERS=12, MAX_SEQ_LEN=2048, ATTN_WINDOW=256, N_MEMORY_TOKENS=64, MEMORY_SEGMENT_LEN=256),
        }
        if self.SCALE in presets:
            for k, v in presets[self.SCALE].items():
                setattr(self, k, v)

        assert self.D_MODEL % 4 == 0, "D_MODEL debe ser divisible por 4 (cuaterniones)"
        assert self.D_MODEL % self.N_HEADS == 0, "D_MODEL debe ser divisible por N_HEADS"
        self.D_QUAT = self.D_MODEL // 4
        self.D_HEAD = self.D_MODEL // self.N_HEADS
        self.SPECTRAL_LATENT_DIM = max(16, int(self.D_MODEL * self.SPECTRAL_LATENT_RATIO))
        self.N_TORUS_NODES = self.TORUS_RADIAL_BINS * self.TORUS_ANGULAR_BINS
        # GQA: resolver N_KV_HEADS
        if self.N_KV_HEADS == 0:
            # Auto: N_HEADS // 4, mínimo 1, divisor de N_HEADS
            kv = max(1, self.N_HEADS // 4)
            while self.N_HEADS % kv != 0:
                kv -= 1
            self.N_KV_HEADS = kv
        elif self.N_KV_HEADS == -1:
            self.N_KV_HEADS = self.N_HEADS   # MHA estándar
        assert self.N_HEADS % self.N_KV_HEADS == 0, \
            "N_HEADS debe ser divisible por N_KV_HEADS"
        self.GQA_GROUPS = self.N_HEADS // self.N_KV_HEADS


def setup_logger(name: str, level: str = 'INFO') -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, level.upper(), logging.INFO))
    if not logger.handlers:
        h = logging.StreamHandler()
        h.setFormatter(logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s'))
        logger.addHandler(h)
    return logger


def set_seed(seed: int, device: str):
    torch.manual_seed(seed)
    np.random.seed(seed)
    if 'cuda' in device and torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)
        torch.backends.cudnn.deterministic = True


# ============================================================================
# ÁLGEBRA DE CUATERNIONES
# ============================================================================

class QuaternionOps:
    """
    Operaciones de cuaterniones puras en PyTorch.
    Representación: [..., 4]  donde last dim = [w, x, y, z]
    q = w + x*i + y*j + z*k
    """

    @staticmethod
    def hamilton_product(q1: torch.Tensor, q2: torch.Tensor) -> torch.Tensor:
        """Producto de Hamilton q1 ⊗ q2. Ambos [..., 4]."""
        w1, x1, y1, z1 = q1[..., 0], q1[..., 1], q1[..., 2], q1[..., 3]
        w2, x2, y2, z2 = q2[..., 0], q2[..., 1], q2[..., 2], q2[..., 3]
        return torch.stack([
            w1*w2 - x1*x2 - y1*y2 - z1*z2,
            w1*x2 + x1*w2 + y1*z2 - z1*y2,
            w1*y2 - x1*z2 + y1*w2 + z1*x2,
            w1*z2 + x1*y2 - y1*x2 + z1*w2,
        ], dim=-1)

    @staticmethod
    def normalize(q: torch.Tensor, eps: float = 1e-8) -> torch.Tensor:
        return q / (q.norm(dim=-1, keepdim=True) + eps)

    @staticmethod
    def conjugate(q: torch.Tensor) -> torch.Tensor:
        sign = q.new_tensor([1, -1, -1, -1])
        return q * sign

    @staticmethod
    def rotate_vector(v: torch.Tensor, q: torch.Tensor) -> torch.Tensor:
        """Rota vector 3D v por cuaternión unitario q. v:[...,3] q:[...,4]"""
        zero = torch.zeros(*v.shape[:-1], 1, device=v.device, dtype=v.dtype)
        v_q = torch.cat([zero, v], dim=-1)  # pure quaternion
        q_c = QuaternionOps.conjugate(q)
        rotated = QuaternionOps.hamilton_product(
            QuaternionOps.hamilton_product(q, v_q), q_c)
        return rotated[..., 1:]


class QuaternionLinear(nn.Module):
    """
    Capa lineal con pesos cuaterniones.

    Implementa la multiplicación W * x en el álgebra de cuaterniones:
    - W = Ww + Wx*i + Wy*j + Wz*k  (cuaternión de pesos)
    - x = xw + xx*i + xy*j + xz*k  (cuaternión de entrada)
    - out = W * x  (producto de Hamilton extendido a vectores)

    Parámetros: 4 matrices reales de forma [out_q, in_q]
    """

    def __init__(self, in_features: int, out_features: int, bias: bool = True):
        super().__init__()
        assert in_features % 4 == 0 and out_features % 4 == 0
        self.in_q = in_features // 4
        self.out_q = out_features // 4

        # 4 componentes del cuaternión de pesos
        self.Ww = nn.Linear(self.in_q, self.out_q, bias=False)
        self.Wx = nn.Linear(self.in_q, self.out_q, bias=False)
        self.Wy = nn.Linear(self.in_q, self.out_q, bias=False)
        self.Wz = nn.Linear(self.in_q, self.out_q, bias=False)
        self.bias = nn.Parameter(torch.zeros(out_features)) if bias else None

        for w in [self.Ww, self.Wx, self.Wy, self.Wz]:
            nn.init.normal_(w.weight, std=0.02)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """x: [..., in_features] → [..., out_features]"""
        d = self.in_q
        xw, xx, xy, xz = x[..., :d], x[..., d:2*d], x[..., 2*d:3*d], x[..., 3*d:]
        # Producto de Hamilton: W * x
        ow = self.Ww(xw) - self.Wx(xx) - self.Wy(xy) - self.Wz(xz)
        ox = self.Ww(xx) + self.Wx(xw) + self.Wy(xz) - self.Wz(xy)
        oy = self.Ww(xy) - self.Wx(xz) + self.Wy(xw) + self.Wz(xx)
        oz = self.Ww(xz) + self.Wx(xy) - self.Wy(xx) + self.Wz(xw)
        out = torch.cat([ow, ox, oy, oz], dim=-1)
        return out + self.bias if self.bias is not None else out


# ============================================================================
# CAPA ESPECTRAL CON CUATERNIONES
# ============================================================================

class QuaternionSpectralLayer(nn.Module):
    """
    Convolución espectral 2D con cuaterniones y producto de Hamilton completo.

    Operación en dominio de frecuencia:
        P(k) = W(k) ⊗ X(k)  (producto de Hamilton de cuaterniones complejos)

    Donde:
        X(k) = FFT2(x) con 4 canales cuaterniones [Xw, Xx, Xy, Xz]
        W(k) = kernel complejo aprendible con componentes [Ww, Wx, Wy, Wz]

    Reglas del producto de Hamilton en dominio de frecuencia:
        Pw = Ww·Xw - Wx·Xx - Wy·Xy - Wz·Xz
        Px = Ww·Xx + Wx·Xw + Wy·Xz - Wz·Xy
        Py = Ww·Xy - Wx·Xz + Wy·Xw + Wz·Xx
        Pz = Ww·Xz + Wx·Xy - Wy·Xx + Wz·Xw

    Cada Wc es un kernel complejo (partes real e imaginaria independientes).
    """

    def __init__(self, in_q: int, out_q: int, grid_h: int, grid_w: int,
                 init_scale: float = 0.02):
        super().__init__()
        self.in_q = in_q
        self.out_q = out_q
        self.grid_h = grid_h
        self.grid_w = grid_w

        # rfft2(x, s=(H, W)) → output shape [..., H, W//2+1]
        freq_h = grid_h
        freq_w = grid_w // 2 + 1

        # Kernel complejo para cada componente cuaternión (w, x, y, z)
        for c in ('w', 'x', 'y', 'z'):
            self.register_parameter(f'kr_{c}',
                nn.Parameter(torch.randn(in_q, out_q, freq_h, freq_w) * init_scale))
            self.register_parameter(f'ki_{c}',
                nn.Parameter(torch.randn(in_q, out_q, freq_h, freq_w) * init_scale))

    def _kernel(self, c: str) -> torch.Tensor:
        return torch.complex(getattr(self, f'kr_{c}'), getattr(self, f'ki_{c}'))

    def _contract(self, W: torch.Tensor, X: torch.Tensor) -> torch.Tensor:
        """Suma sobre canales in_q: Y[b,o,h,w] = Σ_i W[i,o,h,w]·X[b,i,h,w]"""
        return torch.einsum('iohw,bihw->bohw', W, X)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        x: [B, 4*in_q, H, W]  (4 canales cuaterniones sobre grid espacial)
        → [B, 4*out_q, H, W]
        """
        q = self.in_q
        xw, xx, xy, xz = x[:, :q], x[:, q:2*q], x[:, 2*q:3*q], x[:, 3*q:]

        # FFT2 por componente cuaternión → dominio de frecuencia
        Xw = torch.fft.rfft2(xw, s=(self.grid_h, self.grid_w))
        Xx = torch.fft.rfft2(xx, s=(self.grid_h, self.grid_w))
        Xy = torch.fft.rfft2(xy, s=(self.grid_h, self.grid_w))
        Xz = torch.fft.rfft2(xz, s=(self.grid_h, self.grid_w))

        Ww, Wx, Wy, Wz = self._kernel('w'), self._kernel('x'), self._kernel('y'), self._kernel('z')

        # Precomputar 16 contracciones (componente de kernel × componente de señal)
        C = {}
        for wc, W in (('w', Ww), ('x', Wx), ('y', Wy), ('z', Wz)):
            for xc, X in (('w', Xw), ('x', Xx), ('y', Xy), ('z', Xz)):
                C[(wc, xc)] = self._contract(W, X)

        # Producto de Hamilton en dominio de frecuencia
        Pw = C[('w','w')] - C[('x','x')] - C[('y','y')] - C[('z','z')]
        Px = C[('w','x')] + C[('x','w')] + C[('y','z')] - C[('z','y')]
        Py = C[('w','y')] - C[('x','z')] + C[('y','w')] + C[('z','x')]
        Pz = C[('w','z')] + C[('x','y')] - C[('y','x')] + C[('z','w')]

        # IFFT2 y recombinar
        ow = torch.fft.irfft2(Pw, s=(self.grid_h, self.grid_w))
        ox = torch.fft.irfft2(Px, s=(self.grid_h, self.grid_w))
        oy = torch.fft.irfft2(Py, s=(self.grid_h, self.grid_w))
        oz = torch.fft.irfft2(Pz, s=(self.grid_h, self.grid_w))

        return torch.cat([ow, ox, oy, oz], dim=1)  # [B, 4*out_q, H, W]


# ============================================================================
# SPECTRAL AUTOENCODER
# ============================================================================

class SpectralAutoencoder(nn.Module):
    """
    Autoencoder espectral con cuaterniones.

    Opera en dos niveles:
    1. Espectral 1D sobre el vector de features (FFT sobre dim D_MODEL):
       captura la espectrografía global del embedding.
    2. Espectral 2D sobre el grid del toro (QuaternionSpectralLayer):
       captura correlaciones espaciales en la topología.

    Devuelve (latent, recon_loss) para regularización.
    """

    def __init__(self, config: TopoGPT2Config):
        super().__init__()
        d = config.D_MODEL
        d_lat = config.SPECTRAL_LATENT_DIM
        d_q = config.D_QUAT
        g = config.TORUS_GRID_SIZE
        r = config.TORUS_RADIAL_BINS
        a = config.TORUS_ANGULAR_BINS
        init_s = config.SPECTRAL_KERNEL_INIT_SCALE

        n_freq = d // 2 + 1

        # --- Kernels espectrales 1D (reales e imaginarios) ---
        self.enc_kr = nn.Parameter(torch.randn(n_freq) * init_s)
        self.enc_ki = nn.Parameter(torch.randn(n_freq) * init_s)
        self.dec_kr = nn.Parameter(torch.randn(n_freq) * init_s)
        self.dec_ki = nn.Parameter(torch.randn(n_freq) * init_s)

        # Proyección al latente y de vuelta
        self.enc_proj = QuaternionLinear(d, d_lat)
        self.dec_proj = QuaternionLinear(d_lat, d)

        # --- Spectral 2D sobre el grid del toro: in/out_q = d_q, grid = r×a ---
        # Los 'out_q' en la segunda capa son iguales para reconstruir
        self.torus_spectral = nn.ModuleList([
            QuaternionSpectralLayer(d_q, d_q, r, a, init_scale=init_s)
            for _ in range(config.NUM_SPECTRAL_LAYERS)
        ])

        self.act = nn.GELU()
        self.d_model = d

    def _filter1d(self, x: torch.Tensor, kr: torch.Tensor, ki: torch.Tensor) -> torch.Tensor:
        """Filtro espectral 1D: x[..., D] → filtrado[..., D]"""
        X = torch.fft.rfft(x, dim=-1)
        K = torch.complex(kr, ki)
        return torch.fft.irfft(X * K, n=self.d_model, dim=-1)

    def encode(self, x: torch.Tensor) -> torch.Tensor:
        """x: [..., D_MODEL] → latent: [..., D_LAT]"""
        x_filt = self.act(self._filter1d(x, self.enc_kr, self.enc_ki))
        return self.enc_proj(x_filt)

    def decode(self, z: torch.Tensor) -> torch.Tensor:
        """z: [..., D_LAT] → recon: [..., D_MODEL]"""
        x = self.dec_proj(z)
        return self._filter1d(x, self.dec_kr, self.dec_ki)

    def forward(self, x: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        """Devuelve (latent, recon_loss)"""
        z = self.encode(x)
        recon = self.decode(z)
        recon_loss = F.mse_loss(recon, x.detach())
        return z, recon_loss

    def process_torus_grid(self, grid: torch.Tensor) -> torch.Tensor:
        """
        Procesa el grid del toro con QuaternionSpectralLayer.
        grid: [B, 4*D_QUAT, RADIAL, ANGULAR]  →  [B, 4*D_QUAT, RADIAL, ANGULAR]
        """
        h = grid
        for layer in self.torus_spectral:
            h = self.act(layer(h))
        return h


# ============================================================================
# QUATERNION TORUS BRAIN (reemplaza MLP, VECTORIZADO)
# ============================================================================

class QuaternionTorusBrain(nn.Module):
    """
    Reemplaza el MLP en cada capa del transformer.

    Pipeline (completamente vectorizado sobre batch Y secuencia):

    1. Flatten: [B, S, D] → [B·S, D]
    2. SpectralAutoencoder: filtrado espectral 1D + compresión cuaternión
    3. Proyección al toro:
       - Calcula 2 ángulos (phi1, phi2) ∈ [-π, π]²
       - Asignación blanda a los 8 nodos via distancia circular en el toro
    4. Construye grid de nodos: [B·S, N_NODES=8, D_MODEL]
    5. QuaternionSpectralLayer 2D sobre el grid [B·S, 4*D_QUAT, RADIAL, ANGULAR]
    6. Message-passing con rotaciones cuaterniones sobre el grafo toro
    7. Readout: atención sobre los 8 nodos → [B·S, D_MODEL]
    8. Reshape: [B·S, D] → [B, S, D]
    """

    def __init__(self, d_model: int, config: TopoGPT2Config):
        super().__init__()
        self.d_model = d_model
        self.d_lat = config.SPECTRAL_LATENT_DIM
        self.d_q = d_model // 4
        self.n_radial = config.TORUS_RADIAL_BINS    # 2
        self.n_angular = config.TORUS_ANGULAR_BINS  # 4
        self.n_nodes = config.N_TORUS_NODES         # 8
        self.config = config

        # Autoencoder espectral
        self.spectral_ae = SpectralAutoencoder(config)

        # Proyección al espacio de ángulos del toro (2 ángulos × 2 = 4 salidas para Q)
        self.torus_proj = nn.Sequential(
            QuaternionLinear(d_model, d_model),
            nn.GELU(),
            nn.Linear(d_model, 4),  # [phi1, phi2, r_scale, dummy]
        )

        # Embeddings aprendibles para los 8 nodos del toro
        self.node_embed = nn.Parameter(torch.randn(self.n_nodes, d_model) * 0.02)

        # Cuaterniones de rotación aprendibles para message-passing
        # Un cuaternión por tipo de arista: ang-izq, ang-der, rad-abajo, rad-arriba
        self.edge_quat = nn.Parameter(torch.randn(4, 4) * 0.1)  # [n_edge_types, 4]

        # Red de nodo post-message-passing
        self.node_net = QuaternionLinear(d_model, d_model)

        # Proyección final desde nodo-pool al espacio de salida
        self.readout = nn.Sequential(
            nn.Linear(d_model, d_model * 2),
            nn.GELU(),
            nn.Linear(d_model * 2, d_model),
        )

        # Grafo del toro: lista de aristas (nodo_i, nodo_j, tipo_arista)
        self._build_torus_graph()

    def _build_torus_graph(self):
        """
        Construye las aristas del grafo toro 2×4.

        Nodos indexados como: node = r * N_ANGULAR + a
          r ∈ [0, RADIAL-1], a ∈ [0, ANGULAR-1]

        Aristas angulares: nodo ↔ nodo a la izquierda/derecha (periódico)
        Aristas radiales:  nodo ↔ nodo del anillo interior/exterior
        """
        edges_i, edges_j, edge_type = [], [], []
        R, A = self.n_radial, self.n_angular
        for r in range(R):
            for a in range(A):
                n = r * A + a
                # Angular izquierda (tipo 0)
                neighbor = r * A + (a - 1) % A
                edges_i.append(n); edges_j.append(neighbor); edge_type.append(0)
                # Angular derecha (tipo 1)
                neighbor = r * A + (a + 1) % A
                edges_i.append(n); edges_j.append(neighbor); edge_type.append(1)
                # Radial hacia centro (tipo 2) - si existe
                if r > 0:
                    neighbor = (r - 1) * A + a
                    edges_i.append(n); edges_j.append(neighbor); edge_type.append(2)
                # Radial hacia fuera (tipo 3) - si existe
                if r < R - 1:
                    neighbor = (r + 1) * A + a
                    edges_i.append(n); edges_j.append(neighbor); edge_type.append(3)

        self.register_buffer('edges_i', torch.tensor(edges_i, dtype=torch.long))
        self.register_buffer('edges_j', torch.tensor(edges_j, dtype=torch.long))
        self.register_buffer('edge_type', torch.tensor(edge_type, dtype=torch.long))

    def _torus_soft_assign(self, phi1: torch.Tensor, phi2: torch.Tensor) -> torch.Tensor:
        """
        Asignación blanda de tokens a los 8 nodos del toro via distancia circular.

        phi1: [BS] ángulo angular ∈ [-π, π]
        phi2: [BS] ángulo radial ∈ [-π, π]
        → weights: [BS, N_NODES]  (suma a 1, softmax de distancias negativas)
        """
        BS = phi1.shape[0]
        device = phi1.device

        # Posiciones de los nodos en el toro
        ang_pos = torch.linspace(-math.pi, math.pi, self.n_angular + 1, device=device)[:-1]
        rad_pos = torch.linspace(-math.pi, math.pi, self.n_radial + 1, device=device)[:-1]

        # Distancias circulares (usando sin para periodicidad suave)
        # d_ang[BS, N_ANGULAR], d_rad[BS, N_RADIAL]
        d_ang = torch.sin((phi1.unsqueeze(1) - ang_pos.unsqueeze(0)) / 2).pow(2)  # [BS, A]
        d_rad = torch.sin((phi2.unsqueeze(1) - rad_pos.unsqueeze(0)) / 2).pow(2)  # [BS, R]

        # Distancia en el toro para cada nodo [r, a]:  d[r, a] = d_rad[r] + d_ang[a]
        # Resultado: [BS, R, A] → flatten a [BS, N_NODES]
        d_torus = d_rad.unsqueeze(2) + d_ang.unsqueeze(1)  # [BS, R, A]
        d_flat = d_torus.view(BS, -1)  # [BS, N_NODES]

        return torch.softmax(-d_flat / 0.3, dim=-1)  # temperatura 0.3

    def _message_passing(self, node_feat: torch.Tensor) -> torch.Tensor:
        """
        Message-passing VECTORIZADO con rotaciones cuaterniones.
        Sin bucles Python: todas las aristas se procesan en paralelo.

        node_feat: [BS, N_NODES, D_MODEL]
        → [BS, N_NODES, D_MODEL]
        """
        BS = node_feat.shape[0]
        n_edges = self.edges_i.shape[0]
        d_q = self.d_q

        # Cuaterniones de arista normalizados: [n_edge_types=4, 4]
        eq = QuaternionOps.normalize(self.edge_quat)

        # Recoger features de nodos fuente para TODAS las aristas: [BS, n_edges, D]
        src_feat = node_feat[:, self.edges_j, :]   # index [n_edges] → [BS, n_edges, D]

        # Cuaternión de cada arista: [n_edges, 4] → [1, n_edges, 1, 4] para broadcasting
        edge_q = eq[self.edge_type]                # [n_edges, 4]
        edge_q = edge_q.unsqueeze(0).unsqueeze(2)  # [1, n_edges, 1, 4]
        edge_q = edge_q.expand(BS, -1, d_q, -1)   # [BS, n_edges, D_QUAT, 4]

        # Reshapear fuentes: [BS, n_edges, D] → [BS, n_edges, D_QUAT, 4]
        src_q = src_feat.view(BS, n_edges, d_q, 4)

        # Rotación cuaternión para todas las aristas en paralelo: [BS, n_edges, D_QUAT, 4]
        msg_rot = QuaternionOps.hamilton_product(edge_q, src_q)
        msg_rot = msg_rot.view(BS, n_edges, self.d_model)  # [BS, n_edges, D]

        # Scatter-add a nodos destino: edges_i[e] es el nodo destino de la arista e
        agg = torch.zeros_like(node_feat)  # [BS, N_NODES, D]
        dst_idx = self.edges_i.view(1, n_edges, 1).expand(BS, -1, self.d_model)
        agg.scatter_add_(1, dst_idx, msg_rot)

        return self.node_net(node_feat + agg)

    def forward(self, x: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        """
        x: [B, S, D_MODEL]
        → output: [B, S, D_MODEL], recon_loss: scalar
        """
        B, S, D = x.shape
        device = x.device

        # 1. Flatten para procesamiento paralelo
        x_flat = x.reshape(B * S, D)  # [BS, D]

        # 2. Spectral Autoencoder: filtrado + compresión
        z, recon_loss = self.spectral_ae(x_flat)  # z: [BS, D_LAT]

        # 3. Proyección al toro
        coords = self.torus_proj(x_flat)          # [BS, 4]
        phi1 = math.pi * torch.tanh(coords[:, 0]) # ángulo angular ∈ [-π, π]
        phi2 = math.pi * torch.tanh(coords[:, 1]) # ángulo radial ∈ [-π, π]

        # 4. Asignación blanda a 8 nodos
        attn_w = self._torus_soft_assign(phi1, phi2)  # [BS, N_NODES]

        # 5. Construir grid de nodos: weighted combination de embeddings de nodo + input
        #    node_feat[bs, n, :] = attn_w[bs,n] * node_embed[n] + x_flat[bs] * attn_w[bs,n]
        nodes = (
            attn_w.unsqueeze(-1) * self.node_embed.unsqueeze(0)   # [BS, N, D]
            + attn_w.unsqueeze(-1) * x_flat.unsqueeze(1)          # broadcasting [BS, N, D]
        )  # [BS, N_NODES, D_MODEL]

        # 6. QuaternionSpectralLayer 2D sobre el grid del toro
        #    Reshape: [BS, N_NODES, D_MODEL] → [BS, 4*D_QUAT, RADIAL, ANGULAR]
        grid = nodes.view(B * S, self.n_radial, self.n_angular, D)
        grid = grid.permute(0, 3, 1, 2)           # [BS, D_MODEL, RADIAL, ANGULAR]
        # Reorganizar en 4 canales cuaterniones
        d_q = self.d_q
        grid_q = grid.view(B * S, 4, d_q, self.n_radial, self.n_angular)
        # [BS, 4, D_QUAT, RADIAL, ANGULAR] → [BS, 4*D_QUAT, RADIAL, ANGULAR]
        grid_q = grid_q.permute(0, 1, 2, 3, 4).reshape(B * S, 4 * d_q, self.n_radial, self.n_angular)
        grid_spec = self.spectral_ae.process_torus_grid(grid_q)  # [BS, 4*D_QUAT, R, A]

        # Volver a [BS, N_NODES, D_MODEL]
        grid_back = grid_spec.view(B * S, 4, d_q, self.n_radial, self.n_angular)
        grid_back = grid_back.permute(0, 3, 4, 1, 2).reshape(B * S, self.n_nodes, D)

        # 7. Message-passing cuaternión sobre el grafo toro
        nodes_mp = self._message_passing(grid_back)  # [BS, N_NODES, D_MODEL]

        # 8. Readout: suma ponderada por los pesos de asignación
        out_flat = (attn_w.unsqueeze(-1) * nodes_mp).sum(dim=1)  # [BS, D_MODEL]
        out_flat = self.readout(out_flat)  # [BS, D_MODEL]

        # 9. Reshape a secuencia
        output = out_flat.reshape(B, S, D)  # [B, S, D_MODEL]

        return output, recon_loss


# ============================================================================
# ROTARY POSITION EMBEDDINGS (RoPE)
# ============================================================================

class RotaryEmbedding(nn.Module):
    """
    Rotary Position Embeddings (RoPE) - Su et al., 2021.
    Codifica la posicion como rotaciones del espacio de atencion,
    naturalmente relativas y sin parametros extra.

    Las caches _cos/_sin se registran como buffers no-persistentes con
    nombres que no colisionan con checkpoints antiguos (que usaban
    'cos_cache'/'sin_cache'). Esto permite cambiar MAX_SEQ_LEN sin
    errores de shape al cargar checkpoints previos.
    """

    def __init__(self, d_head: int, max_seq_len: int = 2048, base: int = 10000):
        super().__init__()
        inv_freq = 1.0 / (base ** (torch.arange(0, d_head, 2).float() / d_head))
        self.register_buffer('inv_freq', inv_freq)
        self._build_cache(max_seq_len)

    def _build_cache(self, seq_len: int):
        device = self.inv_freq.device
        t = torch.arange(seq_len, device=device).float()
        freqs = torch.outer(t, self.inv_freq)
        emb = torch.cat([freqs, freqs], dim=-1)
        self.register_buffer('_cos_cache', emb.cos(), persistent=False)
        self.register_buffer('_sin_cache', emb.sin(), persistent=False)

    def _rotate_half(self, x: torch.Tensor) -> torch.Tensor:
        x1, x2 = x[..., :x.shape[-1]//2], x[..., x.shape[-1]//2:]
        return torch.cat([-x2, x1], dim=-1)

    def forward(self, q: torch.Tensor, k: torch.Tensor,
                seq_len: int, offset: int = 0) -> Tuple[torch.Tensor, torch.Tensor]:
        """
        q, k: [B, n_heads, S_q/S_k, d_head]
        offset: posicion inicial (para KV cache: longitud del cache existente)
        Aplica posiciones [offset .. offset+S-1] a q y k.
        """
        needed = offset + max(q.shape[2], k.shape[2])
        if needed > self._cos_cache.shape[0]:
            self._build_cache(needed * 2)
        sq, sk = q.shape[2], k.shape[2]
        cos_q = self._cos_cache[offset:offset + sq].unsqueeze(0).unsqueeze(0)
        sin_q = self._sin_cache[offset:offset + sq].unsqueeze(0).unsqueeze(0)
        cos_k = self._cos_cache[offset:offset + sk].unsqueeze(0).unsqueeze(0)
        sin_k = self._sin_cache[offset:offset + sk].unsqueeze(0).unsqueeze(0)
        q_rot = q * cos_q + self._rotate_half(q) * sin_q
        k_rot = k * cos_k + self._rotate_half(k) * sin_k
        return q_rot, k_rot


# ============================================================================
# MULTI-HEAD ATTENTION CON FLASH ATTENTION + ROPE
# ============================================================================

class RMSNorm(nn.Module):
    """Root Mean Square Layer Normalization (sin bias). Más estable que LayerNorm."""

    def __init__(self, d_model: int, eps: float = 1e-6):
        super().__init__()
        self.eps = eps
        self.weight = nn.Parameter(torch.ones(d_model))

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        rms = x.pow(2).mean(-1, keepdim=True).add(self.eps).sqrt()
        return x / rms * self.weight


# ============================================================================
# SWIGLU (activacion de modelos frontier: LLaMA, Qwen, etc.)
# ============================================================================

class SwiGLU(nn.Module):
    """
    SwiGLU: SiLU(gate(x)) * up(x) -> down
    Usado en LLaMA 2/3, Qwen, Mistral en lugar de GELU-FFN.
    Dimension interna: 8/3 * d_model (convención LLaMA, redondeada a múltiplo de 4).
    """

    def __init__(self, d_model: int, expansion: float = 8 / 3,
                 dropout: float = 0.0):
        super().__init__()
        inner = max(4, int(d_model * expansion))
        inner = (inner + 3) // 4 * 4  # redondear a múltiplo de 4
        self.gate_proj = nn.Linear(d_model, inner, bias=False)
        self.up_proj   = nn.Linear(d_model, inner, bias=False)
        self.down_proj = nn.Linear(inner, d_model, bias=False)
        self.drop = nn.Dropout(dropout) if dropout > 0 else nn.Identity()
        # Inicialización estilo GPT
        nn.init.normal_(self.gate_proj.weight, std=0.02)
        nn.init.normal_(self.up_proj.weight,   std=0.02)
        nn.init.normal_(self.down_proj.weight, std=0.02)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.drop(self.down_proj(F.silu(self.gate_proj(x)) * self.up_proj(x)))


# ============================================================================
# MoE: Mixture of Experts topologico
# ============================================================================

class TopoMoEBrain(nn.Module):
    """
    Mixture of Experts sobre la capa topologica.

    Arquitectura (inspirada en DeepSeek-MoE / Mixtral):
      - 1 experto compartido: QuaternionTorusBrain (siempre activo)
      - N_EXPERTS expertos SwiGLU ligeros (activacion esparsa: Top-K por token)
      - Router: Linear(D, N_EXPERTS) + softmax → top-K

    Load-balancing loss (auxiliar): penaliza si un experto acapara todos los tokens.
    Activa MOE_TOP_K de N_EXPERTS expertos por token.

    Sin MoE (MOE_ENABLED=False): se comporta como QuaternionTorusBrain puro.
    """

    def __init__(self, d_model: int, config: 'TopoGPT2Config'):
        super().__init__()
        self.d_model = d_model
        self.moe_enabled = config.MOE_ENABLED
        self.n_experts = config.N_EXPERTS
        self.top_k = config.MOE_TOP_K
        self.aux_weight = config.MOE_AUX_LOSS_WEIGHT

        # Experto compartido: el TopoBrain original (siempre activo)
        self.shared_expert = QuaternionTorusBrain(d_model, config)

        if self.moe_enabled:
            # N_EXPERTS expertos SwiGLU ligeros (dimension reducida para eficiencia)
            self.experts = nn.ModuleList([
                SwiGLU(d_model, expansion=4/3, dropout=config.DROPOUT)
                for _ in range(self.n_experts)
            ])
            # Router: produce logits por experto para cada token
            self.router = nn.Linear(d_model, self.n_experts, bias=False)
            nn.init.normal_(self.router.weight, std=0.02)

    def _route(self, x: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        """
        x: [N, D] donde N = B*S (tokens aplanados)
        Retorna:
        expert_out: [N, D]  suma ponderada de top-K expertos
        aux_loss:   escalar  load-balancing loss
        Routing vectorizado sin boolean indexing ni sincronizacion CUDA.
        Usa dispatch por indices agrupados (estilo Mixtral/DeepSeek) para
        compatibilidad total con torch.utils.checkpoint.
        """
        N, D = x.shape
        router_logits = self.router(x)                    # [N, n_experts]
        router_probs  = F.softmax(router_logits, dim=-1)  # [N, n_experts]
        # Top-K seleccion
        top_k_probs, top_k_idx = torch.topk(router_probs, self.top_k, dim=-1)
        # Renormalizar pesos dentro de los top-K
        top_k_probs = top_k_probs / top_k_probs.sum(dim=-1, keepdim=True).clamp(min=1e-9)
        # Dispatch vectorizado: agrupar tokens por experto asignado
        flat_idx = top_k_idx.reshape(-1)                             # [N*top_k]
        flat_weights = top_k_probs.reshape(-1)                       # [N*top_k]
        token_indices = torch.arange(N, device=x.device, dtype=torch.long)
        token_indices = token_indices.unsqueeze(1).expand(-1, self.top_k).reshape(-1)  # [N*top_k]
        expert_out = torch.zeros_like(x)

        # Se elimina la verificacion con .item() porque fuerza una sincronizacion
        # CPU-GPU que rompe el recomputado de gradient checkpointing.
        # scatter_add_ maneja tensores vacios de forma segura y eficiente.
        for e in range(self.n_experts):
            expert_mask = (flat_idx == e)                             # [N*top_k] boolean
            src_token_idx = token_indices[expert_mask]                # [count] indices en N
            w = flat_weights[expert_mask].unsqueeze(-1).to(x.dtype)   # [count, 1]
            out_e = self.experts[e](x[src_token_idx])                # [count, D]
            contrib = w * out_e
            expert_out.scatter_add_(0, src_token_idx.unsqueeze(1).expand_as(contrib), contrib)

        # Load-balancing loss (Switch Transformer style)
        token_frac    = router_probs.mean(dim=0)                    # [n_experts]
        one_hot       = F.one_hot(top_k_idx, self.n_experts).float()# [N, top_k, n_experts]
        dispatch_frac = one_hot.mean(dim=(0, 1))                    # [n_experts]
        aux_loss = self.n_experts * (token_frac * dispatch_frac).sum()
        return expert_out, aux_loss

    def forward(self, x: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        """
        x: [B, S, D]
        → output: [B, S, D], aux_loss: escalar
        """
        B, S, D = x.shape

        # Experto compartido siempre activo
        shared_out, recon_loss = self.shared_expert(x)  # [B, S, D], scalar

        if not self.moe_enabled:
            return shared_out, recon_loss

        # Expertos SwiGLU (esparso)
        x_flat = x.reshape(B * S, D)
        expert_out, aux_loss = self._route(x_flat)
        expert_out = expert_out.reshape(B, S, D)

        # Combinar: shared + routed (igual peso inicial)
        output = shared_out + expert_out

        # Combinar losses auxiliares
        total_aux = recon_loss + self.aux_weight * aux_loss

        return output, total_aux


class MultiHeadAttention(nn.Module):
    """
    Multi-head attention con:
    - Flash Attention (scaled_dot_product_attention de PyTorch 2.0+)
    - Rotary Position Embeddings (RoPE)
    - GQA (Grouped Query Attention): N_KV_HEADS < N_HEADS, reduce VRAM de K/V
    - KV Cache para inferencia autoregresiva eficiente
    - Temperatura termodinámica aprendible
    """

    def __init__(self, d_model: int, n_heads: int, config: 'TopoGPT2Config'):
        super().__init__()
        self.d_model  = d_model
        self.n_heads  = n_heads
        self.n_kv     = config.N_KV_HEADS   # cabezas K/V (GQA)
        self.n_groups = config.GQA_GROUPS    # n_heads // n_kv
        self.d_head   = d_model // n_heads
        self.window_size = config.ATTN_WINDOW  # 0 = full attention

        # Q con n_heads completo; K/V con n_kv (GQA)
        self.q_proj = nn.Linear(d_model, n_heads * self.d_head, bias=False)
        self.k_proj = nn.Linear(d_model, self.n_kv * self.d_head, bias=False)
        self.v_proj = nn.Linear(d_model, self.n_kv * self.d_head, bias=False)
        self.o_proj = nn.Linear(d_model, d_model, bias=False)

        self.rope = RotaryEmbedding(self.d_head, max_seq_len=config.MAX_SEQ_LEN)
        self.temperature = nn.Parameter(torch.tensor(config.T_INIT))
        self.dropout_p = config.DROPOUT if config.DROPOUT > 0 else 0.0

    def forward(self, x: torch.Tensor, is_causal: bool = True,
                past_kv: Optional[Tuple[torch.Tensor, torch.Tensor]] = None
                ) -> Tuple[torch.Tensor, Tuple[torch.Tensor, torch.Tensor]]:
        """
        Args:
            x:        [B, S, D]
            is_causal: usar mascara causal
            past_kv:  (K_cache, V_cache) de pasos anteriores o None
        Returns:
            out:      [B, S, D]
            kv_cache: (K, V) completos para cachear en generate()
        """
        B, S, D = x.shape

        Q = self.q_proj(x).view(B, S, self.n_heads, self.d_head).transpose(1, 2)
        K = self.k_proj(x).view(B, S, self.n_kv,    self.d_head).transpose(1, 2)
        V = self.v_proj(x).view(B, S, self.n_kv,    self.d_head).transpose(1, 2)

        # RoPE con offset: si hay cache, Q y K_new se posicionan a partir de past_len
        past_len = past_kv[0].shape[2] if past_kv is not None else 0
        Q, K = self.rope(Q, K, seq_len=S, offset=past_len)

        # Concatenar K/V con cache (despues de aplicar RoPE al nuevo K)
        if past_kv is not None:
            K = torch.cat([past_kv[0], K], dim=2)
            V = torch.cat([past_kv[1], V], dim=2)

        attn_mask = None
        use_causal = (is_causal and past_kv is None)

        if self.window_size > 0:
            if past_kv is None:
                S_q = Q.shape[2]
                S_kv = K.shape[2]
                if S_kv > self.window_size:
                    row = torch.arange(S_q, device=Q.device).unsqueeze(1)
                    col = torch.arange(S_kv, device=Q.device).unsqueeze(0)
                    upper = row < col
                    outside = (row - col) >= self.window_size
                    attn_mask = upper | outside
                    use_causal = False
            else:
                if K.shape[2] > self.window_size:
                    K = K[:, :, -self.window_size:, :]
                    V = V[:, :, -self.window_size:, :]
                use_causal = False

        kv_cache = (K, V)
        K_full = K

        # GQA: expandir K/V al numero de cabezas de Q via repeat_interleave
        if self.n_groups > 1:
            K_full = K_full.repeat_interleave(self.n_groups, dim=1)  # [B, n_heads, S_k, d]
            V_exp  = V.repeat_interleave(self.n_groups, dim=1)
        else:
            V_exp = V

        scale = (self.d_head ** -0.5) / self.temperature.abs().clamp(min=1e-6)

        out = F.scaled_dot_product_attention(
            Q, K_full, V_exp,
            attn_mask=attn_mask,
            dropout_p=self.dropout_p if self.training else 0.0,
            is_causal=use_causal,
            scale=scale.item(),
        )  # [B, n_heads, S, d_head]

        out = out.transpose(1, 2).contiguous().view(B, S, D)
        return self.o_proj(out), kv_cache


# ============================================================================
# CAPA TRANSFORMER TOPOLÓGICA
# ============================================================================

class TopoGPT2Layer(nn.Module):
    """
    Capa del transformer con TopoMoEBrain (TopoBrain + MoE SwiGLU experts).

    Esquema pre-norm (estilo LLaMA):
        x = x + Attention_GQA(RMSNorm(x))
        x = x + TopoMoEBrain(RMSNorm(x))
    """

    def __init__(self, d_model: int, n_heads: int, config: 'TopoGPT2Config'):
        super().__init__()
        self.norm1 = RMSNorm(d_model)
        self.norm2 = RMSNorm(d_model)
        self.attn = MultiHeadAttention(d_model, n_heads, config)
        self.topo_brain = TopoMoEBrain(d_model, config)
        self.dropout = nn.Dropout(config.DROPOUT)
        self.use_ckpt = config.GRADIENT_CHECKPOINTING

    def _forward_impl(self, x: torch.Tensor,
                      past_kv: Optional[Tuple] = None
                      ) -> Tuple[torch.Tensor, torch.Tensor, Tuple]:
        attn_out, kv_cache = self.attn(self.norm1(x), past_kv=past_kv)
        x = x + self.dropout(attn_out)
        brain_out, aux_loss = self.topo_brain(self.norm2(x))
        x = x + self.dropout(brain_out)
        return x, aux_loss, kv_cache

    def forward(self, x: torch.Tensor,
                past_kv: Optional[Tuple] = None
                ) -> Tuple[torch.Tensor, torch.Tensor, Tuple]:
        """
        Retorna (x_out, aux_loss, kv_cache).
        Con gradient checkpointing en training (solo cuando no hay KV cache).
        """
        if self.use_ckpt and self.training and past_kv is None:
            def ckpt_fn(x_in):
                out, al, kvc = self._forward_impl(x_in, past_kv=None)
                return out, al
            out, al = grad_ckpt(ckpt_fn, x, use_reentrant=False)
            return out, al, None   # kv_cache no disponible con ckpt (solo entrenamiento)
        return self._forward_impl(x, past_kv=past_kv)


# ============================================================================
# MODELO COMPLETO
# ============================================================================

class TopoGPT2(nn.Module):
    """
    TopoGPT2: Transformer de lenguaje con TopoBrain cuaternión-espectral.

    Arquitectura:
        Embedding de tokens + RoPE (en Attention)
        N_LAYERS × TopoGPT2Layer (Attention + QuaternionTorusBrain)
        RMSNorm final
        Proyección a vocabulario (weight-tied con embeddings)
    """

    def __init__(self, config: TopoGPT2Config):
        super().__init__()
        self.config = config

        self.token_embed = nn.Embedding(config.VOCAB_SIZE, config.D_MODEL)
        nn.init.normal_(self.token_embed.weight, std=0.02)

        self.layers = nn.ModuleList([
            TopoGPT2Layer(config.D_MODEL, config.N_HEADS, config)
            for _ in range(config.N_LAYERS)
        ])
        self.final_norm = RMSNorm(config.D_MODEL)
        self.lm_head = nn.Linear(config.D_MODEL, config.VOCAB_SIZE, bias=False)

        # Weight tying (GPT-2 style): embedding y cabeza de lenguaje comparten pesos
        self.lm_head.weight = self.token_embed.weight

        self.memory_tokens: Optional[nn.Parameter] = None
        if config.N_MEMORY_TOKENS > 0:
            self.memory_tokens = nn.Parameter(
                torch.randn(1, config.N_MEMORY_TOKENS, config.D_MODEL) * 0.02
            )

        self._init_weights()

    def _init_weights(self):
        for module in self.modules():
            if isinstance(module, nn.Linear) and module is not self.lm_head:
                nn.init.normal_(module.weight, std=0.02)
                if module.bias is not None:
                    nn.init.zeros_(module.bias)

    def forward(self, token_ids: torch.Tensor,
                past_kvs: Optional[List[Optional[Tuple]]] = None
                ) -> Tuple[torch.Tensor, torch.Tensor, List[Tuple]]:
        """
        token_ids: [B, S]  (enteros)
        past_kvs:  lista de (K, V) por capa, o None para entrenamiento
        → logits: [B, S, VOCAB_SIZE], aux_loss: scalar, new_kvs: list[(K,V)]
        """
        x = self.token_embed(token_ids)  # [B, S, D_MODEL]

        total_aux = torch.tensor(0.0, device=x.device)
        new_kvs: List[Tuple] = []

        for i, layer in enumerate(self.layers):
            pkv = past_kvs[i] if past_kvs is not None else None
            x, al, kvc = layer(x, past_kv=pkv)
            total_aux = total_aux + al
            new_kvs.append(kvc)

        x = self.final_norm(x)
        logits = self.lm_head(x)
        return logits, total_aux / len(self.layers), new_kvs

    def forward_with_memory(
        self, token_ids: torch.Tensor
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        """Process long sequences with latent memory-token context compression.

        Splits `token_ids` [B, S] into segments of size MEMORY_SEGMENT_LEN.
        Each segment is processed with N_MEMORY_TOKENS prepended. The output
        at memory-token positions after segment k becomes the memory-state
        input for segment k+1, compressing all prior context into a fixed-size
        latent vector.

        Returns (logits [B, S, VOCAB_SIZE], aux_loss).
        """
        cfg = self.config
        B, S = token_ids.shape
        N_mem = cfg.N_MEMORY_TOKENS
        seg_len = cfg.MEMORY_SEGMENT_LEN

        if self.memory_tokens is None or N_mem == 0 or seg_len == 0:
            logits, aux, _ = self.forward(token_ids)
            return logits, aux

        device = token_ids.device
        mem = self.memory_tokens.expand(B, -1, -1)

        all_logits = []
        total_aux = torch.tensor(0.0, device=device)

        for seg_start in range(0, S, seg_len):
            seg_end = min(seg_start + seg_len, S)
            seg_ids = token_ids[:, seg_start:seg_end]
            seg_emb = self.token_embed(seg_ids)

            x = torch.cat([mem, seg_emb], dim=1)

            for layer in self.layers:
                x, al, _ = layer(x)
                total_aux = total_aux + al

            seg_out = x[:, N_mem:, :]
            mem = x[:, :N_mem, :]

            seg_out = self.final_norm(seg_out)
            seg_logits = self.lm_head(seg_out)
            all_logits.append(seg_logits)

        logits = torch.cat(all_logits, dim=1)
        aux_loss = total_aux / len(self.layers)
        return logits, aux_loss

    def count_params(self) -> Dict[str, int]:
        total = sum(p.numel() for p in self.parameters())
        trainable = sum(p.numel() for p in self.parameters() if p.requires_grad)
        return {'total': total, 'trainable': trainable}

    @torch.no_grad()
    def generate(self, token_ids: torch.Tensor, max_new_tokens: int = 200,
                 temperature: float = 0.8, top_k: int = 50,
                 repetition_penalty: float = 1.0) -> torch.Tensor:
        """
        Autoregressive generation with KV cache and top-k sampling.

        Args:
            token_ids: [B, S_prompt] prompt tokens.
            max_new_tokens: Maximum tokens to generate.
            temperature: Sampling temperature (lower = more deterministic).
            top_k: Top-k filtering (0 = disabled).
            repetition_penalty: Penalty for repeating tokens (>1 = penalize).

        Returns:
            [B, S_prompt + generated] full token sequence.
        """
        self.eval()
        cfg = self.config

        ctx = token_ids[:, -cfg.MAX_SEQ_LEN:]
        logits, _, past_kvs = self(ctx)
        logits = logits[:, -1, :] / max(temperature, 1e-8)
        if repetition_penalty != 1.0:
            mask = torch.zeros_like(logits, dtype=torch.bool)
            mask.scatter_(1, ctx, True)
            logits = torch.where(mask, logits / repetition_penalty, logits)
        if top_k > 0:
            v, _ = torch.topk(logits, min(top_k, logits.size(-1)))
            logits[logits < v[:, -1:]] = float('-inf')
        next_tok = torch.multinomial(F.softmax(logits, dim=-1), 1)
        token_ids = torch.cat([token_ids, next_tok], dim=1)

        for _ in range(max_new_tokens - 1):
            logits, _, past_kvs = self(next_tok, past_kvs=past_kvs)
            logits = logits[:, -1, :] / max(temperature, 1e-8)
            if repetition_penalty != 1.0:
                mask = torch.zeros_like(logits, dtype=torch.bool)
                mask.scatter_(1, token_ids, True)
                logits = torch.where(mask, logits / repetition_penalty, logits)
            if top_k > 0:
                v, _ = torch.topk(logits, min(top_k, logits.size(-1)))
                logits[logits < v[:, -1:]] = float('-inf')
            next_tok = torch.multinomial(F.softmax(logits, dim=-1), 1)
            token_ids = torch.cat([token_ids, next_tok], dim=1)

            if (next_tok == 50256).all():
                break

        return token_ids

    @torch.no_grad()
    def generate_with_continuation(self, token_ids: torch.Tensor,
                                   tokenizer: Any, max_new_tokens: int = 200,
                                   temperature: float = 0.8, top_k: int = 50,
                                   repetition_penalty: float = 1.0,
                                   max_continuations: int = 3,
                                   tail_lines: int = 2) -> torch.Tensor:
        full_ids = token_ids.clone()
        continuations = 0

        while continuations <= max_continuations:
            n_new = max_new_tokens - (full_ids.shape[1] - token_ids.shape[1]) if continuations > 0 else max_new_tokens
            if n_new <= 0:
                break

            out = self.generate(full_ids, max_new_tokens=n_new,
                                temperature=temperature, top_k=top_k,
                                repetition_penalty=repetition_penalty)
            full_ids = out

            out_text = tokenizer.decode(out[0].tolist())
            prompt_text = tokenizer.decode(token_ids[0].tolist())
            generated = out_text[len(prompt_text):]

            from .continuation import is_response_complete, extract_tail_for_continuation

            if is_response_complete(generated):
                break

            tail = extract_tail_for_continuation(generated, tail_lines=tail_lines)
            if not tail:
                break

            continuations += 1
            full_text = prompt_text + tail
            full_ids = torch.tensor([tokenizer.encode(full_text)],
                                    dtype=torch.long, device=full_ids.device)

        return full_ids


# ============================================================================
# TOKENIZADOR
# ============================================================================

class BPETokenizer:
    """Wrapper alrededor de tiktoken (GPT-2 compatible)."""

    def __init__(self, encoding: str = 'gpt2'):
        try:
            import tiktoken
            self.enc = tiktoken.get_encoding(encoding)
            self.vocab_size = self.enc.n_vocab
        except ImportError:
            raise ImportError("Instala tiktoken: pip install tiktoken")

    def encode(self, text: str) -> List[int]:
        return self.enc.encode(text, allowed_special={'<|endoftext|>'})

    def decode(self, tokens: List[int]) -> str:
        return self.enc.decode(tokens)

    def eot_token(self) -> int:
        return self.enc.eot_token


# ============================================================================
# MULTI-FILE CORPUS SYSTEM
# ============================================================================

_TEXT_EXTENSIONS: set = {
    '.py', '.c', '.h', '.cpp', '.cc', '.cxx', '.hpp', '.hxx',
    '.go', '.rs', '.js', '.ts', '.tsx', '.jsx', '.mjs', '.mts',
    '.md', '.txt', '.json', '.jsonl', '.jsonc',
    '.yaml', '.yml', '.toml', '.xml', '.svg',
    '.html', '.htm', '.css', '.scss', '.sass', '.less',
    '.sh', '.bash', '.zsh', '.fish', '.ash', '.ksh',
    '.asm', '.s', '.S', '.h',
    '.tex', '.cls', '.sty',
    '.r', '.R', '.rb', '.erb', '.rake',
    '.java', '.kt', '.kts', '.scala', '.groovy', '.gradle',
    '.swift', '.cs', '.fs', '.fsx', '.vb',
    '.lua', '.vim', '.el', '.clj', '.cljs', '.cljc', '.edn',
    '.ex', '.exs', '.erl', '.hrl', '.gleam',
    '.hs', '.purs', '.Agda', '.Idris',
    '.sql', '.pl', '.pm', '.t', '.prolog',
    '.ini', '.cfg', '.conf', '.inf', '.reg',
    '.env', '.editorconfig', '.gitignore', '.gitattributes',
    '.dockerfile', 'dockerfile', 'makefile', 'makefile', 'gnumakefile',
    '.cmake', '.cmake.in', '.mk', '.bazel', '.bzl', '.build',
    '.proto', '.graphql', '.gql', '.thrift',
    '.ps1', '.psm1', '.psd1', '.pssc',
    '.过户', '.汉',  # rare but valid UTF-8 filenames
}

_NO_EXT_NAMES: set = {
    'makefile', 'gnumakefile', 'cmakelists.txt', 'makefile.in',
    'dockerfile', 'containerfile', 'jenkinsfile', 'vagrantfile',
    'procfile', 'ruff.toml', 'pylintrc', 'flake8', 'mypy.ini',
    'setup.cfg', 'tox.ini', 'pytest.ini', '.coveragerc',
    'requirements.txt', 'requirements-dev.txt', 'pyproject.toml',
    'package.json', 'package-lock.json', 'tsconfig.json', 'jsconfig.json',
    'browserslist', '.babelrc', '.eslintrc', '.prettierrc',
    'vite.config', 'rollup.config', 'webpack.config', 'next.config',
    'nuxt.config', 'svelte.config', 'tailwind.config', 'postcss.config',
    'gradle.properties', 'build.gradle', 'settings.gradle',
    'cargo.toml', 'cargo.lock', 'rustfmt.toml', 'clippy.toml',
    'go.mod', 'go.sum', 'go.work',
    'build.gradle.kts', 'settings.gradle.kts',
    'composercjson', 'composer.lock',
    'gemfile', 'gemfile.lock', 'rakefile', 'rakefile.rb',
    'dockerignore', 'editorconfig', 'gitignore', 'gitattributes',
    'pre-commit', 'shell.nix', 'default.nix', 'flake.nix',
    'hosts', 'resolv.conf', 'nginx.conf', 'apache2.conf',
    'run', 'env', 'configure', 'install', 'build', 'clean',
}

_SKIP_SUFFIXES: set = {
    '.o', '.obj', '.so', '.dll', '.dylib', '.exe', '.elf', '.ko',
    '.bin', '.dat', '.pt', '.pth', '.ckpt', '.safetensors',
    '.zip', '.tar', '.gz', '.tar.gz', '.tgz', '.bz2', '.xz', '.7z',
    '.mp4', '.avi', '.mkv', '.mov', '.webm', '.mp3', '.wav', '.flac',
    '.png', '.jpg', '.jpeg', '.gif', '.bmp', '.svg', '.ico',
    '.ttf', '.woff', '.woff2', '.eot', '.otf',
    '.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx',
    '.db', '.sqlite', '.sqlite3', '.db3',
    '.pem', '.key', '.ccache', '.jks', '.keystore', '.p12', '.pfx',
    '.pyc', '.pyo', '.class', '.jar', '.war',
    '.iso', '.img', '.qcow2', '.vmdk', '.ova',
    '.py.bak', '.py.old', '.py.orig',
    '.min.js', '.min.css', '.bundle.js',
    '.lock', '.lock.json',  # package lock files are data, not code
}

_SKIP_DIRS: set = {
    '.git', '.svn', '.hg', '.bzr', 'node_modules', '__pycache__',
    '.venv', 'venv', 'env', '.env', '.conda',
    'build', 'dist', '.next', 'out', '.nuxt', '.svelte-kit',
    '.obsidian', '.trash', '.cache', '.tmp',
    'target', '.rustup', '.cargo', '.cargo/registry',
    '.mypy_cache', '.pytest_cache', '.ruff_cache',
    '.phpunit', '.parrot', 'lombok', '.gradle',
    'pb_data', '.qtcreator', '.idea', '.vscode',
    '.android', 'gradle/wrapper', '.gradle',
    'site-packages', 'node_modules', 'bower_components',
    '__pypackages__', '.pip-cache', '.npm', '.yarn',
    '.cache/pip', '.cache/modernizr',
}

_SKIP_DIRS: set = {
    '.git', 'node_modules', '__pycache__', '.venv', 'venv',
    'build', 'dist', '.obsidian', '.mypy_cache', '.pytest_cache',
    '.ruff_cache', 'target', '.next', 'out', '.qtcreator',
    'pb_data',
}

_SKIP_SUFFIXES: set = {
    '.o', '.obj', '.so', '.dll', '.dylib', '.exe', '.elf', '.ko',
    '.bin', '.dat', '.pt', '.pth', '.ckpt', '.safetensors',
    '.zip', '.tar', '.gz', '.tar.gz', '.tgz', '.bz2', '.xz', '.7z',
    '.mp4', '.avi', '.mkv', '.mov', '.webm', '.mp3', '.wav', '.flac',
    '.png', '.jpg', '.jpeg', '.gif', '.bmp', '.svg', '.ico',
    '.ttf', '.woff', '.woff2', '.eot', '.otf',
    '.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx',
    '.db', '.sqlite', '.sqlite3', '.db3',
    '.pem', '.key', '.ccache', '.jks', '.keystore',
    '.pyc', '.pyo', '.class', '.jar', '.war',
    '.iso', '.img', '.qcow2', '.vmdk', '.ova', '.safetensors',
}


class FileManifest:
    """Disk-cached manifest of text files found in a directory tree."""

    def __init__(self, root: str, cache_dir: str, logger: logging.Logger):
        self.root = root
        self.cache_dir = cache_dir
        self.logger = logger
        os.makedirs(cache_dir, exist_ok=True)
        self.cache_path = os.path.join(cache_dir, 'file_manifest.json')

    def scan(self, force: bool = False) -> List[str]:
        """Walk directory tree collecting text file paths. Cached to disk."""
        if not force and os.path.exists(self.cache_path):
            self.logger.info(f"Loading file manifest from cache: {self.cache_path}")
            try:
                with open(self.cache_path, 'r', encoding='utf-8') as f:
                    paths = json.load(f)
                self.logger.info(f"Manifest: {len(paths)} files (cached)")
                return paths
            except (json.JSONDecodeError, IOError):
                self.logger.warning("Corrupted manifest cache, rescanning...")

        self.logger.info(f"Scanning directory tree: {self.root}")
        paths = []
        count_total = 0
        count_skipped = 0
        try:
            base = Path(self.root).resolve()
            for entry in base.rglob('*'):
                count_total += 1
                if count_total % 50_000 == 0:
                    self.logger.info(
                        f"  Scan progress: {count_total:,} entries visited, "
                        f"{len(paths):,} text files found, "
                        f"{count_skipped:,} skipped")

                if not entry.is_file():
                    continue
                parts = set(entry.relative_to(base).parts)
                if parts & _SKIP_DIRS:
                    count_skipped += 1
                    continue
                suffix = entry.suffix.lower()
                if suffix in _SKIP_SUFFIXES:
                    count_skipped += 1
                    continue
                if suffix in _TEXT_EXTENSIONS:
                    paths.append(str(entry))
                    continue
                if suffix == '' and entry.name.lower() in _NO_EXT_NAMES:
                    paths.append(str(entry))
                    continue
                if suffix == '':
                    count_skipped += 1
                    continue
                count_skipped += 1
        except PermissionError:
            pass

        self.logger.info(
            f"Scan complete: {count_total:,} total entries, "
            f"{len(paths):,} text files, {count_skipped:,} skipped")
        with open(self.cache_path, 'w', encoding='utf-8') as f:
            json.dump(paths, f)
        return paths


class MemmapTokenizer:
    """Tokenizes file paths into a memory-mapped numpy array on disk.

    Uses incremental file reading and batched writing to avoid loading
    all tokens into RAM. Tokens are stored as raw int64 on disk and
    accessed via numpy memmap (OS-level paging, near-zero RAM footprint).
    """

    CHUNK_TOKENS = 2_000_000

    def __init__(self, cache_dir: str, logger: logging.Logger):
        self.cache_dir = cache_dir
        self.logger = logger
        os.makedirs(cache_dir, exist_ok=True)

    def tokenize(self, file_paths: List[str], tokenizer: 'BPETokenizer',
                 cache_key: str, max_tokens: int,
                 min_chars: int = 20) -> np.ndarray:
        """Tokenize all files and return a memory-mapped numpy array.

        Args:
            file_paths: List of absolute file paths to tokenize.
            tokenizer: BPE tokenizer instance.
            cache_key: Unique key for caching tokens to disk.
            max_tokens: Maximum number of tokens to produce.
            min_chars: Skip files with fewer characters.

        Returns:
            np.ndarray backed by a memmap on disk. Only accessed pages
            are loaded into RAM by the OS virtual memory system.
        """
        cache_path = os.path.join(self.cache_dir, f'tokens_{cache_key}.bin')
        meta_path = os.path.join(self.cache_dir, f'tokens_{cache_key}.json')

        if os.path.exists(cache_path) and os.path.exists(meta_path):
            with open(meta_path, 'r') as f:
                meta = json.load(f)
            n = meta['num_tokens']
            self.logger.info(f"Loading cached tokens: {n:,} tokens ({cache_key})")
            return np.memmap(cache_path, dtype=np.int64, mode='r', shape=(n,))

        self.logger.info(
            f"Tokenizing {len(file_paths):,} files (max {max_tokens:,} tokens)...")

        batch = []
        total = 0
        processed = 0

        with open(cache_path, 'wb') as f:
            for path in file_paths:
                try:
                    with open(path, 'r', encoding='utf-8', errors='replace') as fh:
                        text = fh.read()
                except (OSError, UnicodeError):
                    continue
                if len(text) < min_chars:
                    continue
                file_tokens = tokenizer.encode(text)
                batch.extend(file_tokens)
                total += len(file_tokens)
                processed += 1

                if len(batch) >= self.CHUNK_TOKENS:
                    arr = np.array(batch, dtype=np.int64)
                    f.write(arr.tobytes())
                    batch = []

                if total >= max_tokens > 0:
                    self.logger.info(
                        f"Reached max_tokens ({max_tokens:,}) after {processed} files")
                    break

            if batch:
                arr = np.array(batch, dtype=np.int64)
                f.write(arr.tobytes())

        total = os.path.getsize(cache_path) // 8
        with open(meta_path, 'w') as f:
            json.dump({
                'num_tokens': total,
                'cache_key': cache_key,
                'files_processed': processed,
            }, f)

        self.logger.info(
            f"Tokenized {total:,} tokens from {processed} files, cached: {cache_path}")
        return np.memmap(cache_path, dtype=np.int64, mode='r', shape=(total,))


class MappedTokenDataset(torch.utils.data.Dataset):
    """Memory-mapped token dataset for sequence-to-sequence LM training.

    The token array is backed by a numpy memmap file on disk.
    Only accessed slices are paged into RAM by the OS. The .copy()
    in __getitem__ ensures the returned torch.Tensor owns its memory,
    which is required for DataLoader collation with worker processes.
    """

    def __init__(self, tokens: np.ndarray, seq_len: int):
        self.tokens = tokens
        self.seq_len = seq_len
        self.n_seqs = (len(tokens) - 1) // seq_len

    def __len__(self) -> int:
        return self.n_seqs

    def __getitem__(self, idx: int) -> Tuple[torch.Tensor, torch.Tensor]:
        start = idx * self.seq_len
        x = torch.as_tensor(
            self.tokens[start:start + self.seq_len].copy(),
            dtype=torch.long,
        )
        y = torch.as_tensor(
            self.tokens[start + 1:start + self.seq_len + 1].copy(),
            dtype=torch.long,
        )
        return x, y


# ============================================================================
# TEXT QUALITY FILTER
# ============================================================================

class TextFilter:
    """Filters low-quality files from the corpus based on multiple heuristics."""

    def __init__(self, config: 'TopoGPT2Config', logger: logging.Logger):
        self.cfg = config
        self.logger = logger
        self._seen_hashes: set = set()
        self._stats = {
            'total': 0, 'entropy_low': 0, 'entropy_high': 0,
            'line_too_long': 0, 'special_token_high': 0, 'dup': 0, 'passed': 0,
        }

    def _compute_entropy(self, text: str) -> float:
        """Shannon entropy of byte frequencies (bits per byte)."""
        if not text:
            return 0.0
        import collections
        freq = collections.Counter(text)
        total = len(text)
        entropy = 0.0
        for count in freq.values():
            p = count / total
            if p > 0:
                entropy -= p * math.log2(p)
        return entropy

    def _has_long_lines(self, text: str, threshold: int) -> bool:
        """Return True if any line exceeds threshold characters."""
        for line in text.split('\n'):
            if len(line) > threshold:
                return True
        return False

    def _special_token_ratio(self, text: str, tokenizer: 'BPETokenizer') -> float:
        """Fraction of tokens that are pure whitespace or indentation-only."""
        try:
            tokens = tokenizer.encode(text)
        except Exception:
            return 1.0
        if not tokens:
            return 1.0
        whitespace_toks = sum(
            1 for t in tokens
            if tokenizer.enc.decode([t]).strip() == ''
        )
        return whitespace_toks / len(tokens)

    def _content_hash(self, text: str) -> str:
        return hashlib.sha256(text.encode('utf-8', errors='replace')).hexdigest()[:16]

    def filter_file(self, path: str, tokenizer: Optional['BPETokenizer'] = None) -> Optional[str]:
        """Read and evaluate a file. Returns text if passed, None if filtered."""
        self._stats['total'] += 1
        try:
            with open(path, 'r', encoding='utf-8', errors='replace') as f:
                text = f.read()
        except (OSError, UnicodeError):
            return None

        if len(text) < self.cfg.CORPUS_MIN_FILE_CHARS:
            return None

        entropy = self._compute_entropy(text)
        if entropy < self.cfg.FILTER_ENTROPY_MIN:
            self._stats['entropy_low'] += 1
            return None
        if entropy > self.cfg.FILTER_ENTROPY_MAX:
            self._stats['entropy_high'] += 1
            return None

        if self._has_long_lines(text, self.cfg.FILTER_MAX_LINE_LEN):
            self._stats['line_too_long'] += 1
            return None

        if tokenizer is not None and self.cfg.FILTER_SPECIAL_TOKEN_RATIO_MAX < 1.0:
            ratio = self._special_token_ratio(text, tokenizer)
            if ratio > self.cfg.FILTER_SPECIAL_TOKEN_RATIO_MAX:
                self._stats['special_token_high'] += 1
                return None

        if self.cfg.FILTER_ENABLE_DEDUP:
            h = self._content_hash(text)
            if h in self._seen_hashes:
                self._stats['dup'] += 1
                return None
            self._seen_hashes.add(h)

        self._stats['passed'] += 1
        return text

    def report(self) -> Dict[str, int]:
        s = self._stats
        self.logger.info(
            f"TextFilter: total={s['total']} passed={s['passed']} "
            f"entropy_low={s['entropy_low']} entropy_high={s['entropy_high']} "
            f"long_line={s['line_too_long']} special_tok={s['special_token_high']} "
            f"dedup={s['dup']}")
        return dict(self._stats)


# ============================================================================
# CURRICULUM DATASET
# ============================================================================

class CurriculumDataset(torch.utils.data.Dataset):
    """Tiered dataset that exposes short/medium/all files based on line count.

    Works as a wrapper around MappedTokenDataset. Provides __getitem__ that
    only samples from the active tier, avoiding dataset duplication.
    """

    def __init__(self, tokens: np.ndarray, seq_len: int,
                 file_tiers: Dict[int, List[int]],
                 active_tier: int = 0,
                 logger: Optional[logging.Logger] = None):
        self.base = MappedTokenDataset(tokens, seq_len)
        self.file_tiers = file_tiers
        self.active_tier = active_tier
        self.logger = logger or setup_logger('CurriculumDS')
        self._update_len()

    def _update_len(self):
        tier_files = self.file_tiers.get(self.active_tier, [])
        self.n_seqs = len(tier_files) if tier_files else 0
        self.logger.info(
            f"Curriculum tier {self.active_tier}: {self.n_seqs} sequences")

    def set_tier(self, tier: int):
        self.active_tier = tier
        self._update_len()

    def __len__(self) -> int:
        return self.n_seqs

    def __getitem__(self, idx: int) -> Tuple[torch.Tensor, torch.Tensor]:
        return self.base[idx]


# ============================================================================
# CURRICULUM BUILDERS
# ============================================================================

def build_file_tiers(paths: List[str], short: int, med: int) -> Dict[int, List[int]]:
    """Classify file paths into complexity tiers by line count.

    Returns dict: tier -> list of file indices in that tier.
    Tier 0 = short (<=short lines), tier 1 = medium, tier 2 = all.
    """
    tiers: Dict[int, list] = {0: [], 1: [], 2: []}
    for i, path in enumerate(paths):
        try:
            with open(path, 'r', encoding='utf-8', errors='replace') as f:
                n_lines = sum(1 for _ in f)
        except OSError:
            n_lines = 0
        if n_lines <= short:
            tiers[0].append(i)
        elif n_lines <= med:
            tiers[1].append(i)
        else:
            tiers[2].append(i)
    return tiers


# ============================================================================
# PROGRESSIVE SEQUENCE LENGTH TRAINER
# ============================================================================

class ProgressiveSeqLenTrainer:
    """Trainer that dynamically adjusts MAX_SEQ_LEN across training phases.

    Phase schedule (configurable):
        phase 0: seq_len=128, epochs=3
        phase 1: seq_len=256, epochs=3
        phase 2: seq_len=512, epochs=4

    Each phase rebuilds the DataLoader with the new sequence length.
    """

    def __init__(self, base_trainer: 'TopoGPT2Trainer'):
        self.trainer = base_trainer
        self.cfg = base_trainer.config
        self.logger = base_trainer.logger
        self.phase = 0

    def _build_dataloader(self, dataset: MappedTokenDataset, seq_len: int,
                          batch_size: int, is_train: bool) -> torch.utils.data.DataLoader:
        ds = MappedTokenDataset(dataset.tokens, seq_len)
        n_cpu = max(1, os.cpu_count() // 2)
        pin = 'cuda' in self.cfg.DEVICE
        return torch.utils.data.DataLoader(
            ds, batch_size=batch_size, shuffle=is_train,
            num_workers=n_cpu, pin_memory=pin, drop_last=is_train,
        )

    def run(self, train_paths: List[str], val_paths: List[str],
            tokenizer: 'BPETokenizer',
            file_tiers: Optional[Dict[int, List[int]]] = None,
            phases: Optional[Tuple[Tuple[int, int], ...]] = None) -> Dict:
        """Run training with progressive sequence length across phases."""
        if phases is None:
            phases = tuple(zip(
                self.cfg.PROGRESSIVE_SEQ_STEPS,
                self.cfg.PROGRESSIVE_SEQ_EPOCHS,
            ))

        self.logger.info(
            f"ProgressiveSeqLen: {len(phases)} phases, "
            f"{self.cfg.EPOCHS} total epochs")

        for phase_idx, (seq_len, n_epochs) in enumerate(phases):
            self.logger.info(
                f"[Phase {phase_idx}] seq_len={seq_len}, epochs={n_epochs}")

            self.cfg.MAX_SEQ_LEN = seq_len

            train_ds = MappedTokenDataset(
                self.trainer._tokens_cache['train'], seq_len)
            val_ds = MappedTokenDataset(
                self.trainer._tokens_cache.get('val', self.trainer._tokens_cache['train']),
                seq_len)

            n_cpu = max(1, os.cpu_count() // 2)
            pin = 'cuda' in self.cfg.DEVICE
            train_dl = torch.utils.data.DataLoader(
                train_ds, batch_size=self.cfg.BATCH_SIZE, shuffle=True,
                num_workers=n_cpu, pin_memory=pin, drop_last=True)
            val_dl = torch.utils.data.DataLoader(
                val_ds, batch_size=self.cfg.BATCH_SIZE * 2, shuffle=False,
                num_workers=max(1, n_cpu // 2), pin_memory=pin, drop_last=True)

            prev_epochs = self.trainer.completed_epochs
            self.trainer.train(train_dl, val_dl)
            self.logger.info(
                f"[Phase {phase_idx}] done. Epochs completed: "
                f"{prev_epochs} -> {self.trainer.completed_epochs}")

        return self.trainer.history


# ============================================================================
# SPECULATIVE DECODING
# ============================================================================

class SpeculativeDecoder:
    """Speculative decoding with a small draft model.

    Draft model uses SPEC_DECODE_DRAFT_SCALE (e.g. 'micro').
    The draft generates K tokens, then the target model verifies them
    in a single forward pass. Accepted tokens are kept; rejected ones
    trigger a fallback to the target model sampling.
    """

    def __init__(self, target_model: 'TopoGPT2', config: 'TopoGPT2Config',
                 logger: logging.Logger):
        self.target = target_model
        self.cfg = config
        self.logger = logger
        self.draft: Optional[TopoGPT2] = None
        self._build_draft()

    def _build_draft(self):
        draft_cfg = TopoGPT2Config(
            SCALE=self.cfg.SPEC_DECODE_DRAFT_SCALE,
            DEVICE=self.cfg.DEVICE,
            RANDOM_SEED=self.cfg.RANDOM_SEED,
        )
        draft_cfg.N_KV_HEADS = max(1, draft_cfg.N_HEADS // 4)
        self.draft = TopoGPT2(draft_cfg).to(self.cfg.DEVICE)
        self.draft.eval()
        self.logger.info(
            f"SpeculativeDecoder: draft scale={self.cfg.SPEC_DECODE_DRAFT_SCALE}, "
            f"params={self.draft.count_params()['total']:,}")

    @torch.no_grad()
    def generate(self, token_ids: torch.Tensor,
                max_new_tokens: int = 200,
                temperature: float = 0.8,
                top_k: int = 50,
                repetition_penalty: float = 1.0) -> torch.Tensor:
        """Autoregressive generation via speculative decoding.

        Each round: draft generates K tokens, target verifies all K in
        one O(1) forward pass (longest context), then samples the first
        rejection from the target.
        """
        self.target.eval()
        self.draft.eval()
        cfg = self.cfg

        ctx = token_ids[:, -cfg.MAX_SEQ_LEN:]
        logits, _, past_kvs = self.target(ctx)
        logits = logits[:, -1, :] / max(temperature, 1e-8)
        if repetition_penalty != 1.0:
            mask = torch.zeros_like(logits, dtype=torch.bool)
            mask.scatter_(1, ctx, True)
            logits = torch.where(mask, logits / repetition_penalty, logits)
        if top_k > 0:
            v, _ = torch.topk(logits, min(top_k, logits.size(-1)))
            logits[logits < v[:, -1:]] = float('-inf')
        next_tok = torch.multinomial(F.softmax(logits, dim=-1), 1)
        token_ids = torch.cat([token_ids, next_tok], dim=1)

        generated = [next_tok.item()]
        draft_past_kvs = None

        while len(generated) < max_new_tokens:
            k = min(cfg.SPEC_DECODE_K, max_new_tokens - len(generated))

            draft_ctx = token_ids
            if draft_past_kvs is not None:
                draft_logits, _, draft_past_kvs = self.draft(
                    token_ids[:, -self.draft.config.MAX_SEQ_LEN:],
                    past_kvs=draft_past_kvs)
            else:
                draft_logits, _, draft_past_kvs = self.draft(draft_ctx)
            draft_tok = torch.multinomial(
                F.softmax(draft_logits[:, -1, :] / max(temperature, 1e-8), dim=-1), k)

            accepted = []
            for t in range(k):
                d_tok = draft_tok[:, t:t+1]
                target_logits, _, past_kvs = self.target(
                    d_tok, past_kvs=past_kvs)
                t_logits = target_logits[:, -1, :] / max(temperature, 1e-8)
                if repetition_penalty != 1.0:
                    mask = torch.zeros_like(t_logits, dtype=torch.bool)
                    mask.scatter_(1, token_ids, True)
                    t_logits = torch.where(mask, t_logits / repetition_penalty, t_logits)
                prob = F.softmax(t_logits, dim=-1)
                if top_k > 0:
                    v, _ = torch.topk(t_logits, min(top_k, t_logits.size(-1)))
                    mask_k = t_logits < v[:, -1:]
                    logits_topk = t_logits.clone()
                    logits_topk[mask_k] = float('-inf')
                    prob = F.softmax(logits_topk, dim=-1)
                target_tok = torch.multinomial(prob, 1)
                if target_tok.item() == d_tok.item():
                    accepted.append(d_tok.item())
                    token_ids = torch.cat([token_ids, d_tok], dim=1)
                else:
                    token_ids = torch.cat([token_ids, target_tok], dim=1)
                    generated.extend(accepted)
                    break
            else:
                for t in range(k):
                    token_ids = torch.cat([token_ids, draft_tok[:, t:t+1]], dim=1)
                generated.extend([draft_tok[:, t:t+1].item() for t in range(k)])

            if (token_ids[:, -1:] == 50256).all():
                break

        return token_ids


# ============================================================================
# QUANTIZED EMBEDDING FOR INFERENCE
# ============================================================================

class QuantizedEmbedding(nn.Module):
    """Wrapper around nn.Embedding that applies dynamic quantization.

    Applies int8 quantization to the embedding weight matrix after loading.
    Supports both embed (int8) and FFN (int4) quantization modes.
    """

    def __init__(self, embed: nn.Embedding, mode: str = 'int8'):
        super().__init__()
        self.num_embeddings = embed.num_embeddings
        self.embedding_dim = embed.embedding_dim
        self.padding_idx = embed.padding_idx
        self.max_norm = embed.max_norm
        self.norm_type = embed.norm_type
        self.scale_grad_by_freq = embed.scale_grad_by_freq
        self.sparse = embed.sparse

        if mode == 'int8':
            self.weight = torch.quantize_per_channel(
                embed.weight.data.to(torch.float32),  # fp32 for quantize_per_channel
                scales=torch.ones(embed.weight.shape[0]),
                zero_points=torch.zeros(embed.weight.shape[0], dtype=torch.long),
                axis=0,
                dtype=torch.qint8,
            )
        elif mode == 'int4':
            self.weight = torch.quantize_per_channel(
                embed.weight.data.to(torch.float32),
                scales=torch.ones(embed.weight.shape[0]),
                zero_points=torch.zeros(embed.weight.shape[0], dtype=torch.long),
                axis=0,
                dtype=torch.qint8,
            )
        else:
            self.weight = embed.weight

    def forward(self, indices: torch.Tensor) -> torch.Tensor:
        return torch.embedding(self.weight, indices, padding_idx=self.padding_idx)


def apply_quantization(model: 'TopoGPT2', config: 'TopoGPT2Config') -> 'TopoGPT2':
    """Quantize embedding and lm_head layers for reduced VRAM usage."""
    if not config.QUANTIZE_EMBEDDINGS:
        return model

    logger = setup_logger('Quantize')
    device = config.DEVICE

    embed = model.token_embed
    quantized_embed = QuantizedEmbedding(embed, mode='int8')
    model.token_embed = quantized_embed
    model.lm_head = nn.Linear(
        model.lm_head.in_features, model.lm_head.out_features, bias=False)
    model.lm_head.weight = quantized_embed.weight

    logger.info(
        f"Quantized embeddings to int8: shape={quantized_embed.weight.shape}")

    if config.QUANTIZE_FFN:
        logger.warning("FFN int4 quantization is experimental; skipping.")

    return model


# ============================================================================
# CURRICULUM TRAINER WRAPPER
# ============================================================================

class CurriculumTrainer:
    """Extends TopoGPT2Trainer with curriculum + progressive seq len support.

    Provides:
    - Tokens cache for progressive sequence length rebuilding
    - Curriculum dataset wrapping (short / medium / all tiers)
    """

    def __init__(self, model, config, tokenizer=None):
        self._base = TopoGPT2Trainer(model, config, tokenizer)
        self.cfg = config
        self.logger = self._base.logger
        self._tokens_cache: Dict[str, np.ndarray] = {}
        self._curriculum_ds: Optional[CurriculumDataset] = None

    def cache_tokens(self, key: str, tokens: np.ndarray):
        self._tokens_cache[key] = tokens

    @property
    def model(self):
        return self._base.model

    @property
    def optimizer(self):
        return self._base.optimizer

    @property
    def scaler(self):
        return self._base.scaler

    @property
    def amp_dtype(self):
        return self._base.amp_dtype

    @property
    def completed_epochs(self):
        return self._base.completed_epochs

    @completed_epochs.setter
    def completed_epochs(self, v):
        self._base.completed_epochs = v

    @property
    def global_step(self):
        return self._base.global_step

    @global_step.setter
    def global_step(self, v):
        self._base.global_step = v

    @property
    def best_val_loss(self):
        return self._base.best_val_loss

    @best_val_loss.setter
    def best_val_loss(self, v):
        self._base.best_val_loss = v

    @property
    def history(self):
        return self._base.history

    @property
    def ckpt_mgr(self):
        return self._base.ckpt_mgr

    def resume(self) -> bool:
        return self._base.resume()

    def _current_state(self) -> Dict:
        return self._base._current_state()

    def _cosine_lr(self, *args, **kwargs):
        return self._base._cosine_lr(*args, **kwargs)

    def _set_lr(self, *args, **kwargs):
        self._base._set_lr(*args, **kwargs)

    def evaluate(self, dataloader):
        return self._base.evaluate(dataloader)

    def _sample_text(self, *args, **kwargs):
        self._base._sample_text(*args, **kwargs)

    def _progressive_train(self, train_paths: List[str], val_paths: List[str],
                          tokenizer: 'BPETokenizer',
                          phases: Tuple[Tuple[int, int], ...],
                          memtok: 'MemmapTokenizer') -> Dict:
        """Training loop with progressive sequence length across phases."""
        cfg = self.cfg
        device = cfg.DEVICE
        logger = self.logger

        for phase_idx, (seq_len, n_epochs) in enumerate(phases):
            logger.info(
                f"[ProgressiveSeqLen Phase {phase_idx}] "
                f"seq_len={seq_len}, epochs={n_epochs}")

            cfg.MAX_SEQ_LEN = seq_len

            train_ds = MappedTokenDataset(
                self._tokens_cache['train'], seq_len)
            val_ds = MappedTokenDataset(
                self._tokens_cache.get('val', self._tokens_cache['train']),
                seq_len)

            n_cpu = max(1, os.cpu_count() // 2)
            pin = 'cuda' in device
            train_dl = torch.utils.data.DataLoader(
                train_ds, batch_size=cfg.BATCH_SIZE, shuffle=True,
                num_workers=n_cpu, pin_memory=pin, drop_last=True)
            val_dl = torch.utils.data.DataLoader(
                val_ds, batch_size=cfg.BATCH_SIZE * 2, shuffle=False,
                num_workers=max(1, n_cpu // 2), pin_memory=pin, drop_last=True)

            prev_completed = self.completed_epochs
            self._base.train(train_dl, val_dl)
            logger.info(
                f"[Phase {phase_idx}] done. "
                f"Epochs: {prev_completed} -> {self.completed_epochs}")

        return self.history

    def train(self, train_dl, val_dl):
        return self._base.train(train_dl, val_dl)

    def run_curriculum(self, train_paths: List[str], val_paths: List[str],
                       tokenizer: 'BPETokenizer',
                       phases: Optional[Tuple[Tuple[int, int], ...]] = None):
        """Top-level entry point: curriculum + progressive seq len."""
        if phases is None:
            phases = tuple(zip(
                self.cfg.PROGRESSIVE_SEQ_STEPS,
                self.cfg.PROGRESSIVE_SEQ_EPOCHS,
            ))
        return self._progressive_train(
            train_paths, val_paths, tokenizer, phases,
            MemmapTokenizer(self.cfg.DATA_DIR, self.logger))


def _tokenize_text_to_memmap(text: str, tokenizer: 'BPETokenizer',
                              path: str, max_tokens: int) -> np.ndarray:
    """Tokenize a single text string and write tokens to disk as raw int64."""
    tokens = np.array(tokenizer.encode(text)[:max_tokens], dtype=np.int64)
    tokens.tofile(path)
    return np.memmap(path, dtype=np.int64, mode='r', shape=(len(tokens),))


# ============================================================================
# CHECKPOINT MANAGER (safetensors + JSON + optimizer.pt)
# ============================================================================

class CheckpointManager:
    """
    Gestiona checkpoints de forma acumulativa y segura.

    Estructura en disco:
        checkpoints_topogpt2/
          latest/
            model.safetensors   <- pesos del modelo (formato seguro, sin pickle)
            optimizer.pt        <- estado del optimizador (requiere .pt)
            state.json          <- metadatos: epoch, step, historial, config
          best/
            model.safetensors
            state.json
          step_NNNNN/           <- snapshots periodicos (rotados)
            model.safetensors
            optimizer.pt
            state.json

    El historial se ACUMULA entre sesiones de entrenamiento: cada --resume
    agrega nuevas entradas a train_loss[], val_loss[], etc.
    """

    LATEST = 'latest'
    BEST = 'best'

    def __init__(self, config: TopoGPT2Config, logger: logging.Logger):
        self.root = config.CHECKPOINT_DIR
        self.max_snapshots = config.MAX_CHECKPOINTS
        self.interval_min = config.CHECKPOINT_INTERVAL_MINUTES
        self.logger = logger
        self._last_save_time = time.time()
        self._snapshot_dirs: List[str] = []
        for sub in (self.LATEST, self.BEST):
            os.makedirs(os.path.join(self.root, sub), exist_ok=True)

    def patch_config_for_resume(self, cfg: 'TopoGPT2Config') -> None:
        """
        Lee el checkpoint 'latest' y ajusta cfg.N_KV_HEADS / cfg.GQA_GROUPS
        para que coincidan con la arquitectura guardada.
        Necesario cuando el codigo cambio GQA despues de guardar el checkpoint.
        """
        model_path = os.path.join(self.root, self.LATEST, 'model.safetensors')
        if not os.path.exists(model_path):
            return
        sd = st_load(model_path, device='cpu')
        key = 'layers.0.attn.k_proj.weight'
        if key in sd:
            ckpt_kv_dim = sd[key].shape[0]
            d_head = cfg.D_MODEL // cfg.N_HEADS
            ckpt_n_kv = ckpt_kv_dim // d_head
            if ckpt_n_kv != cfg.N_KV_HEADS:
                self.logger.info(
                    f"Checkpoint usa N_KV_HEADS={ckpt_n_kv} "
                    f"(config actual: {cfg.N_KV_HEADS}). "
                    "Ajustando para compatibilidad con el checkpoint."
                )
                cfg.N_KV_HEADS = ckpt_n_kv
                cfg.GQA_GROUPS = cfg.N_HEADS // ckpt_n_kv
        del sd

    # ------------------------------------------------------------------
    # Persistencia de pesos: safetensors (sin pickle, sin ejecucion de codigo)
    # ------------------------------------------------------------------

    def _save_model(self, model: 'TopoGPT2', directory: str) -> None:
        path = os.path.join(directory, 'model.safetensors')
        # El weight-tying hace que lm_head.weight y token_embed.weight sean el
        # mismo tensor en memoria. safetensors rechaza tensores compartidos,
        # por lo que excluimos lm_head.weight al guardar; al cargar el modelo
        # el weight-tying lo restaura automaticamente desde token_embed.weight.
        sd = {
            k: v.contiguous().cpu()
            for k, v in model.state_dict().items()
            if k != 'lm_head.weight'
        }
        st_save(sd, path)

    def _load_model(self, model: 'TopoGPT2', directory: str) -> None:
        path = os.path.join(directory, 'model.safetensors')
        sd = st_load(path, device=model.config.DEVICE)
        # strict=False porque lm_head.weight no esta en el archivo
        # (se reconstruye via weight-tying con token_embed.weight)
        missing, unexpected = model.load_state_dict(sd, strict=False)
        # lm_head.weight se reconstruye via weight-tying, ignorar siempre
        unexpected_real = [k for k in unexpected if k != 'lm_head.weight']
        missing_real    = [k for k in missing    if k != 'lm_head.weight']
        if unexpected_real:
            # Claves del checkpoint que ya no existen en el modelo (modulos eliminados).
            # Con strict=False esos pesos simplemente no se cargan; solo advertimos.
            modules = sorted({k.split('.')[2] if k.count('.') >= 2 else k
                               for k in unexpected_real})
            self.logger.warning(
                f"Checkpoint tiene {len(unexpected_real)} claves no presentes en el "
                f"modelo actual (modulos eliminados: {modules}). Se ignoran."
            )
        if missing_real:
            # Claves del modelo que no estaban en el checkpoint (modulos nuevos).
            modules = sorted({k.split('.')[2] if k.count('.') >= 2 else k
                               for k in missing_real})
            self.logger.warning(
                f"Modelo tiene {len(missing_real)} claves sin checkpoint "
                f"(modulos nuevos: {modules}). Se inicializan aleatoriamente."
            )

    # ------------------------------------------------------------------
    # Persistencia del optimizador: torch.save (estado con tipos mixtos)
    # ------------------------------------------------------------------

    def _save_optimizer(self, optimizer, directory: str) -> None:
        torch.save(optimizer.state_dict(), os.path.join(directory, 'optimizer.pt'))

    def _load_optimizer(self, optimizer, directory: str, device: str) -> None:
        path = os.path.join(directory, 'optimizer.pt')
        sd = torch.load(path, map_location=device, weights_only=True)
        optimizer.load_state_dict(sd)

    # ------------------------------------------------------------------
    # Metadatos en JSON (legible por humanos, sin ejecucion de codigo)
    # ------------------------------------------------------------------

    def _save_state(self, state: Dict, directory: str) -> None:
        path = os.path.join(directory, 'state.json')
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(state, f, indent=2)

    def _load_state(self, directory: str) -> Dict:
        path = os.path.join(directory, 'state.json')
        if not os.path.exists(path):
            return {}
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    # ------------------------------------------------------------------
    # API publica
    # ------------------------------------------------------------------

    def should_save(self) -> bool:
        return (time.time() - self._last_save_time) / 60 >= self.interval_min

    def save(self, model: 'TopoGPT2', optimizer,
             state: Dict, is_best: bool = False) -> str:
        """
        Guarda checkpoint completo.

        state debe contener al menos: completed_epochs, global_step,
        best_val_loss, history, config.
        """
        # Siempre actualizar 'latest'
        latest_dir = os.path.join(self.root, self.LATEST)
        self._save_model(model, latest_dir)
        self._save_optimizer(optimizer, latest_dir)
        self._save_state(state, latest_dir)

        # Guardar 'best' si mejoro la perdida de validacion
        if is_best:
            best_dir = os.path.join(self.root, self.BEST)
            self._save_model(model, best_dir)
            self._save_state(state, best_dir)
            self.logger.info(
                f"Nuevo mejor modelo guardado "
                f"(val_loss={state.get('best_val_loss', '?'):.4f})"
            )

        # Snapshot periodico con rotacion
        step = state.get('global_step', 0)
        snap_dir = os.path.join(self.root, f'step_{step:07d}')
        os.makedirs(snap_dir, exist_ok=True)
        self._save_model(model, snap_dir)
        self._save_optimizer(optimizer, snap_dir)
        self._save_state(state, snap_dir)
        self._snapshot_dirs.append(snap_dir)

        # Eliminar snapshots antiguos manteniendo solo max_snapshots
        while len(self._snapshot_dirs) > self.max_snapshots:
            old = self._snapshot_dirs.pop(0)
            import shutil
            if os.path.isdir(old):
                shutil.rmtree(old, ignore_errors=True)

        self._last_save_time = time.time()
        self.logger.info(f"Checkpoint guardado: epoch={state.get('completed_epochs')}, "
                         f"step={step}")
        return snap_dir

    def load_latest(self, model: 'TopoGPT2', optimizer) -> Dict:
        """
        Carga el ultimo checkpoint guardado.
        Devuelve el state dict (vacio si no hay checkpoint).
        """
        latest_dir = os.path.join(self.root, self.LATEST)
        model_path = os.path.join(latest_dir, 'model.safetensors')
        if not os.path.exists(model_path):
            self.logger.info("No se encontro checkpoint previo, iniciando desde cero.")
            return {}

        self._load_model(model, latest_dir)
        opt_path = os.path.join(latest_dir, 'optimizer.pt')
        if os.path.exists(opt_path):
            try:
                self._load_optimizer(optimizer, latest_dir, model.config.DEVICE)
            except Exception as e:
                self.logger.warning(f"No se pudo cargar estado del optimizador: {e}")

        state = self._load_state(latest_dir)
        self.logger.info(
            f"Checkpoint cargado: epoch={state.get('completed_epochs', 0)}, "
            f"step={state.get('global_step', 0)}, "
            f"best_val_loss={state.get('best_val_loss', float('inf')):.4f}"
        )
        return state

    def load_best(self, model: 'TopoGPT2') -> Dict:
        """Carga el mejor modelo guardado (solo pesos, sin optimizador)."""
        best_dir = os.path.join(self.root, self.BEST)
        model_path = os.path.join(best_dir, 'model.safetensors')
        if not os.path.exists(model_path):
            self.logger.warning("No hay checkpoint 'best' disponible.")
            return {}
        self._load_model(model, best_dir)
        state = self._load_state(best_dir)
        self.logger.info(f"Mejor modelo cargado: val_loss={state.get('best_val_loss', '?'):.4f}")
        return state

    def has_checkpoint(self) -> bool:
        return os.path.exists(
            os.path.join(self.root, self.LATEST, 'model.safetensors')
        )


# ============================================================================
# ENTRENADOR ACUMULATIVO
# ============================================================================

class TopoGPT2Trainer:
    """
    Entrenador acumulativo y resumible.

    Caracteristicas:
    - Checkpoint automatico en safetensors cada N minutos + cada epoch
    - Historial acumulativo entre sesiones (--resume agrega al historial existente)
    - Guarda el mejor modelo en checkpoints/best/ automaticamente
    - LR schedule: cosine con warmup relativo a los steps de ESTA sesion
    - Mixed Precision (AMP) + acumulacion de gradientes
    """

    def __init__(self, model: 'TopoGPT2', config: TopoGPT2Config,
                 tokenizer: Optional['BPETokenizer'] = None):
        self.model = model.to(config.DEVICE)
        self.config = config
        self.tokenizer = tokenizer        # para generacion de muestra por epoch
        self.logger = setup_logger('Trainer', config.LOG_LEVEL)
        self.ckpt_mgr = CheckpointManager(config, self.logger)

        self.optimizer = torch.optim.AdamW(
            model.parameters(),
            lr=config.LEARNING_RATE,
            weight_decay=config.WEIGHT_DECAY,
            betas=(0.9, 0.95),
        )

        dev = config.DEVICE
        self.scaler = torch.amp.GradScaler(
            dev.split(':')[0],
            enabled=config.USE_AMP and 'cuda' in dev,
        )
        self.amp_dtype = torch.float16 if 'cuda' in dev else torch.bfloat16

        # Estado de entrenamiento (se carga desde checkpoint si se hace --resume)
        self.completed_epochs: int = 0
        self.global_step: int = 0
        self.best_val_loss: float = float('inf')
        self.history: Dict[str, List] = {
            'train_loss': [], 'val_loss': [], 'perplexity': [], 'recon_loss': [],
            'delta': [], 'alpha': [], 't_eff': [], 'kappa': [],
            'berry_phase': [], 'winding_number': [], 'lc': [], 'sp': [], 'phase': [],
        }

        # Metricas mecanisticas (Book.md)
        self.mets = MechanisticMetrics(config)

    def resume(self) -> bool:
        """
        Carga el ultimo checkpoint disponible.
        Restaura: pesos del modelo, estado del optimizador, historial acumulado,
        epoch/step completados y mejor val_loss.
        Devuelve True si se cargo un checkpoint, False si empieza de cero.
        """
        if not self.ckpt_mgr.has_checkpoint():
            return False

        state = self.ckpt_mgr.load_latest(self.model, self.optimizer)
        if not state:
            return False

        self.completed_epochs = state.get('completed_epochs', 0)
        self.global_step = state.get('global_step', 0)
        self.best_val_loss = state.get('best_val_loss', float('inf'))

        # Restaurar historial acumulado (incluye metricas mecanisticas)
        prev_hist = state.get('history', {})
        for key in self.history:
            self.history[key] = prev_hist.get(key, [])

        return True

    def _current_state(self) -> Dict:
        """Construye el dict de estado para persistir en state.json."""
        return {
            'completed_epochs': self.completed_epochs,
            'global_step': self.global_step,
            'best_val_loss': self.best_val_loss,
            'history': self.history,
            'config': asdict(self.config),
            'saved_at': datetime.now().isoformat(),
        }

    def _cosine_lr(self, step_in_session: int, total_steps_session: int) -> float:
        """Cosine decay con warmup. El schedule es relativo a la sesion actual."""
        warmup = max(1, int(total_steps_session * self.config.WARMUP_RATIO))
        if step_in_session < warmup:
            return self.config.LEARNING_RATE * step_in_session / warmup
        t = (step_in_session - warmup) / max(total_steps_session - warmup, 1)
        return self.config.LEARNING_RATE * 0.5 * (1.0 + math.cos(math.pi * t))

    def _set_lr(self, lr: float) -> None:
        for pg in self.optimizer.param_groups:
            pg['lr'] = lr

    def train(self, train_dl: torch.utils.data.DataLoader,
              val_dl: torch.utils.data.DataLoader) -> Dict[str, List[float]]:
        """
        Entrena cfg.EPOCHS epocas adicionales a partir de completed_epochs.
        El historial se acumula sobre sesiones previas.
        """
        cfg = self.config
        device = cfg.DEVICE
        epochs_this_session = cfg.EPOCHS
        steps_per_epoch = len(train_dl)
        total_steps_session = steps_per_epoch * epochs_this_session // cfg.GRAD_ACCUM_STEPS
        step_in_session = 0

        self.logger.info("=" * 70)
        self.logger.info("TopoGPT2 - Entrenamiento acumulativo")
        p = self.model.count_params()
        self.logger.info(f"Parametros: {p['total']:,}")
        self.logger.info(f"Device: {device} | AMP: {cfg.USE_AMP} | "
                         f"GradCkpt: {cfg.GRADIENT_CHECKPOINTING}")
        self.logger.info(f"Escala: {cfg.SCALE} | D_MODEL: {cfg.D_MODEL} | "
                         f"Capas: {cfg.N_LAYERS} | SEQ_LEN: {cfg.MAX_SEQ_LEN}")
        self.logger.info(f"Toro: {cfg.TORUS_RADIAL_BINS}x{cfg.TORUS_ANGULAR_BINS} "
                         f"= {cfg.N_TORUS_NODES} nodos")
        self.logger.info(f"Epocas previas completadas: {self.completed_epochs}")
        self.logger.info(f"Epocas a entrenar ahora: {epochs_this_session}")
        self.logger.info(f"Mejor val_loss hasta ahora: {self.best_val_loss:.4f}")
        self.logger.info("=" * 70)

        for epoch_offset in range(1, epochs_this_session + 1):
            epoch_abs = self.completed_epochs + epoch_offset
            self.model.train()
            epoch_lm_loss = 0.0
            epoch_recon = 0.0
            n_batches = 0

            self.optimizer.zero_grad()

            for batch_x, batch_y in train_dl:
                batch_x = batch_x.to(device, non_blocking=True)
                batch_y = batch_y.to(device, non_blocking=True)

                lr = self._cosine_lr(step_in_session, total_steps_session)
                self._set_lr(lr)

                with torch.amp.autocast(device_type=device.split(':')[0],
                                        dtype=self.amp_dtype,
                                        enabled=cfg.USE_AMP):
                    logits, recon_loss, _ = self.model(batch_x)
                    lm_loss = F.cross_entropy(
                        logits.view(-1, cfg.VOCAB_SIZE),
                        batch_y.view(-1),
                    )
                    loss = (lm_loss + cfg.AE_RECON_WEIGHT * recon_loss) / cfg.GRAD_ACCUM_STEPS

                self.scaler.scale(loss).backward()
                self.mets.update_grad_buffer(self.model)

                n_batches += 1
                if n_batches % cfg.GRAD_ACCUM_STEPS == 0:
                    self.scaler.unscale_(self.optimizer)
                    torch.nn.utils.clip_grad_norm_(
                        self.model.parameters(), cfg.GRADIENT_CLIP_NORM)
                    self.scaler.step(self.optimizer)
                    self.scaler.update()
                    self.optimizer.zero_grad()
                    self.global_step += 1
                    step_in_session += 1

                epoch_lm_loss += lm_loss.item()
                epoch_recon += recon_loss.item()

                if n_batches % cfg.LOG_INTERVAL_STEPS == 0:
                    self.logger.info(
                        f"Epoch {epoch_abs} | batch {n_batches}/{steps_per_epoch} | "
                        f"lm_loss={epoch_lm_loss/n_batches:.4f} | "
                        f"recon={epoch_recon/n_batches:.4f} | "
                        f"lr={lr:.2e}"
                    )

                # Checkpoint periodico intra-epoch
                if self.ckpt_mgr.should_save():
                    self.ckpt_mgr.save(
                        self.model, self.optimizer,
                        self._current_state(), is_best=False,
                    )

            # -- Fin de epoch --
            avg_lm = epoch_lm_loss / max(n_batches, 1)
            avg_recon = epoch_recon / max(n_batches, 1)
            val_loss, ppl = self.evaluate(val_dl)

            # Metricas mecanisticas (Book.md)
            m = self.mets.compute_all(
                self.model, lr=self._cosine_lr(step_in_session, total_steps_session),
                dataloader=val_dl, compute_kappa=False,
            )

            self.completed_epochs += 1
            self.history['train_loss'].append(avg_lm)
            self.history['val_loss'].append(val_loss)
            self.history['perplexity'].append(ppl)
            self.history['recon_loss'].append(avg_recon)
            self.history['delta'].append(m.get('delta', 0.0))
            self.history['alpha'].append(m.get('alpha', 0.0))
            self.history['t_eff'].append(m.get('t_eff', 0.0))
            self.history['kappa'].append(m.get('kappa', 0.0))
            self.history['berry_phase'].append(m.get('berry_phase', 0.0))
            self.history['winding_number'].append(m.get('winding_number', 0))
            self.history['lc'].append(m.get('lc', 0.0))
            self.history['sp'].append(m.get('sp', 0.0))
            self.history['phase'].append(m.get('phase', 'unknown'))

            is_best = val_loss < self.best_val_loss
            if is_best:
                self.best_val_loss = val_loss

            self.logger.info(
                f"[Epoch {epoch_abs:4d}] "
                f"train={avg_lm:.4f} | val={val_loss:.4f} | "
                f"ppl={ppl:.2f} | recon={avg_recon:.4f} | "
                + self.mets.format_log(m)
                + (" <- mejor" if is_best else "")
            )

            # Checkpoint al final de cada epoch
            self.ckpt_mgr.save(
                self.model, self.optimizer,
                self._current_state(), is_best=is_best,
            )

            # Muestra de texto (calidad cualitativa)
            self._sample_text(self.tokenizer)

        return self.history

    @torch.no_grad()
    def _sample_text(self, tokenizer=None, prompts: Optional[List[str]] = None,
                     max_new: int = 80, temperature: float = 0.8, top_k: int = 40) -> None:
        """
        Genera una muestra de texto al final de cada epoch para monitorear
        la calidad cualitativa del modelo (detecta degeneracion, repeticion, etc.).
        """
        if tokenizer is None:
            return
        default_prompts = [
            "Once upon a time",
            "The little girl",
            "In the forest there",
        ]
        sample_prompts = prompts or default_prompts
        self.model.eval()
        device = self.config.DEVICE
        self.logger.info("-" * 60)
        self.logger.info("Muestra de generacion:")
        for prompt in sample_prompts:
            ids = tokenizer.encode(prompt)
            ids_t = torch.tensor([ids], dtype=torch.long, device=device)
            gen = self.model.generate(
                ids_t, max_new_tokens=max_new,
                temperature=temperature, top_k=top_k)
            text = tokenizer.decode(gen[0].tolist())
            # Mostrar solo los primeros 200 chars para no saturar el log
            preview = text.replace('\n', ' ')[:200]
            self.logger.info(f"  [{prompt!r}] -> {preview!r}")
        self.logger.info("-" * 60)
        self.model.train()

    @torch.no_grad()
    def evaluate(self, dataloader) -> Tuple[float, float]:
        self.model.eval()
        total_loss, n = 0.0, 0
        device = self.config.DEVICE

        for batch_x, batch_y in dataloader:
            batch_x = batch_x.to(device, non_blocking=True)
            batch_y = batch_y.to(device, non_blocking=True)
            with torch.amp.autocast(device_type=device.split(':')[0],
                                    dtype=self.amp_dtype,
                                    enabled=self.config.USE_AMP):
                logits, _, _ = self.model(batch_x)
                loss = F.cross_entropy(
                    logits.view(-1, self.config.VOCAB_SIZE), batch_y.view(-1))
            total_loss += loss.item()
            n += 1

        self.model.train()
        avg = total_loss / max(n, 1)
        ppl = math.exp(min(avg, 20.0))
        return avg, ppl


# ============================================================================
# INTERPRETACION MECANISTICA (Book.md)
# Metricas del diagrama de fases: delta, kappa, T_eff, alpha, Berry, LC, SP
# Clasificacion de fases: cold_glass, functional_glass,
#                         topological_insulator, discrete_crystal
# ============================================================================

class MechanisticMetrics:
    """
    Calcula todas las metricas del diagrama de fases de Book.md.

    Todas las metricas se derivan de cantidades medibles (pesos, gradientes):

    delta  (δ): margen de discretizacion.  max|w - round(w)|
                δ≈0 -> cristal;  δ≈0.49 -> vidrio frio
    kappa  (κ): numero de condicion de la covarianza del gradiente.
                κ≈1 -> cristalino;  κ>>1 -> amorfo
    T_eff:      temperatura efectiva = (lr/2) * Var(gradiente).
                T_eff→0 -> congelado; T_eff alto -> ruidoso
    alpha  (α): indice de pureza = -log(δ + ε).
                α=20 -> perfecto; α<1 -> vidrio
    berry:      fase de Berry de los kernels espectrales imaginarios.
                |berry|>π/2 con winding≠0 -> insulador topologico
    lc:         complejidad local = 1 - similitud coseno promedio entre filas.
    sp:         superposicion = correlacion promedio inter-fila de pesos.
    """

    def __init__(self, config: 'TopoGPT2Config'):
        self.config = config
        self.grad_buffer: deque = deque(maxlen=50)
        self.max_grad_sample = 500
    # ------------------------------------------------------------------
    # Metricas individuales
    # ------------------------------------------------------------------

    def compute_delta(self, model: nn.Module) -> float:
        margins = []
        for p in model.parameters():
            if p.numel() > 0 and p.is_floating_point():
                margins.append((p.data - p.data.round()).abs().max().item())
        return max(margins) if margins else 0.0

    def compute_alpha(self, delta: float) -> float:
        if delta < 1e-8:
            return 20.0
        return -math.log(delta + 1e-10)

    def update_grad_buffer(self, model: nn.Module) -> None:
        """Captura gradientes de forma segura, ignorando tensores corruptos."""
        parts = []
        for p in model.parameters():
            if p.grad is not None and p.numel() > 0:
                try:
                    # Mover a CPU de forma síncrona y segura. Si la GPU está en estado
                    # corrupto, se captura aquí sin abortar el entrenamiento.
                    grad_cpu = p.grad.detach().cpu().float()
                except RuntimeError:
                    continue

                # 1. Verificar corrupción numérica en CPU (evita sincronizaciones CUDA bloqueantes)
                if torch.isnan(grad_cpu).any() or torch.isinf(grad_cpu).any():
                    continue  # Salta gradientes inválidos generados por overflow AMP

                # 2. Muestreo uniforme para mantener el buffer ligero y estadísticamente representativo
                flat = grad_cpu.flatten()
                if flat.numel() > self.max_grad_sample:
                    step = max(1, flat.numel() // self.max_grad_sample)
                    flat = flat[::step][:self.max_grad_sample]
                parts.append(flat)

        if parts:
            self.grad_buffer.append(torch.cat(parts))

    def compute_t_eff(self, lr: float) -> float:
        """T_eff = lr/2 * Var(gradiente). Temperatura termodinamica efectiva."""
        if len(self.grad_buffer) < 2:
            return float('inf')
        G = torch.stack(list(self.grad_buffer))   # [N, D]
        var = G.pow(2).mean() - G.mean(0).pow(2).mean()
        return float(lr * var.clamp(min=0).item() / 2.0)

    def compute_kappa(self, model: nn.Module, dataloader,
                      n_batches: int = 5) -> float:
        """
        κ = λ_max / λ_min de la covarianza del gradiente.
        Parámetro de orden para cristalización (κ≈1 = cristal).
        Nota: requiere pasadas backward adicionales. Se ejecuta con protección
        para no corromper el estado AMP del trainer principal.
        """
        device = self.config.DEVICE
        model.eval()
        grad_samples = []
        for i, (bx, by) in enumerate(dataloader):
            if i >= n_batches:
                break
            bx, by = bx.to(device), by.to(device)
            model.zero_grad()
            try:
                with torch.no_grad():
                    pass # Placeholder para mantener estructura
                logits, _, _ = model(bx)
                loss = F.cross_entropy(
                    logits.view(-1, self.config.VOCAB_SIZE), by.view(-1))
                loss.backward()

                parts = []
                for p in model.parameters():
                    if p.grad is not None:
                        # Muestreo seguro a CPU para análisis
                        g = p.grad.detach().flatten()[:300].cpu().float()
                        if not torch.isnan(g).any() and not torch.isinf(g).any():
                            parts.append(g)
                if parts:
                    grad_samples.append(torch.cat(parts))
            except RuntimeError:
                # Si el cálculo de kappa falla (ej. OOM o kernel crash),
                # retorna inf para marcar inestabilidad sin abortar
                model.zero_grad()
                return float('inf')
            finally:
                model.zero_grad()

        model.train()
        if len(grad_samples) < 2:
            return float('inf')
        G = torch.stack(grad_samples)
        try:
            if G.size(0) < G.size(1):
                gram = G @ G.t() / max(G.size(0) - 1, 1)
                eigs = torch.linalg.eigvalsh(gram).real
            else:
                eigs = torch.linalg.eigvalsh(torch.cov(G.t())).real
            eigs = eigs[eigs > 1e-10]
            if len(eigs) < 2:
                return float('inf')
            return float(eigs.max() / eigs.min())
        except Exception:
            return float('inf')

    def compute_berry_phase(self, model: nn.Module) -> float:
        """
        Fase de Berry de los kernels espectrales imaginarios.
        Surge de los parametros ki_w, ki_x, ki_y, ki_z de QuaternionSpectralLayer.
        |berry|>pi/2 con winding!=0 indica estructura topologica.
        """
        phases = []
        for name, p in model.named_parameters():
            if 'ki_' in name and p.numel() > 0:
                flat = p.detach().flatten().float()
                phases.append(torch.atan2(flat, flat.abs() + 1e-10).sum().item())
        return sum(phases) if phases else 0.0

    def compute_lc(self, model: nn.Module) -> float:
        """Complejidad local: 1 - similitud coseno promedio entre filas de pesos."""
        vals = []
        for name, p in model.named_parameters():
            if 'weight' in name and p.dim() >= 2 and p.size(0) >= 4:
                w = p.detach()[:min(p.size(0), 64), :min(p.size(1), 64)].float()
                norms = w.norm(dim=1, keepdim=True).clamp(min=1e-8)
                w = w / norms
                sim = (w @ w.t()).abs()
                mask = ~torch.eye(sim.size(0), dtype=torch.bool)
                if mask.any():
                    vals.append(float(1.0 - sim[mask].mean().clamp(0, 1)))
        return float(np.mean(vals)) if vals else 0.0

    def compute_sp(self, model: nn.Module) -> float:
        """Superposicion: correlacion inter-fila promedio (entrelazamiento de features)."""
        vals = []
        for name, p in model.named_parameters():
            if 'weight' in name and p.dim() >= 2 and p.size(0) >= 4:
                w = p.detach()[:min(p.size(0), 64)].float()
                w = w.reshape(w.size(0), -1)
                try:
                    corr = torch.corrcoef(w).nan_to_num(0.0).abs()
                    mask = ~torch.eye(corr.size(0), dtype=torch.bool)
                    if mask.any():
                        vals.append(float(corr[mask].mean()))
                except Exception:
                    pass
        return float(np.mean(vals)) if vals else 0.0

    def classify_phase(self, delta: float, kappa: float,
                        berry: float) -> str:
        """
        Clasificacion de fase segun Book.md:

        discrete_crystal:       delta<0.05, kappa<1.5
        topological_insulator:  |berry|>pi/2, winding!=0
        cold_glass:             kappa>>1, delta>0.3
        functional_glass:       intermedio (lo mas comun en LM)
        """
        winding = round(berry / (2 * math.pi))
        if delta < 0.05 and kappa < 1.5:
            return 'discrete_crystal'
        if abs(berry) > math.pi / 2 and abs(winding) >= 1:
            return 'topological_insulator'
        if kappa > 100 and delta > 0.3:
            return 'cold_glass'
        return 'functional_glass'

    def compute_all(self, model: nn.Module, lr: float,
                    dataloader=None, compute_kappa: bool = False) -> Dict[str, Any]:
        """
        Calcula todas las metricas.
        compute_kappa=True hace pasadas backward adicionales (caro, usar cada N epochs).
        """
        delta = self.compute_delta(model)
        alpha = self.compute_alpha(delta)
        t_eff = self.compute_t_eff(lr)
        berry = self.compute_berry_phase(model)
        winding = round(berry / (2 * math.pi))
        lc = self.compute_lc(model)
        sp = self.compute_sp(model)
        kappa = (
            self.compute_kappa(model, dataloader)
            if compute_kappa and dataloader is not None
            else float('inf')
        )
        phase = self.classify_phase(delta, kappa, berry)
        return {
            'delta': delta, 'alpha': alpha, 't_eff': t_eff, 'kappa': kappa,
            'berry_phase': berry, 'winding_number': winding,
            'lc': lc, 'sp': sp, 'phase': phase,
        }

    def format_log(self, m: Dict[str, Any]) -> str:
        inf = float('inf')
        kappa = m.get('kappa', 0.0)
        kappa_str = f"{kappa:.2f}" if kappa < inf else "inf"
        return (
            f"delta={m.get('delta', 0.0):.4f} alpha={m.get('alpha', 0.0):.2f} "
            f"T_eff={m.get('t_eff', 0.0):.2e} kappa={kappa_str} "
            f"berry={m.get('berry_phase', 0.0):.2f} "
            f"wind={m.get('winding_number', 0)} "
            f"lc={m.get('lc', 0.0):.3f} sp={m.get('sp', 0.0):.3f} "
            f"[{m.get('phase', 'unknown').upper()}]"
        )


# ============================================================================
# FASE 0: Optimizacion del ratio de kernels espectrales (GOE-GUE)
# ============================================================================

class Phase0_KernelOptimizer:
    """
    Encuentra el ratio imaginario/real optimo para los kernels espectrales.

    Analogia con main.py: evalua la transicion GOE→GUE en el espacio
    de kernels. Un ratio optimo promueve estructura topologica (insulador)
    vs estructura amorfa (vidrio).

    Metodo: calibra con un mini-batch y mide la varianza del gradiente
    en funcion del ratio. Ratios que minimizan la varianza de gradiente
    (maxima coherencia espectral) son preferibles.

    No entrena: solo inicializa los kernels con distintos ratios y mide.
    Tiempo tipico: < 30 segundos.
    """

    RATIOS_TO_TEST = [0.05, 0.10, 0.18, 0.30, 0.50]  # del config original

    def __init__(self, config: 'TopoGPT2Config', logger: logging.Logger):
        self.config = config
        self.logger = logger

    def _measure_ratio(self, ratio: float, sample_batch: Tuple[torch.Tensor, torch.Tensor]) -> float:
        """
        Mide la coherencia espectral para un ratio dado.
        Retorna: varianza del gradiente (menor = mas coherente = mejor).
        """
        # Modelo temporal con ese ratio
        tmp_cfg = TopoGPT2Config.__new__(TopoGPT2Config)
        tmp_cfg.__dict__.update(self.config.__dict__)
        tmp_cfg.SPECTRAL_KERNEL_INIT_SCALE = ratio
        model = TopoGPT2(tmp_cfg).to(self.config.DEVICE)

        bx, by = sample_batch
        bx, by = bx.to(self.config.DEVICE), by.to(self.config.DEVICE)

        model.zero_grad()
        logits, _, _ = model(bx)
        loss = F.cross_entropy(logits.view(-1, self.config.VOCAB_SIZE), by.view(-1))
        loss.backward()

        grads = []
        for p in model.parameters():
            if p.grad is not None:
                grads.append(p.grad.detach().flatten()[:200].float())
        if not grads:
            return float('inf')
        G = torch.cat(grads)
        # Menor varianza = gradientes mas isotropos = mejor coherencia
        return float(G.var().item())

    def optimize(self, dataloader) -> float:
        """Retorna el mejor ratio de inicializacion de kernels espectrales."""
        self.logger.info("Fase 0: optimizando ratio de kernels espectrales...")
        try:
            sample_batch = next(iter(dataloader))
        except StopIteration:
            self.logger.warning("Fase 0: dataloader vacio, usando ratio default 0.02")
            return 0.02

        results = {}
        for ratio in self.RATIOS_TO_TEST:
            score = self._measure_ratio(ratio, sample_batch)
            results[ratio] = score
            self.logger.info(f"  ratio={ratio:.2f} -> grad_var={score:.4e}")

        best_ratio = min(results, key=results.get)
        self.logger.info(f"Fase 0: mejor ratio = {best_ratio} (grad_var={results[best_ratio]:.4e})")
        return best_ratio


# ============================================================================
# FASE 1: Prospecting de batch size
# ============================================================================

class Phase1_BatchProspector:
    """
    Encuentra el batch size optimo testando candidatos con pocos pasos.

    De main.py: el batch size regula la temperatura del horno de cristalizacion.
    Batch sizes demasiado chicos -> ruido excesivo (vidrio frio).
    Batch sizes demasiado grandes -> sin presion annealing (amorfos).
    La ventana optima empirica de main.py: [24, 128] para Strassen.

    Para LM, testeamos candidatos midiendo:
    - delta (δ): velocidad de descenso en prospect_steps pasos
    - T_eff: temperatura efectiva del gradiente

    Tiempo tipico: < 2 minutos para 3 candidatos × 30 pasos.
    """

    def __init__(self, config: 'TopoGPT2Config', logger: logging.Logger):
        self.config = config
        self.logger = logger

    def prospect(self, candidates: List[int], train_dataset,
                 prospect_steps: int = 30) -> int:
        """Retorna el mejor batch size segun delta y T_eff."""
        self.logger.info(
            f"Fase 1: prospecting batch sizes {candidates} "
            f"({prospect_steps} pasos cada uno)...")
        device = self.config.DEVICE
        results = {}

        for bs in candidates:
            dl = torch.utils.data.DataLoader(
                train_dataset, batch_size=bs, shuffle=True, drop_last=True)
            model = TopoGPT2(self.config).to(device)
            optimizer = torch.optim.AdamW(
                model.parameters(), lr=self.config.LEARNING_RATE)
            metrics = MechanisticMetrics(self.config)

            model.train()
            delta_start = metrics.compute_delta(model)

            for step, (bx, by) in enumerate(dl):
                if step >= prospect_steps:
                    break
                bx, by = bx.to(device), by.to(device)
                optimizer.zero_grad()
                logits, rl, _ = model(bx)
                loss = (F.cross_entropy(logits.view(-1, self.config.VOCAB_SIZE),
                                        by.view(-1))
                        + self.config.AE_RECON_WEIGHT * rl)
                loss.backward()
                metrics.update_grad_buffer(model)
                torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
                optimizer.step()

            delta_end = metrics.compute_delta(model)
            t_eff = metrics.compute_t_eff(self.config.LEARNING_RATE)
            delta_velocity = (delta_end - delta_start) / max(prospect_steps, 1)

            results[bs] = {
                'delta_end': delta_end,
                'delta_velocity': delta_velocity,
                't_eff': t_eff,
            }
            self.logger.info(
                f"  bs={bs:4d}: delta={delta_end:.4f} "
                f"d_vel={delta_velocity:.2e} T_eff={t_eff:.2e}")

            del model, optimizer

        # Criterio: batch size con velocidad de delta mas negativa
        # (enfriamiento mas rapido). Desempate: T_eff mas bajo.
        best_bs = min(
            results,
            key=lambda b: (results[b]['delta_velocity'], results[b]['t_eff'])
        )
        self.logger.info(f"Fase 1: mejor batch size = {best_bs}")
        return best_bs


# ============================================================================
# FASE 2: Mineria de semillas (seed mining)
# ============================================================================

class Phase2_SeedMiner:
    """
    Encuentra semillas prometedoras midiendo la trayectoria de delta.

    De main.py: una semilla "buena" muestra delta descendente en los
    primeros N pasos (enfriamiento). Una semilla "mala" se estanca en
    el plateau vidrioso (~0.49).

    Criterio de seleccion:
    1. Semillas con delta_velocity < 0 (enfriando) AND kappa bajo.
    2. Si no hay, semillas solo enfriando.
    3. Fallback: semilla con menor delta final.

    Tiempo tipico: < 3 minutos para 5 semillas × 50 pasos.
    """

    def __init__(self, config: 'TopoGPT2Config', logger: logging.Logger):
        self.config = config
        self.logger = logger

    def mine(self, seed_start: int, n_seeds: int, train_dataset,
             prospect_steps: int = 50) -> int:
        """Retorna la semilla con la mejor trayectoria de delta."""
        self.logger.info(
            f"Fase 2: minando {n_seeds} semillas desde seed={seed_start} "
            f"({prospect_steps} pasos cada una)...")
        device = self.config.DEVICE
        dl = torch.utils.data.DataLoader(
            train_dataset, batch_size=self.config.BATCH_SIZE,
            shuffle=True, drop_last=True)
        results = {}

        for s in range(seed_start, seed_start + n_seeds):
            set_seed(s, device)
            model = TopoGPT2(self.config).to(device)
            optimizer = torch.optim.AdamW(
                model.parameters(), lr=self.config.LEARNING_RATE)
            mets = MechanisticMetrics(self.config)

            delta_start = mets.compute_delta(model)
            model.train()

            for step, (bx, by) in enumerate(dl):
                if step >= prospect_steps:
                    break
                bx, by = bx.to(device), by.to(device)
                optimizer.zero_grad()
                logits, rl, _ = model(bx)
                loss = (F.cross_entropy(logits.view(-1, self.config.VOCAB_SIZE),
                                        by.view(-1))
                        + self.config.AE_RECON_WEIGHT * rl)
                loss.backward()
                mets.update_grad_buffer(model)
                torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
                optimizer.step()

            delta_end = mets.compute_delta(model)
            t_eff = mets.compute_t_eff(self.config.LEARNING_RATE)
            delta_vel = (delta_end - delta_start) / max(prospect_steps, 1)
            is_cooling = delta_vel < 0

            results[s] = {
                'delta_end': delta_end, 'delta_velocity': delta_vel,
                't_eff': t_eff, 'is_cooling': is_cooling,
            }
            self.logger.info(
                f"  seed={s:4d}: delta={delta_end:.4f} "
                f"d_vel={delta_vel:.2e} cooling={is_cooling}")
            del model, optimizer

        # Ordenar: cooling primero, luego delta_velocity mas negativo
        cooling_seeds = {s: v for s, v in results.items() if v['is_cooling']}
        pool = cooling_seeds if cooling_seeds else results
        best_seed = min(pool, key=lambda s: (pool[s]['delta_velocity'], pool[s]['delta_end']))
        self.logger.info(f"Fase 2: mejor semilla = {best_seed}")
        return best_seed


# ============================================================================
# FASE 4: Refinamiento por Recocido Simulado (Simulated Annealing)
# ============================================================================

class Phase4_AnnealingRefiner:
    """
    Refinamiento post-entrenamiento mediante recocido simulado.

    De main.py: despues de que el modelo converge, una fase de annealing
    con criterio de aceptacion de Metropolis puede empujar los pesos
    hacia estados de menor energia libre (menor delta o mejor val_loss).

    Aceptacion de Metropolis:
        si Δloss < 0: siempre acepta (mejora)
        si Δloss >= 0: acepta con prob exp(-Δloss / T)

    La temperatura T decae exponencialmente: T(t) = T0 * cooling_rate^t

    Al rechazar: restaura el mejor estado conocido.
    Si se estanca: perturbacion termica (ruido gaussiano en pesos).

    Tiempo: proporcional a refine_epochs (user-controlled).
    """

    def __init__(self, trainer: 'TopoGPT2Trainer',
                 t0: float = 0.5, cooling_rate: float = 0.95,
                 stagnation_patience: int = 5):
        self.trainer = trainer
        self.t0 = t0
        self.cooling_rate = cooling_rate
        self.stagnation_patience = stagnation_patience
        self.logger = trainer.logger

    def refine(self, train_dl, val_dl, refine_epochs: int) -> Dict:
        """
        Ejecuta refine_epochs epocas de recocido simulado.
        Retorna el historial de refinamiento.
        """
        cfg = self.trainer.config
        device = cfg.DEVICE
        model = self.trainer.model
        optimizer = self.trainer.optimizer
        metrics = MechanisticMetrics(cfg)

        T = self.t0
        best_val_loss = self.trainer.best_val_loss
        best_state = {k: v.clone() for k, v in model.state_dict().items()}
        prev_val_loss = best_val_loss
        stagnation_count = 0
        refine_history: List[Dict] = []

        self.logger.info("=" * 70)
        self.logger.info(f"Fase 4: recocido simulado ({refine_epochs} epocas)")
        self.logger.info(f"  T0={self.t0} cooling={self.cooling_rate} "
                         f"best_val={best_val_loss:.4f}")
        self.logger.info("=" * 70)

        for epoch_idx in range(1, refine_epochs + 1):
            epoch_abs = self.trainer.completed_epochs + 1

            # Guardar estado pre-epoch para posible rechazo
            prev_state = {k: v.clone() for k, v in model.state_dict().items()}

            # Entrenamiento de una epoch
            model.train()
            ep_loss, n = 0.0, 0
            optimizer.zero_grad()
            for step, (bx, by) in enumerate(train_dl):
                bx, by = bx.to(device), by.to(device)
                with torch.amp.autocast(
                        device_type=device.split(':')[0],
                        dtype=self.trainer.amp_dtype,
                        enabled=cfg.USE_AMP):
                    logits, rl, _ = model(bx)
                    loss = (
                        F.cross_entropy(logits.view(-1, cfg.VOCAB_SIZE), by.view(-1))
                        + cfg.AE_RECON_WEIGHT * rl
                    ) / cfg.GRAD_ACCUM_STEPS
                self.trainer.scaler.scale(loss).backward()
                metrics.update_grad_buffer(model)
                if (step + 1) % cfg.GRAD_ACCUM_STEPS == 0:
                    self.trainer.scaler.unscale_(optimizer)
                    torch.nn.utils.clip_grad_norm_(model.parameters(), cfg.GRADIENT_CLIP_NORM)
                    self.trainer.scaler.step(optimizer)
                    self.trainer.scaler.update()
                    optimizer.zero_grad()
                ep_loss += loss.item() * cfg.GRAD_ACCUM_STEPS
                n += 1

            val_loss, ppl = self.trainer.evaluate(val_dl)
            delta = metrics.compute_delta(model)
            t_eff = metrics.compute_t_eff(cfg.LEARNING_RATE)

            # Criterio de Metropolis: acepta o rechaza la epoch
            delta_loss = val_loss - prev_val_loss
            if delta_loss < 0:
                accept = True
            else:
                prob = math.exp(-delta_loss / max(T, 1e-12))
                accept = (torch.rand(1).item() < prob)

            if accept:
                prev_val_loss = val_loss
                if val_loss < best_val_loss:
                    best_val_loss = val_loss
                    best_state = {k: v.clone() for k, v in model.state_dict().items()}
                    self.trainer.best_val_loss = best_val_loss
                stagnation_count = 0
            else:
                # Rechazar: volver al estado anterior
                model.load_state_dict(prev_state)
                stagnation_count += 1
                self.logger.info(
                    f"  [Annealing] Epoch rechazada (Δloss={delta_loss:.4f}, T={T:.4f})")

            # Estancamiento: perturbacion termica
            if stagnation_count >= self.stagnation_patience:
                self.logger.info("  [Annealing] Estancamiento: perturbacion termica")
                model.load_state_dict(best_state)
                with torch.no_grad():
                    for p in model.parameters():
                        p.add_(torch.randn_like(p) * T * 1e-3)
                stagnation_count = 0

            # Enfriar temperatura
            T *= self.cooling_rate

            # Actualizar estado del trainer
            self.trainer.completed_epochs += 1
            self.trainer.history['train_loss'].append(ep_loss / max(n, 1))
            self.trainer.history['val_loss'].append(val_loss)
            self.trainer.history['perplexity'].append(ppl)
            self.trainer.history['recon_loss'].append(0.0)

            rec = {
                'epoch': epoch_abs, 'val_loss': val_loss, 'ppl': ppl,
                'delta': delta, 't_eff': t_eff, 'T_anneal': T,
                'accepted': accept,
            }
            refine_history.append(rec)

            self.logger.info(
                f"[Annealing {epoch_idx:3d}] "
                f"val={val_loss:.4f} ppl={ppl:.2f} delta={delta:.4f} "
                f"T={T:.4f} accept={accept}"
            )

            # Checkpoint
            self.trainer.ckpt_mgr.save(
                model, optimizer,
                self.trainer._current_state(),
                is_best=(val_loss < best_val_loss + 1e-8),
            )

        # Restaurar mejor modelo encontrado
        model.load_state_dict(best_state)
        self.logger.info(
            f"Fase 4 completa. Mejor val_loss = {best_val_loss:.4f}")
        return {'refine_history': refine_history, 'best_val_loss': best_val_loss}


# ============================================================================
# PIPELINE V2: Curriculum + Progressive Sequence Length
# ============================================================================

class TopoPhasePipelineV2:
    """Pipeline with curriculum learning and progressive sequence length.

    Replaces TopoPhasePipeline when --curriculum or --progressive-seq-len is set.
    Handles:
    - Text quality filtering before tokenization (via TextFilter)
    - Curriculum tiers (short/medium/all files)
    - Progressive MAX_SEQ_LEN across phases: 128->256->512
    - Tokens cached in memory for fast DataLoader rebuilding per phase
    """

    def __init__(self, config: 'TopoGPT2Config',
                 train_tokens: np.ndarray, val_tokens: np.ndarray,
                 tokenizer: 'BPETokenizer', logger: logging.Logger,
                 curriculum_tiers: Optional[Dict[int, List[int]]] = None,
                 progressive_seq: bool = True):
        self.config = config
        self.train_tokens = train_tokens
        self.val_tokens = val_tokens
        self.tokenizer = tokenizer
        self.logger = logger
        self.curriculum_tiers = curriculum_tiers
        self.progressive_seq = progressive_seq

    def _build_dataloader(self, tokens: np.ndarray, seq_len: int,
                           batch_size: int, shuffle: bool,
                           tag: str = '') -> torch.utils.data.DataLoader:
        n_cpu = max(1, os.cpu_count() // 2)
        pin = 'cuda' in self.config.DEVICE
        ds = MappedTokenDataset(tokens, seq_len)
        dl = torch.utils.data.DataLoader(
            ds, batch_size=batch_size, shuffle=shuffle,
            num_workers=n_cpu, pin_memory=pin, drop_last=shuffle)
        self.logger.info(
            f"[{tag}] seq_len={seq_len} -> {len(ds):,} sequences, "
            f"bs={batch_size}, steps={len(dl)}")
        return dl

    def _build_phases(self) -> Tuple[Tuple[int, int], ...]:
        if self.progressive_seq:
            return tuple(zip(
                self.config.PROGRESSIVE_SEQ_STEPS,
                self.config.PROGRESSIVE_SEQ_EPOCHS,
            ))
        seq = self.config.MAX_SEQ_LEN
        return ((seq, self.config.EPOCHS),)

    def run(self, run_prospect: bool = False,
            refine_epochs: int = 0,
            resume: bool = False,
            prospect_steps: int = 50,
            probe_seeds: int = 3,
            seed_start: int = 1) -> 'CurriculumTrainer':
        cfg = self.config
        logger = self.logger

        if run_prospect:
            logger.info(
                "Prospecting disabled in V2 pipeline (use standard pipeline for that).")

        set_seed(cfg.RANDOM_SEED, cfg.DEVICE)

        model = TopoGPT2(cfg)
        trainer = CurriculumTrainer(model, cfg, tokenizer=self.tokenizer)
        trainer.cache_tokens('train', self.train_tokens)
        trainer.cache_tokens('val', self.val_tokens)

        if resume:
            loaded = trainer.resume()
            if not loaded:
                logger.info("No checkpoint, starting from scratch.")

        phases = self._build_phases()
        logger.info(
            f"ProgressiveSeqLen={self.progressive_seq} phases={len(phases)} "
            f"curriculum={self.curriculum_tiers is not None}")

        for phase_idx, (seq_len, n_epochs) in enumerate(phases):
            logger.info(
                f"[Phase {phase_idx}] seq_len={seq_len}, epochs={n_epochs}")
            cfg.MAX_SEQ_LEN = seq_len

            if self.curriculum_tiers is not None:
                short = cfg.CURRICULUM_SHORT_LINES
                med = cfg.CURRICULUM_MED_LINES
                tier_map = {
                    0: (0, short),
                    1: (short + 1, med),
                    2: (med + 1, 999_999_999),
                }
                tier_file_counts = {
                    t: len(files) for t, files in self.curriculum_tiers.items()
                }
                phase_tier = min(phase_idx, 2)
                logger.info(
                    f"[Phase {phase_idx}] Curriculum tier {phase_tier} "
                    f"({tier_file_counts.get(phase_tier,0):,} files), "
                    f"range: {tier_map[phase_tier]}")

            train_dl = self._build_dataloader(
                self.train_tokens, seq_len, cfg.BATCH_SIZE, True, 'train')
            val_dl = self._build_dataloader(
                self.val_tokens, seq_len, cfg.BATCH_SIZE * 2, False, 'val')

            prev_completed = trainer.completed_epochs

            if self.curriculum_tiers is not None:
                for epoch_in_phase in range(n_epochs):
                    cfg.EPOCHS = 1
                    trainer.train(train_dl, val_dl)
            else:
                cfg.EPOCHS = n_epochs
                trainer.train(train_dl, val_dl)

            logger.info(
                f"[Phase {phase_idx}] done. Epochs: {prev_completed} -> "
                f"{trainer.completed_epochs}")

        if refine_epochs > 0:
            refiner = Phase4_AnnealingRefiner(trainer._base)
            refiner.refine(train_dl, val_dl, refine_epochs)

        return trainer


# ============================================================================
# PIPELINE COMPLETO (5 FASES)
# ============================================================================

class TopoPhasePipeline:
    """
    Orquesta las 5 fases de entrenamiento segun main.py + Book.md.

    Fases:
      0  Kernel ratio optimization  (GOE-GUE spectral calibration)
      1  Batch size prospecting      (temperatura del horno de cristalizacion)
      2  Seed mining                 (seleccion de semilla enfriante)
      3  Full training               (entrenamiento principal con metricas)
      4  Annealing refinement        (recocido simulado post-entrenamiento)

    Las fases 0-2 son rapidas (prospecting). La fase 3 es el grueso.
    La fase 4 es opcional (--refine).

    Para no ser prohibitivo:
      --prospect         activa fases 0, 1, 2 antes del entrenamiento
      --refine-epochs N  activa fase 4 con N epocas de annealing
      Sin flags: solo fase 3 (comportamiento original, identico a antes)
    """

    def __init__(self, config: 'TopoGPT2Config',
                 train_dataset, val_dataset,
                 tokenizer: 'BPETokenizer',
                 logger: logging.Logger):
        self.config = config
        self.train_dataset = train_dataset
        self.val_dataset = val_dataset
        self.tokenizer = tokenizer
        self.logger = logger

    def _make_dataloaders(self, batch_size: int = 0):
        bs = batch_size or self.config.BATCH_SIZE
        n_cpu = min(4, os.cpu_count() or 1)
        pin = 'cuda' in self.config.DEVICE
        train_dl = torch.utils.data.DataLoader(
            self.train_dataset, batch_size=bs, shuffle=True,
            num_workers=n_cpu, pin_memory=pin, drop_last=True)
        val_dl = torch.utils.data.DataLoader(
            self.val_dataset, batch_size=bs * 2, shuffle=False,
            num_workers=max(1, n_cpu // 2), pin_memory=pin, drop_last=True)
        return train_dl, val_dl

    def run(self, run_prospect: bool = False,
            refine_epochs: int = 0,
            resume: bool = False,
            prospect_steps: int = 50,
            probe_seeds: int = 3,
            seed_start: int = 1) -> 'TopoGPT2Trainer':
        """
        Ejecuta el pipeline completo.
        Retorna el trainer con el modelo entrenado.
        """
        cfg = self.config

        # ---- Fase 0: ratio de kernels espectrales ----
        if run_prospect:
            dl0, _ = self._make_dataloaders()
            p0 = Phase0_KernelOptimizer(cfg, self.logger)
            best_ratio = p0.optimize(dl0)
            cfg.SPECTRAL_KERNEL_INIT_SCALE = best_ratio
            self.logger.info(f"Fase 0 -> SPECTRAL_KERNEL_INIT_SCALE={best_ratio}")

        # ---- Fase 1: batch size ----
        if run_prospect:
            candidates = [
                max(2, cfg.BATCH_SIZE // 2),
                cfg.BATCH_SIZE,
                min(cfg.BATCH_SIZE * 2, 32),
            ]
            candidates = sorted(set(candidates))
            p1 = Phase1_BatchProspector(cfg, self.logger)
            best_bs = p1.prospect(candidates, self.train_dataset, prospect_steps)
            cfg.BATCH_SIZE = best_bs

        # ---- Fase 2: seed mining ----
        if run_prospect:
            p2 = Phase2_SeedMiner(cfg, self.logger)
            best_seed = p2.mine(seed_start, probe_seeds,
                                self.train_dataset, prospect_steps)
            cfg.RANDOM_SEED = best_seed
            set_seed(best_seed, cfg.DEVICE)
            self.logger.info(f"Fases 0-2 completas. "
                             f"ratio={cfg.SPECTRAL_KERNEL_INIT_SCALE} "
                             f"bs={cfg.BATCH_SIZE} seed={best_seed}")
        else:
            set_seed(cfg.RANDOM_SEED, cfg.DEVICE)

        # ---- Fase 3: entrenamiento principal ----
        train_dl, val_dl = self._make_dataloaders()

        # Ajustar arquitectura GQA si el checkpoint usa una config distinta
        if resume:
            tmp_mgr = CheckpointManager(cfg, self.logger)
            tmp_mgr.patch_config_for_resume(cfg)

        model = TopoGPT2(cfg)
        trainer = TopoGPT2Trainer(model, cfg, tokenizer=self.tokenizer)

        if resume:
            loaded = trainer.resume()
            if not loaded:
                self.logger.info("No habia checkpoint, iniciando desde cero.")
        elif trainer.ckpt_mgr.has_checkpoint():
            self.logger.info(
                f"AVISO: existe checkpoint en '{cfg.CHECKPOINT_DIR}/latest/'. "
                "Usa --resume para continuarlo.")

        # Entrenamiento con metricas mecanisticas integradas
        trainer.train(train_dl, val_dl)

        # ---- Fase 4: recocido simulado (opcional) ----
        if refine_epochs > 0:
            refiner = Phase4_AnnealingRefiner(trainer)
            refiner.refine(train_dl, val_dl, refine_epochs)

        return trainer


# ============================================================================
# FUNCIÓN PRINCIPAL
# ============================================================================

def main():
    parser = argparse.ArgumentParser(description='TopoGPT2 - Topological Quaternion LM')
    parser.add_argument('--scale', default='small',
                        choices=['micro', 'small', 'medium', 'gpt2'],
                        help='Escala del modelo')
    parser.add_argument('--corpus', default='directory',
                        choices=['directory', 'file'],
                        help='Corpus mode: directory walks tree, file reads single file')
    parser.add_argument('--corpus-root', default='/home/grisun0/src_note',
                        help='Root directory for --corpus=directory')
    parser.add_argument('--corpus-file', default='', help='Text file path if --corpus=file')
    parser.add_argument('--corpus-min-chars', type=int, default=30,
                        help='Minimum chars per file for --corpus=directory')
    parser.add_argument('--max-train-tokens', type=int, default=0,
                        help='Max tokens to tokenize (0 = use config default: 500M)')
    parser.add_argument('--epochs', type=int, default=5)
    parser.add_argument('--batch-size', type=int, default=4)
    parser.add_argument('--seq-len', type=int, default=0,
                        help='Longitud de secuencia (0 = usar preset de escala)')
    parser.add_argument('--lr', type=float, default=3e-4)
    parser.add_argument('--device', default='cuda' if torch.cuda.is_available() else 'cpu')
    parser.add_argument('--no-grad-ckpt', action='store_true',
                        help='Desactivar gradient checkpointing (mas rapido, mas VRAM)')
    parser.add_argument('--generate', action='store_true', help='Generar texto tras entrenar')
    parser.add_argument('--prompt', default='Once upon a time', help='Prompt para generacion')
    parser.add_argument('--resume', action='store_true', help='Reanudar desde checkpoint')
    # Fases del pipeline (main.py)
    parser.add_argument('--prospect', action='store_true',
                        help='Activar fases 0-2: optimizar kernel ratio, batch size y seed '
                             'antes del entrenamiento principal (rapido, ~5-10 min)')
    parser.add_argument('--prospect-steps', type=int, default=50,
                        help='Pasos por candidato en las fases de prospecting (default: 50)')
    parser.add_argument('--probe-seeds', type=int, default=3,
                        help='Numero de semillas a evaluar en fase 2 (default: 3)')
    parser.add_argument('--seed-start', type=int, default=1,
                        help='Primera semilla a probar en fase 2 (default: 1)')
    parser.add_argument('--refine-epochs', type=int, default=0,
                        help='Epocas de recocido simulado (fase 4) tras el entrenamiento '
                             'principal (default: 0 = desactivado)')
    parser.add_argument('--progressive-seq-len', action='store_true',
                        help='Enable progressive sequence length warmup (128->256->512)')
    parser.add_argument('--curriculum', action='store_true',
                        help='Enable curriculum learning (short->medium->all files)')
    parser.add_argument('--spec-decode', action='store_true',
                        help='Enable speculative decoding for faster inference')
    parser.add_argument('--generate-synthetic', action='store_true',
                        help='Generate synthetic dataset instead of training')
    parser.add_argument('--synth-provider', type=str, default='groq',
                        choices=['groq', 'openrouter', 'ollama'],
                        help='LLM provider for synthetic data generation')
    parser.add_argument('--synth-model', type=str, default='granite4.1:3b',
                        help='Model for synthetic data generation')
    parser.add_argument('--synth-output', type=str, default='data/synthetic_dataset.jsonl',
                        help='Output path for synthetic dataset JSONL')
    parser.add_argument('--synth-manifest', type=str, default='data/synthetic_manifest.json',
                        help='Manifest path for synthetic dataset (resumable)')
    parser.add_argument('--synth-workers', type=int, default=4,
                        help='Parallel workers for synthetic generation')
    parser.add_argument('--synth-api-key', type=str, default='',
                        help='API key for LLM (or set GROQ_API_KEY env var)')
    parser.add_argument('--synth-max-files', type=int, default=0,
                        help='Max files to generate from (0 = all)')
    args = parser.parse_args()

    config = TopoGPT2Config(
        SCALE=args.scale,
        CORPUS=args.corpus,
        CORPUS_ROOT=args.corpus_root,
        CORPUS_FILE=args.corpus_file,
        CORPUS_MIN_FILE_CHARS=args.corpus_min_chars,
        EPOCHS=args.epochs,
        BATCH_SIZE=args.batch_size,
        LEARNING_RATE=args.lr,
        DEVICE=args.device,
        GRADIENT_CHECKPOINTING=not args.no_grad_ckpt,
    )
    if args.seq_len > 0:
        config.MAX_SEQ_LEN = args.seq_len
    if args.max_train_tokens > 0:
        config.MAX_TRAIN_TOKENS = args.max_train_tokens

    logger = setup_logger('TopoGPT2.main', config.LOG_LEVEL)

    # Tokenizador
    logger.info("Cargando tokenizador GPT-2 (tiktoken)...")
    tokenizer = BPETokenizer('gpt2')
    config.VOCAB_SIZE = tokenizer.vocab_size

    # Corpus
    if config.CORPUS == 'file':
        if not config.CORPUS_FILE or not os.path.exists(config.CORPUS_FILE):
            logger.error(f"File not found: {config.CORPUS_FILE}")
            sys.exit(1)
        with open(config.CORPUS_FILE, 'r', encoding='utf-8', errors='replace') as f:
            full_text = f.read()
        train_split = int(len(full_text) * 0.95)
        train_tokens = _tokenize_text_to_memmap(
            full_text[:train_split], tokenizer,
            os.path.join(config.DATA_DIR, 'tokens_train.bin'),
            config.MAX_TRAIN_TOKENS)
        val_tokens = _tokenize_text_to_memmap(
            full_text[train_split:], tokenizer,
            os.path.join(config.DATA_DIR, 'tokens_val.bin'),
            config.MAX_TRAIN_TOKENS // 10)
    elif config.CORPUS == 'directory':
        manifest = FileManifest(config.CORPUS_ROOT, config.DATA_DIR, logger)
        all_paths = manifest.scan()
        if not all_paths:
            logger.error(f"No text files found in {config.CORPUS_ROOT}")
            sys.exit(1)
        logger.info(f"Total files found: {len(all_paths):,}")

        text_filter = TextFilter(config, logger)
        filtered_paths = []
        for p in all_paths:
            if text_filter.filter_file(p, tokenizer) is not None:
                filtered_paths.append(p)
        filter_stats = text_filter.report()
        logger.info(f"Files after quality filter: {len(filtered_paths):,}")

        if not filtered_paths:
            logger.error("All files filtered out. Check FILTER_* settings.")
            sys.exit(1)

        rng = np.random.RandomState(config.RANDOM_SEED)
        rng.shuffle(filtered_paths)
        split = int(len(filtered_paths) * 0.95)
        train_paths = filtered_paths[:split]
        val_paths = filtered_paths[split:]
        logger.info(
            f"Train files: {len(train_paths):,}  Val files: {len(val_paths):,}")

        memtok = MemmapTokenizer(config.DATA_DIR, logger)
        train_max = config.MAX_TRAIN_TOKENS
        val_max = config.MAX_TRAIN_TOKENS // 10 if train_max > 0 else 10_000_000
        train_tokens = memtok.tokenize(
            train_paths, tokenizer, 'train',
            train_max, config.CORPUS_MIN_FILE_CHARS)
        val_tokens = memtok.tokenize(
            val_paths, tokenizer, 'val',
            val_max, config.CORPUS_MIN_FILE_CHARS)
        logger.info(
            f"Train tokens: {len(train_tokens):,}  Val tokens: {len(val_tokens):,}")

        curriculum_tiers = None
        if args.curriculum and config.CURRICULUM_ENABLED:
            logger.info("Building curriculum tiers...")
            curriculum_tiers = build_file_tiers(
                train_paths,
                config.CURRICULUM_SHORT_LINES,
                config.CURRICULUM_MED_LINES,
            )
            logger.info(
                f"Tier 0 (short): {len(curriculum_tiers.get(0,[])):,} files, "
                f"Tier 1 (med): {len(curriculum_tiers.get(1,[])):,} files, "
                f"Tier 2 (all): {len(curriculum_tiers.get(2,[])):,} files")
    else:
        logger.error(f"Unknown corpus mode: {config.CORPUS}")
        sys.exit(1)

    if args.generate_synthetic:
        logger.info("Entering synthetic dataset generation mode...")
        synth_paths = train_paths + val_paths
        logger.info(f"Total files for synthetic generation: {len(synth_paths):,}")

        import synthetic_dataset as synth_mod

        api_key = args.synth_api_key or os.environ.get(
            "GROQ_API_KEY", os.environ.get("OPENROUTER_API_KEY", ""))
        if not api_key:
            logger.error("No API key. Set GROQ_API_KEY or OPENROUTER_API_KEY env var.")
            sys.exit(1)

        backend = synth_mod.build_backend(
            args.synth_provider, args.synth_model)
        logger.info(f"Synthetic backend: {backend.name()}")

        gen = synth_mod.SyntheticDatasetGenerator(
            backend=backend,
            output_path=args.synth_output,
            manifest_path=args.synth_manifest,
            logger=logger,
            max_workers=args.synth_workers,
        )
        max_files = args.synth_max_files if args.synth_max_files > 0 else len(synth_paths)
        logger.info(f"Processing up to {max_files:,} files with {args.synth_workers} workers...")

        for i in range(0, min(len(synth_paths), max_files), 100):
            batch = synth_paths[i:i+100]
            results = gen.process_batch(batch)
            logger.info(
                f"Batch {i//100+1}: processed={results['processed']} "
                f"skipped={results['skipped']} failed={results['failed']}")

        stats = gen.finish()
        logger.info(
            f"Synthetic generation complete: {stats['total_samples']:,} samples "
            f"written to {stats['output_path']}")
        sys.exit(0)

    train_ds = MappedTokenDataset(train_tokens, config.MAX_SEQ_LEN)
    val_ds = MappedTokenDataset(val_tokens, config.MAX_SEQ_LEN)
    logger.info(
        f"Train sequences: {len(train_ds):,}  Val sequences: {len(val_ds):,}")

    # Pipeline de 5 fases
    pipeline = TopoPhasePipeline(config, train_ds, val_ds, tokenizer, logger)

    use_progressive = args.progressive_seq_len and config.PROGRESSIVE_SEQ
    use_curriculum = args.curriculum and config.CURRICULUM_ENABLED

    if use_progressive or use_curriculum:
        pipeline = TopoPhasePipelineV2(
            config, train_tokens, val_tokens, tokenizer, logger,
            curriculum_tiers=curriculum_tiers if use_curriculum else None,
            progressive_seq=use_progressive,
        )
        trainer = pipeline.run(
            run_prospect=args.prospect,
            refine_epochs=args.refine_epochs,
            resume=args.resume,
            prospect_steps=args.prospect_steps,
            probe_seeds=args.probe_seeds,
            seed_start=args.seed_start,
        )
    else:
        trainer = pipeline.run(
            run_prospect=args.prospect,
            refine_epochs=args.refine_epochs,
            resume=args.resume,
            prospect_steps=args.prospect_steps,
            probe_seeds=args.probe_seeds,
            seed_start=args.seed_start,
        )

    # Historial final en results/ para inspeccion rapida
    results_dir = 'results_topogpt2'
    os.makedirs(results_dir, exist_ok=True)
    hist_path = os.path.join(results_dir, 'history.json')
    with open(hist_path, 'w', encoding='utf-8') as f:
        json.dump(trainer._current_state(), f, indent=2)
    logger.info(f"Estado completo guardado: {hist_path}")

    # Generacion de muestra
    if args.generate:
        logger.info(f"Generando desde prompt: '{args.prompt}'")
        trainer.model.eval()
        prompt_tokens = tokenizer.encode(args.prompt)
        ids = torch.tensor([prompt_tokens], dtype=torch.long, device=config.DEVICE)
        gen_ids = trainer.model.generate(ids, max_new_tokens=200, temperature=0.8, top_k=50)
        logger.info(f"Generado:\n{tokenizer.decode(gen_ids[0].tolist())}")


if __name__ == '__main__':
    main()