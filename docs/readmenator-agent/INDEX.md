# Index

| File | Purpose | Subsystem | Symbols | Used by |
|------|---------|-----------|---------|---------|
| `app.py` | Drop-in entry point that demonstrates how to use the topogpt3 package. | root | 5 | 0 |
| `convert_weights.py` | TopoGPT3 Weight Converter: safetensors -> flat float32 binary. | root | 2 | 0 |
| `convert_weights_minios.py` | Convert TopoGPT3 safetensors weights to float16 binary for MiniOS. | root | 1 | 0 |
| `encode_tokens.py` | Tokenize text using GPT-2 BPE and output binary token IDs. | root | 1 | 0 |
| `eval/analyze.py` | Aggregate HumanEval result JSONL files into a summary table. | eval | 5 | 0 |
| `eval/analyze_results.py` | Analyze a HumanEval JSONL produced by harness.py. | eval | 4 | 0 |
| `eval/diag_static.py` | Diagnostico estatico de un checkpoint TopoGPT3 congelado. | eval | 5 | 0 |
| `eval/governor.py` | Streaming + governance for autoregressive generation. | eval | 20 | 1 |
| `eval/governor_smoke.py` | Smoke test for eval.governor (TokenStream + GenerationGovernor). | eval | 7 | 0 |
| `eval/harness.py` | Harness for evaluating TopoGPT3 on HumanEval (164 problems). | eval | 12 | 3 |
| `eval/integration_smoke.py` | End-to-end smoke test of all P0+P1 components working together. | eval | 1 | 0 |
| `eval/noise_analysis.py` | Analisis post-hoc del noise sweep. | eval | 3 | 0 |
| `eval/noise_sweep.py` | Barrido de ruido en los pesos espectrales del checkpoint TopoGPT3. | eval | 4 | 1 |
| `eval/repair.py` | Self-repair loop on top of a greedy JSONL. | eval | 6 | 0 |
| `eval/report.py` | Aggregate every JSONL in eval/runs into a final report. | eval | 6 | 0 |
| `eval/samplers.py` | Registry of sampler constructors for the HumanEval harness. | eval | 7 | 1 |
| `eval/sandbox.py` | Sandbox for executing model-generated code during HumanEval evaluation. | eval | 9 | 3 |
| `eval/sandbox_smoke.py` | Smoke test for eval.sandbox. | eval | 1 | 0 |
| `eval/smoke.py` | Smoke test: load the TopoGPT3 checkpoint and produce a small completion. | eval | 2 | 0 |
| `eval/temp_sweep.py` | Barrido de temperatura x top-k sobre HumanEval. | eval | 5 | 0 |
| `gradio_app.py` | TopoGPT3 Gradio Interface for Hugging Face Spaces. | root | 4 | 0 |
| `install.sh` | - | root | 0 | 0 |
| `synthetic_dataset.py` | Synthetic Dataset Generator for TopoGPT2. | root | 35 | 1 |
| `tests/test_heritage.py` | Advanced-training tests: LoRA/RL/chat modules preserve quaternionic identity. | tests | 9 | 0 |
| `tests/test_jlens.py` | TestValidPositionMask: Feature: valid_position_mask excludes attention-sink and final positions. | tests | 51 | 0 |
| `tests/test_lens_model.py` | TestTopoGPT3LensConfig: Feature: TopoGPT3LensConfig provides centralized adapter configuration. | tests | 34 | 0 |
| `topogpt3.c` | FILE: topogpt3 -p "prompt" [-n N] [-t T]   Headless mode topogpt3 -i... | root | 128 | 2 |
| `topogpt3/__init__.py` | TopoGPT3: complex-valued spectral language model for code. | topogpt3 | 0 | 7 |
| `topogpt3/__main__.py` | main: TopoGPT3 entry point. | topogpt3 | 1 | 0 |
| `topogpt3/api_server.py` | OpenAI-compatible HTTP API server so TopoGPT3 can be used as a backend for coding agents (e.g. | topogpt3 | 46 | 1 |
| `topogpt3/chat.py` | Chat template + special tokens for TopoGPT3. | topogpt3 | 7 | 6 |
| `topogpt3/continuation.py` | Auto-continuation engine: detects truncated responses and feeds the last incomplete lines back... | topogpt3 | 5 | 3 |
| `topogpt3/convert.py` | Export / convert utilities for TopoGPT3 checkpoints. | topogpt3 | 3 | 1 |
| `topogpt3/eval_toolcall.py` | Tool-call evaluation for TopoGPT3 agents. | topogpt3 | 2 | 2 |
| `topogpt3/export_chat.py` | Export the real 4-tier curriculum (HF) to chat JSONL for the heritage trainers. | topogpt3 | 5 | 1 |
| `topogpt3/inference.py` | TopoGPT3 inference engine. | topogpt3 | 54 | 2 |
| `topogpt3/inference_hrm.py` | TopoGPT3.1: Hierarchical Recursive Reasoning Inference Engine. | topogpt3 | 76 | 2 |
| `topogpt3/jlens.py` | TopoGPT3JLensFitConfig: Centralized configuration for Jacobian lens fitting. | topogpt3 | 29 | 4 |
| `topogpt3/lens_model.py` | LensModel: What the lens needs from a model. | topogpt3 | 29 | 5 |
| `topogpt3/lora.py` | Native LoRA for TopoGPT3. | topogpt3 | 12 | 4 |
| `topogpt3/model.py` | TopoGPT2: Quaternion-Enhanced Topological Transformer Language Model  Author: Gris Iscomeback... | topogpt3 | 188 | 16 |
| `topogpt3/rewards.py` | Reward + advantage + loss helpers for TopoGPT3 group-RL. | topogpt3 | 9 | 7 |
| `topogpt3/rollout.py` | Rollout engine for TopoGPT3 RL self-sampling. | topogpt3 | 10 | 4 |
| `topogpt3/tools_agent.py` | Code-first tool definitions for TopoGPT3 Agent-RL. | topogpt3 | 2 | 4 |
| `topogpt3/train.py` | TopoGPT3: Grassmannian / Berry-Holonomy extension of TopoGPT2  Author: Gris Iscomeback License... | topogpt3 | 62 | 4 |
| `topogpt3/train_agent.py` | Agentic RL for TopoGPT3 (multi-turn Tool-Use). | topogpt3 | 2 | 1 |
| `topogpt3/train_distill.py` | White-box distillation for TopoGPT3. | topogpt3 | 1 | 1 |
| `topogpt3/train_dpo.py` | DPO for TopoGPT3. | topogpt3 | 2 | 1 |
| `topogpt3/train_grpo.py` | GRPO / CISPO for TopoGPT3. | topogpt3 | 2 | 1 |
| `topogpt3/train_lora.py` | SFT with native LoRA for TopoGPT3. | topogpt3 | 2 | 1 |
| `topogpt3/train_ppo.py` | PPO for TopoGPT3. | topogpt3 | 4 | 1 |
| `topogpt3/trainer_utils_topo.py` | Shared training utilities for TopoGPT3 advanced trainers. | topogpt3 | 10 | 7 |
| `topogpt3/yarn.py` | YaRN RoPE extrapolation for TopoGPT3. | topogpt3 | 3 | 3 |
