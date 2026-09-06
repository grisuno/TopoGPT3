# Polyglot Codebase Knowledge Graph

> Generated offline by **readmenator**. Supports C, C++, Python, Go, Rust, JS/TS, Java, C#, Shell, PHP, Dart, GDScript, Nim, ASM, Ruby, Swift, Kotlin, Scala, Lua, Elixir.
> No LLMs. No tokens. Pure static analysis. See more [here](https://github.com/grisuno/ReadMenator)

**Total Files Parsed:** 36 | **Total Symbols Extracted:** 818 | **Total Imports:** 367
 | **Resolved Imports:** 52

<!-- ranking_model: v1.0 | weights: {ppr:0.45,auth:0.2,test:0.15,doc:0.1,fresh:0.1} | alpha:0.85 | commit:4c8e0d2 | date:2026-07-18 -->


## Table of Contents

1. [Statistics Dashboard](#statistics-dashboard)
2. [Architectural Layers](#architectural-layers)
3. [Ranked Context](#ranked-context)
4. [God Nodes](#god-nodes)
5. [Community Analysis](#community-analysis)
6. [Surprising Connections](#surprising-connections)
7. [Suggested Questions](#suggested-questions)
8. [Taint Propagation Map](#taint-propagation-map)
9. [Hotspot Analysis](#hotspot-analysis)
10. [Change Impact Analysis](#change-impact-analysis)
11. [Suggested Linting Rules](#suggested-linting-rules)
12. [Orphans](#orphans)
13. [Query Recipes](#query-recipes)
14. [Structural Knowledge Map](#structural-knowledge-map)
15. [UML Class Diagram](#uml-class-diagram)
16. [Code Property Graph](#code-property-graph)
17. [Architecture Reference](#architecture-reference)
    - [C (1 files)](#c-1-files)
    - [PY (34 files)](#py-34-files)
    - [SH (1 files)](#sh-1-files)

---

## Statistics Dashboard

| Metric | Value |
|--------|-------|
| Total Files | 36 |
| Total Symbols | 818 |
| Total Imports | 367 |
| Call Edges | 4814 |
| Inheritance Edges | 28 |
| Languages | 3 |
| Avg Symbols/File | 22.7 |
| Avg Imports/File | 10.2 |
| Resolved Imports | 52 |

### Top Files by Import Count (Fan-Out)

| File | Imports | Symbols | Language |
|------|---------|---------|----------|
| `api_server.py` | 27 | 46 | py |
| `model.py` | 25 | 187 | py |
| `harness.py` | 24 | 12 | py |
| `synthetic_dataset.py` | 24 | 35 | py |
| `train.py` | 21 | 62 | py |
| `repair.py` | 16 | 6 | py |
| `noise_sweep.py` | 14 | 4 | py |
| `jlens.py` | 14 | 29 | py |
| `lens_model.py` | 14 | 29 | py |
| `diag_static.py` | 13 | 5 | py |

---

## Architectural Layers

Auto-detected from path patterns, naming conventions, and imported frameworks.

| Layer | Files |
|-------|-------|
| utility | 28 |
| infrastructure | 2 |
| testing | 2 |
| business_logic | 2 |
| data_access | 1 |
| presentation | 1 |

### utility

- `app.py` (py, 5 symbols)
- `convert_weights.py` (py, 2 symbols)
- `convert_weights_minios.py` (py, 1 symbols)
- `encode_tokens.py` (py, 1 symbols)
- `analyze.py` (py, 5 symbols)
- `analyze_results.py` (py, 4 symbols)
- `governor.py` (py, 20 symbols)
- `governor_smoke.py` (py, 7 symbols)
- `harness.py` (py, 12 symbols)
- `integration_smoke.py` (py, 1 symbols)
- `noise_analysis.py` (py, 3 symbols)
- `noise_sweep.py` (py, 4 symbols)
- `repair.py` (py, 6 symbols)
- `report.py` (py, 6 symbols)
- `samplers.py` (py, 7 symbols)
- *... and 13 more*

### infrastructure

- `diag_static.py` (py, 5 symbols)
- `gradio_app.py` (py, 4 symbols)

### data_access

- `synthetic_dataset.py` (py, 35 symbols)

### testing

- `test_jlens.py` (py, 51 symbols)
- `test_lens_model.py` (py, 34 symbols)

### presentation

- `api_server.py` (py, 46 symbols)

### business_logic

- `lens_model.py` (py, 29 symbols)
- `model.py` (py, 187 symbols)

---

## Ranked Context

Files ranked by composite score for the current query context. The ranking combines Personalized PageRank (query relevance), global authority, test coverage, documentation coverage, and code freshness. Model: v1.0.

| Rank | File | Composite | PPR | Authority | Test | Doc |
|------|------|-----------|-----|-----------|------|-----|
| 1 | `model.py` | 0.1306 | 0.1269 | 0.1269 | 0.00 | 0.48 |
| 2 | `continuation.py` | 0.1243 | 0.0989 | 0.0989 | 0.00 | 0.60 |
| 3 | `app.py` | 0.1105 | 0.0162 | 0.0162 | 0.00 | 1.00 |
| 4 | `gradio_app.py` | 0.1105 | 0.0162 | 0.0162 | 0.00 | 1.00 |
| 5 | `__main__.py` | 0.1105 | 0.0162 | 0.0162 | 0.00 | 1.00 |
| 6 | `test_lens_model.py` | 0.1017 | 0.0162 | 0.0162 | 0.00 | 0.91 |
| 7 | `test_jlens.py` | 0.1007 | 0.0162 | 0.0162 | 0.00 | 0.90 |
| 8 | `inference_hrm.py` | 0.0963 | 0.0246 | 0.0246 | 0.00 | 0.80 |
| 9 | `inference.py` | 0.0956 | 0.0246 | 0.0246 | 0.00 | 0.80 |
| 10 | `sandbox.py` | 0.0921 | 0.0391 | 0.0391 | 0.00 | 0.67 |

---

## God Nodes

Most architecturally central files ranked by combined import/export degree and symbol richness.

| File | Score | Connections | PageRank |
|------|-------|-------------|----------|
| `model.py` | 36.7 | | 0.1269 |
| `topogpt3.c` | 23.9 | | 0.0000 |
| `__init__.py` | 16.0 | | 0.0000 |
| `lens_model.py` | 14.9 | | 0.0000 |
| `train.py` | 14.2 | | 0.0000 |
| `inference_hrm.py` | 13.6 | | 0.0246 |
| `harness.py` | 13.2 | | 0.0000 |
| `jlens.py` | 12.9 | | 0.0000 |
| `__main__.py` | 12.1 | | 0.0162 |
| `api_server.py` | 10.6 | | 0.0000 |

---

## Community Analysis

Files grouped by import-based community detection. Cohesion measures how tightly connected each community is internally.

### topogpt3 (Cohesion: 0.94)

**16 files** in this community:

- `app.py` (py, 5 symbols)
- `diag_static.py` (py, 5 symbols)
- `gradio_app.py` (py, 4 symbols)
- `synthetic_dataset.py` (py, 35 symbols)
- `test_jlens.py` (py, 51 symbols)
- `test_lens_model.py` (py, 34 symbols)
- `__init__.py` (py, 0 symbols)
- `__main__.py` (py, 1 symbols)
- `api_server.py` (py, 46 symbols)
- `continuation.py` (py, 5 symbols)
- `inference.py` (py, 54 symbols)
- `inference_hrm.py` (py, 76 symbols)
- `jlens.py` (py, 29 symbols)
- `lens_model.py` (py, 29 symbols)
- `model.py` (py, 187 symbols)
- `train.py` (py, 62 symbols)

### eval (Cohesion: 0.50)

**2 files** in this community:

- `governor.py` (py, 20 symbols)
- `governor_smoke.py` (py, 7 symbols)

### eval (Cohesion: 0.80)

**10 files** in this community:

- `harness.py` (py, 12 symbols)
- `integration_smoke.py` (py, 1 symbols)
- `noise_sweep.py` (py, 4 symbols)
- `repair.py` (py, 6 symbols)
- `samplers.py` (py, 7 symbols)
- `sandbox.py` (py, 9 symbols)
- `sandbox_smoke.py` (py, 1 symbols)
- `smoke.py` (py, 2 symbols)
- `temp_sweep.py` (py, 5 symbols)
- `topogpt3.c` (c, 99 symbols)

---

## Surprising Connections

Files in different communities connected through 3+ indirect hops.

- `app.py` <-> `governor.py` (6 hops, across 3 communities)
- `app.py` <-> `sandbox_smoke.py` (6 hops, across 2 communities)
- `governor.py` <-> `gradio_app.py` (6 hops, across 3 communities)
- `governor.py` <-> `test_jlens.py` (6 hops, across 3 communities)
- `governor.py` <-> `inference.py` (6 hops, across 3 communities)

---

## Suggested Questions

Auto-generated exploration prompts based on graph structure:

- What does model.py depend on, and what depends on it? (9 connections)
- What does topogpt3.c depend on, and what depends on it? (7 connections)
- What does __init__.py depend on, and what depends on it? (8 connections)
- How are the 16 files in 'topogpt3' related to each other?
- Why are app.py and governor.py connected through 6 hops across 3 communities?

---

## Taint Propagation Map

Taint analysis traces how dangerous imports propagate through the codebase via transitive dependencies. Source files import dangerous modules directly; sink files receive the danger indirectly.

**Taint Sources:** 3 | **Taint Sinks:** 7 | **Propagation Paths:** 20

- `governor_smoke.py` imports `eval` (0 hop to `governor_smoke.py`) [critical]
  Path: governor_smoke.py
- `governor_smoke.py` imports `eval` (1 hop to `governor.py`) [critical]
  Path: governor_smoke.py -> governor.py
- `governor_smoke.py` imports `eval` (1 hop to `topogpt3.c`) [critical]
  Path: governor_smoke.py -> topogpt3.c
- `harness.py` imports `subprocess` (0 hop to `harness.py`) [high]
  Path: harness.py
- `harness.py` imports `subprocess` (1 hop to `samplers.py`) [high]
  Path: harness.py -> samplers.py
- `harness.py` imports `subprocess` (1 hop to `sandbox.py`) [high]
  Path: harness.py -> sandbox.py
- `harness.py` imports `subprocess` (1 hop to `topogpt3.c`) [high]
  Path: harness.py -> topogpt3.c
- `harness.py` imports `eval` (0 hop to `harness.py`) [critical]
  Path: harness.py
- `harness.py` imports `eval` (1 hop to `samplers.py`) [critical]
  Path: harness.py -> samplers.py
- `harness.py` imports `eval` (1 hop to `sandbox.py`) [critical]
  Path: harness.py -> sandbox.py
- `harness.py` imports `eval` (1 hop to `topogpt3.c`) [critical]
  Path: harness.py -> topogpt3.c
- `harness.py` imports `eval` (0 hop to `harness.py`) [critical]
  Path: harness.py
- `harness.py` imports `eval` (1 hop to `samplers.py`) [critical]
  Path: harness.py -> samplers.py
- `harness.py` imports `eval` (1 hop to `sandbox.py`) [critical]
  Path: harness.py -> sandbox.py
- `harness.py` imports `eval` (1 hop to `topogpt3.c`) [critical]
  Path: harness.py -> topogpt3.c
- `harness.py` imports `eval` (0 hop to `harness.py`) [critical]
  Path: harness.py
- `harness.py` imports `eval` (1 hop to `samplers.py`) [critical]
  Path: harness.py -> samplers.py
- `harness.py` imports `eval` (1 hop to `sandbox.py`) [critical]
  Path: harness.py -> sandbox.py
- `harness.py` imports `eval` (1 hop to `topogpt3.c`) [critical]
  Path: harness.py -> topogpt3.c
- `integration_smoke.py` imports `eval` (0 hop to `integration_smoke.py`) [critical]
  Path: integration_smoke.py

---

## Hotspot Analysis

Files ranked by combined complexity (symbol count) and centrality (connection count). High-scoring files are architecturally critical and may need refactoring attention.

| File | Complexity | Centrality | Combined | Symbols | Connections |
|------|-----------|------------|----------|---------|-------------|
| `model.py` | 1.000 | 1.000 | 1.000 | 187 | 36 |
| `continuation.py` | 0.027 | 0.167 | 0.111 | 5 | 6 |
| `app.py` | 0.027 | 0.194 | 0.127 | 5 | 7 |
| `gradio_app.py` | 0.021 | 0.250 | 0.159 | 4 | 9 |
| `__main__.py` | 0.005 | 0.389 | 0.235 | 1 | 14 |
| `test_lens_model.py` | 0.182 | 0.500 | 0.373 | 34 | 18 |
| `test_jlens.py` | 0.273 | 0.194 | 0.226 | 51 | 7 |
| `inference_hrm.py` | 0.406 | 0.444 | 0.429 | 76 | 16 |
| `inference.py` | 0.289 | 0.361 | 0.332 | 54 | 13 |
| `sandbox.py` | 0.048 | 0.361 | 0.236 | 9 | 13 |
| `api_server.py` | 0.246 | 0.833 | 0.598 | 46 | 30 |
| `train.py` | 0.332 | 0.694 | 0.549 | 62 | 25 |
| `harness.py` | 0.064 | 0.861 | 0.542 | 12 | 31 |
| `synthetic_dataset.py` | 0.187 | 0.694 | 0.491 | 35 | 25 |
| `jlens.py` | 0.155 | 0.639 | 0.445 | 29 | 23 |

---

## Change Impact Analysis

Files sorted by how many other files would be affected if they changed. High-impact files should be changed with caution.

| File | Direct Dependents | Transitive Dependents | Total Impact |
|------|------------------|----------------------|--------------|
| `continuation.py` | 3 | 12 | 15 |
| `synthetic_dataset.py` | 1 | 13 | 14 |
| `model.py` | 7 | 6 | 13 |
| `topogpt3.c` | 7 | 2 | 9 |
| `lens_model.py` | 5 | 2 | 7 |
| `jlens.py` | 4 | 2 | 6 |
| `sandbox.py` | 2 | 3 | 5 |
| `train.py` | 3 | 2 | 5 |
| `samplers.py` | 1 | 3 | 4 |
| `inference.py` | 2 | 2 | 4 |
| `inference_hrm.py` | 2 | 2 | 4 |
| `harness.py` | 3 | 0 | 3 |
| `__init__.py` | 2 | 0 | 2 |
| `governor.py` | 1 | 0 | 1 |
| `noise_sweep.py` | 1 | 0 | 1 |

---

## Suggested Linting Rules

Automatically suggested linting and security rules based on patterns detected in the codebase. These can be exported as Semgrep rules using the `--export-rules` flag.

| Rule ID | Severity | Description | Language | Matches |
|---------|----------|-------------|----------|---------|
| `RM001` | info | Large number of functions in py: 593 total | py | 593 |
| `RM002` | info | Large number of functions in c: 57 total | c | 57 |
| `RM003` | info | Print statement found (consider logging instead) | python | 213 |

---

## Orphans

Files with no documentation or low connectivity. These are candidates for documentation investment or cleanup.

- `convert_weights.py` (2 symbols, no doc)
- `convert_weights_minios.py` (1 symbols, no doc)
- `encode_tokens.py` (1 symbols, no doc)
- `analyze_results.py` (4 symbols, no doc)
- `governor_smoke.py` (7 symbols, no doc)
- `integration_smoke.py` (1 symbols, no doc)
- `repair.py` (6 symbols, no doc)
- `report.py` (6 symbols, no doc)
- `sandbox_smoke.py` (1 symbols, no doc)
- `smoke.py` (2 symbols, no doc)
- `temp_sweep.py` (5 symbols, no doc)
- `install.sh` (0 symbols, no doc)
- `__init__.py` (0 symbols, no doc)

---

## Query Recipes

Example queries you can run against this knowledge base using the ranking engine:

```
# Find files most relevant to a concept
readmenator query "Where is the import resolver implemented?"

# Rank files by relevance to a topic
readmenator query "How does documentation generation work?"

# Explain why a file ranks highly
readmenator query "explain readmenator/_documentation.py"

# Trace dependency paths with ranked context
readmenator query "path from CLI to exporter"
```

The ranking model uses the following signals:

- **Personalized PageRank** (45% weight): query-specific relevance via seed propagation
- **Global Authority** (20% weight): structural importance via standard PageRank
- **Test Coverage** (15% weight): fraction of symbols referenced in test files
- **Doc Coverage** (10% weight): presence of docstrings and file-level docs
- **Freshness** (10% weight): recent modification activity

Results include score decomposition and justification paths for each ranked item.

---

## Structural Knowledge Map

```mermaid
graph TD
    classDef mod fill:#1e1e1e,stroke:#ff6666,stroke-width:2px,color:#fff;
    classDef cls fill:#2d2d2d,stroke:#4ec9b0,stroke-width:2px,color:#fff;
    classDef fn fill:#333,stroke:#dcdcaa,stroke-width:1px,color:#dcdcaa;
    classDef ext fill:#111,stroke:#666,stroke-dasharray:5 5,color:#aaa;
    subgraph community_0 ["topogpt3"]
    topogpt3_api_server_py["api_server.py (py)"]
    class topogpt3_api_server_py mod;
    topogpt3_api_server_py__setup_logging["_setup_logging"]
    class topogpt3_api_server_py__setup_logging fn;
    topogpt3_api_server_py --> topogpt3_api_server_py__setup_logging
    topogpt3_api_server_py_ApiKey["ApiKey"]
    class topogpt3_api_server_py_ApiKey cls;
    topogpt3_api_server_py --> topogpt3_api_server_py_ApiKey
    topogpt3_api_server_py_AuthState["AuthState"]
    class topogpt3_api_server_py_AuthState cls;
    topogpt3_api_server_py --> topogpt3_api_server_py_AuthState
    topogpt3_api_server_py__parse_keys["_parse_keys"]
    class topogpt3_api_server_py__parse_keys fn;
    topogpt3_api_server_py --> topogpt3_api_server_py__parse_keys
    topogpt3_api_server_py__sha256["_sha256"]
    class topogpt3_api_server_py__sha256 fn;
    topogpt3_api_server_py --> topogpt3_api_server_py__sha256
    end
    subgraph community_2 ["eval"]
    eval_harness_py["harness.py (py)"]
    class eval_harness_py mod;
    topogpt3_model_py["model.py (py)"]
    class topogpt3_model_py mod;
    synthetic_dataset_py["synthetic_dataset.py (py)"]
    class synthetic_dataset_py mod;
    topogpt3_train_py["train.py (py)"]
    class topogpt3_train_py mod;
    tests_test_lens_model_py["test_lens_model.py (py)"]
    class tests_test_lens_model_py mod;
    eval_repair_py["repair.py (py)"]
    class eval_repair_py mod;
    eval_noise_sweep_py["noise_sweep.py (py)"]
    class eval_noise_sweep_py mod;
    topogpt3_jlens_py["jlens.py (py)"]
    class topogpt3_jlens_py mod;
    topogpt3_lens_model_py["lens_model.py (py)"]
    class topogpt3_lens_model_py mod;
    eval_diag_static_py["diag_static.py (py)"]
    class eval_diag_static_py mod;
    topogpt3_inference_hrm_py["inference_hrm.py (py)"]
    class topogpt3_inference_hrm_py mod;
    topogpt3___main___py["__main__.py (py)"]
    class topogpt3___main___py mod;
    eval_temp_sweep_py["temp_sweep.py (py)"]
    class eval_temp_sweep_py mod;
    topogpt3___init___py["__init__.py (py)"]
    class topogpt3___init___py mod;
    topogpt3_inference_py["inference.py (py)"]
    class topogpt3_inference_py mod;
    eval_sandbox_py["sandbox.py (py)"]
    class eval_sandbox_py mod;
    end
    subgraph community_1 ["eval"]
    eval_governor_smoke_py["governor_smoke.py (py)"]
    class eval_governor_smoke_py mod;
    eval_report_py["report.py (py)"]
    class eval_report_py mod;
    gradio_app_py["gradio_app.py (py)"]
    class gradio_app_py mod;
    eval_noise_analysis_py["noise_analysis.py (py)"]
    class eval_noise_analysis_py mod;
    eval_governor_py["governor.py (py)"]
    class eval_governor_py mod;
    eval_analyze_py["analyze.py (py)"]
    class eval_analyze_py mod;
    tests_test_jlens_py["test_jlens.py (py)"]
    class tests_test_jlens_py mod;
    app_py["app.py (py)"]
    class app_py mod;
    convert_weights_minios_py["convert_weights_minios.py (py)"]
    class convert_weights_minios_py mod;
    topogpt3_c["topogpt3.c (c)"]
    class topogpt3_c mod;
    eval_samplers_py["samplers.py (py)"]
    class eval_samplers_py mod;
    eval_analyze_results_py["analyze_results.py (py)"]
    class eval_analyze_results_py mod;
    convert_weights_py["convert_weights.py (py)"]
    class convert_weights_py mod;
    eval_smoke_py["smoke.py (py)"]
    class eval_smoke_py mod;
    encode_tokens_py["encode_tokens.py (py)"]
    class encode_tokens_py mod;
    eval_integration_smoke_py["integration_smoke.py (py)"]
    class eval_integration_smoke_py mod;
    eval_sandbox_smoke_py["sandbox_smoke.py (py)"]
    class eval_sandbox_smoke_py mod;
    topogpt3_continuation_py["continuation.py (py)"]
    class topogpt3_continuation_py mod;
    install_sh["install.sh (sh)"]
    class install_sh mod;
    end
    app_py -- resolved_imports --> topogpt3___init___py
    eval_diag_static_py -- resolved_imports --> topogpt3_c
    eval_diag_static_py -- resolved_imports --> topogpt3_model_py
    eval_diag_static_py -- resolved_imports --> topogpt3_train_py
    eval_governor_smoke_py -- resolved_imports --> eval_governor_py
    eval_governor_smoke_py -- resolved_imports --> topogpt3_c
    eval_harness_py -- resolved_imports --> topogpt3_c
    eval_harness_py -- resolved_imports --> eval_samplers_py
    eval_harness_py -- resolved_imports --> eval_sandbox_py
    eval_harness_py -- resolved_imports --> eval_samplers_py
    eval_integration_smoke_py -- resolved_imports --> eval_harness_py
    eval_noise_sweep_py -- resolved_imports --> topogpt3_c
    eval_noise_sweep_py -- resolved_imports --> topogpt3_model_py
    eval_noise_sweep_py -- resolved_imports --> eval_harness_py
    eval_repair_py -- resolved_imports --> topogpt3_c
    eval_samplers_py -- resolved_imports --> topogpt3_c
    eval_sandbox_smoke_py -- resolved_imports --> eval_sandbox_py
    eval_smoke_py -- resolved_imports --> topogpt3_c
    eval_temp_sweep_py -- resolved_imports --> eval_noise_sweep_py
    eval_temp_sweep_py -- resolved_imports --> eval_harness_py
    gradio_app_py -- resolved_imports --> topogpt3___init___py
    tests_test_jlens_py -- resolved_imports --> topogpt3_lens_model_py
    tests_test_jlens_py -- resolved_imports --> topogpt3_jlens_py
    tests_test_lens_model_py -- resolved_imports --> topogpt3_lens_model_py
    tests_test_lens_model_py -- resolved_imports --> topogpt3_model_py
    tests_test_lens_model_py -- resolved_imports --> topogpt3_model_py
    tests_test_lens_model_py -- resolved_imports --> topogpt3_jlens_py
    tests_test_lens_model_py -- resolved_imports --> topogpt3_jlens_py
    tests_test_lens_model_py -- resolved_imports --> topogpt3_jlens_py
    tests_test_lens_model_py -- resolved_imports --> topogpt3_jlens_py
    topogpt3___init___py -- resolved_imports --> topogpt3_model_py
    topogpt3___init___py -- resolved_imports --> topogpt3_train_py
    topogpt3___init___py -- resolved_imports --> topogpt3_inference_py
    topogpt3___init___py -- resolved_imports --> topogpt3_inference_hrm_py
    topogpt3___init___py -- resolved_imports --> topogpt3_lens_model_py
    topogpt3___init___py -- resolved_imports --> topogpt3_jlens_py
    topogpt3___main___py -- resolved_imports --> topogpt3_jlens_py
    topogpt3___main___py -- resolved_imports --> topogpt3_lens_model_py
    topogpt3___main___py -- resolved_imports --> topogpt3_api_server_py
    topogpt3___main___py -- resolved_imports --> topogpt3_inference_py
    topogpt3___main___py -- resolved_imports --> topogpt3_inference_hrm_py
    topogpt3___main___py -- resolved_imports --> topogpt3_train_py
    topogpt3_api_server_py -- resolved_imports --> topogpt3_model_py
    topogpt3_api_server_py -- resolved_imports --> topogpt3_continuation_py
    topogpt3_inference_hrm_py -- resolved_imports --> topogpt3_continuation_py
    topogpt3_jlens_py -- resolved_imports --> topogpt3_lens_model_py
    topogpt3_jlens_py -- resolved_imports --> topogpt3_lens_model_py
    topogpt3_lens_model_py -- resolved_imports --> topogpt3_model_py
    topogpt3_lens_model_py -- resolved_imports --> topogpt3_model_py
    topogpt3_model_py -- resolved_imports --> synthetic_dataset_py
    topogpt3_model_py -- resolved_imports --> topogpt3_continuation_py
    topogpt3_train_py -- resolved_imports --> topogpt3_model_py
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
    ext_struct["struct"]
    class ext_struct ext;
    convert_weights_py -.->|imports| ext_struct
    convert_weights_py -.->|imports| ext_sys
    convert_weights_py -.->|imports| ext_argparse
    ext_pathlib["pathlib"]
    class ext_pathlib ext;
    convert_weights_py -.->|imports| ext_pathlib
    ext_safetensors["safetensors"]
    class ext_safetensors ext;
    convert_weights_py -.->|imports| ext_safetensors
    convert_weights_minios_py -.->|imports| ext_argparse
    convert_weights_minios_py -.->|imports| ext_struct
    ext_numpy["numpy"]
    class ext_numpy ext;
    convert_weights_minios_py -.->|imports| ext_numpy
    convert_weights_minios_py -.->|imports| ext_sys
    convert_weights_minios_py -.->|imports| ext_safetensors
    ext_os["os"]
    class ext_os ext;
    convert_weights_minios_py -.->|imports| ext_os
    encode_tokens_py -.->|imports| ext_sys
    encode_tokens_py -.->|imports| ext_struct
    encode_tokens_py -.->|imports| ext_argparse
    ext_tiktoken["tiktoken"]
    class ext_tiktoken ext;
    encode_tokens_py -.->|imports| ext_tiktoken
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
    ext_topogpt3_train["topogpt3.train"]
    class ext_topogpt3_train ext;
    eval_diag_static_py -.->|imports| ext_topogpt3_train
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
    gradio_app_py -.->|imports| ext___future__
    gradio_app_py -.->|imports| ext_os
    gradio_app_py -.->|imports| ext_sys
    gradio_app_py -.->|imports| ext_pathlib
    gradio_app_py -.->|imports| ext_torch
    ext_gradio["gradio"]
    class ext_gradio ext;
    gradio_app_py -.->|imports| ext_gradio
    gradio_app_py -.->|imports| ext_topogpt3
    ext_huggingface_hub["huggingface_hub"]
    class ext_huggingface_hub ext;
    gradio_app_py -.->|imports| ext_huggingface_hub
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
    synthetic_dataset_py -.->|imports| ext_numpy
    synthetic_dataset_py -.->|imports| ext_tiktoken
    ext_requests["requests"]
    class ext_requests ext;
    synthetic_dataset_py -.->|imports| ext_requests
    synthetic_dataset_py -.->|imports| ext_requests
    synthetic_dataset_py -.->|imports| ext_requests
    synthetic_dataset_py -.->|imports| ext_requests
    synthetic_dataset_py -.->|imports| ext_requests
    synthetic_dataset_py -.->|imports| ext_requests
    tests_test_jlens_py -.->|imports| ext___future__
    ext_pytest["pytest"]
    class ext_pytest ext;
    tests_test_jlens_py -.->|imports| ext_pytest
    tests_test_jlens_py -.->|imports| ext_torch
    ext_topogpt3_lens_model["topogpt3.lens_model"]
    class ext_topogpt3_lens_model ext;
    tests_test_jlens_py -.->|imports| ext_topogpt3_lens_model
    ext_topogpt3_jlens["topogpt3.jlens"]
    class ext_topogpt3_jlens ext;
    tests_test_jlens_py -.->|imports| ext_topogpt3_jlens
    tests_test_lens_model_py -.->|imports| ext___future__
    tests_test_lens_model_py -.->|imports| ext_pytest
    tests_test_lens_model_py -.->|imports| ext_torch
    tests_test_lens_model_py -.->|imports| ext_topogpt3_lens_model
    tests_test_lens_model_py -.->|imports| ext_topogpt3_model
    tests_test_lens_model_py -.->|imports| ext_topogpt3_model
    ext_types["types"]
    class ext_types ext;
    tests_test_lens_model_py -.->|imports| ext_types
    tests_test_lens_model_py -.->|imports| ext_topogpt3_jlens
    tests_test_lens_model_py -.->|imports| ext_topogpt3_jlens
    tests_test_lens_model_py -.->|imports| ext_topogpt3_jlens
    tests_test_lens_model_py -.->|imports| ext_topogpt3_jlens
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
    ext_lens_model["lens_model"]
    class ext_lens_model ext;
    topogpt3___init___py -.->|imports| ext_lens_model
    ext_jlens["jlens"]
    class ext_jlens ext;
    topogpt3___init___py -.->|imports| ext_jlens
    topogpt3___main___py -.->|imports| ext___future__
    topogpt3___main___py -.->|imports| ext_sys
    topogpt3___main___py -.->|imports| ext_jlens
    topogpt3___main___py -.->|imports| ext_lens_model
    ext_api_server["api_server"]
    class ext_api_server ext;
    topogpt3___main___py -.->|imports| ext_api_server
    topogpt3___main___py -.->|imports| ext_inference
    topogpt3___main___py -.->|imports| ext_inference_hrm
    topogpt3___main___py -.->|imports| ext_train
    topogpt3_api_server_py -.->|imports| ext___future__
    topogpt3_api_server_py -.->|imports| ext_argparse
    topogpt3_api_server_py -.->|imports| ext_hashlib
    ext_hmac["hmac"]
    class ext_hmac ext;
    topogpt3_api_server_py -.->|imports| ext_hmac
    topogpt3_api_server_py -.->|imports| ext_json
    topogpt3_api_server_py -.->|imports| ext_logging
    topogpt3_api_server_py -.->|imports| ext_os
    topogpt3_api_server_py -.->|imports| ext_re
    ext_secrets["secrets"]
    class ext_secrets ext;
    topogpt3_api_server_py -.->|imports| ext_secrets
    topogpt3_api_server_py -.->|imports| ext_sys
    topogpt3_api_server_py -.->|imports| ext_time
    topogpt3_api_server_py -.->|imports| ext_collections
    topogpt3_api_server_py -.->|imports| ext_contextlib
    topogpt3_api_server_py -.->|imports| ext_dataclasses
    topogpt3_api_server_py -.->|imports| ext_pathlib
    topogpt3_api_server_py -.->|imports| ext_typing
    topogpt3_api_server_py -.->|imports| ext_torch
    topogpt3_api_server_py -.->|imports| ext_model
    topogpt3_api_server_py -.->|imports| ext_safetensors_torch
    ext_fastapi["fastapi"]
    class ext_fastapi ext;
    topogpt3_api_server_py -.->|imports| ext_fastapi
    ext_fastapi_middleware_cors["fastapi.middleware.cors"]
    class ext_fastapi_middleware_cors ext;
    topogpt3_api_server_py -.->|imports| ext_fastapi_middleware_cors
    ext_fastapi_middleware_gzip["fastapi.middleware.gzip"]
    class ext_fastapi_middleware_gzip ext;
    topogpt3_api_server_py -.->|imports| ext_fastapi_middleware_gzip
    ext_fastapi_responses["fastapi.responses"]
    class ext_fastapi_responses ext;
    topogpt3_api_server_py -.->|imports| ext_fastapi_responses
    ext_pydantic["pydantic"]
    class ext_pydantic ext;
    topogpt3_api_server_py -.->|imports| ext_pydantic
    ext_uvicorn["uvicorn"]
    class ext_uvicorn ext;
    topogpt3_api_server_py -.->|imports| ext_uvicorn
    topogpt3_api_server_py -.->|imports| ext_safetensors
    ext_continuation["continuation"]
    class ext_continuation ext;
    topogpt3_api_server_py -.->|imports| ext_continuation
    topogpt3_continuation_py -.->|imports| ext___future__
    topogpt3_continuation_py -.->|imports| ext_re
    topogpt3_continuation_py -.->|imports| ext_typing
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
    topogpt3_inference_hrm_py -.->|imports| ext_continuation
    topogpt3_jlens_py -.->|imports| ext___future__
    topogpt3_jlens_py -.->|imports| ext_logging
    topogpt3_jlens_py -.->|imports| ext_math
    topogpt3_jlens_py -.->|imports| ext_os
    topogpt3_jlens_py -.->|imports| ext_time
    ext_collections_abc["collections.abc"]
    class ext_collections_abc ext;
    topogpt3_jlens_py -.->|imports| ext_collections_abc
    topogpt3_jlens_py -.->|imports| ext_dataclasses
    topogpt3_jlens_py -.->|imports| ext_typing
    topogpt3_jlens_py -.->|imports| ext_torch
    topogpt3_jlens_py -.->|imports| ext_torch
    topogpt3_jlens_py -.->|imports| ext_lens_model
    topogpt3_jlens_py -.->|imports| ext_argparse
    topogpt3_jlens_py -.->|imports| ext_lens_model
    topogpt3_jlens_py -.->|imports| ext_huggingface_hub
    topogpt3_lens_model_py -.->|imports| ext___future__
    topogpt3_lens_model_py -.->|imports| ext_json
    topogpt3_lens_model_py -.->|imports| ext_collections_abc
    topogpt3_lens_model_py -.->|imports| ext_dataclasses
    topogpt3_lens_model_py -.->|imports| ext_pathlib
    topogpt3_lens_model_py -.->|imports| ext_types
    topogpt3_lens_model_py -.->|imports| ext_typing
    topogpt3_lens_model_py -.->|imports| ext_torch
    topogpt3_lens_model_py -.->|imports| ext_torch
    topogpt3_lens_model_py -.->|imports| ext_safetensors_torch
    topogpt3_lens_model_py -.->|imports| ext_time
    topogpt3_lens_model_py -.->|imports| ext_torch
    topogpt3_lens_model_py -.->|imports| ext_model
    topogpt3_lens_model_py -.->|imports| ext_model
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
    topogpt3_model_py -.->|imports| ext_continuation
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
    ext_stdio_h["stdio.h"]
    class ext_stdio_h ext;
    topogpt3_c -.->|imports| ext_stdio_h
    ext_string_h["string.h"]
    class ext_string_h ext;
    topogpt3_c -.->|imports| ext_string_h
    ext_stdlib_h["stdlib.h"]
    class ext_stdlib_h ext;
    topogpt3_c -.->|imports| ext_stdlib_h
    topogpt3_c -.->|imports| ext_stdio_h
    topogpt3_c -.->|imports| ext_string_h
```

---

## UML Class Diagram

Auto-generated Mermaid class diagram from parsed class-level symbols. Shows classes, structs, interfaces, traits, and their methods with inheritance and dependency relationships.

```mermaid
classDiagram
  class governor_py_TokenStream {
    <<class>>
    +make_loop_detector(window, min_repeats)
    +make_timeout_hook(per_token_s)
    +__init__(self)
    +put(self, tok)
    +mark_done(self)
    +drain(self)
    +wait_for_new(self, timeout)
    +is_closed(self)
    +__len__(self)
    +__post_init__(self)
  }
  class governor_py_StopReason {
    <<class>>
    +make_loop_detector(window, min_repeats)
    +make_timeout_hook(per_token_s)
    +__init__(self)
    +put(self, tok)
    +mark_done(self)
    +drain(self)
    +wait_for_new(self, timeout)
    +is_closed(self)
    +__len__(self)
    +__post_init__(self)
  }
  class governor_py_GenerationResult {
    <<class>>
    +make_loop_detector(window, min_repeats)
    +make_timeout_hook(per_token_s)
    +__init__(self)
    +put(self, tok)
    +mark_done(self)
    +drain(self)
    +wait_for_new(self, timeout)
    +is_closed(self)
    +__len__(self)
    +__post_init__(self)
  }
  class governor_py_GenerationGovernor {
    <<class>>
    +make_loop_detector(window, min_repeats)
    +make_timeout_hook(per_token_s)
    +__init__(self)
    +put(self, tok)
    +mark_done(self)
    +drain(self)
    +wait_for_new(self, timeout)
    +is_closed(self)
    +__len__(self)
    +__post_init__(self)
  }
  class harness_py_ModelLoader {
    <<class>>
    +load_humaneval(cache_dir)
    +build_prompt(problem)
    +extract_candidate(prompt, completion)
    +run_one_test(problem, candidate_src, timeout)
    +run_one_test_sandboxed(problem, candidate_src, timeout, sandbox_cfg)
    +make_sampler(mode, settings_kwargs)
    +completion_for_problem(sampler, prompt)
    +evaluate_problem(problem, loader, args, sample_idx)
    +main()
    +__init__(self, ckpt_dir, ckpt_name, device)
  }
  class sandbox_py_SandboxConfig {
    <<class>>
    +_names_imported(tree)
    +_blocked_dunder_access(tree, blocked)
    +_max_depth(tree)
    +check_safety(source, cfg)
    +_build_worker_src(allowed_builtin_names, program_src, blocked_modules)
    +safe_exec(program_src, cfg, extra_globals)
    +describe_policy(cfg)
    +d(node, cur)
  }
  class synthetic_dataset_py_LLMBackend {
    <<class>>
    +build_backend(provider, model)
    +validate_sample(sample)
    +build_logger(level)
    +parse_args()
    +load_paths(paths_arg, paths_file, max_files)
    +main()
    +generate(self, prompt)
    +name(self)
    +__init__(self, model, api_key, max_tokens, temperature, timeout)
    +name(self)
  }
  class synthetic_dataset_py_GroqBackend {
    <<class>>
    +build_backend(provider, model)
    +validate_sample(sample)
    +build_logger(level)
    +parse_args()
    +load_paths(paths_arg, paths_file, max_files)
    +main()
    +generate(self, prompt)
    +name(self)
    +__init__(self, model, api_key, max_tokens, temperature, timeout)
    +name(self)
  }
  class synthetic_dataset_py_OpenRouterBackend {
    <<class>>
    +build_backend(provider, model)
    +validate_sample(sample)
    +build_logger(level)
    +parse_args()
    +load_paths(paths_arg, paths_file, max_files)
    +main()
    +generate(self, prompt)
    +name(self)
    +__init__(self, model, api_key, max_tokens, temperature, timeout)
    +name(self)
  }
  class synthetic_dataset_py_OllamaBackend {
    <<class>>
    +build_backend(provider, model)
    +validate_sample(sample)
    +build_logger(level)
    +parse_args()
    +load_paths(paths_arg, paths_file, max_files)
    +main()
    +generate(self, prompt)
    +name(self)
    +__init__(self, model, api_key, max_tokens, temperature, timeout)
    +name(self)
  }
  class synthetic_dataset_py_ProcessedManifest {
    <<class>>
    +build_backend(provider, model)
    +validate_sample(sample)
    +build_logger(level)
    +parse_args()
    +load_paths(paths_arg, paths_file, max_files)
    +main()
    +generate(self, prompt)
    +name(self)
    +__init__(self, model, api_key, max_tokens, temperature, timeout)
    +name(self)
  }
  class synthetic_dataset_py_SyntheticDatasetGenerator {
    <<class>>
    +build_backend(provider, model)
    +validate_sample(sample)
    +build_logger(level)
    +parse_args()
    +load_paths(paths_arg, paths_file, max_files)
    +main()
    +generate(self, prompt)
    +name(self)
    +__init__(self, model, api_key, max_tokens, temperature, timeout)
    +name(self)
  }
  class test_jlens_py_TestValidPositionMask {
    <<class>>
    +test_basic_mask(self)
    +test_too_short_raises(self)
    +test_negative_skip_raises(self)
    +test_all_positions_valid(self)
    +test_exact_minimum_length(self)
    +model(self)
    +test_returns_jacobians_for_source_layers(self, model)
    +test_late_layer_jacobian_close_to_identity(self, model)
    +test_earlier_layers_further_from_identity(self, model)
    +test_exact_jacobian_for_last_block(self, model)
  }
  class test_jlens_py_TestJacobianForPrompt {
    <<class>>
    +test_basic_mask(self)
    +test_too_short_raises(self)
    +test_negative_skip_raises(self)
    +test_all_positions_valid(self)
    +test_exact_minimum_length(self)
    +model(self)
    +test_returns_jacobians_for_source_layers(self, model)
    +test_late_layer_jacobian_close_to_identity(self, model)
    +test_earlier_layers_further_from_identity(self, model)
    +test_exact_jacobian_for_last_block(self, model)
  }
  class test_jlens_py_TestFit {
    <<class>>
    +test_basic_mask(self)
    +test_too_short_raises(self)
    +test_negative_skip_raises(self)
    +test_all_positions_valid(self)
    +test_exact_minimum_length(self)
    +model(self)
    +test_returns_jacobians_for_source_layers(self, model)
    +test_late_layer_jacobian_close_to_identity(self, model)
    +test_earlier_layers_further_from_identity(self, model)
    +test_exact_jacobian_for_last_block(self, model)
  }
  class test_jlens_py_TestJacobianLens {
    <<class>>
    +test_basic_mask(self)
    +test_too_short_raises(self)
    +test_negative_skip_raises(self)
    +test_all_positions_valid(self)
    +test_exact_minimum_length(self)
    +model(self)
    +test_returns_jacobians_for_source_layers(self, model)
    +test_late_layer_jacobian_close_to_identity(self, model)
    +test_earlier_layers_further_from_identity(self, model)
    +test_exact_jacobian_for_last_block(self, model)
  }
  class test_jlens_py_TestFitCheckpoint {
    <<class>>
    +test_basic_mask(self)
    +test_too_short_raises(self)
    +test_negative_skip_raises(self)
    +test_all_positions_valid(self)
    +test_exact_minimum_length(self)
    +model(self)
    +test_returns_jacobians_for_source_layers(self, model)
    +test_late_layer_jacobian_close_to_identity(self, model)
    +test_earlier_layers_further_from_identity(self, model)
    +test_exact_jacobian_for_last_block(self, model)
  }
  class test_jlens_py_TestConfig {
    <<class>>
    +test_basic_mask(self)
    +test_too_short_raises(self)
    +test_negative_skip_raises(self)
    +test_all_positions_valid(self)
    +test_exact_minimum_length(self)
    +model(self)
    +test_returns_jacobians_for_source_layers(self, model)
    +test_late_layer_jacobian_close_to_identity(self, model)
    +test_earlier_layers_further_from_identity(self, model)
    +test_exact_jacobian_for_last_block(self, model)
  }
  class test_jlens_py_TestTopoGPT3JLensAppConfig {
    <<class>>
    +test_basic_mask(self)
    +test_too_short_raises(self)
    +test_negative_skip_raises(self)
    +test_all_positions_valid(self)
    +test_exact_minimum_length(self)
    +model(self)
    +test_returns_jacobians_for_source_layers(self, model)
    +test_late_layer_jacobian_close_to_identity(self, model)
    +test_earlier_layers_further_from_identity(self, model)
    +test_exact_jacobian_for_last_block(self, model)
  }
  class test_lens_model_py_TestTopoGPT3LensConfig {
    <<class>>
    +test_default_config(self)
    +test_from_topogpt2_config(self)
    +test_probe_checkpoint_missing_raises(self, tmp_path)
    +test_default_parameters(self)
    +test_forward_output_shape(self)
    +test_weight_tied(self)
    +raw_model(self)
    +lens_model(self, raw_model)
    +test_exposes_protocol_attributes(self, lens_model, raw_model)
    +test_encode_text_to_token_ids(self, lens_model)
  }
  class test_lens_model_py_TestTinyDecoder {
    <<class>>
    +test_default_config(self)
    +test_from_topogpt2_config(self)
    +test_probe_checkpoint_missing_raises(self, tmp_path)
    +test_default_parameters(self)
    +test_forward_output_shape(self)
    +test_weight_tied(self)
    +raw_model(self)
    +lens_model(self, raw_model)
    +test_exposes_protocol_attributes(self, lens_model, raw_model)
    +test_encode_text_to_token_ids(self, lens_model)
  }
  class test_lens_model_py_TestTopoGPT3LensModel {
    <<class>>
    +test_default_config(self)
    +test_from_topogpt2_config(self)
    +test_probe_checkpoint_missing_raises(self, tmp_path)
    +test_default_parameters(self)
    +test_forward_output_shape(self)
    +test_weight_tied(self)
    +raw_model(self)
    +lens_model(self, raw_model)
    +test_exposes_protocol_attributes(self, lens_model, raw_model)
    +test_encode_text_to_token_ids(self, lens_model)
  }
  class test_lens_model_py_TestTopoGPT3LensModelWithRecording {
    <<class>>
    +test_default_config(self)
    +test_from_topogpt2_config(self)
    +test_probe_checkpoint_missing_raises(self, tmp_path)
    +test_default_parameters(self)
    +test_forward_output_shape(self)
    +test_weight_tied(self)
    +raw_model(self)
    +lens_model(self, raw_model)
    +test_exposes_protocol_attributes(self, lens_model, raw_model)
    +test_encode_text_to_token_ids(self, lens_model)
  }
  class test_lens_model_py_TestTopoGPT3LensModelEdgeCases {
    <<class>>
    +test_default_config(self)
    +test_from_topogpt2_config(self)
    +test_probe_checkpoint_missing_raises(self, tmp_path)
    +test_default_parameters(self)
    +test_forward_output_shape(self)
    +test_weight_tied(self)
    +raw_model(self)
    +lens_model(self, raw_model)
    +test_exposes_protocol_attributes(self, lens_model, raw_model)
    +test_encode_text_to_token_ids(self, lens_model)
  }
  class api_server_py_ApiKey {
    <<class>>
    +_setup_logging(verbose)
    +_parse_keys(raw)
    +_sha256(raw)
    +_sanitize_stop(stop)
    +_resolve_device(device)
    +_probe_n_kv(checkpoint_dir)
    +load_model(checkpoint, device)
    +lifespan(app)
    +_security_middleware(request, call_next)
    +_real_ip(request)
  }
  class api_server_py_AuthState {
    <<class>>
    +_setup_logging(verbose)
    +_parse_keys(raw)
    +_sha256(raw)
    +_sanitize_stop(stop)
    +_resolve_device(device)
    +_probe_n_kv(checkpoint_dir)
    +load_model(checkpoint, device)
    +lifespan(app)
    +_security_middleware(request, call_next)
    +_real_ip(request)
  }
  class api_server_py_TokenBucket {
    <<class>>
    +_setup_logging(verbose)
    +_parse_keys(raw)
    +_sha256(raw)
    +_sanitize_stop(stop)
    +_resolve_device(device)
    +_probe_n_kv(checkpoint_dir)
    +load_model(checkpoint, device)
    +lifespan(app)
    +_security_middleware(request, call_next)
    +_real_ip(request)
  }
  class api_server_py_RateLimiter {
    <<class>>
    +_setup_logging(verbose)
    +_parse_keys(raw)
    +_sha256(raw)
    +_sanitize_stop(stop)
    +_resolve_device(device)
    +_probe_n_kv(checkpoint_dir)
    +load_model(checkpoint, device)
    +lifespan(app)
    +_security_middleware(request, call_next)
    +_real_ip(request)
  }
  class api_server_py_IpBanner {
    <<class>>
    +_setup_logging(verbose)
    +_parse_keys(raw)
    +_sha256(raw)
    +_sanitize_stop(stop)
    +_resolve_device(device)
    +_probe_n_kv(checkpoint_dir)
    +load_model(checkpoint, device)
    +lifespan(app)
    +_security_middleware(request, call_next)
    +_real_ip(request)
  }
  class api_server_py_CompletionRequest {
    <<class>>
    +_setup_logging(verbose)
    +_parse_keys(raw)
    +_sha256(raw)
    +_sanitize_stop(stop)
    +_resolve_device(device)
    +_probe_n_kv(checkpoint_dir)
    +load_model(checkpoint, device)
    +lifespan(app)
    +_security_middleware(request, call_next)
    +_real_ip(request)
  }
  class api_server_py_Message {
    <<class>>
    +_setup_logging(verbose)
    +_parse_keys(raw)
    +_sha256(raw)
    +_sanitize_stop(stop)
    +_resolve_device(device)
    +_probe_n_kv(checkpoint_dir)
    +load_model(checkpoint, device)
    +lifespan(app)
    +_security_middleware(request, call_next)
    +_real_ip(request)
  }
  class api_server_py_ChatCompletionRequest {
    <<class>>
    +_setup_logging(verbose)
    +_parse_keys(raw)
    +_sha256(raw)
    +_sanitize_stop(stop)
    +_resolve_device(device)
    +_probe_n_kv(checkpoint_dir)
    +load_model(checkpoint, device)
    +lifespan(app)
    +_security_middleware(request, call_next)
    +_real_ip(request)
  }
  class api_server_py_ServerModel {
    <<class>>
    +_setup_logging(verbose)
    +_parse_keys(raw)
    +_sha256(raw)
    +_sanitize_stop(stop)
    +_resolve_device(device)
    +_probe_n_kv(checkpoint_dir)
    +load_model(checkpoint, device)
    +lifespan(app)
    +_security_middleware(request, call_next)
    +_real_ip(request)
  }
  class inference_py_ScalePreset {
    <<class>>
    +main(argv)
    +scale_presets()
    +preset(self)
    +validate(self)
    +build(settings)
    +resolve_under(root)
    +require_existing_file(path, expected_suffix)
    +__init__(self, settings, logger)
    +load(self)
    +__init__(self, settings)
  }
  class inference_py_InferenceSettings {
    <<class>>
    +main(argv)
    +scale_presets()
    +preset(self)
    +validate(self)
    +build(settings)
    +resolve_under(root)
    +require_existing_file(path, expected_suffix)
    +__init__(self, settings, logger)
    +load(self)
    +__init__(self, settings)
  }
  class inference_py_InferenceLoggerFactory {
    <<class>>
    +main(argv)
    +scale_presets()
    +preset(self)
    +validate(self)
    +build(settings)
    +resolve_under(root)
    +require_existing_file(path, expected_suffix)
    +__init__(self, settings, logger)
    +load(self)
    +__init__(self, settings)
  }
  class inference_py_SecurePathResolver {
    <<class>>
    +main(argv)
    +scale_presets()
    +preset(self)
    +validate(self)
    +build(settings)
    +resolve_under(root)
    +require_existing_file(path, expected_suffix)
    +__init__(self, settings, logger)
    +load(self)
    +__init__(self, settings)
  }
  class inference_py_SourceModuleLoader {
    <<class>>
    +main(argv)
    +scale_presets()
    +preset(self)
    +validate(self)
    +build(settings)
    +resolve_under(root)
    +require_existing_file(path, expected_suffix)
    +__init__(self, settings, logger)
    +load(self)
    +__init__(self, settings)
  }
  class inference_py_CheckpointPaths {
    <<class>>
    +main(argv)
    +scale_presets()
    +preset(self)
    +validate(self)
    +build(settings)
    +resolve_under(root)
    +require_existing_file(path, expected_suffix)
    +__init__(self, settings, logger)
    +load(self)
    +__init__(self, settings)
  }
  class inference_py_WeightShapeProbe {
    <<class>>
    +main(argv)
    +scale_presets()
    +preset(self)
    +validate(self)
    +build(settings)
    +resolve_under(root)
    +require_existing_file(path, expected_suffix)
    +__init__(self, settings, logger)
    +load(self)
    +__init__(self, settings)
  }
  class inference_py_TopoGPT2ConfigAligner {
    <<class>>
    +main(argv)
    +scale_presets()
    +preset(self)
    +validate(self)
    +build(settings)
    +resolve_under(root)
    +require_existing_file(path, expected_suffix)
    +__init__(self, settings, logger)
    +load(self)
    +__init__(self, settings)
  }
  class inference_py_TokenizerFactory {
    <<class>>
    +main(argv)
    +scale_presets()
    +preset(self)
    +validate(self)
    +build(settings)
    +resolve_under(root)
    +require_existing_file(path, expected_suffix)
    +__init__(self, settings, logger)
    +load(self)
    +__init__(self, settings)
  }
  class inference_py_GaussPatchApplier {
    <<class>>
    +main(argv)
    +scale_presets()
    +preset(self)
    +validate(self)
    +build(settings)
    +resolve_under(root)
    +require_existing_file(path, expected_suffix)
    +__init__(self, settings, logger)
    +load(self)
    +__init__(self, settings)
  }
  class inference_py_ModelAssembler {
    <<class>>
    +main(argv)
    +scale_presets()
    +preset(self)
    +validate(self)
    +build(settings)
    +resolve_under(root)
    +require_existing_file(path, expected_suffix)
    +__init__(self, settings, logger)
    +load(self)
    +__init__(self, settings)
  }
  class inference_py_SeedSynchronizer {
    <<class>>
    +main(argv)
    +scale_presets()
    +preset(self)
    +validate(self)
    +build(settings)
    +resolve_under(root)
    +require_existing_file(path, expected_suffix)
    +__init__(self, settings, logger)
    +load(self)
    +__init__(self, settings)
  }
  class inference_py_SamplingPolicy {
    <<class>>
    +main(argv)
    +scale_presets()
    +preset(self)
    +validate(self)
    +build(settings)
    +resolve_under(root)
    +require_existing_file(path, expected_suffix)
    +__init__(self, settings, logger)
    +load(self)
    +__init__(self, settings)
  }
  class inference_py_GenerationReport {
    <<class>>
    +main(argv)
    +scale_presets()
    +preset(self)
    +validate(self)
    +build(settings)
    +resolve_under(root)
    +require_existing_file(path, expected_suffix)
    +__init__(self, settings, logger)
    +load(self)
    +__init__(self, settings)
  }
  class inference_py_GenerationEngine {
    <<class>>
    +main(argv)
    +scale_presets()
    +preset(self)
    +validate(self)
    +build(settings)
    +resolve_under(root)
    +require_existing_file(path, expected_suffix)
    +__init__(self, settings, logger)
    +load(self)
    +__init__(self, settings)
  }
  class inference_py_ResultRenderer {
    <<class>>
    +main(argv)
    +scale_presets()
    +preset(self)
    +validate(self)
    +build(settings)
    +resolve_under(root)
    +require_existing_file(path, expected_suffix)
    +__init__(self, settings, logger)
    +load(self)
    +__init__(self, settings)
  }
  class inference_py_InferencePipeline {
    <<class>>
    +main(argv)
    +scale_presets()
    +preset(self)
    +validate(self)
    +build(settings)
    +resolve_under(root)
    +require_existing_file(path, expected_suffix)
    +__init__(self, settings, logger)
    +load(self)
    +__init__(self, settings)
  }
```

---

## Code Property Graph

Machine-readable Code Property Graph (CPG) in JSON-LD format. This block allows AI agents to parse the full structural graph without additional file reads. Compatible with GraphRAG pipelines.

```json
{"@context": "https://schema.org", "analysis": {"communities": [{"cohesion": 0.935, "id": 0, "label": "topogpt3", "size": 16}, {"cohesion": 0.5, "id": 1, "label": "eval", "size": 2}, {"cohesion": 0.8, "id": 2, "label": "eval", "size": 10}], "god_nodes": [{"node_id": "topogpt3/model.py", "score": 36.7}, {"node_id": "topogpt3.c", "score": 23.9}, {"node_id": "topogpt3/__init__.py", "score": 16.0}, {"node_id": "topogpt3/lens_model.py", "score": 14.9}, {"node_id": "topogpt3/train.py", "score": 14.2}, {"node_id": "topogpt3/inference_hrm.py", "score": 13.6}, {"node_id": "eval/harness.py", "score": 13.2}, {"node_id": "topogpt3/jlens.py", "score": 12.9}, {"node_id": "topogpt3/__main__.py", "score": 12.1}, {"node_id": "topogpt3/api_server.py", "score": 10.6}], "surprising_connections": [{"hops": 6, "source": "app.py", "target": "eval/governor.py"}, {"hops": 6, "source": "app.py", "target": "eval/sandbox_smoke.py"}, {"hops": 6, "source": "eval/governor.py", "target": "gradio_app.py"}, {"hops": 6, "source": "eval/governor.py", "target": "tests/test_jlens.py"}, {"hops": 6, "source": "eval/governor.py", "target": "topogpt3/inference.py"}]}, "edges": [{"confidence": "EXTRACTED", "relation": "imports", "source": "app.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app.py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app.py", "target": "topogpt3"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "convert_weights.py", "target": "struct"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "convert_weights.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "convert_weights.py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "convert_weights.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "convert_weights.py", "target": "safetensors"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "convert_weights_minios.py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "convert_weights_minios.py", "target": "struct"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "convert_weights_minios.py", "target": "numpy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "convert_weights_minios.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "convert_weights_minios.py", "target": "safetensors"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "convert_weights_minios.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "encode_tokens.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "encode_tokens.py", "target": "struct"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "encode_tokens.py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "encode_tokens.py", "target": "tiktoken"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/analyze.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/analyze.py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/analyze.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/analyze.py", "target": "math"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/analyze.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/analyze.py", "target": "collections"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/analyze.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/analyze.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/analyze_results.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/analyze_results.py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/analyze_results.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/analyze_results.py", "target": "collections"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/analyze_results.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/diag_static.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/diag_static.py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/diag_static.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/diag_static.py", "target": "math"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/diag_static.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/diag_static.py", "target": "time"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/diag_static.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/diag_static.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/diag_static.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/diag_static.py", "target": "topogpt3"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/diag_static.py", "target": "topogpt3.model"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/diag_static.py", "target": "safetensors.torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/diag_static.py", "target": "topogpt3.train"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/governor.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/governor.py", "target": "threading"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/governor.py", "target": "time"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/governor.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/governor.py", "target": "enum"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/governor.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/governor.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/governor.py", "target": "torch.nn.functional"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/governor_smoke.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/governor_smoke.py", "target": "threading"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/governor_smoke.py", "target": "time"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/governor_smoke.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/governor_smoke.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/governor_smoke.py", "target": "eval.governor"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/governor_smoke.py", "target": "topogpt3"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/governor_smoke.py", "target": "safetensors"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/governor_smoke.py", "target": "safetensors.torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/harness.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/harness.py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/harness.py", "target": "contextlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/harness.py", "target": "io"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/harness.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/harness.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/harness.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/harness.py", "target": "signal"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/harness.py", "target": "subprocess"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/harness.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/harness.py", "target": "time"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/harness.py", "target": "traceback"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/harness.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/harness.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/harness.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/harness.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/harness.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/harness.py", "target": "topogpt3"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/harness.py", "target": "eval.samplers"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/harness.py", "target": "safetensors.torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/harness.py", "target": "datasets"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/harness.py", "target": "eval.sandbox"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/harness.py", "target": "eval.samplers"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/harness.py", "target": "safetensors"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/integration_smoke.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/integration_smoke.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/integration_smoke.py", "target": "eval.harness"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/noise_analysis.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/noise_analysis.py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/noise_analysis.py", "target": "ast"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/noise_analysis.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/noise_analysis.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/noise_analysis.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/noise_analysis.py", "target": "collections"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/noise_analysis.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/noise_analysis.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/noise_sweep.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/noise_sweep.py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/noise_sweep.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/noise_sweep.py", "target": "math"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/noise_sweep.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/noise_sweep.py", "target": "time"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/noise_sweep.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/noise_sweep.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/noise_sweep.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/noise_sweep.py", "target": "topogpt3"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/noise_sweep.py", "target": "topogpt3.model"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/noise_sweep.py", "target": "safetensors.torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/noise_sweep.py", "target": "safetensors"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/noise_sweep.py", "target": "eval.harness"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/repair.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/repair.py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/repair.py", "target": "contextlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/repair.py", "target": "io"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/repair.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/repair.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/repair.py", "target": "time"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/repair.py", "target": "traceback"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/repair.py", "target": "collections"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/repair.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/repair.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/repair.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/repair.py", "target": "safetensors"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/repair.py", "target": "safetensors.torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/repair.py", "target": "topogpt3"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/repair.py", "target": "datasets"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/report.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/report.py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/report.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/report.py", "target": "math"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/report.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/report.py", "target": "shutil"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/report.py", "target": "statistics"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/report.py", "target": "collections"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/report.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/samplers.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/samplers.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/samplers.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/samplers.py", "target": "topogpt3"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/sandbox.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/sandbox.py", "target": "ast"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/sandbox.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/sandbox.py", "target": "subprocess"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/sandbox.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/sandbox.py", "target": "tempfile"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/sandbox.py", "target": "textwrap"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/sandbox.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/sandbox.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/sandbox.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/sandbox.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/sandbox_smoke.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/sandbox_smoke.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/sandbox_smoke.py", "target": "eval.sandbox"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/smoke.py", "target": "time"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/smoke.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/smoke.py", "target": "topogpt3"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/temp_sweep.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/temp_sweep.py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/temp_sweep.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/temp_sweep.py", "target": "math"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/temp_sweep.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/temp_sweep.py", "target": "time"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/temp_sweep.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/temp_sweep.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/temp_sweep.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/temp_sweep.py", "target": "eval.noise_sweep"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "eval/temp_sweep.py", "target": "eval.harness"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "gradio_app.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "gradio_app.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "gradio_app.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "gradio_app.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "gradio_app.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "gradio_app.py", "target": "gradio"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "gradio_app.py", "target": "topogpt3"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "gradio_app.py", "target": "huggingface_hub"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "synthetic_dataset.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "synthetic_dataset.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "synthetic_dataset.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "synthetic_dataset.py", "target": "time"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "synthetic_dataset.py", "target": "hashlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "synthetic_dataset.py", "target": "logging"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "synthetic_dataset.py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "synthetic_dataset.py", "target": "tempfile"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "synthetic_dataset.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "synthetic_dataset.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "synthetic_dataset.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "synthetic_dataset.py", "target": "datetime"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "synthetic_dataset.py", "target": "threading"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "synthetic_dataset.py", "target": "queue"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "synthetic_dataset.py", "target": "concurrent.futures"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "synthetic_dataset.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "synthetic_dataset.py", "target": "numpy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "synthetic_dataset.py", "target": "tiktoken"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "synthetic_dataset.py", "target": "requests"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "synthetic_dataset.py", "target": "requests"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "synthetic_dataset.py", "target": "requests"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "synthetic_dataset.py", "target": "requests"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "synthetic_dataset.py", "target": "requests"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "synthetic_dataset.py", "target": "requests"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_jlens.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_jlens.py", "target": "pytest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_jlens.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_jlens.py", "target": "topogpt3.lens_model"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_jlens.py", "target": "topogpt3.jlens"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_lens_model.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_lens_model.py", "target": "pytest"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_lens_model.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_lens_model.py", "target": "topogpt3.lens_model"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_lens_model.py", "target": "topogpt3.model"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_lens_model.py", "target": "topogpt3.model"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_lens_model.py", "target": "types"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_lens_model.py", "target": "topogpt3.jlens"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_lens_model.py", "target": "topogpt3.jlens"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_lens_model.py", "target": "topogpt3.jlens"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "tests/test_lens_model.py", "target": "topogpt3.jlens"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/__init__.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/__init__.py", "target": "model"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/__init__.py", "target": "train"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/__init__.py", "target": "inference"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/__init__.py", "target": "inference_hrm"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/__init__.py", "target": "lens_model"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/__init__.py", "target": "jlens"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/__main__.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/__main__.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/__main__.py", "target": "jlens"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/__main__.py", "target": "lens_model"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/__main__.py", "target": "api_server"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/__main__.py", "target": "inference"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/__main__.py", "target": "inference_hrm"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/__main__.py", "target": "train"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/api_server.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/api_server.py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/api_server.py", "target": "hashlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/api_server.py", "target": "hmac"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/api_server.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/api_server.py", "target": "logging"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/api_server.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/api_server.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/api_server.py", "target": "secrets"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/api_server.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/api_server.py", "target": "time"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/api_server.py", "target": "collections"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/api_server.py", "target": "contextlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/api_server.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/api_server.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/api_server.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/api_server.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/api_server.py", "target": "model"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/api_server.py", "target": "safetensors.torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/api_server.py", "target": "fastapi"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/api_server.py", "target": "fastapi.middleware.cors"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/api_server.py", "target": "fastapi.middleware.gzip"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/api_server.py", "target": "fastapi.responses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/api_server.py", "target": "pydantic"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/api_server.py", "target": "uvicorn"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/api_server.py", "target": "safetensors"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/api_server.py", "target": "continuation"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/continuation.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/continuation.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/continuation.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/inference.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/inference.py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/inference.py", "target": "logging"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/inference.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/inference.py", "target": "time"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/inference.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/inference.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/inference.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/inference.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/inference.py", "target": "safetensors"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/inference.py", "target": "safetensors.torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/inference_hrm.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/inference_hrm.py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/inference_hrm.py", "target": "logging"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/inference_hrm.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/inference_hrm.py", "target": "time"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/inference_hrm.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/inference_hrm.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/inference_hrm.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/inference_hrm.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/inference_hrm.py", "target": "torch.nn.functional"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/inference_hrm.py", "target": "safetensors"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/inference_hrm.py", "target": "safetensors.torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/inference_hrm.py", "target": "continuation"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/jlens.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/jlens.py", "target": "logging"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/jlens.py", "target": "math"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/jlens.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/jlens.py", "target": "time"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/jlens.py", "target": "collections.abc"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/jlens.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/jlens.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/jlens.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/jlens.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/jlens.py", "target": "lens_model"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/jlens.py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/jlens.py", "target": "lens_model"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/jlens.py", "target": "huggingface_hub"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/lens_model.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/lens_model.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/lens_model.py", "target": "collections.abc"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/lens_model.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/lens_model.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/lens_model.py", "target": "types"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/lens_model.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/lens_model.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/lens_model.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/lens_model.py", "target": "safetensors.torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/lens_model.py", "target": "time"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/lens_model.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/lens_model.py", "target": "model"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/lens_model.py", "target": "model"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/model.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/model.py", "target": "torch.nn"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/model.py", "target": "torch.nn.functional"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/model.py", "target": "torch.utils.checkpoint"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/model.py", "target": "safetensors.torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/model.py", "target": "numpy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/model.py", "target": "math"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/model.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/model.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/model.py", "target": "time"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/model.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/model.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/model.py", "target": "hashlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/model.py", "target": "logging"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/model.py", "target": "warnings"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/model.py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/model.py", "target": "datetime"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/model.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/model.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/model.py", "target": "collections"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/model.py", "target": "collections"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/model.py", "target": "synthetic_dataset"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/model.py", "target": "continuation"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/model.py", "target": "tiktoken"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/model.py", "target": "shutil"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/train.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/train.py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/train.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/train.py", "target": "logging"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/train.py", "target": "math"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/train.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/train.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/train.py", "target": "time"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/train.py", "target": "collections"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/train.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/train.py", "target": "datetime"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/train.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/train.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/train.py", "target": "numpy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/train.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/train.py", "target": "torch.nn"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/train.py", "target": "torch.nn.functional"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/train.py", "target": "model"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/train.py", "target": "safetensors.torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/train.py", "target": "safetensors.torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3/train.py", "target": "datasets"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3.c", "target": "stdio.h"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3.c", "target": "string.h"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3.c", "target": "stdlib.h"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3.c", "target": "stdio.h"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt3.c", "target": "string.h"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "app.py", "target": "topogpt3/__init__.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "eval/diag_static.py", "target": "topogpt3.c"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "eval/diag_static.py", "target": "topogpt3/model.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "eval/diag_static.py", "target": "topogpt3/train.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "eval/governor_smoke.py", "target": "eval/governor.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "eval/governor_smoke.py", "target": "topogpt3.c"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "eval/harness.py", "target": "topogpt3.c"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "eval/harness.py", "target": "eval/samplers.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "eval/harness.py", "target": "eval/sandbox.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "eval/harness.py", "target": "eval/samplers.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "eval/integration_smoke.py", "target": "eval/harness.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "eval/noise_sweep.py", "target": "topogpt3.c"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "eval/noise_sweep.py", "target": "topogpt3/model.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "eval/noise_sweep.py", "target": "eval/harness.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "eval/repair.py", "target": "topogpt3.c"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "eval/samplers.py", "target": "topogpt3.c"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "eval/sandbox_smoke.py", "target": "eval/sandbox.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "eval/smoke.py", "target": "topogpt3.c"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "eval/temp_sweep.py", "target": "eval/noise_sweep.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "eval/temp_sweep.py", "target": "eval/harness.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "gradio_app.py", "target": "topogpt3/__init__.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_jlens.py", "target": "topogpt3/lens_model.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_jlens.py", "target": "topogpt3/jlens.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_lens_model.py", "target": "topogpt3/lens_model.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_lens_model.py", "target": "topogpt3/model.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_lens_model.py", "target": "topogpt3/model.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_lens_model.py", "target": "topogpt3/jlens.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_lens_model.py", "target": "topogpt3/jlens.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_lens_model.py", "target": "topogpt3/jlens.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "tests/test_lens_model.py", "target": "topogpt3/jlens.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "topogpt3/__init__.py", "target": "topogpt3/model.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "topogpt3/__init__.py", "target": "topogpt3/train.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "topogpt3/__init__.py", "target": "topogpt3/inference.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "topogpt3/__init__.py", "target": "topogpt3/inference_hrm.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "topogpt3/__init__.py", "target": "topogpt3/lens_model.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "topogpt3/__init__.py", "target": "topogpt3/jlens.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "topogpt3/__main__.py", "target": "topogpt3/jlens.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "topogpt3/__main__.py", "target": "topogpt3/lens_model.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "topogpt3/__main__.py", "target": "topogpt3/api_server.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "topogpt3/__main__.py", "target": "topogpt3/inference.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "topogpt3/__main__.py", "target": "topogpt3/inference_hrm.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "topogpt3/__main__.py", "target": "topogpt3/train.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "topogpt3/api_server.py", "target": "topogpt3/model.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "topogpt3/api_server.py", "target": "topogpt3/continuation.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "topogpt3/inference_hrm.py", "target": "topogpt3/continuation.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "topogpt3/jlens.py", "target": "topogpt3/lens_model.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "topogpt3/jlens.py", "target": "topogpt3/lens_model.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "topogpt3/lens_model.py", "target": "topogpt3/model.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "topogpt3/lens_model.py", "target": "topogpt3/model.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "topogpt3/model.py", "target": "synthetic_dataset.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "topogpt3/model.py", "target": "topogpt3/continuation.py"}, {"confidence": "EXTRACTED", "relation": "resolved_imports", "source": "topogpt3/train.py", "target": "topogpt3/model.py"}], "generator": "readmenator", "metadata": {"edge_count": 5261, "file_count": 36, "language_count": 3, "symbol_count": 818}, "nodes": [{"id": "app.py", "kind": "module", "label": "app.py", "language": "py", "sha256": "d456da403bd5058f", "symbol_count": 5, "symbols": [{"doc": "Run the standard sampler and return the generated completion text.", "kind": "function", "line": 46, "name": "run_inference", "signature": "def run_inference(prompt, checkpoint_dir, checkpoint_name, max_new_tokens, temperature, top_k, repetition_penalty, device)"}, {"doc": "Run the hierarchical recursive sampler and return the completion.", "kind": "function", "line": 71, "name": "run_inference_hrm", "signature": "def run_inference_hrm(prompt, checkpoint_dir, checkpoint_name, max_new_tokens, temperature, top_k, repetition_penalty, high_level_iters, low_level_iters, low_level_window, device)"}, {"doc": "Run the full TopoGPT3 curriculum trainer.", "kind": "function", "line": 105, "name": "run_training", "signature": "def run_training(scale, start_tier, device, prepare_data)"}, {"doc": "Build the top-level CLI for this entry point script.", "kind": "function", "line": 121, "name": "_build_parser", "signature": "def _build_parser()"}, {"doc": "Entry point invoked when the file is executed as a script.", "kind": "function", "line": 159, "name": "main", "signature": "def main(argv)"}]}, {"id": "convert_weights.py", "kind": "module", "label": "convert_weights.py", "language": "py", "sha256": "5e41f9845fd9a3c4", "symbol_count": 2, "symbols": [{"kind": "function", "line": 102, "name": "convert", "signature": "def convert(input_path, output_path)"}, {"kind": "function", "line": 160, "name": "main", "signature": "def main()"}]}, {"id": "convert_weights_minios.py", "kind": "module", "label": "convert_weights_minios.py", "language": "py", "sha256": "c9b5b4c0a63a6bff", "symbol_count": 1, "symbols": [{"kind": "function", "line": 85, "name": "main", "signature": "def main()"}]}, {"id": "encode_tokens.py", "kind": "module", "label": "encode_tokens.py", "language": "py", "sha256": "499b0ef3c8c17b8c", "symbol_count": 1, "symbols": [{"kind": "function", "line": 19, "name": "main", "signature": "def main()"}]}, {"id": "eval/analyze.py", "kind": "module", "label": "analyze.py", "language": "py", "sha256": "351b50620aa106b7", "symbol_count": 5, "symbols": [{"doc": "Unbiased estimator from the HumanEval paper.\n\npass@k = 1 - C(n-c, k) / C(n, k)   if n - c >= k else 1.0\nn = total samples, c = correct samples, k = target", "kind": "function", "line": 21, "name": "pass_at_k", "signature": "def pass_at_k(n, c, k)"}, {"doc": "Heuristic single-label error classifier.", "kind": "function", "line": 32, "name": "classify_error", "signature": "def classify_error(msg, candidate_src)"}, {"kind": "function", "line": 56, "name": "load_jsonl", "signature": "def load_jsonl(path)"}, {"kind": "function", "line": 61, "name": "summarize", "signature": "def summarize(paths)"}, {"kind": "function", "line": 103, "name": "main", "signature": "def main()"}]}, {"id": "eval/analyze_results.py", "kind": "module", "label": "analyze_results.py", "language": "py", "sha256": "aed01199698beec6", "symbol_count": 4, "symbols": [{"kind": "function", "line": 26, "name": "load_records", "signature": "def load_records(path)"}, {"kind": "function", "line": 31, "name": "summarize", "signature": "def summarize(records)"}, {"kind": "function", "line": 44, "name": "show_failures", "signature": "def show_failures(records, task_id)"}, {"kind": "function", "line": 82, "name": "main", "signature": "def main()"}]}, {"id": "eval/diag_static.py", "kind": "module", "label": "diag_static.py", "language": "py", "sha256": "80ab610c55205ed7", "symbol_count": 5, "symbols": [{"doc": "Muestrea n_samples overlaps aleatorios <u_i | u_j> sobre los vectores\nsingulares de K y mide cuanto se aleja su fase arg del reticulo 2*pi*Z.\n\ndelta = max |theta/2pi - round(theta/2pi)| sobre la muestra.\n\nTambien devuelve:\n  delta_mean, delta_median, frac_near_integer (|.| < 0.05)", "kind": "function", "line": 49, "name": "phase_discretization", "signature": "def phase_discretization(K, n_samples, seed)"}, {"doc": "Como el checkpoint es estatico, no hay trayectoria temporal.\nConstruimos una pseudo-trayectoria deslizando una ventana sobre\nlos modos de frecuencia (filas de K) y acumulando arg det del\noverlap entre ventanas consecutivas.\n\nW = (1/2pi) sum_n arg det <U_{n} | U_{n+1}>", "kind": "function", "line": 95, "name": "synthetic_winding", "signature": "def synthetic_winding(K, n_windows, window_size)"}, {"kind": "function", "line": 144, "name": "static_kappa", "signature": "def static_kappa(K)"}, {"kind": "function", "line": 171, "name": "context_length_diagnostic", "signature": "def context_length_diagnostic(model, tracker, device, lengths)"}, {"kind": "function", "line": 248, "name": "main", "signature": "def main()"}]}, {"id": "eval/governor.py", "kind": "module", "label": "governor.py", "language": "py", "sha256": "0a2e0b070f049594", "symbol_count": 20, "symbols": [{"doc": "Thread-safe single-producer / single-consumer queue of token IDs.\n\nThe producer (the generation loop) calls `put(tok)` for each new\ntoken. Consumers can iterate via `iter_tokens(block=True)` or\n`drain()` to get everything emitted so far.\n\nThe stream tracks a monotonic counter so consumers can detect\n\"no new tokens since last call\" cheaply.", "kind": "class", "line": 45, "name": "TokenStream", "signature": "class TokenStream"}, {"kind": "class", "line": 99, "name": "StopReason", "signature": "class StopReason(str, Enum)"}, {"doc": "Outcome of a governed generation.", "kind": "class", "line": 109, "name": "GenerationResult", "signature": "class GenerationResult"}, {"doc": "Run a model's autoregressive generation loop with optional stop\nhooks and a streaming interface.\n\nUsage:\n    ts = TokenStream()\n    governor = GenerationGovernor(\n        model=model,\n        ctx=prompt_tensor,\n        stream=ts,\n        max_new_tokens=256,\n        temperature=0.2,\n        top_k=40,\n        repetition_penalty=1.1,\n    )\n    result = governor.run(stop_hooks=[loop_detector, timeout_hook])\n    if result.stop_reason == StopReason.LOOP:\n        ...", "kind": "class", "line": 134, "name": "GenerationGovernor", "signature": "class GenerationGovernor"}, {"doc": "Return True if the last `window` tokens contain a sub-sequence\nof length >= `min_repeats` that repeats consecutively.\n\nCatches the \"model is stuck in a loop\" pathology where a 24M-param\nmodel emits the same 4-token pattern indefinitely.", "kind": "method", "line": 285, "name": "make_loop_detector", "signature": "def make_loop_detector(window, min_repeats)"}, {"doc": "Return True if the per-token wall time exceeds `per_token_s`.\nUseful for catching token-generation stalls (rare on CPU, but\nhappens under memory pressure).", "kind": "method", "line": 314, "name": "make_timeout_hook", "signature": "def make_timeout_hook(per_token_s)"}, {"kind": "method", "line": 56, "name": "__init__", "signature": "def __init__(self)"}, {"kind": "method", "line": 62, "name": "put", "signature": "def put(self, tok)"}, {"kind": "method", "line": 67, "name": "mark_done", "signature": "def mark_done(self)"}, {"doc": "Return all tokens emitted so far, atomic snapshot.", "kind": "method", "line": 72, "name": "drain", "signature": "def drain(self)"}, {"doc": "Block up to `timeout` seconds for a new token. Returns True\nif a new token arrived (or stream closed), False on timeout.", "kind": "method", "line": 77, "name": "wait_for_new", "signature": "def wait_for_new(self, timeout)"}, {"kind": "method", "line": 86, "name": "is_closed", "signature": "def is_closed(self)"}, {"kind": "method", "line": 90, "name": "__len__", "signature": "def __len__(self)"}, {"kind": "method", "line": 117, "name": "__post_init__", "signature": "def __post_init__(self)"}, {"kind": "method", "line": 156, "name": "__init__", "signature": "def __init__(self, model, ctx, stream, max_new_tokens, temperature, top_k, repetition_penalty, max_seq_len)"}, {"doc": "Asynchronously stop the generation. Safe to call from any\nthread (e.g. a watchdog thread or the main UI loop).", "kind": "method", "line": 177, "name": "cancel", "signature": "def cancel(self)"}, {"kind": "method", "line": 182, "name": "_should_cancel", "signature": "def _should_cancel(self)"}, {"doc": "Execute the generation loop. Returns when the model emits\nEOS, hits max_new_tokens, a hook returns True, or cancel() is\ncalled.", "kind": "method", "line": 185, "name": "run", "signature": "def run(self, stop_hooks)"}, {"kind": "method", "line": 292, "name": "hook", "signature": "def hook(generated)"}, {"kind": "method", "line": 320, "name": "hook", "signature": "def hook(generated)"}]}, {"id": "eval/governor_smoke.py", "kind": "module", "label": "governor_smoke.py", "language": "py", "sha256": "6adca837aa8182c8", "symbol_count": 7, "symbols": [{"kind": "function", "line": 30, "name": "load_model", "signature": "def load_model()"}, {"kind": "function", "line": 49, "name": "test_tokenstream_threadsafety", "signature": "def test_tokenstream_threadsafety()"}, {"kind": "function", "line": 79, "name": "test_governor_basic", "signature": "def test_governor_basic()"}, {"kind": "function", "line": 98, "name": "test_loop_detector", "signature": "def test_loop_detector()"}, {"kind": "function", "line": 118, "name": "test_cancel", "signature": "def test_cancel()"}, {"kind": "function", "line": 53, "name": "producer", "signature": "def producer()"}, {"kind": "function", "line": 59, "name": "consumer", "signature": "def consumer()"}]}, {"id": "eval/harness.py", "kind": "module", "label": "harness.py", "language": "py", "sha256": "384baed586db5396", "symbol_count": 12, "symbols": [{"kind": "function", "line": 59, "name": "load_humaneval", "signature": "def load_humaneval(cache_dir)"}, {"doc": "Return the exact prompt text fed to the model.\n\nHumanEval's `prompt` field already contains the function signature and\ndocstring, with the body to be completed starting on the next line.", "kind": "function", "line": 75, "name": "build_prompt", "signature": "def build_prompt(problem)"}, {"doc": "Combine prompt + completion into a single Python source string.\n\nThe completion may itself start with whitespace/indentation that\nbelongs inside the function body. We strip leading blank lines and\nthen concatenate; we also stop at the first top-level `def ` or\n`class ` to avoid the model continuing with extra functions.\n\nRobustness fixes:\n  - Strip the special <|endoftext|> (GPT-2 EOT) token that the model\n    emits at the end of every generation. Leaving it in the candidate\n    produces a SyntaxError and zeroes the pass rate.\n  - Drop any training-format delimiters (### Response, <|assistant|>,\n    <|user|>) that leak from the instruction-tuning corpus.\n  - Cut at the first top-level def/class/__main__ guard after the\n    function body has started.", "kind": "function", "line": 100, "name": "extract_candidate", "signature": "def extract_candidate(prompt, completion)"}, {"doc": "Execute the candidate against the hidden test.\n\nReturns (passed, message, stdout, stderr, traceback). We follow HumanEval's\n`evaluate` function: build namespace, exec the candidate, exec the test,\nexpect `check(candidate) == None`.", "kind": "function", "line": 150, "name": "run_one_test", "signature": "def run_one_test(problem, candidate_src, timeout)"}, {"doc": "Sandboxed variant of `run_one_test`. Runs the candidate in a\nsubprocess with stripped builtins, AST pre-check, and OS-enforced\ntimeout. Drop-in replacement: same 5-tuple return.\n\nEnable by passing `--sandbox` to `harness.py` (not yet wired) or\nby calling this function directly from your own evaluation script.", "kind": "function", "line": 172, "name": "run_one_test_sandboxed", "signature": "def run_one_test_sandboxed(problem, candidate_src, timeout, sandbox_cfg)"}, {"doc": "Backwards-compatible shim. The real implementation lives in\n`eval.samplers` as a decorator-based registry. We re-export here\nso existing imports of `from eval.harness import make_sampler`\nkeep working. New code should import from `eval.samplers`.", "kind": "function", "line": 195, "name": "make_sampler", "signature": "def make_sampler(mode, settings_kwargs)"}, {"doc": "Run a single completion and return (raw_output_text, metrics_dict).", "kind": "function", "line": 204, "name": "completion_for_problem", "signature": "def completion_for_problem(sampler, prompt)"}, {"doc": "Build the model and tokenizer once, run many generations.", "kind": "class", "line": 217, "name": "ModelLoader", "signature": "class ModelLoader"}, {"kind": "method", "line": 272, "name": "evaluate_problem", "signature": "def evaluate_problem(problem, loader, args, sample_idx)"}, {"kind": "method", "line": 315, "name": "main", "signature": "def main()"}, {"kind": "method", "line": 220, "name": "__init__", "signature": "def __init__(self, ckpt_dir, ckpt_name, device)"}, {"kind": "method", "line": 246, "name": "generate", "signature": "def generate(self, prompt, max_new_tokens, temperature, top_k, repetition_penalty)"}]}, {"id": "eval/integration_smoke.py", "kind": "module", "label": "integration_smoke.py", "language": "py", "sha256": "d23b6c8473c4cf4b", "symbol_count": 1, "symbols": [{"kind": "function", "line": 18, "name": "main", "signature": "def main()"}]}, {"id": "eval/noise_analysis.py", "kind": "module", "label": "noise_analysis.py", "language": "py", "sha256": "ab6bbc133fa88eb1", "symbol_count": 3, "symbols": [{"kind": "function", "line": 43, "name": "_load", "signature": "def _load(p)"}, {"doc": "Para cada problema, mira si pasa consistentemente a traves de los\n4 niveles de ruido. Devuelve:\n  - always_pass, always_fail, mixed (count)\n  - per_sigma_pass_lists: {sigma: {task_id: bool}}", "kind": "function", "line": 47, "name": "consistency_across_runs", "signature": "def consistency_across_runs(per_run)"}, {"kind": "function", "line": 83, "name": "main", "signature": "def main()"}]}, {"id": "eval/noise_sweep.py", "kind": "module", "label": "noise_sweep.py", "language": "py", "sha256": "0cbc44aa54b2844b", "symbol_count": 4, "symbols": [{"doc": "Anade N(0, sigma) a TODOS los kernels espectrales (kr_*, ki_*).\nRetorna un dict con conteo de tensores ruidosos y de parametros\nmodificados.", "kind": "function", "line": 46, "name": "inject_noise", "signature": "def inject_noise(model, sigma, seed)"}, {"doc": "Reconstruye TopoGPT2 alineado con el checkpoint, sin acceso a\nharness.ModelLoader (queremos un loader limpio que no comparta\nestado con corridas paralelas).", "kind": "function", "line": 74, "name": "load_model", "signature": "def load_model(ckpt_dir, ckpt_name, device)"}, {"kind": "function", "line": 99, "name": "generate_one", "signature": "def generate_one(model, tok, prompt, max_new_tokens, device)"}, {"kind": "function", "line": 117, "name": "main", "signature": "def main()"}]}, {"id": "eval/repair.py", "kind": "module", "label": "repair.py", "language": "py", "sha256": "826f80ea70d53790", "symbol_count": 6, "symbols": [{"kind": "function", "line": 36, "name": "_new_loader", "signature": "def _new_loader(ckpt_dir, ckpt_name)"}, {"kind": "function", "line": 49, "name": "extract_candidate", "signature": "def extract_candidate(prompt, completion)"}, {"kind": "function", "line": 75, "name": "run_test", "signature": "def run_test(problem, candidate_src)"}, {"kind": "function", "line": 89, "name": "build_repair_prompt", "signature": "def build_repair_prompt(prompt, candidate, err, entry_point)"}, {"kind": "function", "line": 104, "name": "gen", "signature": "def gen(model, tok, text, max_new_tokens, temperature, top_k, rep_penalty)"}, {"kind": "function", "line": 119, "name": "main", "signature": "def main()"}]}, {"id": "eval/report.py", "kind": "module", "label": "report.py", "language": "py", "sha256": "87956c8496bab9b5", "symbol_count": 6, "symbols": [{"kind": "function", "line": 25, "name": "pass_at_k", "signature": "def pass_at_k(n, c, k)"}, {"kind": "function", "line": 31, "name": "classify_error", "signature": "def classify_error(msg)"}, {"kind": "function", "line": 52, "name": "load_jsonl", "signature": "def load_jsonl(p)"}, {"kind": "function", "line": 56, "name": "summarize_run", "signature": "def summarize_run(p)"}, {"kind": "function", "line": 90, "name": "repair_summary", "signature": "def repair_summary(repair_path, baseline_path)"}, {"kind": "function", "line": 117, "name": "main", "signature": "def main()"}]}, {"id": "eval/samplers.py", "kind": "module", "label": "samplers.py", "language": "py", "sha256": "60f441ded1682d30", "symbol_count": 7, "symbols": [{"doc": "Decorator. Register a factory under `name`. If `enabled_env` is set,\nthe factory is only registered when that env var is truthy. This\nmirrors the `feature('XXX')` gating in claude-code-main/src/tools.ts.", "kind": "function", "line": 36, "name": "register_sampler", "signature": "def register_sampler(name)"}, {"kind": "function", "line": 55, "name": "_is_env_truthy", "signature": "def _is_env_truthy(name)"}, {"kind": "function", "line": 64, "name": "_make_standard", "signature": "def _make_standard(settings_kwargs)"}, {"kind": "function", "line": 69, "name": "_make_hrm", "signature": "def _make_hrm(settings_kwargs)"}, {"kind": "function", "line": 86, "name": "list_samplers", "signature": "def list_samplers()"}, {"doc": "Construct a sampler. Drop-in replacement for the old\n`make_sampler(mode, settings_kwargs)` in `eval.harness`.", "kind": "function", "line": 90, "name": "build_sampler", "signature": "def build_sampler(mode, settings_kwargs)"}, {"kind": "function", "line": 42, "name": "deco", "signature": "def deco(fn)"}]}, {"id": "eval/sandbox.py", "kind": "module", "label": "sandbox.py", "language": "py", "sha256": "bf933df740f00cef", "symbol_count": 9, "symbols": [{"doc": "One knob per defence layer. Defaults match HumanEval-style eval.", "kind": "class", "line": 53, "name": "SandboxConfig", "signature": "class SandboxConfig"}, {"doc": "Return the set of top-level names brought into scope by imports.", "kind": "method", "line": 100, "name": "_names_imported", "signature": "def _names_imported(tree)"}, {"doc": "Find Attribute nodes whose attr is in `blocked`. Returns attr names found.", "kind": "method", "line": 114, "name": "_blocked_dunder_access", "signature": "def _blocked_dunder_access(tree, blocked)"}, {"doc": "Compute max nesting depth of the AST. Catches obfuscated huge trees.", "kind": "method", "line": 123, "name": "_max_depth", "signature": "def _max_depth(tree)"}, {"doc": "Return (ok, reason). `reason` is \"\" when ok, else a human-readable\none-line explanation. Reasons are stable (used in test fixtures).", "kind": "method", "line": 133, "name": "check_safety", "signature": "def check_safety(source, cfg)"}, {"kind": "method", "line": 254, "name": "_build_worker_src", "signature": "def _build_worker_src(allowed_builtin_names, program_src, blocked_modules)"}, {"doc": "Execute `program_src` in a sandboxed child process. Returns the same\n5-tuple as `eval.harness.run_one_test` for drop-in compatibility.\n\nThe child is killed (SIGKILL) by the OS after `cfg.timeout` seconds.", "kind": "method", "line": 270, "name": "safe_exec", "signature": "def safe_exec(program_src, cfg, extra_globals)"}, {"kind": "method", "line": 373, "name": "describe_policy", "signature": "def describe_policy(cfg)"}, {"kind": "method", "line": 125, "name": "d", "signature": "def d(node, cur)"}]}, {"id": "eval/sandbox_smoke.py", "kind": "module", "label": "sandbox_smoke.py", "language": "py", "sha256": "89cee69fb565fbe9", "symbol_count": 1, "symbols": [{"kind": "function", "line": 15, "name": "main", "signature": "def main()"}]}, {"id": "eval/smoke.py", "kind": "module", "label": "smoke.py", "language": "py", "sha256": "94ee21110f91e4c2", "symbol_count": 2, "symbols": [{"kind": "function", "line": 17, "name": "run_standard", "signature": "def run_standard()"}, {"kind": "function", "line": 36, "name": "run_hrm", "signature": "def run_hrm()"}]}, {"id": "eval/temp_sweep.py", "kind": "module", "label": "temp_sweep.py", "language": "py", "sha256": "61dea99f11f6e36b", "symbol_count": 5, "symbols": [{"kind": "function", "line": 39, "name": "generate_one", "signature": "def generate_one(model, tok, prompt, max_new_tokens, temperature, top_k, device, seed_offset)"}, {"kind": "function", "line": 58, "name": "evaluate_problems", "signature": "def evaluate_problems(model, tok, problems, max_new_tokens, temperature, top_k, n_samples, device)"}, {"kind": "function", "line": 88, "name": "pass_at_k_unbiased", "signature": "def pass_at_k_unbiased(n, c, k)"}, {"kind": "function", "line": 96, "name": "summarize", "signature": "def summarize(results, n_samples)"}, {"kind": "function", "line": 116, "name": "main", "signature": "def main()"}]}, {"id": "gradio_app.py", "kind": "module", "label": "gradio_app.py", "language": "py", "sha256": "f8f1e1e9e50419e6", "symbol_count": 4, "symbols": [{"doc": "Return the path to the checkpoint directory, downloading if needed.", "kind": "function", "line": 35, "name": "ensure_checkpoint", "signature": "def ensure_checkpoint()"}, {"doc": "Run standard autoregressive inference.", "kind": "function", "line": 59, "name": "run_standard_inference", "signature": "def run_standard_inference(prompt, max_new_tokens, temperature, top_k, repetition_penalty, auto_continue)"}, {"doc": "Run hierarchical recursive reasoning inference.", "kind": "function", "line": 95, "name": "run_hrm_inference", "signature": "def run_hrm_inference(prompt, max_new_tokens, temperature, top_k, repetition_penalty, high_level_iters, low_level_iters, low_level_window, thinking, auto_continue)"}, {"doc": "Construct the Gradio Blocks interface.", "kind": "function", "line": 144, "name": "build_ui", "signature": "def build_ui()"}]}, {"id": "install.sh", "kind": "module", "label": "install.sh", "language": "sh", "sha256": "c907d80fd6734993", "symbol_count": 0, "symbols": []}, {"id": "synthetic_dataset.py", "kind": "module", "label": "synthetic_dataset.py", "language": "py", "sha256": "a91dbe7020222e8f", "symbol_count": 35, "symbols": [{"doc": "Abstract LLM backend. Subclass for each provider.", "kind": "class", "line": 61, "name": "LLMBackend", "signature": "class LLMBackend"}, {"doc": "Groq API backend using requests.\n\nSupports models: llama-3.3-70b-versatile, deepseek-r1.\nSet GROQ_API_KEY env var.", "kind": "class", "line": 71, "name": "GroqBackend", "signature": "class GroqBackend(LLMBackend)"}, {"doc": "OpenRouter unified API backend.\n\nSupports any OpenRouter model:\n    anthropic/claude-3.5-sonnet,\n    openai/gpt-4o,\n    deepseek/deepseek-chat,\n    google/gemini-2.0-flash-thinking,\nSet OPENROUTER_API_KEY env var.", "kind": "class", "line": 121, "name": "OpenRouterBackend", "signature": "class OpenRouterBackend(LLMBackend)"}, {"doc": "Ollama local inference backend.\n\nSupports any local model: llama3.1:8b, granite4.1:3b, etc.\nConnects to Ollama server at OLLAMA_HOST (default: http://localhost:11434).", "kind": "class", "line": 177, "name": "OllamaBackend", "signature": "class OllamaBackend(LLMBackend)"}, {"doc": "Factory for LLM backends.", "kind": "method", "line": 227, "name": "build_backend", "signature": "def build_backend(provider, model)"}, {"doc": "Validate that a generated sample meets quality bar.\n\nReturns (is_valid, reason).", "kind": "method", "line": 330, "name": "validate_sample", "signature": "def validate_sample(sample)"}, {"doc": "Tracks processed files for resumability.", "kind": "class", "line": 364, "name": "ProcessedManifest", "signature": "class ProcessedManifest"}, {"doc": "Generates synthetic instruction-tuning data from source files.\n\nPipeline (one LLM call per file):\n    file → MASTER_PROMPT → LLM → validate → dedup → JSONL\n\nFeatures:\n- Streaming JSONL writes (bounded RAM)\n- SHA256 dedup across corpus\n- Resumable (manifest tracks progress)\n- Threaded request batching for throughput\n- Configurable quality thresholds", "kind": "class", "line": 399, "name": "SyntheticDatasetGenerator", "signature": "class SyntheticDatasetGenerator"}, {"kind": "method", "line": 614, "name": "build_logger", "signature": "def build_logger(level)"}, {"kind": "method", "line": 625, "name": "parse_args", "signature": "def parse_args()"}, {"doc": "Load file paths from CLI args or file.", "kind": "method", "line": 652, "name": "load_paths", "signature": "def load_paths(paths_arg, paths_file, max_files)"}, {"kind": "method", "line": 667, "name": "main", "signature": "def main()"}, {"kind": "method", "line": 64, "name": "generate", "signature": "def generate(self, prompt)"}, {"kind": "method", "line": 67, "name": "name", "signature": "def name(self)"}, {"kind": "method", "line": 78, "name": "__init__", "signature": "def __init__(self, model, api_key, max_tokens, temperature, timeout)"}, {"kind": "method", "line": 95, "name": "name", "signature": "def name(self)"}, {"kind": "method", "line": 98, "name": "generate", "signature": "def generate(self, prompt)"}, {"kind": "method", "line": 132, "name": "__init__", "signature": "def __init__(self, model, api_key, max_tokens, temperature, timeout)"}, {"kind": "method", "line": 151, "name": "name", "signature": "def name(self)"}, {"kind": "method", "line": 154, "name": "generate", "signature": "def generate(self, prompt)"}, {"kind": "method", "line": 184, "name": "__init__", "signature": "def __init__(self, model, host, max_tokens, temperature, timeout)"}, {"kind": "method", "line": 198, "name": "name", "signature": "def name(self)"}, {"kind": "method", "line": 201, "name": "generate", "signature": "def generate(self, prompt)"}, {"kind": "method", "line": 374, "name": "load", "signature": "def load(path)"}, {"kind": "method", "line": 387, "name": "save", "signature": "def save(self, path)"}, {"kind": "method", "line": 418, "name": "__init__", "signature": "def __init__(self, backend, output_path, manifest_path, logger, max_workers, max_file_chars)"}, {"doc": "Background thread that drains the queue and writes JSONL lines.", "kind": "method", "line": 447, "name": "_jsonl_writer", "signature": "def _jsonl_writer(self)"}, {"kind": "method", "line": 465, "name": "_enqueue_sample", "signature": "def _enqueue_sample(self, sample)"}, {"kind": "method", "line": 468, "name": "_flush_writer", "signature": "def _flush_writer(self)"}, {"doc": "Read file content and detect language. Truncate if needed.", "kind": "method", "line": 477, "name": "_read_file", "signature": "def _read_file(self, path)"}, {"kind": "method", "line": 490, "name": "_build_prompt", "signature": "def _build_prompt(self, content, lang)"}, {"doc": "Call LLM with retry logic.", "kind": "method", "line": 496, "name": "_generate_sample", "signature": "def _generate_sample(self, content, lang)"}, {"doc": "Process a single file. Returns True if a sample was written.", "kind": "method", "line": 533, "name": "process_file", "signature": "def process_file(self, path)"}, {"doc": "Process a batch of files in parallel using thread pool.", "kind": "method", "line": 568, "name": "process_batch", "signature": "def process_batch(self, paths)"}, {"doc": "Signal end of processing and flush writer.", "kind": "method", "line": 590, "name": "finish", "signature": "def finish(self)"}]}, {"id": "tests/test_jlens.py", "kind": "module", "label": "test_jlens.py", "language": "py", "sha256": "3fd9fb4a583778eb", "symbol_count": 51, "symbols": [{"doc": "Feature: valid_position_mask excludes attention-sink and final positions.", "kind": "class", "line": 17, "name": "TestValidPositionMask", "signature": "class TestValidPositionMask"}, {"doc": "Feature: jacobian_for_prompt computes J_l for one prompt.", "kind": "class", "line": 52, "name": "TestJacobianForPrompt", "signature": "class TestJacobianForPrompt"}, {"doc": "Feature: fit() averages Jacobians over multiple prompts.", "kind": "class", "line": 172, "name": "TestFit", "signature": "class TestFit"}, {"doc": "Feature: JacobianLens saves, loads, applies, and merges.", "kind": "class", "line": 210, "name": "TestJacobianLens", "signature": "class TestJacobianLens"}, {"doc": "Feature: fit() with checkpoint resume works correctly.", "kind": "class", "line": 367, "name": "TestFitCheckpoint", "signature": "class TestFitCheckpoint"}, {"doc": "Feature: Config classes centralize all tunable parameters.", "kind": "class", "line": 473, "name": "TestConfig", "signature": "class TestConfig"}, {"doc": "Feature: Application config controls readout behavior.", "kind": "class", "line": 494, "name": "TestTopoGPT3JLensAppConfig", "signature": "class TestTopoGPT3JLensAppConfig"}, {"doc": "Scenario: Correct mask for a standard-length prompt.", "kind": "method", "line": 20, "name": "test_basic_mask", "signature": "def test_basic_mask(self)"}, {"doc": "Scenario: Too-short prompt raises ValueError.", "kind": "method", "line": 29, "name": "test_too_short_raises", "signature": "def test_too_short_raises(self)"}, {"doc": "Scenario: Negative skip_first raises ValueError.", "kind": "method", "line": 34, "name": "test_negative_skip_raises", "signature": "def test_negative_skip_raises(self)"}, {"doc": "Scenario: skip_first=0 includes all but final position.", "kind": "method", "line": 39, "name": "test_all_positions_valid", "signature": "def test_all_positions_valid(self)"}, {"doc": "Scenario: Exact minimum length (skip_first + 2) works.", "kind": "method", "line": 45, "name": "test_exact_minimum_length", "signature": "def test_exact_minimum_length(self)"}, {"kind": "method", "line": 56, "name": "model", "signature": "def model(self)"}, {"doc": "Scenario: Returns Jacobians for all requested source layers.", "kind": "method", "line": 63, "name": "test_returns_jacobians_for_source_layers", "signature": "def test_returns_jacobians_for_source_layers(self, model)"}, {"doc": "Scenario: J_{n_layers-2} has diag ~= 1 (identity property).", "kind": "method", "line": 76, "name": "test_late_layer_jacobian_close_to_identity", "signature": "def test_late_layer_jacobian_close_to_identity(self, model)"}, {"doc": "Scenario: Earlier layers compound deviations from identity.", "kind": "method", "line": 85, "name": "test_earlier_layers_further_from_identity", "signature": "def test_earlier_layers_further_from_identity(self, model)"}, {"doc": "Scenario: J_{n_layers-2} equals I + W_{last} exactly.\n\nFor TinyDecoder with block = h + 0.1*W*h, J_{n_layers-2} = I + W.", "kind": "method", "line": 95, "name": "test_exact_jacobian_for_last_block", "signature": "def test_exact_jacobian_for_last_block(self, model)"}, {"doc": "Scenario: Negative layer indices are normalized correctly.", "kind": "method", "line": 110, "name": "test_negative_layer_indices", "signature": "def test_negative_layer_indices(self, model)"}, {"doc": "Scenario: Out-of-range layers raise ValueError.", "kind": "method", "line": 133, "name": "test_out_of_range_layers_rejected", "signature": "def test_out_of_range_layers_rejected(self, model)"}, {"doc": "Scenario: source_layers must be below target_layer.", "kind": "method", "line": 145, "name": "test_source_below_target_enforced", "signature": "def test_source_below_target_enforced(self, model)"}, {"doc": "Scenario: target_layer out of range raises ValueError.", "kind": "method", "line": 158, "name": "test_target_out_of_range_raises", "signature": "def test_target_out_of_range_raises(self, model)"}, {"kind": "method", "line": 176, "name": "model", "signature": "def model(self)"}, {"doc": "Scenario: fit() returns JacobianLens with correct metadata.", "kind": "method", "line": 183, "name": "test_fit_returns_lens_with_correct_attributes", "signature": "def test_fit_returns_lens_with_correct_attributes(self, model)"}, {"doc": "Scenario: No valid prompts raises ValueError.", "kind": "method", "line": 191, "name": "test_fit_empty_prompts_raises", "signature": "def test_fit_empty_prompts_raises(self, model)"}, {"doc": "Scenario: Too-short prompts are skipped.", "kind": "method", "line": 196, "name": "test_fit_skips_short_prompts", "signature": "def test_fit_skips_short_prompts(self, model)"}, {"doc": "Scenario: Default source_layers covers all layers below target.", "kind": "method", "line": 202, "name": "test_fit_with_default_source_layers", "signature": "def test_fit_with_default_source_layers(self, model)"}, {"kind": "method", "line": 214, "name": "model", "signature": "def model(self)"}, {"kind": "method", "line": 222, "name": "fitted_lens", "signature": "def fitted_lens(self, model)"}, {"doc": "Scenario: save/load preserves jacobians (fp16 tolerance).", "kind": "method", "line": 226, "name": "test_save_and_load_round_trip", "signature": "def test_save_and_load_round_trip(self, fitted_lens, tmp_path)"}, {"doc": "Scenario: apply() returns correct logit shapes.", "kind": "method", "line": 242, "name": "test_apply_returns_correct_shapes", "signature": "def test_apply_returns_correct_shapes(self, fitted_lens, model)"}, {"doc": "Scenario: Transported late-layer logits match model logits.", "kind": "method", "line": 254, "name": "test_fitted_late_layer_matches_model", "signature": "def test_fitted_late_layer_matches_model(self, fitted_lens, model)"}, {"doc": "Scenario: Explicit positions return correct subset.", "kind": "method", "line": 263, "name": "test_apply_with_explicit_positions", "signature": "def test_apply_with_explicit_positions(self, fitted_lens, model)"}, {"doc": "Scenario: use_jacobian=False returns untransported logits.", "kind": "method", "line": 274, "name": "test_logit_lens_baseline", "signature": "def test_logit_lens_baseline(self, fitted_lens, model)"}, {"doc": "Scenario: Unfitted layer raises ValueError.", "kind": "method", "line": 281, "name": "test_unfitted_layer_rejected", "signature": "def test_unfitted_layer_rejected(self, fitted_lens, model)"}, {"doc": "Scenario: Out-of-range layer raises ValueError.", "kind": "method", "line": 286, "name": "test_out_of_range_layer_rejected", "signature": "def test_out_of_range_layer_rejected(self, fitted_lens, model)"}, {"doc": "Scenario: merge() computes n_prompts-weighted mean.", "kind": "method", "line": 291, "name": "test_merge_weighted_mean", "signature": "def test_merge_weighted_mean(self)"}, {"doc": "Scenario: Mismatched lenses raise ValueError.", "kind": "method", "line": 319, "name": "test_merge_mismatch_raises", "signature": "def test_merge_mismatch_raises(self)"}, {"doc": "Scenario: Empty merge raises ValueError.", "kind": "method", "line": 326, "name": "test_merge_empty_raises", "signature": "def test_merge_empty_raises(self)"}, {"doc": "Scenario: transport() maps residual to final-layer basis.", "kind": "method", "line": 331, "name": "test_transport_produces_correct_shape", "signature": "def test_transport_produces_correct_shape(self, fitted_lens)"}, {"doc": "Scenario: Loading non-lens file raises ValueError.", "kind": "method", "line": 337, "name": "test_load_invalid_file_raises", "signature": "def test_load_invalid_file_raises(self, tmp_path)"}, {"doc": "Scenario: from_pretrained resolves a local file.", "kind": "method", "line": 344, "name": "test_from_pretrained_local_file", "signature": "def test_from_pretrained_local_file(self, fitted_lens, tmp_path)"}, {"doc": "Scenario: from_pretrained resolves a local directory.", "kind": "method", "line": 351, "name": "test_from_pretrained_local_directory", "signature": "def test_from_pretrained_local_directory(self, fitted_lens, tmp_path)"}, {"doc": "Scenario: repr contains key metadata.", "kind": "method", "line": 359, "name": "test_repr", "signature": "def test_repr(self, fitted_lens)"}, {"kind": "method", "line": 371, "name": "model", "signature": "def model(self)"}, {"doc": "Scenario: Resumed fit matches fresh fit.", "kind": "method", "line": 378, "name": "test_checkpoint_resume_produces_same_result", "signature": "def test_checkpoint_resume_produces_same_result(self, model, tmp_path)"}, {"doc": "Scenario: Resume after a skipped prompt does not double-count.\n\nRegression: a skipped prompt must not desync success-count from\nlist-position.", "kind": "method", "line": 408, "name": "test_resume_after_skip_no_double_count", "signature": "def test_resume_after_skip_no_double_count(self, model, tmp_path)"}, {"doc": "Scenario: Mismatched checkpoint settings raise ValueError.", "kind": "method", "line": 450, "name": "test_checkpoint_mismatch_raises", "signature": "def test_checkpoint_mismatch_raises(self, model, tmp_path)"}, {"doc": "Scenario: Default fit config has sensible defaults.", "kind": "method", "line": 476, "name": "test_fit_config_defaults", "signature": "def test_fit_config_defaults(self)"}, {"doc": "Scenario: Default app config has sensible defaults.", "kind": "method", "line": 485, "name": "test_app_config_defaults", "signature": "def test_app_config_defaults(self)"}, {"doc": "Scenario: Default app config uses all positions.", "kind": "method", "line": 497, "name": "test_default_config", "signature": "def test_default_config(self)"}, {"doc": "Scenario: Custom app config overrides specific layers.", "kind": "method", "line": 505, "name": "test_custom_config", "signature": "def test_custom_config(self)"}]}, {"id": "tests/test_lens_model.py", "kind": "module", "label": "test_lens_model.py", "language": "py", "sha256": "479f36e827cda9ce", "symbol_count": 34, "symbols": [{"doc": "Feature: TopoGPT3LensConfig provides centralized adapter configuration.", "kind": "class", "line": 13, "name": "TestTopoGPT3LensConfig", "signature": "class TestTopoGPT3LensConfig"}, {"doc": "Feature: TinyDecoder provides a minimal test model.", "kind": "class", "line": 41, "name": "TestTinyDecoder", "signature": "class TestTinyDecoder"}, {"doc": "Feature: TopoGPT3LensModel wraps a model to implement LensModel protocol.", "kind": "class", "line": 65, "name": "TestTopoGPT3LensModel", "signature": "class TestTopoGPT3LensModel"}, {"doc": "Feature: ActivationRecorder works with TopoGPT3LensModel.", "kind": "class", "line": 214, "name": "TestTopoGPT3LensModelWithRecording", "signature": "class TestTopoGPT3LensModelWithRecording"}, {"doc": "Feature: Edge cases are handled gracefully.", "kind": "class", "line": 278, "name": "TestTopoGPT3LensModelEdgeCases", "signature": "class TestTopoGPT3LensModelEdgeCases"}, {"doc": "Scenario: Default config matches small scale preset.", "kind": "method", "line": 16, "name": "test_default_config", "signature": "def test_default_config(self)"}, {"doc": "Scenario: Build lens config from TopoGPT2Config.", "kind": "method", "line": 25, "name": "test_from_topogpt2_config", "signature": "def test_from_topogpt2_config(self)"}, {"doc": "Scenario: Missing state.json raises FileNotFoundError.", "kind": "method", "line": 35, "name": "test_probe_checkpoint_missing_raises", "signature": "def test_probe_checkpoint_missing_raises(self, tmp_path)"}, {"doc": "Scenario: TinyDecoder has correct default shape.", "kind": "method", "line": 44, "name": "test_default_parameters", "signature": "def test_default_parameters(self)"}, {"doc": "Scenario: Forward pass produces correct logit shape.", "kind": "method", "line": 51, "name": "test_forward_output_shape", "signature": "def test_forward_output_shape(self)"}, {"doc": "Scenario: Embedding and LM head share weights.", "kind": "method", "line": 59, "name": "test_weight_tied", "signature": "def test_weight_tied(self)"}, {"kind": "method", "line": 69, "name": "raw_model", "signature": "def raw_model(self)"}, {"kind": "method", "line": 77, "name": "lens_model", "signature": "def lens_model(self, raw_model)"}, {"doc": "Scenario: LensModel attributes match underlying model.", "kind": "method", "line": 80, "name": "test_exposes_protocol_attributes", "signature": "def test_exposes_protocol_attributes(self, lens_model, raw_model)"}, {"doc": "Scenario: encode() returns tensor of shape [1, seq_len].", "kind": "method", "line": 87, "name": "test_encode_text_to_token_ids", "signature": "def test_encode_text_to_token_ids(self, lens_model)"}, {"doc": "Scenario: encode() uses BPETokenizer when available.", "kind": "method", "line": 95, "name": "test_encode_with_tokenizer", "signature": "def test_encode_with_tokenizer(self)"}, {"doc": "Scenario: encode() truncates at max_length.", "kind": "method", "line": 107, "name": "test_encode_respects_max_length", "signature": "def test_encode_respects_max_length(self, lens_model)"}, {"doc": "Scenario: forward() returns hidden states with d_model dim, not vocab.\n\nThe lens model forward should stop before final_norm and lm_head.\nThe output should have d_model as last dimension, not vocab_size.", "kind": "method", "line": 113, "name": "test_forward_returns_residual_only", "signature": "def test_forward_returns_residual_only(self)"}, {"doc": "Scenario: Residual forward shape differs from full model logits.", "kind": "method", "line": 128, "name": "test_forward_differs_from_full_model", "signature": "def test_forward_differs_from_full_model(self)"}, {"doc": "Scenario: unembed() maps residual to logits.", "kind": "method", "line": 141, "name": "test_unembed_produces_logits", "signature": "def test_unembed_produces_logits(self, lens_model)"}, {"doc": "Scenario: residual forward + unembed == model forward logits.\n\nThis validates that our split forward matches the original model's\nfull forward pass.", "kind": "method", "line": 150, "name": "test_forward_plus_unembed_matches_model_logits", "signature": "def test_forward_plus_unembed_matches_model_logits(self, lens_model, raw_model)"}, {"doc": "Scenario: Gradient flows through residual layers when grads enabled.", "kind": "method", "line": 163, "name": "test_autograd_graph_tracks_through_layers", "signature": "def test_autograd_graph_tracks_through_layers(self)"}, {"doc": "Scenario: input_device returns the embedding weight device.", "kind": "method", "line": 180, "name": "test_input_device_property", "signature": "def test_input_device_property(self, lens_model)"}, {"doc": "Scenario: input_device can be overridden.", "kind": "method", "line": 185, "name": "test_input_device_setter", "signature": "def test_input_device_setter(self, lens_model)"}, {"doc": "Scenario: tokenizer can be set after construction.", "kind": "method", "line": 191, "name": "test_tokenizer_setter", "signature": "def test_tokenizer_setter(self, lens_model)"}, {"doc": "Scenario: from_checkpoint with missing directory raises.", "kind": "method", "line": 198, "name": "test_from_checkpoint_missing_raises", "signature": "def test_from_checkpoint_missing_raises(self)"}, {"doc": "Scenario: Multiple forward passes with same input are deterministic.", "kind": "method", "line": 205, "name": "test_grad_enabled_deterministic", "signature": "def test_grad_enabled_deterministic(self, lens_model)"}, {"kind": "method", "line": 218, "name": "lens_model", "signature": "def lens_model(self)"}, {"doc": "Scenario: ActivationRecorder captures all requested layer outputs.", "kind": "method", "line": 225, "name": "test_recorder_captures_layer_outputs", "signature": "def test_recorder_captures_layer_outputs(self, lens_model)"}, {"doc": "Scenario: start_graph_at roots the autograd graph.", "kind": "method", "line": 238, "name": "test_recorder_with_start_graph_at", "signature": "def test_recorder_with_start_graph_at(self, lens_model)"}, {"doc": "Scenario: Hooks are removed even if construction fails.", "kind": "method", "line": 252, "name": "test_recorder_cleanup_on_exception", "signature": "def test_recorder_cleanup_on_exception(self, lens_model)"}, {"doc": "Scenario: Activations can be detached after recorder exits.", "kind": "method", "line": 264, "name": "test_recorder_detach_after_forward", "signature": "def test_recorder_detach_after_forward(self, lens_model)"}, {"doc": "Scenario: Empty input produces error or minimal output.", "kind": "method", "line": 281, "name": "test_empty_sequence", "signature": "def test_empty_sequence(self)"}, {"doc": "Scenario: Single token input works.", "kind": "method", "line": 291, "name": "test_single_token", "signature": "def test_single_token(self)"}]}, {"id": "topogpt3/__init__.py", "kind": "module", "label": "__init__.py", "language": "py", "sha256": "f0c0693661707d14", "symbol_count": 0, "symbols": []}, {"id": "topogpt3/__main__.py", "kind": "module", "label": "__main__.py", "language": "py", "sha256": "1019f2b8207d812f", "symbol_count": 1, "symbols": [{"doc": "TopoGPT3 entry point. Delegates to subcommands.", "kind": "function", "line": 6, "name": "main", "signature": "def main()"}]}, {"id": "topogpt3/api_server.py", "kind": "module", "label": "api_server.py", "language": "py", "sha256": "9e0b94fefed45b89", "symbol_count": 46, "symbols": [{"kind": "function", "line": 116, "name": "_setup_logging", "signature": "def _setup_logging(verbose)"}, {"kind": "class", "line": 137, "name": "ApiKey", "signature": "class ApiKey"}, {"kind": "class", "line": 143, "name": "AuthState", "signature": "class AuthState"}, {"doc": "Accept ``key1,admin:key2,key3``. The ``admin:`` prefix marks an\nadmin-level key; everything else is a regular user key.", "kind": "method", "line": 164, "name": "_parse_keys", "signature": "def _parse_keys(raw)"}, {"kind": "method", "line": 192, "name": "_sha256", "signature": "def _sha256(raw)"}, {"kind": "class", "line": 202, "name": "TokenBucket", "signature": "class TokenBucket"}, {"kind": "class", "line": 219, "name": "RateLimiter", "signature": "class RateLimiter"}, {"kind": "class", "line": 250, "name": "IpBanner", "signature": "class IpBanner"}, {"kind": "method", "line": 281, "name": "_sanitize_stop", "signature": "def _sanitize_stop(stop)"}, {"kind": "class", "line": 291, "name": "CompletionRequest", "signature": "class CompletionRequest(BaseModel)"}, {"kind": "class", "line": 310, "name": "Message", "signature": "class Message(BaseModel)"}, {"kind": "class", "line": 316, "name": "ChatCompletionRequest", "signature": "class ChatCompletionRequest(BaseModel)"}, {"kind": "class", "line": 341, "name": "ServerModel", "signature": "class ServerModel"}, {"kind": "method", "line": 499, "name": "_resolve_device", "signature": "def _resolve_device(device)"}, {"kind": "method", "line": 505, "name": "_probe_n_kv", "signature": "def _probe_n_kv(checkpoint_dir)"}, {"kind": "method", "line": 513, "name": "load_model", "signature": "def load_model(checkpoint, device)"}, {"kind": "method", "line": 534, "name": "lifespan", "signature": "def lifespan(app)"}, {"doc": "Global middleware: rate-limit, IP-ban, security headers, audit log.", "kind": "method", "line": 574, "name": "_security_middleware", "signature": "def _security_middleware(request, call_next)"}, {"doc": "Best-effort real client IP. We trust no proxy headers by default.", "kind": "method", "line": 602, "name": "_real_ip", "signature": "def _real_ip(request)"}, {"kind": "method", "line": 613, "name": "_json_error", "signature": "def _json_error(status, detail)"}, {"doc": "FastAPI dependency: extract & validate Bearer token.", "kind": "method", "line": 625, "name": "_authenticate", "signature": "def _authenticate(request)"}, {"doc": "Rate limit per-key (with admin exemption / higher limit).", "kind": "method", "line": 643, "name": "_check_rate_limit", "signature": "def _check_rate_limit(api_key, request)"}, {"kind": "method", "line": 661, "name": "health", "signature": "def health(request)"}, {"kind": "method", "line": 668, "name": "list_models", "signature": "def list_models(request)"}, {"kind": "method", "line": 685, "name": "completions", "signature": "def completions(req, request)"}, {"kind": "method", "line": 741, "name": "chat_completions", "signature": "def chat_completions(req, request)"}, {"kind": "method", "line": 799, "name": "_check_model", "signature": "def _check_model()"}, {"kind": "method", "line": 804, "name": "_short_id", "signature": "def _short_id()"}, {"kind": "method", "line": 808, "name": "_build_chat_prompt", "signature": "def _build_chat_prompt(messages)"}, {"kind": "method", "line": 815, "name": "_extract_text", "signature": "def _extract_text(content)"}, {"kind": "method", "line": 829, "name": "_stream_completion", "signature": "def _stream_completion(prompt, max_tokens, temperature, top_k, repetition_penalty, stop, auto_continue, max_continuations)"}, {"kind": "method", "line": 864, "name": "_stream_chat", "signature": "def _stream_chat(t0_ms, prompt, max_tokens, temperature, top_k, repetition_penalty, stop, auto_continue, max_continuations)"}, {"kind": "method", "line": 902, "name": "main", "signature": "def main()"}, {"kind": "method", "line": 148, "name": "validate", "signature": "def validate(self, raw)"}, {"kind": "method", "line": 208, "name": "consume", "signature": "def consume(self, n)"}, {"kind": "method", "line": 220, "name": "__init__", "signature": "def __init__(self, user_rps, admin_rps, capacity)"}, {"kind": "method", "line": 227, "name": "_cleanup", "signature": "def _cleanup(self)"}, {"kind": "method", "line": 233, "name": "allow", "signature": "def allow(self, key, role)"}, {"kind": "method", "line": 251, "name": "__init__", "signature": "def __init__(self, max_failures, window)"}, {"kind": "method", "line": 257, "name": "record_failure", "signature": "def record_failure(self, ip)"}, {"kind": "method", "line": 265, "name": "is_banned", "signature": "def is_banned(self, ip)"}, {"kind": "method", "line": 306, "name": "_normalize_stop", "signature": "def _normalize_stop(cls, v)"}, {"kind": "method", "line": 331, "name": "_normalize_stop", "signature": "def _normalize_stop(cls, v)"}, {"kind": "method", "line": 348, "name": "complete", "signature": "def complete(self, prompt)"}, {"kind": "method", "line": 393, "name": "stream_complete", "signature": "def stream_complete(self, prompt)"}, {"kind": "method", "line": 482, "name": "_is_eos", "signature": "def _is_eos(self, token_id)"}]}, {"id": "topogpt3/continuation.py", "kind": "module", "label": "continuation.py", "language": "py", "sha256": "9d0c4e1576ec926a", "symbol_count": 5, "symbols": [{"kind": "function", "line": 25, "name": "_count_unclosed_brackets", "signature": "def _count_unclosed_brackets(text)"}, {"kind": "function", "line": 36, "name": "_count_unclosed_fences", "signature": "def _count_unclosed_fences(text)"}, {"doc": "Heuristic to decide whether a model response looks finished.\n\nReturns True when the response seems naturally complete (no need to\ncontinue), False when it appears truncated and continuation may help.", "kind": "function", "line": 45, "name": "is_response_complete", "signature": "def is_response_complete(text, min_chars)"}, {"doc": "Return the last N lines (or up to tail_chars) of `text` as a\ncontinuation prefix to feed back into the model.\n\nThe returned string can be prepended as context for the model's next\ngeneration call so it continues naturally from that point.", "kind": "function", "line": 75, "name": "extract_tail_for_continuation", "signature": "def extract_tail_for_continuation(text, tail_lines, tail_chars)"}, {"doc": "Split `text` at the last newline.\n\nReturns (prefix_without_last_line, last_line).\nUseful for discarding a trailing incomplete line before continuation.", "kind": "function", "line": 105, "name": "split_at_last_newline", "signature": "def split_at_last_newline(text)"}]}, {"id": "topogpt3/inference.py", "kind": "module", "label": "inference.py", "language": "py", "sha256": "1de9afb5a96dab29", "symbol_count": 54, "symbols": [{"doc": "Immutable architecture preset for a named model scale.", "kind": "class", "line": 32, "name": "ScalePreset", "signature": "class ScalePreset"}, {"doc": "Centralized configuration container for the inference pipeline.\n\nEvery value consumed downstream resides here. Adding a new tunable means\nextending this class; no other module should embed literals.", "kind": "class", "line": 42, "name": "InferenceSettings", "signature": "class InferenceSettings"}, {"doc": "Builds a stdout-attached logger from inference settings.", "kind": "class", "line": 158, "name": "InferenceLoggerFactory", "signature": "class InferenceLoggerFactory"}, {"doc": "Resolves filesystem paths while rejecting traversal outside their root.", "kind": "class", "line": 178, "name": "SecurePathResolver", "signature": "class SecurePathResolver"}, {"doc": "Resolves the TopoGPT3 runtime module via the package import system.", "kind": "class", "line": 212, "name": "SourceModuleLoader", "signature": "class SourceModuleLoader"}, {"doc": "Computes and validates checkpoint file paths under a single root.", "kind": "class", "line": 228, "name": "CheckpointPaths", "signature": "class CheckpointPaths"}, {"doc": "Reads tensor metadata from safetensors to infer architecture details.", "kind": "class", "line": 274, "name": "WeightShapeProbe", "signature": "class WeightShapeProbe"}, {"doc": "Builds a TopoGPT2Config matching the loaded checkpoint and tokenizer.", "kind": "class", "line": 318, "name": "TopoGPT2ConfigAligner", "signature": "class TopoGPT2ConfigAligner"}, {"doc": "Builds a BPETokenizer instance using the configured encoding.", "kind": "class", "line": 349, "name": "TokenizerFactory", "signature": "class TokenizerFactory"}, {"doc": "Applies the idempotent Gauss complex-multiply patch when enabled.", "kind": "class", "line": 362, "name": "GaussPatchApplier", "signature": "class GaussPatchApplier"}, {"doc": "Instantiates the model and loads weights from safetensors.", "kind": "class", "line": 380, "name": "ModelAssembler", "signature": "class ModelAssembler"}, {"doc": "Applies deterministic seeds across torch, CUDA and the model package.", "kind": "class", "line": 417, "name": "SeedSynchronizer", "signature": "class SeedSynchronizer"}, {"doc": "Immutable sampling parameters consumed by the generation engine.", "kind": "class", "line": 441, "name": "SamplingPolicy", "signature": "class SamplingPolicy"}, {"doc": "Quantitative summary of a single generation call.", "kind": "class", "line": 461, "name": "GenerationReport", "signature": "class GenerationReport"}, {"doc": "Runs autoregressive sampling against a loaded model and tokenizer.", "kind": "class", "line": 475, "name": "GenerationEngine", "signature": "class GenerationEngine"}, {"doc": "Prints a GenerationReport to stdout using settings-defined formatting.", "kind": "class", "line": 533, "name": "ResultRenderer", "signature": "class ResultRenderer"}, {"doc": "Orchestrator wiring loader, builder, engine and renderer.", "kind": "class", "line": 562, "name": "InferencePipeline", "signature": "class InferencePipeline"}, {"doc": "Translates command-line arguments into an InferenceSettings instance.", "kind": "class", "line": 615, "name": "CliArgumentParser", "signature": "class CliArgumentParser"}, {"doc": "CLI entry point. Returns a process exit code.", "kind": "method", "line": 721, "name": "main", "signature": "def main(argv)"}, {"doc": "Return the architecture preset table indexed by scale name.", "kind": "method", "line": 103, "name": "scale_presets", "signature": "def scale_presets()"}, {"doc": "Return the resolved preset for the configured model scale.", "kind": "method", "line": 116, "name": "preset", "signature": "def preset(self)"}, {"doc": "Raise ValueError if any setting falls outside its safety bounds.", "kind": "method", "line": 126, "name": "validate", "signature": "def validate(self)"}, {"doc": "Return a configured Logger with a single deduplicated stdout handler.", "kind": "method", "line": 162, "name": "build", "signature": "def build(settings)"}, {"doc": "Join `parts` under `root` and return the canonical resolved path.\n\nRaises ValueError if the resolved path escapes `root`.", "kind": "method", "line": 182, "name": "resolve_under", "signature": "def resolve_under(root)"}, {"doc": "Validate `path` points to an existing regular file with the expected suffix.", "kind": "method", "line": 198, "name": "require_existing_file", "signature": "def require_existing_file(path, expected_suffix)"}, {"kind": "method", "line": 215, "name": "__init__", "signature": "def __init__(self, settings, logger)"}, {"doc": "Return the topogpt3.train module which re-exports model symbols.", "kind": "method", "line": 219, "name": "load", "signature": "def load(self)"}, {"kind": "method", "line": 231, "name": "__init__", "signature": "def __init__(self, settings)"}, {"doc": "Directory holding the active checkpoint slot.", "kind": "method", "line": 239, "name": "slot_dir", "signature": "def slot_dir(self)"}, {"doc": "Resolved path to the safetensors weights file inside the slot.", "kind": "method", "line": 243, "name": "model_file", "signature": "def model_file(self)"}, {"doc": "Resolved path to the JSON training-state file inside the slot.", "kind": "method", "line": 249, "name": "state_file", "signature": "def state_file(self)"}, {"doc": "Verify weights exist and the on-disk size lies within safety bounds.", "kind": "method", "line": 255, "name": "assert_ready", "signature": "def assert_ready(self)"}, {"kind": "method", "line": 277, "name": "__init__", "signature": "def __init__(self, settings, logger)"}, {"doc": "Recover N_KV_HEADS used at training by inspecting the k_proj shape.\n\nReturns None when the probe key is absent, signalling the caller to\nfall back to scale defaults rather than guess.", "kind": "method", "line": 281, "name": "detect_n_kv_heads", "signature": "def detect_n_kv_heads(self, weights_path, d_model, n_heads)"}, {"kind": "method", "line": 321, "name": "__init__", "signature": "def __init__(self, settings, source_module, logger)"}, {"doc": "Return a TopoGPT2Config dataclass ready to instantiate the model.", "kind": "method", "line": 327, "name": "build", "signature": "def build(self, n_kv_heads, vocab_size)"}, {"kind": "method", "line": 352, "name": "__init__", "signature": "def __init__(self, settings, source_module)"}, {"doc": "Return an instance of BPETokenizer bound to the configured encoding.", "kind": "method", "line": 356, "name": "build", "signature": "def build(self)"}, {"kind": "method", "line": 365, "name": "__init__", "signature": "def __init__(self, settings, source_module, logger)"}, {"doc": "Patch QuaternionSpectralLayer to use the 3-multiply Gauss contract.", "kind": "method", "line": 371, "name": "apply_if_enabled", "signature": "def apply_if_enabled(self)"}, {"kind": "method", "line": 383, "name": "__init__", "signature": "def __init__(self, settings, source_module, logger)"}, {"doc": "Build the TopoGPT2 graph, load weights into it, and return it in eval mode.", "kind": "method", "line": 389, "name": "assemble", "signature": "def assemble(self, aligned_cfg, paths)"}, {"kind": "method", "line": 420, "name": "__init__", "signature": "def __init__(self, settings, source_module, logger)"}, {"doc": "Seed all relevant RNGs using the model package helper when available.", "kind": "method", "line": 426, "name": "apply", "signature": "def apply(self)"}, {"doc": "Construct a SamplingPolicy from inference settings.", "kind": "method", "line": 450, "name": "from_settings", "signature": "def from_settings(cls, settings)"}, {"doc": "Return throughput in tokens/sec, clamped to avoid divide-by-zero.", "kind": "method", "line": 470, "name": "tokens_per_second", "signature": "def tokens_per_second(self, elapsed_floor)"}, {"kind": "method", "line": 478, "name": "__init__", "signature": "def __init__(self, settings, logger)"}, {"doc": "Generate a completion for `prompt` and return a GenerationReport.", "kind": "method", "line": 483, "name": "run", "signature": "def run(self, model, tokenizer, prompt, policy)"}, {"kind": "method", "line": 536, "name": "__init__", "signature": "def __init__(self, settings, logger)"}, {"doc": "Emit a banner with prompt and completion, plus a throughput log line.", "kind": "method", "line": 540, "name": "render", "signature": "def render(self, report)"}, {"kind": "method", "line": 565, "name": "__init__", "signature": "def __init__(self, settings, logger)"}, {"doc": "Run the full inference pipeline end-to-end and return the report.", "kind": "method", "line": 571, "name": "execute", "signature": "def execute(self)"}, {"doc": "Return the configured argparse.ArgumentParser.", "kind": "method", "line": 619, "name": "build_parser", "signature": "def build_parser()"}, {"doc": "Parse `argv` (or sys.argv) and return a populated InferenceSettings.", "kind": "method", "line": 698, "name": "parse", "signature": "def parse(argv)"}]}, {"id": "topogpt3/inference_hrm.py", "kind": "module", "label": "inference_hrm.py", "language": "py", "sha256": "a037ba082478370d", "symbol_count": 76, "symbols": [{"doc": "Immutable architecture preset for a named model scale.", "kind": "class", "line": 54, "name": "ScalePreset", "signature": "class ScalePreset"}, {"doc": "Hyperparameters governing the hierarchical recursive thinking loop.\n\nThe semantics follow the HRM and GRAM literature, adapted to operate\nsafely with zero additional learnable parameters on a model that was\nnot trained with recurrence in its computational graph. The reasoner\nperforms damped fixed-point iteration entirely in the residual-stream\nspace produced by the baseline forward pass; deep activations are never\nfed back into the token-embedding-input layers, preserving the trained\nactivation distribution at every layer boundary.\n\nAttributes:\n    enabled: master switch; when False the pipeline degrades to the\n        standard non-recursive autoregressive loop.\n    max_high_level_iters: maximum slow-loop iterations per emitted token.\n        Each iteration applies a deeper trailing window of layers.\n    max_low_level_iters: maximum fast-loop iterations per high-level step.\n        Each iteration applies the short trailing window of layers.\n    low_level_window: number of trailing transformer layers iterated by\n        the low-level fast loop.\n    high_level_window: number of trailing transformer layers iterated by\n        the high-level slow loop. Should be greater than or equal to\n        low_level_window so the hierarchy matches the HRM coarse/fine\n        split.\n    low_level_step: damping coefficient in [0, 1] for the low-level\n        update rule z <- z + step * (window(z) - z).\n    high_level_step: damping coefficient for the high-level update.\n    attractor_low_epsilon: relative L2 change threshold that declares the\n        low-level state converged.\n    attractor_high_epsilon: relative L2 change threshold that declares the\n        high-level state converged.\n    high_level_persist_tokens: tokens during which the refinement vector\n        is reused as a warm start before being re-initialized to zero.\n        This is the sparse temporal-memory dimension.\n    cache_warm_start_weight: scalar in [0, 1] applied to the cached\n        refinement before warm-starting the next token's iteration.\n    max_drift_relative: relative L2 distance ceiling between the iterated\n        latent and the baseline latent; exceeding it triggers a reset to\n        the baseline state and aborts thinking for the current token.\n    latent_change_eps: floor used in the denominator of relative change\n        computations to avoid division by zero.\n    safety_max_total_iterations: hard cap on total layer invocations per\n        emitted token regardless of configured iters.\n    minimum_low_level_iters: floor on low-level iterations before\n        convergence checks may halt the loop.\n    minimum_high_level_iters: floor on high-level iterations before\n        convergence checks may halt the loop.\n    diagnostic_logging: when True, emits per-token iteration statistics.", "kind": "class", "line": 64, "name": "RecursiveReasoningConfig", "signature": "class RecursiveReasoningConfig"}, {"doc": "Centralized configuration for the TopoGPT3.1 inference pipeline.\n\nEvery value consumed downstream resides here. Extending the pipeline with\na new tunable means extending this dataclass; no other module should\nembed literals.", "kind": "class", "line": 134, "name": "HRMInferenceSettings", "signature": "class HRMInferenceSettings"}, {"doc": "Builds a stdout-attached logger from inference settings.", "kind": "class", "line": 343, "name": "HRMLoggerFactory", "signature": "class HRMLoggerFactory"}, {"doc": "Resolves filesystem paths while rejecting traversal outside their root.", "kind": "class", "line": 363, "name": "SecurePathResolver", "signature": "class SecurePathResolver"}, {"doc": "Resolves the TopoGPT3 runtime module via the package import system.", "kind": "class", "line": 397, "name": "SourceModuleLoader", "signature": "class SourceModuleLoader"}, {"doc": "Computes and validates checkpoint file paths under a single root.", "kind": "class", "line": 413, "name": "CheckpointPaths", "signature": "class CheckpointPaths"}, {"doc": "Reads tensor metadata from safetensors to infer architecture details.", "kind": "class", "line": 459, "name": "WeightShapeProbe", "signature": "class WeightShapeProbe"}, {"doc": "Builds a TopoGPT2Config matching the loaded checkpoint and tokenizer.", "kind": "class", "line": 502, "name": "TopoGPT2ConfigAligner", "signature": "class TopoGPT2ConfigAligner"}, {"doc": "Builds a BPETokenizer instance using the configured encoding.", "kind": "class", "line": 533, "name": "TokenizerFactory", "signature": "class TokenizerFactory"}, {"doc": "Applies the idempotent Gauss complex-multiply patch when enabled.", "kind": "class", "line": 546, "name": "GaussPatchApplier", "signature": "class GaussPatchApplier"}, {"doc": "Instantiates the model and loads weights from safetensors.", "kind": "class", "line": 564, "name": "ModelAssembler", "signature": "class ModelAssembler"}, {"doc": "Applies deterministic seeds across torch, CUDA and the model package.", "kind": "class", "line": 601, "name": "SeedSynchronizer", "signature": "class SeedSynchronizer"}, {"doc": "Computes the relative L2 distance between two latent tensors.", "kind": "class", "line": 624, "name": "LatentChangeMetric", "signature": "class LatentChangeMetric"}, {"doc": "Aggregated counters describing a single token's reasoning episode.", "kind": "class", "line": 648, "name": "ReasoningIterationStats", "signature": "class ReasoningIterationStats"}, {"doc": "Aggregated statistics over the full generation episode.", "kind": "class", "line": 661, "name": "GenerationReasoningSummary", "signature": "class GenerationReasoningSummary"}, {"doc": "Persists the high-level latent state across consecutive emitted tokens.\n\nThe cache is reset whenever its age in tokens reaches the configured\npersistence horizon, at which point the next reasoning episode begins\nwith a zero high-level state. This is the temporal-sparsity mechanism:\nexpensive full-stack passes are amortized across multiple emissions.", "kind": "class", "line": 684, "name": "SparseHighLevelStateCache", "signature": "class SparseHighLevelStateCache"}, {"doc": "Parameter-free hierarchical recursive reasoning over a trained stack.\n\nThe reasoner does not own any learnable parameters. It treats the trained\nTopoGPT2 transformer layers as a deterministic recurrent step function\nand composes them into a two-speed damped fixed-point iteration that\nmirrors HRM, while never violating the activation distribution the\ntrained layers expect.\n\nAlgorithm per emitted token:\n\n    1. Run the standard full forward pass once to obtain the baseline\n       residual-stream latent z_base and the per-layer kv caches that\n       will cross the token boundary. z_base is the trained model's\n       native answer for this position.\n    2. If recursion is disabled or both iteration budgets are zero,\n       return z_base unchanged.\n    3. Optionally warm-start z by adding a fraction of the cached\n       refinement vector from previous tokens (sparse temporal memory).\n    4. Hierarchical refinement, all in residual-stream space:\n          for h_step in range(max_high_level_iters):\n              for l_step in range(max_low_level_iters):\n                  z <- z + low_level_step * (W_low(z) - z)\n              z <- z + high_level_step * (W_high(z) - z)\n       where W_low and W_high are the last low_level_window and\n       high_level_window trained layers respectively, invoked with the\n       prefix kv cache treated as immutable. Each update is damped, so\n       layer inputs remain close to the trained residual-stream\n       distribution.\n    5. Hard divergence guard: if the iterated latent drifts farther\n       from the baseline than max_drift_relative, reset to the baseline\n       and abort thinking for this token. This eliminates the\n       catastrophic-attractor failure mode without retraining.\n    6. Attractor halting per loop, plus a global cap on total layer\n       invocations.\n\nThe cached refinement returned to the sparse cache is z_final - z_base,\na small residual-stream displacement that persists across configurable\nhorizons to amortize thinking effort over multiple tokens.", "kind": "class", "line": 727, "name": "HierarchicalRecursiveReasoner", "signature": "class HierarchicalRecursiveReasoner"}, {"doc": "Applies temperature, repetition penalty, top-k filtering and multinomial draw.", "kind": "class", "line": 935, "name": "LogitsSampler", "signature": "class LogitsSampler"}, {"doc": "Immutable sampling parameters consumed by the generation engine.", "kind": "class", "line": 963, "name": "SamplingPolicy", "signature": "class SamplingPolicy"}, {"doc": "Quantitative summary of a single generation call.", "kind": "class", "line": 985, "name": "GenerationReport", "signature": "class GenerationReport"}, {"doc": "Runs autoregressive sampling driven by hierarchical recursive reasoning.\n\nThe engine reimplements the prompt encoding and token emission loop so\nthat the per-token latent state can be intercepted before final norm and\nLM-head projection. The intercepted state is handed to a\nHierarchicalRecursiveReasoner, which iterates the trained layer stack in\na two-speed loop until the attractor is reached. The final stabilized\nlatent is then projected to logits and sampled in the standard fashion.", "kind": "class", "line": 1000, "name": "HRMGenerationEngine", "signature": "class HRMGenerationEngine"}, {"doc": "Prints a GenerationReport to stdout using settings-defined formatting.", "kind": "class", "line": 1189, "name": "ResultRenderer", "signature": "class ResultRenderer"}, {"doc": "Orchestrator wiring loader, builder, reasoner, engine and renderer.", "kind": "class", "line": 1230, "name": "HRMInferencePipeline", "signature": "class HRMInferencePipeline"}, {"doc": "Translates command-line arguments into an HRMInferenceSettings instance.", "kind": "class", "line": 1283, "name": "CliArgumentParser", "signature": "class CliArgumentParser"}, {"doc": "CLI entry point. Returns a process exit code.", "kind": "method", "line": 1494, "name": "main", "signature": "def main(argv)"}, {"doc": "Return the architecture preset table indexed by scale name.", "kind": "method", "line": 221, "name": "scale_presets", "signature": "def scale_presets()"}, {"doc": "Return the resolved preset for the configured model scale.", "kind": "method", "line": 234, "name": "preset", "signature": "def preset(self)"}, {"doc": "Raise ValueError if any setting falls outside its safety bounds.", "kind": "method", "line": 244, "name": "validate", "signature": "def validate(self)"}, {"doc": "Return a configured Logger with a single deduplicated stdout handler.", "kind": "method", "line": 347, "name": "build", "signature": "def build(settings)"}, {"doc": "Join parts under root and return the canonical resolved path.\n\nRaises ValueError if the resolved path escapes root.", "kind": "method", "line": 367, "name": "resolve_under", "signature": "def resolve_under(root)"}, {"doc": "Validate path points to an existing regular file with the expected suffix.", "kind": "method", "line": 383, "name": "require_existing_file", "signature": "def require_existing_file(path, expected_suffix)"}, {"kind": "method", "line": 400, "name": "__init__", "signature": "def __init__(self, settings, logger)"}, {"doc": "Return the topogpt3.train module which re-exports model symbols.", "kind": "method", "line": 404, "name": "load", "signature": "def load(self)"}, {"kind": "method", "line": 416, "name": "__init__", "signature": "def __init__(self, settings)"}, {"doc": "Directory holding the active checkpoint slot.", "kind": "method", "line": 424, "name": "slot_dir", "signature": "def slot_dir(self)"}, {"doc": "Resolved path to the safetensors weights file inside the slot.", "kind": "method", "line": 428, "name": "model_file", "signature": "def model_file(self)"}, {"doc": "Resolved path to the JSON training-state file inside the slot.", "kind": "method", "line": 434, "name": "state_file", "signature": "def state_file(self)"}, {"doc": "Verify weights exist and the on-disk size lies within safety bounds.", "kind": "method", "line": 440, "name": "assert_ready", "signature": "def assert_ready(self)"}, {"kind": "method", "line": 462, "name": "__init__", "signature": "def __init__(self, settings, logger)"}, {"doc": "Recover N_KV_HEADS used at training by inspecting the k_proj shape.\n\nReturns None when the probe key is absent, signalling the caller to\nfall back to scale defaults rather than guess.", "kind": "method", "line": 466, "name": "detect_n_kv_heads", "signature": "def detect_n_kv_heads(self, weights_path, d_model, n_heads)"}, {"kind": "method", "line": 505, "name": "__init__", "signature": "def __init__(self, settings, source_module, logger)"}, {"doc": "Return a TopoGPT2Config dataclass ready to instantiate the model.", "kind": "method", "line": 511, "name": "build", "signature": "def build(self, n_kv_heads, vocab_size)"}, {"kind": "method", "line": 536, "name": "__init__", "signature": "def __init__(self, settings, source_module)"}, {"doc": "Return an instance of BPETokenizer bound to the configured encoding.", "kind": "method", "line": 540, "name": "build", "signature": "def build(self)"}, {"kind": "method", "line": 549, "name": "__init__", "signature": "def __init__(self, settings, source_module, logger)"}, {"doc": "Patch QuaternionSpectralLayer to use the 3-multiply Gauss contract.", "kind": "method", "line": 555, "name": "apply_if_enabled", "signature": "def apply_if_enabled(self)"}, {"kind": "method", "line": 567, "name": "__init__", "signature": "def __init__(self, settings, source_module, logger)"}, {"doc": "Build the TopoGPT2 graph, load weights into it, and return it in eval mode.", "kind": "method", "line": 573, "name": "assemble", "signature": "def assemble(self, aligned_cfg, paths)"}, {"kind": "method", "line": 604, "name": "__init__", "signature": "def __init__(self, settings, source_module, logger)"}, {"doc": "Seed all relevant RNGs using the model package helper when available.", "kind": "method", "line": 610, "name": "apply", "signature": "def apply(self)"}, {"kind": "method", "line": 627, "name": "__init__", "signature": "def __init__(self, epsilon_floor)"}, {"doc": "Return ||current - previous|| / max(||previous||, epsilon_floor).", "kind": "method", "line": 632, "name": "relative_change", "signature": "def relative_change(self, current, previous)"}, {"doc": "Fold a per-token sample into the running totals.", "kind": "method", "line": 671, "name": "absorb", "signature": "def absorb(self, sample)"}, {"kind": "method", "line": 693, "name": "__init__", "signature": "def __init__(self, persist_tokens)"}, {"doc": "Return the cached high-level state or a zeroed one when stale.\n\nThe boolean flag indicates whether the returned tensor came from a\nlive cache hit (True) or a fresh zero initialization (False).", "kind": "method", "line": 700, "name": "get_or_init", "signature": "def get_or_init(self, reference)"}, {"doc": "Store a fresh high-level state and increment the cache age.", "kind": "method", "line": 716, "name": "commit", "signature": "def commit(self, new_state)"}, {"doc": "Drop any cached state and reset the age counter.", "kind": "method", "line": 721, "name": "invalidate", "signature": "def invalidate(self)"}, {"kind": "method", "line": 768, "name": "__init__", "signature": "def __init__(self, layers, final_norm, reasoning_config, logger)"}, {"doc": "Return the number of trained transformer layers.", "kind": "method", "line": 789, "name": "num_layers", "signature": "def num_layers(self)"}, {"doc": "Forward z_in through every layer using base_kvs as immutable prefix cache.\n\nReturns the layer-stack output and the freshly produced per-layer kv\ncaches that incorporate the K and V derived from z_in.", "kind": "method", "line": 793, "name": "_full_pass", "signature": "def _full_pass(self, z_in, base_kvs)"}, {"doc": "Forward z_in through the trailing `window` layers only.\n\nThe per-layer kv caches produced during this read-only pass are\ndiscarded; only the baseline pass's committed kvs cross the token\nboundary, preserving cache consistency across thinking iterations.", "kind": "method", "line": 808, "name": "_window_pass", "signature": "def _window_pass(self, z_in, base_kvs, window)"}, {"doc": "Run hierarchical recursive thinking for a single emission step.\n\nArgs:\n    z_initial: token embedding of the new position, shape [B, 1, D].\n    base_kvs: per-layer kv cache for all previously emitted tokens,\n        treated as immutable during thinking iterations.\n    cached_refinement: persistent refinement displacement from prior\n        tokens, or None to skip the warm start.\n\nReturns:\n    A tuple (z_final, committed_kvs, refinement_for_cache, stats):\n        z_final is the latent state about to enter the final norm\n        and lm head; committed_kvs is the new per-layer kv cache\n        including this token's K and V from the baseline pass;\n        refinement_for_cache is z_final - z_baseline, to be\n        persisted across tokens; stats holds the loop counters.", "kind": "method", "line": 827, "name": "reason", "signature": "def reason(self, z_initial, base_kvs, cached_refinement)"}, {"kind": "method", "line": 938, "name": "__init__", "signature": "def __init__(self, logger)"}, {"doc": "Return a sampled token id tensor of shape [B, 1] from raw logits [B, V].", "kind": "method", "line": 941, "name": "sample", "signature": "def sample(self, logits, token_history, temperature, top_k, repetition_penalty)"}, {"doc": "Construct a SamplingPolicy from inference settings.", "kind": "method", "line": 973, "name": "from_settings", "signature": "def from_settings(cls, settings)"}, {"doc": "Return throughput in tokens/sec, clamped to avoid divide-by-zero.", "kind": "method", "line": 995, "name": "tokens_per_second", "signature": "def tokens_per_second(self, elapsed_floor)"}, {"kind": "method", "line": 1011, "name": "__init__", "signature": "def __init__(self, settings, logger)"}, {"doc": "Run the prompt through the full stack once, returning the final\nhidden state of the last position, the per-layer base kv caches that\ncover all prompt tokens except the last one, and the embedding of the\nlast prompt token as the seed for the first reasoning episode.", "kind": "method", "line": 1016, "name": "_encode_prompt", "signature": "def _encode_prompt(self, model, prompt_ids)"}, {"doc": "Generate a completion for prompt and return a GenerationReport.", "kind": "method", "line": 1048, "name": "run", "signature": "def run(self, model, tokenizer, prompt, policy)"}, {"kind": "method", "line": 1192, "name": "__init__", "signature": "def __init__(self, settings, logger)"}, {"doc": "Emit a banner with prompt, completion, throughput and reasoning stats.", "kind": "method", "line": 1196, "name": "render", "signature": "def render(self, report)"}, {"kind": "method", "line": 1233, "name": "__init__", "signature": "def __init__(self, settings, logger)"}, {"doc": "Run the full inference pipeline end-to-end and return the report.", "kind": "method", "line": 1239, "name": "execute", "signature": "def execute(self)"}, {"doc": "Return the configured argparse.ArgumentParser.", "kind": "method", "line": 1287, "name": "build_parser", "signature": "def build_parser()"}, {"doc": "Parse argv (or sys.argv) and return a populated HRMInferenceSettings.", "kind": "method", "line": 1448, "name": "parse", "signature": "def parse(argv)"}]}, {"id": "topogpt3/jlens.py", "kind": "module", "label": "jlens.py", "language": "py", "sha256": "4aefc982cee01936", "symbol_count": 29, "symbols": [{"doc": "Centralized configuration for Jacobian lens fitting.\n\nEvery value consumed downstream resides here. Adding a new tunable means\nextending this class; no other module should embed literals.", "kind": "class", "line": 37, "name": "TopoGPT3JLensFitConfig", "signature": "class TopoGPT3JLensFitConfig"}, {"doc": "Centralized configuration for Jacobian lens application.\n\nEvery value consumed downstream resides here. Adding a new tunable means\nextending this class; no other module should embed literals.", "kind": "class", "line": 56, "name": "TopoGPT3JLensAppConfig", "signature": "class TopoGPT3JLensAppConfig"}, {"doc": "Captures residual-stream tensors at the given block indices.\n\nRegisters a forward hook on each requested block on ``__enter__`` and\nremoves them on ``__exit__``. On the next forward pass each block's output\nis stored in ``activations``, keyed by block index. Stored tensors are\nnot detached, so they can be passed straight to ``torch.autograd.grad``.\n\nArgs:\n    blocks: The sequence of residual blocks (e.g. ``model.layers``).\n    at: Block indices to record at.\n    start_graph_at: If given, the captured tensor at this index is marked\n        ``requires_grad_(True)`` before downstream blocks see it. When the\n        model's parameters all have ``requires_grad=False``, this makes the\n        captured residual the leaf that roots the autograd graph, so the\n        retained graph spans only this block onward.", "kind": "class", "line": 69, "name": "ActivationRecorder", "signature": "class ActivationRecorder"}, {"doc": "Boolean mask over sequence positions to include in the Jacobian average.\n\nEarly positions are dominated by attention-sink behaviour and the final\nposition has no next-token target, so both are excluded.\n\nArgs:\n    seq_len: Length of the tokenized prompt.\n    skip_first: Number of leading positions to exclude.\n\nReturns:\n    Boolean tensor of shape ``[seq_len]``.\n\nRaises:\n    ValueError: If ``skip_first`` is negative or the prompt is too short to\n        leave any valid positions.", "kind": "method", "line": 132, "name": "valid_position_mask", "signature": "def valid_position_mask(seq_len)"}, {"doc": "Resolve None/negative layer indices, bounds-check, enforce source < target.", "kind": "method", "line": 162, "name": "_check_layer_indices", "signature": "def _check_layer_indices(source_layers, target_layer, n_layers)"}, {"doc": "Compute the per-layer Jacobian estimator ``J_l`` for one prompt.\n\nRuns one forward pass on the prompt replicated ``dim_batch`` times along\nthe batch axis, retains the graph, then runs ``ceil(d_model / dim_batch)``\nbackward passes against it. Each backward computes ``dim_batch`` rows of\n``J_l`` at once: batch element ``b`` carries a one-hot cotangent at output\ndimension ``dim_start + b``, set at every valid target position.\n\nArgs:\n    model: The model to compute Jacobians for.\n    prompt: Input text.\n    source_layers: Layer indices ``l`` to compute ``J_l`` at.\n    target_layer: Layer to take gradients with respect to. Defaults to the\n        final layer; negative indices count from the end.\n    dim_batch: Output dimensions computed per backward pass.\n    max_seq_len: Truncate the prompt to this many tokens.\n    skip_first: Leading positions to exclude.\n\nReturns:\n    ``(jacobians, seq_len, n_valid_positions)``. ``jacobians`` maps each\n    source layer to a ``[d_model, d_model]`` fp32 CPU tensor.", "kind": "method", "line": 187, "name": "jacobian_for_prompt", "signature": "def jacobian_for_prompt(model, prompt, source_layers)"}, {"doc": "``torch.save`` to a temp file then ``os.replace`` so a crash never\nleaves a half-written checkpoint.", "kind": "method", "line": 283, "name": "_atomic_save", "signature": "def _atomic_save(obj, path)"}, {"doc": "Fit ``J_l`` over a list of prompts and return a JacobianLens.\n\nPer-prompt Jacobians from ``jacobian_for_prompt`` are accumulated as a\nrunning mean. If ``checkpoint_path`` is set, the running sum is written\nevery ``checkpoint_every`` prompts (atomic) and resumed from on restart.\n\nArgs:\n    model: The model to fit on.\n    prompts: Text prompts to average over.\n    source_layers: Layers to fit at. Defaults to every layer below\n        ``target_layer``; negative indices count from the end.\n    target_layer: See ``jacobian_for_prompt``.\n    dim_batch: See ``jacobian_for_prompt``.\n    max_seq_len: Truncate each prompt to this many tokens.\n    skip_first: See ``jacobian_for_prompt``.\n    checkpoint_path: If set, write a resumable checkpoint here.\n    checkpoint_every: Write checkpoint every N prompts (default 1).\n    resume: If True and checkpoint_path exists, resume from it.\n\nReturns:\n    The fitted JacobianLens.\n\nRaises:\n    ValueError: If no prompts are long enough to fit on, or if checkpoint\n        settings mismatch.", "kind": "method", "line": 291, "name": "fit", "signature": "def fit(model, prompts)"}, {"doc": "A fitted Jacobian lens: per-layer ``J_l`` matrices and the readout method.\n\nAttributes:\n    jacobians: ``{layer_index: Tensor[d_model, d_model]}``. Each ``J_l``\n        maps the residual at layer ``l`` into the final-layer basis.\n    source_layers: Sorted list of fitted layer indices.\n    n_prompts: Number of prompts the lens was averaged over.\n    d_model: Residual-stream width.", "kind": "class", "line": 459, "name": "JacobianLens", "signature": "class JacobianLens"}, {"doc": "Text-format slice data: top-K token predictions per (position, layer).\n\n``layers`` always includes the model's final layer (the actual model\noutput) so divergences from lens-transported earlier layers are visible.\n\nAttributes:\n    seq_len: Number of token positions in the slice.\n    layers: Layer indices shown (includes final layer).\n    prompt: The input prompt text.\n    input_ids: Tensor ``[1, seq_len]`` of token IDs.\n    token_strs: Decoded strings for each token position.\n    top_ids: ``[seq_len, n_layers, top_n]`` top token IDs per cell.\n    top_probs: ``[seq_len, n_layers, top_n]`` softmax probabilities.\n    top_token_strs: ``[seq_len, n_layers, top_n]`` decoded token strings\n        for each prediction. Empty string if tokenizer was unavailable.", "kind": "class", "line": 664, "name": "SliceData", "signature": "class SliceData"}, {"doc": "Compute a position x layer slice of top-K token predictions.\n\nFor each layer in the fitted lens, projects the residual at each position\nthrough the Jacobian into the final-layer basis, then unembeds to get\nlogits and softmax probabilities. Returns the top-N predicted token IDs\nand their probabilities per (position, layer) cell.\n\nArgs:\n    model: The model to read out from.\n    lens: A fitted JacobianLens.\n    prompt: Input text.\n    top_n: Top tokens to keep per (position, layer) cell.\n    max_seq_len: Truncate the prompt to this many tokens.\n\nReturns:\n    A SliceData instance with arrays indexed ``[seq_len, n_layers, top_n]``.", "kind": "method", "line": 705, "name": "compute_slice", "signature": "def compute_slice(model, lens, prompt)"}, {"doc": "Render a SliceData as a readable text table showing decoded words.\n\nFor each token position, shows what each layer predicts as the next token.\nThe first column shows the actual input token; subsequent columns show the\ntop-1 prediction at each layer with its softmax probability. Token strings\nare read from ``slice_data.top_token_strs`` (always populated by\n``compute_slice``).\n\nArgs:\n    slice_data: The slice to render.\n    tokenizer: Legacy parameter, ignored. Top token strings are already\n        stored in ``slice_data.top_token_strs``.\n    n_cols: Number of layer columns to show (default 3).\n\nReturns:\n    A multi-line string table.", "kind": "method", "line": 789, "name": "text_slice", "signature": "def text_slice(slice_data, tokenizer, n_cols)"}, {"doc": "Run a full jacobian lens demo loading real weights from checkpoint.", "kind": "method", "line": 842, "name": "_demo_jlens", "signature": "def _demo_jlens()"}, {"kind": "method", "line": 87, "name": "__init__", "signature": "def __init__(self, blocks, at)"}, {"kind": "method", "line": 102, "name": "_make_hook", "signature": "def _make_hook(self, index)"}, {"kind": "method", "line": 113, "name": "__enter__", "signature": "def __enter__(self)"}, {"kind": "method", "line": 126, "name": "__exit__", "signature": "def __exit__(self)"}, {"kind": "method", "line": 378, "name": "write_checkpoint", "signature": "def write_checkpoint()"}, {"kind": "method", "line": 470, "name": "__init__", "signature": "def __init__(self, jacobians)"}, {"kind": "method", "line": 482, "name": "__repr__", "signature": "def __repr__(self)"}, {"doc": "Save to ``path``. Jacobians are stored as ``dtype`` (default fp16).", "kind": "method", "line": 489, "name": "save", "signature": "def save(self, path)"}, {"doc": "Load a lens previously written by ``save``.", "kind": "method", "line": 504, "name": "load", "signature": "def load(cls, path)"}, {"doc": "Load a lens from a local file, a local directory, or a HuggingFace\nHub ``repo_id``.\n\n``filename`` is the path inside the directory or repo; ignored when\n``name_or_path`` is itself a file. ``revision`` selects a Hub branch,\ntag, or commit.", "kind": "method", "line": 519, "name": "from_pretrained", "signature": "def from_pretrained(cls, name_or_path)"}, {"doc": "Combine lenses fitted on disjoint prompt subsets into one\n(``n_prompts``-weighted mean of the inputs).\n\nArgs:\n    lenses: Lenses to merge. Must agree on ``source_layers`` and\n        ``d_model``.\n\nRaises:\n    ValueError: If ``lenses`` is empty or the inputs disagree on shape.", "kind": "method", "line": 543, "name": "merge", "signature": "def merge(cls, lenses)"}, {"doc": "Map a residual at ``layer`` into the final-layer basis: ``J_l @ h``.\n\nArgs:\n    residual: Tensor of shape ``[..., d_model]``.\n    layer: Source layer index (must be in ``source_layers``).", "kind": "method", "line": 574, "name": "transport", "signature": "def transport(self, residual, layer)"}, {"doc": "Run ``model`` on ``prompt`` and return lens logits at ``positions``.\n\nArgs:\n    model: The model to read out from.\n    prompt: Input text.\n    layers: Layers to read out at. Defaults to all of\n        ``source_layers``. Must be a subset of ``source_layers`` when\n        ``use_jacobian`` is True.\n    positions: Token positions to read out (Python indexing into the\n        sequence; negative indices count from the end). None returns\n        every position.\n    max_seq_len: Truncate the prompt to this many tokens.\n    use_jacobian: If False, skip the ``J_l`` transport (vanilla\n        logit-lens baseline).\n\nReturns:\n    A triple ``(lens_logits, model_logits, input_ids)``. ``lens_logits``\n    maps each requested layer to a ``[n_positions, vocab_size]`` tensor;\n    ``model_logits`` is the model's actual final-layer logits at the\n    same positions (same shape).\n\nRaises:\n    ValueError: If any requested layer is out of range for the model,\n        or (with use_jacobian) not in source_layers.", "kind": "method", "line": 585, "name": "apply", "signature": "def apply(self, model, prompt)"}, {"kind": "method", "line": 692, "name": "__post_init__", "signature": "def __post_init__(self)"}, {"kind": "method", "line": 105, "name": "hook", "signature": "def hook(module, inputs, output)"}, {"kind": "method", "line": 646, "name": "select", "signature": "def select(layer)"}]}, {"id": "topogpt3/lens_model.py", "kind": "module", "label": "lens_model.py", "language": "py", "sha256": "47fabe41f0bbfa6b", "symbol_count": 29, "symbols": [{"doc": "What the lens needs from a model.\n\nAttributes:\n    n_layers: Number of residual blocks.\n    d_model: Residual-stream width.\n    layers: The residual blocks, indexable by integer; what\n        ActivationRecorder hooks.\n    tokenizer: Tokenizer used by the visualisation helpers; must provide\n        ``decode(token_ids) -> str``. Fitting and apply() never touch it.", "kind": "class", "line": 23, "name": "LensModel", "signature": "class LensModel(Protocol)"}, {"doc": "Centralized configuration for the TopoGPT3 lens model adapter.\n\nEvery value consumed downstream resides here. Adding a new tunable means\nextending this class; no other module should embed literals.", "kind": "class", "line": 59, "name": "TopoGPT3LensConfig", "signature": "class TopoGPT3LensConfig"}, {"doc": "Runs the residual block stack only (no final norm, no LM head).\n\nThis is the forward subgraph that ActivationRecorder hooks capture.\nExtracted from TopoGPT2.forward() to expose the residual stream for\nJacobian lens fitting and application.", "kind": "class", "line": 142, "name": "_TopoGPT3ResidualForward", "signature": "class _TopoGPT3ResidualForward(Module)"}, {"doc": "LensModel adapter over a loaded TopoGPT2 model.\n\nWraps a TopoGPT2 instance and implements the LensModel protocol for use\nwith ActivationRecorder, JacobianLens fitting, and apply().\n\nThe adapter owns no parameters --- all weights live in the wrapped model.\nCall ``.eval()`` and set ``requires_grad_(False)`` on the wrapped model\nbefore fitting.", "kind": "class", "line": 161, "name": "TopoGPT3LensModel", "signature": "class TopoGPT3LensModel(Module)"}, {"doc": "A tiny CPU-only decoder for end-to-end tests.\n\nImplements the LensModel protocol indirectly (wrapped by\nTopoGPT3LensModel). Residual blocks are ``h + 0.1 * linear(h)``:\nthe small gain keeps the Jacobian well-conditioned so the late-layer\n``diag(J) ~= 1`` property holds.", "kind": "class", "line": 306, "name": "TinyDecoder", "signature": "class TinyDecoder(Module)"}, {"kind": "class", "line": 359, "name": "_ResidualBlock", "signature": "class _ResidualBlock(Module)"}, {"doc": "Tokenize ``text`` to ``input_ids`` of shape ``[1, seq_len]`` on the\nmodel's input device.", "kind": "method", "line": 40, "name": "encode", "signature": "def encode(self, text)"}, {"doc": "Run the residual stack on ``input_ids`` (no LM head). Must build an\nautograd graph through layers when grad is enabled, and must be\ndeterministic across batch elements (eval mode, dropout off) --- the\nfitting estimator replicates the prompt along the batch axis.", "kind": "method", "line": 45, "name": "forward", "signature": "def forward(self, input_ids)"}, {"doc": "Map a residual-stream tensor ``[..., d_model]`` to logits\n``[..., vocab_size]`` (final norm + LM head).", "kind": "method", "line": 52, "name": "unembed", "signature": "def unembed(self, residual)"}, {"doc": "Construct a lens config from a TopoGPT2Config dataclass.", "kind": "method", "line": 84, "name": "from_topogpt2_config", "signature": "def from_topogpt2_config(cls, cfg)"}, {"doc": "Probe a checkpoint directory and infer lens config from state.json.\n\nArgs:\n    checkpoint_dir: Path to the checkpoint slot directory.\n    state_filename: JSON file containing training config.\n\nReturns:\n    A TopoGPT3LensConfig matching the checkpoint.\n\nRaises:\n    FileNotFoundError: If state.json is missing.\n    ValueError: If required fields are absent from the state.", "kind": "method", "line": 104, "name": "probe_checkpoint", "signature": "def probe_checkpoint(cls, checkpoint_dir)"}, {"kind": "method", "line": 150, "name": "__init__", "signature": "def __init__(self, model)"}, {"kind": "method", "line": 154, "name": "forward", "signature": "def forward(self, input_ids)"}, {"kind": "method", "line": 172, "name": "__init__", "signature": "def __init__(self, model, tokenizer)"}, {"kind": "method", "line": 184, "name": "n_layers", "signature": "def n_layers(self)"}, {"kind": "method", "line": 188, "name": "d_model", "signature": "def d_model(self)"}, {"kind": "method", "line": 192, "name": "layers", "signature": "def layers(self)"}, {"kind": "method", "line": 196, "name": "tokenizer", "signature": "def tokenizer(self)"}, {"kind": "method", "line": 200, "name": "tokenizer", "signature": "def tokenizer(self, tok)"}, {"kind": "method", "line": 204, "name": "input_device", "signature": "def input_device(self)"}, {"kind": "method", "line": 210, "name": "input_device", "signature": "def input_device(self, device)"}, {"doc": "Tokenize text to input_ids of shape ``[1, seq_len]``.\n\nUses BPETokenizer if available, otherwise falls back to a byte-level\nencoding compatible with GPT-2 BPE tokenization.", "kind": "method", "line": 213, "name": "encode", "signature": "def encode(self, text)"}, {"doc": "Run the residual stack on ``input_ids``.\n\nReturns hidden states of shape ``[batch, seq_len, d_model]``\n(pre-final-norm, pre-LM-head). The autograd graph is retained through\nall layers when grad is enabled.", "kind": "method", "line": 228, "name": "forward", "signature": "def forward(self, input_ids)"}, {"doc": "Map residual ``[..., d_model]`` to logits ``[..., vocab_size]``.\n\nApplies the model's final norm and LM head projection.", "kind": "method", "line": 237, "name": "unembed", "signature": "def unembed(self, residual)"}, {"doc": "Build a TopoGPT3LensModel from a checkpoint directory.\n\nProbes state.json for configuration, instantiates the model, loads\nsafetensors weights, and wraps the result.\n\nArgs:\n    checkpoint_dir: Path to the checkpoint slot directory.\n    device: Target device. Defaults to cuda if available else cpu.\n    encoding: Tokenizer encoding name (passed to BPETokenizer).\n    strict: Whether to enforce strict state dict loading.\n\nReturns:\n    A TopoGPT3LensModel in eval mode with requires_grad_(False).\n\nRaises:\n    FileNotFoundError: If model.safetensors or state.json is missing.", "kind": "method", "line": 246, "name": "from_checkpoint", "signature": "def from_checkpoint(cls, checkpoint_dir)"}, {"kind": "method", "line": 315, "name": "__init__", "signature": "def __init__(self, n_layers, d_model, vocab_size, seed)"}, {"kind": "method", "line": 344, "name": "forward", "signature": "def forward(self, token_ids, past_kvs)"}, {"kind": "method", "line": 360, "name": "__init__", "signature": "def __init__(self, d_model)"}, {"kind": "method", "line": 366, "name": "forward", "signature": "def forward(self, x, past_kv)"}]}, {"id": "topogpt3/model.py", "kind": "module", "label": "model.py", "language": "py", "sha256": "727d864f753242b1", "symbol_count": 187, "symbols": [{"doc": "Configuración completa para TopoGPT2.", "kind": "class", "line": 56, "name": "TopoGPT2Config", "signature": "class TopoGPT2Config"}, {"kind": "method", "line": 192, "name": "setup_logger", "signature": "def setup_logger(name, level)"}, {"kind": "method", "line": 202, "name": "set_seed", "signature": "def set_seed(seed, device)"}, {"doc": "Operaciones de cuaterniones puras en PyTorch.\nRepresentación: [..., 4]  donde last dim = [w, x, y, z]\nq = w + x*i + y*j + z*k", "kind": "class", "line": 214, "name": "QuaternionOps", "signature": "class QuaternionOps"}, {"doc": "Capa lineal con pesos cuaterniones.\n\nImplementa la multiplicación W * x en el álgebra de cuaterniones:\n- W = Ww + Wx*i + Wy*j + Wz*k  (cuaternión de pesos)\n- x = xw + xx*i + xy*j + xz*k  (cuaternión de entrada)\n- out = W * x  (producto de Hamilton extendido a vectores)\n\nParámetros: 4 matrices reales de forma [out_q, in_q]", "kind": "class", "line": 253, "name": "QuaternionLinear", "signature": "class QuaternionLinear(Module)"}, {"doc": "Convolución espectral 2D con cuaterniones y producto de Hamilton completo.\n\nOperación en dominio de frecuencia:\n    P(k) = W(k) ⊗ X(k)  (producto de Hamilton de cuaterniones complejos)\n\nDonde:\n    X(k) = FFT2(x) con 4 canales cuaterniones [Xw, Xx, Xy, Xz]\n    W(k) = kernel complejo aprendible con componentes [Ww, Wx, Wy, Wz]\n\nReglas del producto de Hamilton en dominio de frecuencia:\n    Pw = Ww·Xw - Wx·Xx - Wy·Xy - Wz·Xz\n    Px = Ww·Xx + Wx·Xw + Wy·Xz - Wz·Xy\n    Py = Ww·Xy - Wx·Xz + Wy·Xw + Wz·Xx\n    Pz = Ww·Xz + Wx·Xy - Wy·Xx + Wz·Xw\n\nCada Wc es un kernel complejo (partes real e imaginaria independientes).", "kind": "class", "line": 298, "name": "QuaternionSpectralLayer", "signature": "class QuaternionSpectralLayer(Module)"}, {"doc": "Autoencoder espectral con cuaterniones.\n\nOpera en dos niveles:\n1. Espectral 1D sobre el vector de features (FFT sobre dim D_MODEL):\n   captura la espectrografía global del embedding.\n2. Espectral 2D sobre el grid del toro (QuaternionSpectralLayer):\n   captura correlaciones espaciales en la topología.\n\nDevuelve (latent, recon_loss) para regularización.", "kind": "class", "line": 385, "name": "SpectralAutoencoder", "signature": "class SpectralAutoencoder(Module)"}, {"doc": "Reemplaza el MLP en cada capa del transformer.\n\nPipeline (completamente vectorizado sobre batch Y secuencia):\n\n1. Flatten: [B, S, D] → [B·S, D]\n2. SpectralAutoencoder: filtrado espectral 1D + compresión cuaternión\n3. Proyección al toro:\n   - Calcula 2 ángulos (phi1, phi2) ∈ [-π, π]²\n   - Asignación blanda a los 8 nodos via distancia circular en el toro\n4. Construye grid de nodos: [B·S, N_NODES=8, D_MODEL]\n5. QuaternionSpectralLayer 2D sobre el grid [B·S, 4*D_QUAT, RADIAL, ANGULAR]\n6. Message-passing con rotaciones cuaterniones sobre el grafo toro\n7. Readout: atención sobre los 8 nodos → [B·S, D_MODEL]\n8. Reshape: [B·S, D] → [B, S, D]", "kind": "class", "line": 468, "name": "QuaternionTorusBrain", "signature": "class QuaternionTorusBrain(Module)"}, {"doc": "Rotary Position Embeddings (RoPE) - Su et al., 2021.\nCodifica la posicion como rotaciones del espacio de atencion,\nnaturalmente relativas y sin parametros extra.\n\nLas caches _cos/_sin se registran como buffers no-persistentes con\nnombres que no colisionan con checkpoints antiguos (que usaban\n'cos_cache'/'sin_cache'). Esto permite cambiar MAX_SEQ_LEN sin\nerrores de shape al cargar checkpoints previos.", "kind": "class", "line": 685, "name": "RotaryEmbedding", "signature": "class RotaryEmbedding(Module)"}, {"doc": "Root Mean Square Layer Normalization (sin bias). Más estable que LayerNorm.", "kind": "class", "line": 739, "name": "RMSNorm", "signature": "class RMSNorm(Module)"}, {"doc": "SwiGLU: SiLU(gate(x)) * up(x) -> down\nUsado en LLaMA 2/3, Qwen, Mistral en lugar de GELU-FFN.\nDimension interna: 8/3 * d_model (convención LLaMA, redondeada a múltiplo de 4).", "kind": "class", "line": 756, "name": "SwiGLU", "signature": "class SwiGLU(Module)"}, {"doc": "Mixture of Experts sobre la capa topologica.\n\nArquitectura (inspirada en DeepSeek-MoE / Mixtral):\n  - 1 experto compartido: QuaternionTorusBrain (siempre activo)\n  - N_EXPERTS expertos SwiGLU ligeros (activacion esparsa: Top-K por token)\n  - Router: Linear(D, N_EXPERTS) + softmax → top-K\n\nLoad-balancing loss (auxiliar): penaliza si un experto acapara todos los tokens.\nActiva MOE_TOP_K de N_EXPERTS expertos por token.\n\nSin MoE (MOE_ENABLED=False): se comporta como QuaternionTorusBrain puro.", "kind": "class", "line": 785, "name": "TopoMoEBrain", "signature": "class TopoMoEBrain(Module)"}, {"doc": "Multi-head attention con:\n- Flash Attention (scaled_dot_product_attention de PyTorch 2.0+)\n- Rotary Position Embeddings (RoPE)\n- GQA (Grouped Query Attention): N_KV_HEADS < N_HEADS, reduce VRAM de K/V\n- KV Cache para inferencia autoregresiva eficiente\n- Temperatura termodinámica aprendible", "kind": "class", "line": 890, "name": "MultiHeadAttention", "signature": "class MultiHeadAttention(Module)"}, {"doc": "Capa del transformer con TopoMoEBrain (TopoBrain + MoE SwiGLU experts).\n\nEsquema pre-norm (estilo LLaMA):\n    x = x + Attention_GQA(RMSNorm(x))\n    x = x + TopoMoEBrain(RMSNorm(x))", "kind": "class", "line": 994, "name": "TopoGPT2Layer", "signature": "class TopoGPT2Layer(Module)"}, {"doc": "TopoGPT2: Transformer de lenguaje con TopoBrain cuaternión-espectral.\n\nArquitectura:\n    Embedding de tokens + RoPE (en Attention)\n    N_LAYERS × TopoGPT2Layer (Attention + QuaternionTorusBrain)\n    RMSNorm final\n    Proyección a vocabulario (weight-tied con embeddings)", "kind": "class", "line": 1041, "name": "TopoGPT2", "signature": "class TopoGPT2(Module)"}, {"doc": "Wrapper alrededor de tiktoken (GPT-2 compatible).", "kind": "class", "line": 1258, "name": "BPETokenizer", "signature": "class BPETokenizer"}, {"doc": "Disk-cached manifest of text files found in a directory tree.", "kind": "class", "line": 1384, "name": "FileManifest", "signature": "class FileManifest"}, {"doc": "Tokenizes file paths into a memory-mapped numpy array on disk.\n\nUses incremental file reading and batched writing to avoid loading\nall tokens into RAM. Tokens are stored as raw int64 on disk and\naccessed via numpy memmap (OS-level paging, near-zero RAM footprint).", "kind": "class", "line": 1451, "name": "MemmapTokenizer", "signature": "class MemmapTokenizer"}, {"doc": "Memory-mapped token dataset for sequence-to-sequence LM training.\n\nThe token array is backed by a numpy memmap file on disk.\nOnly accessed slices are paged into RAM by the OS. The .copy()\nin __getitem__ ensures the returned torch.Tensor owns its memory,\nwhich is required for DataLoader collation with worker processes.", "kind": "class", "line": 1540, "name": "MappedTokenDataset", "signature": "class MappedTokenDataset(Dataset)"}, {"doc": "Filters low-quality files from the corpus based on multiple heuristics.", "kind": "class", "line": 1574, "name": "TextFilter", "signature": "class TextFilter"}, {"doc": "Tiered dataset that exposes short/medium/all files based on line count.\n\nWorks as a wrapper around MappedTokenDataset. Provides __getitem__ that\nonly samples from the active tier, avoiding dataset duplication.", "kind": "class", "line": 1678, "name": "CurriculumDataset", "signature": "class CurriculumDataset(Dataset)"}, {"doc": "Classify file paths into complexity tiers by line count.\n\nReturns dict: tier -> list of file indices in that tier.\nTier 0 = short (<=short lines), tier 1 = medium, tier 2 = all.", "kind": "method", "line": 1716, "name": "build_file_tiers", "signature": "def build_file_tiers(paths, short, med)"}, {"doc": "Trainer that dynamically adjusts MAX_SEQ_LEN across training phases.\n\nPhase schedule (configurable):\n    phase 0: seq_len=128, epochs=3\n    phase 1: seq_len=256, epochs=3\n    phase 2: seq_len=512, epochs=4\n\nEach phase rebuilds the DataLoader with the new sequence length.", "kind": "class", "line": 1742, "name": "ProgressiveSeqLenTrainer", "signature": "class ProgressiveSeqLenTrainer"}, {"doc": "Speculative decoding with a small draft model.\n\nDraft model uses SPEC_DECODE_DRAFT_SCALE (e.g. 'micro').\nThe draft generates K tokens, then the target model verifies them\nin a single forward pass. Accepted tokens are kept; rejected ones\ntrigger a fallback to the target model sampling.", "kind": "class", "line": 1818, "name": "SpeculativeDecoder", "signature": "class SpeculativeDecoder"}, {"doc": "Wrapper around nn.Embedding that applies dynamic quantization.\n\nApplies int8 quantization to the embedding weight matrix after loading.\nSupports both embed (int8) and FFN (int4) quantization modes.", "kind": "class", "line": 1933, "name": "QuantizedEmbedding", "signature": "class QuantizedEmbedding(Module)"}, {"doc": "Quantize embedding and lm_head layers for reduced VRAM usage.", "kind": "method", "line": 1973, "name": "apply_quantization", "signature": "def apply_quantization(model, config)"}, {"doc": "Extends TopoGPT2Trainer with curriculum + progressive seq len support.\n\nProvides:\n- Tokens cache for progressive sequence length rebuilding\n- Curriculum dataset wrapping (short / medium / all tiers)", "kind": "class", "line": 2001, "name": "CurriculumTrainer", "signature": "class CurriculumTrainer"}, {"doc": "Tokenize a single text string and write tokens to disk as raw int64.", "kind": "method", "line": 2141, "name": "_tokenize_text_to_memmap", "signature": "def _tokenize_text_to_memmap(text, tokenizer, path, max_tokens)"}, {"doc": "Gestiona checkpoints de forma acumulativa y segura.\n\nEstructura en disco:\n    checkpoints_topogpt2/\n      latest/\n        model.safetensors   <- pesos del modelo (formato seguro, sin pickle)\n        optimizer.pt        <- estado del optimizador (requiere .pt)\n        state.json          <- metadatos: epoch, step, historial, config\n      best/\n        model.safetensors\n        state.json\n      step_NNNNN/           <- snapshots periodicos (rotados)\n        model.safetensors\n        optimizer.pt\n        state.json\n\nEl historial se ACUMULA entre sesiones de entrenamiento: cada --resume\nagrega nuevas entradas a train_loss[], val_loss[], etc.", "kind": "class", "line": 2153, "name": "CheckpointManager", "signature": "class CheckpointManager"}, {"doc": "Entrenador acumulativo y resumible.\n\nCaracteristicas:\n- Checkpoint automatico en safetensors cada N minutos + cada epoch\n- Historial acumulativo entre sesiones (--resume agrega al historial existente)\n- Guarda el mejor modelo en checkpoints/best/ automaticamente\n- LR schedule: cosine con warmup relativo a los steps de ESTA sesion\n- Mixed Precision (AMP) + acumulacion de gradientes", "kind": "class", "line": 2386, "name": "TopoGPT2Trainer", "signature": "class TopoGPT2Trainer"}, {"doc": "Calcula todas las metricas del diagrama de fases de Book.md.\n\nTodas las metricas se derivan de cantidades medibles (pesos, gradientes):\n\ndelta  (δ): margen de discretizacion.  max|w - round(w)|\n            δ≈0 -> cristal;  δ≈0.49 -> vidrio frio\nkappa  (κ): numero de condicion de la covarianza del gradiente.\n            κ≈1 -> cristalino;  κ>>1 -> amorfo\nT_eff:      temperatura efectiva = (lr/2) * Var(gradiente).\n            T_eff→0 -> congelado; T_eff alto -> ruidoso\nalpha  (α): indice de pureza = -log(δ + ε).\n            α=20 -> perfecto; α<1 -> vidrio\nberry:      fase de Berry de los kernels espectrales imaginarios.\n            |berry|>π/2 con winding≠0 -> insulador topologico\nlc:         complejidad local = 1 - similitud coseno promedio entre filas.\nsp:         superposicion = correlacion promedio inter-fila de pesos.", "kind": "class", "line": 2679, "name": "MechanisticMetrics", "signature": "class MechanisticMetrics"}, {"doc": "Encuentra el ratio imaginario/real optimo para los kernels espectrales.\n\nAnalogia con main.py: evalua la transicion GOE→GUE en el espacio\nde kernels. Un ratio optimo promueve estructura topologica (insulador)\nvs estructura amorfa (vidrio).\n\nMetodo: calibra con un mini-batch y mide la varianza del gradiente\nen funcion del ratio. Ratios que minimizan la varianza de gradiente\n(maxima coherencia espectral) son preferibles.\n\nNo entrena: solo inicializa los kernels con distintos ratios y mide.\nTiempo tipico: < 30 segundos.", "kind": "class", "line": 2916, "name": "Phase0_KernelOptimizer", "signature": "class Phase0_KernelOptimizer"}, {"doc": "Encuentra el batch size optimo testando candidatos con pocos pasos.\n\nDe main.py: el batch size regula la temperatura del horno de cristalizacion.\nBatch sizes demasiado chicos -> ruido excesivo (vidrio frio).\nBatch sizes demasiado grandes -> sin presion annealing (amorfos).\nLa ventana optima empirica de main.py: [24, 128] para Strassen.\n\nPara LM, testeamos candidatos midiendo:\n- delta (δ): velocidad de descenso en prospect_steps pasos\n- T_eff: temperatura efectiva del gradiente\n\nTiempo tipico: < 2 minutos para 3 candidatos × 30 pasos.", "kind": "class", "line": 2991, "name": "Phase1_BatchProspector", "signature": "class Phase1_BatchProspector"}, {"doc": "Encuentra semillas prometedoras midiendo la trayectoria de delta.\n\nDe main.py: una semilla \"buena\" muestra delta descendente en los\nprimeros N pasos (enfriamiento). Una semilla \"mala\" se estanca en\nel plateau vidrioso (~0.49).\n\nCriterio de seleccion:\n1. Semillas con delta_velocity < 0 (enfriando) AND kappa bajo.\n2. Si no hay, semillas solo enfriando.\n3. Fallback: semilla con menor delta final.\n\nTiempo tipico: < 3 minutos para 5 semillas × 50 pasos.", "kind": "class", "line": 3074, "name": "Phase2_SeedMiner", "signature": "class Phase2_SeedMiner"}, {"doc": "Refinamiento post-entrenamiento mediante recocido simulado.\n\nDe main.py: despues de que el modelo converge, una fase de annealing\ncon criterio de aceptacion de Metropolis puede empujar los pesos\nhacia estados de menor energia libre (menor delta o mejor val_loss).\n\nAceptacion de Metropolis:\n    si Δloss < 0: siempre acepta (mejora)\n    si Δloss >= 0: acepta con prob exp(-Δloss / T)\n\nLa temperatura T decae exponencialmente: T(t) = T0 * cooling_rate^t\n\nAl rechazar: restaura el mejor estado conocido.\nSi se estanca: perturbacion termica (ruido gaussiano en pesos).\n\nTiempo: proporcional a refine_epochs (user-controlled).", "kind": "class", "line": 3156, "name": "Phase4_AnnealingRefiner", "signature": "class Phase4_AnnealingRefiner"}, {"doc": "Pipeline with curriculum learning and progressive sequence length.\n\nReplaces TopoPhasePipeline when --curriculum or --progressive-seq-len is set.\nHandles:\n- Text quality filtering before tokenization (via TextFilter)\n- Curriculum tiers (short/medium/all files)\n- Progressive MAX_SEQ_LEN across phases: 128->256->512\n- Tokens cached in memory for fast DataLoader rebuilding per phase", "kind": "class", "line": 3317, "name": "TopoPhasePipelineV2", "signature": "class TopoPhasePipelineV2"}, {"doc": "Orquesta las 5 fases de entrenamiento segun main.py + Book.md.\n\nFases:\n  0  Kernel ratio optimization  (GOE-GUE spectral calibration)\n  1  Batch size prospecting      (temperatura del horno de cristalizacion)\n  2  Seed mining                 (seleccion de semilla enfriante)\n  3  Full training               (entrenamiento principal con metricas)\n  4  Annealing refinement        (recocido simulado post-entrenamiento)\n\nLas fases 0-2 son rapidas (prospecting). La fase 3 es el grueso.\nLa fase 4 es opcional (--refine).\n\nPara no ser prohibitivo:\n  --prospect         activa fases 0, 1, 2 antes del entrenamiento\n  --refine-epochs N  activa fase 4 con N epocas de annealing\n  Sin flags: solo fase 3 (comportamiento original, identico a antes)", "kind": "class", "line": 3446, "name": "TopoPhasePipeline", "signature": "class TopoPhasePipeline"}, {"kind": "method", "line": 3568, "name": "main", "signature": "def main()"}, {"kind": "method", "line": 161, "name": "__post_init__", "signature": "def __post_init__(self)"}, {"doc": "Producto de Hamilton q1 ⊗ q2. Ambos [..., 4].", "kind": "method", "line": 222, "name": "hamilton_product", "signature": "def hamilton_product(q1, q2)"}, {"kind": "method", "line": 234, "name": "normalize", "signature": "def normalize(q, eps)"}, {"kind": "method", "line": 238, "name": "conjugate", "signature": "def conjugate(q)"}, {"doc": "Rota vector 3D v por cuaternión unitario q. v:[...,3] q:[...,4]", "kind": "method", "line": 243, "name": "rotate_vector", "signature": "def rotate_vector(v, q)"}, {"kind": "method", "line": 265, "name": "__init__", "signature": "def __init__(self, in_features, out_features, bias)"}, {"doc": "x: [..., in_features] → [..., out_features]", "kind": "method", "line": 281, "name": "forward", "signature": "def forward(self, x)"}, {"kind": "method", "line": 318, "name": "__init__", "signature": "def __init__(self, in_q, out_q, grid_h, grid_w, init_scale)"}, {"kind": "method", "line": 337, "name": "_kernel", "signature": "def _kernel(self, c)"}, {"doc": "Suma sobre canales in_q: Y[b,o,h,w] = Σ_i W[i,o,h,w]·X[b,i,h,w]", "kind": "method", "line": 340, "name": "_contract", "signature": "def _contract(self, W, X)"}, {"doc": "x: [B, 4*in_q, H, W]  (4 canales cuaterniones sobre grid espacial)\n→ [B, 4*out_q, H, W]", "kind": "method", "line": 344, "name": "forward", "signature": "def forward(self, x)"}, {"kind": "method", "line": 398, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Filtro espectral 1D: x[..., D] → filtrado[..., D]", "kind": "method", "line": 430, "name": "_filter1d", "signature": "def _filter1d(self, x, kr, ki)"}, {"doc": "x: [..., D_MODEL] → latent: [..., D_LAT]", "kind": "method", "line": 436, "name": "encode", "signature": "def encode(self, x)"}, {"doc": "z: [..., D_LAT] → recon: [..., D_MODEL]", "kind": "method", "line": 441, "name": "decode", "signature": "def decode(self, z)"}, {"doc": "Devuelve (latent, recon_loss)", "kind": "method", "line": 446, "name": "forward", "signature": "def forward(self, x)"}, {"doc": "Procesa el grid del toro con QuaternionSpectralLayer.\ngrid: [B, 4*D_QUAT, RADIAL, ANGULAR]  →  [B, 4*D_QUAT, RADIAL, ANGULAR]", "kind": "method", "line": 453, "name": "process_torus_grid", "signature": "def process_torus_grid(self, grid)"}, {"kind": "method", "line": 486, "name": "__init__", "signature": "def __init__(self, d_model, config)"}, {"doc": "Construye las aristas del grafo toro 2×4.\n\nNodos indexados como: node = r * N_ANGULAR + a\n  r ∈ [0, RADIAL-1], a ∈ [0, ANGULAR-1]\n\nAristas angulares: nodo ↔ nodo a la izquierda/derecha (periódico)\nAristas radiales:  nodo ↔ nodo del anillo interior/exterior", "kind": "method", "line": 526, "name": "_build_torus_graph", "signature": "def _build_torus_graph(self)"}, {"doc": "Asignación blanda de tokens a los 8 nodos del toro via distancia circular.\n\nphi1: [BS] ángulo angular ∈ [-π, π]\nphi2: [BS] ángulo radial ∈ [-π, π]\n→ weights: [BS, N_NODES]  (suma a 1, softmax de distancias negativas)", "kind": "method", "line": 560, "name": "_torus_soft_assign", "signature": "def _torus_soft_assign(self, phi1, phi2)"}, {"doc": "Message-passing VECTORIZADO con rotaciones cuaterniones.\nSin bucles Python: todas las aristas se procesan en paralelo.\n\nnode_feat: [BS, N_NODES, D_MODEL]\n→ [BS, N_NODES, D_MODEL]", "kind": "method", "line": 587, "name": "_message_passing", "signature": "def _message_passing(self, node_feat)"}, {"doc": "x: [B, S, D_MODEL]\n→ output: [B, S, D_MODEL], recon_loss: scalar", "kind": "method", "line": 624, "name": "forward", "signature": "def forward(self, x)"}, {"kind": "method", "line": 697, "name": "__init__", "signature": "def __init__(self, d_head, max_seq_len, base)"}, {"kind": "method", "line": 703, "name": "_build_cache", "signature": "def _build_cache(self, seq_len)"}, {"kind": "method", "line": 711, "name": "_rotate_half", "signature": "def _rotate_half(self, x)"}, {"doc": "q, k: [B, n_heads, S_q/S_k, d_head]\noffset: posicion inicial (para KV cache: longitud del cache existente)\nAplica posiciones [offset .. offset+S-1] a q y k.", "kind": "method", "line": 715, "name": "forward", "signature": "def forward(self, q, k, seq_len, offset)"}, {"kind": "method", "line": 742, "name": "__init__", "signature": "def __init__(self, d_model, eps)"}, {"kind": "method", "line": 747, "name": "forward", "signature": "def forward(self, x)"}, {"kind": "method", "line": 763, "name": "__init__", "signature": "def __init__(self, d_model, expansion, dropout)"}, {"kind": "method", "line": 777, "name": "forward", "signature": "def forward(self, x)"}, {"kind": "method", "line": 800, "name": "__init__", "signature": "def __init__(self, d_model, config)"}, {"doc": "x: [N, D] donde N = B*S (tokens aplanados)\nRetorna:\nexpert_out: [N, D]  suma ponderada de top-K expertos\naux_loss:   escalar  load-balancing loss\nRouting vectorizado sin boolean indexing ni sincronizacion CUDA.\nUsa dispatch por indices agrupados (estilo Mixtral/DeepSeek) para\ncompatibilidad total con torch.utils.checkpoint.", "kind": "method", "line": 821, "name": "_route", "signature": "def _route(self, x)"}, {"doc": "x: [B, S, D]\n→ output: [B, S, D], aux_loss: escalar", "kind": "method", "line": 863, "name": "forward", "signature": "def forward(self, x)"}, {"kind": "method", "line": 900, "name": "__init__", "signature": "def __init__(self, d_model, n_heads, config)"}, {"doc": "Args:\n    x:        [B, S, D]\n    is_causal: usar mascara causal\n    past_kv:  (K_cache, V_cache) de pasos anteriores o None\nReturns:\n    out:      [B, S, D]\n    kv_cache: (K, V) completos para cachear en generate()", "kind": "method", "line": 919, "name": "forward", "signature": "def forward(self, x, is_causal, past_kv)"}, {"kind": "method", "line": 1003, "name": "__init__", "signature": "def __init__(self, d_model, n_heads, config)"}, {"kind": "method", "line": 1012, "name": "_forward_impl", "signature": "def _forward_impl(self, x, past_kv)"}, {"doc": "Retorna (x_out, aux_loss, kv_cache).\nCon gradient checkpointing en training (solo cuando no hay KV cache).", "kind": "method", "line": 1021, "name": "forward", "signature": "def forward(self, x, past_kv)"}, {"kind": "method", "line": 1052, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 1077, "name": "_init_weights", "signature": "def _init_weights(self)"}, {"doc": "token_ids: [B, S]  (enteros)\npast_kvs:  lista de (K, V) por capa, o None para entrenamiento\n→ logits: [B, S, VOCAB_SIZE], aux_loss: scalar, new_kvs: list[(K,V)]", "kind": "method", "line": 1084, "name": "forward", "signature": "def forward(self, token_ids, past_kvs)"}, {"doc": "Process long sequences with latent memory-token context compression.\n\nSplits `token_ids` [B, S] into segments of size MEMORY_SEGMENT_LEN.\nEach segment is processed with N_MEMORY_TOKENS prepended. The output\nat memory-token positions after segment k becomes the memory-state\ninput for segment k+1, compressing all prior context into a fixed-size\nlatent vector.\n\nReturns (logits [B, S, VOCAB_SIZE], aux_loss).", "kind": "method", "line": 1107, "name": "forward_with_memory", "signature": "def forward_with_memory(self, token_ids)"}, {"kind": "method", "line": 1157, "name": "count_params", "signature": "def count_params(self)"}, {"doc": "Autoregressive generation with KV cache and top-k sampling.\n\nArgs:\n    token_ids: [B, S_prompt] prompt tokens.\n    max_new_tokens: Maximum tokens to generate.\n    temperature: Sampling temperature (lower = more deterministic).\n    top_k: Top-k filtering (0 = disabled).\n    repetition_penalty: Penalty for repeating tokens (>1 = penalize).\n\nReturns:\n    [B, S_prompt + generated] full token sequence.", "kind": "method", "line": 1163, "name": "generate", "signature": "def generate(self, token_ids, max_new_tokens, temperature, top_k, repetition_penalty)"}, {"kind": "method", "line": 1214, "name": "generate_with_continuation", "signature": "def generate_with_continuation(self, token_ids, tokenizer, max_new_tokens, temperature, top_k, repetition_penalty, max_continuations, tail_lines)"}, {"kind": "method", "line": 1261, "name": "__init__", "signature": "def __init__(self, encoding)"}, {"kind": "method", "line": 1269, "name": "encode", "signature": "def encode(self, text)"}, {"kind": "method", "line": 1272, "name": "decode", "signature": "def decode(self, tokens)"}, {"kind": "method", "line": 1275, "name": "eot_token", "signature": "def eot_token(self)"}, {"kind": "method", "line": 1387, "name": "__init__", "signature": "def __init__(self, root, cache_dir, logger)"}, {"doc": "Walk directory tree collecting text file paths. Cached to disk.", "kind": "method", "line": 1394, "name": "scan", "signature": "def scan(self, force)"}, {"kind": "method", "line": 1461, "name": "__init__", "signature": "def __init__(self, cache_dir, logger)"}, {"doc": "Tokenize all files and return a memory-mapped numpy array.\n\nArgs:\n    file_paths: List of absolute file paths to tokenize.\n    tokenizer: BPE tokenizer instance.\n    cache_key: Unique key for caching tokens to disk.\n    max_tokens: Maximum number of tokens to produce.\n    min_chars: Skip files with fewer characters.\n\nReturns:\n    np.ndarray backed by a memmap on disk. Only accessed pages\n    are loaded into RAM by the OS virtual memory system.", "kind": "method", "line": 1466, "name": "tokenize", "signature": "def tokenize(self, file_paths, tokenizer, cache_key, max_tokens, min_chars)"}, {"kind": "method", "line": 1549, "name": "__init__", "signature": "def __init__(self, tokens, seq_len)"}, {"kind": "method", "line": 1554, "name": "__len__", "signature": "def __len__(self)"}, {"kind": "method", "line": 1557, "name": "__getitem__", "signature": "def __getitem__(self, idx)"}, {"kind": "method", "line": 1577, "name": "__init__", "signature": "def __init__(self, config, logger)"}, {"doc": "Shannon entropy of byte frequencies (bits per byte).", "kind": "method", "line": 1586, "name": "_compute_entropy", "signature": "def _compute_entropy(self, text)"}, {"doc": "Return True if any line exceeds threshold characters.", "kind": "method", "line": 1600, "name": "_has_long_lines", "signature": "def _has_long_lines(self, text, threshold)"}, {"doc": "Fraction of tokens that are pure whitespace or indentation-only.", "kind": "method", "line": 1607, "name": "_special_token_ratio", "signature": "def _special_token_ratio(self, text, tokenizer)"}, {"kind": "method", "line": 1621, "name": "_content_hash", "signature": "def _content_hash(self, text)"}, {"doc": "Read and evaluate a file. Returns text if passed, None if filtered.", "kind": "method", "line": 1624, "name": "filter_file", "signature": "def filter_file(self, path, tokenizer)"}, {"kind": "method", "line": 1664, "name": "report", "signature": "def report(self)"}, {"kind": "method", "line": 1685, "name": "__init__", "signature": "def __init__(self, tokens, seq_len, file_tiers, active_tier, logger)"}, {"kind": "method", "line": 1695, "name": "_update_len", "signature": "def _update_len(self)"}, {"kind": "method", "line": 1701, "name": "set_tier", "signature": "def set_tier(self, tier)"}, {"kind": "method", "line": 1705, "name": "__len__", "signature": "def __len__(self)"}, {"kind": "method", "line": 1708, "name": "__getitem__", "signature": "def __getitem__(self, idx)"}, {"kind": "method", "line": 1753, "name": "__init__", "signature": "def __init__(self, base_trainer)"}, {"kind": "method", "line": 1759, "name": "_build_dataloader", "signature": "def _build_dataloader(self, dataset, seq_len, batch_size, is_train)"}, {"doc": "Run training with progressive sequence length across phases.", "kind": "method", "line": 1769, "name": "run", "signature": "def run(self, train_paths, val_paths, tokenizer, file_tiers, phases)"}, {"kind": "method", "line": 1827, "name": "__init__", "signature": "def __init__(self, target_model, config, logger)"}, {"kind": "method", "line": 1835, "name": "_build_draft", "signature": "def _build_draft(self)"}, {"doc": "Autoregressive generation via speculative decoding.\n\nEach round: draft generates K tokens, target verifies all K in\none O(1) forward pass (longest context), then samples the first\nrejection from the target.", "kind": "method", "line": 1849, "name": "generate", "signature": "def generate(self, token_ids, max_new_tokens, temperature, top_k, repetition_penalty)"}, {"kind": "method", "line": 1940, "name": "__init__", "signature": "def __init__(self, embed, mode)"}, {"kind": "method", "line": 1969, "name": "forward", "signature": "def forward(self, indices)"}, {"kind": "method", "line": 2009, "name": "__init__", "signature": "def __init__(self, model, config, tokenizer)"}, {"kind": "method", "line": 2016, "name": "cache_tokens", "signature": "def cache_tokens(self, key, tokens)"}, {"kind": "method", "line": 2020, "name": "model", "signature": "def model(self)"}, {"kind": "method", "line": 2024, "name": "optimizer", "signature": "def optimizer(self)"}, {"kind": "method", "line": 2028, "name": "scaler", "signature": "def scaler(self)"}, {"kind": "method", "line": 2032, "name": "amp_dtype", "signature": "def amp_dtype(self)"}, {"kind": "method", "line": 2036, "name": "completed_epochs", "signature": "def completed_epochs(self)"}, {"kind": "method", "line": 2040, "name": "completed_epochs", "signature": "def completed_epochs(self, v)"}, {"kind": "method", "line": 2044, "name": "global_step", "signature": "def global_step(self)"}, {"kind": "method", "line": 2048, "name": "global_step", "signature": "def global_step(self, v)"}, {"kind": "method", "line": 2052, "name": "best_val_loss", "signature": "def best_val_loss(self)"}, {"kind": "method", "line": 2056, "name": "best_val_loss", "signature": "def best_val_loss(self, v)"}, {"kind": "method", "line": 2060, "name": "history", "signature": "def history(self)"}, {"kind": "method", "line": 2064, "name": "ckpt_mgr", "signature": "def ckpt_mgr(self)"}, {"kind": "method", "line": 2067, "name": "resume", "signature": "def resume(self)"}, {"kind": "method", "line": 2070, "name": "_current_state", "signature": "def _current_state(self)"}, {"kind": "method", "line": 2073, "name": "_cosine_lr", "signature": "def _cosine_lr(self)"}, {"kind": "method", "line": 2076, "name": "_set_lr", "signature": "def _set_lr(self)"}, {"kind": "method", "line": 2079, "name": "evaluate", "signature": "def evaluate(self, dataloader)"}, {"kind": "method", "line": 2082, "name": "_sample_text", "signature": "def _sample_text(self)"}, {"doc": "Training loop with progressive sequence length across phases.", "kind": "method", "line": 2085, "name": "_progressive_train", "signature": "def _progressive_train(self, train_paths, val_paths, tokenizer, phases, memtok)"}, {"kind": "method", "line": 2124, "name": "train", "signature": "def train(self, train_dl, val_dl)"}, {"doc": "Top-level entry point: curriculum + progressive seq len.", "kind": "method", "line": 2127, "name": "run_curriculum", "signature": "def run_curriculum(self, train_paths, val_paths, tokenizer, phases)"}, {"kind": "method", "line": 2178, "name": "__init__", "signature": "def __init__(self, config, logger)"}, {"doc": "Lee el checkpoint 'latest' y ajusta cfg.N_KV_HEADS / cfg.GQA_GROUPS\npara que coincidan con la arquitectura guardada.\nNecesario cuando el codigo cambio GQA despues de guardar el checkpoint.", "kind": "method", "line": 2188, "name": "patch_config_for_resume", "signature": "def patch_config_for_resume(self, cfg)"}, {"kind": "method", "line": 2217, "name": "_save_model", "signature": "def _save_model(self, model, directory)"}, {"kind": "method", "line": 2230, "name": "_load_model", "signature": "def _load_model(self, model, directory)"}, {"kind": "method", "line": 2261, "name": "_save_optimizer", "signature": "def _save_optimizer(self, optimizer, directory)"}, {"kind": "method", "line": 2264, "name": "_load_optimizer", "signature": "def _load_optimizer(self, optimizer, directory, device)"}, {"kind": "method", "line": 2273, "name": "_save_state", "signature": "def _save_state(self, state, directory)"}, {"kind": "method", "line": 2278, "name": "_load_state", "signature": "def _load_state(self, directory)"}, {"kind": "method", "line": 2289, "name": "should_save", "signature": "def should_save(self)"}, {"doc": "Guarda checkpoint completo.\n\nstate debe contener al menos: completed_epochs, global_step,\nbest_val_loss, history, config.", "kind": "method", "line": 2292, "name": "save", "signature": "def save(self, model, optimizer, state, is_best)"}, {"doc": "Carga el ultimo checkpoint guardado.\nDevuelve el state dict (vacio si no hay checkpoint).", "kind": "method", "line": 2337, "name": "load_latest", "signature": "def load_latest(self, model, optimizer)"}, {"doc": "Carga el mejor modelo guardado (solo pesos, sin optimizador).", "kind": "method", "line": 2364, "name": "load_best", "signature": "def load_best(self, model)"}, {"kind": "method", "line": 2376, "name": "has_checkpoint", "signature": "def has_checkpoint(self)"}, {"kind": "method", "line": 2398, "name": "__init__", "signature": "def __init__(self, model, config, tokenizer)"}, {"doc": "Carga el ultimo checkpoint disponible.\nRestaura: pesos del modelo, estado del optimizador, historial acumulado,\nepoch/step completados y mejor val_loss.\nDevuelve True si se cargo un checkpoint, False si empieza de cero.", "kind": "method", "line": 2433, "name": "resume", "signature": "def resume(self)"}, {"doc": "Construye el dict de estado para persistir en state.json.", "kind": "method", "line": 2458, "name": "_current_state", "signature": "def _current_state(self)"}, {"doc": "Cosine decay con warmup. El schedule es relativo a la sesion actual.", "kind": "method", "line": 2469, "name": "_cosine_lr", "signature": "def _cosine_lr(self, step_in_session, total_steps_session)"}, {"kind": "method", "line": 2477, "name": "_set_lr", "signature": "def _set_lr(self, lr)"}, {"doc": "Entrena cfg.EPOCHS epocas adicionales a partir de completed_epochs.\nEl historial se acumula sobre sesiones previas.", "kind": "method", "line": 2481, "name": "train", "signature": "def train(self, train_dl, val_dl)"}, {"doc": "Genera una muestra de texto al final de cada epoch para monitorear\nla calidad cualitativa del modelo (detecta degeneracion, repeticion, etc.).", "kind": "method", "line": 2617, "name": "_sample_text", "signature": "def _sample_text(self, tokenizer, prompts, max_new, temperature, top_k)"}, {"kind": "method", "line": 2649, "name": "evaluate", "signature": "def evaluate(self, dataloader)"}, {"kind": "method", "line": 2699, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 2707, "name": "compute_delta", "signature": "def compute_delta(self, model)"}, {"kind": "method", "line": 2714, "name": "compute_alpha", "signature": "def compute_alpha(self, delta)"}, {"doc": "Captura gradientes de forma segura, ignorando tensores corruptos.", "kind": "method", "line": 2719, "name": "update_grad_buffer", "signature": "def update_grad_buffer(self, model)"}, {"doc": "T_eff = lr/2 * Var(gradiente). Temperatura termodinamica efectiva.", "kind": "method", "line": 2745, "name": "compute_t_eff", "signature": "def compute_t_eff(self, lr)"}, {"doc": "κ = λ_max / λ_min de la covarianza del gradiente.\nParámetro de orden para cristalización (κ≈1 = cristal).\nNota: requiere pasadas backward adicionales. Se ejecuta con protección\npara no corromper el estado AMP del trainer principal.", "kind": "method", "line": 2753, "name": "compute_kappa", "signature": "def compute_kappa(self, model, dataloader, n_batches)"}, {"doc": "Fase de Berry de los kernels espectrales imaginarios.\nSurge de los parametros ki_w, ki_x, ki_y, ki_z de QuaternionSpectralLayer.\n|berry|>pi/2 con winding!=0 indica estructura topologica.", "kind": "method", "line": 2811, "name": "compute_berry_phase", "signature": "def compute_berry_phase(self, model)"}, {"doc": "Complejidad local: 1 - similitud coseno promedio entre filas de pesos.", "kind": "method", "line": 2824, "name": "compute_lc", "signature": "def compute_lc(self, model)"}, {"doc": "Superposicion: correlacion inter-fila promedio (entrelazamiento de features).", "kind": "method", "line": 2838, "name": "compute_sp", "signature": "def compute_sp(self, model)"}, {"doc": "Clasificacion de fase segun Book.md:\n\ndiscrete_crystal:       delta<0.05, kappa<1.5\ntopological_insulator:  |berry|>pi/2, winding!=0\ncold_glass:             kappa>>1, delta>0.3\nfunctional_glass:       intermedio (lo mas comun en LM)", "kind": "method", "line": 2854, "name": "classify_phase", "signature": "def classify_phase(self, delta, kappa, berry)"}, {"doc": "Calcula todas las metricas.\ncompute_kappa=True hace pasadas backward adicionales (caro, usar cada N epochs).", "kind": "method", "line": 2873, "name": "compute_all", "signature": "def compute_all(self, model, lr, dataloader, compute_kappa)"}, {"kind": "method", "line": 2898, "name": "format_log", "signature": "def format_log(self, m)"}, {"kind": "method", "line": 2934, "name": "__init__", "signature": "def __init__(self, config, logger)"}, {"doc": "Mide la coherencia espectral para un ratio dado.\nRetorna: varianza del gradiente (menor = mas coherente = mejor).", "kind": "method", "line": 2938, "name": "_measure_ratio", "signature": "def _measure_ratio(self, ratio, sample_batch)"}, {"doc": "Retorna el mejor ratio de inicializacion de kernels espectrales.", "kind": "method", "line": 2967, "name": "optimize", "signature": "def optimize(self, dataloader)"}, {"kind": "method", "line": 3007, "name": "__init__", "signature": "def __init__(self, config, logger)"}, {"doc": "Retorna el mejor batch size segun delta y T_eff.", "kind": "method", "line": 3011, "name": "prospect", "signature": "def prospect(self, candidates, train_dataset, prospect_steps)"}, {"kind": "method", "line": 3090, "name": "__init__", "signature": "def __init__(self, config, logger)"}, {"doc": "Retorna la semilla con la mejor trayectoria de delta.", "kind": "method", "line": 3094, "name": "mine", "signature": "def mine(self, seed_start, n_seeds, train_dataset, prospect_steps)"}, {"kind": "method", "line": 3176, "name": "__init__", "signature": "def __init__(self, trainer, t0, cooling_rate, stagnation_patience)"}, {"doc": "Ejecuta refine_epochs epocas de recocido simulado.\nRetorna el historial de refinamiento.", "kind": "method", "line": 3185, "name": "refine", "signature": "def refine(self, train_dl, val_dl, refine_epochs)"}, {"kind": "method", "line": 3328, "name": "__init__", "signature": "def __init__(self, config, train_tokens, val_tokens, tokenizer, logger, curriculum_tiers, progressive_seq)"}, {"kind": "method", "line": 3341, "name": "_build_dataloader", "signature": "def _build_dataloader(self, tokens, seq_len, batch_size, shuffle, tag)"}, {"kind": "method", "line": 3355, "name": "_build_phases", "signature": "def _build_phases(self)"}, {"kind": "method", "line": 3364, "name": "run", "signature": "def run(self, run_prospect, refine_epochs, resume, prospect_steps, probe_seeds, seed_start)"}, {"kind": "method", "line": 3466, "name": "__init__", "signature": "def __init__(self, config, train_dataset, val_dataset, tokenizer, logger)"}, {"kind": "method", "line": 3476, "name": "_make_dataloaders", "signature": "def _make_dataloaders(self, batch_size)"}, {"doc": "Ejecuta el pipeline completo.\nRetorna el trainer con el modelo entrenado.", "kind": "method", "line": 3488, "name": "run", "signature": "def run(self, run_prospect, refine_epochs, resume, prospect_steps, probe_seeds, seed_start)"}, {"kind": "method", "line": 1029, "name": "ckpt_fn", "signature": "def ckpt_fn(x_in)"}]}, {"id": "topogpt3/train.py", "kind": "module", "label": "train.py", "language": "py", "sha256": "e60ba0317cdc3212", "symbol_count": 62, "symbols": [{"doc": "Configuracion del pipeline TopoGPT3 (Grassmanniana + curriculum).", "kind": "class", "line": 83, "name": "TopoGPT3Config", "signature": "class TopoGPT3Config"}, {"doc": "Observables geometricos sobre la trayectoria SGD.\n\nEn cada snapshot:\n  - Apila los kernels espectrales (kr_*, ki_*) del modelo en\n    K(theta) en C^{N_f x N_c}.\n  - SVD truncada -> U_r(theta) en St(r,N).\n  - Rango r dinamico por elbow de los valores singulares.\n  - Gap funcional Delta_F estimado por covarianza de gradientes\n    muestrales (proxy de la matriz de Fisher).\n  - Conexion de Berry discreta entre snapshots consecutivos:\n       A_n = i * U_n^dagger (U_{n+1} - U_n)\n    Holonomia acumulada U_Gamma = P prod_n exp(-i A_n) en U(r).\n  - Distancia de conjugacion en SU(2) (r=1 efectivo cuaternionico).\n  - Winding W como proxy barato.\n\nTodos los calculos viven en CPU/float32 para no contaminar AMP.", "kind": "class", "line": 197, "name": "GrassmannianTracker", "signature": "class GrassmannianTracker"}, {"doc": "Sustituye QuaternionSpectralLayer._contract usando el truco de Gauss.\n\nPara (Wr + i Wi)(Xr + i Xi) la version naive requiere 4 productos reales:\n    Yr = Wr Xr - Wi Xi\n    Yi = Wr Xi + Wi Xr\nGauss (Karatsuba) baja a 3 productos reales:\n    m1 = Wr * Xr\n    m2 = Wi * Xi\n    m3 = (Wr + Wi) * (Xr + Xi)\n    Yr = m1 - m2\n    Yi = m3 - m1 - m2\n\nImportante (AMP): el _contract original opera sobre complex64 y PyTorch no\nautocastea operaciones complejas; el resultado es complex64. Si dejamos que\nautocast convierta nuestros einsums reales a fp16, la dtype de salida cambia\ny rompe el scatter_add_ corriente abajo en QuaternionTorusBrain. Por eso\ndesactivamos autocast aqui y forzamos fp32 para preservar la semantica.", "kind": "method", "line": 532, "name": "_gauss_complex_contract", "signature": "def _gauss_complex_contract(self, W, X)"}, {"doc": "Activa la version Gauss de _contract en QuaternionSpectralLayer.\nIdempotente: solo parchea una vez por proceso.", "kind": "method", "line": 568, "name": "apply_gauss_patch", "signature": "def apply_gauss_patch(logger)"}, {"doc": "Mide y calcula los tres ratios pedidos:\n\n  perf_per_param  =  (1 / val_ppl) / params_M\n  perf_per_FLOP   =  tokens_per_sec / FLOPs_per_sec_aprox\n  perf_per_BW     =  tokens_per_sec / bytes_moved_per_sec_aprox\n\nFLOPs estimados con la heuristica de Kaplan/Hoffmann:\n    FLOPs_forward_per_token ~= 2 * N_no_embed\n    FLOPs_total_per_token  ~= 6 * N_no_embed       (forward + backward)\nBandwidth estimada como params_bytes leidos + activations_bytes movidas por step.\ntokens_per_sec se cronometra empiricamente sobre el dataloader.", "kind": "class", "line": 585, "name": "EfficiencyMetrics", "signature": "class EfficiencyMetrics"}, {"doc": "    Carga los 4 datasets, normaliza cada ejemplo a una unica cadena de texto,\n    tokeniza con BPE y produce splits train / val / holdout disjuntos.\n\n    Politica de normalizacion por dataset:\n      - CodeAlpaca:           \"### Instruction\n{i}\n### Input\n{x}\n### Response\n{o}\"\n      - Code-Feedback:        concat de turnos: \"<usr> ... </usr>\n<asst> ... </asst>\"\n      - Magicoder-Evol:       \"### Problem\n{p}\n### Solution\n{s}\"\n      - Tiny-The-Stack:       texto crudo del archivo (truncado a 32k chars/file)\n\n    Cache en disco: tokens_{tier}_{split}.bin (int32 memmap) + manifest .json.\n    El HOLDOUT se separa con seed fija antes de tokenizar para garantizar\n    que la misma muestra nunca aparezca en train o val entre corridas.\n    ", "kind": "class", "line": 713, "name": "CodeCurriculumLoader", "signature": "class CodeCurriculumLoader"}, {"doc": "Dataset autoregresivo sobre un stream de tokens.\nCada item es (x, y) con shape [seq_len].", "kind": "class", "line": 1000, "name": "BlockTokenDataset", "signature": "class BlockTokenDataset(Dataset)"}, {"doc": "Persiste pesos del modelo + estado del trainer (sin AMP scaler para portabilidad).", "kind": "class", "line": 1027, "name": "CheckpointStore", "signature": "class CheckpointStore"}, {"doc": "Orquesta el curriculum sobre los 4 tiers.\n\nPipeline por tier:\n  1. Abre memmap de tokens (train/val/holdout).\n  2. Construye DataLoaders con seq_len(tier).\n  3. Entrena TIER_EPOCHS[tier] epocas con AMP + grad accum.\n  4. Cada GRASS_TRACK_EVERY steps: snapshot Grassmanniano.\n  5. Al final de cada epoca: eval en VAL.\n  6. Al final del tier: eval en HOLDOUT (datos nunca vistos).\n  7. Checkpoint y avanza al siguiente tier.\n\nAl final del pipeline: eval en HOLDOUT *combinado* de los 4 tiers.", "kind": "class", "line": 1103, "name": "TopoGPT3Trainer", "signature": "class TopoGPT3Trainer"}, {"kind": "method", "line": 1538, "name": "parse_args", "signature": "def parse_args()"}, {"kind": "method", "line": 1567, "name": "main", "signature": "def main()"}, {"kind": "method", "line": 170, "name": "build_topogpt2_config", "signature": "def build_topogpt2_config(self, max_seq_len, attn_window)"}, {"kind": "method", "line": 217, "name": "__init__", "signature": "def __init__(self, config, logger)"}, {"doc": "Devuelve K(theta) en C^{N_f x N_c}:\n  - filas = frecuencias planas (todos los modos espaciales de todos los kernels)\n  - columnas = canales (in_q * out_q por componente cuaternionico, sumados)", "kind": "method", "line": 231, "name": "_stack_spectral_kernels", "signature": "def _stack_spectral_kernels(model)"}, {"doc": "Punto donde el valor singular cae por debajo de elbow_ratio * sigma_max.", "kind": "method", "line": 268, "name": "_elbow_rank", "signature": "def _elbow_rank(self, sigmas)"}, {"doc": "SVD compacta y truncada.\nDevuelve (U_r, sigmas, r) con U_r en C^{N_f x r} ortonormal.", "kind": "method", "line": 277, "name": "_dominant_subspace", "signature": "def _dominant_subspace(self, K)"}, {"doc": "Concatena un sub-sample de gradientes para mantener costo acotado.", "kind": "method", "line": 295, "name": "_flatten_grads", "signature": "def _flatten_grads(model, max_per_tensor)"}, {"doc": "Sigma_F ~= (1/M) sum_m g_m g_m^T  (covarianza muestral de gradientes).\nDelta_F = lambda_{r_eff} - lambda_{r_eff+1}, donde r_eff = min(r_target, M-2)\npara no salir del rango efectivo del estimador con M gradientes.\nDevuelve (gap, eigs_desc, r_eff).", "kind": "method", "line": 313, "name": "estimate_fisher_gap", "signature": "def estimate_fisher_gap(self, model, dataloader, vocab_size, r_target)"}, {"doc": "Proyeccion a U(r) por descomposicion polar (M ~= U H -> retorna U).", "kind": "method", "line": 381, "name": "_project_unitary", "signature": "def _project_unitary(M)"}, {"doc": "Holonomia discreta:\n    T_n = U_n^dagger U_{n+1}  en C^{r x r}  (transporte paralelo discreto)\n    U_Gamma <- T_n * U_Gamma  (acumulado)\nTras cada paso, U_Gamma se proyecta a U(r) para evitar deriva numerica.", "kind": "method", "line": 386, "name": "update_holonomy", "signature": "def update_holonomy(self, U_new)"}, {"doc": "Para U1, U2 en U(1)/U(2):  d_conj(U1, U2) = min_g || U1 - g U2 g^{-1} ||_F.\nEn U(1) coincide con |U1 - U2|.\nEn SU(2) se reduce a comparar |Tr(U1)| con |Tr(U2)| (clase de conjugacion).", "kind": "method", "line": 412, "name": "conjugation_distance_su2", "signature": "def conjugation_distance_su2(U1, U2)"}, {"doc": "W += (1/2pi) * arg det <U_prev | U_new>  acumulado sobre la trayectoria.", "kind": "method", "line": 429, "name": "_accumulate_winding", "signature": "def _accumulate_winding(self, U_new)"}, {"kind": "method", "line": 445, "name": "snapshot", "signature": "def snapshot(self, model, step, dataloader, vocab_size)"}, {"kind": "method", "line": 500, "name": "format_log", "signature": "def format_log(self, snap)"}, {"kind": "method", "line": 522, "name": "save", "signature": "def save(self, path)"}, {"kind": "method", "line": 600, "name": "__init__", "signature": "def __init__(self, model, config, logger, gauss_enabled)"}, {"kind": "method", "line": 611, "name": "_embed_params", "signature": "def _embed_params(model)"}, {"doc": "Devuelve (tokens_por_segundo, segundos_por_step).", "kind": "method", "line": 619, "name": "measure_throughput", "signature": "def measure_throughput(self, dataloader, vocab_size)"}, {"doc": "Heuristica: 6 * N_no_embed * tokens (forward + backward).", "kind": "method", "line": 651, "name": "estimate_flops_per_step", "signature": "def estimate_flops_per_step(self, batch_size, seq_len)"}, {"doc": "Bandwidth aproximada: lectura de pesos + activaciones por step.\nAsume AMP fp16 (2 bytes); pesos fp32 (4 bytes) leidos una vez.", "kind": "method", "line": 656, "name": "estimate_bytes_per_step", "signature": "def estimate_bytes_per_step(self, batch_size, seq_len, dtype_bytes)"}, {"kind": "method", "line": 664, "name": "compute", "signature": "def compute(self, dataloader, vocab_size, val_loss, val_ppl, val_acc, batch_size, seq_len)"}, {"kind": "method", "line": 696, "name": "format_log", "signature": "def format_log(self, m)"}, {"kind": "method", "line": 729, "name": "__init__", "signature": "def __init__(self, config, tokenizer, logger)"}, {"kind": "method", "line": 746, "name": "_format_codealpaca", "signature": "def _format_codealpaca(ex)"}, {"kind": "method", "line": 757, "name": "_format_code_feedback", "signature": "def _format_code_feedback(ex)"}, {"kind": "method", "line": 777, "name": "_format_magicoder", "signature": "def _format_magicoder(ex)"}, {"kind": "method", "line": 785, "name": "_format_tiny_stack", "signature": "def _format_tiny_stack(ex)"}, {"kind": "method", "line": 797, "name": "_get_formatter", "signature": "def _get_formatter(cls, tier)"}, {"kind": "method", "line": 819, "name": "_tier_paths", "signature": "def _tier_paths(self, tier)"}, {"kind": "method", "line": 825, "name": "_manifest_path", "signature": "def _manifest_path(self, tier)"}, {"doc": "True solo si los 3 splits existen, son no-vacios y el manifest concuerda.", "kind": "method", "line": 828, "name": "_already_prepared", "signature": "def _already_prepared(self, tier)"}, {"doc": "Carga el dataset HF; para tiny_the_stack prueba una cadena de fallbacks\npublicos hasta que uno funcione.", "kind": "method", "line": 858, "name": "_load_hf_with_fallback", "signature": "def _load_hf_with_fallback(self, tier)"}, {"kind": "method", "line": 891, "name": "prepare_tier", "signature": "def prepare_tier(self, tier_index, force)"}, {"kind": "method", "line": 986, "name": "open_memmap", "signature": "def open_memmap(self, tier, split)"}, {"kind": "method", "line": 1006, "name": "__init__", "signature": "def __init__(self, tokens, seq_len)"}, {"kind": "method", "line": 1011, "name": "__len__", "signature": "def __len__(self)"}, {"kind": "method", "line": 1014, "name": "__getitem__", "signature": "def __getitem__(self, idx)"}, {"kind": "method", "line": 1030, "name": "__init__", "signature": "def __init__(self, root, max_keep, logger)"}, {"doc": "Guarda checkpoint atomico en <root>/last/ sobreescribiendo el anterior.\n\nEl argumento `tag` se conserva por compatibilidad pero se ignora: solo\nexiste un checkpoint llamado `last` y los pesos en safetensors.", "kind": "method", "line": 1037, "name": "save", "signature": "def save(self, tag, model, optimizer, state)"}, {"kind": "method", "line": 1071, "name": "load_latest", "signature": "def load_latest(self, model, optimizer)"}, {"kind": "method", "line": 1095, "name": "should_save", "signature": "def should_save(self, interval_min)"}, {"kind": "method", "line": 1119, "name": "__init__", "signature": "def __init__(self, config, start_tier)"}, {"doc": "Prepara cada tier; un fallo en uno no detiene los demas.", "kind": "method", "line": 1174, "name": "prepare_all", "signature": "def prepare_all(self, force)"}, {"kind": "method", "line": 1190, "name": "_build_loaders", "signature": "def _build_loaders(self, tier_index)"}, {"kind": "method", "line": 1222, "name": "_cosine_lr", "signature": "def _cosine_lr(self, step, total_steps)"}, {"kind": "method", "line": 1229, "name": "_set_lr", "signature": "def _set_lr(self, lr)"}, {"kind": "method", "line": 1237, "name": "_train_one_tier", "signature": "def _train_one_tier(self, tier_index)"}, {"doc": "Devuelve (avg_loss, perplexity, token_accuracy).", "kind": "method", "line": 1398, "name": "_evaluate", "signature": "def _evaluate(self, dl)"}, {"kind": "method", "line": 1436, "name": "_state_dict", "signature": "def _state_dict(self)"}, {"kind": "method", "line": 1449, "name": "run", "signature": "def run(self)"}, {"kind": "method", "line": 1506, "name": "_eval_combined_holdout", "signature": "def _eval_combined_holdout(self)"}, {"kind": "method", "line": 922, "name": "flush", "signature": "def flush(split)"}]}, {"id": "topogpt3.c", "kind": "module", "label": "topogpt3.c", "language": "c", "sha256": "0d10689ae4344eff", "symbol_count": 99, "symbols": [{"kind": "function", "line": 113, "name": "tg_exp", "signature": "static float tg_exp(float x)"}, {"kind": "function", "line": 127, "name": "tg_tanh", "signature": "static float tg_tanh(float x)"}, {"kind": "function", "line": 134, "name": "tg_sin", "signature": "static float tg_sin(float x)"}, {"kind": "function", "line": 143, "name": "tg_cos", "signature": "static float tg_cos(float x)"}, {"kind": "function", "line": 147, "name": "tg_fabs", "signature": "static float tg_fabs(float x)"}, {"kind": "function", "line": 151, "name": "tg_log", "signature": "static float tg_log(float x)"}, {"kind": "function", "line": 163, "name": "tg_fmax", "signature": "static float tg_fmax(float a, float b)"}, {"kind": "function", "line": 167, "name": "tg_fmin", "signature": "static float tg_fmin(float a, float b)"}, {"kind": "function", "line": 254, "name": "load_vocab", "signature": "static void load_vocab(const char *path)"}, {"doc": "====================================================================== SECTION 4: TORUS GRAPH BUILDER * ======================================================================", "kind": "function", "line": 295, "name": "build_torus_graph", "signature": "static void build_torus_graph(void)"}, {"doc": "====================================================================== SECTION 5: ROPE PRECOMPUTATION * ======================================================================", "kind": "function", "line": 326, "name": "precompute_rope", "signature": "static void precompute_rope(void)"}, {"doc": "====================================================================== SECTION 6: MATRIX OPERATIONS * ======================================================================", "kind": "function", "line": 358, "name": "matvec", "signature": "static void matvec(const float *W, const float *x, float *y, int rows, int cols)"}, {"kind": "function", "line": 369, "name": "matvec_bias", "signature": "static void matvec_bias(const float *W, const float *b, const float *x, float *y,\n               ..."}, {"kind": "function", "line": 381, "name": "rmsnorm", "signature": "static void rmsnorm(const float *x, const float *w, float *y, int d)"}, {"kind": "function", "line": 390, "name": "softmax", "signature": "static void softmax(float *x, int n)"}, {"kind": "function", "line": 399, "name": "gelu", "signature": "static void gelu(float *x, int n)"}, {"kind": "function", "line": 409, "name": "silu", "signature": "static void silu(float *x, int n)"}, {"kind": "function", "line": 417, "name": "swiglu", "signature": "static void swiglu(const float *gate_w, const float *up_w, const float *down_w,\n                 ..."}, {"doc": "====================================================================== SECTION 7: QUATERNION OPERATIONS * ======================================================================", "kind": "function", "line": 434, "name": "quat_normalize", "signature": "static void quat_normalize(float *q)"}, {"kind": "function", "line": 439, "name": "quat_hamilton", "signature": "static void quat_hamilton(const float *a, const float *b, float *c)"}, {"doc": "static void quat_normalize(float *q) { float n = tg_sqrt(q[0]*q[0] + q[1]*q[1] + q[2]*q[2] + q[3]*q[3]); if (n > 1e-8f) { q[0]/=n; q[1]/=n; q[2]/=n; q[3]/=n; } } static void quat_hamilton(const float *a, const float *b, float *c) { c[0] = a[0]*b[0] - a[1]*b[1] - a[2]*b[2] - a[3]*b[3]; c[1] = a[0]*b[1] + a[1]*b[0] + a[2]*b[3] - a[3]*b[2]; c[2] = a[0]*b[2] - a[1]*b[3] + a[2]*b[0] + a[3]*b[1]; c[3] = a[0]*b[3] + a[1]*b[2] - a[2]*b[1] + a[3]*b[0]; } /* QuaternionLinear: x[w,x,y,z] -> y[w,x,y,z]", "kind": "function", "line": 448, "name": "quat_linear", "signature": "static void quat_linear(const float *Ww, const float *Wx, const float *Wy, const float *Wz,\n     ..."}, {"kind": "function", "line": 504, "name": "ifft_radix2", "signature": "static void ifft_radix2(float *real, float *imag, int n)"}, {"doc": "cur_r = nr; } } } } static void ifft_radix2(float *real, float *imag, int n) { int i; for (i = 0; i < n; i++) imag[i] = -imag[i]; fft_radix2(real, imag, n); for (i = 0; i < n; i++) { real[i] /= (float)n; imag[i] = -imag[i] / (float)n; } } /* Real FFT: x[n] -> X[n/2+1] complex", "kind": "function", "line": 513, "name": "rfft", "signature": "static void rfft(const float *x, float *Xr, float *Xi, int n)"}, {"doc": "fft_radix2(real, imag, n); for (i = 0; i < n; i++) { real[i] /= (float)n; imag[i] = -imag[i] / (float)n; } } /* Real FFT: x[n] -> X[n/2+1] complex static void rfft(const float *x, float *Xr, float *Xi, int n) { float re[n], im[n]; int i; for (i = 0; i < n; i++) { re[i] = x[i]; im[i] = 0.0f; } fft_radix2(re, im, n); for (i = 0; i <= n/2; i++) { Xr[i] = re[i]; Xi[i] = im[i]; } } /* Inverse real FFT: X[n/2+1] complex -> x[n]", "kind": "function", "line": 522, "name": "irfft", "signature": "static void irfft(const float *Xr, const float *Xi, float *x, int n)"}, {"doc": "====================================================================== SECTION 9: SPECTRAL 1D FILTER * ======================================================================", "kind": "function", "line": 536, "name": "filter1d", "signature": "static void filter1d(const float *x, const float *kr, const float *ki,\n                      floa..."}, {"kind": "function", "line": 579, "name": "ifft2d", "signature": "static void ifft2d(float *data_r, float *data_i, int h, int w)"}, {"doc": "ifft_radix2(row_re, row_im, w); for (c = 0; c < w; c++) { re[r*w+c] = row_re[c]; im[r*w+c] = row_im[c]; } } /* IFFT columns float col_re[h], col_im[h]; for (c = 0; c < w; c++) { for (r = 0; r < h; r++) { col_re[r] = re[r*w+c]; col_im[r] = im[r*w+c]; } ifft_radix2(col_re, col_im, h); for (r = 0; r < h; r++) { re[r*w+c] = col_re[r]; im[r*w+c] = col_im[r]; } } for (i = 0; i < h * w; i++) { data_r[i] = re[i]; data_i[i] = im[i]; } } /* RFFT2: 2D real FFT, output is [h][w/2+1] complex", "kind": "function", "line": 602, "name": "rfft2d_real", "signature": "static void rfft2d_real(const float *data, float *out_r, float *out_i,\n                         i..."}, {"doc": "for (r = 0; r < h; r++) { col_re[r] = re[r*w+c]; col_im[r] = im[r*w+c]; } fft_radix2(col_re, col_im, h); for (r = 0; r < h; r++) { re[r*w+c] = col_re[r]; im[r*w+c] = col_im[r]; } } int fw = w / 2 + 1; for (r = 0; r < h; r++) { for (c = 0; c < fw; c++) { out_r[r * fw + c] = re[r * w + c]; out_i[r * fw + c] = im[r * w + c]; } } } /* IRFFT2: inverse of rfft2d_real", "kind": "function", "line": 629, "name": "irfft2d", "signature": "static void irfft2d(const float *in_r, const float *in_i, float *out,\n                     int h,..."}, {"doc": "====================================================================== SECTION 11: QUATERNION SPECTRAL LAYER 2D * ====================================================================== /* Complex multiply: (ar+bi)(cr+di) = (ac-bd)+(ad+bc)i", "kind": "function", "line": 664, "name": "cmul", "signature": "static void cmul(float ar, float ai, float cr, float di, float *rr, float *ri)"}, {"doc": "====================================================================== SECTION 11: QUATERNION SPECTRAL LAYER 2D * ====================================================================== /* Complex multiply: (ar+bi)(cr+di) = (ac-bd)+(ad+bc)i static void cmul(float ar, float ai, float cr, float di, float *rr, float *ri) { rr = ar*cr - ai*di; ri = ar*di + ai*cr; } /* Contract: Y[o,h,w] = sum_i W[i,o,h,w] * X[b,i,h,w] (complex)", "kind": "function", "line": 670, "name": "spectral_contract", "signature": "static void spectral_contract(const float *Wr, const float *Wi,\n                               co..."}, {"kind": "function", "line": 694, "name": "quat_spectral_layer_2d", "signature": "static void quat_spectral_layer_2d(\n    const float *x, float *y,\n    const float *kr_w, const fl..."}, {"doc": "====================================================================== SECTION 12: SPECTRAL AUTOENCODER FORWARD * ======================================================================", "kind": "function", "line": 784, "name": "spectral_ae_encode", "signature": "static void spectral_ae_encode(const float *x, float *z, const LayerWeights *lw)"}, {"kind": "function", "line": 792, "name": "spectral_ae_decode", "signature": "static void spectral_ae_decode(const float *z, float *x, const LayerWeights *lw)"}, {"kind": "function", "line": 799, "name": "process_torus_grid", "signature": "static void process_torus_grid(const float *grid, float *out, const LayerWeights *lw)"}, {"doc": "====================================================================== SECTION 13: TORUS BRAIN FORWARD * ======================================================================", "kind": "function", "line": 820, "name": "torus_soft_assign", "signature": "static void torus_soft_assign(const float *phi1, const float *phi2,\n                             ..."}, {"kind": "function", "line": 842, "name": "message_passing", "signature": "static void message_passing(const float *node_feat, float *out,\n                             cons..."}, {"kind": "function", "line": 887, "name": "torus_brain_forward", "signature": "static void torus_brain_forward(const float *x, float *out, float *recon_loss,\n                  ..."}, {"doc": "====================================================================== SECTION 14: ATTENTION FORWARD * ======================================================================", "kind": "function", "line": 977, "name": "attention_forward", "signature": "static void attention_forward(const float *x, float *out, int layer_idx, int pos, int total_kv_co..."}, {"doc": "====================================================================== SECTION 15: MoE ROUTING * ======================================================================", "kind": "function", "line": 1077, "name": "moe_forward", "signature": "static void moe_forward(const float *x, float *out, const LayerWeights *lw)"}, {"doc": "====================================================================== SECTION 16: FULL MODEL FORWARD  Processes tokens autoregressively through all layers. Each token position goes through ALL layers before the next position. This is the correct order: layer 0 must see all positions before layer 1 can process them.  After processing, logits_out holds logits for the LAST position only. * ======================================================================", "kind": "function", "line": 1127, "name": "forward", "signature": "static void forward(const int *token_ids, int seq_len, float *logits_out)"}, {"kind": "function", "line": 1194, "name": "tokenize_string", "signature": "static int tokenize_string(const char *text, int *tokens, int max_tokens)"}, {"doc": "====================================================================== SECTION 18: SAMPLING * ======================================================================", "kind": "function", "line": 1209, "name": "apply_temperature", "signature": "static void apply_temperature(float *logits, int n, float temp)"}, {"kind": "function", "line": 1215, "name": "apply_repetition_penalty", "signature": "static void apply_repetition_penalty(float *logits, int n, const int *tokens,\n                   ..."}, {"kind": "function", "line": 1228, "name": "apply_top_k", "signature": "static void apply_top_k(float *logits, int n, int k)"}, {"kind": "function", "line": 1247, "name": "sample", "signature": "static int sample(const float *logits, int n)"}, {"doc": "====================================================================== SECTION 19: WEIGHT LOADER  Reads the binary file produced by convert_weights.py. The converter writes tensors in a fixed order. We read them in the same order, matching each to its destination buffer by position. No string parsing needed. * ======================================================================", "kind": "function", "line": 1281, "name": "load_weights", "signature": "static int load_weights(const char *path)"}, {"kind": "function", "line": 1451, "name": "load_weights_fp16", "signature": "static int load_weights_fp16(const char *path)"}, {"doc": "printf(\"  Layer %d loaded\\n\", i); } READ_TENSOR16(W.final_norm, D_MODEL); #undef SKIP_TENSOR16 #undef READ_TENSOR16 fclose(f); printf(\"Weights loaded successfully (fp16).\\n\"); return 0; } /* Auto-detect format and load weights", "kind": "function", "line": 1583, "name": "load_weights_auto", "signature": "static int load_weights_auto(const char *path)"}, {"doc": "====================================================================== SECTION 20: TIMING * ====================================================================== /* Portable wall-clock timer using rdtsc where available, else microseconds", "kind": "function", "line": 1600, "name": "time_now_ms", "signature": "static double time_now_ms(void)"}, {"doc": "====================================================================== SECTION 21: GENERATION * ======================================================================", "kind": "function", "line": 1613, "name": "decode_token", "signature": "static void decode_token(int tid)"}, {"doc": "if (tid < 256) { /* Map GPT-2 byte-level encoding back to original byte int n = tid; if (n < 94) n += 33; else if (n < 163) n += 161 - 94; else n += 173 - 163; putchar(n); } else { /* Multi-byte token: output placeholder or skip putchar('?'); } } /* Load pre-tokenized binary file (format: \"TKID\" + uint32 count + int32 ids[])", "kind": "function", "line": 1629, "name": "load_token_file", "signature": "static int load_token_file(const char *path, int *out_ids, int max_ids)"}, {"doc": "if (fread(&n, 4, 1, f) != 1) { fclose(f); return 0; } if (n > (unsigned)max_ids) n = max_ids; int count = (int)n; int i; for (i = 0; i < count; i++) { int id; if (fread(&id, 4, 1, f) != 1) break; out_ids[i] = id; } fclose(f); return count; } /* Decode token ID using loaded vocabulary", "kind": "function", "line": 1652, "name": "decode_token_tiktoken", "signature": "static void decode_token_tiktoken(int tid)"}, {"kind": "function", "line": 1660, "name": "generate_tokens", "signature": "static void generate_tokens(int *prompt_tokens, int n_prompt, int max_new_tokens,\n               ..."}, {"kind": "function", "line": 1724, "name": "generate", "signature": "static void generate(const char *prompt, int max_new_tokens, float temperature,\n                 ..."}, {"doc": "====================================================================== SECTION 22: INTERACTIVE MODE * ======================================================================", "kind": "function", "line": 1735, "name": "interactive_mode", "signature": "static void interactive_mode(void)"}, {"doc": "====================================================================== SECTION 23: HELP AND MAIN * ======================================================================", "kind": "function", "line": 1849, "name": "print_help", "signature": "static void print_help(void)"}, {"kind": "function", "line": 1884, "name": "main", "signature": "int main(int argc, char **argv)"}, {"kind": "macro", "line": 43, "name": "NULL"}, {"kind": "macro", "line": 44, "name": "SEEK_SET"}, {"kind": "macro", "line": 45, "name": "SEEK_CUR"}, {"kind": "macro", "line": 46, "name": "SEEK_END"}, {"kind": "macro", "line": 64, "name": "VOCAB_SIZE"}, {"kind": "macro", "line": 66, "name": "D_MODEL"}, {"kind": "macro", "line": 67, "name": "N_HEADS"}, {"kind": "macro", "line": 68, "name": "N_KV_HEADS"}, {"kind": "macro", "line": 69, "name": "GQA_GROUPS"}, {"kind": "macro", "line": 70, "name": "D_HEAD"}, {"kind": "macro", "line": 71, "name": "D_QUAT"}, {"kind": "macro", "line": 72, "name": "N_LAYERS"}, {"kind": "macro", "line": 73, "name": "MAX_SEQ_LEN"}, {"kind": "macro", "line": 74, "name": "N_EXPERTS"}, {"kind": "macro", "line": 75, "name": "MOE_TOP_K"}, {"kind": "macro", "line": 76, "name": "N_NODES"}, {"kind": "macro", "line": 77, "name": "N_RADIAL"}, {"kind": "macro", "line": 78, "name": "N_ANGULAR"}, {"kind": "macro", "line": 79, "name": "N_EDGE_TYPES"}, {"kind": "macro", "line": 80, "name": "N_EDGES"}, {"kind": "macro", "line": 81, "name": "SPECTRAL_LATENT_DIM"}, {"kind": "macro", "line": 82, "name": "D_LAT_Q"}, {"kind": "macro", "line": 83, "name": "TORUS_GRID_H"}, {"kind": "macro", "line": 84, "name": "TORUS_GRID_W"}, {"kind": "macro", "line": 85, "name": "FREQ_W"}, {"kind": "macro", "line": 86, "name": "N_SPECTRAL_LAYERS"}, {"kind": "macro", "line": 87, "name": "EXPERT_INNER"}, {"kind": "macro", "line": 88, "name": "READOUT_INNER"}, {"kind": "macro", "line": 89, "name": "EOS_TOKEN"}, {"kind": "macro", "line": 90, "name": "EMBED_INNER"}, {"kind": "macro", "line": 91, "name": "PI"}, {"kind": "macro", "line": 92, "name": "EPS_RMS"}, {"kind": "macro", "line": 93, "name": "TORUS_TEMP"}, {"kind": "macro", "line": 94, "name": "MAX_TOKENS"}, {"kind": "macro", "line": 95, "name": "MAX_PROMPT_LEN"}, {"kind": "macro", "line": 96, "name": "MAX_LINE"}, {"kind": "macro", "line": 97, "name": "TOK_TAB_SIZE"}, {"kind": "macro", "line": 98, "name": "TOK_VOCAB_SIZE"}, {"kind": "macro", "line": 1300, "name": "SKIP_TENSOR"}, {"kind": "macro", "line": 1310, "name": "READ_TENSOR"}, {"kind": "macro", "line": 1470, "name": "SKIP_TENSOR16"}, {"kind": "macro", "line": 1480, "name": "READ_TENSOR16"}]}], "type": "CodePropertyGraph", "version": "1.0"}
```

---

## Architecture Reference

### C (1 files)

#### `topogpt3.c`
**Path:** `topogpt3.c`

**Functions:**
- `tg_exp` (line 113) `static float tg_exp(float x)`
- `tg_tanh` (line 127) `static float tg_tanh(float x)`
- `tg_sin` (line 134) `static float tg_sin(float x)`
- `tg_cos` (line 143) `static float tg_cos(float x)`
- `tg_fabs` (line 147) `static float tg_fabs(float x)`
- `tg_log` (line 151) `static float tg_log(float x)`
- `tg_fmax` (line 163) `static float tg_fmax(float a, float b)`
- `tg_fmin` (line 167) `static float tg_fmin(float a, float b)`
- `load_vocab` (line 254) `static void load_vocab(const char *path)`
- `build_torus_graph` (line 295) `static void build_torus_graph(void)` - *====================================================================== SECTION 4: TORUS GRAPH BUILDER * ======================================================================*
- `precompute_rope` (line 326) `static void precompute_rope(void)` - *====================================================================== SECTION 5: ROPE PRECOMPUTATION * ======================================================================*
- `matvec` (line 358) `static void matvec(const float *W, const float *x, float *y, int rows, int cols)` - *====================================================================== SECTION 6: MATRIX OPERATIONS * ======================================================================*
- `matvec_bias` (line 369) `static void matvec_bias(const float *W, const float *b, const float *x, float *y,
               ...`
- `rmsnorm` (line 381) `static void rmsnorm(const float *x, const float *w, float *y, int d)`
- `softmax` (line 390) `static void softmax(float *x, int n)`
- `gelu` (line 399) `static void gelu(float *x, int n)`
- `silu` (line 409) `static void silu(float *x, int n)`
- `swiglu` (line 417) `static void swiglu(const float *gate_w, const float *up_w, const float *down_w,
                 ...`
- `quat_normalize` (line 434) `static void quat_normalize(float *q)` - *====================================================================== SECTION 7: QUATERNION OPERATIONS * ======================================================================*
- `quat_hamilton` (line 439) `static void quat_hamilton(const float *a, const float *b, float *c)`
- `quat_linear` (line 448) `static void quat_linear(const float *Ww, const float *Wx, const float *Wy, const float *Wz,
     ...` - *static void quat_normalize(float *q) { float n = tg_sqrt(q[0]*q[0] + q[1]*q[1] + q[2]*q[2] + q[3]*q[3]); if (n > 1e-8f) { q[0]/=n; q[1]/=n; q[2]/=n; q[3]/=n; } } static void quat_hamilton(const float *a, const float *b, float *c) { c[0] = a[0]*b[0] - a[1]*b[1] - a[2]*b[2] - a[3]*b[3]; c[1] = a[0]*b[1] + a[1]*b[0] + a[2]*b[3] - a[3]*b[2]; c[2] = a[0]*b[2] - a[1]*b[3] + a[2]*b[0] + a[3]*b[1]; c[3] = a[0]*b[3] + a[1]*b[2] - a[2]*b[1] + a[3]*b[0]; } /* QuaternionLinear: x[w,x,y,z] -> y[w,x,y,z]*
- `ifft_radix2` (line 504) `static void ifft_radix2(float *real, float *imag, int n)`
- `rfft` (line 513) `static void rfft(const float *x, float *Xr, float *Xi, int n)` - *cur_r = nr; } } } } static void ifft_radix2(float *real, float *imag, int n) { int i; for (i = 0; i < n; i++) imag[i] = -imag[i]; fft_radix2(real, imag, n); for (i = 0; i < n; i++) { real[i] /= (float)n; imag[i] = -imag[i] / (float)n; } } /* Real FFT: x[n] -> X[n/2+1] complex*
- `irfft` (line 522) `static void irfft(const float *Xr, const float *Xi, float *x, int n)` - *fft_radix2(real, imag, n); for (i = 0; i < n; i++) { real[i] /= (float)n; imag[i] = -imag[i] / (float)n; } } /* Real FFT: x[n] -> X[n/2+1] complex static void rfft(const float *x, float *Xr, float *Xi, int n) { float re[n], im[n]; int i; for (i = 0; i < n; i++) { re[i] = x[i]; im[i] = 0.0f; } fft_radix2(re, im, n); for (i = 0; i <= n/2; i++) { Xr[i] = re[i]; Xi[i] = im[i]; } } /* Inverse real FFT: X[n/2+1] complex -> x[n]*
- `filter1d` (line 536) `static void filter1d(const float *x, const float *kr, const float *ki,
                      floa...` - *====================================================================== SECTION 9: SPECTRAL 1D FILTER * ======================================================================*
- `ifft2d` (line 579) `static void ifft2d(float *data_r, float *data_i, int h, int w)`
- `rfft2d_real` (line 602) `static void rfft2d_real(const float *data, float *out_r, float *out_i,
                         i...` - *ifft_radix2(row_re, row_im, w); for (c = 0; c < w; c++) { re[r*w+c] = row_re[c]; im[r*w+c] = row_im[c]; } } /* IFFT columns float col_re[h], col_im[h]; for (c = 0; c < w; c++) { for (r = 0; r < h; r++) { col_re[r] = re[r*w+c]; col_im[r] = im[r*w+c]; } ifft_radix2(col_re, col_im, h); for (r = 0; r < h; r++) { re[r*w+c] = col_re[r]; im[r*w+c] = col_im[r]; } } for (i = 0; i < h * w; i++) { data_r[i] = re[i]; data_i[i] = im[i]; } } /* RFFT2: 2D real FFT, output is [h][w/2+1] complex*
- `irfft2d` (line 629) `static void irfft2d(const float *in_r, const float *in_i, float *out,
                     int h,...` - *for (r = 0; r < h; r++) { col_re[r] = re[r*w+c]; col_im[r] = im[r*w+c]; } fft_radix2(col_re, col_im, h); for (r = 0; r < h; r++) { re[r*w+c] = col_re[r]; im[r*w+c] = col_im[r]; } } int fw = w / 2 + 1; for (r = 0; r < h; r++) { for (c = 0; c < fw; c++) { out_r[r * fw + c] = re[r * w + c]; out_i[r * fw + c] = im[r * w + c]; } } } /* IRFFT2: inverse of rfft2d_real*
- `cmul` (line 664) `static void cmul(float ar, float ai, float cr, float di, float *rr, float *ri)` - *====================================================================== SECTION 11: QUATERNION SPECTRAL LAYER 2D * ====================================================================== /* Complex multiply: (ar+bi)(cr+di) = (ac-bd)+(ad+bc)i*
- `spectral_contract` (line 670) `static void spectral_contract(const float *Wr, const float *Wi,
                               co...` - *====================================================================== SECTION 11: QUATERNION SPECTRAL LAYER 2D * ====================================================================== /* Complex multiply: (ar+bi)(cr+di) = (ac-bd)+(ad+bc)i static void cmul(float ar, float ai, float cr, float di, float *rr, float *ri) { rr = ar*cr - ai*di; ri = ar*di + ai*cr; } /* Contract: Y[o,h,w] = sum_i W[i,o,h,w] * X[b,i,h,w] (complex)*
- `quat_spectral_layer_2d` (line 694) `static void quat_spectral_layer_2d(
    const float *x, float *y,
    const float *kr_w, const fl...`
- `spectral_ae_encode` (line 784) `static void spectral_ae_encode(const float *x, float *z, const LayerWeights *lw)` - *====================================================================== SECTION 12: SPECTRAL AUTOENCODER FORWARD * ======================================================================*
- `spectral_ae_decode` (line 792) `static void spectral_ae_decode(const float *z, float *x, const LayerWeights *lw)`
- `process_torus_grid` (line 799) `static void process_torus_grid(const float *grid, float *out, const LayerWeights *lw)`
- `torus_soft_assign` (line 820) `static void torus_soft_assign(const float *phi1, const float *phi2,
                             ...` - *====================================================================== SECTION 13: TORUS BRAIN FORWARD * ======================================================================*
- `message_passing` (line 842) `static void message_passing(const float *node_feat, float *out,
                             cons...`
- `torus_brain_forward` (line 887) `static void torus_brain_forward(const float *x, float *out, float *recon_loss,
                  ...`
- `attention_forward` (line 977) `static void attention_forward(const float *x, float *out, int layer_idx, int pos, int total_kv_co...` - *====================================================================== SECTION 14: ATTENTION FORWARD * ======================================================================*
- `moe_forward` (line 1077) `static void moe_forward(const float *x, float *out, const LayerWeights *lw)` - *====================================================================== SECTION 15: MoE ROUTING * ======================================================================*
- `forward` (line 1127) `static void forward(const int *token_ids, int seq_len, float *logits_out)` - *====================================================================== SECTION 16: FULL MODEL FORWARD  Processes tokens autoregressively through all layers. Each token position goes through ALL layers before the next position. This is the correct order: layer 0 must see all positions before layer 1 can process them.  After processing, logits_out holds logits for the LAST position only. * ======================================================================*
- `tokenize_string` (line 1194) `static int tokenize_string(const char *text, int *tokens, int max_tokens)`
- `apply_temperature` (line 1209) `static void apply_temperature(float *logits, int n, float temp)` - *====================================================================== SECTION 18: SAMPLING * ======================================================================*
- `apply_repetition_penalty` (line 1215) `static void apply_repetition_penalty(float *logits, int n, const int *tokens,
                   ...`
- `apply_top_k` (line 1228) `static void apply_top_k(float *logits, int n, int k)`
- `sample` (line 1247) `static int sample(const float *logits, int n)`
- `load_weights` (line 1281) `static int load_weights(const char *path)` - *====================================================================== SECTION 19: WEIGHT LOADER  Reads the binary file produced by convert_weights.py. The converter writes tensors in a fixed order. We read them in the same order, matching each to its destination buffer by position. No string parsing needed. * ======================================================================*
- `load_weights_fp16` (line 1451) `static int load_weights_fp16(const char *path)`
- `load_weights_auto` (line 1583) `static int load_weights_auto(const char *path)` - *printf("  Layer %d loaded\n", i); } READ_TENSOR16(W.final_norm, D_MODEL); #undef SKIP_TENSOR16 #undef READ_TENSOR16 fclose(f); printf("Weights loaded successfully (fp16).\n"); return 0; } /* Auto-detect format and load weights*
- `time_now_ms` (line 1600) `static double time_now_ms(void)` - *====================================================================== SECTION 20: TIMING * ====================================================================== /* Portable wall-clock timer using rdtsc where available, else microseconds*
- `decode_token` (line 1613) `static void decode_token(int tid)` - *====================================================================== SECTION 21: GENERATION * ======================================================================*
- `load_token_file` (line 1629) `static int load_token_file(const char *path, int *out_ids, int max_ids)` - *if (tid < 256) { /* Map GPT-2 byte-level encoding back to original byte int n = tid; if (n < 94) n += 33; else if (n < 163) n += 161 - 94; else n += 173 - 163; putchar(n); } else { /* Multi-byte token: output placeholder or skip putchar('?'); } } /* Load pre-tokenized binary file (format: "TKID" + uint32 count + int32 ids[])*
- `decode_token_tiktoken` (line 1652) `static void decode_token_tiktoken(int tid)` - *if (fread(&n, 4, 1, f) != 1) { fclose(f); return 0; } if (n > (unsigned)max_ids) n = max_ids; int count = (int)n; int i; for (i = 0; i < count; i++) { int id; if (fread(&id, 4, 1, f) != 1) break; out_ids[i] = id; } fclose(f); return count; } /* Decode token ID using loaded vocabulary*
- `generate_tokens` (line 1660) `static void generate_tokens(int *prompt_tokens, int n_prompt, int max_new_tokens,
               ...`
- `generate` (line 1724) `static void generate(const char *prompt, int max_new_tokens, float temperature,
                 ...`
- `interactive_mode` (line 1735) `static void interactive_mode(void)` - *====================================================================== SECTION 22: INTERACTIVE MODE * ======================================================================*
- `print_help` (line 1849) `static void print_help(void)` - *====================================================================== SECTION 23: HELP AND MAIN * ======================================================================*
- `main` (line 1884) `int main(int argc, char **argv)`

**Macros:**
- `NULL` (line 43)
- `SEEK_SET` (line 44)
- `SEEK_CUR` (line 45)
- `SEEK_END` (line 46)
- `VOCAB_SIZE` (line 64)
- `D_MODEL` (line 66)
- `N_HEADS` (line 67)
- `N_KV_HEADS` (line 68)
- `GQA_GROUPS` (line 69)
- `D_HEAD` (line 70)
- `D_QUAT` (line 71)
- `N_LAYERS` (line 72)
- `MAX_SEQ_LEN` (line 73)
- `N_EXPERTS` (line 74)
- `MOE_TOP_K` (line 75)
- `N_NODES` (line 76)
- `N_RADIAL` (line 77)
- `N_ANGULAR` (line 78)
- `N_EDGE_TYPES` (line 79)
- `N_EDGES` (line 80)
- `SPECTRAL_LATENT_DIM` (line 81)
- `D_LAT_Q` (line 82)
- `TORUS_GRID_H` (line 83)
- `TORUS_GRID_W` (line 84)
- `FREQ_W` (line 85)
- `N_SPECTRAL_LAYERS` (line 86)
- `EXPERT_INNER` (line 87)
- `READOUT_INNER` (line 88)
- `EOS_TOKEN` (line 89)
- `EMBED_INNER` (line 90)
- `PI` (line 91)
- `EPS_RMS` (line 92)
- `TORUS_TEMP` (line 93)
- `MAX_TOKENS` (line 94)
- `MAX_PROMPT_LEN` (line 95)
- `MAX_LINE` (line 96)
- `TOK_TAB_SIZE` (line 97)
- `TOK_VOCAB_SIZE` (line 98)
- `SKIP_TENSOR` (line 1300)
- `READ_TENSOR` (line 1310)
- `SKIP_TENSOR16` (line 1470)
- `READ_TENSOR16` (line 1480)

### PY (34 files)

#### `app.py`
**Path:** `app.py`

**Functions:**
- `run_inference` (line 46) `def run_inference(prompt, checkpoint_dir, checkpoint_name, max_new_tokens, temperature, top_k, repetition_penalty, device)` - *Run the standard sampler and return the generated completion text.*
- `run_inference_hrm` (line 71) `def run_inference_hrm(prompt, checkpoint_dir, checkpoint_name, max_new_tokens, temperature, top_k, repetition_penalty, high_level_iters, low_level_iters, low_level_window, device)` - *Run the hierarchical recursive sampler and return the completion.*
- `run_training` (line 105) `def run_training(scale, start_tier, device, prepare_data)` - *Run the full TopoGPT3 curriculum trainer.*
- `_build_parser` (line 121) `def _build_parser()` - *Build the top-level CLI for this entry point script.*
- `main` (line 159) `def main(argv)` - *Entry point invoked when the file is executed as a script.*

#### `convert_weights.py`
**Path:** `convert_weights.py`

**Functions:**
- `convert` (line 102) `def convert(input_path, output_path)`
- `main` (line 160) `def main()`

#### `convert_weights_minios.py`
**Path:** `convert_weights_minios.py`

**Functions:**
- `main` (line 85) `def main()`

#### `encode_tokens.py`
**Path:** `encode_tokens.py`

**Functions:**
- `main` (line 19) `def main()`

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
- `context_length_diagnostic` (line 171) `def context_length_diagnostic(model, tracker, device, lengths)`
- `main` (line 248) `def main()`

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

**Methods:**
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

**Methods:**
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

**Methods:**
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

#### `gradio_app.py`
**Path:** `gradio_app.py`

**Functions:**
- `ensure_checkpoint` (line 35) `def ensure_checkpoint()` - *Return the path to the checkpoint directory, downloading if needed.*
- `run_standard_inference` (line 59) `def run_standard_inference(prompt, max_new_tokens, temperature, top_k, repetition_penalty, auto_continue)` - *Run standard autoregressive inference.*
- `run_hrm_inference` (line 95) `def run_hrm_inference(prompt, max_new_tokens, temperature, top_k, repetition_penalty, high_level_iters, low_level_iters, low_level_window, thinking, auto_continue)` - *Run hierarchical recursive reasoning inference.*
- `build_ui` (line 144) `def build_ui()` - *Construct the Gradio Blocks interface.*

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

**Methods:**
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

#### `test_jlens.py`
**Path:** `tests/test_jlens.py`

**Classes:**
- `TestValidPositionMask` (line 17) `class TestValidPositionMask` - *Feature: valid_position_mask excludes attention-sink and final positions.*
- `TestJacobianForPrompt` (line 52) `class TestJacobianForPrompt` - *Feature: jacobian_for_prompt computes J_l for one prompt.*
- `TestFit` (line 172) `class TestFit` - *Feature: fit() averages Jacobians over multiple prompts.*
- `TestJacobianLens` (line 210) `class TestJacobianLens` - *Feature: JacobianLens saves, loads, applies, and merges.*
- `TestFitCheckpoint` (line 367) `class TestFitCheckpoint` - *Feature: fit() with checkpoint resume works correctly.*
- `TestConfig` (line 473) `class TestConfig` - *Feature: Config classes centralize all tunable parameters.*
- `TestTopoGPT3JLensAppConfig` (line 494) `class TestTopoGPT3JLensAppConfig` - *Feature: Application config controls readout behavior.*

**Methods:**
- `test_basic_mask` (line 20) `def test_basic_mask(self)` - *Scenario: Correct mask for a standard-length prompt.*
- `test_too_short_raises` (line 29) `def test_too_short_raises(self)` - *Scenario: Too-short prompt raises ValueError.*
- `test_negative_skip_raises` (line 34) `def test_negative_skip_raises(self)` - *Scenario: Negative skip_first raises ValueError.*
- `test_all_positions_valid` (line 39) `def test_all_positions_valid(self)` - *Scenario: skip_first=0 includes all but final position.*
- `test_exact_minimum_length` (line 45) `def test_exact_minimum_length(self)` - *Scenario: Exact minimum length (skip_first + 2) works.*
- `model` (line 56) `def model(self)`
- `test_returns_jacobians_for_source_layers` (line 63) `def test_returns_jacobians_for_source_layers(self, model)` - *Scenario: Returns Jacobians for all requested source layers.*
- `test_late_layer_jacobian_close_to_identity` (line 76) `def test_late_layer_jacobian_close_to_identity(self, model)` - *Scenario: J_{n_layers-2} has diag ~= 1 (identity property).*
- `test_earlier_layers_further_from_identity` (line 85) `def test_earlier_layers_further_from_identity(self, model)` - *Scenario: Earlier layers compound deviations from identity.*
- `test_exact_jacobian_for_last_block` (line 95) `def test_exact_jacobian_for_last_block(self, model)` - *Scenario: J_{n_layers-2} equals I + W_{last} exactly.

For TinyDecoder with block = h + 0.1*W*h, J_{n_layers-2} = I + W.*
- `test_negative_layer_indices` (line 110) `def test_negative_layer_indices(self, model)` - *Scenario: Negative layer indices are normalized correctly.*
- `test_out_of_range_layers_rejected` (line 133) `def test_out_of_range_layers_rejected(self, model)` - *Scenario: Out-of-range layers raise ValueError.*
- `test_source_below_target_enforced` (line 145) `def test_source_below_target_enforced(self, model)` - *Scenario: source_layers must be below target_layer.*
- `test_target_out_of_range_raises` (line 158) `def test_target_out_of_range_raises(self, model)` - *Scenario: target_layer out of range raises ValueError.*
- `model` (line 176) `def model(self)`
- `test_fit_returns_lens_with_correct_attributes` (line 183) `def test_fit_returns_lens_with_correct_attributes(self, model)` - *Scenario: fit() returns JacobianLens with correct metadata.*
- `test_fit_empty_prompts_raises` (line 191) `def test_fit_empty_prompts_raises(self, model)` - *Scenario: No valid prompts raises ValueError.*
- `test_fit_skips_short_prompts` (line 196) `def test_fit_skips_short_prompts(self, model)` - *Scenario: Too-short prompts are skipped.*
- `test_fit_with_default_source_layers` (line 202) `def test_fit_with_default_source_layers(self, model)` - *Scenario: Default source_layers covers all layers below target.*
- `model` (line 214) `def model(self)`
- `fitted_lens` (line 222) `def fitted_lens(self, model)`
- `test_save_and_load_round_trip` (line 226) `def test_save_and_load_round_trip(self, fitted_lens, tmp_path)` - *Scenario: save/load preserves jacobians (fp16 tolerance).*
- `test_apply_returns_correct_shapes` (line 242) `def test_apply_returns_correct_shapes(self, fitted_lens, model)` - *Scenario: apply() returns correct logit shapes.*
- `test_fitted_late_layer_matches_model` (line 254) `def test_fitted_late_layer_matches_model(self, fitted_lens, model)` - *Scenario: Transported late-layer logits match model logits.*
- `test_apply_with_explicit_positions` (line 263) `def test_apply_with_explicit_positions(self, fitted_lens, model)` - *Scenario: Explicit positions return correct subset.*
- `test_logit_lens_baseline` (line 274) `def test_logit_lens_baseline(self, fitted_lens, model)` - *Scenario: use_jacobian=False returns untransported logits.*
- `test_unfitted_layer_rejected` (line 281) `def test_unfitted_layer_rejected(self, fitted_lens, model)` - *Scenario: Unfitted layer raises ValueError.*
- `test_out_of_range_layer_rejected` (line 286) `def test_out_of_range_layer_rejected(self, fitted_lens, model)` - *Scenario: Out-of-range layer raises ValueError.*
- `test_merge_weighted_mean` (line 291) `def test_merge_weighted_mean(self)` - *Scenario: merge() computes n_prompts-weighted mean.*
- `test_merge_mismatch_raises` (line 319) `def test_merge_mismatch_raises(self)` - *Scenario: Mismatched lenses raise ValueError.*
- `test_merge_empty_raises` (line 326) `def test_merge_empty_raises(self)` - *Scenario: Empty merge raises ValueError.*
- `test_transport_produces_correct_shape` (line 331) `def test_transport_produces_correct_shape(self, fitted_lens)` - *Scenario: transport() maps residual to final-layer basis.*
- `test_load_invalid_file_raises` (line 337) `def test_load_invalid_file_raises(self, tmp_path)` - *Scenario: Loading non-lens file raises ValueError.*
- `test_from_pretrained_local_file` (line 344) `def test_from_pretrained_local_file(self, fitted_lens, tmp_path)` - *Scenario: from_pretrained resolves a local file.*
- `test_from_pretrained_local_directory` (line 351) `def test_from_pretrained_local_directory(self, fitted_lens, tmp_path)` - *Scenario: from_pretrained resolves a local directory.*
- `test_repr` (line 359) `def test_repr(self, fitted_lens)` - *Scenario: repr contains key metadata.*
- `model` (line 371) `def model(self)`
- `test_checkpoint_resume_produces_same_result` (line 378) `def test_checkpoint_resume_produces_same_result(self, model, tmp_path)` - *Scenario: Resumed fit matches fresh fit.*
- `test_resume_after_skip_no_double_count` (line 408) `def test_resume_after_skip_no_double_count(self, model, tmp_path)` - *Scenario: Resume after a skipped prompt does not double-count.

Regression: a skipped prompt must not desync success-count from
list-position.*
- `test_checkpoint_mismatch_raises` (line 450) `def test_checkpoint_mismatch_raises(self, model, tmp_path)` - *Scenario: Mismatched checkpoint settings raise ValueError.*
- `test_fit_config_defaults` (line 476) `def test_fit_config_defaults(self)` - *Scenario: Default fit config has sensible defaults.*
- `test_app_config_defaults` (line 485) `def test_app_config_defaults(self)` - *Scenario: Default app config has sensible defaults.*
- `test_default_config` (line 497) `def test_default_config(self)` - *Scenario: Default app config uses all positions.*
- `test_custom_config` (line 505) `def test_custom_config(self)` - *Scenario: Custom app config overrides specific layers.*

#### `test_lens_model.py`
**Path:** `tests/test_lens_model.py`

**Classes:**
- `TestTopoGPT3LensConfig` (line 13) `class TestTopoGPT3LensConfig` - *Feature: TopoGPT3LensConfig provides centralized adapter configuration.*
- `TestTinyDecoder` (line 41) `class TestTinyDecoder` - *Feature: TinyDecoder provides a minimal test model.*
- `TestTopoGPT3LensModel` (line 65) `class TestTopoGPT3LensModel` - *Feature: TopoGPT3LensModel wraps a model to implement LensModel protocol.*
- `TestTopoGPT3LensModelWithRecording` (line 214) `class TestTopoGPT3LensModelWithRecording` - *Feature: ActivationRecorder works with TopoGPT3LensModel.*
- `TestTopoGPT3LensModelEdgeCases` (line 278) `class TestTopoGPT3LensModelEdgeCases` - *Feature: Edge cases are handled gracefully.*

**Methods:**
- `test_default_config` (line 16) `def test_default_config(self)` - *Scenario: Default config matches small scale preset.*
- `test_from_topogpt2_config` (line 25) `def test_from_topogpt2_config(self)` - *Scenario: Build lens config from TopoGPT2Config.*
- `test_probe_checkpoint_missing_raises` (line 35) `def test_probe_checkpoint_missing_raises(self, tmp_path)` - *Scenario: Missing state.json raises FileNotFoundError.*
- `test_default_parameters` (line 44) `def test_default_parameters(self)` - *Scenario: TinyDecoder has correct default shape.*
- `test_forward_output_shape` (line 51) `def test_forward_output_shape(self)` - *Scenario: Forward pass produces correct logit shape.*
- `test_weight_tied` (line 59) `def test_weight_tied(self)` - *Scenario: Embedding and LM head share weights.*
- `raw_model` (line 69) `def raw_model(self)`
- `lens_model` (line 77) `def lens_model(self, raw_model)`
- `test_exposes_protocol_attributes` (line 80) `def test_exposes_protocol_attributes(self, lens_model, raw_model)` - *Scenario: LensModel attributes match underlying model.*
- `test_encode_text_to_token_ids` (line 87) `def test_encode_text_to_token_ids(self, lens_model)` - *Scenario: encode() returns tensor of shape [1, seq_len].*
- `test_encode_with_tokenizer` (line 95) `def test_encode_with_tokenizer(self)` - *Scenario: encode() uses BPETokenizer when available.*
- `test_encode_respects_max_length` (line 107) `def test_encode_respects_max_length(self, lens_model)` - *Scenario: encode() truncates at max_length.*
- `test_forward_returns_residual_only` (line 113) `def test_forward_returns_residual_only(self)` - *Scenario: forward() returns hidden states with d_model dim, not vocab.

The lens model forward should stop before final_norm and lm_head.
The output should have d_model as last dimension, not vocab_size.*
- `test_forward_differs_from_full_model` (line 128) `def test_forward_differs_from_full_model(self)` - *Scenario: Residual forward shape differs from full model logits.*
- `test_unembed_produces_logits` (line 141) `def test_unembed_produces_logits(self, lens_model)` - *Scenario: unembed() maps residual to logits.*
- `test_forward_plus_unembed_matches_model_logits` (line 150) `def test_forward_plus_unembed_matches_model_logits(self, lens_model, raw_model)` - *Scenario: residual forward + unembed == model forward logits.

This validates that our split forward matches the original model's
full forward pass.*
- `test_autograd_graph_tracks_through_layers` (line 163) `def test_autograd_graph_tracks_through_layers(self)` - *Scenario: Gradient flows through residual layers when grads enabled.*
- `test_input_device_property` (line 180) `def test_input_device_property(self, lens_model)` - *Scenario: input_device returns the embedding weight device.*
- `test_input_device_setter` (line 185) `def test_input_device_setter(self, lens_model)` - *Scenario: input_device can be overridden.*
- `test_tokenizer_setter` (line 191) `def test_tokenizer_setter(self, lens_model)` - *Scenario: tokenizer can be set after construction.*
- `test_from_checkpoint_missing_raises` (line 198) `def test_from_checkpoint_missing_raises(self)` - *Scenario: from_checkpoint with missing directory raises.*
- `test_grad_enabled_deterministic` (line 205) `def test_grad_enabled_deterministic(self, lens_model)` - *Scenario: Multiple forward passes with same input are deterministic.*
- `lens_model` (line 218) `def lens_model(self)`
- `test_recorder_captures_layer_outputs` (line 225) `def test_recorder_captures_layer_outputs(self, lens_model)` - *Scenario: ActivationRecorder captures all requested layer outputs.*
- `test_recorder_with_start_graph_at` (line 238) `def test_recorder_with_start_graph_at(self, lens_model)` - *Scenario: start_graph_at roots the autograd graph.*
- `test_recorder_cleanup_on_exception` (line 252) `def test_recorder_cleanup_on_exception(self, lens_model)` - *Scenario: Hooks are removed even if construction fails.*
- `test_recorder_detach_after_forward` (line 264) `def test_recorder_detach_after_forward(self, lens_model)` - *Scenario: Activations can be detached after recorder exits.*
- `test_empty_sequence` (line 281) `def test_empty_sequence(self)` - *Scenario: Empty input produces error or minimal output.*
- `test_single_token` (line 291) `def test_single_token(self)` - *Scenario: Single token input works.*

#### `__init__.py`
**Path:** `topogpt3/__init__.py`

*No symbols extracted*

#### `__main__.py`
**Path:** `topogpt3/__main__.py`

**Functions:**
- `main` (line 6) `def main()` - *TopoGPT3 entry point. Delegates to subcommands.*

#### `api_server.py`
**Path:** `topogpt3/api_server.py`

**Classes:**
- `ApiKey` (line 137) `class ApiKey`
- `AuthState` (line 143) `class AuthState`
- `TokenBucket` (line 202) `class TokenBucket`
- `RateLimiter` (line 219) `class RateLimiter`
- `IpBanner` (line 250) `class IpBanner`
- `CompletionRequest` (line 291) `class CompletionRequest(BaseModel)`
- `Message` (line 310) `class Message(BaseModel)`
- `ChatCompletionRequest` (line 316) `class ChatCompletionRequest(BaseModel)`
- `ServerModel` (line 341) `class ServerModel`

**Functions:**
- `_setup_logging` (line 116) `def _setup_logging(verbose)`

**Methods:**
- `_parse_keys` (line 164) `def _parse_keys(raw)` - *Accept ``key1,admin:key2,key3``. The ``admin:`` prefix marks an
admin-level key; everything else is a regular user key.*
- `_sha256` (line 192) `def _sha256(raw)`
- `_sanitize_stop` (line 281) `def _sanitize_stop(stop)`
- `_resolve_device` (line 499) `def _resolve_device(device)`
- `_probe_n_kv` (line 505) `def _probe_n_kv(checkpoint_dir)`
- `load_model` (line 513) `def load_model(checkpoint, device)`
- `lifespan` (line 534) `def lifespan(app)`
- `_security_middleware` (line 574) `def _security_middleware(request, call_next)` - *Global middleware: rate-limit, IP-ban, security headers, audit log.*
- `_real_ip` (line 602) `def _real_ip(request)` - *Best-effort real client IP. We trust no proxy headers by default.*
- `_json_error` (line 613) `def _json_error(status, detail)`
- `_authenticate` (line 625) `def _authenticate(request)` - *FastAPI dependency: extract & validate Bearer token.*
- `_check_rate_limit` (line 643) `def _check_rate_limit(api_key, request)` - *Rate limit per-key (with admin exemption / higher limit).*
- `health` (line 661) `def health(request)`
- `list_models` (line 668) `def list_models(request)`
- `completions` (line 685) `def completions(req, request)`
- `chat_completions` (line 741) `def chat_completions(req, request)`
- `_check_model` (line 799) `def _check_model()`
- `_short_id` (line 804) `def _short_id()`
- `_build_chat_prompt` (line 808) `def _build_chat_prompt(messages)`
- `_extract_text` (line 815) `def _extract_text(content)`
- `_stream_completion` (line 829) `def _stream_completion(prompt, max_tokens, temperature, top_k, repetition_penalty, stop, auto_continue, max_continuations)`
- `_stream_chat` (line 864) `def _stream_chat(t0_ms, prompt, max_tokens, temperature, top_k, repetition_penalty, stop, auto_continue, max_continuations)`
- `main` (line 902) `def main()`
- `validate` (line 148) `def validate(self, raw)`
- `consume` (line 208) `def consume(self, n)`
- `__init__` (line 220) `def __init__(self, user_rps, admin_rps, capacity)`
- `_cleanup` (line 227) `def _cleanup(self)`
- `allow` (line 233) `def allow(self, key, role)`
- `__init__` (line 251) `def __init__(self, max_failures, window)`
- `record_failure` (line 257) `def record_failure(self, ip)`
- `is_banned` (line 265) `def is_banned(self, ip)`
- `_normalize_stop` (line 306) `def _normalize_stop(cls, v)`
- `_normalize_stop` (line 331) `def _normalize_stop(cls, v)`
- `complete` (line 348) `def complete(self, prompt)`
- `stream_complete` (line 393) `def stream_complete(self, prompt)`
- `_is_eos` (line 482) `def _is_eos(self, token_id)`

#### `continuation.py`
**Path:** `topogpt3/continuation.py`

**Functions:**
- `_count_unclosed_brackets` (line 25) `def _count_unclosed_brackets(text)`
- `_count_unclosed_fences` (line 36) `def _count_unclosed_fences(text)`
- `is_response_complete` (line 45) `def is_response_complete(text, min_chars)` - *Heuristic to decide whether a model response looks finished.

Returns True when the response seems naturally complete (no need to
continue), False when it appears truncated and continuation may help.*
- `extract_tail_for_continuation` (line 75) `def extract_tail_for_continuation(text, tail_lines, tail_chars)` - *Return the last N lines (or up to tail_chars) of `text` as a
continuation prefix to feed back into the model.

The returned string can be prepended as context for the model's next
generation call so it continues naturally from that point.*
- `split_at_last_newline` (line 105) `def split_at_last_newline(text)` - *Split `text` at the last newline.

Returns (prefix_without_last_line, last_line).
Useful for discarding a trailing incomplete line before continuation.*

#### `inference.py`
**Path:** `topogpt3/inference.py`

**Classes:**
- `ScalePreset` (line 32) `class ScalePreset` - *Immutable architecture preset for a named model scale.*
- `InferenceSettings` (line 42) `class InferenceSettings` - *Centralized configuration container for the inference pipeline.

Every value consumed downstream resides here. Adding a new tunable means
extending this class; no other module should embed literals.*
- `InferenceLoggerFactory` (line 158) `class InferenceLoggerFactory` - *Builds a stdout-attached logger from inference settings.*
- `SecurePathResolver` (line 178) `class SecurePathResolver` - *Resolves filesystem paths while rejecting traversal outside their root.*
- `SourceModuleLoader` (line 212) `class SourceModuleLoader` - *Resolves the TopoGPT3 runtime module via the package import system.*
- `CheckpointPaths` (line 228) `class CheckpointPaths` - *Computes and validates checkpoint file paths under a single root.*
- `WeightShapeProbe` (line 274) `class WeightShapeProbe` - *Reads tensor metadata from safetensors to infer architecture details.*
- `TopoGPT2ConfigAligner` (line 318) `class TopoGPT2ConfigAligner` - *Builds a TopoGPT2Config matching the loaded checkpoint and tokenizer.*
- `TokenizerFactory` (line 349) `class TokenizerFactory` - *Builds a BPETokenizer instance using the configured encoding.*
- `GaussPatchApplier` (line 362) `class GaussPatchApplier` - *Applies the idempotent Gauss complex-multiply patch when enabled.*
- `ModelAssembler` (line 380) `class ModelAssembler` - *Instantiates the model and loads weights from safetensors.*
- `SeedSynchronizer` (line 417) `class SeedSynchronizer` - *Applies deterministic seeds across torch, CUDA and the model package.*
- `SamplingPolicy` (line 441) `class SamplingPolicy` - *Immutable sampling parameters consumed by the generation engine.*
- `GenerationReport` (line 461) `class GenerationReport` - *Quantitative summary of a single generation call.*
- `GenerationEngine` (line 475) `class GenerationEngine` - *Runs autoregressive sampling against a loaded model and tokenizer.*
- `ResultRenderer` (line 533) `class ResultRenderer` - *Prints a GenerationReport to stdout using settings-defined formatting.*
- `InferencePipeline` (line 562) `class InferencePipeline` - *Orchestrator wiring loader, builder, engine and renderer.*
- `CliArgumentParser` (line 615) `class CliArgumentParser` - *Translates command-line arguments into an InferenceSettings instance.*

**Methods:**
- `main` (line 721) `def main(argv)` - *CLI entry point. Returns a process exit code.*
- `scale_presets` (line 103) `def scale_presets()` - *Return the architecture preset table indexed by scale name.*
- `preset` (line 116) `def preset(self)` - *Return the resolved preset for the configured model scale.*
- `validate` (line 126) `def validate(self)` - *Raise ValueError if any setting falls outside its safety bounds.*
- `build` (line 162) `def build(settings)` - *Return a configured Logger with a single deduplicated stdout handler.*
- `resolve_under` (line 182) `def resolve_under(root)` - *Join `parts` under `root` and return the canonical resolved path.

Raises ValueError if the resolved path escapes `root`.*
- `require_existing_file` (line 198) `def require_existing_file(path, expected_suffix)` - *Validate `path` points to an existing regular file with the expected suffix.*
- `__init__` (line 215) `def __init__(self, settings, logger)`
- `load` (line 219) `def load(self)` - *Return the topogpt3.train module which re-exports model symbols.*
- `__init__` (line 231) `def __init__(self, settings)`
- `slot_dir` (line 239) `def slot_dir(self)` - *Directory holding the active checkpoint slot.*
- `model_file` (line 243) `def model_file(self)` - *Resolved path to the safetensors weights file inside the slot.*
- `state_file` (line 249) `def state_file(self)` - *Resolved path to the JSON training-state file inside the slot.*
- `assert_ready` (line 255) `def assert_ready(self)` - *Verify weights exist and the on-disk size lies within safety bounds.*
- `__init__` (line 277) `def __init__(self, settings, logger)`
- `detect_n_kv_heads` (line 281) `def detect_n_kv_heads(self, weights_path, d_model, n_heads)` - *Recover N_KV_HEADS used at training by inspecting the k_proj shape.

Returns None when the probe key is absent, signalling the caller to
fall back to scale defaults rather than guess.*
- `__init__` (line 321) `def __init__(self, settings, source_module, logger)`
- `build` (line 327) `def build(self, n_kv_heads, vocab_size)` - *Return a TopoGPT2Config dataclass ready to instantiate the model.*
- `__init__` (line 352) `def __init__(self, settings, source_module)`
- `build` (line 356) `def build(self)` - *Return an instance of BPETokenizer bound to the configured encoding.*
- `__init__` (line 365) `def __init__(self, settings, source_module, logger)`
- `apply_if_enabled` (line 371) `def apply_if_enabled(self)` - *Patch QuaternionSpectralLayer to use the 3-multiply Gauss contract.*
- `__init__` (line 383) `def __init__(self, settings, source_module, logger)`
- `assemble` (line 389) `def assemble(self, aligned_cfg, paths)` - *Build the TopoGPT2 graph, load weights into it, and return it in eval mode.*
- `__init__` (line 420) `def __init__(self, settings, source_module, logger)`
- `apply` (line 426) `def apply(self)` - *Seed all relevant RNGs using the model package helper when available.*
- `from_settings` (line 450) `def from_settings(cls, settings)` - *Construct a SamplingPolicy from inference settings.*
- `tokens_per_second` (line 470) `def tokens_per_second(self, elapsed_floor)` - *Return throughput in tokens/sec, clamped to avoid divide-by-zero.*
- `__init__` (line 478) `def __init__(self, settings, logger)`
- `run` (line 483) `def run(self, model, tokenizer, prompt, policy)` - *Generate a completion for `prompt` and return a GenerationReport.*
- `__init__` (line 536) `def __init__(self, settings, logger)`
- `render` (line 540) `def render(self, report)` - *Emit a banner with prompt and completion, plus a throughput log line.*
- `__init__` (line 565) `def __init__(self, settings, logger)`
- `execute` (line 571) `def execute(self)` - *Run the full inference pipeline end-to-end and return the report.*
- `build_parser` (line 619) `def build_parser()` - *Return the configured argparse.ArgumentParser.*
- `parse` (line 698) `def parse(argv)` - *Parse `argv` (or sys.argv) and return a populated InferenceSettings.*

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
- `HRMLoggerFactory` (line 343) `class HRMLoggerFactory` - *Builds a stdout-attached logger from inference settings.*
- `SecurePathResolver` (line 363) `class SecurePathResolver` - *Resolves filesystem paths while rejecting traversal outside their root.*
- `SourceModuleLoader` (line 397) `class SourceModuleLoader` - *Resolves the TopoGPT3 runtime module via the package import system.*
- `CheckpointPaths` (line 413) `class CheckpointPaths` - *Computes and validates checkpoint file paths under a single root.*
- `WeightShapeProbe` (line 459) `class WeightShapeProbe` - *Reads tensor metadata from safetensors to infer architecture details.*
- `TopoGPT2ConfigAligner` (line 502) `class TopoGPT2ConfigAligner` - *Builds a TopoGPT2Config matching the loaded checkpoint and tokenizer.*
- `TokenizerFactory` (line 533) `class TokenizerFactory` - *Builds a BPETokenizer instance using the configured encoding.*
- `GaussPatchApplier` (line 546) `class GaussPatchApplier` - *Applies the idempotent Gauss complex-multiply patch when enabled.*
- `ModelAssembler` (line 564) `class ModelAssembler` - *Instantiates the model and loads weights from safetensors.*
- `SeedSynchronizer` (line 601) `class SeedSynchronizer` - *Applies deterministic seeds across torch, CUDA and the model package.*
- `LatentChangeMetric` (line 624) `class LatentChangeMetric` - *Computes the relative L2 distance between two latent tensors.*
- `ReasoningIterationStats` (line 648) `class ReasoningIterationStats` - *Aggregated counters describing a single token's reasoning episode.*
- `GenerationReasoningSummary` (line 661) `class GenerationReasoningSummary` - *Aggregated statistics over the full generation episode.*
- `SparseHighLevelStateCache` (line 684) `class SparseHighLevelStateCache` - *Persists the high-level latent state across consecutive emitted tokens.

The cache is reset whenever its age in tokens reaches the configured
persistence horizon, at which point the next reasoning episode begins
with a zero high-level state. This is the temporal-sparsity mechanism:
expensive full-stack passes are amortized across multiple emissions.*
- `HierarchicalRecursiveReasoner` (line 727) `class HierarchicalRecursiveReasoner` - *Parameter-free hierarchical recursive reasoning over a trained stack.

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
- `LogitsSampler` (line 935) `class LogitsSampler` - *Applies temperature, repetition penalty, top-k filtering and multinomial draw.*
- `SamplingPolicy` (line 963) `class SamplingPolicy` - *Immutable sampling parameters consumed by the generation engine.*
- `GenerationReport` (line 985) `class GenerationReport` - *Quantitative summary of a single generation call.*
- `HRMGenerationEngine` (line 1000) `class HRMGenerationEngine` - *Runs autoregressive sampling driven by hierarchical recursive reasoning.

The engine reimplements the prompt encoding and token emission loop so
that the per-token latent state can be intercepted before final norm and
LM-head projection. The intercepted state is handed to a
HierarchicalRecursiveReasoner, which iterates the trained layer stack in
a two-speed loop until the attractor is reached. The final stabilized
latent is then projected to logits and sampled in the standard fashion.*
- `ResultRenderer` (line 1189) `class ResultRenderer` - *Prints a GenerationReport to stdout using settings-defined formatting.*
- `HRMInferencePipeline` (line 1230) `class HRMInferencePipeline` - *Orchestrator wiring loader, builder, reasoner, engine and renderer.*
- `CliArgumentParser` (line 1283) `class CliArgumentParser` - *Translates command-line arguments into an HRMInferenceSettings instance.*

**Methods:**
- `main` (line 1494) `def main(argv)` - *CLI entry point. Returns a process exit code.*
- `scale_presets` (line 221) `def scale_presets()` - *Return the architecture preset table indexed by scale name.*
- `preset` (line 234) `def preset(self)` - *Return the resolved preset for the configured model scale.*
- `validate` (line 244) `def validate(self)` - *Raise ValueError if any setting falls outside its safety bounds.*
- `build` (line 347) `def build(settings)` - *Return a configured Logger with a single deduplicated stdout handler.*
- `resolve_under` (line 367) `def resolve_under(root)` - *Join parts under root and return the canonical resolved path.

Raises ValueError if the resolved path escapes root.*
- `require_existing_file` (line 383) `def require_existing_file(path, expected_suffix)` - *Validate path points to an existing regular file with the expected suffix.*
- `__init__` (line 400) `def __init__(self, settings, logger)`
- `load` (line 404) `def load(self)` - *Return the topogpt3.train module which re-exports model symbols.*
- `__init__` (line 416) `def __init__(self, settings)`
- `slot_dir` (line 424) `def slot_dir(self)` - *Directory holding the active checkpoint slot.*
- `model_file` (line 428) `def model_file(self)` - *Resolved path to the safetensors weights file inside the slot.*
- `state_file` (line 434) `def state_file(self)` - *Resolved path to the JSON training-state file inside the slot.*
- `assert_ready` (line 440) `def assert_ready(self)` - *Verify weights exist and the on-disk size lies within safety bounds.*
- `__init__` (line 462) `def __init__(self, settings, logger)`
- `detect_n_kv_heads` (line 466) `def detect_n_kv_heads(self, weights_path, d_model, n_heads)` - *Recover N_KV_HEADS used at training by inspecting the k_proj shape.

Returns None when the probe key is absent, signalling the caller to
fall back to scale defaults rather than guess.*
- `__init__` (line 505) `def __init__(self, settings, source_module, logger)`
- `build` (line 511) `def build(self, n_kv_heads, vocab_size)` - *Return a TopoGPT2Config dataclass ready to instantiate the model.*
- `__init__` (line 536) `def __init__(self, settings, source_module)`
- `build` (line 540) `def build(self)` - *Return an instance of BPETokenizer bound to the configured encoding.*
- `__init__` (line 549) `def __init__(self, settings, source_module, logger)`
- `apply_if_enabled` (line 555) `def apply_if_enabled(self)` - *Patch QuaternionSpectralLayer to use the 3-multiply Gauss contract.*
- `__init__` (line 567) `def __init__(self, settings, source_module, logger)`
- `assemble` (line 573) `def assemble(self, aligned_cfg, paths)` - *Build the TopoGPT2 graph, load weights into it, and return it in eval mode.*
- `__init__` (line 604) `def __init__(self, settings, source_module, logger)`
- `apply` (line 610) `def apply(self)` - *Seed all relevant RNGs using the model package helper when available.*
- `__init__` (line 627) `def __init__(self, epsilon_floor)`
- `relative_change` (line 632) `def relative_change(self, current, previous)` - *Return ||current - previous|| / max(||previous||, epsilon_floor).*
- `absorb` (line 671) `def absorb(self, sample)` - *Fold a per-token sample into the running totals.*
- `__init__` (line 693) `def __init__(self, persist_tokens)`
- `get_or_init` (line 700) `def get_or_init(self, reference)` - *Return the cached high-level state or a zeroed one when stale.

The boolean flag indicates whether the returned tensor came from a
live cache hit (True) or a fresh zero initialization (False).*
- `commit` (line 716) `def commit(self, new_state)` - *Store a fresh high-level state and increment the cache age.*
- `invalidate` (line 721) `def invalidate(self)` - *Drop any cached state and reset the age counter.*
- `__init__` (line 768) `def __init__(self, layers, final_norm, reasoning_config, logger)`
- `num_layers` (line 789) `def num_layers(self)` - *Return the number of trained transformer layers.*
- `_full_pass` (line 793) `def _full_pass(self, z_in, base_kvs)` - *Forward z_in through every layer using base_kvs as immutable prefix cache.

Returns the layer-stack output and the freshly produced per-layer kv
caches that incorporate the K and V derived from z_in.*
- `_window_pass` (line 808) `def _window_pass(self, z_in, base_kvs, window)` - *Forward z_in through the trailing `window` layers only.

The per-layer kv caches produced during this read-only pass are
discarded; only the baseline pass's committed kvs cross the token
boundary, preserving cache consistency across thinking iterations.*
- `reason` (line 827) `def reason(self, z_initial, base_kvs, cached_refinement)` - *Run hierarchical recursive thinking for a single emission step.

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
- `__init__` (line 938) `def __init__(self, logger)`
- `sample` (line 941) `def sample(self, logits, token_history, temperature, top_k, repetition_penalty)` - *Return a sampled token id tensor of shape [B, 1] from raw logits [B, V].*
- `from_settings` (line 973) `def from_settings(cls, settings)` - *Construct a SamplingPolicy from inference settings.*
- `tokens_per_second` (line 995) `def tokens_per_second(self, elapsed_floor)` - *Return throughput in tokens/sec, clamped to avoid divide-by-zero.*
- `__init__` (line 1011) `def __init__(self, settings, logger)`
- `_encode_prompt` (line 1016) `def _encode_prompt(self, model, prompt_ids)` - *Run the prompt through the full stack once, returning the final
hidden state of the last position, the per-layer base kv caches that
cover all prompt tokens except the last one, and the embedding of the
last prompt token as the seed for the first reasoning episode.*
- `run` (line 1048) `def run(self, model, tokenizer, prompt, policy)` - *Generate a completion for prompt and return a GenerationReport.*
- `__init__` (line 1192) `def __init__(self, settings, logger)`
- `render` (line 1196) `def render(self, report)` - *Emit a banner with prompt, completion, throughput and reasoning stats.*
- `__init__` (line 1233) `def __init__(self, settings, logger)`
- `execute` (line 1239) `def execute(self)` - *Run the full inference pipeline end-to-end and return the report.*
- `build_parser` (line 1287) `def build_parser()` - *Return the configured argparse.ArgumentParser.*
- `parse` (line 1448) `def parse(argv)` - *Parse argv (or sys.argv) and return a populated HRMInferenceSettings.*

#### `jlens.py`
**Path:** `topogpt3/jlens.py`

**Classes:**
- `TopoGPT3JLensFitConfig` (line 37) `class TopoGPT3JLensFitConfig` - *Centralized configuration for Jacobian lens fitting.

Every value consumed downstream resides here. Adding a new tunable means
extending this class; no other module should embed literals.*
- `TopoGPT3JLensAppConfig` (line 56) `class TopoGPT3JLensAppConfig` - *Centralized configuration for Jacobian lens application.

Every value consumed downstream resides here. Adding a new tunable means
extending this class; no other module should embed literals.*
- `ActivationRecorder` (line 69) `class ActivationRecorder` - *Captures residual-stream tensors at the given block indices.

Registers a forward hook on each requested block on ``__enter__`` and
removes them on ``__exit__``. On the next forward pass each block's output
is stored in ``activations``, keyed by block index. Stored tensors are
not detached, so they can be passed straight to ``torch.autograd.grad``.

Args:
    blocks: The sequence of residual blocks (e.g. ``model.layers``).
    at: Block indices to record at.
    start_graph_at: If given, the captured tensor at this index is marked
        ``requires_grad_(True)`` before downstream blocks see it. When the
        model's parameters all have ``requires_grad=False``, this makes the
        captured residual the leaf that roots the autograd graph, so the
        retained graph spans only this block onward.*
- `JacobianLens` (line 459) `class JacobianLens` - *A fitted Jacobian lens: per-layer ``J_l`` matrices and the readout method.

Attributes:
    jacobians: ``{layer_index: Tensor[d_model, d_model]}``. Each ``J_l``
        maps the residual at layer ``l`` into the final-layer basis.
    source_layers: Sorted list of fitted layer indices.
    n_prompts: Number of prompts the lens was averaged over.
    d_model: Residual-stream width.*
- `SliceData` (line 664) `class SliceData` - *Text-format slice data: top-K token predictions per (position, layer).

``layers`` always includes the model's final layer (the actual model
output) so divergences from lens-transported earlier layers are visible.

Attributes:
    seq_len: Number of token positions in the slice.
    layers: Layer indices shown (includes final layer).
    prompt: The input prompt text.
    input_ids: Tensor ``[1, seq_len]`` of token IDs.
    token_strs: Decoded strings for each token position.
    top_ids: ``[seq_len, n_layers, top_n]`` top token IDs per cell.
    top_probs: ``[seq_len, n_layers, top_n]`` softmax probabilities.
    top_token_strs: ``[seq_len, n_layers, top_n]`` decoded token strings
        for each prediction. Empty string if tokenizer was unavailable.*

**Methods:**
- `valid_position_mask` (line 132) `def valid_position_mask(seq_len)` - *Boolean mask over sequence positions to include in the Jacobian average.

Early positions are dominated by attention-sink behaviour and the final
position has no next-token target, so both are excluded.

Args:
    seq_len: Length of the tokenized prompt.
    skip_first: Number of leading positions to exclude.

Returns:
    Boolean tensor of shape ``[seq_len]``.

Raises:
    ValueError: If ``skip_first`` is negative or the prompt is too short to
        leave any valid positions.*
- `_check_layer_indices` (line 162) `def _check_layer_indices(source_layers, target_layer, n_layers)` - *Resolve None/negative layer indices, bounds-check, enforce source < target.*
- `jacobian_for_prompt` (line 187) `def jacobian_for_prompt(model, prompt, source_layers)` - *Compute the per-layer Jacobian estimator ``J_l`` for one prompt.

Runs one forward pass on the prompt replicated ``dim_batch`` times along
the batch axis, retains the graph, then runs ``ceil(d_model / dim_batch)``
backward passes against it. Each backward computes ``dim_batch`` rows of
``J_l`` at once: batch element ``b`` carries a one-hot cotangent at output
dimension ``dim_start + b``, set at every valid target position.

Args:
    model: The model to compute Jacobians for.
    prompt: Input text.
    source_layers: Layer indices ``l`` to compute ``J_l`` at.
    target_layer: Layer to take gradients with respect to. Defaults to the
        final layer; negative indices count from the end.
    dim_batch: Output dimensions computed per backward pass.
    max_seq_len: Truncate the prompt to this many tokens.
    skip_first: Leading positions to exclude.

Returns:
    ``(jacobians, seq_len, n_valid_positions)``. ``jacobians`` maps each
    source layer to a ``[d_model, d_model]`` fp32 CPU tensor.*
- `_atomic_save` (line 283) `def _atomic_save(obj, path)` - *``torch.save`` to a temp file then ``os.replace`` so a crash never
leaves a half-written checkpoint.*
- `fit` (line 291) `def fit(model, prompts)` - *Fit ``J_l`` over a list of prompts and return a JacobianLens.

Per-prompt Jacobians from ``jacobian_for_prompt`` are accumulated as a
running mean. If ``checkpoint_path`` is set, the running sum is written
every ``checkpoint_every`` prompts (atomic) and resumed from on restart.

Args:
    model: The model to fit on.
    prompts: Text prompts to average over.
    source_layers: Layers to fit at. Defaults to every layer below
        ``target_layer``; negative indices count from the end.
    target_layer: See ``jacobian_for_prompt``.
    dim_batch: See ``jacobian_for_prompt``.
    max_seq_len: Truncate each prompt to this many tokens.
    skip_first: See ``jacobian_for_prompt``.
    checkpoint_path: If set, write a resumable checkpoint here.
    checkpoint_every: Write checkpoint every N prompts (default 1).
    resume: If True and checkpoint_path exists, resume from it.

Returns:
    The fitted JacobianLens.

Raises:
    ValueError: If no prompts are long enough to fit on, or if checkpoint
        settings mismatch.*
- `compute_slice` (line 705) `def compute_slice(model, lens, prompt)` - *Compute a position x layer slice of top-K token predictions.

For each layer in the fitted lens, projects the residual at each position
through the Jacobian into the final-layer basis, then unembeds to get
logits and softmax probabilities. Returns the top-N predicted token IDs
and their probabilities per (position, layer) cell.

Args:
    model: The model to read out from.
    lens: A fitted JacobianLens.
    prompt: Input text.
    top_n: Top tokens to keep per (position, layer) cell.
    max_seq_len: Truncate the prompt to this many tokens.

Returns:
    A SliceData instance with arrays indexed ``[seq_len, n_layers, top_n]``.*
- `text_slice` (line 789) `def text_slice(slice_data, tokenizer, n_cols)` - *Render a SliceData as a readable text table showing decoded words.

For each token position, shows what each layer predicts as the next token.
The first column shows the actual input token; subsequent columns show the
top-1 prediction at each layer with its softmax probability. Token strings
are read from ``slice_data.top_token_strs`` (always populated by
``compute_slice``).

Args:
    slice_data: The slice to render.
    tokenizer: Legacy parameter, ignored. Top token strings are already
        stored in ``slice_data.top_token_strs``.
    n_cols: Number of layer columns to show (default 3).

Returns:
    A multi-line string table.*
- `_demo_jlens` (line 842) `def _demo_jlens()` - *Run a full jacobian lens demo loading real weights from checkpoint.*
- `__init__` (line 87) `def __init__(self, blocks, at)`
- `_make_hook` (line 102) `def _make_hook(self, index)`
- `__enter__` (line 113) `def __enter__(self)`
- `__exit__` (line 126) `def __exit__(self)`
- `write_checkpoint` (line 378) `def write_checkpoint()`
- `__init__` (line 470) `def __init__(self, jacobians)`
- `__repr__` (line 482) `def __repr__(self)`
- `save` (line 489) `def save(self, path)` - *Save to ``path``. Jacobians are stored as ``dtype`` (default fp16).*
- `load` (line 504) `def load(cls, path)` - *Load a lens previously written by ``save``.*
- `from_pretrained` (line 519) `def from_pretrained(cls, name_or_path)` - *Load a lens from a local file, a local directory, or a HuggingFace
Hub ``repo_id``.

``filename`` is the path inside the directory or repo; ignored when
``name_or_path`` is itself a file. ``revision`` selects a Hub branch,
tag, or commit.*
- `merge` (line 543) `def merge(cls, lenses)` - *Combine lenses fitted on disjoint prompt subsets into one
(``n_prompts``-weighted mean of the inputs).

Args:
    lenses: Lenses to merge. Must agree on ``source_layers`` and
        ``d_model``.

Raises:
    ValueError: If ``lenses`` is empty or the inputs disagree on shape.*
- `transport` (line 574) `def transport(self, residual, layer)` - *Map a residual at ``layer`` into the final-layer basis: ``J_l @ h``.

Args:
    residual: Tensor of shape ``[..., d_model]``.
    layer: Source layer index (must be in ``source_layers``).*
- `apply` (line 585) `def apply(self, model, prompt)` - *Run ``model`` on ``prompt`` and return lens logits at ``positions``.

Args:
    model: The model to read out from.
    prompt: Input text.
    layers: Layers to read out at. Defaults to all of
        ``source_layers``. Must be a subset of ``source_layers`` when
        ``use_jacobian`` is True.
    positions: Token positions to read out (Python indexing into the
        sequence; negative indices count from the end). None returns
        every position.
    max_seq_len: Truncate the prompt to this many tokens.
    use_jacobian: If False, skip the ``J_l`` transport (vanilla
        logit-lens baseline).

Returns:
    A triple ``(lens_logits, model_logits, input_ids)``. ``lens_logits``
    maps each requested layer to a ``[n_positions, vocab_size]`` tensor;
    ``model_logits`` is the model's actual final-layer logits at the
    same positions (same shape).

Raises:
    ValueError: If any requested layer is out of range for the model,
        or (with use_jacobian) not in source_layers.*
- `__post_init__` (line 692) `def __post_init__(self)`
- `hook` (line 105) `def hook(module, inputs, output)`
- `select` (line 646) `def select(layer)`

#### `lens_model.py`
**Path:** `topogpt3/lens_model.py`

**Classes:**
- `LensModel` (line 23) `class LensModel(Protocol)` - *What the lens needs from a model.

Attributes:
    n_layers: Number of residual blocks.
    d_model: Residual-stream width.
    layers: The residual blocks, indexable by integer; what
        ActivationRecorder hooks.
    tokenizer: Tokenizer used by the visualisation helpers; must provide
        ``decode(token_ids) -> str``. Fitting and apply() never touch it.*
- `TopoGPT3LensConfig` (line 59) `class TopoGPT3LensConfig` - *Centralized configuration for the TopoGPT3 lens model adapter.

Every value consumed downstream resides here. Adding a new tunable means
extending this class; no other module should embed literals.*
- `_TopoGPT3ResidualForward` (line 142) `class _TopoGPT3ResidualForward(Module)` - *Runs the residual block stack only (no final norm, no LM head).

This is the forward subgraph that ActivationRecorder hooks capture.
Extracted from TopoGPT2.forward() to expose the residual stream for
Jacobian lens fitting and application.*
- `TopoGPT3LensModel` (line 161) `class TopoGPT3LensModel(Module)` - *LensModel adapter over a loaded TopoGPT2 model.

Wraps a TopoGPT2 instance and implements the LensModel protocol for use
with ActivationRecorder, JacobianLens fitting, and apply().

The adapter owns no parameters --- all weights live in the wrapped model.
Call ``.eval()`` and set ``requires_grad_(False)`` on the wrapped model
before fitting.*
- `TinyDecoder` (line 306) `class TinyDecoder(Module)` - *A tiny CPU-only decoder for end-to-end tests.

Implements the LensModel protocol indirectly (wrapped by
TopoGPT3LensModel). Residual blocks are ``h + 0.1 * linear(h)``:
the small gain keeps the Jacobian well-conditioned so the late-layer
``diag(J) ~= 1`` property holds.*
- `_ResidualBlock` (line 359) `class _ResidualBlock(Module)`

**Methods:**
- `encode` (line 40) `def encode(self, text)` - *Tokenize ``text`` to ``input_ids`` of shape ``[1, seq_len]`` on the
model's input device.*
- `forward` (line 45) `def forward(self, input_ids)` - *Run the residual stack on ``input_ids`` (no LM head). Must build an
autograd graph through layers when grad is enabled, and must be
deterministic across batch elements (eval mode, dropout off) --- the
fitting estimator replicates the prompt along the batch axis.*
- `unembed` (line 52) `def unembed(self, residual)` - *Map a residual-stream tensor ``[..., d_model]`` to logits
``[..., vocab_size]`` (final norm + LM head).*
- `from_topogpt2_config` (line 84) `def from_topogpt2_config(cls, cfg)` - *Construct a lens config from a TopoGPT2Config dataclass.*
- `probe_checkpoint` (line 104) `def probe_checkpoint(cls, checkpoint_dir)` - *Probe a checkpoint directory and infer lens config from state.json.

Args:
    checkpoint_dir: Path to the checkpoint slot directory.
    state_filename: JSON file containing training config.

Returns:
    A TopoGPT3LensConfig matching the checkpoint.

Raises:
    FileNotFoundError: If state.json is missing.
    ValueError: If required fields are absent from the state.*
- `__init__` (line 150) `def __init__(self, model)`
- `forward` (line 154) `def forward(self, input_ids)`
- `__init__` (line 172) `def __init__(self, model, tokenizer)`
- `n_layers` (line 184) `def n_layers(self)`
- `d_model` (line 188) `def d_model(self)`
- `layers` (line 192) `def layers(self)`
- `tokenizer` (line 196) `def tokenizer(self)`
- `tokenizer` (line 200) `def tokenizer(self, tok)`
- `input_device` (line 204) `def input_device(self)`
- `input_device` (line 210) `def input_device(self, device)`
- `encode` (line 213) `def encode(self, text)` - *Tokenize text to input_ids of shape ``[1, seq_len]``.

Uses BPETokenizer if available, otherwise falls back to a byte-level
encoding compatible with GPT-2 BPE tokenization.*
- `forward` (line 228) `def forward(self, input_ids)` - *Run the residual stack on ``input_ids``.

Returns hidden states of shape ``[batch, seq_len, d_model]``
(pre-final-norm, pre-LM-head). The autograd graph is retained through
all layers when grad is enabled.*
- `unembed` (line 237) `def unembed(self, residual)` - *Map residual ``[..., d_model]`` to logits ``[..., vocab_size]``.

Applies the model's final norm and LM head projection.*
- `from_checkpoint` (line 246) `def from_checkpoint(cls, checkpoint_dir)` - *Build a TopoGPT3LensModel from a checkpoint directory.

Probes state.json for configuration, instantiates the model, loads
safetensors weights, and wraps the result.

Args:
    checkpoint_dir: Path to the checkpoint slot directory.
    device: Target device. Defaults to cuda if available else cpu.
    encoding: Tokenizer encoding name (passed to BPETokenizer).
    strict: Whether to enforce strict state dict loading.

Returns:
    A TopoGPT3LensModel in eval mode with requires_grad_(False).

Raises:
    FileNotFoundError: If model.safetensors or state.json is missing.*
- `__init__` (line 315) `def __init__(self, n_layers, d_model, vocab_size, seed)`
- `forward` (line 344) `def forward(self, token_ids, past_kvs)`
- `__init__` (line 360) `def __init__(self, d_model)`
- `forward` (line 366) `def forward(self, x, past_kv)`

#### `model.py`
**Path:** `topogpt3/model.py`

**Classes:**
- `TopoGPT2Config` (line 56) `class TopoGPT2Config` - *Configuración completa para TopoGPT2.*
- `QuaternionOps` (line 214) `class QuaternionOps` - *Operaciones de cuaterniones puras en PyTorch.
Representación: [..., 4]  donde last dim = [w, x, y, z]
q = w + x*i + y*j + z*k*
- `QuaternionLinear` (line 253) `class QuaternionLinear(Module)` - *Capa lineal con pesos cuaterniones.

Implementa la multiplicación W * x en el álgebra de cuaterniones:
- W = Ww + Wx*i + Wy*j + Wz*k  (cuaternión de pesos)
- x = xw + xx*i + xy*j + xz*k  (cuaternión de entrada)
- out = W * x  (producto de Hamilton extendido a vectores)

Parámetros: 4 matrices reales de forma [out_q, in_q]*
- `QuaternionSpectralLayer` (line 298) `class QuaternionSpectralLayer(Module)` - *Convolución espectral 2D con cuaterniones y producto de Hamilton completo.

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
- `SpectralAutoencoder` (line 385) `class SpectralAutoencoder(Module)` - *Autoencoder espectral con cuaterniones.

Opera en dos niveles:
1. Espectral 1D sobre el vector de features (FFT sobre dim D_MODEL):
   captura la espectrografía global del embedding.
2. Espectral 2D sobre el grid del toro (QuaternionSpectralLayer):
   captura correlaciones espaciales en la topología.

Devuelve (latent, recon_loss) para regularización.*
- `QuaternionTorusBrain` (line 468) `class QuaternionTorusBrain(Module)` - *Reemplaza el MLP en cada capa del transformer.

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
- `RotaryEmbedding` (line 685) `class RotaryEmbedding(Module)` - *Rotary Position Embeddings (RoPE) - Su et al., 2021.
Codifica la posicion como rotaciones del espacio de atencion,
naturalmente relativas y sin parametros extra.

Las caches _cos/_sin se registran como buffers no-persistentes con
nombres que no colisionan con checkpoints antiguos (que usaban
'cos_cache'/'sin_cache'). Esto permite cambiar MAX_SEQ_LEN sin
errores de shape al cargar checkpoints previos.*
- `RMSNorm` (line 739) `class RMSNorm(Module)` - *Root Mean Square Layer Normalization (sin bias). Más estable que LayerNorm.*
- `SwiGLU` (line 756) `class SwiGLU(Module)` - *SwiGLU: SiLU(gate(x)) * up(x) -> down
Usado en LLaMA 2/3, Qwen, Mistral en lugar de GELU-FFN.
Dimension interna: 8/3 * d_model (convención LLaMA, redondeada a múltiplo de 4).*
- `TopoMoEBrain` (line 785) `class TopoMoEBrain(Module)` - *Mixture of Experts sobre la capa topologica.

Arquitectura (inspirada en DeepSeek-MoE / Mixtral):
  - 1 experto compartido: QuaternionTorusBrain (siempre activo)
  - N_EXPERTS expertos SwiGLU ligeros (activacion esparsa: Top-K por token)
  - Router: Linear(D, N_EXPERTS) + softmax → top-K

Load-balancing loss (auxiliar): penaliza si un experto acapara todos los tokens.
Activa MOE_TOP_K de N_EXPERTS expertos por token.

Sin MoE (MOE_ENABLED=False): se comporta como QuaternionTorusBrain puro.*
- `MultiHeadAttention` (line 890) `class MultiHeadAttention(Module)` - *Multi-head attention con:
- Flash Attention (scaled_dot_product_attention de PyTorch 2.0+)
- Rotary Position Embeddings (RoPE)
- GQA (Grouped Query Attention): N_KV_HEADS < N_HEADS, reduce VRAM de K/V
- KV Cache para inferencia autoregresiva eficiente
- Temperatura termodinámica aprendible*
- `TopoGPT2Layer` (line 994) `class TopoGPT2Layer(Module)` - *Capa del transformer con TopoMoEBrain (TopoBrain + MoE SwiGLU experts).

Esquema pre-norm (estilo LLaMA):
    x = x + Attention_GQA(RMSNorm(x))
    x = x + TopoMoEBrain(RMSNorm(x))*
- `TopoGPT2` (line 1041) `class TopoGPT2(Module)` - *TopoGPT2: Transformer de lenguaje con TopoBrain cuaternión-espectral.

Arquitectura:
    Embedding de tokens + RoPE (en Attention)
    N_LAYERS × TopoGPT2Layer (Attention + QuaternionTorusBrain)
    RMSNorm final
    Proyección a vocabulario (weight-tied con embeddings)*
- `BPETokenizer` (line 1258) `class BPETokenizer` - *Wrapper alrededor de tiktoken (GPT-2 compatible).*
- `FileManifest` (line 1384) `class FileManifest` - *Disk-cached manifest of text files found in a directory tree.*
- `MemmapTokenizer` (line 1451) `class MemmapTokenizer` - *Tokenizes file paths into a memory-mapped numpy array on disk.

Uses incremental file reading and batched writing to avoid loading
all tokens into RAM. Tokens are stored as raw int64 on disk and
accessed via numpy memmap (OS-level paging, near-zero RAM footprint).*
- `MappedTokenDataset` (line 1540) `class MappedTokenDataset(Dataset)` - *Memory-mapped token dataset for sequence-to-sequence LM training.

The token array is backed by a numpy memmap file on disk.
Only accessed slices are paged into RAM by the OS. The .copy()
in __getitem__ ensures the returned torch.Tensor owns its memory,
which is required for DataLoader collation with worker processes.*
- `TextFilter` (line 1574) `class TextFilter` - *Filters low-quality files from the corpus based on multiple heuristics.*
- `CurriculumDataset` (line 1678) `class CurriculumDataset(Dataset)` - *Tiered dataset that exposes short/medium/all files based on line count.

Works as a wrapper around MappedTokenDataset. Provides __getitem__ that
only samples from the active tier, avoiding dataset duplication.*
- `ProgressiveSeqLenTrainer` (line 1742) `class ProgressiveSeqLenTrainer` - *Trainer that dynamically adjusts MAX_SEQ_LEN across training phases.

Phase schedule (configurable):
    phase 0: seq_len=128, epochs=3
    phase 1: seq_len=256, epochs=3
    phase 2: seq_len=512, epochs=4

Each phase rebuilds the DataLoader with the new sequence length.*
- `SpeculativeDecoder` (line 1818) `class SpeculativeDecoder` - *Speculative decoding with a small draft model.

Draft model uses SPEC_DECODE_DRAFT_SCALE (e.g. 'micro').
The draft generates K tokens, then the target model verifies them
in a single forward pass. Accepted tokens are kept; rejected ones
trigger a fallback to the target model sampling.*
- `QuantizedEmbedding` (line 1933) `class QuantizedEmbedding(Module)` - *Wrapper around nn.Embedding that applies dynamic quantization.

Applies int8 quantization to the embedding weight matrix after loading.
Supports both embed (int8) and FFN (int4) quantization modes.*
- `CurriculumTrainer` (line 2001) `class CurriculumTrainer` - *Extends TopoGPT2Trainer with curriculum + progressive seq len support.

Provides:
- Tokens cache for progressive sequence length rebuilding
- Curriculum dataset wrapping (short / medium / all tiers)*
- `CheckpointManager` (line 2153) `class CheckpointManager` - *Gestiona checkpoints de forma acumulativa y segura.

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
- `TopoGPT2Trainer` (line 2386) `class TopoGPT2Trainer` - *Entrenador acumulativo y resumible.

Caracteristicas:
- Checkpoint automatico en safetensors cada N minutos + cada epoch
- Historial acumulativo entre sesiones (--resume agrega al historial existente)
- Guarda el mejor modelo en checkpoints/best/ automaticamente
- LR schedule: cosine con warmup relativo a los steps de ESTA sesion
- Mixed Precision (AMP) + acumulacion de gradientes*
- `MechanisticMetrics` (line 2679) `class MechanisticMetrics` - *Calcula todas las metricas del diagrama de fases de Book.md.

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
- `Phase0_KernelOptimizer` (line 2916) `class Phase0_KernelOptimizer` - *Encuentra el ratio imaginario/real optimo para los kernels espectrales.

Analogia con main.py: evalua la transicion GOE→GUE en el espacio
de kernels. Un ratio optimo promueve estructura topologica (insulador)
vs estructura amorfa (vidrio).

Metodo: calibra con un mini-batch y mide la varianza del gradiente
en funcion del ratio. Ratios que minimizan la varianza de gradiente
(maxima coherencia espectral) son preferibles.

No entrena: solo inicializa los kernels con distintos ratios y mide.
Tiempo tipico: < 30 segundos.*
- `Phase1_BatchProspector` (line 2991) `class Phase1_BatchProspector` - *Encuentra el batch size optimo testando candidatos con pocos pasos.

De main.py: el batch size regula la temperatura del horno de cristalizacion.
Batch sizes demasiado chicos -> ruido excesivo (vidrio frio).
Batch sizes demasiado grandes -> sin presion annealing (amorfos).
La ventana optima empirica de main.py: [24, 128] para Strassen.

Para LM, testeamos candidatos midiendo:
- delta (δ): velocidad de descenso en prospect_steps pasos
- T_eff: temperatura efectiva del gradiente

Tiempo tipico: < 2 minutos para 3 candidatos × 30 pasos.*
- `Phase2_SeedMiner` (line 3074) `class Phase2_SeedMiner` - *Encuentra semillas prometedoras midiendo la trayectoria de delta.

De main.py: una semilla "buena" muestra delta descendente en los
primeros N pasos (enfriamiento). Una semilla "mala" se estanca en
el plateau vidrioso (~0.49).

Criterio de seleccion:
1. Semillas con delta_velocity < 0 (enfriando) AND kappa bajo.
2. Si no hay, semillas solo enfriando.
3. Fallback: semilla con menor delta final.

Tiempo tipico: < 3 minutos para 5 semillas × 50 pasos.*
- `Phase4_AnnealingRefiner` (line 3156) `class Phase4_AnnealingRefiner` - *Refinamiento post-entrenamiento mediante recocido simulado.

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
- `TopoPhasePipelineV2` (line 3317) `class TopoPhasePipelineV2` - *Pipeline with curriculum learning and progressive sequence length.

Replaces TopoPhasePipeline when --curriculum or --progressive-seq-len is set.
Handles:
- Text quality filtering before tokenization (via TextFilter)
- Curriculum tiers (short/medium/all files)
- Progressive MAX_SEQ_LEN across phases: 128->256->512
- Tokens cached in memory for fast DataLoader rebuilding per phase*
- `TopoPhasePipeline` (line 3446) `class TopoPhasePipeline` - *Orquesta las 5 fases de entrenamiento segun main.py + Book.md.

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

**Methods:**
- `setup_logger` (line 192) `def setup_logger(name, level)`
- `set_seed` (line 202) `def set_seed(seed, device)`
- `build_file_tiers` (line 1716) `def build_file_tiers(paths, short, med)` - *Classify file paths into complexity tiers by line count.

Returns dict: tier -> list of file indices in that tier.
Tier 0 = short (<=short lines), tier 1 = medium, tier 2 = all.*
- `apply_quantization` (line 1973) `def apply_quantization(model, config)` - *Quantize embedding and lm_head layers for reduced VRAM usage.*
- `_tokenize_text_to_memmap` (line 2141) `def _tokenize_text_to_memmap(text, tokenizer, path, max_tokens)` - *Tokenize a single text string and write tokens to disk as raw int64.*
- `main` (line 3568) `def main()`
- `__post_init__` (line 161) `def __post_init__(self)`
- `hamilton_product` (line 222) `def hamilton_product(q1, q2)` - *Producto de Hamilton q1 ⊗ q2. Ambos [..., 4].*
- `normalize` (line 234) `def normalize(q, eps)`
- `conjugate` (line 238) `def conjugate(q)`
- `rotate_vector` (line 243) `def rotate_vector(v, q)` - *Rota vector 3D v por cuaternión unitario q. v:[...,3] q:[...,4]*
- `__init__` (line 265) `def __init__(self, in_features, out_features, bias)`
- `forward` (line 281) `def forward(self, x)` - *x: [..., in_features] → [..., out_features]*
- `__init__` (line 318) `def __init__(self, in_q, out_q, grid_h, grid_w, init_scale)`
- `_kernel` (line 337) `def _kernel(self, c)`
- `_contract` (line 340) `def _contract(self, W, X)` - *Suma sobre canales in_q: Y[b,o,h,w] = Σ_i W[i,o,h,w]·X[b,i,h,w]*
- `forward` (line 344) `def forward(self, x)` - *x: [B, 4*in_q, H, W]  (4 canales cuaterniones sobre grid espacial)
→ [B, 4*out_q, H, W]*
- `__init__` (line 398) `def __init__(self, config)`
- `_filter1d` (line 430) `def _filter1d(self, x, kr, ki)` - *Filtro espectral 1D: x[..., D] → filtrado[..., D]*
- `encode` (line 436) `def encode(self, x)` - *x: [..., D_MODEL] → latent: [..., D_LAT]*
- `decode` (line 441) `def decode(self, z)` - *z: [..., D_LAT] → recon: [..., D_MODEL]*
- `forward` (line 446) `def forward(self, x)` - *Devuelve (latent, recon_loss)*
- `process_torus_grid` (line 453) `def process_torus_grid(self, grid)` - *Procesa el grid del toro con QuaternionSpectralLayer.
grid: [B, 4*D_QUAT, RADIAL, ANGULAR]  →  [B, 4*D_QUAT, RADIAL, ANGULAR]*
- `__init__` (line 486) `def __init__(self, d_model, config)`
- `_build_torus_graph` (line 526) `def _build_torus_graph(self)` - *Construye las aristas del grafo toro 2×4.

Nodos indexados como: node = r * N_ANGULAR + a
  r ∈ [0, RADIAL-1], a ∈ [0, ANGULAR-1]

Aristas angulares: nodo ↔ nodo a la izquierda/derecha (periódico)
Aristas radiales:  nodo ↔ nodo del anillo interior/exterior*
- `_torus_soft_assign` (line 560) `def _torus_soft_assign(self, phi1, phi2)` - *Asignación blanda de tokens a los 8 nodos del toro via distancia circular.

phi1: [BS] ángulo angular ∈ [-π, π]
phi2: [BS] ángulo radial ∈ [-π, π]
→ weights: [BS, N_NODES]  (suma a 1, softmax de distancias negativas)*
- `_message_passing` (line 587) `def _message_passing(self, node_feat)` - *Message-passing VECTORIZADO con rotaciones cuaterniones.
Sin bucles Python: todas las aristas se procesan en paralelo.

node_feat: [BS, N_NODES, D_MODEL]
→ [BS, N_NODES, D_MODEL]*
- `forward` (line 624) `def forward(self, x)` - *x: [B, S, D_MODEL]
→ output: [B, S, D_MODEL], recon_loss: scalar*
- `__init__` (line 697) `def __init__(self, d_head, max_seq_len, base)`
- `_build_cache` (line 703) `def _build_cache(self, seq_len)`
- `_rotate_half` (line 711) `def _rotate_half(self, x)`
- `forward` (line 715) `def forward(self, q, k, seq_len, offset)` - *q, k: [B, n_heads, S_q/S_k, d_head]
offset: posicion inicial (para KV cache: longitud del cache existente)
Aplica posiciones [offset .. offset+S-1] a q y k.*
- `__init__` (line 742) `def __init__(self, d_model, eps)`
- `forward` (line 747) `def forward(self, x)`
- `__init__` (line 763) `def __init__(self, d_model, expansion, dropout)`
- `forward` (line 777) `def forward(self, x)`
- `__init__` (line 800) `def __init__(self, d_model, config)`
- `_route` (line 821) `def _route(self, x)` - *x: [N, D] donde N = B*S (tokens aplanados)
Retorna:
expert_out: [N, D]  suma ponderada de top-K expertos
aux_loss:   escalar  load-balancing loss
Routing vectorizado sin boolean indexing ni sincronizacion CUDA.
Usa dispatch por indices agrupados (estilo Mixtral/DeepSeek) para
compatibilidad total con torch.utils.checkpoint.*
- `forward` (line 863) `def forward(self, x)` - *x: [B, S, D]
→ output: [B, S, D], aux_loss: escalar*
- `__init__` (line 900) `def __init__(self, d_model, n_heads, config)`
- `forward` (line 919) `def forward(self, x, is_causal, past_kv)` - *Args:
    x:        [B, S, D]
    is_causal: usar mascara causal
    past_kv:  (K_cache, V_cache) de pasos anteriores o None
Returns:
    out:      [B, S, D]
    kv_cache: (K, V) completos para cachear en generate()*
- `__init__` (line 1003) `def __init__(self, d_model, n_heads, config)`
- `_forward_impl` (line 1012) `def _forward_impl(self, x, past_kv)`
- `forward` (line 1021) `def forward(self, x, past_kv)` - *Retorna (x_out, aux_loss, kv_cache).
Con gradient checkpointing en training (solo cuando no hay KV cache).*
- `__init__` (line 1052) `def __init__(self, config)`
- `_init_weights` (line 1077) `def _init_weights(self)`
- `forward` (line 1084) `def forward(self, token_ids, past_kvs)` - *token_ids: [B, S]  (enteros)
past_kvs:  lista de (K, V) por capa, o None para entrenamiento
→ logits: [B, S, VOCAB_SIZE], aux_loss: scalar, new_kvs: list[(K,V)]*
- `forward_with_memory` (line 1107) `def forward_with_memory(self, token_ids)` - *Process long sequences with latent memory-token context compression.

Splits `token_ids` [B, S] into segments of size MEMORY_SEGMENT_LEN.
Each segment is processed with N_MEMORY_TOKENS prepended. The output
at memory-token positions after segment k becomes the memory-state
input for segment k+1, compressing all prior context into a fixed-size
latent vector.

Returns (logits [B, S, VOCAB_SIZE], aux_loss).*
- `count_params` (line 1157) `def count_params(self)`
- `generate` (line 1163) `def generate(self, token_ids, max_new_tokens, temperature, top_k, repetition_penalty)` - *Autoregressive generation with KV cache and top-k sampling.

Args:
    token_ids: [B, S_prompt] prompt tokens.
    max_new_tokens: Maximum tokens to generate.
    temperature: Sampling temperature (lower = more deterministic).
    top_k: Top-k filtering (0 = disabled).
    repetition_penalty: Penalty for repeating tokens (>1 = penalize).

Returns:
    [B, S_prompt + generated] full token sequence.*
- `generate_with_continuation` (line 1214) `def generate_with_continuation(self, token_ids, tokenizer, max_new_tokens, temperature, top_k, repetition_penalty, max_continuations, tail_lines)`
- `__init__` (line 1261) `def __init__(self, encoding)`
- `encode` (line 1269) `def encode(self, text)`
- `decode` (line 1272) `def decode(self, tokens)`
- `eot_token` (line 1275) `def eot_token(self)`
- `__init__` (line 1387) `def __init__(self, root, cache_dir, logger)`
- `scan` (line 1394) `def scan(self, force)` - *Walk directory tree collecting text file paths. Cached to disk.*
- `__init__` (line 1461) `def __init__(self, cache_dir, logger)`
- `tokenize` (line 1466) `def tokenize(self, file_paths, tokenizer, cache_key, max_tokens, min_chars)` - *Tokenize all files and return a memory-mapped numpy array.

Args:
    file_paths: List of absolute file paths to tokenize.
    tokenizer: BPE tokenizer instance.
    cache_key: Unique key for caching tokens to disk.
    max_tokens: Maximum number of tokens to produce.
    min_chars: Skip files with fewer characters.

Returns:
    np.ndarray backed by a memmap on disk. Only accessed pages
    are loaded into RAM by the OS virtual memory system.*
- `__init__` (line 1549) `def __init__(self, tokens, seq_len)`
- `__len__` (line 1554) `def __len__(self)`
- `__getitem__` (line 1557) `def __getitem__(self, idx)`
- `__init__` (line 1577) `def __init__(self, config, logger)`
- `_compute_entropy` (line 1586) `def _compute_entropy(self, text)` - *Shannon entropy of byte frequencies (bits per byte).*
- `_has_long_lines` (line 1600) `def _has_long_lines(self, text, threshold)` - *Return True if any line exceeds threshold characters.*
- `_special_token_ratio` (line 1607) `def _special_token_ratio(self, text, tokenizer)` - *Fraction of tokens that are pure whitespace or indentation-only.*
- `_content_hash` (line 1621) `def _content_hash(self, text)`
- `filter_file` (line 1624) `def filter_file(self, path, tokenizer)` - *Read and evaluate a file. Returns text if passed, None if filtered.*
- `report` (line 1664) `def report(self)`
- `__init__` (line 1685) `def __init__(self, tokens, seq_len, file_tiers, active_tier, logger)`
- `_update_len` (line 1695) `def _update_len(self)`
- `set_tier` (line 1701) `def set_tier(self, tier)`
- `__len__` (line 1705) `def __len__(self)`
- `__getitem__` (line 1708) `def __getitem__(self, idx)`
- `__init__` (line 1753) `def __init__(self, base_trainer)`
- `_build_dataloader` (line 1759) `def _build_dataloader(self, dataset, seq_len, batch_size, is_train)`
- `run` (line 1769) `def run(self, train_paths, val_paths, tokenizer, file_tiers, phases)` - *Run training with progressive sequence length across phases.*
- `__init__` (line 1827) `def __init__(self, target_model, config, logger)`
- `_build_draft` (line 1835) `def _build_draft(self)`
- `generate` (line 1849) `def generate(self, token_ids, max_new_tokens, temperature, top_k, repetition_penalty)` - *Autoregressive generation via speculative decoding.

Each round: draft generates K tokens, target verifies all K in
one O(1) forward pass (longest context), then samples the first
rejection from the target.*
- `__init__` (line 1940) `def __init__(self, embed, mode)`
- `forward` (line 1969) `def forward(self, indices)`
- `__init__` (line 2009) `def __init__(self, model, config, tokenizer)`
- `cache_tokens` (line 2016) `def cache_tokens(self, key, tokens)`
- `model` (line 2020) `def model(self)`
- `optimizer` (line 2024) `def optimizer(self)`
- `scaler` (line 2028) `def scaler(self)`
- `amp_dtype` (line 2032) `def amp_dtype(self)`
- `completed_epochs` (line 2036) `def completed_epochs(self)`
- `completed_epochs` (line 2040) `def completed_epochs(self, v)`
- `global_step` (line 2044) `def global_step(self)`
- `global_step` (line 2048) `def global_step(self, v)`
- `best_val_loss` (line 2052) `def best_val_loss(self)`
- `best_val_loss` (line 2056) `def best_val_loss(self, v)`
- `history` (line 2060) `def history(self)`
- `ckpt_mgr` (line 2064) `def ckpt_mgr(self)`
- `resume` (line 2067) `def resume(self)`
- `_current_state` (line 2070) `def _current_state(self)`
- `_cosine_lr` (line 2073) `def _cosine_lr(self)`
- `_set_lr` (line 2076) `def _set_lr(self)`
- `evaluate` (line 2079) `def evaluate(self, dataloader)`
- `_sample_text` (line 2082) `def _sample_text(self)`
- `_progressive_train` (line 2085) `def _progressive_train(self, train_paths, val_paths, tokenizer, phases, memtok)` - *Training loop with progressive sequence length across phases.*
- `train` (line 2124) `def train(self, train_dl, val_dl)`
- `run_curriculum` (line 2127) `def run_curriculum(self, train_paths, val_paths, tokenizer, phases)` - *Top-level entry point: curriculum + progressive seq len.*
- `__init__` (line 2178) `def __init__(self, config, logger)`
- `patch_config_for_resume` (line 2188) `def patch_config_for_resume(self, cfg)` - *Lee el checkpoint 'latest' y ajusta cfg.N_KV_HEADS / cfg.GQA_GROUPS
para que coincidan con la arquitectura guardada.
Necesario cuando el codigo cambio GQA despues de guardar el checkpoint.*
- `_save_model` (line 2217) `def _save_model(self, model, directory)`
- `_load_model` (line 2230) `def _load_model(self, model, directory)`
- `_save_optimizer` (line 2261) `def _save_optimizer(self, optimizer, directory)`
- `_load_optimizer` (line 2264) `def _load_optimizer(self, optimizer, directory, device)`
- `_save_state` (line 2273) `def _save_state(self, state, directory)`
- `_load_state` (line 2278) `def _load_state(self, directory)`
- `should_save` (line 2289) `def should_save(self)`
- `save` (line 2292) `def save(self, model, optimizer, state, is_best)` - *Guarda checkpoint completo.

state debe contener al menos: completed_epochs, global_step,
best_val_loss, history, config.*
- `load_latest` (line 2337) `def load_latest(self, model, optimizer)` - *Carga el ultimo checkpoint guardado.
Devuelve el state dict (vacio si no hay checkpoint).*
- `load_best` (line 2364) `def load_best(self, model)` - *Carga el mejor modelo guardado (solo pesos, sin optimizador).*
- `has_checkpoint` (line 2376) `def has_checkpoint(self)`
- `__init__` (line 2398) `def __init__(self, model, config, tokenizer)`
- `resume` (line 2433) `def resume(self)` - *Carga el ultimo checkpoint disponible.
Restaura: pesos del modelo, estado del optimizador, historial acumulado,
epoch/step completados y mejor val_loss.
Devuelve True si se cargo un checkpoint, False si empieza de cero.*
- `_current_state` (line 2458) `def _current_state(self)` - *Construye el dict de estado para persistir en state.json.*
- `_cosine_lr` (line 2469) `def _cosine_lr(self, step_in_session, total_steps_session)` - *Cosine decay con warmup. El schedule es relativo a la sesion actual.*
- `_set_lr` (line 2477) `def _set_lr(self, lr)`
- `train` (line 2481) `def train(self, train_dl, val_dl)` - *Entrena cfg.EPOCHS epocas adicionales a partir de completed_epochs.
El historial se acumula sobre sesiones previas.*
- `_sample_text` (line 2617) `def _sample_text(self, tokenizer, prompts, max_new, temperature, top_k)` - *Genera una muestra de texto al final de cada epoch para monitorear
la calidad cualitativa del modelo (detecta degeneracion, repeticion, etc.).*
- `evaluate` (line 2649) `def evaluate(self, dataloader)`
- `__init__` (line 2699) `def __init__(self, config)`
- `compute_delta` (line 2707) `def compute_delta(self, model)`
- `compute_alpha` (line 2714) `def compute_alpha(self, delta)`
- `update_grad_buffer` (line 2719) `def update_grad_buffer(self, model)` - *Captura gradientes de forma segura, ignorando tensores corruptos.*
- `compute_t_eff` (line 2745) `def compute_t_eff(self, lr)` - *T_eff = lr/2 * Var(gradiente). Temperatura termodinamica efectiva.*
- `compute_kappa` (line 2753) `def compute_kappa(self, model, dataloader, n_batches)` - *κ = λ_max / λ_min de la covarianza del gradiente.
Parámetro de orden para cristalización (κ≈1 = cristal).
Nota: requiere pasadas backward adicionales. Se ejecuta con protección
para no corromper el estado AMP del trainer principal.*
- `compute_berry_phase` (line 2811) `def compute_berry_phase(self, model)` - *Fase de Berry de los kernels espectrales imaginarios.
Surge de los parametros ki_w, ki_x, ki_y, ki_z de QuaternionSpectralLayer.
|berry|>pi/2 con winding!=0 indica estructura topologica.*
- `compute_lc` (line 2824) `def compute_lc(self, model)` - *Complejidad local: 1 - similitud coseno promedio entre filas de pesos.*
- `compute_sp` (line 2838) `def compute_sp(self, model)` - *Superposicion: correlacion inter-fila promedio (entrelazamiento de features).*
- `classify_phase` (line 2854) `def classify_phase(self, delta, kappa, berry)` - *Clasificacion de fase segun Book.md:

discrete_crystal:       delta<0.05, kappa<1.5
topological_insulator:  |berry|>pi/2, winding!=0
cold_glass:             kappa>>1, delta>0.3
functional_glass:       intermedio (lo mas comun en LM)*
- `compute_all` (line 2873) `def compute_all(self, model, lr, dataloader, compute_kappa)` - *Calcula todas las metricas.
compute_kappa=True hace pasadas backward adicionales (caro, usar cada N epochs).*
- `format_log` (line 2898) `def format_log(self, m)`
- `__init__` (line 2934) `def __init__(self, config, logger)`
- `_measure_ratio` (line 2938) `def _measure_ratio(self, ratio, sample_batch)` - *Mide la coherencia espectral para un ratio dado.
Retorna: varianza del gradiente (menor = mas coherente = mejor).*
- `optimize` (line 2967) `def optimize(self, dataloader)` - *Retorna el mejor ratio de inicializacion de kernels espectrales.*
- `__init__` (line 3007) `def __init__(self, config, logger)`
- `prospect` (line 3011) `def prospect(self, candidates, train_dataset, prospect_steps)` - *Retorna el mejor batch size segun delta y T_eff.*
- `__init__` (line 3090) `def __init__(self, config, logger)`
- `mine` (line 3094) `def mine(self, seed_start, n_seeds, train_dataset, prospect_steps)` - *Retorna la semilla con la mejor trayectoria de delta.*
- `__init__` (line 3176) `def __init__(self, trainer, t0, cooling_rate, stagnation_patience)`
- `refine` (line 3185) `def refine(self, train_dl, val_dl, refine_epochs)` - *Ejecuta refine_epochs epocas de recocido simulado.
Retorna el historial de refinamiento.*
- `__init__` (line 3328) `def __init__(self, config, train_tokens, val_tokens, tokenizer, logger, curriculum_tiers, progressive_seq)`
- `_build_dataloader` (line 3341) `def _build_dataloader(self, tokens, seq_len, batch_size, shuffle, tag)`
- `_build_phases` (line 3355) `def _build_phases(self)`
- `run` (line 3364) `def run(self, run_prospect, refine_epochs, resume, prospect_steps, probe_seeds, seed_start)`
- `__init__` (line 3466) `def __init__(self, config, train_dataset, val_dataset, tokenizer, logger)`
- `_make_dataloaders` (line 3476) `def _make_dataloaders(self, batch_size)`
- `run` (line 3488) `def run(self, run_prospect, refine_epochs, resume, prospect_steps, probe_seeds, seed_start)` - *Ejecuta el pipeline completo.
Retorna el trainer con el modelo entrenado.*
- `ckpt_fn` (line 1029) `def ckpt_fn(x_in)`

#### `train.py`
**Path:** `topogpt3/train.py`

**Classes:**
- `TopoGPT3Config` (line 83) `class TopoGPT3Config` - *Configuracion del pipeline TopoGPT3 (Grassmanniana + curriculum).*
- `GrassmannianTracker` (line 197) `class GrassmannianTracker` - *Observables geometricos sobre la trayectoria SGD.

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
- `EfficiencyMetrics` (line 585) `class EfficiencyMetrics` - *Mide y calcula los tres ratios pedidos:

  perf_per_param  =  (1 / val_ppl) / params_M
  perf_per_FLOP   =  tokens_per_sec / FLOPs_per_sec_aprox
  perf_per_BW     =  tokens_per_sec / bytes_moved_per_sec_aprox

FLOPs estimados con la heuristica de Kaplan/Hoffmann:
    FLOPs_forward_per_token ~= 2 * N_no_embed
    FLOPs_total_per_token  ~= 6 * N_no_embed       (forward + backward)
Bandwidth estimada como params_bytes leidos + activations_bytes movidas por step.
tokens_per_sec se cronometra empiricamente sobre el dataloader.*
- `CodeCurriculumLoader` (line 713) `class CodeCurriculumLoader` - *    Carga los 4 datasets, normaliza cada ejemplo a una unica cadena de texto,
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
- `BlockTokenDataset` (line 1000) `class BlockTokenDataset(Dataset)` - *Dataset autoregresivo sobre un stream de tokens.
Cada item es (x, y) con shape [seq_len].*
- `CheckpointStore` (line 1027) `class CheckpointStore` - *Persiste pesos del modelo + estado del trainer (sin AMP scaler para portabilidad).*
- `TopoGPT3Trainer` (line 1103) `class TopoGPT3Trainer` - *Orquesta el curriculum sobre los 4 tiers.

Pipeline por tier:
  1. Abre memmap de tokens (train/val/holdout).
  2. Construye DataLoaders con seq_len(tier).
  3. Entrena TIER_EPOCHS[tier] epocas con AMP + grad accum.
  4. Cada GRASS_TRACK_EVERY steps: snapshot Grassmanniano.
  5. Al final de cada epoca: eval en VAL.
  6. Al final del tier: eval en HOLDOUT (datos nunca vistos).
  7. Checkpoint y avanza al siguiente tier.

Al final del pipeline: eval en HOLDOUT *combinado* de los 4 tiers.*

**Methods:**
- `_gauss_complex_contract` (line 532) `def _gauss_complex_contract(self, W, X)` - *Sustituye QuaternionSpectralLayer._contract usando el truco de Gauss.

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
- `apply_gauss_patch` (line 568) `def apply_gauss_patch(logger)` - *Activa la version Gauss de _contract en QuaternionSpectralLayer.
Idempotente: solo parchea una vez por proceso.*
- `parse_args` (line 1538) `def parse_args()`
- `main` (line 1567) `def main()`
- `build_topogpt2_config` (line 170) `def build_topogpt2_config(self, max_seq_len, attn_window)`
- `__init__` (line 217) `def __init__(self, config, logger)`
- `_stack_spectral_kernels` (line 231) `def _stack_spectral_kernels(model)` - *Devuelve K(theta) en C^{N_f x N_c}:
  - filas = frecuencias planas (todos los modos espaciales de todos los kernels)
  - columnas = canales (in_q * out_q por componente cuaternionico, sumados)*
- `_elbow_rank` (line 268) `def _elbow_rank(self, sigmas)` - *Punto donde el valor singular cae por debajo de elbow_ratio * sigma_max.*
- `_dominant_subspace` (line 277) `def _dominant_subspace(self, K)` - *SVD compacta y truncada.
Devuelve (U_r, sigmas, r) con U_r en C^{N_f x r} ortonormal.*
- `_flatten_grads` (line 295) `def _flatten_grads(model, max_per_tensor)` - *Concatena un sub-sample de gradientes para mantener costo acotado.*
- `estimate_fisher_gap` (line 313) `def estimate_fisher_gap(self, model, dataloader, vocab_size, r_target)` - *Sigma_F ~= (1/M) sum_m g_m g_m^T  (covarianza muestral de gradientes).
Delta_F = lambda_{r_eff} - lambda_{r_eff+1}, donde r_eff = min(r_target, M-2)
para no salir del rango efectivo del estimador con M gradientes.
Devuelve (gap, eigs_desc, r_eff).*
- `_project_unitary` (line 381) `def _project_unitary(M)` - *Proyeccion a U(r) por descomposicion polar (M ~= U H -> retorna U).*
- `update_holonomy` (line 386) `def update_holonomy(self, U_new)` - *Holonomia discreta:
    T_n = U_n^dagger U_{n+1}  en C^{r x r}  (transporte paralelo discreto)
    U_Gamma <- T_n * U_Gamma  (acumulado)
Tras cada paso, U_Gamma se proyecta a U(r) para evitar deriva numerica.*
- `conjugation_distance_su2` (line 412) `def conjugation_distance_su2(U1, U2)` - *Para U1, U2 en U(1)/U(2):  d_conj(U1, U2) = min_g || U1 - g U2 g^{-1} ||_F.
En U(1) coincide con |U1 - U2|.
En SU(2) se reduce a comparar |Tr(U1)| con |Tr(U2)| (clase de conjugacion).*
- `_accumulate_winding` (line 429) `def _accumulate_winding(self, U_new)` - *W += (1/2pi) * arg det <U_prev | U_new>  acumulado sobre la trayectoria.*
- `snapshot` (line 445) `def snapshot(self, model, step, dataloader, vocab_size)`
- `format_log` (line 500) `def format_log(self, snap)`
- `save` (line 522) `def save(self, path)`
- `__init__` (line 600) `def __init__(self, model, config, logger, gauss_enabled)`
- `_embed_params` (line 611) `def _embed_params(model)`
- `measure_throughput` (line 619) `def measure_throughput(self, dataloader, vocab_size)` - *Devuelve (tokens_por_segundo, segundos_por_step).*
- `estimate_flops_per_step` (line 651) `def estimate_flops_per_step(self, batch_size, seq_len)` - *Heuristica: 6 * N_no_embed * tokens (forward + backward).*
- `estimate_bytes_per_step` (line 656) `def estimate_bytes_per_step(self, batch_size, seq_len, dtype_bytes)` - *Bandwidth aproximada: lectura de pesos + activaciones por step.
Asume AMP fp16 (2 bytes); pesos fp32 (4 bytes) leidos una vez.*
- `compute` (line 664) `def compute(self, dataloader, vocab_size, val_loss, val_ppl, val_acc, batch_size, seq_len)`
- `format_log` (line 696) `def format_log(self, m)`
- `__init__` (line 729) `def __init__(self, config, tokenizer, logger)`
- `_format_codealpaca` (line 746) `def _format_codealpaca(ex)`
- `_format_code_feedback` (line 757) `def _format_code_feedback(ex)`
- `_format_magicoder` (line 777) `def _format_magicoder(ex)`
- `_format_tiny_stack` (line 785) `def _format_tiny_stack(ex)`
- `_get_formatter` (line 797) `def _get_formatter(cls, tier)`
- `_tier_paths` (line 819) `def _tier_paths(self, tier)`
- `_manifest_path` (line 825) `def _manifest_path(self, tier)`
- `_already_prepared` (line 828) `def _already_prepared(self, tier)` - *True solo si los 3 splits existen, son no-vacios y el manifest concuerda.*
- `_load_hf_with_fallback` (line 858) `def _load_hf_with_fallback(self, tier)` - *Carga el dataset HF; para tiny_the_stack prueba una cadena de fallbacks
publicos hasta que uno funcione.*
- `prepare_tier` (line 891) `def prepare_tier(self, tier_index, force)`
- `open_memmap` (line 986) `def open_memmap(self, tier, split)`
- `__init__` (line 1006) `def __init__(self, tokens, seq_len)`
- `__len__` (line 1011) `def __len__(self)`
- `__getitem__` (line 1014) `def __getitem__(self, idx)`
- `__init__` (line 1030) `def __init__(self, root, max_keep, logger)`
- `save` (line 1037) `def save(self, tag, model, optimizer, state)` - *Guarda checkpoint atomico en <root>/last/ sobreescribiendo el anterior.

El argumento `tag` se conserva por compatibilidad pero se ignora: solo
existe un checkpoint llamado `last` y los pesos en safetensors.*
- `load_latest` (line 1071) `def load_latest(self, model, optimizer)`
- `should_save` (line 1095) `def should_save(self, interval_min)`
- `__init__` (line 1119) `def __init__(self, config, start_tier)`
- `prepare_all` (line 1174) `def prepare_all(self, force)` - *Prepara cada tier; un fallo en uno no detiene los demas.*
- `_build_loaders` (line 1190) `def _build_loaders(self, tier_index)`
- `_cosine_lr` (line 1222) `def _cosine_lr(self, step, total_steps)`
- `_set_lr` (line 1229) `def _set_lr(self, lr)`
- `_train_one_tier` (line 1237) `def _train_one_tier(self, tier_index)`
- `_evaluate` (line 1398) `def _evaluate(self, dl)` - *Devuelve (avg_loss, perplexity, token_accuracy).*
- `_state_dict` (line 1436) `def _state_dict(self)`
- `run` (line 1449) `def run(self)`
- `_eval_combined_holdout` (line 1506) `def _eval_combined_holdout(self)`
- `flush` (line 922) `def flush(split)`

### SH (1 files)

#### `install.sh`
**Path:** `install.sh`

*No symbols extracted*
