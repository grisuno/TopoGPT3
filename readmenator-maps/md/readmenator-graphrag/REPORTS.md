# GraphRAG Community Reports

Entities: 1265 | Relationships: 3647 | Communities: 7 | Themes: 3 | Text units: 1139

Query with `readmenator . ask "<question>"` (local: BM25 + Personalized PageRank; global: map-reduce over these reports) or the MCP tool `readmenator.graphrag`.

## Project overview (`root`, root, rating 7.0)

64 files in 7 communities and 3 themes. Highest-impact communities: topogpt3: model (7.0), eval (5.0), topogpt3: tasks (4.4). God nodes: topogpt3/model.py, topogpt3/__init__.py, topogpt3/checkpoint_meta.py, topogpt3/__main__.py, topogpt3/chat.py.

- [topogpt3: model] rating 7.0: `topogpt3/model.py` ranks 1 by PageRank, 22 importers, 188 symbols: TopoGPT2: Quaternion-Enhanced Topological Transformer Language Model  Author: Gris Iscomeback Email: grisiscomeback@gmail.com License: GPL v3  Mejoras sobre topogpt.py: - Álgebra de cuaterniones completa (QuaternionLinear...
- [eval] rating 5.0: `topogpt3/yarn.py` ranks 1 by PageRank, 3 importers, 3 symbols: YaRN RoPE extrapolation for TopoGPT3.
- [topogpt3: tasks] rating 4.4: `topogpt3/chat.py` ranks 1 by PageRank, 16 importers, 8 symbols: Chat template + special tokens for TopoGPT3.
- [topogpt3: inference_hrm] rating 3.8: `topogpt3/checkpoint_meta.py` ranks 1 by PageRank, 13 importers, 5 symbols: Checkpoint architecture discovery shared by inference, API and trainers.
- [unassigned files] rating 1.8: `convert_weights.py` ranks 1 by PageRank, 0 importers, 2 symbols: TopoGPT3 Weight Converter: safetensors -> flat float32 binary.
- [topogpt3: jlens] rating 1.5: `topogpt3/lens_model.py` ranks 1 by PageRank, 6 importers, 29 symbols: LensModel: What the lens needs from a model.
- [root] rating 0.8: `topogpt3.c` ranks 1 by PageRank, 2 importers, 128 symbols: FILE: topogpt3 -p "prompt" [-n N] [-t T]   Headless mode topogpt3 -i                          Interactive mode topogpt3 -f file.txt                 Read prompt from file  #pragma GCC diagnostic ignored "-Wunused-function" #ifdef...
- Key entities: file:topogpt3/model.py, file:topogpt3/train.py, file:eval/governor.py, file:eval/harness.py, file:eval/tasks.py, file:tests/test_fallback.py
- Children: t0, t1, t2
- Root rating = highest community rating.

## topogpt3: model + eval +3 (`t0`, theme, rating 7.0)

Theme of 5 communities and 51 files: topogpt3: model (15 files, rating 7.0); eval (13 files, rating 5.0); topogpt3: tasks (10 files, rating 4.4); topogpt3: inference_hrm (9 files, rating 3.8); topogpt3: jlens (4 files, rating 1.5).

- [topogpt3: model] `topogpt3/model.py` ranks 1 by PageRank, 22 importers, 188 symbols: TopoGPT2: Quaternion-Enhanced Topological Transformer Language Model  Author: Gris Iscomeback Email: grisiscomeback@gmail.com License: GPL v3  Mejoras sobre topogpt.py: - Álgebra de cuaterniones completa (QuaternionLinear...
- [topogpt3: model] `synthetic_dataset.py` ranks 2 by PageRank, 1 importers, 35 symbols: Synthetic Dataset Generator for TopoGPT2.
- [eval] `topogpt3/yarn.py` ranks 1 by PageRank, 3 importers, 3 symbols: YaRN RoPE extrapolation for TopoGPT3.
- [eval] `topogpt3/__init__.py` ranks 2 by PageRank, 7 importers, 0 symbols: TopoGPT3: complex-valued spectral language model for code.
- [topogpt3: tasks] `topogpt3/chat.py` ranks 1 by PageRank, 16 importers, 8 symbols: Chat template + special tokens for TopoGPT3.
- [topogpt3: tasks] `topogpt3/fallback.py` ranks 2 by PageRank, 10 importers, 15 symbols: Local-fallback profiles, apt_chain tooling and deterministic reranking.
- [topogpt3: inference_hrm] `topogpt3/checkpoint_meta.py` ranks 1 by PageRank, 13 importers, 5 symbols: Checkpoint architecture discovery shared by inference, API and trainers.
- [topogpt3: inference_hrm] `topogpt3/continuation.py` ranks 2 by PageRank, 3 importers, 5 symbols: Auto-continuation engine: detects truncated responses and feeds the last incomplete lines back so the model can resume where it left off.
- Key entities: file:topogpt3/model.py, file:topogpt3/train.py, file:eval/governor.py, file:eval/harness.py, file:eval/tasks.py, file:tests/test_fallback.py, file:topogpt3/inference_hrm.py, file:topogpt3/api_server.py
- Children: c0, c1, c2, c3, c4
- Theme rating = highest child community rating.

## unassigned files (`t1`, theme, rating 1.8)

Theme of 1 communities and 10 files: unassigned files (10 files, rating 1.8).

- [unassigned files] `convert_weights.py` ranks 1 by PageRank, 0 importers, 2 symbols: TopoGPT3 Weight Converter: safetensors -> flat float32 binary.
- [unassigned files] `convert_weights_minios.py` ranks 2 by PageRank, 0 importers, 1 symbols: Convert TopoGPT3 safetensors weights to float16 binary for MiniOS.
- Key entities: file:eval/report.py, file:tests/test_data_pipeline.py
- Children: c6
- Theme rating = highest child community rating.

## root (`t2`, theme, rating 0.8)

Theme of 1 communities and 3 files: root (3 files, rating 0.8).

- [root] `topogpt3.c` ranks 1 by PageRank, 2 importers, 128 symbols: FILE: topogpt3 -p "prompt" [-n N] [-t T]   Headless mode topogpt3 -i                          Interactive mode topogpt3 -f file.txt                 Read prompt from file  #pragma GCC diagnostic ignored "-Wunused-function" #ifdef...
- [root] `app.py` ranks 2 by PageRank, 0 importers, 5 symbols: Drop-in entry point that demonstrates how to use the topogpt3 package.
- Key entities: file:topogpt3.c, file:gradio_app.py
- Children: c5
- Theme rating = highest child community rating.

## topogpt3: model (`c0`, community, rating 7.0)

15 files under topogpt3 (py 15), mostly utility. Core file topogpt3/model.py (PageRank 0.1151, imported by 22 files): TopoGPT2: Quaternion-Enhanced Topological Transformer Language Model  Author: Gris Iscomeback Email: grisiscomeback@gmail.com License: GPL v3  Mejoras sobre topogpt.py: - Álgebra de cuaterniones completa (QuaternionLinear... Key abstractions: TopoGPT2Config, QuaternionOps, QuaternionLinear, QuaternionSpectralLayer, SpectralAutoencoder, QuaternionTorusBrain. Depends on topogpt3: inference_hrm (9), topogpt3: tasks (5), eval (2). Used by topogpt3: tasks (7), eval (6), topogpt3: jlens (4).

- `topogpt3/model.py` ranks 1 by PageRank, 22 importers, 188 symbols: TopoGPT2: Quaternion-Enhanced Topological Transformer Language Model  Author: Gris Iscomeback Email: grisiscomeback@gmail.com License: GPL v3  Mejoras sobre topogpt.py: - Álgebra de cuaterniones completa (QuaternionLinear...
- `synthetic_dataset.py` ranks 2 by PageRank, 1 importers, 35 symbols: Synthetic Dataset Generator for TopoGPT2.
- `topogpt3/trainer_utils_topo.py` ranks 3 by PageRank, 7 importers, 10 symbols: Shared training utilities for TopoGPT3 advanced trainers.
- Hotspot `topogpt3/model.py`: 188 symbols, 53 connections (score 0.99).
- Hotspot `topogpt3/train.py`: 62 symbols, 26 connections (score 0.42).
- Taint: 5 paths reach this group via eval.
- Dataflow: 4 INFERRED issues (first: UNCHECKED_ALLOC in main).
- Surprising bridge: sandbox_smoke.py <-> synthetic_dataset.py (5 hops across communities).
- Key entities: file:topogpt3/model.py, file:topogpt3/train.py, file:synthetic_dataset.py, file:topogpt3/trainer_utils_topo.py, sym:topogpt3/model.py::main@4330, sym:topogpt3/model.py::run@2324, sym:topogpt3/model.py::__init__@336, file:topogpt3/rollout.py
- Rating 7.0/10 = 7 x PageRank share 1.00 + 3 x risk 0.00. Internal imports: 29.

## eval (`c1`, community, rating 5.0)

13 files under eval (py 13), mostly utility. Core file topogpt3/yarn.py (PageRank 0.0433, imported by 3 files): YaRN RoPE extrapolation for TopoGPT3. Key abstractions: YaRNConfig, yarn_scale_inv_freq, apply_yarn_to_rope, SandboxConfig, d, check_safety. Depends on topogpt3: model (6), topogpt3: tasks (4), topogpt3: inference_hrm (3). Used by topogpt3: model (2), topogpt3: tasks (2).

- `topogpt3/yarn.py` ranks 1 by PageRank, 3 importers, 3 symbols: YaRN RoPE extrapolation for TopoGPT3.
- `topogpt3/__init__.py` ranks 2 by PageRank, 7 importers, 0 symbols: TopoGPT3: complex-valued spectral language model for code.
- `eval/sandbox.py` ranks 3 by PageRank, 3 importers, 9 symbols: Sandbox for executing model-generated code during HumanEval evaluation.
- Hotspot `topogpt3/__init__.py`: 0 symbols, 36 connections (score 0.40).
- Hotspot `eval/harness.py`: 12 symbols, 27 connections (score 0.33).
- Taint: 4 paths reach this group via eval.
- Dataflow: 1 INFERRED issues (first: UNCHECKED_ALLOC in main).
- Surprising bridge: governor.py <-> test_checkpoint_meta.py (5 hops across communities).
- Key entities: file:eval/governor.py, file:eval/harness.py, file:eval/sandbox.py, file:topogpt3/__init__.py, file:eval/repair.py, file:eval/noise_sweep.py, file:eval/temp_sweep.py, file:eval/governor_smoke.py
- Rating 5.0/10 = 7 x PageRank share 0.71 + 3 x risk 0.00. Internal imports: 16.

## topogpt3: tasks (`c2`, community, rating 4.4)

10 files under topogpt3 (py 10), mostly utility. Core file topogpt3/chat.py (PageRank 0.0672, imported by 16 files): Chat template + special tokens for TopoGPT3. Key abstractions: pre_processing_chat, post_processing_chat, apply_chat_template, parse_tool_calls, parse_thinking, split_reasoning_content. Depends on topogpt3: model (7), eval (2), topogpt3: inference_hrm (2). Used by topogpt3: inference_hrm (7), topogpt3: model (5), eval (4).

- `topogpt3/chat.py` ranks 1 by PageRank, 16 importers, 8 symbols: Chat template + special tokens for TopoGPT3.
- `topogpt3/fallback.py` ranks 2 by PageRank, 10 importers, 15 symbols: Local-fallback profiles, apt_chain tooling and deterministic reranking.
- `topogpt3/rewards.py` ranks 3 by PageRank, 7 importers, 12 symbols: Reward + advantage + loss helpers for TopoGPT3 group-RL.
- Hotspot `eval/tasks.py`: 15 symbols, 25 connections (score 0.31).
- Hotspot `topogpt3/train_agent.py`: 2 symbols, 25 connections (score 0.28).
- Taint: 5 paths reach this group via eval.
- Key entities: file:eval/tasks.py, file:tests/test_fallback.py, file:topogpt3/fallback.py, file:topogpt3/rewards.py, file:topogpt3/chat.py, file:topogpt3/train_agent.py, file:topogpt3/tools_agent.py, file:tests/test_heritage.py
- Rating 4.4/10 = 7 x PageRank share 0.63 + 3 x risk 0.00. Internal imports: 25.

## topogpt3: inference_hrm (`c3`, community, rating 3.8)

9 files under topogpt3 (py 9), mostly utility. Core file topogpt3/checkpoint_meta.py (PageRank 0.0474, imported by 13 files): Checkpoint architecture discovery shared by inference, API and trainers. Key abstractions: read_state, probe_checkpoint, config_from_checkpoint, state_summary, config_dict, is_response_complete. Depends on topogpt3: tasks (7), topogpt3: model (3). Used by topogpt3: model (9), eval (3), topogpt3: tasks (2).

- `topogpt3/checkpoint_meta.py` ranks 1 by PageRank, 13 importers, 5 symbols: Checkpoint architecture discovery shared by inference, API and trainers.
- `topogpt3/continuation.py` ranks 2 by PageRank, 3 importers, 5 symbols: Auto-continuation engine: detects truncated responses and feeds the last incomplete lines back so the model can resume where it left off.
- `topogpt3/api_server.py` ranks 3 by PageRank, 6 importers, 63 symbols: OpenAI-compatible HTTP API server so TopoGPT3 can be used as a backend for coding agents (e.g.
- Hotspot `topogpt3/api_server.py`: 63 symbols, 54 connections (score 0.73).
- Hotspot `topogpt3/inference_hrm.py`: 76 symbols, 19 connections (score 0.37).
- 5 layer violations, e.g. test_structured_output.py (testing) -> api_server.py (presentation).
- Taint: 4 paths reach this group via eval.
- Surprising bridge: governor.py <-> test_checkpoint_meta.py (5 hops across communities).
- Key entities: file:topogpt3/inference_hrm.py, file:topogpt3/api_server.py, file:topogpt3/inference.py, file:tests/test_structured_output.py, file:topogpt3/structured_output.py, file:topogpt3/tokenizer_tools.py, sym:topogpt3/inference_hrm.py::execute@1346, sym:topogpt3/inference.py::execute@622
- Rating 3.8/10 = 7 x PageRank share 0.55 + 3 x risk 0.00. Internal imports: 14.

## unassigned files (`c6`, community, rating 1.8)

10 files under eval (py 8, sh 2), mostly utility. Core file convert_weights.py (PageRank 0.0073, imported by 0 files): TopoGPT3 Weight Converter: safetensors -> flat float32 binary. Key abstractions: convert, main, main, main, pass_at_k, classify_error.

- `convert_weights.py` ranks 1 by PageRank, 0 importers, 2 symbols: TopoGPT3 Weight Converter: safetensors -> flat float32 binary.
- `convert_weights_minios.py` ranks 2 by PageRank, 0 importers, 1 symbols: Convert TopoGPT3 safetensors weights to float16 binary for MiniOS.
- `encode_tokens.py` ranks 3 by PageRank, 0 importers, 1 symbols: Tokenize text using GPT-2 BPE and output binary token IDs.
- Hotspot `eval/report.py`: 6 symbols, 9 connections (score 0.11).
- Hotspot `eval/noise_analysis.py`: 3 symbols, 9 connections (score 0.11).
- Key entities: file:eval/report.py, file:tests/test_data_pipeline.py, file:eval/analyze.py, file:eval/noise_analysis.py, file:eval/analyze_results.py, file:convert_weights.py, file:convert_weights_minios.py, file:encode_tokens.py
- Rating 1.8/10 = 7 x PageRank share 0.26 + 3 x risk 0.00. Internal imports: 0.

## topogpt3: jlens (`c4`, community, rating 1.5)

4 files under topogpt3 (py 4), mostly testing. Core file topogpt3/lens_model.py (PageRank 0.0290, imported by 6 files): LensModel: What the lens needs from a model. Key abstractions: LensModel, TopoGPT3LensConfig, TopoGPT3LensModel, TinyDecoder, encode, forward. Depends on topogpt3: model (4). Used by topogpt3: model (2), eval (2).

- `topogpt3/lens_model.py` ranks 1 by PageRank, 6 importers, 29 symbols: LensModel: What the lens needs from a model.
- `topogpt3/jlens.py` ranks 2 by PageRank, 7 importers, 29 symbols: TopoGPT3JLensFitConfig: Centralized configuration for Jacobian lens fitting.
- `tests/test_jlens.py` ranks 3 by PageRank, 0 importers, 51 symbols: TestValidPositionMask: Feature: valid_position_mask excludes attention-sink and final positions.
- Hotspot `topogpt3/jlens.py`: 29 symbols, 23 connections (score 0.32).
- Hotspot `topogpt3/lens_model.py`: 29 symbols, 22 connections (score 0.31).
- Taint: 2 paths reach this group via eval.
- Surprising bridge: sandbox_smoke.py <-> test_jlens.py (5 hops across communities).
- Key entities: file:tests/test_jlens.py, file:topogpt3/lens_model.py, file:tests/test_lens_model.py, file:topogpt3/jlens.py, sym:topogpt3/jlens.py::fit@291, sym:topogpt3/jlens.py::jacobian_for_prompt@187, sym:topogpt3/lens_model.py::TinyDecoder@306, sym:topogpt3/lens_model.py::TopoGPT3LensModel@161
- Rating 1.5/10 = 7 x PageRank share 0.21 + 3 x risk 0.00. Internal imports: 9.

## root (`c5`, community, rating 0.8)

3 files under root (py 2, c 1), mostly utility. Core file topogpt3.c (PageRank 0.0198, imported by 2 files): FILE: topogpt3 -p "prompt" [-n N] [-t T]   Headless mode topogpt3 -i                          Interactive mode topogpt3 -f file.txt                 Read prompt from file  #pragma GCC diagnostic ignored "-Wunused-function" #ifdef... Key abstractions: FILE, LayerWeights, ModelWeights, stdin, stdout, stderr.

- `topogpt3.c` ranks 1 by PageRank, 2 importers, 128 symbols: FILE: topogpt3 -p "prompt" [-n N] [-t T]   Headless mode topogpt3 -i                          Interactive mode topogpt3 -f file.txt                 Read prompt from file  #pragma GCC diagnostic ignored "-Wunused-function" #ifdef...
- `app.py` ranks 2 by PageRank, 0 importers, 5 symbols: Drop-in entry point that demonstrates how to use the topogpt3 package.
- `gradio_app.py` ranks 3 by PageRank, 0 importers, 4 symbols: TopoGPT3 Gradio Interface for Hugging Face Spaces.
- Hotspot `topogpt3.c`: 128 symbols, 5 connections (score 0.33).
- Hotspot `gradio_app.py`: 4 symbols, 9 connections (score 0.11).
- Key entities: file:topogpt3.c, file:gradio_app.py, file:app.py, sym:topogpt3.c::softmax@391, sym:app.py::main@159, sym:app.py::run_training@105, sym:gradio_app.py::run_hrm_inference@95, sym:app.py::run_inference_hrm@71
- Rating 0.8/10 = 7 x PageRank share 0.12 + 3 x risk 0.00. Internal imports: 2.
