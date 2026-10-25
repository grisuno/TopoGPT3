# GraphRAG Community Reports

Entities: 1153 | Relationships: 3274 | Communities: 7 | Themes: 3 | Text units: 1029

Query with `readmenator . ask "<question>"` (local: BM25 + Personalized PageRank; global: map-reduce over these reports) or the MCP tool `readmenator.graphrag`.

## Project overview (`root`, root, rating 7.0)

55 files in 7 communities and 3 themes. Highest-impact communities: topogpt3: model (7.0), eval (4.8), topogpt3: lora (4.3). God nodes: topogpt3/model.py, topogpt3/__init__.py, topogpt3/__main__.py, topogpt3/api_server.py, tests/test_heritage.py.

- [topogpt3: model] rating 7.0: `topogpt3/model.py` ranks 1 by PageRank, 20 importers, 188 symbols: TopoGPT2: Quaternion-Enhanced Topological Transformer Language Model  Author: Gris Iscomeback Email: grisiscomeback@gmail.com License: GPL v3  Mejoras sobre topogpt.py: - Álgebra de cuaterniones completa (QuaternionLinear...
- [eval] rating 4.8: `topogpt3/__init__.py` ranks 1 by PageRank, 7 importers, 0 symbols: TopoGPT3: complex-valued spectral language model for code.
- [topogpt3: lora] rating 4.3: `topogpt3/trainer_utils_topo.py` ranks 1 by PageRank, 7 importers, 10 symbols: Shared training utilities for TopoGPT3 advanced trainers.
- [topogpt3: sandbox] rating 4.0: `topogpt3/yarn.py` ranks 1 by PageRank, 3 importers, 3 symbols: YaRN RoPE extrapolation for TopoGPT3.
- [topogpt3: jlens] rating 2.0: `topogpt3/lens_model.py` ranks 1 by PageRank, 6 importers, 29 symbols: LensModel: What the lens needs from a model.
- [unassigned files] rating 1.9: `convert_weights.py` ranks 1 by PageRank, 0 importers, 2 symbols: TopoGPT3 Weight Converter: safetensors -> flat float32 binary.
- [root] rating 1.1: `topogpt3.c` ranks 1 by PageRank, 2 importers, 128 symbols: FILE: topogpt3 -p "prompt" [-n N] [-t T]   Headless mode topogpt3 -i                          Interactive mode topogpt3 -f file.txt                 Read prompt from file  #pragma GCC diagnostic ignored "-Wunused-function" #ifdef...
- Key entities: file:topogpt3/model.py, file:topogpt3/inference_hrm.py, file:topogpt3/inference.py, file:eval/harness.py, file:topogpt3/trainer_utils_topo.py, file:topogpt3/rollout.py
- Children: t0, t1, t2
- Root rating = highest community rating.

## topogpt3: model + eval +3 (`t0`, theme, rating 7.0)

Theme of 5 communities and 44 files: topogpt3: model (10 files, rating 7.0); eval (11 files, rating 4.8); topogpt3: lora (12 files, rating 4.3); topogpt3: sandbox (7 files, rating 4.0); topogpt3: jlens (4 files, rating 2.0).

- [topogpt3: model] `topogpt3/model.py` ranks 1 by PageRank, 20 importers, 188 symbols: TopoGPT2: Quaternion-Enhanced Topological Transformer Language Model  Author: Gris Iscomeback Email: grisiscomeback@gmail.com License: GPL v3  Mejoras sobre topogpt.py: - Álgebra de cuaterniones completa (QuaternionLinear...
- [topogpt3: model] `topogpt3/continuation.py` ranks 2 by PageRank, 3 importers, 5 symbols: Auto-continuation engine: detects truncated responses and feeds the last incomplete lines back so the model can resume where it left off.
- [eval] `topogpt3/__init__.py` ranks 1 by PageRank, 7 importers, 0 symbols: TopoGPT3: complex-valued spectral language model for code.
- [eval] `eval/harness.py` ranks 2 by PageRank, 3 importers, 12 symbols: Harness for evaluating TopoGPT3 on HumanEval (164 problems).
- [topogpt3: lora] `topogpt3/trainer_utils_topo.py` ranks 1 by PageRank, 7 importers, 10 symbols: Shared training utilities for TopoGPT3 advanced trainers.
- [topogpt3: lora] `topogpt3/rewards.py` ranks 2 by PageRank, 7 importers, 9 symbols: Reward + advantage + loss helpers for TopoGPT3 group-RL.
- [topogpt3: sandbox] `topogpt3/yarn.py` ranks 1 by PageRank, 3 importers, 3 symbols: YaRN RoPE extrapolation for TopoGPT3.
- [topogpt3: sandbox] `topogpt3/chat.py` ranks 2 by PageRank, 9 importers, 7 symbols: Chat template + special tokens for TopoGPT3.
- Key entities: file:topogpt3/model.py, file:topogpt3/inference_hrm.py, file:topogpt3/inference.py, file:eval/harness.py, file:topogpt3/trainer_utils_topo.py, file:topogpt3/rollout.py, file:eval/sandbox.py, file:topogpt3/chat.py
- Children: c2, c1, c0, c3, c4
- Theme rating = highest child community rating.

## unassigned files (`t1`, theme, rating 1.9)

Theme of 1 communities and 8 files: unassigned files (8 files, rating 1.9).

- [unassigned files] `convert_weights.py` ranks 1 by PageRank, 0 importers, 2 symbols: TopoGPT3 Weight Converter: safetensors -> flat float32 binary.
- [unassigned files] `convert_weights_minios.py` ranks 2 by PageRank, 0 importers, 1 symbols: Convert TopoGPT3 safetensors weights to float16 binary for MiniOS.
- Key entities: file:eval/report.py, file:eval/noise_analysis.py
- Children: c6
- Theme rating = highest child community rating.

## root (`t2`, theme, rating 1.1)

Theme of 1 communities and 3 files: root (3 files, rating 1.1).

- [root] `topogpt3.c` ranks 1 by PageRank, 2 importers, 128 symbols: FILE: topogpt3 -p "prompt" [-n N] [-t T]   Headless mode topogpt3 -i                          Interactive mode topogpt3 -f file.txt                 Read prompt from file  #pragma GCC diagnostic ignored "-Wunused-function" #ifdef...
- [root] `app.py` ranks 2 by PageRank, 0 importers, 5 symbols: Drop-in entry point that demonstrates how to use the topogpt3 package.
- Key entities: file:topogpt3.c, file:gradio_app.py
- Children: c5
- Theme rating = highest child community rating.

## topogpt3: model (`c2`, community, rating 7.0)

10 files under topogpt3 (py 10), mostly utility. Core file topogpt3/model.py (PageRank 0.0991, imported by 20 files): TopoGPT2: Quaternion-Enhanced Topological Transformer Language Model  Author: Gris Iscomeback Email: grisiscomeback@gmail.com License: GPL v3  Mejoras sobre topogpt.py: - Álgebra de cuaterniones completa (QuaternionLinear... Key abstractions: TopoGPT2Config, QuaternionOps, QuaternionLinear, QuaternionSpectralLayer, SpectralAutoencoder, QuaternionTorusBrain. Depends on topogpt3: sandbox (3), eval (1). Used by topogpt3: lora (11), eval (4), topogpt3: jlens (4).

- `topogpt3/model.py` ranks 1 by PageRank, 20 importers, 188 symbols: TopoGPT2: Quaternion-Enhanced Topological Transformer Language Model  Author: Gris Iscomeback Email: grisiscomeback@gmail.com License: GPL v3  Mejoras sobre topogpt.py: - Álgebra de cuaterniones completa (QuaternionLinear...
- `topogpt3/continuation.py` ranks 2 by PageRank, 3 importers, 5 symbols: Auto-continuation engine: detects truncated responses and feeds the last incomplete lines back so the model can resume where it left off.
- `synthetic_dataset.py` ranks 3 by PageRank, 1 importers, 35 symbols: Synthetic Dataset Generator for TopoGPT2.
- Hotspot `topogpt3/model.py`: 188 symbols, 50 connections (score 1.00).
- Hotspot `topogpt3/api_server.py`: 50 symbols, 41 connections (score 0.60).
- 5 layer violations, e.g. test_structured_output.py (testing) -> api_server.py (presentation).
- Taint: 5 paths reach this group via eval.
- Dataflow: 4 INFERRED issues (first: UNCHECKED_ALLOC in main).
- Key entities: file:topogpt3/model.py, file:topogpt3/inference_hrm.py, file:topogpt3/train.py, file:topogpt3/api_server.py, file:synthetic_dataset.py, file:tests/test_structured_output.py, file:topogpt3/structured_output.py, sym:topogpt3/inference_hrm.py::execute@1239
- Rating 7.0/10 = 7 x PageRank share 1.00 + 3 x risk 0.00. Internal imports: 18.

## eval (`c1`, community, rating 4.8)

11 files under eval (py 11), mostly utility. Core file topogpt3/__init__.py (PageRank 0.0582, imported by 7 files): TopoGPT3: complex-valued spectral language model for code. Key abstractions: ModelLoader, load_humaneval, build_prompt, extract_candidate, run_one_test, run_one_test_sandboxed. Depends on topogpt3: sandbox (5), topogpt3: lora (4), topogpt3: model (4). Used by topogpt3: lora (1), topogpt3: model (1).

- `topogpt3/__init__.py` ranks 1 by PageRank, 7 importers, 0 symbols: TopoGPT3: complex-valued spectral language model for code.
- `eval/harness.py` ranks 2 by PageRank, 3 importers, 12 symbols: Harness for evaluating TopoGPT3 on HumanEval (164 problems).
- `eval/samplers.py` ranks 3 by PageRank, 2 importers, 7 symbols: Registry of sampler constructors for the HumanEval harness.
- Hotspot `topogpt3/__init__.py`: 0 symbols, 36 connections (score 0.43).
- Hotspot `eval/harness.py`: 12 symbols, 31 connections (score 0.40).
- Taint: 4 paths reach this group via eval.
- Dataflow: 1 INFERRED issues (first: UNCHECKED_ALLOC in main).
- Surprising bridge: governor.py <-> sandbox_smoke.py (5 hops across communities).
- Key entities: file:topogpt3/inference.py, file:eval/harness.py, file:eval/governor.py, sym:topogpt3/inference.py::execute@571, file:topogpt3/__init__.py, file:eval/repair.py, file:eval/noise_sweep.py, file:eval/temp_sweep.py
- Rating 4.8/10 = 7 x PageRank share 0.68 + 3 x risk 0.00. Internal imports: 14.

## topogpt3: lora (`c0`, community, rating 4.3)

12 files under topogpt3 (py 12), mostly utility. Core file topogpt3/trainer_utils_topo.py (PageRank 0.0273, imported by 7 files): Shared training utilities for TopoGPT3 advanced trainers. Key abstractions: SkipBatchSampler, Logger, is_main_process, get_lr, setup_seed, init_distributed_mode. Depends on topogpt3: model (11), topogpt3: sandbox (2), topogpt3: jlens (2). Used by eval (4), topogpt3: sandbox (3).

- `topogpt3/trainer_utils_topo.py` ranks 1 by PageRank, 7 importers, 10 symbols: Shared training utilities for TopoGPT3 advanced trainers.
- `topogpt3/rewards.py` ranks 2 by PageRank, 7 importers, 9 symbols: Reward + advantage + loss helpers for TopoGPT3 group-RL.
- `topogpt3/lora.py` ranks 3 by PageRank, 4 importers, 12 symbols: Native LoRA for TopoGPT3.
- Hotspot `topogpt3/__main__.py`: 1 symbols, 30 connections (score 0.36).
- Hotspot `topogpt3/train_agent.py`: 2 symbols, 23 connections (score 0.28).
- Taint: 4 paths reach this group via eval.
- Key entities: file:topogpt3/trainer_utils_topo.py, file:topogpt3/rollout.py, file:topogpt3/lora.py, file:topogpt3/train_agent.py, file:topogpt3/train_ppo.py, file:topogpt3/rewards.py, file:topogpt3/train_grpo.py, file:topogpt3/train_dpo.py
- Rating 4.3/10 = 7 x PageRank share 0.61 + 3 x risk 0.00. Internal imports: 22.

## topogpt3: sandbox (`c3`, community, rating 4.0)

7 files under topogpt3 (py 7), mostly utility. Core file topogpt3/yarn.py (PageRank 0.0419, imported by 3 files): YaRN RoPE extrapolation for TopoGPT3. Key abstractions: YaRNConfig, yarn_scale_inv_freq, apply_yarn_to_rope, pre_processing_chat, post_processing_chat, apply_chat_template. Depends on topogpt3: lora (3), topogpt3: model (2). Used by eval (5), topogpt3: model (3), topogpt3: lora (2).

- `topogpt3/yarn.py` ranks 1 by PageRank, 3 importers, 3 symbols: YaRN RoPE extrapolation for TopoGPT3.
- `topogpt3/chat.py` ranks 2 by PageRank, 9 importers, 7 symbols: Chat template + special tokens for TopoGPT3.
- `eval/sandbox.py` ranks 3 by PageRank, 3 importers, 9 symbols: Sandbox for executing model-generated code during HumanEval evaluation.
- Hotspot `tests/test_heritage.py`: 9 symbols, 20 connections (score 0.26).
- Hotspot `topogpt3/tools_agent.py`: 2 symbols, 16 connections (score 0.20).
- Taint: 5 paths reach this group via eval.
- Surprising bridge: governor.py <-> sandbox_smoke.py (5 hops across communities).
- Key entities: file:eval/sandbox.py, file:topogpt3/chat.py, file:tests/test_heritage.py, file:topogpt3/tools_agent.py, file:topogpt3/yarn.py, file:topogpt3/eval_toolcall.py, sym:topogpt3/chat.py::apply_chat_template@71, sym:tests/test_heritage.py::test_dpo_grpo_losses_finite@76
- Rating 4.0/10 = 7 x PageRank share 0.58 + 3 x risk 0.00. Internal imports: 11.

## topogpt3: jlens (`c4`, community, rating 2.0)

4 files under topogpt3 (py 4), mostly testing. Core file topogpt3/lens_model.py (PageRank 0.0374, imported by 6 files): LensModel: What the lens needs from a model. Key abstractions: LensModel, TopoGPT3LensConfig, TopoGPT3LensModel, TinyDecoder, encode, forward. Depends on topogpt3: model (4). Used by topogpt3: lora (2), eval (2).

- `topogpt3/lens_model.py` ranks 1 by PageRank, 6 importers, 29 symbols: LensModel: What the lens needs from a model.
- `topogpt3/jlens.py` ranks 2 by PageRank, 7 importers, 29 symbols: TopoGPT3JLensFitConfig: Centralized configuration for Jacobian lens fitting.
- `tests/test_jlens.py` ranks 3 by PageRank, 0 importers, 51 symbols: TestValidPositionMask: Feature: valid_position_mask excludes attention-sink and final positions.
- Hotspot `topogpt3/jlens.py`: 29 symbols, 23 connections (score 0.34).
- Hotspot `topogpt3/lens_model.py`: 29 symbols, 22 connections (score 0.33).
- Taint: 2 paths reach this group via eval.
- Surprising bridge: sandbox_smoke.py <-> test_jlens.py (5 hops across communities).
- Key entities: file:tests/test_jlens.py, file:topogpt3/lens_model.py, file:topogpt3/jlens.py, file:tests/test_lens_model.py, sym:topogpt3/jlens.py::fit@291, sym:topogpt3/jlens.py::jacobian_for_prompt@187, sym:topogpt3/lens_model.py::TinyDecoder@306, sym:topogpt3/lens_model.py::TopoGPT3LensModel@161
- Rating 2.0/10 = 7 x PageRank share 0.28 + 3 x risk 0.00. Internal imports: 9.

## unassigned files (`c6`, community, rating 1.9)

8 files under eval (py 7, sh 1), mostly utility. Core file convert_weights.py (PageRank 0.0094, imported by 0 files): TopoGPT3 Weight Converter: safetensors -> flat float32 binary. Key abstractions: convert, main, main, main, pass_at_k, classify_error.

- `convert_weights.py` ranks 1 by PageRank, 0 importers, 2 symbols: TopoGPT3 Weight Converter: safetensors -> flat float32 binary.
- `convert_weights_minios.py` ranks 2 by PageRank, 0 importers, 1 symbols: Convert TopoGPT3 safetensors weights to float16 binary for MiniOS.
- `encode_tokens.py` ranks 3 by PageRank, 0 importers, 1 symbols: Tokenize text using GPT-2 BPE and output binary token IDs.
- Hotspot `eval/report.py`: 6 symbols, 9 connections (score 0.12).
- Hotspot `eval/noise_analysis.py`: 3 symbols, 9 connections (score 0.11).
- Key entities: file:eval/report.py, file:eval/noise_analysis.py, file:eval/analyze.py, file:eval/analyze_results.py, file:convert_weights.py, file:convert_weights_minios.py, file:encode_tokens.py, sym:eval/analyze.py::summarize@61
- Rating 1.9/10 = 7 x PageRank share 0.27 + 3 x risk 0.00. Internal imports: 0.

## root (`c5`, community, rating 1.1)

3 files under root (py 2, c 1), mostly utility. Core file topogpt3.c (PageRank 0.0253, imported by 2 files): FILE: topogpt3 -p "prompt" [-n N] [-t T]   Headless mode topogpt3 -i                          Interactive mode topogpt3 -f file.txt                 Read prompt from file  #pragma GCC diagnostic ignored "-Wunused-function" #ifdef... Key abstractions: FILE, LayerWeights, ModelWeights, stdin, stdout, stderr.

- `topogpt3.c` ranks 1 by PageRank, 2 importers, 128 symbols: FILE: topogpt3 -p "prompt" [-n N] [-t T]   Headless mode topogpt3 -i                          Interactive mode topogpt3 -f file.txt                 Read prompt from file  #pragma GCC diagnostic ignored "-Wunused-function" #ifdef...
- `app.py` ranks 2 by PageRank, 0 importers, 5 symbols: Drop-in entry point that demonstrates how to use the topogpt3 package.
- `gradio_app.py` ranks 3 by PageRank, 0 importers, 4 symbols: TopoGPT3 Gradio Interface for Hugging Face Spaces.
- Hotspot `topogpt3.c`: 128 symbols, 5 connections (score 0.33).
- Hotspot `gradio_app.py`: 4 symbols, 9 connections (score 0.12).
- Key entities: file:topogpt3.c, file:gradio_app.py, file:app.py, sym:topogpt3.c::softmax@391, sym:app.py::main@159, sym:gradio_app.py::run_hrm_inference@95, sym:app.py::run_training@105, sym:app.py::run_inference_hrm@71
- Rating 1.1/10 = 7 x PageRank share 0.16 + 3 x risk 0.00. Internal imports: 2.
