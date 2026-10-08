# Gotchas

## God Nodes (high connectivity)

These files have the most connections. Changes here have high blast radius.

- `topogpt3/model.py` (score: 56.80, imported by 16 files)
- `topogpt3/__init__.py` (score: 42.00, imported by 7 files)
- `topogpt3/__main__.py` (score: 28.10)
- `topogpt3.c` (score: 16.80, imported by 2 files)
- `topogpt3/train.py` (score: 16.20, imported by 4 files)
- `topogpt3/trainer_utils_topo.py` (score: 15.00, imported by 7 files)
- `topogpt3/lens_model.py` (score: 14.90, imported by 5 files)
- `topogpt3/rewards.py` (score: 14.90, imported by 7 files)
- `topogpt3/inference_hrm.py` (score: 13.60, imported by 2 files)

## Blast Radius (change impact)

Editing these files can break the listed number of dependents. Run their tests after any change.

- `topogpt3/continuation.py` -- 3 direct, 28 total dependents
- `synthetic_dataset.py` -- 1 direct, 27 total dependents
- `topogpt3/yarn.py` -- 3 direct, 27 total dependents
- `topogpt3/model.py` -- 16 direct, 26 total dependents
- `topogpt3/rewards.py` -- 7 direct, 17 total dependents
- `topogpt3/trainer_utils_topo.py` -- 7 direct, 17 total dependents
- `eval/sandbox.py` -- 3 direct, 16 total dependents
- `topogpt3/chat.py` -- 6 direct, 16 total dependents
- `topogpt3/lens_model.py` -- 5 direct, 14 total dependents
- `topogpt3/lora.py` -- 4 direct, 14 total dependents

## Hotspots (complexity + centrality)

- `topogpt3/model.py` -- complexity: 1.0, centrality: 1.0, combined: 1.0
- `topogpt3/api_server.py` -- complexity: 0.2, centrality: 0.7, combined: 0.5
- `topogpt3/train.py` -- complexity: 0.3, centrality: 0.5, combined: 0.5
- `topogpt3/__init__.py` -- complexity: 0.0, centrality: 0.7, combined: 0.4
- `eval/harness.py` -- complexity: 0.1, centrality: 0.6, combined: 0.4
- `synthetic_dataset.py` -- complexity: 0.2, centrality: 0.5, combined: 0.4
- `topogpt3/__main__.py` -- complexity: 0.0, centrality: 0.6, combined: 0.4
- `topogpt3/inference_hrm.py` -- complexity: 0.4, centrality: 0.3, combined: 0.4
- `topogpt3/jlens.py` -- complexity: 0.2, centrality: 0.5, combined: 0.3
- `topogpt3.c` -- complexity: 0.7, centrality: 0.1, combined: 0.3

## Dataflow Issues (INFERRED, review each lead)

- `eval/repair.py:140` `main` [UNCHECKED_ALLOC] `base`: Result of allocator stored in `base` is never checked against NULL.
- `topogpt3/export_chat.py:105` `main` [UNCHECKED_ALLOC] `sft`: Result of allocator stored in `sft` is never checked against NULL.
- `topogpt3/export_chat.py:106` `main` [UNCHECKED_ALLOC] `rla`: Result of allocator stored in `rla` is never checked against NULL.
- `topogpt3/export_chat.py:107` `main` [UNCHECKED_ALLOC] `dpo`: Result of allocator stored in `dpo` is never checked against NULL.
- `topogpt3/export_chat.py:132` `main` [UNCHECKED_ALLOC] `pre`: Result of allocator stored in `pre` is never checked against NULL.
