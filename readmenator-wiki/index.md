# Second Brain

*Last synthesized: 2026-10-07 | 53 files | 7 concept pages | offline, zero tokens*

> Raw sources -> readmenator wiki -> links (Karpathy LLM Wiki Pattern, deterministic).
> Start here, then open one community page. Prefer grep over full reads.

## Vault Overview

The codebase centres on `model.py`, `__init__.py`, `__main__.py`. Architecturally it is 5 layers, dominant utility (46 files) across 7 import-based communities. Recorded risk surface: 0 security findings and 0 dependency cycles.

Surprising tissue lives between topogpt3: lora, eval, topogpt3: model: 9 extracted cross-community imports and 11 inferred bridges. Follow `connections.json` sorted by strength before refactoring.

Open work clusters around documentation (87% file coverage), 0 security findings, 20 taint paths, and 5 suggested exploration questions in `queries.md`.

## Stats

| Metric | Value |
|--------|-------|
| Files | 53 |
| Symbols | 933 |
| Resolved imports | 112 |
| Languages | c, py, sh |
| Communities | 7 |
| Doc coverage | 87% (46/53 files) |
| Security findings | 0 |
| Estimated read cost | ~27351 tokens (chars/4, offline so $0) |

## Reading Order

1. Skim Stats and God Nodes below for blast radius.
2. Open the largest community page first, then follow Connections.
3. Use `queries.md` for the next question; log the answer there.

```
grep -rn '<keyword>' index.md community_*.md
readmenator query "<question>" --target readmenator_TopoGPT3_dnp72ga8
```

## Concept Wiki

- [topogpt3: lora (12 files, cohesion 0.49)](./community_0_topogpt3_lora.md)
- [eval (11 files, cohesion 0.43)](./community_1_eval.md)
- [topogpt3: model (8 files, cohesion 0.32)](./community_2_topogpt3_model.md)
- [topogpt3: sandbox (7 files, cohesion 0.41)](./community_3_topogpt3_sandbox.md)
- [topogpt3: jlens (4 files, cohesion 0.45)](./community_4_topogpt3_jlens.md)
- [root (3 files, cohesion 1.00)](./community_5_root.md)
- [orphans (8 files, cohesion 0.00)](./community_6_orphans.md)

## God Nodes

| File | Score |
|------|-------|
| `topogpt3/model.py` | 56.8 |
| `topogpt3/__init__.py` | 42.0 |
| `topogpt3/__main__.py` | 28.1 |
| `tests/test_heritage.py` | 16.9 |
| `topogpt3.c` | 16.8 |

## Strongest Connections

- 2 -> 1: depends_on (strength 0.9, EXTRACTED)
- 1 -> 3: depends_on (strength 0.9, EXTRACTED)
- 3 -> 0: depends_on (strength 0.9, EXTRACTED)
- 3 -> 2: depends_on (strength 0.9, EXTRACTED)
- 4 -> 2: depends_on (strength 0.9, EXTRACTED)
- 1 -> 4: depends_on (strength 0.9, EXTRACTED)
- 1 -> 0: depends_on (strength 0.9, EXTRACTED)
- 0 -> 4: depends_on (strength 0.9, EXTRACTED)
- 0 -> 2: depends_on (strength 0.9, EXTRACTED)
- 1 -> 3: bridges (strength 0.5, INFERRED)

## Navigation Tips

- Obsidian Graph View works: every community page links back here.
- `connections.json` is machine-readable for GraphRAG pipelines.
- `REPORT.md` states what was extracted vs inferred and current limits.
- Regenerate offline: `readmenator . --rebuild` (no network, no tokens).
