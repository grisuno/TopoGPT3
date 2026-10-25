# topogpt3: model

topogpt3: model groups 10 files (py) around TopoGPT2Config, __post_init__, setup_logger, set_seed, QuaternionOps. Diagnostico estatico de un checkpoint TopoGPT3 congelado.

```mermaid
graph LR
    eval["eval"]
    root["root"]
    tests["tests"]
    topogpt3["topogpt3"]
    eval -- "calls into" --> topogpt3
    root -- "calls into" --> topogpt3
    tests -- "calls into" --> topogpt3
    topogpt3 -- "calls into" --> root
```

## eval (3.1)

eval groups 1 files (py) around phase_discretization, synthetic_winding, static_kappa, context_length_diagnostic, main. Diagnostico estatico de un checkpoint TopoGPT3 congelado.

## root (3.2)

root groups 1 files (py) around LLMBackend, generate, name, GroqBackend, __init__. Synthetic Dataset Generator for TopoGPT2.

## tests (3.3)

tests groups 1 files (py) around tokenizer, TestParseResponseFormat, test_none_and_text, test_json_object, test_json_schema. Tests for DeepInfer-style structured outputs and deterministic seeds.

## topogpt3 (3.4)

topogpt3 groups 7 files (py) around TopoGPT2Config, __post_init__, setup_logger, set_seed, QuaternionOps. OpenAI-compatible HTTP API server so TopoGPT3 can be used as a backend for coding...

**Files**:

- eval/diag_static.py
- synthetic_dataset.py
- tests/test_structured_output.py
- topogpt3/api_server.py
- topogpt3/continuation.py
- topogpt3/export_chat.py
- topogpt3/inference_hrm.py
- topogpt3/model.py
- topogpt3/structured_output.py
- topogpt3/train.py
