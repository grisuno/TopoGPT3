# TIER 1: Static Diagnostics & Robustness Sweep on `checkpoints_topogpt3/last`

**Date:** 2026-06-15
**Checkpoint:** `checkpoints_topogpt3/last` (24,457,622 params, global_step=51,712)
**Mode:** Frozen-checkpoint analysis. No retraining performed.
**Tools:** `eval/diag_static.py`, `eval/noise_sweep.py`, `eval/noise_analysis.py`,
`eval/temp_sweep.py`

---

## 1. What was measured

The proposed experiments were decomposed into three groups based on what
the existing code can do today:

| Proposed experiment | Status here | Tool |
|---|---|---|
| 1. Compute κ on TopoGPT3 | implemented and run | `diag_static.py` |
| 2. Compute δ in spectral space | implemented and run | `diag_static.py` |
| 4. Inject noise on weights | implemented and run | `noise_sweep.py` + `noise_analysis.py` |
| 7. Apply HRM during training | requires `HRMTrainer` (TIER 3) | not run |
| 5. Train real vs complex | requires refactor (TIER 3) | not run |
| 6. Use quaternions vs complex | requires refactor (TIER 3) | not run |
| 3. Batch sizes outside [24,128] | requires retraining (TIER 2) | not run |

Of the seven proposed, four are within reach without code surgery.
We report what was actually measured and what it does and does not say.

---

## 2. Static spectral diagnostics (`diag_static.py`)

Stacked all `QuaternionSpectralLayer` kernels (kr/ki × w/x/y/z) into a
single `K(theta) in C^{N_f x N_c}` with `K.shape = (288, 4096)`,
then performed a single SVD on the frozen checkpoint.

| Metric | Value | Interpretation |
|---|---|---|
| κ (kappa)         | 3.59      | regime: stable (crystal-like) |
| σ_max             | 4.00      | |
| σ_min             | 1.12      | |
| n_singular        | 288       | (capped to subspace dim) |
| δ_max             | 0.5000    | phases NOT quantized |
| δ_mean            | 0.2518    | uniform phase distribution |
| frac_near_integer | 0.170     | only 17% of phases within 5% of 2π·Z |
| W (synthetic)     | +2.50     | frequency-window sweep winding |

**Reading the numbers:**

- **κ = 3.59** supports the "stable regime" prediction of the
  framework. The top of the singular spectrum is well separated from
  the tail (κ of order 1 to 10), not diverging to 10^3 or higher.
  This is consistent with the trainer-reported `Δ_F > 0` from
  `train.py:474` during the actual optimization.

- **δ = 0.5** is the worst possible value. `δ_max = 0.5` is exactly
  what you get when phases are uniformly distributed on the circle
  (the half-diagonal of the unit square). This **fails** the
  "phases discretize" prediction of the framework, at least on the
  static kernel tensor of the final checkpoint.

  Important caveat: `δ` is being measured on a single frozen
  snapshot. The framework's claim is that phases *crystallize
  during training*, which we cannot test without trajectories.
  The current measurement is closer to a "post-crystallization
  audit" than to the framework's intended setting.

- **W = +2.5** was computed by sweeping frequency windows, not
  optimization steps. The number is meaningful only as a coherence
  diagnostic of the spectral tensor, not as a topological
  invariant of training. The trainer's own W computation lives in
  `GrassmannianTracker._accumulate_winding` and operates on
  consecutive step snapshots; that one is what would actually
  test the framework.

**Artefacts:**
- `eval/runs/diag_static_1781498496.jsonl`

---

## 3. Noise injection sweep (`noise_sweep.py` + `noise_analysis.py`)

For each σ ∈ {0, 1e-4, 1e-3, 1e-2}, added iid Gaussian noise
N(0, σ) to all 96 spectral kernel tensors (kr/ki × w/x/y/z) of the
QuaternionSpectralLayers only. That is 2,359,296 parameters
contaminated per σ, all in the spectral subdomain the framework
claims to be topologically protected.

Then evaluated pass@1 (greedy, T=0, top_k=0, max_new=256) on the
first 50 HumanEval problems.

| σ       | n_pass / 50 | pass@1 | pair-wise agreement with σ=0 |
|---------|-------------|--------|------------------------------|
| 0.0     | 2           | 4.00%  | —                            |
| 1e-4    | 2           | 4.00%  | 100% (50/50)                 |
| 1e-3    | 2           | 4.00%  | 100% (50/50)                 |
| 1e-2    | 2           | 4.00%  | 100% (50/50)                 |

**The same 2 problems pass at every noise level.** They are
HumanEval/30 (`get_positive`: return positive numbers) and
HumanEval/35 (`max_element`: return max). Both are one-liners that
any reasonable completion passes. The remaining 48 problems never
pass, at any σ.

**What this does and does not say:**

- It does **not** demonstrate topological protection of the
  manifold. A pass@1=4% on HumanEval is too coarse a probe —
  it saturates on trivial problems and floors on hard ones.
  To actually test the framework's "phase protection" claim we
  would need a finer probe: token-level prefix agreement, exact
  match, BLEU, perplexity, or a pass@k with many samples at
  high T (where the model has room to fail differently).

- It does **not** contradict the framework either. A relative
  metric (prefix agreement, distribution shift) is needed.
  The current harness only stores post-extracted candidates
  (the cleanup regex in `harness.py:extract_candidate` discards
  the raw token stream), so we cannot re-derive those metrics
  post-hoc without rerunning with raw output capture.

**Wall clock:** ~77s per σ on CPU, 50 problems. Total ~5 min.

**Artefacts:**
- `eval/runs/noise_sigma0e+00_v1.jsonl` and 3 sibling files
- `eval/runs/noise_sweep_v1.jsonl` (summary)
- `eval/runs/noise_analysis_v1.json` (consistency)

---

## 4. Temperature × top-k sweep (`temp_sweep.py`)

30 HumanEval problems × 5 samples per (T, top_k) cell. n_samples=5
is small for pass@5 but matches the framework's "variance
diagnosis" intent.

| T   | top_k | pass@1 | pass@5 | any-pass | wall |
|-----|-------|--------|--------|----------|------|
| 0.0 | 0     | 0.00%  | 0.00%  | 0.00%    | 184s |
| 0.2 | 40    | 0.00%  | 0.00%  | 0.00%    | 160s |
| 0.5 | 40    | 0.00%  | 3.33%  | 3.33%    | 227s |
| 0.8 | 40    | 0.00%  | 3.33%  | 3.33%    | 264s |

**Reading the phase map:**

- At T=0.0 and T=0.2 the model is locked: it commits to a
  single (failing) completion and never escapes.
- At T=0.5 it begins to explore enough to land one passing
  sample across the 30×5=150 trials.
- At T=0.8 the same one problem is found; no new ones emerge.

This is a **small** sweep on a **small** subset, so the
conclusion is qualitative only. The "frozen crystal vs
fluctuating glass" transition that the framework predicts
*does* seem to occur between T=0.2 and T=0.5 here, but with
n=30 problems and a 24M-parameter model we cannot disentangle
"the temperature transition" from "the model is just bad at
HumanEval".

**Artefacts:**
- `eval/runs/temp_T<T>_top<k>_v1.jsonl` (4 detail files)
- `eval/runs/temp_sweep_v1.jsonl` (summary)

---

## 5. What the framework's predictions need that TIER 1 cannot provide

The 7-experiment plan lists several predictions whose truth
value is not testable on a single frozen checkpoint:

1. **κ separation between regimes during training** — `κ = 3.59`
   on the final checkpoint is one number. The framework's claim
   is that κ → ∞ in the chaotic regime and κ ≈ 1 in the stable
   regime. To test this we would need a training trajectory with
   checkpoints at multiple phases, and a `δ` series showing
   crystallization.

2. **δ discretization** — needs the same trajectory. δ measured
   on a static K only tells you the final state, not the
   trajectory of phase quantization.

3. **W dynamics** — the trainer already computes W in
   `GrassmannianTracker._accumulate_winding` on consecutive
   steps. That series was logged to stdout during the original
   training but not persisted to a JSONL. Without that
   history we cannot plot W(t).

4. **Batch-size phase boundary** — requires retraining at
   different batch sizes. TIER 2.

5. **Real vs complex** — requires a refactor of
   `QuaternionLinear` to make the algebra swappable. TIER 3.

6. **Quaternions vs complex** — same refactor.

7. **HRM during training** — `inference_hrm.py` is a sampler
   only. There is no trainer that uses the model as the step
   function of a refinement loop. TIER 3.

---

## 6. Recommended next steps (TIER 2, ~1 day of work)

1. **Persist `GrassmannianTracker.history` to a JSONL**
   inside `topogpt3/train.py`. Two lines: a `tracker.save()`
   call inside `CheckpointStore.save` and a snapshot trigger on
   the existing interval. This unblocks W(t) and κ(t) plots.

2. **Add δ to `GrassmannianTracker.snapshot()`** — a 5-line
   addition that calls `phase_discretization(K)` on the
   already-computed K tensor. Now δ joins κ, W, and Δ_F as a
   native training diagnostic.

3. **Add `--ablate-batch-sizes` to `topogpt3-train`** — train
   for 200 steps at each of {8, 16, 32, 64, 128, 256} and dump
   κ, W, Δ_F, δ every 10 steps. ~2 hours on GPU. Tests
   "winding/Δ_F collapse outside [24,128]".

4. **Capture raw token streams in `harness.py`** so post-hoc
   prefix-agreement and BLEU metrics on the noise sweep
   become possible. ~30 lines of plumbing.

These four changes convert "static audit" into "dynamic
diagnosis" and let us actually stress-test the framework's
predictions about phase transitions.

---

## 7. Reproducibility

```
# Static diagnostics
.venv-eval/bin/python eval/diag_static.py

# Noise sweep (CPU, ~5 min, 50 problems, 4 sigmas)
.venv-eval/bin/python eval/noise_sweep.py \
    --sigmas 0,1e-4,1e-3,1e-2 \
    --n-problems 50 \
    --tag v1

# Cross-sigma consistency
.venv-eval/bin/python eval/noise_analysis.py --tag v1

# Temperature sweep (~14 min, 30 problems, 4 configs, 5 samples each)
.venv-eval/bin/python eval/temp_sweep.py \
    --n-problems 30 \
    --n-samples 5 \
    --tag v1 \
    --configs 0.0/0,0.2/40,0.5/40,0.8/40
```

All paths relative to repo root.
