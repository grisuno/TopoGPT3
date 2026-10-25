# Second Brain

*Last synthesized: 2026-10-25 | 64 files | 7 concept pages | offline, zero tokens*

> Raw sources -> readmenator wiki -> links (Karpathy LLM Wiki Pattern, deterministic).
> Start here, then open one community page. Prefer grep over full reads.

## Vault Overview

The codebase centres on `model.py`, `__init__.py`, `checkpoint_meta.py`. Architecturally it is 5 layers, dominant utility (52 files) across 7 import-based communities. Recorded risk surface: 0 security findings and 0 dependency cycles.

Surprising tissue lives between topogpt3: model, eval, topogpt3: tasks: 8 extracted cross-community imports and 12 inferred bridges. Follow `connections.json` sorted by strength before refactoring.

Open work clusters around documentation (89% file coverage), 0 security findings, 20 taint paths, and 5 suggested exploration questions in `queries.md`.

## Stats

| Metric | Value |
|--------|-------|
| Files | 64 |
| Symbols | 1082 |
| Resolved imports | 153 |
| Languages | c, py, sh |
| Communities | 7 |
| Doc coverage | 89% (57/64 files) |
| Security findings | 0 |
| Estimated read cost | ~29412 tokens (chars/4, offline so $0) |

## Reading Order

1. Skim Stats and God Nodes below for blast radius.
2. Open the largest community page first, then follow Connections.
3. Use `queries.md` for the next question; log the answer there.

```
grep -rn '<keyword>' index.md community_*.md
readmenator query "<question>" --target TopoGPT3
```

## Concept Wiki

- [topogpt3: model (15 files, cohesion 0.45)](./community_0_topogpt3_model.md)
- [eval (13 files, cohesion 0.44)](./community_1_eval.md)
- [topogpt3: tasks (10 files, cohesion 0.51)](./community_2_topogpt3_tasks.md)
- [topogpt3: inference_hrm (9 files, cohesion 0.34)](./community_3_topogpt3_inference_hrm.md)
- [topogpt3: jlens (4 files, cohesion 0.45)](./community_4_topogpt3_jlens.md)
- [root (3 files, cohesion 1.00)](./community_5_root.md)
- [orphans (10 files, cohesion 0.00)](./community_6_orphans.md)

## God Nodes

| File | Score |
|------|-------|
| `topogpt3/model.py` | 62.8 |
| `topogpt3/__init__.py` | 42.0 |
| `topogpt3/checkpoint_meta.py` | 28.5 |
| `topogpt3/__main__.py` | 28.1 |
| `topogpt3/chat.py` | 22.8 |

## Strongest Connections

- 0 -> 1: depends_on (strength 0.9, EXTRACTED)
- 1 -> 3: depends_on (strength 0.9, EXTRACTED)
- 2 -> 3: depends_on (strength 0.9, EXTRACTED)
- 2 -> 0: depends_on (strength 0.9, EXTRACTED)
- 2 -> 1: depends_on (strength 0.9, EXTRACTED)
- 4 -> 0: depends_on (strength 0.9, EXTRACTED)
- 3 -> 0: depends_on (strength 0.9, EXTRACTED)
- 1 -> 4: depends_on (strength 0.9, EXTRACTED)
- 1 -> 3: bridges (strength 0.5, INFERRED)
- 1 -> 3: bridges (strength 0.5, INFERRED)

## Navigation Tips

- Obsidian Graph View works: every community page links back here.
- `connections.json` is machine-readable for GraphRAG pipelines.
- `REPORT.md` states what was extracted vs inferred and current limits.
- Regenerate offline: `readmenator . --rebuild` (no network, no tokens).
