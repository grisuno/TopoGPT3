# Polyglot Codebase Knowledge Graph

> Generated offline by **readmenator**. Supports C, C++, Python, Go, Rust, JS/TS, Java, C#, Shell, PHP, Dart, GDScript, Nim, ASM.
> No LLMs. No tokens. Pure static analysis. See more [here](https://github.com/grisuno/ReadMenator)

**Total Files Parsed:** 24 | **Total Symbols Extracted:** 513 | **Total Imports:** 252

## Structural Knowledge Map
```mermaid
graph TD
    classDef mod fill:#1e1e1e,stroke:#ff6666,stroke-width:2px,color:#fff;
    classDef cls fill:#2d2d2d,stroke:#4ec9b0,stroke-width:2px,color:#fff;
    classDef fn fill:#333,stroke:#dcdcaa,stroke-width:1px,color:#dcdcaa;
    classDef ext fill:#111,stroke:#666,stroke-dasharray:5 5,color:#aaa;
    topogpt3_model_py["model.py (py)"]
    class topogpt3_model_py mod;
    topogpt3_model_py_TopoGPT2Config["TopoGPT2Config"]
    class topogpt3_model_py_TopoGPT2Config cls;
    topogpt3_model_py --> topogpt3_model_py_TopoGPT2Config
    topogpt3_model_py_setup_logger["setup_logger"]
    class topogpt3_model_py_setup_logger fn;
    topogpt3_model_py --> topogpt3_model_py_setup_logger
    topogpt3_model_py_set_seed["set_seed"]
    class topogpt3_model_py_set_seed fn;
    topogpt3_model_py --> topogpt3_model_py_set_seed
    topogpt3_model_py_QuaternionOps["QuaternionOps"]
    class topogpt3_model_py_QuaternionOps cls;
    topogpt3_model_py --> topogpt3_model_py_QuaternionOps
    topogpt3_model_py_QuaternionLinear["QuaternionLinear"]
    class topogpt3_model_py_QuaternionLinear cls;
    topogpt3_model_py --> topogpt3_model_py_QuaternionLinear
    synthetic_dataset_py["synthetic_dataset.py (py)"]
    class synthetic_dataset_py mod;
    synthetic_dataset_py_LLMBackend["LLMBackend"]
    class synthetic_dataset_py_LLMBackend cls;
    synthetic_dataset_py --> synthetic_dataset_py_LLMBackend
    synthetic_dataset_py_GroqBackend["GroqBackend"]
    class synthetic_dataset_py_GroqBackend cls;
    synthetic_dataset_py --> synthetic_dataset_py_GroqBackend
    synthetic_dataset_py_OpenRouterBackend["OpenRouterBackend"]
    class synthetic_dataset_py_OpenRouterBackend cls;
    synthetic_dataset_py --> synthetic_dataset_py_OpenRouterBackend
    synthetic_dataset_py_OllamaBackend["OllamaBackend"]
    class synthetic_dataset_py_OllamaBackend cls;
    synthetic_dataset_py --> synthetic_dataset_py_OllamaBackend
    synthetic_dataset_py_build_backend["build_backend"]
    class synthetic_dataset_py_build_backend fn;
    synthetic_dataset_py --> synthetic_dataset_py_build_backend
    eval_harness_py["harness.py (py)"]
    class eval_harness_py mod;
    eval_harness_py_load_humaneval["load_humaneval"]
    class eval_harness_py_load_humaneval fn;
    eval_harness_py --> eval_harness_py_load_humaneval
    eval_harness_py_build_prompt["build_prompt"]
    class eval_harness_py_build_prompt fn;
    eval_harness_py --> eval_harness_py_build_prompt
    eval_harness_py_extract_candidate["extract_candidate"]
    class eval_harness_py_extract_candidate fn;
    eval_harness_py --> eval_harness_py_extract_candidate
    eval_harness_py_run_one_test["run_one_test"]
    class eval_harness_py_run_one_test fn;
    eval_harness_py --> eval_harness_py_run_one_test
    eval_harness_py_run_one_test_sandboxed["run_one_test_sandboxed"]
    class eval_harness_py_run_one_test_sandboxed fn;
    eval_harness_py --> eval_harness_py_run_one_test_sandboxed
    topogpt3_train_py["train.py (py)"]
    class topogpt3_train_py mod;
    topogpt3_train_py_TopoGPT3Config["TopoGPT3Config"]
    class topogpt3_train_py_TopoGPT3Config cls;
    topogpt3_train_py --> topogpt3_train_py_TopoGPT3Config
    topogpt3_train_py_GrassmannianTracker["GrassmannianTracker"]
    class topogpt3_train_py_GrassmannianTracker cls;
    topogpt3_train_py --> topogpt3_train_py_GrassmannianTracker
    topogpt3_train_py__gauss_complex_contract["_gauss_complex_contract"]
    class topogpt3_train_py__gauss_complex_contract fn;
    topogpt3_train_py --> topogpt3_train_py__gauss_complex_contract
    topogpt3_train_py_apply_gauss_patch["apply_gauss_patch"]
    class topogpt3_train_py_apply_gauss_patch fn;
    topogpt3_train_py --> topogpt3_train_py_apply_gauss_patch
    topogpt3_train_py_EfficiencyMetrics["EfficiencyMetrics"]
    class topogpt3_train_py_EfficiencyMetrics cls;
    topogpt3_train_py --> topogpt3_train_py_EfficiencyMetrics
    eval_repair_py["repair.py (py)"]
    class eval_repair_py mod;
    eval_repair_py__new_loader["_new_loader"]
    class eval_repair_py__new_loader fn;
    eval_repair_py --> eval_repair_py__new_loader
    eval_repair_py_extract_candidate["extract_candidate"]
    class eval_repair_py_extract_candidate fn;
    eval_repair_py --> eval_repair_py_extract_candidate
    eval_repair_py_run_test["run_test"]
    class eval_repair_py_run_test fn;
    eval_repair_py --> eval_repair_py_run_test
    eval_repair_py_build_repair_prompt["build_repair_prompt"]
    class eval_repair_py_build_repair_prompt fn;
    eval_repair_py --> eval_repair_py_build_repair_prompt
    eval_repair_py_gen["gen"]
    class eval_repair_py_gen fn;
    eval_repair_py --> eval_repair_py_gen
    eval_noise_sweep_py["noise_sweep.py (py)"]
    class eval_noise_sweep_py mod;
    eval_noise_sweep_py_inject_noise["inject_noise"]
    class eval_noise_sweep_py_inject_noise fn;
    eval_noise_sweep_py --> eval_noise_sweep_py_inject_noise
    eval_noise_sweep_py_load_model["load_model"]
    class eval_noise_sweep_py_load_model fn;
    eval_noise_sweep_py --> eval_noise_sweep_py_load_model
    eval_noise_sweep_py_generate_one["generate_one"]
    class eval_noise_sweep_py_generate_one fn;
    eval_noise_sweep_py --> eval_noise_sweep_py_generate_one
    eval_noise_sweep_py_main["main"]
    class eval_noise_sweep_py_main fn;
    eval_noise_sweep_py --> eval_noise_sweep_py_main
    topogpt3_inference_hrm_py["inference_hrm.py (py)"]
    class topogpt3_inference_hrm_py mod;
    topogpt3_inference_hrm_py_ScalePreset["ScalePreset"]
    class topogpt3_inference_hrm_py_ScalePreset cls;
    topogpt3_inference_hrm_py --> topogpt3_inference_hrm_py_ScalePreset
    topogpt3_inference_hrm_py_RecursiveReasoningConfig["RecursiveReasoningConfig"]
    class topogpt3_inference_hrm_py_RecursiveReasoningConfig cls;
    topogpt3_inference_hrm_py --> topogpt3_inference_hrm_py_RecursiveReasoningConfig
    topogpt3_inference_hrm_py_HRMInferenceSettings["HRMInferenceSettings"]
    class topogpt3_inference_hrm_py_HRMInferenceSettings cls;
    topogpt3_inference_hrm_py --> topogpt3_inference_hrm_py_HRMInferenceSettings
    topogpt3_inference_hrm_py_HRMLoggerFactory["HRMLoggerFactory"]
    class topogpt3_inference_hrm_py_HRMLoggerFactory cls;
    topogpt3_inference_hrm_py --> topogpt3_inference_hrm_py_HRMLoggerFactory
    topogpt3_inference_hrm_py_SecurePathResolver["SecurePathResolver"]
    class topogpt3_inference_hrm_py_SecurePathResolver cls;
    topogpt3_inference_hrm_py --> topogpt3_inference_hrm_py_SecurePathResolver
    eval_diag_static_py["diag_static.py (py)"]
    class eval_diag_static_py mod;
    eval_diag_static_py_phase_discretization["phase_discretization"]
    class eval_diag_static_py_phase_discretization fn;
    eval_diag_static_py --> eval_diag_static_py_phase_discretization
    eval_diag_static_py_synthetic_winding["synthetic_winding"]
    class eval_diag_static_py_synthetic_winding fn;
    eval_diag_static_py --> eval_diag_static_py_synthetic_winding
    eval_diag_static_py_static_kappa["static_kappa"]
    class eval_diag_static_py_static_kappa fn;
    eval_diag_static_py --> eval_diag_static_py_static_kappa
    eval_diag_static_py_main["main"]
    class eval_diag_static_py_main fn;
    eval_diag_static_py --> eval_diag_static_py_main
    topogpt3_inference_py["inference.py (py)"]
    class topogpt3_inference_py mod;
    topogpt3_inference_py_ScalePreset["ScalePreset"]
    class topogpt3_inference_py_ScalePreset cls;
    topogpt3_inference_py --> topogpt3_inference_py_ScalePreset
    topogpt3_inference_py_InferenceSettings["InferenceSettings"]
    class topogpt3_inference_py_InferenceSettings cls;
    topogpt3_inference_py --> topogpt3_inference_py_InferenceSettings
    topogpt3_inference_py_InferenceLoggerFactory["InferenceLoggerFactory"]
    class topogpt3_inference_py_InferenceLoggerFactory cls;
    topogpt3_inference_py --> topogpt3_inference_py_InferenceLoggerFactory
    topogpt3_inference_py_SecurePathResolver["SecurePathResolver"]
    class topogpt3_inference_py_SecurePathResolver cls;
    topogpt3_inference_py --> topogpt3_inference_py_SecurePathResolver
    topogpt3_inference_py_SourceModuleLoader["SourceModuleLoader"]
    class topogpt3_inference_py_SourceModuleLoader cls;
    topogpt3_inference_py --> topogpt3_inference_py_SourceModuleLoader
    eval_sandbox_py["sandbox.py (py)"]
    class eval_sandbox_py mod;
    eval_sandbox_py_SandboxConfig["SandboxConfig"]
    class eval_sandbox_py_SandboxConfig cls;
    eval_sandbox_py --> eval_sandbox_py_SandboxConfig
    eval_sandbox_py__names_imported["_names_imported"]
    class eval_sandbox_py__names_imported fn;
    eval_sandbox_py --> eval_sandbox_py__names_imported
    eval_sandbox_py__blocked_dunder_access["_blocked_dunder_access"]
    class eval_sandbox_py__blocked_dunder_access fn;
    eval_sandbox_py --> eval_sandbox_py__blocked_dunder_access
    eval_sandbox_py__max_depth["_max_depth"]
    class eval_sandbox_py__max_depth fn;
    eval_sandbox_py --> eval_sandbox_py__max_depth
    eval_sandbox_py_check_safety["check_safety"]
    class eval_sandbox_py_check_safety fn;
    eval_sandbox_py --> eval_sandbox_py_check_safety
    eval_temp_sweep_py["temp_sweep.py (py)"]
    class eval_temp_sweep_py mod;
    eval_temp_sweep_py_generate_one["generate_one"]
    class eval_temp_sweep_py_generate_one fn;
    eval_temp_sweep_py --> eval_temp_sweep_py_generate_one
    eval_temp_sweep_py_evaluate_problems["evaluate_problems"]
    class eval_temp_sweep_py_evaluate_problems fn;
    eval_temp_sweep_py --> eval_temp_sweep_py_evaluate_problems
    eval_temp_sweep_py_pass_at_k_unbiased["pass_at_k_unbiased"]
    class eval_temp_sweep_py_pass_at_k_unbiased fn;
    eval_temp_sweep_py --> eval_temp_sweep_py_pass_at_k_unbiased
    eval_temp_sweep_py_summarize["summarize"]
    class eval_temp_sweep_py_summarize fn;
    eval_temp_sweep_py --> eval_temp_sweep_py_summarize
    eval_temp_sweep_py_main["main"]
    class eval_temp_sweep_py_main fn;
    eval_temp_sweep_py --> eval_temp_sweep_py_main
    eval_governor_smoke_py["governor_smoke.py (py)"]
    class eval_governor_smoke_py mod;
    eval_governor_smoke_py_load_model["load_model"]
    class eval_governor_smoke_py_load_model fn;
    eval_governor_smoke_py --> eval_governor_smoke_py_load_model
    eval_governor_smoke_py_test_tokenstream_threadsafety["test_tokenstream_threadsafety"]
    class eval_governor_smoke_py_test_tokenstream_threadsafety fn;
    eval_governor_smoke_py --> eval_governor_smoke_py_test_tokenstream_threadsafety
    eval_governor_smoke_py_test_governor_basic["test_governor_basic"]
    class eval_governor_smoke_py_test_governor_basic fn;
    eval_governor_smoke_py --> eval_governor_smoke_py_test_governor_basic
    eval_governor_smoke_py_test_loop_detector["test_loop_detector"]
    class eval_governor_smoke_py_test_loop_detector fn;
    eval_governor_smoke_py --> eval_governor_smoke_py_test_loop_detector
    eval_governor_smoke_py_test_cancel["test_cancel"]
    class eval_governor_smoke_py_test_cancel fn;
    eval_governor_smoke_py --> eval_governor_smoke_py_test_cancel
    eval_report_py["report.py (py)"]
    class eval_report_py mod;
    eval_report_py_pass_at_k["pass_at_k"]
    class eval_report_py_pass_at_k fn;
    eval_report_py --> eval_report_py_pass_at_k
    eval_report_py_classify_error["classify_error"]
    class eval_report_py_classify_error fn;
    eval_report_py --> eval_report_py_classify_error
    eval_report_py_load_jsonl["load_jsonl"]
    class eval_report_py_load_jsonl fn;
    eval_report_py --> eval_report_py_load_jsonl
    eval_report_py_summarize_run["summarize_run"]
    class eval_report_py_summarize_run fn;
    eval_report_py --> eval_report_py_summarize_run
    eval_report_py_repair_summary["repair_summary"]
    class eval_report_py_repair_summary fn;
    eval_report_py --> eval_report_py_repair_summary
    eval_noise_analysis_py["noise_analysis.py (py)"]
    class eval_noise_analysis_py mod;
    eval_noise_analysis_py__load["_load"]
    class eval_noise_analysis_py__load fn;
    eval_noise_analysis_py --> eval_noise_analysis_py__load
    eval_noise_analysis_py_consistency_across_runs["consistency_across_runs"]
    class eval_noise_analysis_py_consistency_across_runs fn;
    eval_noise_analysis_py --> eval_noise_analysis_py_consistency_across_runs
    eval_noise_analysis_py_main["main"]
    class eval_noise_analysis_py_main fn;
    eval_noise_analysis_py --> eval_noise_analysis_py_main
    eval_governor_py["governor.py (py)"]
    class eval_governor_py mod;
    eval_governor_py_TokenStream["TokenStream"]
    class eval_governor_py_TokenStream cls;
    eval_governor_py --> eval_governor_py_TokenStream
    eval_governor_py_StopReason["StopReason"]
    class eval_governor_py_StopReason cls;
    eval_governor_py --> eval_governor_py_StopReason
    eval_governor_py_GenerationResult["GenerationResult"]
    class eval_governor_py_GenerationResult cls;
    eval_governor_py --> eval_governor_py_GenerationResult
    eval_governor_py_GenerationGovernor["GenerationGovernor"]
    class eval_governor_py_GenerationGovernor cls;
    eval_governor_py --> eval_governor_py_GenerationGovernor
    eval_governor_py_make_loop_detector["make_loop_detector"]
    class eval_governor_py_make_loop_detector fn;
    eval_governor_py --> eval_governor_py_make_loop_detector
    eval_analyze_py["analyze.py (py)"]
    class eval_analyze_py mod;
    eval_analyze_py_pass_at_k["pass_at_k"]
    class eval_analyze_py_pass_at_k fn;
    eval_analyze_py --> eval_analyze_py_pass_at_k
    eval_analyze_py_classify_error["classify_error"]
    class eval_analyze_py_classify_error fn;
    eval_analyze_py --> eval_analyze_py_classify_error
    eval_analyze_py_load_jsonl["load_jsonl"]
    class eval_analyze_py_load_jsonl fn;
    eval_analyze_py --> eval_analyze_py_load_jsonl
    eval_analyze_py_summarize["summarize"]
    class eval_analyze_py_summarize fn;
    eval_analyze_py --> eval_analyze_py_summarize
    eval_analyze_py_main["main"]
    class eval_analyze_py_main fn;
    eval_analyze_py --> eval_analyze_py_main
    app_py["app.py (py)"]
    class app_py mod;
    app_py_run_inference["run_inference"]
    class app_py_run_inference fn;
    app_py --> app_py_run_inference
    app_py_run_inference_hrm["run_inference_hrm"]
    class app_py_run_inference_hrm fn;
    app_py --> app_py_run_inference_hrm
    app_py_run_training["run_training"]
    class app_py_run_training fn;
    app_py --> app_py_run_training
    app_py__build_parser["_build_parser"]
    class app_py__build_parser fn;
    app_py --> app_py__build_parser
    app_py_main["main"]
    class app_py_main fn;
    app_py --> app_py_main
    eval_analyze_results_py["analyze_results.py (py)"]
    class eval_analyze_results_py mod;
    eval_analyze_results_py_load_records["load_records"]
    class eval_analyze_results_py_load_records fn;
    eval_analyze_results_py --> eval_analyze_results_py_load_records
    eval_analyze_results_py_summarize["summarize"]
    class eval_analyze_results_py_summarize fn;
    eval_analyze_results_py --> eval_analyze_results_py_summarize
    eval_analyze_results_py_show_failures["show_failures"]
    class eval_analyze_results_py_show_failures fn;
    eval_analyze_results_py --> eval_analyze_results_py_show_failures
    eval_analyze_results_py_main["main"]
    class eval_analyze_results_py_main fn;
    eval_analyze_results_py --> eval_analyze_results_py_main
    topogpt3___init___py["__init__.py (py)"]
    class topogpt3___init___py mod;
    eval_samplers_py["samplers.py (py)"]
    class eval_samplers_py mod;
    eval_samplers_py_register_sampler["register_sampler"]
    class eval_samplers_py_register_sampler fn;
    eval_samplers_py --> eval_samplers_py_register_sampler
    eval_samplers_py__is_env_truthy["_is_env_truthy"]
    class eval_samplers_py__is_env_truthy fn;
    eval_samplers_py --> eval_samplers_py__is_env_truthy
    eval_samplers_py__make_standard["_make_standard"]
    class eval_samplers_py__make_standard fn;
    eval_samplers_py --> eval_samplers_py__make_standard
    eval_samplers_py__make_hrm["_make_hrm"]
    class eval_samplers_py__make_hrm fn;
    eval_samplers_py --> eval_samplers_py__make_hrm
    eval_samplers_py_list_samplers["list_samplers"]
    class eval_samplers_py_list_samplers fn;
    eval_samplers_py --> eval_samplers_py_list_samplers
    eval_smoke_py["smoke.py (py)"]
    class eval_smoke_py mod;
    eval_smoke_py_run_standard["run_standard"]
    class eval_smoke_py_run_standard fn;
    eval_smoke_py --> eval_smoke_py_run_standard
    eval_smoke_py_run_hrm["run_hrm"]
    class eval_smoke_py_run_hrm fn;
    eval_smoke_py --> eval_smoke_py_run_hrm
    eval_integration_smoke_py["integration_smoke.py (py)"]
    class eval_integration_smoke_py mod;
    eval_integration_smoke_py_main["main"]
    class eval_integration_smoke_py_main fn;
    eval_integration_smoke_py --> eval_integration_smoke_py_main
    eval_sandbox_smoke_py["sandbox_smoke.py (py)"]
    class eval_sandbox_smoke_py mod;
    eval_sandbox_smoke_py_main["main"]
    class eval_sandbox_smoke_py_main fn;
    eval_sandbox_smoke_py --> eval_sandbox_smoke_py_main
    install_sh["install.sh (sh)"]
    class install_sh mod;
    ext___future__["__future__"]
    class ext___future__ ext;
    app_py -.->|imports| ext___future__
    ext_argparse["argparse"]
    class ext_argparse ext;
    app_py -.->|imports| ext_argparse
    ext_sys["sys"]
    class ext_sys ext;
    app_py -.->|imports| ext_sys
    ext_typing["typing"]
    class ext_typing ext;
    app_py -.->|imports| ext_typing
    ext_torch["torch"]
    class ext_torch ext;
    app_py -.->|imports| ext_torch
    ext_topogpt3["topogpt3"]
    class ext_topogpt3 ext;
    app_py -.->|imports| ext_topogpt3
    eval_analyze_py -.->|imports| ext___future__
    eval_analyze_py -.->|imports| ext_argparse
    ext_json["json"]
    class ext_json ext;
    eval_analyze_py -.->|imports| ext_json
    ext_math["math"]
    class ext_math ext;
    eval_analyze_py -.->|imports| ext_math
    ext_re["re"]
    class ext_re ext;
    eval_analyze_py -.->|imports| ext_re
    ext_collections["collections"]
    class ext_collections ext;
    eval_analyze_py -.->|imports| ext_collections
    ext_pathlib["pathlib"]
    class ext_pathlib ext;
    eval_analyze_py -.->|imports| ext_pathlib
    eval_analyze_py -.->|imports| ext_typing
    eval_analyze_results_py -.->|imports| ext___future__
    eval_analyze_results_py -.->|imports| ext_argparse
    eval_analyze_results_py -.->|imports| ext_json
    eval_analyze_results_py -.->|imports| ext_collections
    eval_analyze_results_py -.->|imports| ext_pathlib
    eval_diag_static_py -.->|imports| ext___future__
    eval_diag_static_py -.->|imports| ext_argparse
    eval_diag_static_py -.->|imports| ext_json
    eval_diag_static_py -.->|imports| ext_math
    eval_diag_static_py -.->|imports| ext_sys
    ext_time["time"]
    class ext_time ext;
    eval_diag_static_py -.->|imports| ext_time
    eval_diag_static_py -.->|imports| ext_pathlib
    eval_diag_static_py -.->|imports| ext_typing
    eval_diag_static_py -.->|imports| ext_torch
    eval_diag_static_py -.->|imports| ext_topogpt3
    ext_topogpt3_model["topogpt3.model"]
    class ext_topogpt3_model ext;
    eval_diag_static_py -.->|imports| ext_topogpt3_model
    ext_safetensors_torch["safetensors.torch"]
    class ext_safetensors_torch ext;
    eval_diag_static_py -.->|imports| ext_safetensors_torch
    eval_governor_py -.->|imports| ext___future__
    ext_threading["threading"]
    class ext_threading ext;
    eval_governor_py -.->|imports| ext_threading
    eval_governor_py -.->|imports| ext_time
    ext_dataclasses["dataclasses"]
    class ext_dataclasses ext;
    eval_governor_py -.->|imports| ext_dataclasses
    ext_enum["enum"]
    class ext_enum ext;
    eval_governor_py -.->|imports| ext_enum
    eval_governor_py -.->|imports| ext_typing
    eval_governor_py -.->|imports| ext_torch
    ext_torch_nn_functional["torch.nn.functional"]
    class ext_torch_nn_functional ext;
    eval_governor_py -.->|imports| ext_torch_nn_functional
    eval_governor_smoke_py -.->|imports| ext_sys
    eval_governor_smoke_py -.->|imports| ext_threading
    eval_governor_smoke_py -.->|imports| ext_time
    eval_governor_smoke_py -.->|imports| ext_pathlib
    eval_governor_smoke_py -.->|imports| ext_torch
    ext_eval_governor["eval.governor"]
    class ext_eval_governor ext;
    eval_governor_smoke_py -.->|imports| ext_eval_governor
    eval_governor_smoke_py -.->|imports| ext_topogpt3
    ext_safetensors["safetensors"]
    class ext_safetensors ext;
    eval_governor_smoke_py -.->|imports| ext_safetensors
    eval_governor_smoke_py -.->|imports| ext_safetensors_torch
    eval_harness_py -.->|imports| ext___future__
    eval_harness_py -.->|imports| ext_argparse
    ext_contextlib["contextlib"]
    class ext_contextlib ext;
    eval_harness_py -.->|imports| ext_contextlib
    ext_io["io"]
    class ext_io ext;
    eval_harness_py -.->|imports| ext_io
    eval_harness_py -.->|imports| ext_json
    ext_os["os"]
    class ext_os ext;
    eval_harness_py -.->|imports| ext_os
    eval_harness_py -.->|imports| ext_re
    ext_signal["signal"]
    class ext_signal ext;
    eval_harness_py -.->|imports| ext_signal
    ext_subprocess["subprocess"]
    class ext_subprocess ext;
    eval_harness_py -.->|imports| ext_subprocess
    eval_harness_py -.->|imports| ext_sys
    eval_harness_py -.->|imports| ext_time
    ext_traceback["traceback"]
    class ext_traceback ext;
    eval_harness_py -.->|imports| ext_traceback
    eval_harness_py -.->|imports| ext_dataclasses
    eval_harness_py -.->|imports| ext_pathlib
    eval_harness_py -.->|imports| ext_typing
    eval_harness_py -.->|imports| ext_torch
    eval_harness_py -.->|imports| ext_torch
    eval_harness_py -.->|imports| ext_topogpt3
    ext_eval_samplers["eval.samplers"]
    class ext_eval_samplers ext;
    eval_harness_py -.->|imports| ext_eval_samplers
    eval_harness_py -.->|imports| ext_safetensors_torch
    ext_datasets["datasets"]
    class ext_datasets ext;
    eval_harness_py -.->|imports| ext_datasets
    ext_eval_sandbox["eval.sandbox"]
    class ext_eval_sandbox ext;
    eval_harness_py -.->|imports| ext_eval_sandbox
    eval_harness_py -.->|imports| ext_eval_samplers
    eval_harness_py -.->|imports| ext_safetensors
    eval_integration_smoke_py -.->|imports| ext_sys
    eval_integration_smoke_py -.->|imports| ext_pathlib
    ext_eval_harness["eval.harness"]
    class ext_eval_harness ext;
    eval_integration_smoke_py -.->|imports| ext_eval_harness
    eval_noise_analysis_py -.->|imports| ext___future__
    eval_noise_analysis_py -.->|imports| ext_argparse
    ext_ast["ast"]
    class ext_ast ext;
    eval_noise_analysis_py -.->|imports| ext_ast
    eval_noise_analysis_py -.->|imports| ext_json
    eval_noise_analysis_py -.->|imports| ext_re
    eval_noise_analysis_py -.->|imports| ext_sys
    eval_noise_analysis_py -.->|imports| ext_collections
    eval_noise_analysis_py -.->|imports| ext_pathlib
    eval_noise_analysis_py -.->|imports| ext_typing
    eval_noise_sweep_py -.->|imports| ext___future__
    eval_noise_sweep_py -.->|imports| ext_argparse
    eval_noise_sweep_py -.->|imports| ext_json
    eval_noise_sweep_py -.->|imports| ext_math
    eval_noise_sweep_py -.->|imports| ext_sys
    eval_noise_sweep_py -.->|imports| ext_time
    eval_noise_sweep_py -.->|imports| ext_pathlib
    eval_noise_sweep_py -.->|imports| ext_typing
    eval_noise_sweep_py -.->|imports| ext_torch
    eval_noise_sweep_py -.->|imports| ext_topogpt3
    eval_noise_sweep_py -.->|imports| ext_topogpt3_model
    eval_noise_sweep_py -.->|imports| ext_safetensors_torch
    eval_noise_sweep_py -.->|imports| ext_safetensors
    eval_noise_sweep_py -.->|imports| ext_eval_harness
    eval_repair_py -.->|imports| ext___future__
    eval_repair_py -.->|imports| ext_argparse
    eval_repair_py -.->|imports| ext_contextlib
    eval_repair_py -.->|imports| ext_io
    eval_repair_py -.->|imports| ext_json
    eval_repair_py -.->|imports| ext_re
    eval_repair_py -.->|imports| ext_time
    eval_repair_py -.->|imports| ext_traceback
    eval_repair_py -.->|imports| ext_collections
    eval_repair_py -.->|imports| ext_pathlib
    eval_repair_py -.->|imports| ext_typing
    eval_repair_py -.->|imports| ext_torch
    eval_repair_py -.->|imports| ext_safetensors
    eval_repair_py -.->|imports| ext_safetensors_torch
    eval_repair_py -.->|imports| ext_topogpt3
    eval_repair_py -.->|imports| ext_datasets
    eval_report_py -.->|imports| ext___future__
    eval_report_py -.->|imports| ext_argparse
    eval_report_py -.->|imports| ext_json
    eval_report_py -.->|imports| ext_math
    eval_report_py -.->|imports| ext_re
    ext_shutil["shutil"]
    class ext_shutil ext;
    eval_report_py -.->|imports| ext_shutil
    ext_statistics["statistics"]
    class ext_statistics ext;
    eval_report_py -.->|imports| ext_statistics
    eval_report_py -.->|imports| ext_collections
    eval_report_py -.->|imports| ext_pathlib
    eval_samplers_py -.->|imports| ext___future__
    eval_samplers_py -.->|imports| ext_os
    eval_samplers_py -.->|imports| ext_typing
    eval_samplers_py -.->|imports| ext_topogpt3
    eval_sandbox_py -.->|imports| ext___future__
    eval_sandbox_py -.->|imports| ext_ast
    eval_sandbox_py -.->|imports| ext_os
    eval_sandbox_py -.->|imports| ext_subprocess
    eval_sandbox_py -.->|imports| ext_sys
    ext_tempfile["tempfile"]
    class ext_tempfile ext;
    eval_sandbox_py -.->|imports| ext_tempfile
    ext_textwrap["textwrap"]
    class ext_textwrap ext;
    eval_sandbox_py -.->|imports| ext_textwrap
    eval_sandbox_py -.->|imports| ext_dataclasses
    eval_sandbox_py -.->|imports| ext_pathlib
    eval_sandbox_py -.->|imports| ext_typing
    eval_sandbox_py -.->|imports| ext_json
    eval_sandbox_smoke_py -.->|imports| ext_sys
    eval_sandbox_smoke_py -.->|imports| ext_pathlib
    eval_sandbox_smoke_py -.->|imports| ext_eval_sandbox
    eval_smoke_py -.->|imports| ext_time
    eval_smoke_py -.->|imports| ext_torch
    eval_smoke_py -.->|imports| ext_topogpt3
    eval_temp_sweep_py -.->|imports| ext___future__
    eval_temp_sweep_py -.->|imports| ext_argparse
    eval_temp_sweep_py -.->|imports| ext_json
    eval_temp_sweep_py -.->|imports| ext_math
    eval_temp_sweep_py -.->|imports| ext_sys
    eval_temp_sweep_py -.->|imports| ext_time
    eval_temp_sweep_py -.->|imports| ext_pathlib
    eval_temp_sweep_py -.->|imports| ext_typing
    eval_temp_sweep_py -.->|imports| ext_torch
    ext_eval_noise_sweep["eval.noise_sweep"]
    class ext_eval_noise_sweep ext;
    eval_temp_sweep_py -.->|imports| ext_eval_noise_sweep
    eval_temp_sweep_py -.->|imports| ext_eval_harness
    synthetic_dataset_py -.->|imports| ext_os
    synthetic_dataset_py -.->|imports| ext_sys
    synthetic_dataset_py -.->|imports| ext_json
    synthetic_dataset_py -.->|imports| ext_time
    ext_hashlib["hashlib"]
    class ext_hashlib ext;
    synthetic_dataset_py -.->|imports| ext_hashlib
    ext_logging["logging"]
    class ext_logging ext;
    synthetic_dataset_py -.->|imports| ext_logging
    synthetic_dataset_py -.->|imports| ext_argparse
    synthetic_dataset_py -.->|imports| ext_tempfile
    synthetic_dataset_py -.->|imports| ext_pathlib
    synthetic_dataset_py -.->|imports| ext_typing
    synthetic_dataset_py -.->|imports| ext_dataclasses
    ext_datetime["datetime"]
    class ext_datetime ext;
    synthetic_dataset_py -.->|imports| ext_datetime
    synthetic_dataset_py -.->|imports| ext_threading
    ext_queue["queue"]
    class ext_queue ext;
    synthetic_dataset_py -.->|imports| ext_queue
    ext_concurrent_futures["concurrent.futures"]
    class ext_concurrent_futures ext;
    synthetic_dataset_py -.->|imports| ext_concurrent_futures
    synthetic_dataset_py -.->|imports| ext_torch
    ext_numpy["numpy"]
    class ext_numpy ext;
    synthetic_dataset_py -.->|imports| ext_numpy
    ext_tiktoken["tiktoken"]
    class ext_tiktoken ext;
    synthetic_dataset_py -.->|imports| ext_tiktoken
    ext_requests["requests"]
    class ext_requests ext;
    synthetic_dataset_py -.->|imports| ext_requests
    synthetic_dataset_py -.->|imports| ext_requests
    synthetic_dataset_py -.->|imports| ext_requests
    synthetic_dataset_py -.->|imports| ext_requests
    synthetic_dataset_py -.->|imports| ext_requests
    synthetic_dataset_py -.->|imports| ext_requests
    topogpt3___init___py -.->|imports| ext___future__
    ext_model["model"]
    class ext_model ext;
    topogpt3___init___py -.->|imports| ext_model
    ext_train["train"]
    class ext_train ext;
    topogpt3___init___py -.->|imports| ext_train
    ext_inference["inference"]
    class ext_inference ext;
    topogpt3___init___py -.->|imports| ext_inference
    ext_inference_hrm["inference_hrm"]
    class ext_inference_hrm ext;
    topogpt3___init___py -.->|imports| ext_inference_hrm
    topogpt3_inference_py -.->|imports| ext___future__
    topogpt3_inference_py -.->|imports| ext_argparse
    topogpt3_inference_py -.->|imports| ext_logging
    topogpt3_inference_py -.->|imports| ext_sys
    topogpt3_inference_py -.->|imports| ext_time
    topogpt3_inference_py -.->|imports| ext_dataclasses
    topogpt3_inference_py -.->|imports| ext_pathlib
    topogpt3_inference_py -.->|imports| ext_typing
    topogpt3_inference_py -.->|imports| ext_torch
    topogpt3_inference_py -.->|imports| ext_safetensors
    topogpt3_inference_py -.->|imports| ext_safetensors_torch
    topogpt3_inference_hrm_py -.->|imports| ext___future__
    topogpt3_inference_hrm_py -.->|imports| ext_argparse
    topogpt3_inference_hrm_py -.->|imports| ext_logging
    topogpt3_inference_hrm_py -.->|imports| ext_sys
    topogpt3_inference_hrm_py -.->|imports| ext_time
    topogpt3_inference_hrm_py -.->|imports| ext_dataclasses
    topogpt3_inference_hrm_py -.->|imports| ext_pathlib
    topogpt3_inference_hrm_py -.->|imports| ext_typing
    topogpt3_inference_hrm_py -.->|imports| ext_torch
    topogpt3_inference_hrm_py -.->|imports| ext_torch_nn_functional
    topogpt3_inference_hrm_py -.->|imports| ext_safetensors
    topogpt3_inference_hrm_py -.->|imports| ext_safetensors_torch
    topogpt3_model_py -.->|imports| ext_torch
    ext_torch_nn["torch.nn"]
    class ext_torch_nn ext;
    topogpt3_model_py -.->|imports| ext_torch_nn
    topogpt3_model_py -.->|imports| ext_torch_nn_functional
    ext_torch_utils_checkpoint["torch.utils.checkpoint"]
    class ext_torch_utils_checkpoint ext;
    topogpt3_model_py -.->|imports| ext_torch_utils_checkpoint
    topogpt3_model_py -.->|imports| ext_safetensors_torch
    topogpt3_model_py -.->|imports| ext_numpy
    topogpt3_model_py -.->|imports| ext_math
    topogpt3_model_py -.->|imports| ext_os
    topogpt3_model_py -.->|imports| ext_sys
    topogpt3_model_py -.->|imports| ext_time
    topogpt3_model_py -.->|imports| ext_pathlib
    topogpt3_model_py -.->|imports| ext_json
    topogpt3_model_py -.->|imports| ext_hashlib
    topogpt3_model_py -.->|imports| ext_logging
    ext_warnings["warnings"]
    class ext_warnings ext;
    topogpt3_model_py -.->|imports| ext_warnings
    topogpt3_model_py -.->|imports| ext_argparse
    topogpt3_model_py -.->|imports| ext_datetime
    topogpt3_model_py -.->|imports| ext_typing
    topogpt3_model_py -.->|imports| ext_dataclasses
    topogpt3_model_py -.->|imports| ext_collections
    topogpt3_model_py -.->|imports| ext_collections
    ext_synthetic_dataset["synthetic_dataset"]
    class ext_synthetic_dataset ext;
    topogpt3_model_py -.->|imports| ext_synthetic_dataset
    topogpt3_model_py -.->|imports| ext_tiktoken
    topogpt3_model_py -.->|imports| ext_shutil
    topogpt3_train_py -.->|imports| ext___future__
    topogpt3_train_py -.->|imports| ext_argparse
    topogpt3_train_py -.->|imports| ext_json
    topogpt3_train_py -.->|imports| ext_logging
    topogpt3_train_py -.->|imports| ext_math
    topogpt3_train_py -.->|imports| ext_os
    topogpt3_train_py -.->|imports| ext_sys
    topogpt3_train_py -.->|imports| ext_time
    topogpt3_train_py -.->|imports| ext_collections
    topogpt3_train_py -.->|imports| ext_dataclasses
    topogpt3_train_py -.->|imports| ext_datetime
    topogpt3_train_py -.->|imports| ext_pathlib
    topogpt3_train_py -.->|imports| ext_typing
    topogpt3_train_py -.->|imports| ext_numpy
    topogpt3_train_py -.->|imports| ext_torch
    topogpt3_train_py -.->|imports| ext_torch_nn
    topogpt3_train_py -.->|imports| ext_torch_nn_functional
    topogpt3_train_py -.->|imports| ext_model
    topogpt3_train_py -.->|imports| ext_safetensors_torch
    topogpt3_train_py -.->|imports| ext_safetensors_torch
    topogpt3_train_py -.->|imports| ext_datasets
```

---

## Architecture Reference

### PY (23 files)

#### `app.py`
**Path:** `app.py`

**Functions:**
- `run_inference` (line 46) `def run_inference(prompt, checkpoint_dir, checkpoint_name, max_new_tokens, temperature, top_k, repetition_penalty, device)` - *Run the standard sampler and return the generated completion text.*
- `run_inference_hrm` (line 71) `def run_inference_hrm(prompt, checkpoint_dir, checkpoint_name, max_new_tokens, temperature, top_k, repetition_penalty, high_level_iters, low_level_iters, low_level_window, device)` - *Run the hierarchical recursive sampler and return the completion.*
- `run_training` (line 105) `def run_training(scale, start_tier, device, prepare_data)` - *Run the full TopoGPT3 curriculum trainer.*
- `_build_parser` (line 121) `def _build_parser()` - *Build the top-level CLI for this entry point script.*
- `main` (line 159) `def main(argv)` - *Entry point invoked when the file is executed as a script.*

#### `analyze.py`
**Path:** `eval/analyze.py`

**Functions:**
- `pass_at_k` (line 21) `def pass_at_k(n, c, k)` - *Unbiased estimator from the HumanEval paper.

pass@k = 1 - C(n-c, k) / C(n, k)   if n - c >= k else 1.0
n = total samples, c = correct samples, k = target*
- `classify_error` (line 32) `def classify_error(msg, candidate_src)` - *Heuristic single-label error classifier.*
- `load_jsonl` (line 56) `def load_jsonl(path)`
- `summarize` (line 61) `def summarize(paths)`
- `main` (line 103) `def main()`

#### `analyze_results.py`
**Path:** `eval/analyze_results.py`

**Functions:**
- `load_records` (line 26) `def load_records(path)`
- `summarize` (line 31) `def summarize(records)`
- `show_failures` (line 44) `def show_failures(records, task_id)`
- `main` (line 82) `def main()`

#### `diag_static.py`
**Path:** `eval/diag_static.py`

**Functions:**
- `phase_discretization` (line 49) `def phase_discretization(K, n_samples, seed)` - *Muestrea n_samples overlaps aleatorios <u_i | u_j> sobre los vectores
singulares de K y mide cuanto se aleja su fase arg del reticulo 2*pi*Z.

delta = max |theta/2pi - round(theta/2pi)| sobre la muestra.

Tambien devuelve:
  delta_mean, delta_median, frac_near_integer (|.| < 0.05)*
- `synthetic_winding` (line 95) `def synthetic_winding(K, n_windows, window_size)` - *Como el checkpoint es estatico, no hay trayectoria temporal.
Construimos una pseudo-trayectoria deslizando una ventana sobre
los modos de frecuencia (filas de K) y acumulando arg det del
overlap entre ventanas consecutivas.

W = (1/2pi) sum_n arg det <U_{n} | U_{n+1}>*
- `static_kappa` (line 144) `def static_kappa(K)`
- `main` (line 168) `def main()`

#### `governor.py`
**Path:** `eval/governor.py`

**Classes:**
- `TokenStream` (line 45) `class TokenStream` - *Thread-safe single-producer / single-consumer queue of token IDs.

The producer (the generation loop) calls `put(tok)` for each new
token. Consumers can iterate via `iter_tokens(block=True)` or
`drain()` to get everything emitted so far.

The stream tracks a monotonic counter so consumers can detect
"no new tokens since last call" cheaply.*
- `StopReason` (line 99) `class StopReason(str, Enum)`
- `GenerationResult` (line 109) `class GenerationResult` - *Outcome of a governed generation.*
- `GenerationGovernor` (line 134) `class GenerationGovernor` - *Run a model's autoregressive generation loop with optional stop
hooks and a streaming interface.

Usage:
    ts = TokenStream()
    governor = GenerationGovernor(
        model=model,
        ctx=prompt_tensor,
        stream=ts,
        max_new_tokens=256,
        temperature=0.2,
        top_k=40,
        repetition_penalty=1.1,
    )
    result = governor.run(stop_hooks=[loop_detector, timeout_hook])
    if result.stop_reason == StopReason.LOOP:
        ...*

**Functions:**
- `make_loop_detector` (line 285) `def make_loop_detector(window, min_repeats)` - *Return True if the last `window` tokens contain a sub-sequence
of length >= `min_repeats` that repeats consecutively.

Catches the "model is stuck in a loop" pathology where a 24M-param
model emits the same 4-token pattern indefinitely.*
- `make_timeout_hook` (line 314) `def make_timeout_hook(per_token_s)` - *Return True if the per-token wall time exceeds `per_token_s`.
Useful for catching token-generation stalls (rare on CPU, but
happens under memory pressure).*
- `__init__` (line 56) `def __init__(self)`
- `put` (line 62) `def put(self, tok)`
- `mark_done` (line 67) `def mark_done(self)`
- `drain` (line 72) `def drain(self)` - *Return all tokens emitted so far, atomic snapshot.*
- `wait_for_new` (line 77) `def wait_for_new(self, timeout)` - *Block up to `timeout` seconds for a new token. Returns True
if a new token arrived (or stream closed), False on timeout.*
- `is_closed` (line 86) `def is_closed(self)`
- `__len__` (line 90) `def __len__(self)`
- `__post_init__` (line 117) `def __post_init__(self)`
- `__init__` (line 156) `def __init__(self, model, ctx, stream, max_new_tokens, temperature, top_k, repetition_penalty, max_seq_len)`
- `cancel` (line 177) `def cancel(self)` - *Asynchronously stop the generation. Safe to call from any
thread (e.g. a watchdog thread or the main UI loop).*
- `_should_cancel` (line 182) `def _should_cancel(self)`
- `run` (line 185) `def run(self, stop_hooks)` - *Execute the generation loop. Returns when the model emits
EOS, hits max_new_tokens, a hook returns True, or cancel() is
called.*
- `hook` (line 292) `def hook(generated)`
- `hook` (line 320) `def hook(generated)`

#### `governor_smoke.py`
**Path:** `eval/governor_smoke.py`

**Functions:**
- `load_model` (line 30) `def load_model()`
- `test_tokenstream_threadsafety` (line 49) `def test_tokenstream_threadsafety()`
- `test_governor_basic` (line 79) `def test_governor_basic()`
- `test_loop_detector` (line 98) `def test_loop_detector()`
- `test_cancel` (line 118) `def test_cancel()`
- `producer` (line 53) `def producer()`
- `consumer` (line 59) `def consumer()`

#### `harness.py`
**Path:** `eval/harness.py`

**Classes:**
- `ModelLoader` (line 217) `class ModelLoader` - *Build the model and tokenizer once, run many generations.*

**Functions:**
- `load_humaneval` (line 59) `def load_humaneval(cache_dir)`
- `build_prompt` (line 75) `def build_prompt(problem)` - *Return the exact prompt text fed to the model.

HumanEval's `prompt` field already contains the function signature and
docstring, with the body to be completed starting on the next line.*
- `extract_candidate` (line 100) `def extract_candidate(prompt, completion)` - *Combine prompt + completion into a single Python source string.

The completion may itself start with whitespace/indentation that
belongs inside the function body. We strip leading blank lines and
then concatenate; we also stop at the first top-level `def ` or
`class ` to avoid the model continuing with extra functions.

Robustness fixes:
  - Strip the special <|endoftext|> (GPT-2 EOT) token that the model
    emits at the end of every generation. Leaving it in the candidate
    produces a SyntaxError and zeroes the pass rate.
  - Drop any training-format delimiters (### Response, <|assistant|>,
    <|user|>) that leak from the instruction-tuning corpus.
  - Cut at the first top-level def/class/__main__ guard after the
    function body has started.*
- `run_one_test` (line 150) `def run_one_test(problem, candidate_src, timeout)` - *Execute the candidate against the hidden test.

Returns (passed, message, stdout, stderr, traceback). We follow HumanEval's
`evaluate` function: build namespace, exec the candidate, exec the test,
expect `check(candidate) == None`.*
- `run_one_test_sandboxed` (line 172) `def run_one_test_sandboxed(problem, candidate_src, timeout, sandbox_cfg)` - *Sandboxed variant of `run_one_test`. Runs the candidate in a
subprocess with stripped builtins, AST pre-check, and OS-enforced
timeout. Drop-in replacement: same 5-tuple return.

Enable by passing `--sandbox` to `harness.py` (not yet wired) or
by calling this function directly from your own evaluation script.*
- `make_sampler` (line 195) `def make_sampler(mode, settings_kwargs)` - *Backwards-compatible shim. The real implementation lives in
`eval.samplers` as a decorator-based registry. We re-export here
so existing imports of `from eval.harness import make_sampler`
keep working. New code should import from `eval.samplers`.*
- `completion_for_problem` (line 204) `def completion_for_problem(sampler, prompt)` - *Run a single completion and return (raw_output_text, metrics_dict).*
- `evaluate_problem` (line 272) `def evaluate_problem(problem, loader, args, sample_idx)`
- `main` (line 315) `def main()`
- `__init__` (line 220) `def __init__(self, ckpt_dir, ckpt_name, device)`
- `generate` (line 246) `def generate(self, prompt, max_new_tokens, temperature, top_k, repetition_penalty)`

#### `integration_smoke.py`
**Path:** `eval/integration_smoke.py`

**Functions:**
- `main` (line 18) `def main()`

#### `noise_analysis.py`
**Path:** `eval/noise_analysis.py`

**Functions:**
- `_load` (line 43) `def _load(p)`
- `consistency_across_runs` (line 47) `def consistency_across_runs(per_run)` - *Para cada problema, mira si pasa consistentemente a traves de los
4 niveles de ruido. Devuelve:
  - always_pass, always_fail, mixed (count)
  - per_sigma_pass_lists: {sigma: {task_id: bool}}*
- `main` (line 83) `def main()`

#### `noise_sweep.py`
**Path:** `eval/noise_sweep.py`

**Functions:**
- `inject_noise` (line 46) `def inject_noise(model, sigma, seed)` - *Anade N(0, sigma) a TODOS los kernels espectrales (kr_*, ki_*).
Retorna un dict con conteo de tensores ruidosos y de parametros
modificados.*
- `load_model` (line 74) `def load_model(ckpt_dir, ckpt_name, device)` - *Reconstruye TopoGPT2 alineado con el checkpoint, sin acceso a
harness.ModelLoader (queremos un loader limpio que no comparta
estado con corridas paralelas).*
- `generate_one` (line 99) `def generate_one(model, tok, prompt, max_new_tokens, device)`
- `main` (line 117) `def main()`

#### `repair.py`
**Path:** `eval/repair.py`

**Functions:**
- `_new_loader` (line 36) `def _new_loader(ckpt_dir, ckpt_name)`
- `extract_candidate` (line 49) `def extract_candidate(prompt, completion)`
- `run_test` (line 75) `def run_test(problem, candidate_src)`
- `build_repair_prompt` (line 89) `def build_repair_prompt(prompt, candidate, err, entry_point)`
- `gen` (line 104) `def gen(model, tok, text, max_new_tokens, temperature, top_k, rep_penalty)`
- `main` (line 119) `def main()`

#### `report.py`
**Path:** `eval/report.py`

**Functions:**
- `pass_at_k` (line 25) `def pass_at_k(n, c, k)`
- `classify_error` (line 31) `def classify_error(msg)`
- `load_jsonl` (line 52) `def load_jsonl(p)`
- `summarize_run` (line 56) `def summarize_run(p)`
- `repair_summary` (line 90) `def repair_summary(repair_path, baseline_path)`
- `main` (line 117) `def main()`

#### `samplers.py`
**Path:** `eval/samplers.py`

**Functions:**
- `register_sampler` (line 36) `def register_sampler(name)` - *Decorator. Register a factory under `name`. If `enabled_env` is set,
the factory is only registered when that env var is truthy. This
mirrors the `feature('XXX')` gating in claude-code-main/src/tools.ts.*
- `_is_env_truthy` (line 55) `def _is_env_truthy(name)`
- `_make_standard` (line 64) `def _make_standard(settings_kwargs)`
- `_make_hrm` (line 69) `def _make_hrm(settings_kwargs)`
- `list_samplers` (line 86) `def list_samplers()`
- `build_sampler` (line 90) `def build_sampler(mode, settings_kwargs)` - *Construct a sampler. Drop-in replacement for the old
`make_sampler(mode, settings_kwargs)` in `eval.harness`.*
- `deco` (line 42) `def deco(fn)`

#### `sandbox.py`
**Path:** `eval/sandbox.py`

**Classes:**
- `SandboxConfig` (line 53) `class SandboxConfig` - *One knob per defence layer. Defaults match HumanEval-style eval.*

**Functions:**
- `_names_imported` (line 100) `def _names_imported(tree)` - *Return the set of top-level names brought into scope by imports.*
- `_blocked_dunder_access` (line 114) `def _blocked_dunder_access(tree, blocked)` - *Find Attribute nodes whose attr is in `blocked`. Returns attr names found.*
- `_max_depth` (line 123) `def _max_depth(tree)` - *Compute max nesting depth of the AST. Catches obfuscated huge trees.*
- `check_safety` (line 133) `def check_safety(source, cfg)` - *Return (ok, reason). `reason` is "" when ok, else a human-readable
one-line explanation. Reasons are stable (used in test fixtures).*
- `_build_worker_src` (line 254) `def _build_worker_src(allowed_builtin_names, program_src, blocked_modules)`
- `safe_exec` (line 270) `def safe_exec(program_src, cfg, extra_globals)` - *Execute `program_src` in a sandboxed child process. Returns the same
5-tuple as `eval.harness.run_one_test` for drop-in compatibility.

The child is killed (SIGKILL) by the OS after `cfg.timeout` seconds.*
- `describe_policy` (line 373) `def describe_policy(cfg)`
- `d` (line 125) `def d(node, cur)`

#### `sandbox_smoke.py`
**Path:** `eval/sandbox_smoke.py`

**Functions:**
- `main` (line 15) `def main()`

#### `smoke.py`
**Path:** `eval/smoke.py`

**Functions:**
- `run_standard` (line 17) `def run_standard()`
- `run_hrm` (line 36) `def run_hrm()`

#### `temp_sweep.py`
**Path:** `eval/temp_sweep.py`

**Functions:**
- `generate_one` (line 39) `def generate_one(model, tok, prompt, max_new_tokens, temperature, top_k, device, seed_offset)`
- `evaluate_problems` (line 58) `def evaluate_problems(model, tok, problems, max_new_tokens, temperature, top_k, n_samples, device)`
- `pass_at_k_unbiased` (line 88) `def pass_at_k_unbiased(n, c, k)`
- `summarize` (line 96) `def summarize(results, n_samples)`
- `main` (line 116) `def main()`

#### `synthetic_dataset.py`
**Path:** `synthetic_dataset.py`

**Classes:**
- `LLMBackend` (line 61) `class LLMBackend` - *Abstract LLM backend. Subclass for each provider.*
- `GroqBackend` (line 71) `class GroqBackend(LLMBackend)` - *Groq API backend using requests.

Supports models: llama-3.3-70b-versatile, deepseek-r1.
Set GROQ_API_KEY env var.*
- `OpenRouterBackend` (line 121) `class OpenRouterBackend(LLMBackend)` - *OpenRouter unified API backend.

Supports any OpenRouter model:
    anthropic/claude-3.5-sonnet,
    openai/gpt-4o,
    deepseek/deepseek-chat,
    google/gemini-2.0-flash-thinking,
Set OPENROUTER_API_KEY env var.*
- `OllamaBackend` (line 177) `class OllamaBackend(LLMBackend)` - *Ollama local inference backend.

Supports any local model: llama3.1:8b, granite4.1:3b, etc.
Connects to Ollama server at OLLAMA_HOST (default: http://localhost:11434).*
- `ProcessedManifest` (line 364) `class ProcessedManifest` - *Tracks processed files for resumability.*
- `SyntheticDatasetGenerator` (line 399) `class SyntheticDatasetGenerator` - *Generates synthetic instruction-tuning data from source files.

Pipeline (one LLM call per file):
    file → MASTER_PROMPT → LLM → validate → dedup → JSONL

Features:
- Streaming JSONL writes (bounded RAM)
- SHA256 dedup across corpus
- Resumable (manifest tracks progress)
- Threaded request batching for throughput
- Configurable quality thresholds*

**Functions:**
- `build_backend` (line 227) `def build_backend(provider, model)` - *Factory for LLM backends.*
- `validate_sample` (line 330) `def validate_sample(sample)` - *Validate that a generated sample meets quality bar.

Returns (is_valid, reason).*
- `build_logger` (line 614) `def build_logger(level)`
- `parse_args` (line 625) `def parse_args()`
- `load_paths` (line 652) `def load_paths(paths_arg, paths_file, max_files)` - *Load file paths from CLI args or file.*
- `main` (line 667) `def main()`
- `generate` (line 64) `def generate(self, prompt)`
- `name` (line 67) `def name(self)`
- `__init__` (line 78) `def __init__(self, model, api_key, max_tokens, temperature, timeout)`
- `name` (line 95) `def name(self)`
- `generate` (line 98) `def generate(self, prompt)`
- `__init__` (line 132) `def __init__(self, model, api_key, max_tokens, temperature, timeout)`
- `name` (line 151) `def name(self)`
- `generate` (line 154) `def generate(self, prompt)`
- `__init__` (line 184) `def __init__(self, model, host, max_tokens, temperature, timeout)`
- `name` (line 198) `def name(self)`
- `generate` (line 201) `def generate(self, prompt)`
- `load` (line 374) `def load(path)`
- `save` (line 387) `def save(self, path)`
- `__init__` (line 418) `def __init__(self, backend, output_path, manifest_path, logger, max_workers, max_file_chars)`
- `_jsonl_writer` (line 447) `def _jsonl_writer(self)` - *Background thread that drains the queue and writes JSONL lines.*
- `_enqueue_sample` (line 465) `def _enqueue_sample(self, sample)`
- `_flush_writer` (line 468) `def _flush_writer(self)`
- `_read_file` (line 477) `def _read_file(self, path)` - *Read file content and detect language. Truncate if needed.*
- `_build_prompt` (line 490) `def _build_prompt(self, content, lang)`
- `_generate_sample` (line 496) `def _generate_sample(self, content, lang)` - *Call LLM with retry logic.*
- `process_file` (line 533) `def process_file(self, path)` - *Process a single file. Returns True if a sample was written.*
- `process_batch` (line 568) `def process_batch(self, paths)` - *Process a batch of files in parallel using thread pool.*
- `finish` (line 590) `def finish(self)` - *Signal end of processing and flush writer.*

#### `__init__.py`
**Path:** `topogpt3/__init__.py`

*No symbols extracted*

#### `inference.py`
**Path:** `topogpt3/inference.py`

**Classes:**
- `ScalePreset` (line 32) `class ScalePreset` - *Immutable architecture preset for a named model scale.*
- `InferenceSettings` (line 42) `class InferenceSettings` - *Centralized configuration container for the inference pipeline.

Every value consumed downstream resides here. Adding a new tunable means
extending this class; no other module should embed literals.*
- `InferenceLoggerFactory` (line 155) `class InferenceLoggerFactory` - *Builds a stdout-attached logger from inference settings.*
- `SecurePathResolver` (line 175) `class SecurePathResolver` - *Resolves filesystem paths while rejecting traversal outside their root.*
- `SourceModuleLoader` (line 209) `class SourceModuleLoader` - *Resolves the TopoGPT3 runtime module via the package import system.*
- `CheckpointPaths` (line 225) `class CheckpointPaths` - *Computes and validates checkpoint file paths under a single root.*
- `WeightShapeProbe` (line 271) `class WeightShapeProbe` - *Reads tensor metadata from safetensors to infer architecture details.*
- `TopoGPT2ConfigAligner` (line 315) `class TopoGPT2ConfigAligner` - *Builds a TopoGPT2Config matching the loaded checkpoint and tokenizer.*
- `TokenizerFactory` (line 346) `class TokenizerFactory` - *Builds a BPETokenizer instance using the configured encoding.*
- `GaussPatchApplier` (line 359) `class GaussPatchApplier` - *Applies the idempotent Gauss complex-multiply patch when enabled.*
- `ModelAssembler` (line 377) `class ModelAssembler` - *Instantiates the model and loads weights from safetensors.*
- `SeedSynchronizer` (line 414) `class SeedSynchronizer` - *Applies deterministic seeds across torch, CUDA and the model package.*
- `SamplingPolicy` (line 438) `class SamplingPolicy` - *Immutable sampling parameters consumed by the generation engine.*
- `GenerationReport` (line 458) `class GenerationReport` - *Quantitative summary of a single generation call.*
- `GenerationEngine` (line 472) `class GenerationEngine` - *Runs autoregressive sampling against a loaded model and tokenizer.*
- `ResultRenderer` (line 518) `class ResultRenderer` - *Prints a GenerationReport to stdout using settings-defined formatting.*
- `InferencePipeline` (line 547) `class InferencePipeline` - *Orchestrator wiring loader, builder, engine and renderer.*
- `CliArgumentParser` (line 600) `class CliArgumentParser` - *Translates command-line arguments into an InferenceSettings instance.*

**Functions:**
- `main` (line 695) `def main(argv)` - *CLI entry point. Returns a process exit code.*
- `scale_presets` (line 100) `def scale_presets()` - *Return the architecture preset table indexed by scale name.*
- `preset` (line 113) `def preset(self)` - *Return the resolved preset for the configured model scale.*
- `validate` (line 123) `def validate(self)` - *Raise ValueError if any setting falls outside its safety bounds.*
- `build` (line 159) `def build(settings)` - *Return a configured Logger with a single deduplicated stdout handler.*
- `resolve_under` (line 179) `def resolve_under(root)` - *Join `parts` under `root` and return the canonical resolved path.

Raises ValueError if the resolved path escapes `root`.*
- `require_existing_file` (line 195) `def require_existing_file(path, expected_suffix)` - *Validate `path` points to an existing regular file with the expected suffix.*
- `__init__` (line 212) `def __init__(self, settings, logger)`
- `load` (line 216) `def load(self)` - *Return the topogpt3.train module which re-exports model symbols.*
- `__init__` (line 228) `def __init__(self, settings)`
- `slot_dir` (line 236) `def slot_dir(self)` - *Directory holding the active checkpoint slot.*
- `model_file` (line 240) `def model_file(self)` - *Resolved path to the safetensors weights file inside the slot.*
- `state_file` (line 246) `def state_file(self)` - *Resolved path to the JSON training-state file inside the slot.*
- `assert_ready` (line 252) `def assert_ready(self)` - *Verify weights exist and the on-disk size lies within safety bounds.*
- `__init__` (line 274) `def __init__(self, settings, logger)`
- `detect_n_kv_heads` (line 278) `def detect_n_kv_heads(self, weights_path, d_model, n_heads)` - *Recover N_KV_HEADS used at training by inspecting the k_proj shape.

Returns None when the probe key is absent, signalling the caller to
fall back to scale defaults rather than guess.*
- `__init__` (line 318) `def __init__(self, settings, source_module, logger)`
- `build` (line 324) `def build(self, n_kv_heads, vocab_size)` - *Return a TopoGPT2Config dataclass ready to instantiate the model.*
- `__init__` (line 349) `def __init__(self, settings, source_module)`
- `build` (line 353) `def build(self)` - *Return an instance of BPETokenizer bound to the configured encoding.*
- `__init__` (line 362) `def __init__(self, settings, source_module, logger)`
- `apply_if_enabled` (line 368) `def apply_if_enabled(self)` - *Patch QuaternionSpectralLayer to use the 3-multiply Gauss contract.*
- `__init__` (line 380) `def __init__(self, settings, source_module, logger)`
- `assemble` (line 386) `def assemble(self, aligned_cfg, paths)` - *Build the TopoGPT2 graph, load weights into it, and return it in eval mode.*
- `__init__` (line 417) `def __init__(self, settings, source_module, logger)`
- `apply` (line 423) `def apply(self)` - *Seed all relevant RNGs using the model package helper when available.*
- `from_settings` (line 447) `def from_settings(cls, settings)` - *Construct a SamplingPolicy from inference settings.*
- `tokens_per_second` (line 467) `def tokens_per_second(self, elapsed_floor)` - *Return throughput in tokens/sec, clamped to avoid divide-by-zero.*
- `__init__` (line 475) `def __init__(self, settings, logger)`
- `run` (line 480) `def run(self, model, tokenizer, prompt, policy)` - *Generate a completion for `prompt` and return a GenerationReport.*
- `__init__` (line 521) `def __init__(self, settings, logger)`
- `render` (line 525) `def render(self, report)` - *Emit a banner with prompt and completion, plus a throughput log line.*
- `__init__` (line 550) `def __init__(self, settings, logger)`
- `execute` (line 556) `def execute(self)` - *Run the full inference pipeline end-to-end and return the report.*
- `build_parser` (line 604) `def build_parser()` - *Return the configured argparse.ArgumentParser.*
- `parse` (line 674) `def parse(argv)` - *Parse `argv` (or sys.argv) and return a populated InferenceSettings.*

#### `inference_hrm.py`
**Path:** `topogpt3/inference_hrm.py`

**Classes:**
- `ScalePreset` (line 54) `class ScalePreset` - *Immutable architecture preset for a named model scale.*
- `RecursiveReasoningConfig` (line 64) `class RecursiveReasoningConfig` - *Hyperparameters governing the hierarchical recursive thinking loop.

The semantics follow the HRM and GRAM literature, adapted to operate
safely with zero additional learnable parameters on a model that was
not trained with recurrence in its computational graph. The reasoner
performs damped fixed-point iteration entirely in the residual-stream
space produced by the baseline forward pass; deep activations are never
fed back into the token-embedding-input layers, preserving the trained
activation distribution at every layer boundary.

Attributes:
    enabled: master switch; when False the pipeline degrades to the
        standard non-recursive autoregressive loop.
    max_high_level_iters: maximum slow-loop iterations per emitted token.
        Each iteration applies a deeper trailing window of layers.
    max_low_level_iters: maximum fast-loop iterations per high-level step.
        Each iteration applies the short trailing window of layers.
    low_level_window: number of trailing transformer layers iterated by
        the low-level fast loop.
    high_level_window: number of trailing transformer layers iterated by
        the high-level slow loop. Should be greater than or equal to
        low_level_window so the hierarchy matches the HRM coarse/fine
        split.
    low_level_step: damping coefficient in [0, 1] for the low-level
        update rule z <- z + step * (window(z) - z).
    high_level_step: damping coefficient for the high-level update.
    attractor_low_epsilon: relative L2 change threshold that declares the
        low-level state converged.
    attractor_high_epsilon: relative L2 change threshold that declares the
        high-level state converged.
    high_level_persist_tokens: tokens during which the refinement vector
        is reused as a warm start before being re-initialized to zero.
        This is the sparse temporal-memory dimension.
    cache_warm_start_weight: scalar in [0, 1] applied to the cached
        refinement before warm-starting the next token's iteration.
    max_drift_relative: relative L2 distance ceiling between the iterated
        latent and the baseline latent; exceeding it triggers a reset to
        the baseline state and aborts thinking for the current token.
    latent_change_eps: floor used in the denominator of relative change
        computations to avoid division by zero.
    safety_max_total_iterations: hard cap on total layer invocations per
        emitted token regardless of configured iters.
    minimum_low_level_iters: floor on low-level iterations before
        convergence checks may halt the loop.
    minimum_high_level_iters: floor on high-level iterations before
        convergence checks may halt the loop.
    diagnostic_logging: when True, emits per-token iteration statistics.*
- `HRMInferenceSettings` (line 134) `class HRMInferenceSettings` - *Centralized configuration for the TopoGPT3.1 inference pipeline.

Every value consumed downstream resides here. Extending the pipeline with
a new tunable means extending this dataclass; no other module should
embed literals.*
- `HRMLoggerFactory` (line 339) `class HRMLoggerFactory` - *Builds a stdout-attached logger from inference settings.*
- `SecurePathResolver` (line 359) `class SecurePathResolver` - *Resolves filesystem paths while rejecting traversal outside their root.*
- `SourceModuleLoader` (line 393) `class SourceModuleLoader` - *Resolves the TopoGPT3 runtime module via the package import system.*
- `CheckpointPaths` (line 409) `class CheckpointPaths` - *Computes and validates checkpoint file paths under a single root.*
- `WeightShapeProbe` (line 455) `class WeightShapeProbe` - *Reads tensor metadata from safetensors to infer architecture details.*
- `TopoGPT2ConfigAligner` (line 498) `class TopoGPT2ConfigAligner` - *Builds a TopoGPT2Config matching the loaded checkpoint and tokenizer.*
- `TokenizerFactory` (line 529) `class TokenizerFactory` - *Builds a BPETokenizer instance using the configured encoding.*
- `GaussPatchApplier` (line 542) `class GaussPatchApplier` - *Applies the idempotent Gauss complex-multiply patch when enabled.*
- `ModelAssembler` (line 560) `class ModelAssembler` - *Instantiates the model and loads weights from safetensors.*
- `SeedSynchronizer` (line 597) `class SeedSynchronizer` - *Applies deterministic seeds across torch, CUDA and the model package.*
- `LatentChangeMetric` (line 620) `class LatentChangeMetric` - *Computes the relative L2 distance between two latent tensors.*
- `ReasoningIterationStats` (line 644) `class ReasoningIterationStats` - *Aggregated counters describing a single token's reasoning episode.*
- `GenerationReasoningSummary` (line 657) `class GenerationReasoningSummary` - *Aggregated statistics over the full generation episode.*
- `SparseHighLevelStateCache` (line 680) `class SparseHighLevelStateCache` - *Persists the high-level latent state across consecutive emitted tokens.

The cache is reset whenever its age in tokens reaches the configured
persistence horizon, at which point the next reasoning episode begins
with a zero high-level state. This is the temporal-sparsity mechanism:
expensive full-stack passes are amortized across multiple emissions.*
- `HierarchicalRecursiveReasoner` (line 723) `class HierarchicalRecursiveReasoner` - *Parameter-free hierarchical recursive reasoning over a trained stack.

The reasoner does not own any learnable parameters. It treats the trained
TopoGPT2 transformer layers as a deterministic recurrent step function
and composes them into a two-speed damped fixed-point iteration that
mirrors HRM, while never violating the activation distribution the
trained layers expect.

Algorithm per emitted token:

    1. Run the standard full forward pass once to obtain the baseline
       residual-stream latent z_base and the per-layer kv caches that
       will cross the token boundary. z_base is the trained model's
       native answer for this position.
    2. If recursion is disabled or both iteration budgets are zero,
       return z_base unchanged.
    3. Optionally warm-start z by adding a fraction of the cached
       refinement vector from previous tokens (sparse temporal memory).
    4. Hierarchical refinement, all in residual-stream space:
          for h_step in range(max_high_level_iters):
              for l_step in range(max_low_level_iters):
                  z <- z + low_level_step * (W_low(z) - z)
              z <- z + high_level_step * (W_high(z) - z)
       where W_low and W_high are the last low_level_window and
       high_level_window trained layers respectively, invoked with the
       prefix kv cache treated as immutable. Each update is damped, so
       layer inputs remain close to the trained residual-stream
       distribution.
    5. Hard divergence guard: if the iterated latent drifts farther
       from the baseline than max_drift_relative, reset to the baseline
       and abort thinking for this token. This eliminates the
       catastrophic-attractor failure mode without retraining.
    6. Attractor halting per loop, plus a global cap on total layer
       invocations.

The cached refinement returned to the sparse cache is z_final - z_base,
a small residual-stream displacement that persists across configurable
horizons to amortize thinking effort over multiple tokens.*
- `LogitsSampler` (line 931) `class LogitsSampler` - *Applies temperature, repetition penalty, top-k filtering and multinomial draw.*
- `SamplingPolicy` (line 959) `class SamplingPolicy` - *Immutable sampling parameters consumed by the generation engine.*
- `GenerationReport` (line 981) `class GenerationReport` - *Quantitative summary of a single generation call.*
- `HRMGenerationEngine` (line 996) `class HRMGenerationEngine` - *Runs autoregressive sampling driven by hierarchical recursive reasoning.

The engine reimplements the prompt encoding and token emission loop so
that the per-token latent state can be intercepted before final norm and
LM-head projection. The intercepted state is handed to a
HierarchicalRecursiveReasoner, which iterates the trained layer stack in
a two-speed loop until the attractor is reached. The final stabilized
latent is then projected to logits and sampled in the standard fashion.*
- `ResultRenderer` (line 1124) `class ResultRenderer` - *Prints a GenerationReport to stdout using settings-defined formatting.*
- `HRMInferencePipeline` (line 1165) `class HRMInferencePipeline` - *Orchestrator wiring loader, builder, reasoner, engine and renderer.*
- `CliArgumentParser` (line 1218) `class CliArgumentParser` - *Translates command-line arguments into an HRMInferenceSettings instance.*

**Functions:**
- `main` (line 1410) `def main(argv)` - *CLI entry point. Returns a process exit code.*
- `scale_presets` (line 217) `def scale_presets()` - *Return the architecture preset table indexed by scale name.*
- `preset` (line 230) `def preset(self)` - *Return the resolved preset for the configured model scale.*
- `validate` (line 240) `def validate(self)` - *Raise ValueError if any setting falls outside its safety bounds.*
- `build` (line 343) `def build(settings)` - *Return a configured Logger with a single deduplicated stdout handler.*
- `resolve_under` (line 363) `def resolve_under(root)` - *Join parts under root and return the canonical resolved path.

Raises ValueError if the resolved path escapes root.*
- `require_existing_file` (line 379) `def require_existing_file(path, expected_suffix)` - *Validate path points to an existing regular file with the expected suffix.*
- `__init__` (line 396) `def __init__(self, settings, logger)`
- `load` (line 400) `def load(self)` - *Return the topogpt3.train module which re-exports model symbols.*
- `__init__` (line 412) `def __init__(self, settings)`
- `slot_dir` (line 420) `def slot_dir(self)` - *Directory holding the active checkpoint slot.*
- `model_file` (line 424) `def model_file(self)` - *Resolved path to the safetensors weights file inside the slot.*
- `state_file` (line 430) `def state_file(self)` - *Resolved path to the JSON training-state file inside the slot.*
- `assert_ready` (line 436) `def assert_ready(self)` - *Verify weights exist and the on-disk size lies within safety bounds.*
- `__init__` (line 458) `def __init__(self, settings, logger)`
- `detect_n_kv_heads` (line 462) `def detect_n_kv_heads(self, weights_path, d_model, n_heads)` - *Recover N_KV_HEADS used at training by inspecting the k_proj shape.

Returns None when the probe key is absent, signalling the caller to
fall back to scale defaults rather than guess.*
- `__init__` (line 501) `def __init__(self, settings, source_module, logger)`
- `build` (line 507) `def build(self, n_kv_heads, vocab_size)` - *Return a TopoGPT2Config dataclass ready to instantiate the model.*
- `__init__` (line 532) `def __init__(self, settings, source_module)`
- `build` (line 536) `def build(self)` - *Return an instance of BPETokenizer bound to the configured encoding.*
- `__init__` (line 545) `def __init__(self, settings, source_module, logger)`
- `apply_if_enabled` (line 551) `def apply_if_enabled(self)` - *Patch QuaternionSpectralLayer to use the 3-multiply Gauss contract.*
- `__init__` (line 563) `def __init__(self, settings, source_module, logger)`
- `assemble` (line 569) `def assemble(self, aligned_cfg, paths)` - *Build the TopoGPT2 graph, load weights into it, and return it in eval mode.*
- `__init__` (line 600) `def __init__(self, settings, source_module, logger)`
- `apply` (line 606) `def apply(self)` - *Seed all relevant RNGs using the model package helper when available.*
- `__init__` (line 623) `def __init__(self, epsilon_floor)`
- `relative_change` (line 628) `def relative_change(self, current, previous)` - *Return ||current - previous|| / max(||previous||, epsilon_floor).*
- `absorb` (line 667) `def absorb(self, sample)` - *Fold a per-token sample into the running totals.*
- `__init__` (line 689) `def __init__(self, persist_tokens)`
- `get_or_init` (line 696) `def get_or_init(self, reference)` - *Return the cached high-level state or a zeroed one when stale.

The boolean flag indicates whether the returned tensor came from a
live cache hit (True) or a fresh zero initialization (False).*
- `commit` (line 712) `def commit(self, new_state)` - *Store a fresh high-level state and increment the cache age.*
- `invalidate` (line 717) `def invalidate(self)` - *Drop any cached state and reset the age counter.*
- `__init__` (line 764) `def __init__(self, layers, final_norm, reasoning_config, logger)`
- `num_layers` (line 785) `def num_layers(self)` - *Return the number of trained transformer layers.*
- `_full_pass` (line 789) `def _full_pass(self, z_in, base_kvs)` - *Forward z_in through every layer using base_kvs as immutable prefix cache.

Returns the layer-stack output and the freshly produced per-layer kv
caches that incorporate the K and V derived from z_in.*
- `_window_pass` (line 804) `def _window_pass(self, z_in, base_kvs, window)` - *Forward z_in through the trailing `window` layers only.

The per-layer kv caches produced during this read-only pass are
discarded; only the baseline pass's committed kvs cross the token
boundary, preserving cache consistency across thinking iterations.*
- `reason` (line 823) `def reason(self, z_initial, base_kvs, cached_refinement)` - *Run hierarchical recursive thinking for a single emission step.

Args:
    z_initial: token embedding of the new position, shape [B, 1, D].
    base_kvs: per-layer kv cache for all previously emitted tokens,
        treated as immutable during thinking iterations.
    cached_refinement: persistent refinement displacement from prior
        tokens, or None to skip the warm start.

Returns:
    A tuple (z_final, committed_kvs, refinement_for_cache, stats):
        z_final is the latent state about to enter the final norm
        and lm head; committed_kvs is the new per-layer kv cache
        including this token's K and V from the baseline pass;
        refinement_for_cache is z_final - z_baseline, to be
        persisted across tokens; stats holds the loop counters.*
- `__init__` (line 934) `def __init__(self, logger)`
- `sample` (line 937) `def sample(self, logits, token_history, temperature, top_k, repetition_penalty)` - *Return a sampled token id tensor of shape [B, 1] from raw logits [B, V].*
- `from_settings` (line 969) `def from_settings(cls, settings)` - *Construct a SamplingPolicy from inference settings.*
- `tokens_per_second` (line 991) `def tokens_per_second(self, elapsed_floor)` - *Return throughput in tokens/sec, clamped to avoid divide-by-zero.*
- `__init__` (line 1007) `def __init__(self, settings, logger)`
- `_encode_prompt` (line 1012) `def _encode_prompt(self, model, prompt_ids)` - *Run the prompt through the full stack once, returning the final
hidden state of the last position, the per-layer base kv caches that
cover all prompt tokens except the last one, and the embedding of the
last prompt token as the seed for the first reasoning episode.*
- `run` (line 1044) `def run(self, model, tokenizer, prompt, policy)` - *Generate a completion for prompt and return a GenerationReport.*
- `__init__` (line 1127) `def __init__(self, settings, logger)`
- `render` (line 1131) `def render(self, report)` - *Emit a banner with prompt, completion, throughput and reasoning stats.*
- `__init__` (line 1168) `def __init__(self, settings, logger)`
- `execute` (line 1174) `def execute(self)` - *Run the full inference pipeline end-to-end and return the report.*
- `build_parser` (line 1222) `def build_parser()` - *Return the configured argparse.ArgumentParser.*
- `parse` (line 1367) `def parse(argv)` - *Parse argv (or sys.argv) and return a populated HRMInferenceSettings.*

#### `model.py`
**Path:** `topogpt3/model.py`

**Classes:**
- `TopoGPT2Config` (line 56) `class TopoGPT2Config` - *Configuración completa para TopoGPT2.*
- `QuaternionOps` (line 207) `class QuaternionOps` - *Operaciones de cuaterniones puras en PyTorch.
Representación: [..., 4]  donde last dim = [w, x, y, z]
q = w + x*i + y*j + z*k*
- `QuaternionLinear` (line 246) `class QuaternionLinear` - *Capa lineal con pesos cuaterniones.

Implementa la multiplicación W * x en el álgebra de cuaterniones:
- W = Ww + Wx*i + Wy*j + Wz*k  (cuaternión de pesos)
- x = xw + xx*i + xy*j + xz*k  (cuaternión de entrada)
- out = W * x  (producto de Hamilton extendido a vectores)

Parámetros: 4 matrices reales de forma [out_q, in_q]*
- `QuaternionSpectralLayer` (line 291) `class QuaternionSpectralLayer` - *Convolución espectral 2D con cuaterniones y producto de Hamilton completo.

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

Cada Wc es un kernel complejo (partes real e imaginaria independientes).*
- `SpectralAutoencoder` (line 378) `class SpectralAutoencoder` - *Autoencoder espectral con cuaterniones.

Opera en dos niveles:
1. Espectral 1D sobre el vector de features (FFT sobre dim D_MODEL):
   captura la espectrografía global del embedding.
2. Espectral 2D sobre el grid del toro (QuaternionSpectralLayer):
   captura correlaciones espaciales en la topología.

Devuelve (latent, recon_loss) para regularización.*
- `QuaternionTorusBrain` (line 461) `class QuaternionTorusBrain` - *Reemplaza el MLP en cada capa del transformer.

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
8. Reshape: [B·S, D] → [B, S, D]*
- `RotaryEmbedding` (line 678) `class RotaryEmbedding` - *Rotary Position Embeddings (RoPE) - Su et al., 2021.
Codifica la posición como rotaciones del espacio de atención,
naturalmente relativas y sin parámetros extra.*
- `RMSNorm` (line 726) `class RMSNorm` - *Root Mean Square Layer Normalization (sin bias). Más estable que LayerNorm.*
- `SwiGLU` (line 743) `class SwiGLU` - *SwiGLU: SiLU(gate(x)) * up(x) -> down
Usado en LLaMA 2/3, Qwen, Mistral en lugar de GELU-FFN.
Dimension interna: 8/3 * d_model (convención LLaMA, redondeada a múltiplo de 4).*
- `TopoMoEBrain` (line 772) `class TopoMoEBrain` - *Mixture of Experts sobre la capa topologica.

Arquitectura (inspirada en DeepSeek-MoE / Mixtral):
  - 1 experto compartido: QuaternionTorusBrain (siempre activo)
  - N_EXPERTS expertos SwiGLU ligeros (activacion esparsa: Top-K por token)
  - Router: Linear(D, N_EXPERTS) + softmax → top-K

Load-balancing loss (auxiliar): penaliza si un experto acapara todos los tokens.
Activa MOE_TOP_K de N_EXPERTS expertos por token.

Sin MoE (MOE_ENABLED=False): se comporta como QuaternionTorusBrain puro.*
- `MultiHeadAttention` (line 877) `class MultiHeadAttention` - *Multi-head attention con:
- Flash Attention (scaled_dot_product_attention de PyTorch 2.0+)
- Rotary Position Embeddings (RoPE)
- GQA (Grouped Query Attention): N_KV_HEADS < N_HEADS, reduce VRAM de K/V
- KV Cache para inferencia autoregresiva eficiente
- Temperatura termodinámica aprendible*
- `TopoGPT2Layer` (line 959) `class TopoGPT2Layer` - *Capa del transformer con TopoMoEBrain (TopoBrain + MoE SwiGLU experts).

Esquema pre-norm (estilo LLaMA):
    x = x + Attention_GQA(RMSNorm(x))
    x = x + TopoMoEBrain(RMSNorm(x))*
- `TopoGPT2` (line 1006) `class TopoGPT2` - *TopoGPT2: Transformer de lenguaje con TopoBrain cuaternión-espectral.

Arquitectura:
    Embedding de tokens + RoPE (en Attention)
    N_LAYERS × TopoGPT2Layer (Attention + QuaternionTorusBrain)
    RMSNorm final
    Proyección a vocabulario (weight-tied con embeddings)*
- `BPETokenizer` (line 1127) `class BPETokenizer` - *Wrapper alrededor de tiktoken (GPT-2 compatible).*
- `FileManifest` (line 1253) `class FileManifest` - *Disk-cached manifest of text files found in a directory tree.*
- `MemmapTokenizer` (line 1320) `class MemmapTokenizer` - *Tokenizes file paths into a memory-mapped numpy array on disk.

Uses incremental file reading and batched writing to avoid loading
all tokens into RAM. Tokens are stored as raw int64 on disk and
accessed via numpy memmap (OS-level paging, near-zero RAM footprint).*
- `MappedTokenDataset` (line 1409) `class MappedTokenDataset` - *Memory-mapped token dataset for sequence-to-sequence LM training.

The token array is backed by a numpy memmap file on disk.
Only accessed slices are paged into RAM by the OS. The .copy()
in __getitem__ ensures the returned torch.Tensor owns its memory,
which is required for DataLoader collation with worker processes.*
- `TextFilter` (line 1443) `class TextFilter` - *Filters low-quality files from the corpus based on multiple heuristics.*
- `CurriculumDataset` (line 1547) `class CurriculumDataset` - *Tiered dataset that exposes short/medium/all files based on line count.

Works as a wrapper around MappedTokenDataset. Provides __getitem__ that
only samples from the active tier, avoiding dataset duplication.*
- `ProgressiveSeqLenTrainer` (line 1611) `class ProgressiveSeqLenTrainer` - *Trainer that dynamically adjusts MAX_SEQ_LEN across training phases.

Phase schedule (configurable):
    phase 0: seq_len=128, epochs=3
    phase 1: seq_len=256, epochs=3
    phase 2: seq_len=512, epochs=4

Each phase rebuilds the DataLoader with the new sequence length.*
- `SpeculativeDecoder` (line 1687) `class SpeculativeDecoder` - *Speculative decoding with a small draft model.

Draft model uses SPEC_DECODE_DRAFT_SCALE (e.g. 'micro').
The draft generates K tokens, then the target model verifies them
in a single forward pass. Accepted tokens are kept; rejected ones
trigger a fallback to the target model sampling.*
- `QuantizedEmbedding` (line 1803) `class QuantizedEmbedding` - *Wrapper around nn.Embedding that applies dynamic quantization.

Applies int8 quantization to the embedding weight matrix after loading.
Supports both embed (int8) and FFN (int4) quantization modes.*
- `CurriculumTrainer` (line 1871) `class CurriculumTrainer` - *Extends TopoGPT2Trainer with curriculum + progressive seq len support.

Provides:
- Tokens cache for progressive sequence length rebuilding
- Curriculum dataset wrapping (short / medium / all tiers)*
- `CheckpointManager` (line 2023) `class CheckpointManager` - *Gestiona checkpoints de forma acumulativa y segura.

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
agrega nuevas entradas a train_loss[], val_loss[], etc.*
- `TopoGPT2Trainer` (line 2256) `class TopoGPT2Trainer` - *Entrenador acumulativo y resumible.

Caracteristicas:
- Checkpoint automatico en safetensors cada N minutos + cada epoch
- Historial acumulativo entre sesiones (--resume agrega al historial existente)
- Guarda el mejor modelo en checkpoints/best/ automaticamente
- LR schedule: cosine con warmup relativo a los steps de ESTA sesion
- Mixed Precision (AMP) + acumulacion de gradientes*
- `MechanisticMetrics` (line 2549) `class MechanisticMetrics` - *Calcula todas las metricas del diagrama de fases de Book.md.

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
sp:         superposicion = correlacion promedio inter-fila de pesos.*
- `Phase0_KernelOptimizer` (line 2786) `class Phase0_KernelOptimizer` - *Encuentra el ratio imaginario/real optimo para los kernels espectrales.

Analogia con main.py: evalua la transicion GOE→GUE en el espacio
de kernels. Un ratio optimo promueve estructura topologica (insulador)
vs estructura amorfa (vidrio).

Metodo: calibra con un mini-batch y mide la varianza del gradiente
en funcion del ratio. Ratios que minimizan la varianza de gradiente
(maxima coherencia espectral) son preferibles.

No entrena: solo inicializa los kernels con distintos ratios y mide.
Tiempo tipico: < 30 segundos.*
- `Phase1_BatchProspector` (line 2861) `class Phase1_BatchProspector` - *Encuentra el batch size optimo testando candidatos con pocos pasos.

De main.py: el batch size regula la temperatura del horno de cristalizacion.
Batch sizes demasiado chicos -> ruido excesivo (vidrio frio).
Batch sizes demasiado grandes -> sin presion annealing (amorfos).
La ventana optima empirica de main.py: [24, 128] para Strassen.

Para LM, testeamos candidatos midiendo:
- delta (δ): velocidad de descenso en prospect_steps pasos
- T_eff: temperatura efectiva del gradiente

Tiempo tipico: < 2 minutos para 3 candidatos × 30 pasos.*
- `Phase2_SeedMiner` (line 2944) `class Phase2_SeedMiner` - *Encuentra semillas prometedoras midiendo la trayectoria de delta.

De main.py: una semilla "buena" muestra delta descendente en los
primeros N pasos (enfriamiento). Una semilla "mala" se estanca en
el plateau vidrioso (~0.49).

Criterio de seleccion:
1. Semillas con delta_velocity < 0 (enfriando) AND kappa bajo.
2. Si no hay, semillas solo enfriando.
3. Fallback: semilla con menor delta final.

Tiempo tipico: < 3 minutos para 5 semillas × 50 pasos.*
- `Phase4_AnnealingRefiner` (line 3026) `class Phase4_AnnealingRefiner` - *Refinamiento post-entrenamiento mediante recocido simulado.

De main.py: despues de que el modelo converge, una fase de annealing
con criterio de aceptacion de Metropolis puede empujar los pesos
hacia estados de menor energia libre (menor delta o mejor val_loss).

Aceptacion de Metropolis:
    si Δloss < 0: siempre acepta (mejora)
    si Δloss >= 0: acepta con prob exp(-Δloss / T)

La temperatura T decae exponencialmente: T(t) = T0 * cooling_rate^t

Al rechazar: restaura el mejor estado conocido.
Si se estanca: perturbacion termica (ruido gaussiano en pesos).

Tiempo: proporcional a refine_epochs (user-controlled).*
- `TopoPhasePipelineV2` (line 3187) `class TopoPhasePipelineV2` - *Pipeline with curriculum learning and progressive sequence length.

Replaces TopoPhasePipeline when --curriculum or --progressive-seq-len is set.
Handles:
- Text quality filtering before tokenization (via TextFilter)
- Curriculum tiers (short/medium/all files)
- Progressive MAX_SEQ_LEN across phases: 128->256->512
- Tokens cached in memory for fast DataLoader rebuilding per phase*
- `TopoPhasePipeline` (line 3316) `class TopoPhasePipeline` - *Orquesta las 5 fases de entrenamiento segun main.py + Book.md.

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
  Sin flags: solo fase 3 (comportamiento original, identico a antes)*

**Functions:**
- `setup_logger` (line 185) `def setup_logger(name, level)`
- `set_seed` (line 195) `def set_seed(seed, device)`
- `build_file_tiers` (line 1585) `def build_file_tiers(paths, short, med)` - *Classify file paths into complexity tiers by line count.

Returns dict: tier -> list of file indices in that tier.
Tier 0 = short (<=short lines), tier 1 = medium, tier 2 = all.*
- `apply_quantization` (line 1843) `def apply_quantization(model, config)` - *Quantize embedding and lm_head layers for reduced VRAM usage.*
- `_tokenize_text_to_memmap` (line 2011) `def _tokenize_text_to_memmap(text, tokenizer, path, max_tokens)` - *Tokenize a single text string and write tokens to disk as raw int64.*
- `main` (line 3438) `def main()`
- `__post_init__` (line 154) `def __post_init__(self)`
- `hamilton_product` (line 215) `def hamilton_product(q1, q2)` - *Producto de Hamilton q1 ⊗ q2. Ambos [..., 4].*
- `normalize` (line 227) `def normalize(q, eps)`
- `conjugate` (line 231) `def conjugate(q)`
- `rotate_vector` (line 236) `def rotate_vector(v, q)` - *Rota vector 3D v por cuaternión unitario q. v:[...,3] q:[...,4]*
- `__init__` (line 258) `def __init__(self, in_features, out_features, bias)`
- `forward` (line 274) `def forward(self, x)` - *x: [..., in_features] → [..., out_features]*
- `__init__` (line 311) `def __init__(self, in_q, out_q, grid_h, grid_w, init_scale)`
- `_kernel` (line 330) `def _kernel(self, c)`
- `_contract` (line 333) `def _contract(self, W, X)` - *Suma sobre canales in_q: Y[b,o,h,w] = Σ_i W[i,o,h,w]·X[b,i,h,w]*
- `forward` (line 337) `def forward(self, x)` - *x: [B, 4*in_q, H, W]  (4 canales cuaterniones sobre grid espacial)
→ [B, 4*out_q, H, W]*
- `__init__` (line 391) `def __init__(self, config)`
- `_filter1d` (line 423) `def _filter1d(self, x, kr, ki)` - *Filtro espectral 1D: x[..., D] → filtrado[..., D]*
- `encode` (line 429) `def encode(self, x)` - *x: [..., D_MODEL] → latent: [..., D_LAT]*
- `decode` (line 434) `def decode(self, z)` - *z: [..., D_LAT] → recon: [..., D_MODEL]*
- `forward` (line 439) `def forward(self, x)` - *Devuelve (latent, recon_loss)*
- `process_torus_grid` (line 446) `def process_torus_grid(self, grid)` - *Procesa el grid del toro con QuaternionSpectralLayer.
grid: [B, 4*D_QUAT, RADIAL, ANGULAR]  →  [B, 4*D_QUAT, RADIAL, ANGULAR]*
- `__init__` (line 479) `def __init__(self, d_model, config)`
- `_build_torus_graph` (line 519) `def _build_torus_graph(self)` - *Construye las aristas del grafo toro 2×4.

Nodos indexados como: node = r * N_ANGULAR + a
  r ∈ [0, RADIAL-1], a ∈ [0, ANGULAR-1]

Aristas angulares: nodo ↔ nodo a la izquierda/derecha (periódico)
Aristas radiales:  nodo ↔ nodo del anillo interior/exterior*
- `_torus_soft_assign` (line 553) `def _torus_soft_assign(self, phi1, phi2)` - *Asignación blanda de tokens a los 8 nodos del toro via distancia circular.

phi1: [BS] ángulo angular ∈ [-π, π]
phi2: [BS] ángulo radial ∈ [-π, π]
→ weights: [BS, N_NODES]  (suma a 1, softmax de distancias negativas)*
- `_message_passing` (line 580) `def _message_passing(self, node_feat)` - *Message-passing VECTORIZADO con rotaciones cuaterniones.
Sin bucles Python: todas las aristas se procesan en paralelo.

node_feat: [BS, N_NODES, D_MODEL]
→ [BS, N_NODES, D_MODEL]*
- `forward` (line 617) `def forward(self, x)` - *x: [B, S, D_MODEL]
→ output: [B, S, D_MODEL], recon_loss: scalar*
- `__init__` (line 685) `def __init__(self, d_head, max_seq_len, base)`
- `_build_cache` (line 691) `def _build_cache(self, seq_len)`
- `_rotate_half` (line 698) `def _rotate_half(self, x)`
- `forward` (line 702) `def forward(self, q, k, seq_len, offset)` - *q, k: [B, n_heads, S_q/S_k, d_head]
offset: posicion inicial (para KV cache: longitud del cache existente)
Aplica posiciones [offset .. offset+S-1] a q y k.*
- `__init__` (line 729) `def __init__(self, d_model, eps)`
- `forward` (line 734) `def forward(self, x)`
- `__init__` (line 750) `def __init__(self, d_model, expansion, dropout)`
- `forward` (line 764) `def forward(self, x)`
- `__init__` (line 787) `def __init__(self, d_model, config)`
- `_route` (line 808) `def _route(self, x)` - *x: [N, D] donde N = B*S (tokens aplanados)
Retorna:
expert_out: [N, D]  suma ponderada de top-K expertos
aux_loss:   escalar  load-balancing loss
Routing vectorizado sin boolean indexing ni sincronizacion CUDA.
Usa dispatch por indices agrupados (estilo Mixtral/DeepSeek) para
compatibilidad total con torch.utils.checkpoint.*
- `forward` (line 850) `def forward(self, x)` - *x: [B, S, D]
→ output: [B, S, D], aux_loss: escalar*
- `__init__` (line 887) `def __init__(self, d_model, n_heads, config)`
- `forward` (line 905) `def forward(self, x, is_causal, past_kv)` - *Args:
    x:        [B, S, D]
    is_causal: usar mascara causal
    past_kv:  (K_cache, V_cache) de pasos anteriores o None
Returns:
    out:      [B, S, D]
    kv_cache: (K, V) completos para cachear en generate()*
- `__init__` (line 968) `def __init__(self, d_model, n_heads, config)`
- `_forward_impl` (line 977) `def _forward_impl(self, x, past_kv)`
- `forward` (line 986) `def forward(self, x, past_kv)` - *Retorna (x_out, aux_loss, kv_cache).
Con gradient checkpointing en training (solo cuando no hay KV cache).*
- `__init__` (line 1017) `def __init__(self, config)`
- `_init_weights` (line 1036) `def _init_weights(self)`
- `forward` (line 1043) `def forward(self, token_ids, past_kvs)` - *token_ids: [B, S]  (enteros)
past_kvs:  lista de (K, V) por capa, o None para entrenamiento
→ logits: [B, S, VOCAB_SIZE], aux_loss: scalar, new_kvs: list[(K,V)]*
- `count_params` (line 1066) `def count_params(self)`
- `generate` (line 1072) `def generate(self, token_ids, max_new_tokens, temperature, top_k, repetition_penalty)` - *Autoregressive generation with KV cache and top-k sampling.

Args:
    token_ids: [B, S_prompt] prompt tokens.
    max_new_tokens: Maximum tokens to generate.
    temperature: Sampling temperature (lower = more deterministic).
    top_k: Top-k filtering (0 = disabled).
    repetition_penalty: Penalty for repeating tokens (>1 = penalize).

Returns:
    [B, S_prompt + generated] full token sequence.*
- `__init__` (line 1130) `def __init__(self, encoding)`
- `encode` (line 1138) `def encode(self, text)`
- `decode` (line 1141) `def decode(self, tokens)`
- `eot_token` (line 1144) `def eot_token(self)`
- `__init__` (line 1256) `def __init__(self, root, cache_dir, logger)`
- `scan` (line 1263) `def scan(self, force)` - *Walk directory tree collecting text file paths. Cached to disk.*
- `__init__` (line 1330) `def __init__(self, cache_dir, logger)`
- `tokenize` (line 1335) `def tokenize(self, file_paths, tokenizer, cache_key, max_tokens, min_chars)` - *Tokenize all files and return a memory-mapped numpy array.

Args:
    file_paths: List of absolute file paths to tokenize.
    tokenizer: BPE tokenizer instance.
    cache_key: Unique key for caching tokens to disk.
    max_tokens: Maximum number of tokens to produce.
    min_chars: Skip files with fewer characters.

Returns:
    np.ndarray backed by a memmap on disk. Only accessed pages
    are loaded into RAM by the OS virtual memory system.*
- `__init__` (line 1418) `def __init__(self, tokens, seq_len)`
- `__len__` (line 1423) `def __len__(self)`
- `__getitem__` (line 1426) `def __getitem__(self, idx)`
- `__init__` (line 1446) `def __init__(self, config, logger)`
- `_compute_entropy` (line 1455) `def _compute_entropy(self, text)` - *Shannon entropy of byte frequencies (bits per byte).*
- `_has_long_lines` (line 1469) `def _has_long_lines(self, text, threshold)` - *Return True if any line exceeds threshold characters.*
- `_special_token_ratio` (line 1476) `def _special_token_ratio(self, text, tokenizer)` - *Fraction of tokens that are pure whitespace or indentation-only.*
- `_content_hash` (line 1490) `def _content_hash(self, text)`
- `filter_file` (line 1493) `def filter_file(self, path, tokenizer)` - *Read and evaluate a file. Returns text if passed, None if filtered.*
- `report` (line 1533) `def report(self)`
- `__init__` (line 1554) `def __init__(self, tokens, seq_len, file_tiers, active_tier, logger)`
- `_update_len` (line 1564) `def _update_len(self)`
- `set_tier` (line 1570) `def set_tier(self, tier)`
- `__len__` (line 1574) `def __len__(self)`
- `__getitem__` (line 1577) `def __getitem__(self, idx)`
- `__init__` (line 1622) `def __init__(self, base_trainer)`
- `_build_dataloader` (line 1628) `def _build_dataloader(self, dataset, seq_len, batch_size, is_train)`
- `run` (line 1638) `def run(self, train_paths, val_paths, tokenizer, file_tiers, phases)` - *Run training with progressive sequence length across phases.*
- `__init__` (line 1696) `def __init__(self, target_model, config, logger)`
- `_build_draft` (line 1704) `def _build_draft(self)`
- `generate` (line 1718) `def generate(self, token_ids, max_new_tokens, temperature, top_k, repetition_penalty)` - *Autoregressive generation via speculative decoding.

Each round: draft generates K tokens, target verifies all K in
one O(1) forward pass (longest context), then samples the first
rejection from the target.*
- `__init__` (line 1810) `def __init__(self, embed, mode)`
- `forward` (line 1839) `def forward(self, indices)`
- `__init__` (line 1879) `def __init__(self, model, config, tokenizer)`
- `cache_tokens` (line 1886) `def cache_tokens(self, key, tokens)`
- `model` (line 1890) `def model(self)`
- `optimizer` (line 1894) `def optimizer(self)`
- `scaler` (line 1898) `def scaler(self)`
- `amp_dtype` (line 1902) `def amp_dtype(self)`
- `completed_epochs` (line 1906) `def completed_epochs(self)`
- `completed_epochs` (line 1910) `def completed_epochs(self, v)`
- `global_step` (line 1914) `def global_step(self)`
- `global_step` (line 1918) `def global_step(self, v)`
- `best_val_loss` (line 1922) `def best_val_loss(self)`
- `best_val_loss` (line 1926) `def best_val_loss(self, v)`
- `history` (line 1930) `def history(self)`
- `ckpt_mgr` (line 1934) `def ckpt_mgr(self)`
- `resume` (line 1937) `def resume(self)`
- `_current_state` (line 1940) `def _current_state(self)`
- `_cosine_lr` (line 1943) `def _cosine_lr(self)`
- `_set_lr` (line 1946) `def _set_lr(self)`
- `evaluate` (line 1949) `def evaluate(self, dataloader)`
- `_sample_text` (line 1952) `def _sample_text(self)`
- `_progressive_train` (line 1955) `def _progressive_train(self, train_paths, val_paths, tokenizer, phases, memtok)` - *Training loop with progressive sequence length across phases.*
- `train` (line 1994) `def train(self, train_dl, val_dl)`
- `run_curriculum` (line 1997) `def run_curriculum(self, train_paths, val_paths, tokenizer, phases)` - *Top-level entry point: curriculum + progressive seq len.*
- `__init__` (line 2048) `def __init__(self, config, logger)`
- `patch_config_for_resume` (line 2058) `def patch_config_for_resume(self, cfg)` - *Lee el checkpoint 'latest' y ajusta cfg.N_KV_HEADS / cfg.GQA_GROUPS
para que coincidan con la arquitectura guardada.
Necesario cuando el codigo cambio GQA despues de guardar el checkpoint.*
- `_save_model` (line 2087) `def _save_model(self, model, directory)`
- `_load_model` (line 2100) `def _load_model(self, model, directory)`
- `_save_optimizer` (line 2131) `def _save_optimizer(self, optimizer, directory)`
- `_load_optimizer` (line 2134) `def _load_optimizer(self, optimizer, directory, device)`
- `_save_state` (line 2143) `def _save_state(self, state, directory)`
- `_load_state` (line 2148) `def _load_state(self, directory)`
- `should_save` (line 2159) `def should_save(self)`
- `save` (line 2162) `def save(self, model, optimizer, state, is_best)` - *Guarda checkpoint completo.

state debe contener al menos: completed_epochs, global_step,
best_val_loss, history, config.*
- `load_latest` (line 2207) `def load_latest(self, model, optimizer)` - *Carga el ultimo checkpoint guardado.
Devuelve el state dict (vacio si no hay checkpoint).*
- `load_best` (line 2234) `def load_best(self, model)` - *Carga el mejor modelo guardado (solo pesos, sin optimizador).*
- `has_checkpoint` (line 2246) `def has_checkpoint(self)`
- `__init__` (line 2268) `def __init__(self, model, config, tokenizer)`
- `resume` (line 2303) `def resume(self)` - *Carga el ultimo checkpoint disponible.
Restaura: pesos del modelo, estado del optimizador, historial acumulado,
epoch/step completados y mejor val_loss.
Devuelve True si se cargo un checkpoint, False si empieza de cero.*
- `_current_state` (line 2328) `def _current_state(self)` - *Construye el dict de estado para persistir en state.json.*
- `_cosine_lr` (line 2339) `def _cosine_lr(self, step_in_session, total_steps_session)` - *Cosine decay con warmup. El schedule es relativo a la sesion actual.*
- `_set_lr` (line 2347) `def _set_lr(self, lr)`
- `train` (line 2351) `def train(self, train_dl, val_dl)` - *Entrena cfg.EPOCHS epocas adicionales a partir de completed_epochs.
El historial se acumula sobre sesiones previas.*
- `_sample_text` (line 2487) `def _sample_text(self, tokenizer, prompts, max_new, temperature, top_k)` - *Genera una muestra de texto al final de cada epoch para monitorear
la calidad cualitativa del modelo (detecta degeneracion, repeticion, etc.).*
- `evaluate` (line 2519) `def evaluate(self, dataloader)`
- `__init__` (line 2569) `def __init__(self, config)`
- `compute_delta` (line 2577) `def compute_delta(self, model)`
- `compute_alpha` (line 2584) `def compute_alpha(self, delta)`
- `update_grad_buffer` (line 2589) `def update_grad_buffer(self, model)` - *Captura gradientes de forma segura, ignorando tensores corruptos.*
- `compute_t_eff` (line 2615) `def compute_t_eff(self, lr)` - *T_eff = lr/2 * Var(gradiente). Temperatura termodinamica efectiva.*
- `compute_kappa` (line 2623) `def compute_kappa(self, model, dataloader, n_batches)` - *κ = λ_max / λ_min de la covarianza del gradiente.
Parámetro de orden para cristalización (κ≈1 = cristal).
Nota: requiere pasadas backward adicionales. Se ejecuta con protección
para no corromper el estado AMP del trainer principal.*
- `compute_berry_phase` (line 2681) `def compute_berry_phase(self, model)` - *Fase de Berry de los kernels espectrales imaginarios.
Surge de los parametros ki_w, ki_x, ki_y, ki_z de QuaternionSpectralLayer.
|berry|>pi/2 con winding!=0 indica estructura topologica.*
- `compute_lc` (line 2694) `def compute_lc(self, model)` - *Complejidad local: 1 - similitud coseno promedio entre filas de pesos.*
- `compute_sp` (line 2708) `def compute_sp(self, model)` - *Superposicion: correlacion inter-fila promedio (entrelazamiento de features).*
- `classify_phase` (line 2724) `def classify_phase(self, delta, kappa, berry)` - *Clasificacion de fase segun Book.md:

discrete_crystal:       delta<0.05, kappa<1.5
topological_insulator:  |berry|>pi/2, winding!=0
cold_glass:             kappa>>1, delta>0.3
functional_glass:       intermedio (lo mas comun en LM)*
- `compute_all` (line 2743) `def compute_all(self, model, lr, dataloader, compute_kappa)` - *Calcula todas las metricas.
compute_kappa=True hace pasadas backward adicionales (caro, usar cada N epochs).*
- `format_log` (line 2768) `def format_log(self, m)`
- `__init__` (line 2804) `def __init__(self, config, logger)`
- `_measure_ratio` (line 2808) `def _measure_ratio(self, ratio, sample_batch)` - *Mide la coherencia espectral para un ratio dado.
Retorna: varianza del gradiente (menor = mas coherente = mejor).*
- `optimize` (line 2837) `def optimize(self, dataloader)` - *Retorna el mejor ratio de inicializacion de kernels espectrales.*
- `__init__` (line 2877) `def __init__(self, config, logger)`
- `prospect` (line 2881) `def prospect(self, candidates, train_dataset, prospect_steps)` - *Retorna el mejor batch size segun delta y T_eff.*
- `__init__` (line 2960) `def __init__(self, config, logger)`
- `mine` (line 2964) `def mine(self, seed_start, n_seeds, train_dataset, prospect_steps)` - *Retorna la semilla con la mejor trayectoria de delta.*
- `__init__` (line 3046) `def __init__(self, trainer, t0, cooling_rate, stagnation_patience)`
- `refine` (line 3055) `def refine(self, train_dl, val_dl, refine_epochs)` - *Ejecuta refine_epochs epocas de recocido simulado.
Retorna el historial de refinamiento.*
- `__init__` (line 3198) `def __init__(self, config, train_tokens, val_tokens, tokenizer, logger, curriculum_tiers, progressive_seq)`
- `_build_dataloader` (line 3211) `def _build_dataloader(self, tokens, seq_len, batch_size, shuffle, tag)`
- `_build_phases` (line 3225) `def _build_phases(self)`
- `run` (line 3234) `def run(self, run_prospect, refine_epochs, resume, prospect_steps, probe_seeds, seed_start)`
- `__init__` (line 3336) `def __init__(self, config, train_dataset, val_dataset, tokenizer, logger)`
- `_make_dataloaders` (line 3346) `def _make_dataloaders(self, batch_size)`
- `run` (line 3358) `def run(self, run_prospect, refine_epochs, resume, prospect_steps, probe_seeds, seed_start)` - *Ejecuta el pipeline completo.
Retorna el trainer con el modelo entrenado.*
- `ckpt_fn` (line 994) `def ckpt_fn(x_in)`

#### `train.py`
**Path:** `topogpt3/train.py`

**Classes:**
- `TopoGPT3Config` (line 83) `class TopoGPT3Config` - *Configuracion del pipeline TopoGPT3 (Grassmanniana + curriculum).*
- `GrassmannianTracker` (line 191) `class GrassmannianTracker` - *Observables geometricos sobre la trayectoria SGD.

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

Todos los calculos viven en CPU/float32 para no contaminar AMP.*
- `EfficiencyMetrics` (line 579) `class EfficiencyMetrics` - *Mide y calcula los tres ratios pedidos:

  perf_per_param  =  (1 / val_ppl) / params_M
  perf_per_FLOP   =  tokens_per_sec / FLOPs_per_sec_aprox
  perf_per_BW     =  tokens_per_sec / bytes_moved_per_sec_aprox

FLOPs estimados con la heuristica de Kaplan/Hoffmann:
    FLOPs_forward_per_token ~= 2 * N_no_embed
    FLOPs_total_per_token  ~= 6 * N_no_embed       (forward + backward)
Bandwidth estimada como params_bytes leidos + activations_bytes movidas por step.
tokens_per_sec se cronometra empiricamente sobre el dataloader.*
- `CodeCurriculumLoader` (line 707) `class CodeCurriculumLoader` - *    Carga los 4 datasets, normaliza cada ejemplo a una unica cadena de texto,
    tokeniza con BPE y produce splits train / val / holdout disjuntos.

    Politica de normalizacion por dataset:
      - CodeAlpaca:           "### Instruction
{i}
### Input
{x}
### Response
{o}"
      - Code-Feedback:        concat de turnos: "<usr> ... </usr>
<asst> ... </asst>"
      - Magicoder-Evol:       "### Problem
{p}
### Solution
{s}"
      - Tiny-The-Stack:       texto crudo del archivo (truncado a 32k chars/file)

    Cache en disco: tokens_{tier}_{split}.bin (int32 memmap) + manifest .json.
    El HOLDOUT se separa con seed fija antes de tokenizar para garantizar
    que la misma muestra nunca aparezca en train o val entre corridas.
    *
- `BlockTokenDataset` (line 994) `class BlockTokenDataset` - *Dataset autoregresivo sobre un stream de tokens.
Cada item es (x, y) con shape [seq_len].*
- `CheckpointStore` (line 1021) `class CheckpointStore` - *Persiste pesos del modelo + estado del trainer (sin AMP scaler para portabilidad).*
- `TopoGPT3Trainer` (line 1097) `class TopoGPT3Trainer` - *Orquesta el curriculum sobre los 4 tiers.

Pipeline por tier:
  1. Abre memmap de tokens (train/val/holdout).
  2. Construye DataLoaders con seq_len(tier).
  3. Entrena TIER_EPOCHS[tier] epocas con AMP + grad accum.
  4. Cada GRASS_TRACK_EVERY steps: snapshot Grassmanniano.
  5. Al final de cada epoca: eval en VAL.
  6. Al final del tier: eval en HOLDOUT (datos nunca vistos).
  7. Checkpoint y avanza al siguiente tier.

Al final del pipeline: eval en HOLDOUT *combinado* de los 4 tiers.*

**Functions:**
- `_gauss_complex_contract` (line 526) `def _gauss_complex_contract(self, W, X)` - *Sustituye QuaternionSpectralLayer._contract usando el truco de Gauss.

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
desactivamos autocast aqui y forzamos fp32 para preservar la semantica.*
- `apply_gauss_patch` (line 562) `def apply_gauss_patch(logger)` - *Activa la version Gauss de _contract en QuaternionSpectralLayer.
Idempotente: solo parchea una vez por proceso.*
- `parse_args` (line 1531) `def parse_args()`
- `main` (line 1560) `def main()`
- `build_topogpt2_config` (line 167) `def build_topogpt2_config(self, max_seq_len)`
- `__init__` (line 211) `def __init__(self, config, logger)`
- `_stack_spectral_kernels` (line 225) `def _stack_spectral_kernels(model)` - *Devuelve K(theta) en C^{N_f x N_c}:
  - filas = frecuencias planas (todos los modos espaciales de todos los kernels)
  - columnas = canales (in_q * out_q por componente cuaternionico, sumados)*
- `_elbow_rank` (line 262) `def _elbow_rank(self, sigmas)` - *Punto donde el valor singular cae por debajo de elbow_ratio * sigma_max.*
- `_dominant_subspace` (line 271) `def _dominant_subspace(self, K)` - *SVD compacta y truncada.
Devuelve (U_r, sigmas, r) con U_r en C^{N_f x r} ortonormal.*
- `_flatten_grads` (line 289) `def _flatten_grads(model, max_per_tensor)` - *Concatena un sub-sample de gradientes para mantener costo acotado.*
- `estimate_fisher_gap` (line 307) `def estimate_fisher_gap(self, model, dataloader, vocab_size, r_target)` - *Sigma_F ~= (1/M) sum_m g_m g_m^T  (covarianza muestral de gradientes).
Delta_F = lambda_{r_eff} - lambda_{r_eff+1}, donde r_eff = min(r_target, M-2)
para no salir del rango efectivo del estimador con M gradientes.
Devuelve (gap, eigs_desc, r_eff).*
- `_project_unitary` (line 375) `def _project_unitary(M)` - *Proyeccion a U(r) por descomposicion polar (M ~= U H -> retorna U).*
- `update_holonomy` (line 380) `def update_holonomy(self, U_new)` - *Holonomia discreta:
    T_n = U_n^dagger U_{n+1}  en C^{r x r}  (transporte paralelo discreto)
    U_Gamma <- T_n * U_Gamma  (acumulado)
Tras cada paso, U_Gamma se proyecta a U(r) para evitar deriva numerica.*
- `conjugation_distance_su2` (line 406) `def conjugation_distance_su2(U1, U2)` - *Para U1, U2 en U(1)/U(2):  d_conj(U1, U2) = min_g || U1 - g U2 g^{-1} ||_F.
En U(1) coincide con |U1 - U2|.
En SU(2) se reduce a comparar |Tr(U1)| con |Tr(U2)| (clase de conjugacion).*
- `_accumulate_winding` (line 423) `def _accumulate_winding(self, U_new)` - *W += (1/2pi) * arg det <U_prev | U_new>  acumulado sobre la trayectoria.*
- `snapshot` (line 439) `def snapshot(self, model, step, dataloader, vocab_size)`
- `format_log` (line 494) `def format_log(self, snap)`
- `save` (line 516) `def save(self, path)`
- `__init__` (line 594) `def __init__(self, model, config, logger, gauss_enabled)`
- `_embed_params` (line 605) `def _embed_params(model)`
- `measure_throughput` (line 613) `def measure_throughput(self, dataloader, vocab_size)` - *Devuelve (tokens_por_segundo, segundos_por_step).*
- `estimate_flops_per_step` (line 645) `def estimate_flops_per_step(self, batch_size, seq_len)` - *Heuristica: 6 * N_no_embed * tokens (forward + backward).*
- `estimate_bytes_per_step` (line 650) `def estimate_bytes_per_step(self, batch_size, seq_len, dtype_bytes)` - *Bandwidth aproximada: lectura de pesos + activaciones por step.
Asume AMP fp16 (2 bytes); pesos fp32 (4 bytes) leidos una vez.*
- `compute` (line 658) `def compute(self, dataloader, vocab_size, val_loss, val_ppl, val_acc, batch_size, seq_len)`
- `format_log` (line 690) `def format_log(self, m)`
- `__init__` (line 723) `def __init__(self, config, tokenizer, logger)`
- `_format_codealpaca` (line 740) `def _format_codealpaca(ex)`
- `_format_code_feedback` (line 751) `def _format_code_feedback(ex)`
- `_format_magicoder` (line 771) `def _format_magicoder(ex)`
- `_format_tiny_stack` (line 779) `def _format_tiny_stack(ex)`
- `_get_formatter` (line 791) `def _get_formatter(cls, tier)`
- `_tier_paths` (line 813) `def _tier_paths(self, tier)`
- `_manifest_path` (line 819) `def _manifest_path(self, tier)`
- `_already_prepared` (line 822) `def _already_prepared(self, tier)` - *True solo si los 3 splits existen, son no-vacios y el manifest concuerda.*
- `_load_hf_with_fallback` (line 852) `def _load_hf_with_fallback(self, tier)` - *Carga el dataset HF; para tiny_the_stack prueba una cadena de fallbacks
publicos hasta que uno funcione.*
- `prepare_tier` (line 885) `def prepare_tier(self, tier_index, force)`
- `open_memmap` (line 980) `def open_memmap(self, tier, split)`
- `__init__` (line 1000) `def __init__(self, tokens, seq_len)`
- `__len__` (line 1005) `def __len__(self)`
- `__getitem__` (line 1008) `def __getitem__(self, idx)`
- `__init__` (line 1024) `def __init__(self, root, max_keep, logger)`
- `save` (line 1031) `def save(self, tag, model, optimizer, state)` - *Guarda checkpoint atomico en <root>/last/ sobreescribiendo el anterior.

El argumento `tag` se conserva por compatibilidad pero se ignora: solo
existe un checkpoint llamado `last` y los pesos en safetensors.*
- `load_latest` (line 1065) `def load_latest(self, model, optimizer)`
- `should_save` (line 1089) `def should_save(self, interval_min)`
- `__init__` (line 1113) `def __init__(self, config, start_tier)`
- `prepare_all` (line 1167) `def prepare_all(self, force)` - *Prepara cada tier; un fallo en uno no detiene los demas.*
- `_build_loaders` (line 1183) `def _build_loaders(self, tier_index)`
- `_cosine_lr` (line 1215) `def _cosine_lr(self, step, total_steps)`
- `_set_lr` (line 1222) `def _set_lr(self, lr)`
- `_train_one_tier` (line 1230) `def _train_one_tier(self, tier_index)`
- `_evaluate` (line 1391) `def _evaluate(self, dl)` - *Devuelve (avg_loss, perplexity, token_accuracy).*
- `_state_dict` (line 1429) `def _state_dict(self)`
- `run` (line 1442) `def run(self)`
- `_eval_combined_holdout` (line 1499) `def _eval_combined_holdout(self)`
- `flush` (line 916) `def flush(split)`

### SH (1 files)

#### `install.sh`
**Path:** `install.sh`

*No symbols extracted*
