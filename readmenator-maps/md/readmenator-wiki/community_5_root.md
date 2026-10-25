# root

*Community 5 | 3 files | cohesion 1.00*

## Definition

This community groups 3 file(s) rooted at `root` with dominant language py (cohesion 1.00). Central symbols: `D_HEAD`, `D_LAT_Q`, `D_MODEL`, `D_QUAT`, `EMBED_INNER`, `EOS_TOKEN`, `EPS_RMS`, `EXPERT_INNER`. Core file: `topogpt3.c` (128 symbols). Documented purpose: Drop-in entry point that demonstrates how to use the topogpt3 package.  This file lives outside the package on purpose. Copy it (or its sections) into your own .

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `app.py` | py | utility | 5 | yes |
| `gradio_app.py` | py | utility | 4 | yes |
| `topogpt3.c` | c | utility | 128 | no |

## Key Symbols

- `run_inference` (function, `app.py:46`) `def run_inference(prompt, checkpoint_dir, checkpoint_name, max_new_tokens, tempe` - Run the standard sampler and return the generated completion text.
- `run_inference_hrm` (function, `app.py:71`) `def run_inference_hrm(prompt, checkpoint_dir, checkpoint_name, max_new_tokens, t` - Run the hierarchical recursive sampler and return the completion.
- `run_training` (function, `app.py:105`) `def run_training(scale, start_tier, device, prepare_data)` - Run the full TopoGPT3 curriculum trainer.
- `_build_parser` (function, `app.py:121`) `def _build_parser()` - Build the top-level CLI for this entry point script.
- `main` (function, `app.py:159`) `def main(argv)` - Entry point invoked when the file is executed as a script.
- `ensure_checkpoint` (function, `gradio_app.py:35`) `def ensure_checkpoint()` - Return the path to the checkpoint directory, downloading if needed.
- `run_standard_inference` (function, `gradio_app.py:59`) `def run_standard_inference(prompt, max_new_tokens, temperature, top_k, repetitio` - Run standard autoregressive inference.
- `run_hrm_inference` (function, `gradio_app.py:95`) `def run_hrm_inference(prompt, max_new_tokens, temperature, top_k, repetition_pen` - Run hierarchical recursive reasoning inference.
- `build_ui` (function, `gradio_app.py:144`) `def build_ui()` - Construct the Gradio Blocks interface.
- `FILE` (struct, `topogpt3.c:24`) - topogpt3 -p "prompt" [-n N] [-t T]   Headless mode topogpt3 -i                          Interactive
- `stdin` (variable, `topogpt3.c:25`) `extern FILE *stdin;`
- `stdout` (variable, `topogpt3.c:26`) `extern FILE *stdout;`
- `stderr` (variable, `topogpt3.c:27`) `extern FILE *stderr;`
- `printf` (function, `topogpt3.c:28`) `extern int printf(const char *, ...);`
- `fprintf` (function, `topogpt3.c:29`) `extern int fprintf(FILE *, const char *, ...);`
- `sprintf` (function, `topogpt3.c:30`) `extern int sprintf(char *, const char *, ...);`
- `snprintf` (function, `topogpt3.c:31`) `extern int snprintf(char *, unsigned long, const char *, ...);`
- `puts` (function, `topogpt3.c:32`) `extern int puts(const char *);`
- `putchar` (function, `topogpt3.c:33`) `extern int putchar(int);`
- `fputc` (function, `topogpt3.c:34`) `extern int fputc(int, FILE *);`
- `fputs` (function, `topogpt3.c:35`) `extern int fputs(const char *, FILE *);`
- `fopen` (function, `topogpt3.c:36`) `extern FILE *fopen(const char *, const char *);`
- `fclose` (function, `topogpt3.c:37`) `extern int fclose(FILE *);`
- `fread` (function, `topogpt3.c:38`) `extern unsigned long fread(void *, unsigned long, unsigned long, FILE *);`
- `fwrite` (function, `topogpt3.c:39`) `extern unsigned long fwrite(const void *, unsigned long, unsigned long, FILE *);`
- `fseek` (function, `topogpt3.c:40`) `extern int fseek(FILE *, long, int);`
- `ftell` (function, `topogpt3.c:41`) `extern long ftell(FILE *);`
- `fflush` (function, `topogpt3.c:42`) `extern int fflush(FILE *);`
- `NULL` (macro, `topogpt3.c:43`) `#define NULL`
- `SEEK_SET` (macro, `topogpt3.c:44`) `#define SEEK_SET`

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 2
- Cross-boundary resolved imports (EXTRACTED): 0

## Connections

- [INFERRED] shares_context community 0 <-> 5 (strength 0.5): Inferred shared context (language py and layer utility) with no import path between community 0 (topogpt3: lora) and community 5 (root).
- [INFERRED] shares_context community 1 <-> 5 (strength 0.5): Inferred shared context (language py and layer utility) with no import path between community 1 (eval) and community 5 (root).
- [INFERRED] shares_context community 2 <-> 5 (strength 0.5): Inferred shared context (language py and layer utility) with no import path between community 2 (topogpt3: model) and community 5 (root).

## Risks

- No scoped security, taint, cycle, or layer risks.

## Open Questions

- Why do 1 file(s) lack file-level docs (e.g. `topogpt3.c`)? What purpose do they serve?
- What would break if the most connected file in root changed?
- Should root be split, given cohesion 1.00?

## Sources

- `app.py`
- `gradio_app.py`
- `topogpt3.c`
