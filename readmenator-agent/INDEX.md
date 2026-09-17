# Index

| File | Purpose | Subsystem | Symbols |
|------|---------|-----------|---------|
| `app.py` | Drop-in entry point that demonstrates how to use the topogpt3 package.  This fil | root | 5 |
| `convert_weights.py` | TopoGPT3 Weight Converter: safetensors -> flat float32 binary.  Usage: python co | root | 2 |
| `convert_weights_minios.py` | Convert TopoGPT3 safetensors weights to float16 binary for MiniOS.  Produces a c | root | 1 |
| `encode_tokens.py` | Tokenize text using GPT-2 BPE and output binary token IDs.  Usage: python tokeni | root | 1 |
| `eval/analyze.py` | Aggregate HumanEval result JSONL files into a summary table.  Reads one or more  | eval | 5 |
| `eval/analyze_results.py` | Analyze a HumanEval JSONL produced by harness.py.  For each failed problem the r | eval | 4 |
| `eval/diag_static.py` | Diagnostico estatico de un checkpoint TopoGPT3 congelado.  Calcula sobre los pes | eval | 5 |
| `eval/governor.py` | Streaming + governance for autoregressive generation.  Two classes that fix two  | eval | 20 |
| `eval/governor_smoke.py` | Smoke test for eval.governor (TokenStream + GenerationGovernor).  Verifies: - To | eval | 7 |
| `eval/harness.py` | Harness for evaluating TopoGPT3 on HumanEval (164 problems).  Faithful to the of | eval | 12 |
| `eval/integration_smoke.py` | End-to-end smoke test of all P0+P1 components working together.  Verifies that ` | eval | 1 |
| `eval/noise_analysis.py` | Analisis post-hoc del noise sweep.  Generaciones del MISMO prompt bajo distintos | eval | 3 |
| `eval/noise_sweep.py` | Barrido de ruido en los pesos espectrales del checkpoint TopoGPT3.  Para cada ni | eval | 4 |
| `eval/repair.py` | Self-repair loop on top of a greedy JSONL.  Takes the failed problems from --inp | eval | 6 |
| `eval/report.py` | Aggregate every JSONL in eval/runs into a final report.  Reads runs from the ori | eval | 6 |
| `eval/samplers.py` | Registry of sampler constructors for the HumanEval harness.  Replaces the hardco | eval | 7 |
| `eval/sandbox.py` | Sandbox for executing model-generated code during HumanEval evaluation.  This mo | eval | 9 |
| `eval/sandbox_smoke.py` | Smoke test for eval.sandbox.  Verifies all four defence layers: L1 (AST pre-chec | eval | 1 |
| `eval/smoke.py` | Smoke test: load the TopoGPT3 checkpoint and produce a small completion.  Used a | eval | 2 |
| `eval/temp_sweep.py` | Barrido de temperatura x top-k sobre HumanEval.  Mide pass@1 en modo greedy (T=0 | eval | 5 |
| `gradio_app.py` | TopoGPT3 Gradio Interface for Hugging Face Spaces.  Drop-in Gradio app exposing  | root | 4 |
| `install.sh` | - | root | 0 |
| `synthetic_dataset.py` | Synthetic Dataset Generator for TopoGPT2.  Generates high-quality code instructi | root | 35 |
| `tests/test_heritage.py` | Advanced-training tests: LoRA/RL/chat modules preserve quaternionic identity. | tests | 9 |
| `tests/test_jlens.py` | - | tests | 51 |
| `tests/test_lens_model.py` | - | tests | 34 |
| `topogpt3.c` | - | root | 128 |
| `topogpt3/__init__.py` | TopoGPT3: complex-valued spectral language model for code.  This package bundles | topogpt3 | 0 |
| `topogpt3/__main__.py` | - | topogpt3 | 1 |
| `topogpt3/api_server.py` | OpenAI-compatible HTTP API server so TopoGPT3 can be used as a backend for codin | topogpt3 | 46 |
| `topogpt3/chat.py` | Chat template + special tokens for TopoGPT3.  Identity preserved: TopoGPT3 keeps | topogpt3 | 7 |
| `topogpt3/continuation.py` | Auto-continuation engine: detects truncated responses and feeds the last incompl | topogpt3 | 5 |
| `topogpt3/convert.py` | Export / convert utilities for TopoGPT3 checkpoints.  TopoGPT3 keeps its own saf | topogpt3 | 3 |
| `topogpt3/eval_toolcall.py` | Tool-call evaluation for TopoGPT3 agents.  Runs TOOLS cases through a generate_f | topogpt3 | 2 |
| `topogpt3/export_chat.py` | Export the real 4-tier curriculum (HF) to chat JSONL for the heritage trainers.  | topogpt3 | 5 |
| `topogpt3/inference.py` | TopoGPT3 inference engine.  Production-grade autoregressive code completion pipe | topogpt3 | 54 |
| `topogpt3/inference_hrm.py` | TopoGPT3.1: Hierarchical Recursive Reasoning Inference Engine.  This module exte | topogpt3 | 76 |
| `topogpt3/jlens.py` | - | topogpt3 | 29 |
| `topogpt3/lens_model.py` | - | topogpt3 | 29 |
| `topogpt3/lora.py` | Native LoRA for TopoGPT3.  Quaternion-safe: in addition to plain nn.Linear, it d | topogpt3 | 12 |
| `topogpt3/model.py` | TopoGPT2: Quaternion-Enhanced Topological Transformer Language Model  Author: Gr | topogpt3 | 188 |
| `topogpt3/rewards.py` | Reward + advantage + loss helpers for TopoGPT3 group-RL.  Adds an *optional* spe | topogpt3 | 9 |
| `topogpt3/rollout.py` | Rollout engine for TopoGPT3 RL self-sampling.  Works with TopoGPT2.generate(toke | topogpt3 | 10 |
| `topogpt3/tools_agent.py` | Code-first tool definitions for TopoGPT3 Agent-RL.  Keeps TopoGPT3 identity: pri | topogpt3 | 2 |
| `topogpt3/train.py` | TopoGPT3: Grassmannian / Berry-Holonomy extension of TopoGPT2  Author: Gris Isco | topogpt3 | 62 |
| `topogpt3/train_agent.py` | Agentic RL for TopoGPT3 (multi-turn Tool-Use).  Rollout: prompt -> generate -> p | topogpt3 | 2 |
| `topogpt3/train_distill.py` | White-box distillation for TopoGPT3.  Teacher: any HF causal LM (e.g. Qwen/StarC | topogpt3 | 1 |
| `topogpt3/train_dpo.py` | DPO for TopoGPT3. Policy + frozen ref share TopoGPT2 quaternion/spectral weights | topogpt3 | 2 |
| `topogpt3/train_grpo.py` | GRPO / CISPO for TopoGPT3.  Group-relative advantages, k3 KL to frozen ref, no C | topogpt3 | 2 |
| `topogpt3/train_lora.py` | SFT with native LoRA for TopoGPT3.  Freezes quaternion/spectral base, trains onl | topogpt3 | 2 |
| `topogpt3/train_ppo.py` | PPO for TopoGPT3.  Critic = frozen TopoGPT2 trunk + fresh Linear value head (qua | topogpt3 | 4 |
| `topogpt3/trainer_utils_topo.py` | Shared training utilities for TopoGPT3 advanced trainers.  Adapted to TopoGPT3 c | topogpt3 | 10 |
| `topogpt3/yarn.py` | YaRN RoPE extrapolation for TopoGPT3.  Preserves the quaternionic/spectral ident | topogpt3 | 3 |
