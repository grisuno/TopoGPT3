# orphans

*Community 6 | 8 files | cohesion 0.00*

## Definition

This community groups 8 file(s) rooted at `eval` with dominant language py (cohesion 0.00). Central symbols: `_load`, `classify_error`, `consistency_across_runs`, `convert`, `load_jsonl`, `load_records`, `main`, `pass_at_k`. Core file: `eval/report.py` (6 symbols). Documented purpose: TopoGPT3 Weight Converter: safetensors -> flat float32 binary.  Usage: python convert_weights.py [--input model.safetensors] [--output topogpt3.weights]  Output.

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `convert_weights.py` | py | utility | 2 | yes |
| `convert_weights_minios.py` | py | utility | 1 | yes |
| `encode_tokens.py` | py | utility | 1 | yes |
| `eval/analyze.py` | py | utility | 5 | yes |
| `eval/analyze_results.py` | py | utility | 4 | yes |
| `eval/noise_analysis.py` | py | utility | 3 | yes |
| `eval/report.py` | py | utility | 6 | yes |
| `install.sh` | sh | utility | 0 | no |

## Key Symbols

- `convert` (function, `convert_weights.py:102`) `def convert(input_path, output_path)`
- `main` (function, `convert_weights.py:160`) `def main()`
- `main` (function, `convert_weights_minios.py:85`) `def main()`
- `main` (function, `encode_tokens.py:19`) `def main()`
- `pass_at_k` (function, `eval/analyze.py:21`) `def pass_at_k(n, c, k)` - Unbiased estimator from the HumanEval paper.
- `classify_error` (function, `eval/analyze.py:32`) `def classify_error(msg, candidate_src)` - Heuristic single-label error classifier.
- `load_jsonl` (function, `eval/analyze.py:56`) `def load_jsonl(path)`
- `summarize` (function, `eval/analyze.py:61`) `def summarize(paths)`
- `main` (function, `eval/analyze.py:103`) `def main()`
- `load_records` (function, `eval/analyze_results.py:26`) `def load_records(path)`
- `summarize` (function, `eval/analyze_results.py:31`) `def summarize(records)`
- `show_failures` (function, `eval/analyze_results.py:44`) `def show_failures(records, task_id)`
- `main` (function, `eval/analyze_results.py:82`) `def main()`
- `_load` (function, `eval/noise_analysis.py:43`) `def _load(p)`
- `consistency_across_runs` (function, `eval/noise_analysis.py:47`) `def consistency_across_runs(per_run)` - Para cada problema, mira si pasa consistentemente a traves de los
- `main` (function, `eval/noise_analysis.py:83`) `def main()`
- `pass_at_k` (function, `eval/report.py:25`) `def pass_at_k(n, c, k)`
- `classify_error` (function, `eval/report.py:31`) `def classify_error(msg)`
- `load_jsonl` (function, `eval/report.py:52`) `def load_jsonl(p)`
- `summarize_run` (function, `eval/report.py:56`) `def summarize_run(p)`
- `repair_summary` (function, `eval/report.py:90`) `def repair_summary(repair_path, baseline_path)`
- `main` (function, `eval/report.py:117`) `def main()`

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 0
- Cross-boundary resolved imports (EXTRACTED): 0

## Connections

- [INFERRED] shares_context community 0 <-> 6 (strength 0.5): Inferred shared context (language py and layer utility) with no import path between community 0 (topogpt3: lora) and community 6 (orphans).
- [INFERRED] shares_context community 1 <-> 6 (strength 0.5): Inferred shared context (language py and layer utility) with no import path between community 1 (eval) and community 6 (orphans).
- [INFERRED] shares_context community 2 <-> 6 (strength 0.5): Inferred shared context (language py and layer utility) with no import path between community 2 (topogpt3: model) and community 6 (orphans).

## Risks

- No scoped security, taint, cycle, or layer risks.

## Open Questions

- Why do 1 file(s) lack file-level docs (e.g. `install.sh`)? What purpose do they serve?
- What would break if the most connected file in orphans changed?
- Should orphans be split, given cohesion 0.00?

## Sources

- `convert_weights.py`
- `convert_weights_minios.py`
- `encode_tokens.py`
- `eval/analyze.py`
- `eval/analyze_results.py`
- `eval/noise_analysis.py`
- `eval/report.py`
- `install.sh`
