# TopoGPT3 API Reference

> Generated offline by readmenator: 56 modules, 1222 documented entities, documentation coverage 50.1% (367/732 public items). Deterministic, zero tokens: signatures from source, docs parsed from Google, NumPy, reST, Javadoc/JSDoc/Doxygen, C# XML, and Rustdoc comments.

Navigate: [Interactive architecture and flows](flows.html) | [Architecture and flows (Mermaid)](architecture.md) | [Class hierarchy](classes.md) | [General index](genindex.md) | [Coverage and warnings](COVERAGE.md) | [`api/index.json`](api/index.json) | [HTML browser](index.html)

Languages: c (1), py (53), sh (2)

## Modules

### `.`

| Module | Summary | Types | Callables | Coverage |
|---|---|---|---|---|
| [`app`](modules/app.py.md) | Drop-in entry point that demonstrates how to use the topogpt3 package. | 0 | 4 | 100.0% |
| [`convert_weights`](modules/convert_weights.py.md) | TopoGPT3 Weight Converter: safetensors -> flat float32 binary. | 0 | 2 | 33.3% |
| [`convert_weights_minios`](modules/convert_weights_minios.py.md) | Convert TopoGPT3 safetensors weights to float16 binary for MiniOS. | 0 | 1 | 50.0% |
| [`encode_tokens`](modules/encode_tokens.py.md) | Tokenize text using GPT-2 BPE and output binary token IDs. | 0 | 1 | 50.0% |
| [`gradio_app`](modules/gradio_app.py.md) | TopoGPT3 Gradio Interface for Hugging Face Spaces. | 0 | 4 | 100.0% |
| [`install.sh`](modules/install.sh.md) |  | 0 | 0 | 0.0% |
| [`synthetic_dataset`](modules/synthetic_dataset.py.md) | Synthetic Dataset Generator for TopoGPT2. | 6 | 23 | 43.3% |
| [`topogpt3.c`](modules/topogpt3.c.md) |  | 3 | 65 | 8.7% |

### `eval`

| Module | Summary | Types | Callables | Coverage |
|---|---|---|---|---|
| [`eval.analyze`](modules/eval.analyze.py.md) | Aggregate HumanEval result JSONL files into a summary table. | 0 | 5 | 50.0% |
| [`eval.analyze_results`](modules/eval.analyze_results.py.md) | Analyze a HumanEval JSONL produced by harness.py. | 0 | 4 | 20.0% |
| [`eval.diag_static`](modules/eval.diag_static.py.md) | Diagnostico estatico de un checkpoint TopoGPT3 congelado. | 0 | 5 | 50.0% |
| [`eval.governor`](modules/eval.governor.py.md) | Streaming + governance for autoregressive generation. | 4 | 11 | 62.5% |
| [`eval.governor_smoke`](modules/eval.governor_smoke.py.md) | Smoke test for eval.governor (TokenStream + GenerationGovernor). | 0 | 5 | 16.7% |
| [`eval.harness`](modules/eval.harness.py.md) | Harness for evaluating TopoGPT3 on HumanEval (164 problems). | 1 | 11 | 61.5% |
| [`eval.integration_smoke`](modules/eval.integration_smoke.py.md) | End-to-end smoke test of all P0+P1 components working together. | 0 | 1 | 50.0% |
| [`eval.noise_analysis`](modules/eval.noise_analysis.py.md) | Analisis post-hoc del noise sweep. | 0 | 2 | 66.7% |
| [`eval.noise_sweep`](modules/eval.noise_sweep.py.md) | Barrido de ruido en los pesos espectrales del checkpoint TopoGPT3. | 0 | 4 | 60.0% |
| [`eval.repair`](modules/eval.repair.py.md) | Self-repair loop on top of a greedy JSONL. | 0 | 5 | 16.7% |
| [`eval.report`](modules/eval.report.py.md) | Aggregate every JSONL in eval/runs into a final report. | 0 | 6 | 14.3% |
| [`eval.samplers`](modules/eval.samplers.py.md) | Registry of sampler constructors for the HumanEval harness. | 0 | 3 | 75.0% |
| [`eval.sandbox`](modules/eval.sandbox.py.md) | Sandbox for executing model-generated code during HumanEval evaluation. | 1 | 3 | 80.0% |
| [`eval.sandbox_smoke`](modules/eval.sandbox_smoke.py.md) | Smoke test for eval.sandbox. | 0 | 1 | 50.0% |
| [`eval.smoke`](modules/eval.smoke.py.md) | Smoke test: load the TopoGPT3 checkpoint and produce a small completion. | 0 | 2 | 33.3% |
| [`eval.tasks`](modules/eval.tasks.py.md) | Generic task eval: JSONL cases + safe verifiers. | 0 | 12 | 7.7% |
| [`eval.temp_sweep`](modules/eval.temp_sweep.py.md) | Barrido de temperatura x top-k sobre HumanEval. | 0 | 5 | 16.7% |

### `scripts`

| Module | Summary | Types | Callables | Coverage |
|---|---|---|---|---|
| [`scripts/serve_fallback.sh`](modules/scripts.serve_fallback.sh.md) | Serve TopoGPT3 (code) + TopoExploit (red-team) as OpenAI-compatible fallback endpoints for LazyOwn / TopoSwarm. | 0 | 1 | 50.0% |

### `topogpt3`

| Module | Summary | Types | Callables | Coverage |
|---|---|---|---|---|
| [`topogpt3`](modules/topogpt3.__init__.py.md) | TopoGPT3: complex-valued spectral language model for code. | 0 | 0 | 100.0% |
| [`topogpt3.__main__`](modules/topogpt3.__main__.py.md) |  | 0 | 1 | 50.0% |
| [`topogpt3.api_server`](modules/topogpt3.api_server.py.md) | OpenAI-compatible HTTP API server so TopoGPT3 can be used as a backend for coding agents (e.g. | 9 | 17 | 3.7% |
| [`topogpt3.chat`](modules/topogpt3.chat.py.md) | Chat template + special tokens for TopoGPT3. | 0 | 6 | 57.1% |
| [`topogpt3.checkpoint_meta`](modules/topogpt3.checkpoint_meta.py.md) | Checkpoint architecture discovery shared by inference, API and trainers. | 0 | 5 | 66.7% |
| [`topogpt3.continuation`](modules/topogpt3.continuation.py.md) | Auto-continuation engine: detects truncated responses and feeds the last incomplete lines back so the model can resume where it left off. | 0 | 3 | 100.0% |
| [`topogpt3.convert`](modules/topogpt3.convert.py.md) | Export / convert utilities for TopoGPT3 checkpoints. | 0 | 3 | 25.0% |
| [`topogpt3.eval_toolcall`](modules/topogpt3.eval_toolcall.py.md) | Tool-call evaluation for TopoGPT3 agents. | 0 | 2 | 33.3% |
| [`topogpt3.export_chat`](modules/topogpt3.export_chat.py.md) | Export the real 4-tier curriculum (HF) to chat JSONL for the heritage trainers. | 0 | 1 | 50.0% |
| [`topogpt3.fallback`](modules/topogpt3.fallback.py.md) | Local-fallback profiles, apt_chain tooling and deterministic reranking. | 1 | 10 | 41.7% |
| [`topogpt3.inference`](modules/topogpt3.inference.py.md) | TopoGPT3 inference engine. | 18 | 36 | 80.0% |
| [`topogpt3.inference_hrm`](modules/topogpt3.inference_hrm.py.md) | TopoGPT3.1: Hierarchical Recursive Reasoning Inference Engine. | 25 | 48 | 79.7% |
| [`topogpt3.jlens`](modules/topogpt3.jlens.py.md) |  | 5 | 13 | 89.5% |
| [`topogpt3.lens_model`](modules/topogpt3.lens_model.py.md) |  | 4 | 19 | 59.1% |
| [`topogpt3.lora`](modules/topogpt3.lora.py.md) | Native LoRA for TopoGPT3. | 1 | 9 | 36.4% |
| [`topogpt3.model`](modules/topogpt3.model.py.md) | TopoGPT2: Quaternion-Enhanced Topological Transformer Language Model | 32 | 112 | 54.2% |
| [`topogpt3.rewards`](modules/topogpt3.rewards.py.md) | Reward + advantage + loss helpers for TopoGPT3 group-RL. | 0 | 12 | 53.8% |
| [`topogpt3.rollout`](modules/topogpt3.rollout.py.md) | Rollout engine for TopoGPT3 RL self-sampling. | 3 | 7 | 9.1% |
| [`topogpt3.structured_output`](modules/topogpt3.structured_output.py.md) | Constrained decoding for the TopoGPT3 OpenAI-compatible server. | 3 | 10 | 64.3% |
| [`topogpt3.tokenizer_tools`](modules/topogpt3.tokenizer_tools.py.md) | Tokenizer efficiency toolkit. | 0 | 5 | 66.7% |
| [`topogpt3.tools_agent`](modules/topogpt3.tools_agent.py.md) | Code-first tool definitions for TopoGPT3 Agent-RL. | 0 | 2 | 66.7% |
| [`topogpt3.train`](modules/topogpt3.train.py.md) | TopoGPT3: Grassmannian / Berry-Holonomy extension of TopoGPT2 | 7 | 28 | 47.2% |
| [`topogpt3.train_agent`](modules/topogpt3.train_agent.py.md) | Agentic RL for TopoGPT3 (multi-turn Tool-Use). | 0 | 2 | 66.7% |
| [`topogpt3.train_distill`](modules/topogpt3.train_distill.py.md) | White-box distillation for TopoGPT3. | 0 | 1 | 50.0% |
| [`topogpt3.train_dpo`](modules/topogpt3.train_dpo.py.md) | DPO for TopoGPT3. | 0 | 2 | 33.3% |
| [`topogpt3.train_grpo`](modules/topogpt3.train_grpo.py.md) | GRPO / CISPO for TopoGPT3. | 0 | 1 | 50.0% |
| [`topogpt3.train_lora`](modules/topogpt3.train_lora.py.md) | SFT with native LoRA for TopoGPT3. | 0 | 2 | 33.3% |
| [`topogpt3.train_ppo`](modules/topogpt3.train_ppo.py.md) | PPO for TopoGPT3. | 1 | 3 | 20.0% |
| [`topogpt3.trainer_utils_topo`](modules/topogpt3.trainer_utils_topo.py.md) | Shared training utilities for TopoGPT3 advanced trainers. | 1 | 7 | 22.2% |
| [`topogpt3.yarn`](modules/topogpt3.yarn.py.md) | YaRN RoPE extrapolation for TopoGPT3. | 1 | 2 | 75.0% |
