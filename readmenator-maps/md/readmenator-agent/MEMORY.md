# Project Memory

> Cross-session context for agents. Sections 1-6 are regenerated from the source tree with zero LLM tokens: declared rules are quoted verbatim with `file:line`, measured baselines come from the scan. Section 7 is written by agents and humans and is preserved across rebuilds.

Generated from 55 files at commit `c3de8abbea66`. Read this first, then `readmenator-wiki/index.md`, then `readmenator . ask "<question>"` for anything specific.

## 1. Purpose and domain

- What it is: A 24.5M parameter complex-valued autoregressive language model for code, instrumented with spectral and geometric diagnostics over training dynamics. (`README.md:3`)
- Domain vocabulary (term, files): `topo` (36), `gpt3` (34), `topogpt3` (33), `model` (24), `eval` (23), `load` (22), `run` (20), `prompt` (19), `token` (17), `checkpoint` (17), `build` (16), `quaternion` (16), `python` (16), `per` (15), `one` (15)
- Subsystem `topogpt3: lora`: 12 files, core `topogpt3/lora.py`: Native LoRA for TopoGPT3.
- Subsystem `eval`: 11 files, core `topogpt3/inference.py`: TopoGPT3 inference engine.
- Subsystem `topogpt3: model`: 10 files, core `topogpt3/model.py`: TopoGPT2: Quaternion-Enhanced Topological Transformer Language Model  Author: Gris Iscomeback...
- Subsystem `topogpt3: sandbox`: 7 files, core `eval/sandbox.py`: Sandbox for executing model-generated code during HumanEval evaluation.
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
- py: 53 files, 853 symbols; docstrings on 49% of symbols; functions snake_case (100%); types PascalCase (97%); median file 150 lines, max 3843.
- c: 1 files, 128 symbols; docstrings on 10% of symbols; functions snake_case (100%); types PascalCase (100%); median file 1999 lines, max 1999.
- sh: 1 files, 0 symbols; median file 4 lines, max 4.
- Tests: 4 files under tests; follow the existing naming (e.g. `test_heritage.py`).

## 5. Minimum deliverables

Declared:
- none declared in instruction files (add them to AGENTS.md or record them in section 7)

Measured baseline:
- Tests pass: `python -m pytest -q`.
- Docstring coverage stays at or above 44%.
- No new security findings at medium or above (current: 0).
- No new dependency cycles (current: 0).
- Files stay under 300 lines where possible (`readmenator . lint`).
- Docs refreshed: `readmenator . --rebuild`, and decisions recorded in section 7.

## 6. Risks to respect

- God nodes (changes ripple widely): `topogpt3/model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/api_server.py`, `tests/test_heritage.py`
- Hotspots (complex and central): `topogpt3/model.py`, `topogpt3/api_server.py`, `topogpt3/train.py`, `topogpt3/__init__.py`, `eval/harness.py`
- Full blast radius: `readmenator-agent/GOTCHAS.md`; findings: `readmenator-agent/SECURITY.md`.

## 7. Session log (preserved across rebuilds)

Append with `readmenator . remember "<note>" --kind <kind>` (kinds: business, decision, rule, workflow, style, deliverable, gotcha, todo, note) or the MCP tool `readmenator.remember`. Record business rules, decisions and their reasons, workflow changes, and anything the next session must not rediscover.

<!-- readmenator:memory:notes:begin -->
<!-- readmenator:memory:notes:end -->
