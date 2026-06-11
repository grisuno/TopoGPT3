# Plan: HumanEval evaluation of TopoGPT3 checkpoint

## Status
Blocked: terminal commands are being auto-denied by the user's safety layer
(heuristic on pip/rm/venv/keywords). Cannot run the actual benchmark until
the user unblocks.

## Artefacts ready in /home/grisun0/src_note/py/TopoGPT3

- `checkpoints_topogpt3/last/`
  - `model.safetensors`  149,744,752 B  sha256 ab37bc71ff2bb729038e04ba57e161b1c1f1bda2dc792b7669cc3b6a02a57cd0
  - `state.json`         1,790 B         sha256 203a544bd73d9a1594ba88f926f9ea9653976cf85b2ebdf9073be351d09679c0
  - `README.md`          13,512 B
- Real architecture (from safetensors probe):
  - scale = "small", d_model=256, n_heads=8, d_head=32, n_layers=6, max_seq=256
  - n_kv_heads = k_proj_out / d_head = 64 / 32 = 2  (GQA)
  - vocab = 50257 (gpt2 BPE)
  - 6 layers each with `topo_brain.shared_expert` (spectral quaternion MLP)
  - MoE: 4 experts per layer, expert dim 344
  - 447 tensors, 37,422,246 params total  (README claimed 24.5M, this is 37M)
  - Per-layer learned `attn.temperature` scalar
  - global_step = 51,712
  - completed_tiers = []   (no formal tier completion; trained as a single mix)

## Code ready to run
- `eval/smoke.py`   load checkpoint, generate one prompt, run standard + HRM
- `eval/harness.py` HumanEval pass@k with shared ModelLoader (one model load
                     for all 164 problems x k samples), proper candidate
                     extraction, safe `exec` sandbox (no I/O, no subprocess,
                     only function definitions)
- `eval/analyze.py` aggregate JSONL runs into pass@1, pass@k, latency,
                     throughput, error classification

## Plan once terminal is unblocked

1. **Smoke test** — confirm model loads and generates (standard + HRM)
   - `python eval/smoke.py` (timeout 180s, GPU)

2. **Phase 1: pass@1, T=0.0, greedy** (single sample per problem)
   - `python eval/harness.py --out eval/runs/greedy.jsonl --temperature 0.0 --top-k 0 --n-samples 1 --max-new-tokens 512`
   - Expected wall clock on RTX 2060: ~6-15 min for 164 problems
   - 1 generation per problem, max_new=512 tokens

3. **Phase 2: pass@1, T=0.2** (low-temp sampling, single sample)
   - `python eval/harness.py --out eval/runs/t02.jsonl --temperature 0.2 --top-k 40 --n-samples 1`

4. **Phase 3: pass@10, T=0.8** (10 samples, top-k=40, high temp)
   - To keep wall clock reasonable: cap at 100 problems
   - `python eval/harness.py --out eval/runs/pass10.jsonl --temperature 0.8 --top-k 40 --n-samples 10 --limit 100`

5. **Phase 4: pass@20, T=0.8** (20 samples)
   - `python eval/harness.py --out eval/runs/pass20.jsonl --temperature 0.8 --top-k 40 --n-samples 20 --limit 50`

6. **Phase 5: HRM pass@1** (compare HRM vs standard)
   - `python eval/harness.py --mode hrm --out eval/runs/hrm.jsonl --temperature 0.0 --n-samples 1`
   - HRM is slower per token; estimate ~2-3x standard latency

7. **Self-repair loop** (Fase 4 del plan del usuario)
   - Take failing problems from `greedy.jsonl`
   - Build a "rejection-feedback" prompt: previous attempt + traceback
   - Re-prompt the model with that, N=3 rounds
   - Measure pass@1_with_repair

8. **Aggregate + classify errors** (Fase 6)
   - `python eval/analyze.py --md eval/runs/*.jsonl`
   - Classify: syntax, undefined_name, off_by_one, edge_case, wrong_output,
     type_error, runner_crash

9. **Write REPORT.md** with honest numbers, including:
   - The 24.5M vs 37M params discrepancy
   - Wall-clock cost, throughput, GPU memory
   - Failure modes breakdown
   - Comparison standard vs HRM
   - Note that HumanEval is saturated / contamination risk

## What I will NOT do
- Fabricate numbers. If something fails (CUDA still broken, checkpoint
  corrupt, harness crash) I will report that, not invent a pass rate.
- Skip the actual execution. The user explicitly said "no solo hagas lo
  minimo" — that means run it for real.
- Re-train. The checkpoint is what it is.

## What I need from the user
- Unblock terminal so I can run `python eval/smoke.py` and the harness.
  The current auto-deny is triggered by anything mentioning pip/venv/rm
  even in argument strings; a simple `python -c "import torch; ..."`
  was denied. Once unblocked, the actual eval should take < 2 hours of
  wall clock total.
