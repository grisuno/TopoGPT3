"""Shared training utilities for TopoGPT3 advanced trainers.

Adapted to TopoGPT3 checkpoints (safetensors slot `last/` + legacy step_*)
with DDP / cross-GPU resume / wandb-continuity helpers.
Architecture-agnostic: never touches Quaternion/Spectral layers.
"""
from __future__ import annotations

import math
import os
import random
from typing import Optional

import numpy as np
import torch
import torch.distributed as dist
from torch.utils.data import Sampler


def Logger(content, quiet: bool = False):
    if not quiet and (not dist.is_initialized() or dist.get_rank() == 0):
        print(content, flush=True)


def is_main_process() -> bool:
    return not dist.is_initialized() or dist.get_rank() == 0


def get_lr(current_step: int, total_steps: int, lr: float) -> float:
    total_steps = max(total_steps, 1)
    return lr * (0.1 + 0.45 * (1 + math.cos(math.pi * current_step / total_steps)))


def setup_seed(seed: int):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)


def init_distributed_mode() -> int:
    if int(os.environ.get("RANK", -1)) == -1:
        return 0
    dist.init_process_group(backend="nccl")
    local_rank = int(os.environ.get("LOCAL_RANK", 0))
    torch.cuda.set_device(local_rank)
    return local_rank


class SkipBatchSampler(Sampler):
    def __init__(self, sampler, batch_size: int, skip_batches: int = 0):
        self.sampler = sampler
        self.batch_size = batch_size
        self.skip_batches = skip_batches

    def __iter__(self):
        batch, skipped = [], 0
        for idx in self.sampler:
            batch.append(idx)
            if len(batch) == self.batch_size:
                if skipped < self.skip_batches:
                    skipped += 1
                    batch = []
                    continue
                yield batch
                batch = []
        if batch and skipped >= self.skip_batches:
            yield batch

    def __len__(self):
        total = (len(self.sampler) + self.batch_size - 1) // self.batch_size
        return max(0, total - self.skip_batches)


def topo_checkpoint(save_dir: str, weight: str, model=None, optimizer=None,
                    scheduler=None, scaler=None, epoch: int = 0, step: int = 0,
                    wandb=None, extra: Optional[dict] = None):
    """Atomic double-save: fp16 weights + resume state (weights + optim).

    Handles world_size rescale on load (delegated to train.py CheckpointStore
    when present; here we store world_size so future loaders can rescale).
    """
    os.makedirs(save_dir, exist_ok=True)
    if model is None:
        # load mode
        for cand in (f"{save_dir}/{weight}_resume.pt",
                     f"{save_dir}/{weight}_resume.pth"):
            if os.path.exists(cand):
                data = torch.load(cand, map_location="cpu")
                saved_ws = data.get("world_size", 1)
                cur_ws = dist.get_world_size() if dist.is_initialized() else 1
                if saved_ws != cur_ws and "step" in data:
                    data["step"] = data["step"] * saved_ws // cur_ws
                    Logger(f"GPU count changed ({saved_ws}->{cur_ws}), step->{data['step']}")
                return data
        return None
    from torch.nn.parallel import DistributedDataParallel
    raw = model.module if isinstance(model, DistributedDataParallel) else model
    raw = getattr(raw, "_orig_mod", raw)
    sd = {k: v.half().cpu() for k, v in raw.state_dict().items() if ".lora." not in k}
    tmp = f"{save_dir}/{weight}.pt.tmp"
    torch.save(sd, tmp)
    os.replace(tmp, f"{save_dir}/{weight}.pt")
    wid = None
    if wandb is not None:
        try:
            run = wandb.get_run() if hasattr(wandb, "get_run") else None
            wid = getattr(run, "id", None) if run else getattr(wandb, "id", None)
        except Exception:
            wid = None
    resume = {"model": sd,
              "epoch": epoch, "step": step,
              "world_size": dist.get_world_size() if dist.is_initialized() else 1,
              "wandb_id": wid}
    if optimizer is not None:
        resume["optimizer"] = optimizer.state_dict()
    if scheduler is not None:
        resume["scheduler"] = scheduler.state_dict()
    if scaler is not None and hasattr(scaler, "state_dict"):
        try:
            resume["scaler"] = scaler.state_dict()
        except Exception:
            pass
    if extra:
        resume.update(extra)
    rtmp = f"{save_dir}/{weight}_resume.pt.tmp"
    torch.save(resume, rtmp)
    os.replace(rtmp, f"{save_dir}/{weight}_resume.pt")
    del sd, resume
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
