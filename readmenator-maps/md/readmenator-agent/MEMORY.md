# Project Memory

> Cross-session context for agents. Sections 1-6 are regenerated from the source tree with zero LLM tokens: declared rules are quoted verbatim with `file:line`, measured baselines come from the scan. Section 7 is written by agents and humans and is preserved across rebuilds.

Generated from 64 files at commit `aab73bf4e510`. Read this first, then `readmenator-wiki/index.md`, then `readmenator . ask "<question>"` for anything specific.

## 1. Purpose and domain

- What it is: A 24.5M parameter complex-valued autoregressive language model for code, instrumented with spectral and geometric diagnostics over training dynamics. (`README.md:3`)
- Domain vocabulary (term, files): `topo` (40), `topogpt3` (37), `gpt3` (36), `model` (29), `eval` (25), `load` (25), `prompt` (22), `run` (21), `checkpoint` (20), `token` (18), `build` (18), `call` (18), `python` (18), `per` (17), `code` (17)
- Subsystem `topogpt3: model`: 15 files, core `topogpt3/model.py`: TopoGPT2: Quaternion-Enhanced Topological Transformer Language Model  Author: Gris Iscomeback...
- Subsystem `eval`: 13 files, core `eval/governor.py`: Streaming + governance for autoregressive generation.
- Subsystem `topogpt3: tasks`: 10 files, core `eval/tasks.py`: Generic task eval: JSONL cases + safe verifiers.
- Subsystem `topogpt3: inference_hrm`: 9 files, core `topogpt3/inference_hrm.py`: TopoGPT3.1: Hierarchical Recursive Reasoning Inference Engine.
- Subsystem `topogpt3: jlens`: 4 files, core `topogpt3/jlens.py`: TopoGPT3JLensFitConfig: Centralized configuration for Jacobian lens fitting.
- Subsystem `root`: 3 files, core `topogpt3.c`: FILE: topogpt3 -p "prompt" [-n N] [-t T]   Headless mode topogpt3 -i...
- Business rules that the code cannot show live in section 7: record them there.

## 2. Workflow

Detected commands:
- `python -m pytest -q` (pyproject.toml)
- `topogpt3-train --help` (pyproject.toml [project.scripts])
- `topogpt3-infer --help` (pyproject.toml [project.scripts])
- `topogpt3-infer-hrm --help` (pyproject.toml [project.scripts])
- `topogpt3-jlens --help` (pyproject.toml [project.scripts])
- `topogpt3-api --help` (pyproject.toml [project.scripts])
- `topogpt3-train-lora --help` (pyproject.toml [project.scripts])
- `topogpt3-train-dpo --help` (pyproject.toml [project.scripts])
- `topogpt3-train-grpo --help` (pyproject.toml [project.scripts])
- `topogpt3-train-ppo --help` (pyproject.toml [project.scripts])
- `topogpt3-train-distill --help` (pyproject.toml [project.scripts])
- `topogpt3-train-agent --help` (pyproject.toml [project.scripts])

Session protocol:
1. Start: read this file, then `readmenator . fresh` (exit 1 means run `readmenator . --rebuild`).
2. Orient: `readmenator-wiki/index.md`; for a question use `readmenator . ask "<question>"` (local = entities + sources, `--global` = community reports).
3. Before editing a file: `grep -n '<file>' readmenator-agent/GOTCHAS.md readmenator-agent/SECURITY.md`.
4. After the change: run the tests above, then `readmenator . --rebuild` so the maps, wiki, and this file stay true.
5. End: record decisions, business rules, and gotchas with `readmenator . remember "<note>" --kind decision`.

## 3. Rules and constraints

Declared:
- none declared in instruction files (add them to AGENTS.md or record them in section 7)

Measured baseline:
- Security findings at medium or above: 0 (see `readmenator-agent/SECURITY.md`); do not add new ones.
- Dependency cycles: 0; layer violations: 5 (see `readmenator-agent/GOTCHAS.md`).

## 4. Style norms

Declared:
- none declared in instruction files (add them to AGENTS.md or record them in section 7)

Measured baseline:
- py: 61 files, 953 symbols; docstrings on 46% of symbols; functions snake_case (100%); types PascalCase (97%); median file 159 lines, max 4693.
- sh: 2 files, 1 symbols; docstrings on 0% of symbols; functions snake_case (100%); median file 54 lines, max 54.
- c: 1 files, 128 symbols; docstrings on 10% of symbols; functions snake_case (100%); types PascalCase (100%); median file 1999 lines, max 1999.
- Tests: 8 files under tests; follow the existing naming (e.g. `test_checkpoint_meta.py`).

## 5. Minimum deliverables

Declared:
- none declared in instruction files (add them to AGENTS.md or record them in section 7)

Measured baseline:
- Tests pass: `python -m pytest -q`.
- Docstring coverage stays at or above 41%.
- No new security findings at medium or above (current: 0).
- No new dependency cycles (current: 0).
- Files stay under 300 lines where possible (`readmenator . lint`).
- Docs refreshed: `readmenator . --rebuild`, and decisions recorded in section 7.

## 6. Risks to respect

- God nodes (changes ripple widely): `topogpt3/model.py`, `topogpt3/__init__.py`, `topogpt3/checkpoint_meta.py`, `topogpt3/__main__.py`, `topogpt3/chat.py`
- Hotspots (complex and central): `topogpt3/model.py`, `topogpt3/api_server.py`, `topogpt3/train.py`, `topogpt3/__init__.py`, `topogpt3/inference_hrm.py`
- Full blast radius: `readmenator-agent/GOTCHAS.md`; findings: `readmenator-agent/SECURITY.md`.

## 7. Session log (preserved across rebuilds)

Append with `readmenator . remember "<note>" --kind <kind>` (kinds: business, decision, rule, workflow, style, deliverable, gotcha, todo, note) or the MCP tool `readmenator.remember`. Record business rules, decisions and their reasons, workflow changes, and anything the next session must not rediscover.

<!-- readmenator:memory:notes:begin -->
<!-- readmenator:memory:notes:end -->
