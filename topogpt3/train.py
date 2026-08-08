#!/usr/bin/env python3
"""
TopoGPT3: Grassmannian / Berry-Holonomy extension of TopoGPT2

Author: Gris Iscomeback
License: GPL v3

Lo nuevo respecto a model.py
---------------------------------
1. Espacio base: Grassmanniana Gr(r, N) sobre el tensor de kernels espectrales
   K(theta) en C^{N_f x N_c}. El estado geometrico vive en U_r(theta) en St(r,N)/U(r),
   con r elegido dinamicamente por el "elbow" del espectro singular de K.
2. Fisher gap funcional:    Delta_F(theta) = lambda_r(Sigma_F) - lambda_{r+1}(Sigma_F)
   estimado por covarianza empirica de gradientes (mini-batch) o por scores.
3. Conexion de Berry discreta:  A_n = i * U_n^dagger (U_{n+1} - U_n)
   y holonomia acumulada      U_Gamma = P prod_n exp(-i A_n)  en U(r).
4. Distancia de conjugacion en SU(2) (cuaternionico, r=1 efectivo):
       d_conj(U1, U2) = min_{g in SU(2)} || U1 - g U2 g^{-1} ||_F
5. Winding W como proxy heuristico barato (rol secundario).
6. Curriculum por dataset, de mas simple a mas dificil:
       Tier 1: CodeAlpaca               (instrucciones cortas)
       Tier 2: Code-Feedback-Filtered   (chat / explicacion paso a paso)
       Tier 3: Magicoder-Evol-Instruct-110K (problemas complejos)
       Tier 4: Tiny-The-Stack           (codigo real multilenguaje)
   Cada tier mantiene splits train / val / holdout *disjuntos*.
   El conjunto HOLDOUT nunca se ve durante entrenamiento; se usa
   solo para medir generalizacion verdadera al final de cada tier
   y al final del pipeline.

Diseno
------
- Reutiliza la arquitectura TopoGPT2 (tokenizador BPE, modelo cuaternionico
  con torus + spectral autoencoder) cargandola dinamicamente desde model.py.
- Anade encima la maquinaria geometrica nueva en GrassmannianTracker.
- Entrenamiento orquestado por TopoGPT3Trainer que itera 4 tiers en orden,
  con seq_len progresivo y evaluacion en holdout disjunto.

CLI
---
    python train.py --prepare-data            descarga + tokeniza los 4 tiers
    python train.py --train                   entrena el curriculum completo
    python train.py --train --start-tier 2    arranca desde un tier concreto
    python train.py --eval-holdout            evalua sobre holdouts disjuntos
    python train.py --resume                  reanuda desde el ultimo checkpoint
"""

from __future__ import annotations

import argparse
import json
import logging
import math
import os
import sys
import time
from collections import deque
from dataclasses import asdict, dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

from .model import (
    BPETokenizer,
    QuaternionSpectralLayer,
    SpectralAutoencoder,
    TopoGPT2,
    TopoGPT2Config,
    set_seed,
    setup_logger,
)


# ============================================================================
# CONFIGURACION
# ============================================================================

@dataclass
class TopoGPT3Config:
    """Configuracion del pipeline TopoGPT3 (Grassmanniana + curriculum)."""

    # --- Modelo: hereda TopoGPT2 ---
    SCALE: str = "small"            # micro | small | medium | gpt2
    DEVICE: str = "cuda" if torch.cuda.is_available() else "cpu"
    RANDOM_SEED: int = 42
    USE_AMP: bool = True
    GRADIENT_CHECKPOINTING: bool = True

    # --- Hyperparams de entrenamiento ---
    BATCH_SIZE: int = 4
    GRAD_ACCUM_STEPS: int = 8
    LEARNING_RATE: float = 3e-4
    WEIGHT_DECAY: float = 0.1
    GRADIENT_CLIP_NORM: float = 1.0
    WARMUP_RATIO: float = 0.05

    # --- Curriculum (tiers x epocas) ---
    TIER_EPOCHS: Tuple[int, int, int, int] = (2, 2, 3, 3)
    TIER_SEQ_LEN: Tuple[int, int, int, int] = (128, 192, 256, 256)
    TIER_NAMES: Tuple[str, str, str, str] = (
        "codealpaca",
        "code_feedback",
        "magicoder_evol",
        "tiny_the_stack",
    )

    # --- Datasets (HuggingFace IDs) ---
    HF_CODEALPACA: str = "sahil2801/CodeAlpaca-20k"
    HF_CODE_FEEDBACK: str = "m-a-p/CodeFeedback-Filtered-Instruction"
    HF_MAGICODER: str = "ise-uiuc/Magicoder-Evol-Instruct-110K"
    HF_TINY_STACK: str = "bigcode/the-stack-smol"
    # Cadena de fallbacks publicos (sin autenticacion HF) si bigcode/the-stack-smol
    # esta gated. Se prueban en orden hasta que uno funcione.
    HF_TINY_STACK_FALLBACKS: Tuple[str, ...] = (
        "codeparrot/codeparrot-clean-valid",
        "flytech/python-codes-25k",
        "iamtarun/python_code_instructions_18k_alpaca",
    )

    # --- Splits ---
    VAL_FRACTION: float = 0.05         # validacion durante entrenamiento
    HOLDOUT_FRACTION: float = 0.05     # NUNCA visto, medicion de generalizacion
    SPLIT_SEED: int = 1337             # determinismo del split por dataset

    # --- Tokens por tier (limites de seguridad) ---
    MAX_TOKENS_PER_TIER: Tuple[int, int, int, int] = (
        20_000_000,    # CodeAlpaca chico
        80_000_000,    # CodeFeedback medio
        100_000_000,   # Magicoder
        500_000_000,   # Tiny-The-Stack ~1GB
    )

    # --- Grassmanniana ---
    GRASS_TRACK_EVERY: int = 200       # steps entre snapshots de U_r
    GRASS_MAX_RANK: int = 16           # tope para r (elbow se calcula <=)
    GRASS_ELBOW_RATIO: float = 0.05    # corte relativo del elbow
    GRASS_FISHER_BATCHES: int = 40     # batches para estimar Sigma_F (>= r_max+2)
    GRASS_FISHER_GRADS: int = 64       # gradientes muestrales para Sigma_F

    # --- Optimizacion: Gauss para multiplicacion compleja (3 mults en vez de 4) ---
    USE_GAUSS_COMPLEX_MULT: bool = True

    # --- Mediciones de eficiencia ---
    EFFICIENCY_THROUGHPUT_BATCHES: int = 20   # batches para cronometrar tok/s
    # Factor heuristico para activaciones por token (multiplo de D_MODEL guardado en memoria);
    # 12 corresponde a Q,K,V,attn-out + 2 FFN + residuales por capa.
    GRADIENT_CHECKPOINTING_FACTOR: int = 12

    # --- Progressive Window Sizes (Sliding Window Attention) ---
    PROGRESSIVE_WINDOW: Tuple[int, int, int, int] = (64, 96, 128, 128)

    # --- Paths ---
    DATA_CACHE: str = "data_topogpt3"
    CHECKPOINT_DIR: str = "checkpoints_topogpt3"
    LOG_FILE: str = "topogpt3_history.jsonl"

    # --- Logging / checkpoint ---
    LOG_INTERVAL_STEPS: int = 50
    CHECKPOINT_EVERY_MIN: int = 15
    MAX_CHECKPOINTS: int = 5

    # --- Limites de seguridad ---
    MAX_TRAIN_BATCHES_PER_EPOCH: int = 0   # 0 = sin limite
    MAX_EVAL_BATCHES: int = 200            # cap a evaluacion para no saturar

    def build_topogpt2_config(self, max_seq_len: int,
                              attn_window: Optional[int] = None) -> TopoGPT2Config:
        cfg = TopoGPT2Config(
            DEVICE=self.DEVICE,
            RANDOM_SEED=self.RANDOM_SEED,
            USE_AMP=self.USE_AMP,
            SCALE=self.SCALE,
            BATCH_SIZE=self.BATCH_SIZE,
            GRAD_ACCUM_STEPS=self.GRAD_ACCUM_STEPS,
            LEARNING_RATE=self.LEARNING_RATE,
            WEIGHT_DECAY=self.WEIGHT_DECAY,
            GRADIENT_CLIP_NORM=self.GRADIENT_CLIP_NORM,
            WARMUP_RATIO=self.WARMUP_RATIO,
            GRADIENT_CHECKPOINTING=self.GRADIENT_CHECKPOINTING,
            CHECKPOINT_DIR=self.CHECKPOINT_DIR,
            DATA_DIR=self.DATA_CACHE,
        )
        cfg.MAX_SEQ_LEN = max_seq_len
        if attn_window is not None and attn_window > 0:
            cfg.ATTN_WINDOW = attn_window
        return cfg


# ============================================================================
# GRASSMANNIAN TRACKER
# ============================================================================

class GrassmannianTracker:
    """
    Observables geometricos sobre la trayectoria SGD.

    En cada snapshot:
      - Apila los kernels espectrales (kr_*, ki_*) del modelo en
        K(theta) en C^{N_f x N_c}.
      - SVD truncada -> U_r(theta) en St(r,N).
      - Rango r dinamico por elbow de los valores singulares.
      - Gap funcional Delta_F estimado por covarianza de gradientes
        muestrales (proxy de la matriz de Fisher).
      - Conexion de Berry discreta entre snapshots consecutivos:
           A_n = i * U_n^dagger (U_{n+1} - U_n)
        Holonomia acumulada U_Gamma = P prod_n exp(-i A_n) en U(r).
      - Distancia de conjugacion en SU(2) (r=1 efectivo cuaternionico).
      - Winding W como proxy barato.

    Todos los calculos viven en CPU/float32 para no contaminar AMP.
    """

    def __init__(self, config: TopoGPT3Config, logger: logging.Logger):
        self.config = config
        self.logger = logger
        self.U_prev: Optional[torch.Tensor] = None
        self.U_holo: Optional[torch.Tensor] = None     # holonomia acumulada
        self.U_init: Optional[torch.Tensor] = None     # subespacio inicial
        self.winding_accum: float = 0.0
        self.history: List[Dict[str, Any]] = []

    # ------------------------------------------------------------------
    # Construccion del tensor de kernels K(theta)
    # ------------------------------------------------------------------

    @staticmethod
    def _stack_spectral_kernels(model: nn.Module) -> torch.Tensor:
        """
        Devuelve K(theta) en C^{N_f x N_c}:
          - filas = frecuencias planas (todos los modos espaciales de todos los kernels)
          - columnas = canales (in_q * out_q por componente cuaternionico, sumados)
        """
        rows: List[torch.Tensor] = []
        with torch.no_grad():
            for name, mod in model.named_modules():
                if isinstance(mod, QuaternionSpectralLayer):
                    in_q = mod.in_q
                    out_q = mod.out_q
                    for c in ("w", "x", "y", "z"):
                        kr = getattr(mod, f"kr_{c}").detach().cpu().float()
                        ki = getattr(mod, f"ki_{c}").detach().cpu().float()
                        K = torch.complex(kr, ki)            # [in_q, out_q, H, W']
                        K = K.permute(2, 3, 0, 1).contiguous()
                        H, Wp, Iq, Oq = K.shape
                        K = K.reshape(H * Wp, Iq * Oq)
                        rows.append(K)
        if not rows:
            return torch.zeros(1, 1, dtype=torch.complex64)
        max_cols = max(r.shape[1] for r in rows)
        padded = []
        for r in rows:
            if r.shape[1] < max_cols:
                pad = torch.zeros(
                    r.shape[0], max_cols - r.shape[1], dtype=r.dtype
                )
                r = torch.cat([r, pad], dim=1)
            padded.append(r)
        return torch.cat(padded, dim=0)

    # ------------------------------------------------------------------
    # SVD truncada + eleccion de rango por elbow
    # ------------------------------------------------------------------

    def _elbow_rank(self, sigmas: torch.Tensor) -> int:
        """Punto donde el valor singular cae por debajo de elbow_ratio * sigma_max."""
        s = sigmas.float()
        if s.numel() == 0:
            return 1
        cutoff = self.config.GRASS_ELBOW_RATIO * float(s[0])
        r = int((s > cutoff).sum().item())
        return max(1, min(r, self.config.GRASS_MAX_RANK))

    def _dominant_subspace(self, K: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor, int]:
        """
        SVD compacta y truncada.
        Devuelve (U_r, sigmas, r) con U_r en C^{N_f x r} ortonormal.
        """
        try:
            U, S, _Vh = torch.linalg.svd(K, full_matrices=False)
        except RuntimeError as exc:
            self.logger.warning(f"SVD fallida en K({tuple(K.shape)}): {exc}")
            return torch.eye(K.shape[0], 1, dtype=K.dtype), torch.tensor([1.0]), 1
        r = self._elbow_rank(S.abs())
        return U[:, :r].contiguous(), S[:r].abs(), r

    # ------------------------------------------------------------------
    # Fisher gap por covarianza de gradientes (proxy de Sigma_F)
    # ------------------------------------------------------------------

    @staticmethod
    def _flatten_grads(model: nn.Module, max_per_tensor: int = 256) -> Optional[torch.Tensor]:
        """Concatena un sub-sample de gradientes para mantener costo acotado."""
        parts: List[torch.Tensor] = []
        for p in model.parameters():
            if p.grad is None or not p.is_floating_point():
                continue
            g = p.grad.detach()
            if torch.isnan(g).any() or torch.isinf(g).any():
                continue
            flat = g.flatten().float().cpu()
            if flat.numel() > max_per_tensor:
                step = max(1, flat.numel() // max_per_tensor)
                flat = flat[::step][:max_per_tensor]
            parts.append(flat)
        if not parts:
            return None
        return torch.cat(parts)

    def estimate_fisher_gap(
        self,
        model: nn.Module,
        dataloader: Iterable,
        vocab_size: int,
        r_target: int,
    ) -> Tuple[float, torch.Tensor, int]:
        """
        Sigma_F ~= (1/M) sum_m g_m g_m^T  (covarianza muestral de gradientes).
        Delta_F = lambda_{r_eff} - lambda_{r_eff+1}, donde r_eff = min(r_target, M-2)
        para no salir del rango efectivo del estimador con M gradientes.
        Devuelve (gap, eigs_desc, r_eff).
        """
        device = next(model.parameters()).device
        was_training = model.training
        model.train()
        samples: List[torch.Tensor] = []
        n_batches = 0
        for batch in dataloader:
            if n_batches >= self.config.GRASS_FISHER_BATCHES:
                break
            if len(samples) >= self.config.GRASS_FISHER_GRADS:
                break
            bx, by = batch
            bx = bx.to(device, non_blocking=True)
            by = by.to(device, non_blocking=True)
            model.zero_grad(set_to_none=True)
            try:
                logits, _, _ = model(bx)
                loss = F.cross_entropy(
                    logits.view(-1, vocab_size), by.view(-1)
                )
                loss.backward()
            except RuntimeError as exc:
                self.logger.warning(f"Fisher backward fallido: {exc}")
                model.zero_grad(set_to_none=True)
                continue
            g = self._flatten_grads(model)
            if g is not None:
                samples.append(g)
            n_batches += 1
        model.zero_grad(set_to_none=True)
        if not was_training:
            model.eval()
        M = len(samples)
        if M < 3:
            empty = torch.zeros(1)
            return float("nan"), empty, 0
        D = min(s.numel() for s in samples)
        G = torch.stack([s[:D] for s in samples], dim=0)
        gram = (G @ G.t()) / max(G.shape[0] - 1, 1)
        try:
            eigs = torch.linalg.eigvalsh(gram).real.clamp(min=0)
        except RuntimeError:
            empty = torch.zeros(1)
            return float("nan"), empty, 0
        eigs, _ = torch.sort(eigs, descending=True)
        r_eff = max(1, min(r_target, M - 2))
        if r_eff >= eigs.numel():
            r_eff = max(1, eigs.numel() - 1)
        gap = float((eigs[r_eff - 1] - eigs[r_eff]).item())
        return gap, eigs, r_eff

    # ------------------------------------------------------------------
    # Berry connection y holonomia discreta
    # ------------------------------------------------------------------

    @staticmethod
    def _project_unitary(M: torch.Tensor) -> torch.Tensor:
        """Proyeccion a U(r) por descomposicion polar (M ~= U H -> retorna U)."""
        U_l, _S, Vh = torch.linalg.svd(M, full_matrices=False)
        return U_l @ Vh

    def update_holonomy(self, U_new: torch.Tensor) -> Optional[torch.Tensor]:
        """
        Holonomia discreta:
            T_n = U_n^dagger U_{n+1}  en C^{r x r}  (transporte paralelo discreto)
            U_Gamma <- T_n * U_Gamma  (acumulado)
        Tras cada paso, U_Gamma se proyecta a U(r) para evitar deriva numerica.
        """
        if self.U_prev is None:
            self.U_prev = U_new
            self.U_init = U_new
            self.U_holo = torch.eye(U_new.shape[1], dtype=U_new.dtype)
            return self.U_holo
        # Asegurar misma forma (kernel puede haber cambiado de tamano si r vario)
        r_min = min(self.U_prev.shape[1], U_new.shape[1])
        rows = min(self.U_prev.shape[0], U_new.shape[0])
        Up = self.U_prev[:rows, :r_min]
        Un = U_new[:rows, :r_min]
        T = Up.conj().transpose(0, 1) @ Un
        T = self._project_unitary(T)
        if self.U_holo is None or self.U_holo.shape != T.shape:
            self.U_holo = torch.eye(T.shape[0], dtype=T.dtype)
        self.U_holo = self._project_unitary(T @ self.U_holo)
        self.U_prev = U_new
        return self.U_holo

    @staticmethod
    def conjugation_distance_su2(U1: torch.Tensor, U2: torch.Tensor) -> float:
        """
        Para U1, U2 en U(1)/U(2):  d_conj(U1, U2) = min_g || U1 - g U2 g^{-1} ||_F.
        En U(1) coincide con |U1 - U2|.
        En SU(2) se reduce a comparar |Tr(U1)| con |Tr(U2)| (clase de conjugacion).
        """
        n = U1.shape[0]
        if n == 1:
            return float(torch.linalg.norm(U1 - U2).real.item())
        t1 = torch.trace(U1)
        t2 = torch.trace(U2)
        return float(abs(abs(t1) - abs(t2)).item())

    # ------------------------------------------------------------------
    # Winding heuristico
    # ------------------------------------------------------------------

    def _accumulate_winding(self, U_new: torch.Tensor) -> float:
        """W += (1/2pi) * arg det <U_prev | U_new>  acumulado sobre la trayectoria."""
        if self.U_prev is None:
            return self.winding_accum
        r_min = min(self.U_prev.shape[1], U_new.shape[1])
        rows = min(self.U_prev.shape[0], U_new.shape[0])
        overlap = self.U_prev[:rows, :r_min].conj().transpose(0, 1) @ U_new[:rows, :r_min]
        det = torch.linalg.det(overlap)
        phase = float(torch.atan2(det.imag, det.real).item())
        self.winding_accum += phase / (2 * math.pi)
        return self.winding_accum

    # ------------------------------------------------------------------
    # Snapshot completo
    # ------------------------------------------------------------------

    def snapshot(
        self,
        model: nn.Module,
        step: int,
        dataloader: Optional[Iterable] = None,
        vocab_size: Optional[int] = None,
    ) -> Dict[str, Any]:
        K = self._stack_spectral_kernels(model)
        U_r, sigmas, r = self._dominant_subspace(K)
        prev_U = self.U_prev
        winding = self._accumulate_winding(U_r)
        holo = self.update_holonomy(U_r)
        d_conj_init = (
            self.conjugation_distance_su2(self.U_init.conj().transpose(0, 1) @ self.U_init,
                                          U_r.conj().transpose(0, 1) @ U_r)
            if self.U_init is not None else 0.0
        )

        # Berry phase = arg det(U_Gamma)
        if holo is not None and holo.numel() > 0:
            det_holo = torch.linalg.det(holo)
            berry = float(torch.atan2(det_holo.imag, det_holo.real).item())
            holo_norm = float(torch.linalg.norm(holo).real.item())
        else:
            berry = 0.0
            holo_norm = 0.0

        delta_f = float("nan")
        r_eff_fisher = 0
        if dataloader is not None and vocab_size is not None:
            delta_f, eigs, r_eff_fisher = self.estimate_fisher_gap(
                model, dataloader, vocab_size, r
            )
            sigma_max = float(eigs[0].item()) if eigs.numel() > 0 else 0.0
            sigma_min = float(eigs[eigs > 1e-12].min().item()) if (eigs > 1e-12).any() else 0.0
            kappa_F = (sigma_max / sigma_min) if sigma_min > 0 else float("inf")
        else:
            kappa_F = float("inf")

        snap = {
            "step": step,
            "rank_r": int(r),
            "fisher_r_eff": int(r_eff_fisher),
            "sigma_max": float(sigmas[0].item()) if sigmas.numel() > 0 else 0.0,
            "sigma_min": float(sigmas[-1].item()) if sigmas.numel() > 0 else 0.0,
            "fisher_gap": delta_f,
            "fisher_kappa": kappa_F,
            "berry_phase": berry,
            "winding": winding,
            "holo_frobenius": holo_norm,
            "d_conj_to_init": d_conj_init,
        }
        self.history.append(snap)
        return snap

    def format_log(self, snap: Dict[str, Any]) -> str:
        df = snap.get("fisher_gap", float("nan"))
        r_eff = snap.get("fisher_r_eff", 0)
        if r_eff <= 0:
            df_str = "skip"
            r_str = "-"
        elif math.isfinite(df):
            df_str = f"{df:.3e}"
            r_str = str(r_eff)
        else:
            df_str = "nan"
            r_str = str(r_eff)
        return (
            f"r={snap['rank_r']:>2d} "
            f"sig=[{snap['sigma_max']:.3e},{snap['sigma_min']:.3e}] "
            f"Delta_F@r{r_str}={df_str} "
            f"berry={snap['berry_phase']:+.3f} "
            f"W={snap['winding']:+.3f} "
            f"||U_G||={snap['holo_frobenius']:.3f} "
            f"d_conj={snap['d_conj_to_init']:.3e}"
        )

    def save(self, path: str) -> None:
        with open(path, "w", encoding="utf-8") as f:
            for s in self.history:
                f.write(json.dumps(s) + "\n")


# ============================================================================
# GAUSS / KARATSUBA: 3 multiplicaciones reales por multiplicacion compleja
# ============================================================================

def _gauss_complex_contract(self, W: torch.Tensor, X: torch.Tensor) -> torch.Tensor:
    """Sustituye QuaternionSpectralLayer._contract usando el truco de Gauss.

    Para (Wr + i Wi)(Xr + i Xi) la version naive requiere 4 productos reales:
        Yr = Wr Xr - Wi Xi
        Yi = Wr Xi + Wi Xr
    Gauss (Karatsuba) baja a 3 productos reales:
        m1 = Wr * Xr
        m2 = Wi * Xi
        m3 = (Wr + Wi) * (Xr + Xi)
        Yr = m1 - m2
        Yi = m3 - m1 - m2

    Importante (AMP): el _contract original opera sobre complex64 y PyTorch no
    autocastea operaciones complejas; el resultado es complex64. Si dejamos que
    autocast convierta nuestros einsums reales a fp16, la dtype de salida cambia
    y rompe el scatter_add_ corriente abajo en QuaternionTorusBrain. Por eso
    desactivamos autocast aqui y forzamos fp32 para preservar la semantica.
    """
    device_type = W.device.type if W.device.type in ("cuda", "cpu") else "cpu"
    with torch.amp.autocast(device_type=device_type, enabled=False):
        Wr = W.real.float()
        Wi = W.imag.float()
        Xr = X.real.float()
        Xi = X.imag.float()
        m1 = torch.einsum("iohw,bihw->bohw", Wr, Xr)
        m2 = torch.einsum("iohw,bihw->bohw", Wi, Xi)
        m3 = torch.einsum("iohw,bihw->bohw", Wr + Wi, Xr + Xi)
        Yr = m1 - m2
        Yi = m3 - m1 - m2
        return torch.complex(Yr, Yi)


_GAUSS_PATCH_APPLIED = False


def apply_gauss_patch(logger: Optional[logging.Logger] = None) -> None:
    """Activa la version Gauss de _contract en QuaternionSpectralLayer.
    Idempotente: solo parchea una vez por proceso."""
    global _GAUSS_PATCH_APPLIED
    if _GAUSS_PATCH_APPLIED:
        return
    QuaternionSpectralLayer._contract_original = QuaternionSpectralLayer._contract  # type: ignore[attr-defined]
    QuaternionSpectralLayer._contract = _gauss_complex_contract  # type: ignore[assignment]
    _GAUSS_PATCH_APPLIED = True
    if logger is not None:
        logger.info("Gauss complex-mult patch aplicado: 3 productos reales por contraccion.")


# ============================================================================
# EFFICIENCY METRICS: performance / param, / FLOP, / bandwidth
# ============================================================================

class EfficiencyMetrics:
    """
    Mide y calcula los tres ratios pedidos:

      perf_per_param  =  (1 / val_ppl) / params_M
      perf_per_FLOP   =  tokens_per_sec / FLOPs_per_sec_aprox
      perf_per_BW     =  tokens_per_sec / bytes_moved_per_sec_aprox

    FLOPs estimados con la heuristica de Kaplan/Hoffmann:
        FLOPs_forward_per_token ~= 2 * N_no_embed
        FLOPs_total_per_token  ~= 6 * N_no_embed       (forward + backward)
    Bandwidth estimada como params_bytes leidos + activations_bytes movidas por step.
    tokens_per_sec se cronometra empiricamente sobre el dataloader.
    """

    def __init__(self, model: nn.Module, config: TopoGPT3Config,
                 logger: logging.Logger, gauss_enabled: bool):
        self.model = model
        self.config = config
        self.logger = logger
        self.gauss_enabled = gauss_enabled
        self.total_params = sum(p.numel() for p in model.parameters())
        self.embed_params = self._embed_params(model)
        self.non_embed_params = self.total_params - self.embed_params

    @staticmethod
    def _embed_params(model: nn.Module) -> int:
        n = 0
        for name, mod in model.named_modules():
            if isinstance(mod, nn.Embedding):
                n += sum(p.numel() for p in mod.parameters())
        return n

    @torch.no_grad()
    def measure_throughput(self, dataloader, vocab_size: int) -> Tuple[float, float]:
        """Devuelve (tokens_por_segundo, segundos_por_step)."""
        self.model.eval()
        device = self.config.DEVICE
        n_batches = self.config.EFFICIENCY_THROUGHPUT_BATCHES
        # Warmup
        warmup_done = False
        for bx, by in dataloader:
            bx = bx.to(device, non_blocking=True)
            self.model(bx)
            if "cuda" in device:
                torch.cuda.synchronize()
            warmup_done = True
            break
        if not warmup_done:
            return 0.0, 0.0
        total_tokens = 0
        t0 = time.time()
        seen = 0
        for bx, by in dataloader:
            if seen >= n_batches:
                break
            bx = bx.to(device, non_blocking=True)
            self.model(bx)
            total_tokens += int(bx.numel())
            seen += 1
        if "cuda" in device:
            torch.cuda.synchronize()
        dt = max(time.time() - t0, 1e-6)
        self.model.train()
        return total_tokens / dt, dt / max(seen, 1)

    def estimate_flops_per_step(self, batch_size: int, seq_len: int) -> int:
        """Heuristica: 6 * N_no_embed * tokens (forward + backward)."""
        tokens = batch_size * seq_len
        return int(6 * self.non_embed_params * tokens)

    def estimate_bytes_per_step(self, batch_size: int, seq_len: int,
                                 dtype_bytes: int = 2) -> int:
        """Bandwidth aproximada: lectura de pesos + activaciones por step.
        Asume AMP fp16 (2 bytes); pesos fp32 (4 bytes) leidos una vez."""
        weight_bytes = self.total_params * 4
        activation_bytes = batch_size * seq_len * self.config.GRADIENT_CHECKPOINTING_FACTOR * dtype_bytes
        return weight_bytes + activation_bytes

    def compute(self, dataloader, vocab_size: int, val_loss: float,
                val_ppl: float, val_acc: float, batch_size: int,
                seq_len: int) -> Dict[str, Any]:
        tok_per_sec, sec_per_step = self.measure_throughput(dataloader, vocab_size)
        flops_step = self.estimate_flops_per_step(batch_size, seq_len)
        bytes_step = self.estimate_bytes_per_step(batch_size, seq_len)
        flops_per_sec = flops_step / max(sec_per_step, 1e-9)
        bytes_per_sec = bytes_step / max(sec_per_step, 1e-9)

        params_M = self.total_params / 1e6
        perf_quality = (1.0 / max(val_ppl, 1e-6))

        return {
            "params_total": self.total_params,
            "params_non_embed": self.non_embed_params,
            "params_embed": self.embed_params,
            "gauss_complex": self.gauss_enabled,
            "tokens_per_sec": tok_per_sec,
            "sec_per_step": sec_per_step,
            "flops_per_step": flops_step,
            "flops_per_sec": flops_per_sec,
            "bytes_per_step": bytes_step,
            "bytes_per_sec": bytes_per_sec,
            "val_loss": val_loss,
            "val_ppl": val_ppl,
            "val_acc": val_acc,
            # Los tres ratios pedidos:
            "perf_per_param":     perf_quality / max(params_M, 1e-9),
            "perf_per_GFLOP_sec": tok_per_sec / max(flops_per_sec / 1e9, 1e-9),
            "perf_per_GBs":       tok_per_sec / max(bytes_per_sec / 1e9, 1e-9),
        }

    def format_log(self, m: Dict[str, Any]) -> str:
        return (
            f"params={m['params_total']/1e6:.2f}M (non-embed {m['params_non_embed']/1e6:.2f}M) "
            f"gauss={m['gauss_complex']} "
            f"tok/s={m['tokens_per_sec']:.1f} "
            f"GFLOPS={m['flops_per_sec']/1e9:.2f} "
            f"GB/s={m['bytes_per_sec']/1e9:.2f}\n"
            f"  ratios: 1/ppl_per_Mparam={m['perf_per_param']:.4e} | "
            f"tok/s_per_GFLOP={m['perf_per_GFLOP_sec']:.3e} | "
            f"tok/s_per_GB={m['perf_per_GBs']:.3e}"
        )


# ============================================================================
# CURRICULUM DATA LOADER
# ============================================================================

class CodeCurriculumLoader:
    """
    Carga los 4 datasets, normaliza cada ejemplo a una unica cadena de texto,
    tokeniza con BPE y produce splits train / val / holdout disjuntos.

    Politica de normalizacion por dataset:
      - CodeAlpaca:           "### Instruction\n{i}\n### Input\n{x}\n### Response\n{o}"
      - Code-Feedback:        concat de turnos: "<usr> ... </usr>\n<asst> ... </asst>"
      - Magicoder-Evol:       "### Problem\n{p}\n### Solution\n{s}"
      - Tiny-The-Stack:       texto crudo del archivo (truncado a 32k chars/file)

    Cache en disco: tokens_{tier}_{split}.bin (int32 memmap) + manifest .json.
    El HOLDOUT se separa con seed fija antes de tokenizar para garantizar
    que la misma muestra nunca aparezca en train o val entre corridas.
    """

    def __init__(
        self,
        config: TopoGPT3Config,
        tokenizer: BPETokenizer,
        logger: logging.Logger,
    ):
        self.config = config
        self.tokenizer = tokenizer
        self.logger = logger
        self.cache_dir = Path(config.DATA_CACHE)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    # ------------------------------------------------------------------
    # Normalizacion por dataset
    # ------------------------------------------------------------------

    @staticmethod
    def _format_codealpaca(ex: Dict[str, Any]) -> Optional[str]:
        instr = (ex.get("instruction") or "").strip()
        inp = (ex.get("input") or "").strip()
        out = (ex.get("output") or "").strip()
        if not instr or not out:
            return None
        if inp:
            return f"### Instruction\n{instr}\n### Input\n{inp}\n### Response\n{out}\n"
        return f"### Instruction\n{instr}\n### Response\n{out}\n"

    @staticmethod
    def _format_code_feedback(ex: Dict[str, Any]) -> Optional[str]:
        # m-a-p/CodeFeedback-Filtered-Instruction usa columnas query/answer
        q = (ex.get("query") or ex.get("question") or ex.get("instruction") or "").strip()
        a = (ex.get("answer") or ex.get("response") or ex.get("output") or "").strip()
        if q and a:
            return f"<|user|>\n{q}\n<|assistant|>\n{a}\n"
        # Fallback: forma multi-turno (chat)
        msgs = ex.get("messages") or ex.get("conversations") or []
        parts: List[str] = []
        for m in msgs:
            role = (m.get("role") or m.get("from") or "user").strip().lower()
            content = (m.get("content") or m.get("value") or "").strip()
            if not content:
                continue
            tag = "user" if role in ("user", "human") else "assistant"
            parts.append(f"<|{tag}|>\n{content}\n")
        joined = "".join(parts).strip()
        return joined or None

    @staticmethod
    def _format_magicoder(ex: Dict[str, Any]) -> Optional[str]:
        prob = (ex.get("instruction") or ex.get("problem") or "").strip()
        sol = (ex.get("response") or ex.get("solution") or ex.get("output") or "").strip()
        if not prob or not sol:
            return None
        return f"### Problem\n{prob}\n### Solution\n{sol}\n"

    @staticmethod
    def _format_tiny_stack(ex: Dict[str, Any]) -> Optional[str]:
        # bigcode/the-stack-smol usa 'content'; nampdn-ai/tiny-codes usa prompt/response
        content = ex.get("content") or ex.get("text") or ex.get("code") or ""
        if isinstance(content, str) and len(content) >= 30:
            return content[:32_000]
        prompt = (ex.get("prompt") or "").strip()
        response = (ex.get("response") or "").strip()
        if prompt and response:
            return f"### Prompt\n{prompt}\n### Response\n{response}\n"[:32_000]
        return None

    @classmethod
    def _get_formatter(cls, tier: str):
        return {
            "codealpaca":     cls._format_codealpaca,
            "code_feedback":  cls._format_code_feedback,
            "magicoder_evol": cls._format_magicoder,
            "tiny_the_stack": cls._format_tiny_stack,
        }[tier]

    # Por dataset: (attr_de_id, kwargs_extra_para_load_dataset)
    _HF_KWARGS: Dict[str, Tuple[str, Dict[str, Any]]] = {
        "codealpaca":     ("HF_CODEALPACA",    {}),
        "code_feedback":  ("HF_CODE_FEEDBACK", {}),
        "magicoder_evol": ("HF_MAGICODER",     {}),
        # Tiny-The-Stack: bigcode/the-stack-smol esta organizado por
        # data/<lenguaje>; tomamos python como muestra por defecto.
        "tiny_the_stack": ("HF_TINY_STACK",    {"data_dir": "data/python"}),
    }

    # ------------------------------------------------------------------
    # Tokenizacion + memmap por tier/split
    # ------------------------------------------------------------------

    def _tier_paths(self, tier: str) -> Dict[str, Path]:
        return {
            split: self.cache_dir / f"tokens_{tier}_{split}.bin"
            for split in ("train", "val", "holdout")
        }

    def _manifest_path(self, tier: str) -> Path:
        return self.cache_dir / f"manifest_{tier}.json"

    def _already_prepared(self, tier: str) -> bool:
        """True solo si los 3 splits existen, son no-vacios y el manifest concuerda."""
        paths = self._tier_paths(tier)
        manifest = self._manifest_path(tier)
        if not manifest.exists():
            return False
        if not all(p.exists() for p in paths.values()):
            return False
        try:
            with open(manifest, "r", encoding="utf-8") as f:
                meta = json.load(f)
            sizes = meta.get("sizes", {})
        except (json.JSONDecodeError, OSError):
            return False
        for split, p in paths.items():
            disk_n = p.stat().st_size // 4
            if disk_n == 0:
                self.logger.warning(
                    f"[{tier}] cache invalido: {p.name} esta vacio; re-preparando."
                )
                return False
            expected = sizes.get(split, 0)
            if expected > 0 and abs(disk_n - expected) > 4:
                self.logger.warning(
                    f"[{tier}] cache inconsistente: {p.name} disk={disk_n} "
                    f"manifest={expected}; re-preparando."
                )
                return False
        return True

    def _load_hf_with_fallback(self, tier: str):
        """Carga el dataset HF; para tiny_the_stack prueba una cadena de fallbacks
        publicos hasta que uno funcione."""
        try:
            from datasets import load_dataset
        except ImportError as exc:
            raise RuntimeError(
                "Requiere `datasets` de HuggingFace: pip install datasets"
            ) from exc

        attr, extra_kwargs = self._HF_KWARGS[tier]
        hf_id = getattr(self.config, attr)
        candidates: List[Tuple[str, Dict[str, Any]]] = [(hf_id, extra_kwargs)]
        if tier == "tiny_the_stack":
            for alt in self.config.HF_TINY_STACK_FALLBACKS:
                candidates.append((alt, {}))

        last_exc: Optional[Exception] = None
        for cand_id, cand_kwargs in candidates:
            self.logger.info(f"[{tier}] intentando {cand_id} {cand_kwargs} ...")
            try:
                return load_dataset(cand_id, split="train", **cand_kwargs)
            except Exception as exc:
                last_exc = exc
                msg = str(exc).splitlines()[0] if str(exc) else type(exc).__name__
                self.logger.warning(
                    f"[{tier}] {cand_id} no accesible: {msg}; probando siguiente."
                )

        raise RuntimeError(
            f"[{tier}] todos los datasets candidates fallaron. Ultimo error: {last_exc}"
        )

    def prepare_tier(self, tier_index: int, force: bool = False) -> Dict[str, int]:
        tier = self.config.TIER_NAMES[tier_index]
        if not force and self._already_prepared(tier):
            with open(self._manifest_path(tier), "r", encoding="utf-8") as f:
                return json.load(f)["sizes"]

        ds = self._load_hf_with_fallback(tier)
        attr, extra_kwargs = self._HF_KWARGS[tier]
        hf_id = getattr(self.config, attr)
        formatter = self._get_formatter(tier)
        rng = np.random.default_rng(self.config.SPLIT_SEED + tier_index)
        n = len(ds)
        idx = np.arange(n)
        rng.shuffle(idx)
        n_hold = max(1, int(n * self.config.HOLDOUT_FRACTION))
        n_val = max(1, int(n * self.config.VAL_FRACTION))
        hold_idx = set(idx[:n_hold].tolist())
        val_idx = set(idx[n_hold:n_hold + n_val].tolist())
        # train_idx implicito = el resto

        eot = self.tokenizer.eot_token()
        max_tokens = self.config.MAX_TOKENS_PER_TIER[tier_index]
        sizes = {"train": 0, "val": 0, "holdout": 0}
        files = {
            split: open(self._tier_paths(tier)[split], "wb")
            for split in ("train", "val", "holdout")
        }

        batch_tokens: Dict[str, List[int]] = {k: [] for k in files}
        CHUNK = 1_000_000

        def flush(split: str) -> None:
            arr = np.array(batch_tokens[split], dtype=np.int32)
            files[split].write(arr.tobytes())
            sizes[split] += arr.size
            batch_tokens[split] = []

        train_cap_hit = False
        for i, ex in enumerate(ds):
            if i in hold_idx:
                split = "holdout"
            elif i in val_idx:
                split = "val"
            else:
                if train_cap_hit:
                    continue
                split = "train"

            text = formatter(ex)
            if not text:
                continue
            try:
                ids = self.tokenizer.encode(text)
            except Exception:
                continue
            batch_tokens[split].extend(ids)
            batch_tokens[split].append(eot)

            if len(batch_tokens[split]) >= CHUNK:
                flush(split)
            if sizes["train"] >= max_tokens > 0:
                train_cap_hit = True

        for split in files:
            if batch_tokens[split]:
                flush(split)
            files[split].close()

        if sizes["train"] == 0:
            for p in self._tier_paths(tier).values():
                try:
                    p.unlink()
                except OSError:
                    pass
            raise RuntimeError(
                f"[{tier}] el formateador no produjo ejemplos validos. "
                f"Revisa el esquema del dataset (columnas esperadas vs reales)."
            )

        manifest = {
            "tier": tier,
            "hf_id": hf_id,
            "hf_kwargs": extra_kwargs,
            "sizes": sizes,
            "split_seed": self.config.SPLIT_SEED + tier_index,
            "saved_at": datetime.utcnow().isoformat(),
        }
        with open(self._manifest_path(tier), "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=2)
        self.logger.info(
            f"[{tier}] train={sizes['train']:,} val={sizes['val']:,} "
            f"holdout={sizes['holdout']:,} tokens"
        )
        return sizes

    def open_memmap(self, tier: str, split: str) -> np.memmap:
        path = self._tier_paths(tier)[split]
        if not path.exists():
            raise FileNotFoundError(
                f"Falta {path}. Corre --prepare-data primero."
            )
        n = path.stat().st_size // 4
        return np.memmap(path, dtype=np.int32, mode="r", shape=(n,))


# ============================================================================
# DATASET DE BLOQUES SOBRE TOKEN STREAM
# ============================================================================

class BlockTokenDataset(torch.utils.data.Dataset):
    """
    Dataset autoregresivo sobre un stream de tokens.
    Cada item es (x, y) con shape [seq_len].
    """

    def __init__(self, tokens: np.memmap, seq_len: int):
        self.tokens = tokens
        self.seq_len = seq_len
        self.n_blocks = max(0, (len(tokens) - 1) // seq_len)

    def __len__(self) -> int:
        return self.n_blocks

    def __getitem__(self, idx: int) -> Tuple[torch.Tensor, torch.Tensor]:
        start = idx * self.seq_len
        end = start + self.seq_len + 1
        block = np.array(self.tokens[start:end], dtype=np.int64)
        x = torch.from_numpy(block[:-1])
        y = torch.from_numpy(block[1:])
        return x, y


# ============================================================================
# CHECKPOINTING
# ============================================================================

class CheckpointStore:
    """Persiste pesos del modelo + estado del trainer (sin AMP scaler para portabilidad)."""

    def __init__(self, root: str, max_keep: int, logger: logging.Logger):
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)
        self.max_keep = max_keep
        self.logger = logger
        self.last_save_time = time.time()

    def save(self, tag: str, model: nn.Module, optimizer: torch.optim.Optimizer,
             state: Dict[str, Any]) -> None:
        """Guarda checkpoint atomico en <root>/last/ sobreescribiendo el anterior.

        El argumento `tag` se conserva por compatibilidad pero se ignora: solo
        existe un checkpoint llamado `last` y los pesos en safetensors.
        """
        from safetensors.torch import save_file as st_save
        del tag
        out = self.root / "last"
        out.mkdir(parents=True, exist_ok=True)
        model_path = out / "model.safetensors"
        optim_path = out / "optim.pt"
        state_path = out / "state.json"
        tmp_model = model_path.with_suffix(".safetensors.tmp")
        tmp_optim = optim_path.with_suffix(".pt.tmp")
        tmp_state = state_path.with_suffix(".json.tmp")

        st_save({k: v.detach().cpu() for k, v in model.state_dict().items()},
                str(tmp_model))
        torch.save(optimizer.state_dict(), tmp_optim)
        with open(tmp_state, "w", encoding="utf-8") as f:
            json.dump(state, f, indent=2, default=str)
        os.replace(tmp_model, model_path)
        os.replace(tmp_optim, optim_path)
        os.replace(tmp_state, state_path)

        self.last_save_time = time.time()
        size_mb = model_path.stat().st_size / 1024 / 1024
        self.logger.info(
            f"[checkpoint] guardado en {model_path} "
            f"({size_mb:.1f} MB, step={state.get('global_step', '?')})"
        )

    def load_latest(self, model: nn.Module, optimizer: torch.optim.Optimizer
                    ) -> Optional[Dict[str, Any]]:
        from safetensors.torch import load_file as st_load
        latest = self.root / "last"
        if not (latest / "model.safetensors").exists():
            legacy = sorted(
                [p for p in self.root.iterdir()
                 if p.is_dir() and p.name.startswith("step_")
                 and (p / "model.safetensors").exists()],
                key=lambda p: p.stat().st_mtime,
            )
            if not legacy:
                return None
            latest = legacy[-1]
            self.logger.info(f"No existe 'last/', cargando legacy: {latest.name}")
        sd = st_load(str(latest / "model.safetensors"))
        model.load_state_dict(sd, strict=False)
        if (latest / "optim.pt").exists():
            optimizer.load_state_dict(torch.load(latest / "optim.pt", map_location="cpu", weights_only=True))
        with open(latest / "state.json", "r", encoding="utf-8") as f:
            state = json.load(f)
        self.logger.info(f"Reanudado desde {latest}")
        return state

    def should_save(self, interval_min: int) -> bool:
        return (time.time() - self.last_save_time) >= interval_min * 60


# ============================================================================
# TRAINER CURRICULAR
# ============================================================================

class TopoGPT3Trainer:
    """
    Orquesta el curriculum sobre los 4 tiers.

    Pipeline por tier:
      1. Abre memmap de tokens (train/val/holdout).
      2. Construye DataLoaders con seq_len(tier).
      3. Entrena TIER_EPOCHS[tier] epocas con AMP + grad accum.
      4. Cada GRASS_TRACK_EVERY steps: snapshot Grassmanniano.
      5. Al final de cada epoca: eval en VAL.
      6. Al final del tier: eval en HOLDOUT (datos nunca vistos).
      7. Checkpoint y avanza al siguiente tier.

    Al final del pipeline: eval en HOLDOUT *combinado* de los 4 tiers.
    """

    def __init__(self, config: TopoGPT3Config, start_tier: Optional[int] = None):
        self.config = config
        self.logger = setup_logger("TopoGPT3", "INFO")
        self.start_tier_explicit = start_tier is not None
        self.start_tier = 0 if start_tier is None else int(start_tier)
        if not (0 <= self.start_tier < len(config.TIER_NAMES)):
            raise ValueError(
                f"start_tier fuera de rango: {self.start_tier} "
                f"(valido 0..{len(config.TIER_NAMES) - 1})"
            )
        set_seed(config.RANDOM_SEED, config.DEVICE)

        # Activa el truco de Gauss ANTES de instanciar el modelo para que
        # todas las QuaternionSpectralLayer ya usen 3 productos reales.
        if config.USE_GAUSS_COMPLEX_MULT:
            apply_gauss_patch(self.logger)

        # max_seq fijo sobre TODOS los tiers: la forma del embedding posicional
        # queda estable y los safetensors guardados se cargan sin mismatch
        # aunque se cambie start_tier entre runs.
        max_seq = max(config.TIER_SEQ_LEN)
        max_window = max(config.PROGRESSIVE_WINDOW)
        self.base_cfg = config.build_topogpt2_config(max_seq, attn_window=max_window)
        self.tokenizer = BPETokenizer()
        self.model = TopoGPT2(self.base_cfg).to(config.DEVICE)
        self.optimizer = torch.optim.AdamW(
            self.model.parameters(),
            lr=config.LEARNING_RATE,
            weight_decay=config.WEIGHT_DECAY,
            betas=(0.9, 0.95),
        )

        dev = config.DEVICE
        self.amp_dtype = torch.float16 if "cuda" in dev else torch.bfloat16
        self.scaler = torch.amp.GradScaler(
            dev.split(":")[0],
            enabled=config.USE_AMP and "cuda" in dev,
        )

        self.loader = CodeCurriculumLoader(config, self.tokenizer, self.logger)
        self.tracker = GrassmannianTracker(config, self.logger)
        self.ckpt = CheckpointStore(config.CHECKPOINT_DIR, config.MAX_CHECKPOINTS, self.logger)
        self.efficiency = EfficiencyMetrics(
            self.model, config, self.logger,
            gauss_enabled=config.USE_GAUSS_COMPLEX_MULT,
        )

        self.global_step = 0
        self.completed_tiers: List[str] = []
        self.tier_metrics: Dict[str, Dict[str, float]] = {}

    # ------------------------------------------------------------------
    # Preparacion de datos
    # ------------------------------------------------------------------

    def prepare_all(self, force: bool = False) -> None:
        """Prepara cada tier; un fallo en uno no detiene los demas."""
        for i, tier in enumerate(self.config.TIER_NAMES):
            self.logger.info(
                f"=== preparando tier {i+1}/{len(self.config.TIER_NAMES)}: {tier} ==="
            )
            try:
                self.loader.prepare_tier(i, force=force)
            except RuntimeError as exc:
                self.logger.error(f"[{tier}] preparacion fallida: {exc}")
                self.logger.error(f"[{tier}] se omite; otros tiers continuan.")

    # ------------------------------------------------------------------
    # Loaders por tier
    # ------------------------------------------------------------------

    def _build_loaders(self, tier_index: int) -> Tuple[
        torch.utils.data.DataLoader,
        torch.utils.data.DataLoader,
        torch.utils.data.DataLoader,
    ]:
        tier = self.config.TIER_NAMES[tier_index]
        seq_len = self.config.TIER_SEQ_LEN[tier_index]

        train_tok = self.loader.open_memmap(tier, "train")
        val_tok = self.loader.open_memmap(tier, "val")
        hold_tok = self.loader.open_memmap(tier, "holdout")

        train_ds = BlockTokenDataset(train_tok, seq_len)
        val_ds = BlockTokenDataset(val_tok, seq_len)
        hold_ds = BlockTokenDataset(hold_tok, seq_len)

        bs = self.config.BATCH_SIZE
        train_dl = torch.utils.data.DataLoader(
            train_ds, batch_size=bs, shuffle=True, drop_last=True, num_workers=0
        )
        val_dl = torch.utils.data.DataLoader(
            val_ds, batch_size=bs, shuffle=False, drop_last=True, num_workers=0
        )
        hold_dl = torch.utils.data.DataLoader(
            hold_ds, batch_size=bs, shuffle=False, drop_last=True, num_workers=0
        )
        return train_dl, val_dl, hold_dl

    # ------------------------------------------------------------------
    # LR schedule (cosine con warmup)
    # ------------------------------------------------------------------

    def _cosine_lr(self, step: int, total_steps: int) -> float:
        warmup = max(1, int(total_steps * self.config.WARMUP_RATIO))
        if step < warmup:
            return self.config.LEARNING_RATE * step / warmup
        t = (step - warmup) / max(total_steps - warmup, 1)
        return self.config.LEARNING_RATE * 0.5 * (1.0 + math.cos(math.pi * t))

    def _set_lr(self, lr: float) -> None:
        for pg in self.optimizer.param_groups:
            pg["lr"] = lr

    # ------------------------------------------------------------------
    # Train loop por tier
    # ------------------------------------------------------------------

    def _train_one_tier(self, tier_index: int) -> Optional[Dict[str, float]]:
        tier = self.config.TIER_NAMES[tier_index]
        epochs = self.config.TIER_EPOCHS[tier_index]
        seq_len = self.config.TIER_SEQ_LEN[tier_index]
        try:
            train_dl, val_dl, hold_dl = self._build_loaders(tier_index)
        except (FileNotFoundError, ValueError) as exc:
            self.logger.warning(
                f"[{tier}] saltado: no hay datos preparados ({exc})."
            )
            return None
        if len(train_dl.dataset) == 0:
            self.logger.warning(f"[{tier}] saltado: train_blocks=0.")
            return None

        steps_per_epoch = len(train_dl) // self.config.GRAD_ACCUM_STEPS
        if self.config.MAX_TRAIN_BATCHES_PER_EPOCH > 0:
            steps_per_epoch = min(
                steps_per_epoch,
                self.config.MAX_TRAIN_BATCHES_PER_EPOCH // self.config.GRAD_ACCUM_STEPS,
            )
        total_steps = steps_per_epoch * epochs
        self.logger.info(
            f"### TIER {tier_index+1}/{len(self.config.TIER_NAMES)}: {tier} "
            f"| epochs={epochs} seq_len={seq_len} "
            f"| train_blocks={len(train_dl.dataset)} val={len(val_dl.dataset)} "
            f"hold={len(hold_dl.dataset)} optim_steps={total_steps}"
        )

        step_in_tier = 0
        last_val_loss = float("inf")
        last_val_acc = 0.0

        for epoch in range(1, epochs + 1):
            self.model.train()
            self.optimizer.zero_grad(set_to_none=True)
            running_loss = 0.0
            running_correct = 0
            running_total = 0
            seen = 0
            batches_since_step = 0

            for batch_idx, (bx, by) in enumerate(train_dl):
                if (self.config.MAX_TRAIN_BATCHES_PER_EPOCH > 0
                        and batch_idx >= self.config.MAX_TRAIN_BATCHES_PER_EPOCH):
                    break
                bx = bx.to(self.config.DEVICE, non_blocking=True)
                by = by.to(self.config.DEVICE, non_blocking=True)

                lr = self._cosine_lr(step_in_tier, total_steps)
                self._set_lr(lr)

                with torch.amp.autocast(
                    device_type=self.config.DEVICE.split(":")[0],
                    dtype=self.amp_dtype,
                    enabled=self.config.USE_AMP,
                ):
                    logits, recon_loss, _ = self.model(bx)
                    lm_loss = F.cross_entropy(
                        logits.view(-1, self.base_cfg.VOCAB_SIZE),
                        by.view(-1),
                    )
                    loss = (lm_loss + self.base_cfg.AE_RECON_WEIGHT * recon_loss
                            ) / self.config.GRAD_ACCUM_STEPS

                self.scaler.scale(loss).backward()
                running_loss += float(lm_loss.item())
                with torch.no_grad():
                    preds = logits.argmax(dim=-1)
                    running_correct += int((preds == by).sum().item())
                    running_total += int(by.numel())
                seen += 1
                batches_since_step += 1

                if batches_since_step >= self.config.GRAD_ACCUM_STEPS:
                    self.scaler.unscale_(self.optimizer)
                    torch.nn.utils.clip_grad_norm_(
                        self.model.parameters(), self.config.GRADIENT_CLIP_NORM
                    )
                    self.scaler.step(self.optimizer)
                    self.scaler.update()
                    self.optimizer.zero_grad(set_to_none=True)
                    self.global_step += 1
                    step_in_tier += 1
                    batches_since_step = 0

                    if self.global_step % self.config.GRASS_TRACK_EVERY == 0:
                        snap = self.tracker.snapshot(
                            self.model,
                            self.global_step,
                            dataloader=val_dl,
                            vocab_size=self.base_cfg.VOCAB_SIZE,
                        )
                        self.logger.info(
                            f"[grass step={self.global_step}] "
                            + self.tracker.format_log(snap)
                        )

                    if self.global_step % self.config.LOG_INTERVAL_STEPS == 0:
                        train_acc = running_correct / max(running_total, 1)
                        self.logger.info(
                            f"[tier={tier} ep={epoch} step={self.global_step}] "
                            f"lm={running_loss/max(seen,1):.4f} "
                            f"acc={train_acc*100:.2f}% "
                            f"lr={lr:.2e}"
                        )

                if self.ckpt.should_save(self.config.CHECKPOINT_EVERY_MIN):
                    self.ckpt.save(
                        f"step_{self.global_step:07d}",
                        self.model, self.optimizer,
                        self._state_dict(),
                    )

            avg_train = running_loss / max(seen, 1)
            train_acc = running_correct / max(running_total, 1)
            val_loss, val_ppl, val_acc = self._evaluate(val_dl)
            last_val_loss = val_loss
            last_val_acc = val_acc
            self.logger.info(
                f"[tier={tier} epoch {epoch}/{epochs}] "
                f"train_lm={avg_train:.4f} train_acc={train_acc*100:.2f}% | "
                f"val_lm={val_loss:.4f} val_acc={val_acc*100:.2f}% val_ppl={val_ppl:.2f}"
            )

        # Holdout: datos del tier que nunca se vieron durante entrenamiento ni en val
        hold_loss, hold_ppl, hold_acc = self._evaluate(hold_dl)
        self.logger.info(
            f"[tier={tier} HOLDOUT-no-visto] "
            f"hold_lm={hold_loss:.4f} hold_acc={hold_acc*100:.2f}% hold_ppl={hold_ppl:.2f}"
        )

        # Mediciones de eficiencia (perf/param, perf/FLOP, perf/BW)
        eff = self.efficiency.compute(
            dataloader=val_dl, vocab_size=self.base_cfg.VOCAB_SIZE,
            val_loss=last_val_loss, val_ppl=math.exp(min(last_val_loss, 20.0)),
            val_acc=last_val_acc,
            batch_size=self.config.BATCH_SIZE, seq_len=seq_len,
        )
        self.logger.info(f"[tier={tier} EFFICIENCY] " + self.efficiency.format_log(eff))

        self.ckpt.save(
            f"step_{self.global_step:07d}_end_{tier}",
            self.model, self.optimizer,
            self._state_dict(),
        )
        return {
            "tier": tier,
            "val_loss": last_val_loss,
            "val_acc": last_val_acc,
            "holdout_loss": hold_loss,
            "holdout_acc": hold_acc,
            "holdout_ppl": hold_ppl,
            "efficiency": eff,
        }

    # ------------------------------------------------------------------
    # Eval
    # ------------------------------------------------------------------

    @torch.no_grad()
    def _evaluate(self, dl: torch.utils.data.DataLoader) -> Tuple[float, float, float]:
        """Devuelve (avg_loss, perplexity, token_accuracy)."""
        self.model.eval()
        total_loss = 0.0
        n_batches = 0
        n_correct = 0
        n_tokens = 0
        for i, (bx, by) in enumerate(dl):
            if i >= self.config.MAX_EVAL_BATCHES:
                break
            bx = bx.to(self.config.DEVICE, non_blocking=True)
            by = by.to(self.config.DEVICE, non_blocking=True)
            with torch.amp.autocast(
                device_type=self.config.DEVICE.split(":")[0],
                dtype=self.amp_dtype,
                enabled=self.config.USE_AMP,
            ):
                logits, _, _ = self.model(bx)
                loss = F.cross_entropy(
                    logits.view(-1, self.base_cfg.VOCAB_SIZE),
                    by.view(-1),
                )
            total_loss += float(loss.item())
            preds = logits.argmax(dim=-1)
            n_correct += int((preds == by).sum().item())
            n_tokens += int(by.numel())
            n_batches += 1
        self.model.train()
        if n_batches == 0:
            return float("inf"), float("inf"), 0.0
        avg = total_loss / n_batches
        acc = n_correct / max(n_tokens, 1)
        return avg, math.exp(min(avg, 20.0)), acc

    # ------------------------------------------------------------------
    # Estado / checkpoint
    # ------------------------------------------------------------------

    def _state_dict(self) -> Dict[str, Any]:
        return {
            "global_step": self.global_step,
            "completed_tiers": self.completed_tiers,
            "tier_metrics": self.tier_metrics,
            "config": asdict(self.config),
            "saved_at": datetime.utcnow().isoformat(),
        }

    # ------------------------------------------------------------------
    # Loops publicos
    # ------------------------------------------------------------------

    def run(self) -> None:
        if self.start_tier_explicit:
            # El usuario fija el tier inicial: se honra tal cual y se recortan
            # los completed_tiers a [0, start_tier) para que el rerun no quede
            # marcado como "ya hecho" en el state.json del checkpoint.
            effective_start = self.start_tier
            allowed = set(self.config.TIER_NAMES[:effective_start])
            dropped = [t for t in self.completed_tiers if t not in allowed]
            if dropped:
                self.logger.info(
                    f"--start-tier={effective_start} explicito: "
                    f"se reentrenan tiers previamente completados: {dropped}"
                )
            self.completed_tiers = [t for t in self.completed_tiers if t in allowed]
        else:
            # Comportamiento por defecto: si hubo auto-resume, avanza
            # start_tier mas alla de los tiers ya completados.
            effective_start = self.start_tier
            for i, name in enumerate(self.config.TIER_NAMES):
                if name in self.completed_tiers and i == effective_start:
                    effective_start = i + 1

        self.logger.info("=" * 70)
        self.logger.info("TopoGPT3 - curriculum sobre Grassmanniana")
        p = self.model.count_params()
        self.logger.info(f"Parametros: {p['total']:,}")
        self.logger.info(f"Device: {self.config.DEVICE} | AMP: {self.config.USE_AMP}")
        if self.completed_tiers:
            self.logger.info(f"Tiers ya completados: {self.completed_tiers}")
        self.logger.info(
            f"Tiers a entrenar: {list(self.config.TIER_NAMES[effective_start:])}"
        )
        self.logger.info("=" * 70)

        # Snapshot inicial geometrico (referencia U_ref)
        snap0 = self.tracker.snapshot(self.model, step=0)
        self.logger.info("[grass init] " + self.tracker.format_log(snap0))

        for tier_index in range(effective_start, len(self.config.TIER_NAMES)):
            res = self._train_one_tier(tier_index)
            tier = self.config.TIER_NAMES[tier_index]
            if res is None:
                self.logger.warning(f"[{tier}] tier saltado por falta de datos.")
                continue
            if tier not in self.completed_tiers:
                self.completed_tiers.append(tier)
            self.tier_metrics[tier] = res

        # Generalizacion combinada: concatenamos todos los holdouts
        self._eval_combined_holdout()
        self.tracker.save(str(Path(self.config.CHECKPOINT_DIR) / "grass_history.jsonl"))
        with open(Path(self.config.CHECKPOINT_DIR) / self.config.LOG_FILE, "w") as f:
            json.dump({
                "tier_metrics": self.tier_metrics,
                "global_step": self.global_step,
            }, f, indent=2)

    def _eval_combined_holdout(self) -> None:
        self.logger.info("=" * 70)
        self.logger.info("EVALUACION FINAL: holdout combinado (datos NUNCA vistos)")
        results: Dict[str, Tuple[float, float, float]] = {}
        for i, tier in enumerate(self.config.TIER_NAMES):
            try:
                hold = self.loader.open_memmap(tier, "holdout")
            except (FileNotFoundError, ValueError):
                continue
            seq_len = self.config.TIER_SEQ_LEN[i]
            ds = BlockTokenDataset(hold, seq_len)
            if len(ds) == 0:
                continue
            dl = torch.utils.data.DataLoader(
                ds, batch_size=self.config.BATCH_SIZE,
                shuffle=False, drop_last=True, num_workers=0,
            )
            loss, ppl, acc = self._evaluate(dl)
            results[tier] = (loss, ppl, acc)
            self.logger.info(
                f"  {tier:<20s} loss={loss:.4f}  acc={acc*100:.2f}%  ppl={ppl:.2f}"
            )
        self.tier_metrics["__combined_holdout__"] = {
            t: {"loss": l, "ppl": p, "acc": a} for t, (l, p, a) in results.items()
        }
        self.logger.info("=" * 70)


# ============================================================================
# CLI
# ============================================================================

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="TopoGPT3 Grassmannian + curriculum")
    p.add_argument("--prepare-data", action="store_true",
                   help="Descarga y tokeniza los 4 datasets en cache local.")
    p.add_argument("--train", action="store_true",
                   help="Entrena el pipeline curricular completo.")
    p.add_argument("--eval-holdout", action="store_true",
                   help="Evalua solo en los holdouts (datos nunca vistos).")
    p.add_argument("--start-tier", type=int, default=None,
                   help="Tier inicial explicito (0..3). Si se omite, arranca "
                        "en 0 o avanza automaticamente saltando tiers ya "
                        "completados en el checkpoint. Si se pasa, se honra "
                        "tal cual y los tiers >= start_tier se re-entrenan.")
    p.add_argument("--scale", type=str, default="small",
                   choices=["micro", "small", "medium", "gpt2"],
                   help="Escala del modelo TopoGPT2 base.")
    p.add_argument("--resume", action="store_true",
                   help="(legacy) Equivalente al comportamiento por defecto: "
                        "reanuda si existe checkpoint. Mantenido por compat.")
    p.add_argument("--from-scratch", action="store_true",
                   help="Ignora el checkpoint existente y arranca desde cero. "
                        "Por defecto se hace auto-resume si existe 'last/'.")
    p.add_argument("--force-prepare", action="store_true",
                   help="Fuerza re-tokenizacion ignorando cache.")
    p.add_argument("--device", type=str, default=None,
                   help="Override de device (cuda|cpu|cuda:0|...)")
    return p.parse_args()


def main() -> None:
    args = parse_args()
    cfg = TopoGPT3Config(SCALE=args.scale)
    if args.device:
        cfg.DEVICE = args.device

    if not (args.prepare_data or args.train or args.eval_holdout):
        print("Nada que hacer. Pasa --prepare-data, --train o --eval-holdout.",
              file=sys.stderr)
        sys.exit(1)

    trainer = TopoGPT3Trainer(cfg, start_tier=args.start_tier)

    if args.prepare_data:
        trainer.prepare_all(force=args.force_prepare)

    ckpt_exists = (Path(cfg.CHECKPOINT_DIR) / "last" / "model.safetensors").exists()
    legacy_exists = any(
        (Path(cfg.CHECKPOINT_DIR) / d.name / "model.safetensors").exists()
        for d in Path(cfg.CHECKPOINT_DIR).iterdir()
        if d.is_dir() and d.name.startswith("step_")
    ) if Path(cfg.CHECKPOINT_DIR).exists() else False

    should_resume = (not args.from_scratch) and (ckpt_exists or legacy_exists)
    if args.from_scratch and (ckpt_exists or legacy_exists):
        trainer.logger.info(
            "--from-scratch: ignorando checkpoints existentes y arrancando random."
        )

    if should_resume:
        state = trainer.ckpt.load_latest(trainer.model, trainer.optimizer)
        if state is not None:
            trainer.global_step = state.get("global_step", 0)
            trainer.completed_tiers = state.get("completed_tiers", [])
            trainer.logger.info(
                f"Auto-resume desde step={trainer.global_step} "
                f"completed_tiers={trainer.completed_tiers}"
            )

    if args.train:
        trainer.run()

    if args.eval_holdout:
        trainer._eval_combined_holdout()


if __name__ == "__main__":
    main()
