# API (page 1 of 2)
Pages: [API.md](API.md), [API_p2.md](API_p2.md)

## app.py
Depends on: `topogpt3.c`
- `run_inference` (function) `app.py:46` `def run_inference(prompt, checkpoint_dir, checkpoint_name, max_new_tokens, temperature, top_k, repetition_penalty...` -- Run the standard sampler and return the generated completion text.
- `run_inference_hrm` (function) `app.py:71` `def run_inference_hrm(prompt, checkpoint_dir, checkpoint_name, max_new_tokens, temperature, top_k...` -- Run the hierarchical recursive sampler and return the completion.
- `run_training` (function) `app.py:105` `def run_training(scale, start_tier, device, prepare_data)` -- Run the full TopoGPT3 curriculum trainer.
- `main` (function) `app.py:159` `def main(argv)` -- Entry point invoked when the file is executed as a script.

## convert_weights.py
- `convert` (function) `convert_weights.py:102` `def convert(input_path, output_path)`
- `main` (function) `convert_weights.py:160` `def main()`

## convert_weights_minios.py
- `main` (function) `convert_weights_minios.py:85` `def main()`

## encode_tokens.py
- `main` (function) `encode_tokens.py:19` `def main()`

## eval/analyze.py
- `pass_at_k` (function) `eval/analyze.py:21` `def pass_at_k(n, c, k)` -- Unbiased estimator from the HumanEval paper.
- `classify_error` (function) `eval/analyze.py:32` `def classify_error(msg, candidate_src)` -- Heuristic single-label error classifier.
- `load_jsonl` (function) `eval/analyze.py:56` `def load_jsonl(path)`
- `summarize` (function) `eval/analyze.py:61` `def summarize(paths)`
- `main` (function) `eval/analyze.py:103` `def main()`

## eval/analyze_results.py
- `load_records` (function) `eval/analyze_results.py:26` `def load_records(path)`
- `summarize` (function) `eval/analyze_results.py:31` `def summarize(records)`
- `show_failures` (function) `eval/analyze_results.py:44` `def show_failures(records, task_id)`
- `main` (function) `eval/analyze_results.py:82` `def main()`

## eval/diag_static.py
Depends on: `topogpt3/__init__.py`, `topogpt3/model.py`, `topogpt3/train.py`
- `phase_discretization` (function) `eval/diag_static.py:49` `def phase_discretization(K, n_samples, seed)` -- Muestrea n_samples overlaps aleatorios <u_i | u_j> sobre los vectores singulares de K y mide cuanto se aleja su fase...
- `synthetic_winding` (function) `eval/diag_static.py:95` `def synthetic_winding(K, n_windows, window_size)` -- Como el checkpoint es estatico, no hay trayectoria temporal.
- `static_kappa` (function) `eval/diag_static.py:144` `def static_kappa(K)`
- `context_length_diagnostic` (function) `eval/diag_static.py:171` `def context_length_diagnostic(model, tracker, device, lengths)`
- `main` (function) `eval/diag_static.py:248` `def main()`

## eval/governor.py
Imported by: `eval/governor_smoke.py`
- `TokenStream.__init__` (method) `eval/governor.py:56` `def __init__(self)`
- `TokenStream.put` (method) `eval/governor.py:62` `def put(self, tok)`
- `TokenStream.mark_done` (method) `eval/governor.py:67` `def mark_done(self)`
- `TokenStream.drain` (method) `eval/governor.py:72` `def drain(self)` -- Return all tokens emitted so far, atomic snapshot.
- `TokenStream.wait_for_new` (method) `eval/governor.py:77` `def wait_for_new(self, timeout)` -- Block up to `timeout` seconds for a new token.
- `TokenStream.is_closed` (method) `eval/governor.py:86` `def is_closed(self)`
- `GenerationGovernor.__init__` (method) `eval/governor.py:156` `def __init__(self, model, ctx, stream, max_new_tokens, temperature, top_k, repetition_penalty, max_seq_len)`
- `GenerationGovernor.cancel` (method) `eval/governor.py:177` `def cancel(self)` -- Asynchronously stop the generation.
- `GenerationGovernor.run` (method) `eval/governor.py:185` `def run(self, stop_hooks)` -- Execute the generation loop.
- `GenerationGovernor.make_loop_detector` (method) `eval/governor.py:285` `def make_loop_detector(window, min_repeats)` -- Return True if the last `window` tokens contain a sub-sequence of length >= `min_repeats` that repeats consecutively.
- `GenerationGovernor.hook` (method) `eval/governor.py:292` `def hook(generated)`
- `GenerationGovernor.make_timeout_hook` (method) `eval/governor.py:314` `def make_timeout_hook(per_token_s)` -- Return True if the per-token wall time exceeds `per_token_s`.
- `GenerationGovernor.hook` (method) `eval/governor.py:320` `def hook(generated)`

## eval/governor_smoke.py
Depends on: `eval/governor.py`, `topogpt3/__init__.py`
- `load_model` (function) `eval/governor_smoke.py:30` `def load_model()`
- `test_tokenstream_threadsafety` (function) `eval/governor_smoke.py:49` `def test_tokenstream_threadsafety()`
- `producer` (function) `eval/governor_smoke.py:53` `def producer()`
- `consumer` (function) `eval/governor_smoke.py:59` `def consumer()`
- `test_governor_basic` (function) `eval/governor_smoke.py:79` `def test_governor_basic()`
- `test_loop_detector` (function) `eval/governor_smoke.py:98` `def test_loop_detector()`
- `test_cancel` (function) `eval/governor_smoke.py:118` `def test_cancel()`

## eval/harness.py
Depends on: `eval/samplers.py`, `eval/sandbox.py`, `topogpt3/__init__.py`
Imported by: `eval/integration_smoke.py`, `eval/noise_sweep.py`, `eval/temp_sweep.py`
- `load_humaneval` (function) `eval/harness.py:59` `def load_humaneval(cache_dir)`
- `build_prompt` (function) `eval/harness.py:75` `def build_prompt(problem)` -- Return the exact prompt text fed to the model.
- `extract_candidate` (function) `eval/harness.py:100` `def extract_candidate(prompt, completion)` -- Combine prompt + completion into a single Python source string.
- `run_one_test` (function) `eval/harness.py:150` `def run_one_test(problem, candidate_src, timeout)` -- Execute the candidate against the hidden test.
- `run_one_test_sandboxed` (function) `eval/harness.py:172` `def run_one_test_sandboxed(problem, candidate_src, timeout, sandbox_cfg)` -- Sandboxed variant of `run_one_test`.
- `make_sampler` (function) `eval/harness.py:195` `def make_sampler(mode, settings_kwargs)` -- Backwards-compatible shim.
- `completion_for_problem` (function) `eval/harness.py:204` `def completion_for_problem(sampler, prompt)` -- Run a single completion and return (raw_output_text, metrics_dict).
- `ModelLoader.__init__` (method) `eval/harness.py:220` `def __init__(self, ckpt_dir, ckpt_name, device)`
- `ModelLoader.generate` (method) `eval/harness.py:246` `def generate(self, prompt, max_new_tokens, temperature, top_k, repetition_penalty)`
- `ModelLoader.evaluate_problem` (method) `eval/harness.py:272` `def evaluate_problem(problem, loader, args, sample_idx)`
- `ModelLoader.main` (method) `eval/harness.py:315` `def main()`

## eval/integration_smoke.py
Depends on: `eval/harness.py`
- `main` (function) `eval/integration_smoke.py:18` `def main()`

## eval/noise_analysis.py
- `consistency_across_runs` (function) `eval/noise_analysis.py:47` `def consistency_across_runs(per_run)` -- Para cada problema, mira si pasa consistentemente a traves de los 4 niveles de ruido.
- `main` (function) `eval/noise_analysis.py:83` `def main()`

## eval/noise_sweep.py
Depends on: `eval/harness.py`, `topogpt3/__init__.py`, `topogpt3/model.py`
Imported by: `eval/temp_sweep.py`
- `inject_noise` (function) `eval/noise_sweep.py:46` `def inject_noise(model, sigma, seed)` -- Anade N(0, sigma) a TODOS los kernels espectrales (kr_*, ki_*).
- `load_model` (function) `eval/noise_sweep.py:74` `def load_model(ckpt_dir, ckpt_name, device)` -- Reconstruye TopoGPT2 alineado con el checkpoint, sin acceso a harness.ModelLoader (queremos un loader limpio que no...
- `generate_one` (function) `eval/noise_sweep.py:99` `def generate_one(model, tok, prompt, max_new_tokens, device)`
- `main` (function) `eval/noise_sweep.py:117` `def main()`

## eval/repair.py
Depends on: `topogpt3/__init__.py`
- `extract_candidate` (function) `eval/repair.py:49` `def extract_candidate(prompt, completion)`
- `run_test` (function) `eval/repair.py:75` `def run_test(problem, candidate_src)`
- `build_repair_prompt` (function) `eval/repair.py:89` `def build_repair_prompt(prompt, candidate, err, entry_point)`
- `gen` (function) `eval/repair.py:104` `def gen(model, tok, text, max_new_tokens, temperature, top_k, rep_penalty)`
- `main` (function) `eval/repair.py:119` `def main()`

## eval/report.py
- `pass_at_k` (function) `eval/report.py:25` `def pass_at_k(n, c, k)`
- `classify_error` (function) `eval/report.py:31` `def classify_error(msg)`
- `load_jsonl` (function) `eval/report.py:52` `def load_jsonl(p)`
- `summarize_run` (function) `eval/report.py:56` `def summarize_run(p)`
- `repair_summary` (function) `eval/report.py:90` `def repair_summary(repair_path, baseline_path)`
- `main` (function) `eval/report.py:117` `def main()`

## eval/samplers.py
Depends on: `topogpt3/__init__.py`
Imported by: `eval/harness.py`
- `register_sampler` (function) `eval/samplers.py:36` `def register_sampler(name)` -- Decorator.
- `deco` (function) `eval/samplers.py:42` `def deco(fn)`
- `list_samplers` (function) `eval/samplers.py:86` `def list_samplers()`
- `build_sampler` (function) `eval/samplers.py:90` `def build_sampler(mode, settings_kwargs)` -- Construct a sampler.

## eval/sandbox.py
Imported by: `eval/harness.py`, `eval/sandbox_smoke.py`, `topogpt3/tools_agent.py`
- `SandboxConfig.d` (method) `eval/sandbox.py:125` `def d(node, cur)`
- `SandboxConfig.check_safety` (method) `eval/sandbox.py:133` `def check_safety(source, cfg)` -- Return (ok, reason).
- `SandboxConfig.safe_exec` (method) `eval/sandbox.py:270` `def safe_exec(program_src, cfg, extra_globals)` -- Execute `program_src` in a sandboxed child process.
- `SandboxConfig.describe_policy` (method) `eval/sandbox.py:373` `def describe_policy(cfg)`

## eval/sandbox_smoke.py
Depends on: `eval/sandbox.py`
- `main` (function) `eval/sandbox_smoke.py:15` `def main()`

## eval/smoke.py
Depends on: `topogpt3/__init__.py`
- `run_standard` (function) `eval/smoke.py:17` `def run_standard()`
- `run_hrm` (function) `eval/smoke.py:36` `def run_hrm()`

## eval/temp_sweep.py
Depends on: `eval/harness.py`, `eval/noise_sweep.py`
- `generate_one` (function) `eval/temp_sweep.py:39` `def generate_one(model, tok, prompt, max_new_tokens, temperature, top_k, device, seed_offset)`
- `evaluate_problems` (function) `eval/temp_sweep.py:58` `def evaluate_problems(model, tok, problems, max_new_tokens, temperature, top_k, n_samples, device)`
- `pass_at_k_unbiased` (function) `eval/temp_sweep.py:88` `def pass_at_k_unbiased(n, c, k)`
- `summarize` (function) `eval/temp_sweep.py:96` `def summarize(results, n_samples)`
- `main` (function) `eval/temp_sweep.py:116` `def main()`

## gradio_app.py
Depends on: `topogpt3.c`
- `ensure_checkpoint` (function) `gradio_app.py:35` `def ensure_checkpoint()` -- Return the path to the checkpoint directory, downloading if needed.
- `run_standard_inference` (function) `gradio_app.py:59` `def run_standard_inference(prompt, max_new_tokens, temperature, top_k, repetition_penalty, auto_continue)` -- Run standard autoregressive inference.
- `run_hrm_inference` (function) `gradio_app.py:95` `def run_hrm_inference(prompt, max_new_tokens, temperature, top_k, repetition_penalty, high_level_iters...` -- Run hierarchical recursive reasoning inference.
- `build_ui` (function) `gradio_app.py:144` `def build_ui()` -- Construct the Gradio Blocks interface.

## synthetic_dataset.py
Imported by: `topogpt3/model.py`
- `LLMBackend.generate` (method) `synthetic_dataset.py:64` `def generate(self, prompt)`
- `LLMBackend.name` (method) `synthetic_dataset.py:67` `def name(self)`
- `GroqBackend.__init__` (method) `synthetic_dataset.py:78` `def __init__(self, model, api_key, max_tokens, temperature, timeout)`
- `GroqBackend.name` (method) `synthetic_dataset.py:95` `def name(self)`
- `GroqBackend.generate` (method) `synthetic_dataset.py:98` `def generate(self, prompt)`
- `OpenRouterBackend.__init__` (method) `synthetic_dataset.py:132` `def __init__(self, model, api_key, max_tokens, temperature, timeout)`
- `OpenRouterBackend.name` (method) `synthetic_dataset.py:151` `def name(self)`
- `OpenRouterBackend.generate` (method) `synthetic_dataset.py:154` `def generate(self, prompt)`
- `OllamaBackend.__init__` (method) `synthetic_dataset.py:184` `def __init__(self, model, host, max_tokens, temperature, timeout)`
- `OllamaBackend.name` (method) `synthetic_dataset.py:198` `def name(self)`
- `OllamaBackend.generate` (method) `synthetic_dataset.py:201` `def generate(self, prompt)`
- `OllamaBackend.build_backend` (method) `synthetic_dataset.py:227` `def build_backend(provider, model)` -- Factory for LLM backends.
- `OllamaBackend.validate_sample` (method) `synthetic_dataset.py:330` `def validate_sample(sample)` -- Validate that a generated sample meets quality bar.
- `ProcessedManifest.load` (method) `synthetic_dataset.py:374` `def load(path)`
- `ProcessedManifest.save` (method) `synthetic_dataset.py:387` `def save(self, path)`
- `SyntheticDatasetGenerator.__init__` (method) `synthetic_dataset.py:418` `def __init__(self, backend, output_path, manifest_path, logger, max_workers, max_file_chars)`
- `SyntheticDatasetGenerator.process_file` (method) `synthetic_dataset.py:533` `def process_file(self, path)` -- Process a single file.
- `SyntheticDatasetGenerator.process_batch` (method) `synthetic_dataset.py:568` `def process_batch(self, paths)` -- Process a batch of files in parallel using thread pool.
- `SyntheticDatasetGenerator.finish` (method) `synthetic_dataset.py:590` `def finish(self)` -- Signal end of processing and flush writer.
- `SyntheticDatasetGenerator.build_logger` (method) `synthetic_dataset.py:614` `def build_logger(level)`
- `SyntheticDatasetGenerator.parse_args` (method) `synthetic_dataset.py:625` `def parse_args()`
- `SyntheticDatasetGenerator.load_paths` (method) `synthetic_dataset.py:652` `def load_paths(paths_arg, paths_file, max_files)` -- Load file paths from CLI args or file.
- `SyntheticDatasetGenerator.main` (method) `synthetic_dataset.py:667` `def main()`

## topogpt3.c
Imported by: `app.py`, `gradio_app.py`
- `printf` (function) `topogpt3.c:28` `extern int printf(const char *, ...);`
- `fprintf` (function) `topogpt3.c:29` `extern int fprintf(FILE *, const char *, ...);`
- `sprintf` (function) `topogpt3.c:30` `extern int sprintf(char *, const char *, ...);`
- `snprintf` (function) `topogpt3.c:31` `extern int snprintf(char *, unsigned long, const char *, ...);`
- `puts` (function) `topogpt3.c:32` `extern int puts(const char *);`
- `putchar` (function) `topogpt3.c:33` `extern int putchar(int);`
- `fputc` (function) `topogpt3.c:34` `extern int fputc(int, FILE *);`
- `fputs` (function) `topogpt3.c:35` `extern int fputs(const char *, FILE *);`
- `fopen` (function) `topogpt3.c:36` `extern FILE *fopen(const char *, const char *);`
- `fclose` (function) `topogpt3.c:37` `extern int fclose(FILE *);`
- `fread` (function) `topogpt3.c:38` `extern unsigned long fread(void *, unsigned long, unsigned long, FILE *);`
- `fwrite` (function) `topogpt3.c:39` `extern unsigned long fwrite(const void *, unsigned long, unsigned long, FILE *);`
- `fseek` (function) `topogpt3.c:40` `extern int fseek(FILE *, long, int);`
- `ftell` (function) `topogpt3.c:41` `extern long ftell(FILE *);`
- `fflush` (function) `topogpt3.c:42` `extern int fflush(FILE *);`
- `malloc` (function) `topogpt3.c:47` `extern void *malloc(unsigned long);` -- define NULL ((void*)0) define SEEK_SET 0 define SEEK_CUR 1 define SEEK_END 2
- `free` (function) `topogpt3.c:48` `extern void free(void *);`
- `memcpy` (function) `topogpt3.c:49` `extern void *memcpy(void *, const void *, unsigned long);`
- `memset` (function) `topogpt3.c:50` `extern void *memset(void *, int, unsigned long);`
- `strcmp` (function) `topogpt3.c:51` `extern int strcmp(const char *, const char *);`
- `strncmp` (function) `topogpt3.c:52` `extern int strncmp(const char *, const char *, unsigned long);`
- `strlen` (function) `topogpt3.c:53` `extern unsigned long strlen(const char *);`
- `strstr` (function) `topogpt3.c:54` `extern char *strstr(const char *, const char *);`
- `tg_exp` (function) `topogpt3.c:114` `static float tg_exp(float x)`
- `tg_tanh` (function) `topogpt3.c:128` `static float tg_tanh(float x)`
- `tg_sin` (function) `topogpt3.c:135` `static float tg_sin(float x)`
- `tg_cos` (function) `topogpt3.c:144` `static float tg_cos(float x)`
- `tg_fabs` (function) `topogpt3.c:148` `static float tg_fabs(float x)`
- `tg_log` (function) `topogpt3.c:152` `static float tg_log(float x)`
- `tg_fmax` (function) `topogpt3.c:164` `static float tg_fmax(float a, float b)`
- `tg_fmin` (function) `topogpt3.c:168` `static float tg_fmin(float a, float b)`
- `load_vocab` (function) `topogpt3.c:255` `static void load_vocab(const char *path)`
- `build_torus_graph` (function) `topogpt3.c:296` `static void build_torus_graph(void)`
- `precompute_rope` (function) `topogpt3.c:327` `static void precompute_rope(void)`
- `matvec` (function) `topogpt3.c:359` `static void matvec(const float *W, const float *x, float *y, int rows, int cols)`
- `matvec_bias` (function) `topogpt3.c:370` `static void matvec_bias(const float *W, const float *b, const float *x, float *y,
               ...`
- `rmsnorm` (function) `topogpt3.c:382` `static void rmsnorm(const float *x, const float *w, float *y, int d)`
- `softmax` (function) `topogpt3.c:391` `static void softmax(float *x, int n)`
- `gelu` (function) `topogpt3.c:400` `static void gelu(float *x, int n)`
- `silu` (function) `topogpt3.c:410` `static void silu(float *x, int n)`
- `swiglu` (function) `topogpt3.c:418` `static void swiglu(const float *gate_w, const float *up_w, const float *down_w,
                 ...`
- `quat_normalize` (function) `topogpt3.c:435` `static void quat_normalize(float *q)`
- `quat_hamilton` (function) `topogpt3.c:440` `static void quat_hamilton(const float *a, const float *b, float *c)`
- `quat_linear` (function) `topogpt3.c:448` `static void quat_linear(const float *Ww, const float *Wx, const float *Wy, const float *Wz,
     ...` -- static void quat_normalize(float *q) { float n = tg_sqrt(q[0]*q[0] + q[1]*q[1] + q[2]*q[2] + q[3]*q[3]); if (n >...
- `ifft_radix2` (function) `topogpt3.c:505` `static void ifft_radix2(float *real, float *imag, int n)`
- `rfft` (function) `topogpt3.c:513` `static void rfft(const float *x, float *Xr, float *Xi, int n)` -- cur_r = nr; } } } } static void ifft_radix2(float *real, float *imag, int n) { int i; for (i = 0; i < n; i++)...
- `irfft` (function) `topogpt3.c:522` `static void irfft(const float *Xr, const float *Xi, float *x, int n)` -- fft_radix2(real, imag, n); for (i = 0; i < n; i++) { real[i] /= (float)n; imag[i] = -imag[i] / (float)n; } } /* Real...
- `filter1d` (function) `topogpt3.c:537` `static void filter1d(const float *x, const float *kr, const float *ki,
                      floa...`
- `ifft2d` (function) `topogpt3.c:580` `static void ifft2d(float *data_r, float *data_i, int h, int w)`
- `rfft2d_real` (function) `topogpt3.c:602` `static void rfft2d_real(const float *data, float *out_r, float *out_i,
                         i...` -- ifft_radix2(row_re, row_im, w); for (c = 0; c < w; c++) { re[r*w+c] = row_re[c]; im[r*w+c] = row_im[c]; } } /* IFFT...
- `irfft2d` (function) `topogpt3.c:629` `static void irfft2d(const float *in_r, const float *in_i, float *out,
                     int h,...` -- for (r = 0; r < h; r++) { col_re[r] = re[r*w+c]; col_im[r] = im[r*w+c]; } fft_radix2(col_re, col_im, h); for (r = 0...
- `cmul` (function) `topogpt3.c:664` `static void cmul(float ar, float ai, float cr, float di, float *rr, float *ri)`
- `spectral_contract` (function) `topogpt3.c:670` `static void spectral_contract(const float *Wr, const float *Wi,
                               co...`
- `quat_spectral_layer_2d` (function) `topogpt3.c:695` `static void quat_spectral_layer_2d(
    const float *x, float *y,
    const float *kr_w, const fl...`
- `spectral_ae_encode` (function) `topogpt3.c:785` `static void spectral_ae_encode(const float *x, float *z, const LayerWeights *lw)`
- `spectral_ae_decode` (function) `topogpt3.c:793` `static void spectral_ae_decode(const float *z, float *x, const LayerWeights *lw)`
- `process_torus_grid` (function) `topogpt3.c:800` `static void process_torus_grid(const float *grid, float *out, const LayerWeights *lw)`
- `torus_soft_assign` (function) `topogpt3.c:821` `static void torus_soft_assign(const float *phi1, const float *phi2,
                             ...`
- `message_passing` (function) `topogpt3.c:843` `static void message_passing(const float *node_feat, float *out,
                             cons...`
- `torus_brain_forward` (function) `topogpt3.c:888` `static void torus_brain_forward(const float *x, float *out, float *recon_loss,
                  ...`
- `attention_forward` (function) `topogpt3.c:978` `static void attention_forward(const float *x, float *out, int layer_idx, int pos, int total_kv_co...`
- `moe_forward` (function) `topogpt3.c:1078` `static void moe_forward(const float *x, float *out, const LayerWeights *lw)`
- `forward` (function) `topogpt3.c:1128` `static void forward(const int *token_ids, int seq_len, float *logits_out)`
- `tokenize_string` (function) `topogpt3.c:1195` `static int tokenize_string(const char *text, int *tokens, int max_tokens)`
- `apply_temperature` (function) `topogpt3.c:1210` `static void apply_temperature(float *logits, int n, float temp)`
- `apply_repetition_penalty` (function) `topogpt3.c:1216` `static void apply_repetition_penalty(float *logits, int n, const int *tokens,
                   ...`
- `apply_top_k` (function) `topogpt3.c:1229` `static void apply_top_k(float *logits, int n, int k)`
- `sample` (function) `topogpt3.c:1248` `static int sample(const float *logits, int n)`
- `load_weights` (function) `topogpt3.c:1282` `static int load_weights(const char *path)`
- `load_weights_fp16` (function) `topogpt3.c:1452` `static int load_weights_fp16(const char *path)`
- `load_weights_auto` (function) `topogpt3.c:1583` `static int load_weights_auto(const char *path)` -- printf("  Layer %d loaded\n", i); } READ_TENSOR16(W.final_norm, D_MODEL); #undef SKIP_TENSOR16 #undef READ_TENSOR16...
- `time_now_ms` (function) `topogpt3.c:1600` `static double time_now_ms(void)`
- `decode_token` (function) `topogpt3.c:1614` `static void decode_token(int tid)`
- `load_token_file` (function) `topogpt3.c:1629` `static int load_token_file(const char *path, int *out_ids, int max_ids)` -- if (tid < 256) { /* Map GPT-2 byte-level encoding back to original byte int n = tid; if (n < 94) n += 33; else if (n...
- `decode_token_tiktoken` (function) `topogpt3.c:1652` `static void decode_token_tiktoken(int tid)` -- if (fread(&n, 4, 1, f) != 1) { fclose(f); return 0; } if (n > (unsigned)max_ids) n = max_ids; int count = (int)n...
- `generate_tokens` (function) `topogpt3.c:1661` `static void generate_tokens(int *prompt_tokens, int n_prompt, int max_new_tokens,
               ...`
- `generate` (function) `topogpt3.c:1725` `static void generate(const char *prompt, int max_new_tokens, float temperature,
                 ...`
- `interactive_mode` (function) `topogpt3.c:1736` `static void interactive_mode(void)`
- `print_help` (function) `topogpt3.c:1850` `static void print_help(void)`
- `main` (function) `topogpt3.c:1885` `int main(int argc, char **argv)`

## topogpt3/__main__.py
Depends on: `topogpt3/api_server.py`, `topogpt3/convert.py`, `topogpt3/export_chat.py`, `topogpt3/inference.py`, `topogpt3/inference_hrm.py`, `topogpt3/jlens.py`, `topogpt3/lens_model.py`, `topogpt3/train.py`, `topogpt3/train_agent.py`, `topogpt3/train_distill.py`, `topogpt3/train_dpo.py`, `topogpt3/train_grpo.py`, `topogpt3/train_lora.py`, `topogpt3/train_ppo.py`
- `main` (function) `topogpt3/__main__.py:6` `def main()` -- TopoGPT3 entry point.

## topogpt3/api_server.py
Depends on: `topogpt3/chat.py`, `topogpt3/continuation.py`, `topogpt3/model.py`
Imported by: `topogpt3/__main__.py`
- `AuthState.validate` (method) `topogpt3/api_server.py:148` `def validate(self, raw)`
- `TokenBucket.consume` (method) `topogpt3/api_server.py:208` `def consume(self, n)`
- `RateLimiter.__init__` (method) `topogpt3/api_server.py:220` `def __init__(self, user_rps, admin_rps, capacity)`
- `RateLimiter.allow` (method) `topogpt3/api_server.py:233` `def allow(self, key, role)`
- `IpBanner.__init__` (method) `topogpt3/api_server.py:251` `def __init__(self, max_failures, window)`
- `IpBanner.record_failure` (method) `topogpt3/api_server.py:257` `def record_failure(self, ip)`
- `IpBanner.is_banned` (method) `topogpt3/api_server.py:265` `def is_banned(self, ip)`
- `ServerModel.complete` (method) `topogpt3/api_server.py:351` `def complete(self, prompt)`
- `ServerModel.stream_complete` (method) `topogpt3/api_server.py:396` `def stream_complete(self, prompt)`
- `ServerModel.load_model` (method) `topogpt3/api_server.py:516` `def load_model(checkpoint, device)`
- `ServerModel.lifespan` (method) `topogpt3/api_server.py:537` `def lifespan(app)`
- `ServerModel.health` (method) `topogpt3/api_server.py:664` `def health(request)`
- `ServerModel.list_models` (method) `topogpt3/api_server.py:671` `def list_models(request)`
- `ServerModel.completions` (method) `topogpt3/api_server.py:688` `def completions(req, request)`
- `ServerModel.chat_completions` (method) `topogpt3/api_server.py:744` `def chat_completions(req, request)`
- `ServerModel.main` (method) `topogpt3/api_server.py:933` `def main()`

## topogpt3/chat.py
Imported by: `tests/test_heritage.py`, `topogpt3/__init__.py`, `topogpt3/api_server.py`, `topogpt3/eval_toolcall.py`, `topogpt3/tools_agent.py`, `topogpt3/train_agent.py`
- `pre_processing_chat` (function) `topogpt3/chat.py:43` `def pre_processing_chat(conversations, add_system_ratio)` -- Randomly prepend a system prompt (skip when tools present).
- `post_processing_chat` (function) `topogpt3/chat.py:54` `def post_processing_chat(prompt, empty_think_ratio)`
- `apply_chat_template` (function) `topogpt3/chat.py:71` `def apply_chat_template(messages, tools, add_generation_prompt, open_thinking)` -- Render messages with tool definitions, thinking and tool-call blocks.
- `parse_tool_calls` (function) `topogpt3/chat.py:116` `def parse_tool_calls(text)`
- `parse_thinking` (function) `topogpt3/chat.py:126` `def parse_thinking(text)`
- `split_reasoning_content` (function) `topogpt3/chat.py:134` `def split_reasoning_content(text)` -- Split generated text into reasoning_content / content / tool_calls (API).

## topogpt3/continuation.py
Imported by: `topogpt3/api_server.py`, `topogpt3/inference_hrm.py`, `topogpt3/model.py`
- `is_response_complete` (function) `topogpt3/continuation.py:45` `def is_response_complete(text, min_chars)` -- Heuristic to decide whether a model response looks finished.
- `extract_tail_for_continuation` (function) `topogpt3/continuation.py:75` `def extract_tail_for_continuation(text, tail_lines, tail_chars)` -- Return the last N lines (or up to tail_chars) of `text` as a continuation prefix to feed back into the model.
- `split_at_last_newline` (function) `topogpt3/continuation.py:105` `def split_at_last_newline(text)` -- Split `text` at the last newline.

## topogpt3/convert.py
Depends on: `topogpt3/lora.py`, `topogpt3/model.py`
Imported by: `topogpt3/__main__.py`
- `merge_base_lora` (function) `topogpt3/convert.py:19` `def merge_base_lora(base_dir, lora_path, out_dir)`
- `export_hf_stub` (function) `topogpt3/convert.py:38` `def export_hf_stub(ckpt_dir, out_dir)`
- `main` (function) `topogpt3/convert.py:49` `def main()`

## topogpt3/eval_toolcall.py
Depends on: `topogpt3/chat.py`, `topogpt3/tools_agent.py`
Imported by: `tests/test_heritage.py`, `topogpt3/__init__.py`
- `run_case` (function) `topogpt3/eval_toolcall.py:19` `def run_case(generate_fn, prompt, expect_tool)`
- `evaluate` (function) `topogpt3/eval_toolcall.py:35` `def evaluate(generate_fn)`

## topogpt3/export_chat.py
Depends on: `topogpt3/model.py`, `topogpt3/train.py`
Imported by: `topogpt3/__main__.py`
- `main` (function) `topogpt3/export_chat.py:81` `def main()`

## topogpt3/inference.py
Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`
- `InferenceSettings.scale_presets` (method) `topogpt3/inference.py:103` `def scale_presets()` -- Return the architecture preset table indexed by scale name.
- `InferenceSettings.preset` (method) `topogpt3/inference.py:116` `def preset(self)` -- Return the resolved preset for the configured model scale.
- `InferenceSettings.validate` (method) `topogpt3/inference.py:126` `def validate(self)` -- Raise ValueError if any setting falls outside its safety bounds.
- `InferenceLoggerFactory.build` (method) `topogpt3/inference.py:162` `def build(settings)` -- Return a configured Logger with a single deduplicated stdout handler.
- `SecurePathResolver.resolve_under` (method) `topogpt3/inference.py:182` `def resolve_under(root)` -- Join `parts` under `root` and return the canonical resolved path.
- `SecurePathResolver.require_existing_file` (method) `topogpt3/inference.py:198` `def require_existing_file(path, expected_suffix)` -- Validate `path` points to an existing regular file with the expected suffix.
- `SourceModuleLoader.__init__` (method) `topogpt3/inference.py:215` `def __init__(self, settings, logger)`
- `SourceModuleLoader.load` (method) `topogpt3/inference.py:219` `def load(self)` -- Return the topogpt3.train module which re-exports model symbols.
- `CheckpointPaths.__init__` (method) `topogpt3/inference.py:231` `def __init__(self, settings)`
- `CheckpointPaths.slot_dir` (method) `topogpt3/inference.py:239` `def slot_dir(self)` -- Directory holding the active checkpoint slot.
- `CheckpointPaths.model_file` (method) `topogpt3/inference.py:243` `def model_file(self)` -- Resolved path to the safetensors weights file inside the slot.
- `CheckpointPaths.state_file` (method) `topogpt3/inference.py:249` `def state_file(self)` -- Resolved path to the JSON training-state file inside the slot.
- `CheckpointPaths.assert_ready` (method) `topogpt3/inference.py:255` `def assert_ready(self)` -- Verify weights exist and the on-disk size lies within safety bounds.
- `WeightShapeProbe.__init__` (method) `topogpt3/inference.py:277` `def __init__(self, settings, logger)`
- `WeightShapeProbe.detect_n_kv_heads` (method) `topogpt3/inference.py:281` `def detect_n_kv_heads(self, weights_path, d_model, n_heads)` -- Recover N_KV_HEADS used at training by inspecting the k_proj shape.
- `TopoGPT2ConfigAligner.__init__` (method) `topogpt3/inference.py:321` `def __init__(self, settings, source_module, logger)`
- `TopoGPT2ConfigAligner.build` (method) `topogpt3/inference.py:327` `def build(self, n_kv_heads, vocab_size)` -- Return a TopoGPT2Config dataclass ready to instantiate the model.
- `TokenizerFactory.__init__` (method) `topogpt3/inference.py:352` `def __init__(self, settings, source_module)`
- `TokenizerFactory.build` (method) `topogpt3/inference.py:356` `def build(self)` -- Return an instance of BPETokenizer bound to the configured encoding.
- `GaussPatchApplier.__init__` (method) `topogpt3/inference.py:365` `def __init__(self, settings, source_module, logger)`
- `GaussPatchApplier.apply_if_enabled` (method) `topogpt3/inference.py:371` `def apply_if_enabled(self)` -- Patch QuaternionSpectralLayer to use the 3-multiply Gauss contract.
- `ModelAssembler.__init__` (method) `topogpt3/inference.py:383` `def __init__(self, settings, source_module, logger)`
- `ModelAssembler.assemble` (method) `topogpt3/inference.py:389` `def assemble(self, aligned_cfg, paths)` -- Build the TopoGPT2 graph, load weights into it, and return it in eval mode.
- `SeedSynchronizer.__init__` (method) `topogpt3/inference.py:420` `def __init__(self, settings, source_module, logger)`
- `SeedSynchronizer.apply` (method) `topogpt3/inference.py:426` `def apply(self)` -- Seed all relevant RNGs using the model package helper when available.
- `SamplingPolicy.from_settings` (method) `topogpt3/inference.py:450` `def from_settings(cls, settings)` -- Construct a SamplingPolicy from inference settings.
- `GenerationReport.tokens_per_second` (method) `topogpt3/inference.py:470` `def tokens_per_second(self, elapsed_floor)` -- Return throughput in tokens/sec, clamped to avoid divide-by-zero.
- `GenerationEngine.__init__` (method) `topogpt3/inference.py:478` `def __init__(self, settings, logger)`
- `GenerationEngine.run` (method) `topogpt3/inference.py:483` `def run(self, model, tokenizer, prompt, policy)` -- Generate a completion for `prompt` and return a GenerationReport.
- `ResultRenderer.__init__` (method) `topogpt3/inference.py:536` `def __init__(self, settings, logger)`
- `ResultRenderer.render` (method) `topogpt3/inference.py:540` `def render(self, report)` -- Emit a banner with prompt and completion, plus a throughput log line.
- `InferencePipeline.__init__` (method) `topogpt3/inference.py:565` `def __init__(self, settings, logger)`
- `InferencePipeline.execute` (method) `topogpt3/inference.py:571` `def execute(self)` -- Run the full inference pipeline end-to-end and return the report.
- `CliArgumentParser.build_parser` (method) `topogpt3/inference.py:619` `def build_parser()` -- Return the configured argparse.ArgumentParser.
- `CliArgumentParser.parse` (method) `topogpt3/inference.py:698` `def parse(argv)` -- Parse `argv` (or sys.argv) and return a populated InferenceSettings.
- `CliArgumentParser.main` (method) `topogpt3/inference.py:721` `def main(argv)` -- CLI entry point.

## topogpt3/inference_hrm.py
Depends on: `topogpt3/continuation.py`
Imported by: `topogpt3/__init__.py`, `topogpt3/__main__.py`
- `HRMInferenceSettings.scale_presets` (method) `topogpt3/inference_hrm.py:221` `def scale_presets()` -- Return the architecture preset table indexed by scale name.
- `HRMInferenceSettings.preset` (method) `topogpt3/inference_hrm.py:234` `def preset(self)` -- Return the resolved preset for the configured model scale.
- `HRMInferenceSettings.validate` (method) `topogpt3/inference_hrm.py:244` `def validate(self)` -- Raise ValueError if any setting falls outside its safety bounds.
- `HRMLoggerFactory.build` (method) `topogpt3/inference_hrm.py:347` `def build(settings)` -- Return a configured Logger with a single deduplicated stdout handler.
- `SecurePathResolver.resolve_under` (method) `topogpt3/inference_hrm.py:367` `def resolve_under(root)` -- Join parts under root and return the canonical resolved path.
- `SecurePathResolver.require_existing_file` (method) `topogpt3/inference_hrm.py:383` `def require_existing_file(path, expected_suffix)` -- Validate path points to an existing regular file with the expected suffix.
- `SourceModuleLoader.__init__` (method) `topogpt3/inference_hrm.py:400` `def __init__(self, settings, logger)`
- `SourceModuleLoader.load` (method) `topogpt3/inference_hrm.py:404` `def load(self)` -- Return the topogpt3.train module which re-exports model symbols.
- `CheckpointPaths.__init__` (method) `topogpt3/inference_hrm.py:416` `def __init__(self, settings)`
- `CheckpointPaths.slot_dir` (method) `topogpt3/inference_hrm.py:424` `def slot_dir(self)` -- Directory holding the active checkpoint slot.
- `CheckpointPaths.model_file` (method) `topogpt3/inference_hrm.py:428` `def model_file(self)` -- Resolved path to the safetensors weights file inside the slot.
- `CheckpointPaths.state_file` (method) `topogpt3/inference_hrm.py:434` `def state_file(self)` -- Resolved path to the JSON training-state file inside the slot.
- `CheckpointPaths.assert_ready` (method) `topogpt3/inference_hrm.py:440` `def assert_ready(self)` -- Verify weights exist and the on-disk size lies within safety bounds.
- `WeightShapeProbe.__init__` (method) `topogpt3/inference_hrm.py:462` `def __init__(self, settings, logger)`
- `WeightShapeProbe.detect_n_kv_heads` (method) `topogpt3/inference_hrm.py:466` `def detect_n_kv_heads(self, weights_path, d_model, n_heads)` -- Recover N_KV_HEADS used at training by inspecting the k_proj shape.
- `TopoGPT2ConfigAligner.__init__` (method) `topogpt3/inference_hrm.py:505` `def __init__(self, settings, source_module, logger)`
- `TopoGPT2ConfigAligner.build` (method) `topogpt3/inference_hrm.py:511` `def build(self, n_kv_heads, vocab_size)` -- Return a TopoGPT2Config dataclass ready to instantiate the model.
- `TokenizerFactory.__init__` (method) `topogpt3/inference_hrm.py:536` `def __init__(self, settings, source_module)`
- `TokenizerFactory.build` (method) `topogpt3/inference_hrm.py:540` `def build(self)` -- Return an instance of BPETokenizer bound to the configured encoding.
- `GaussPatchApplier.__init__` (method) `topogpt3/inference_hrm.py:549` `def __init__(self, settings, source_module, logger)`
- `GaussPatchApplier.apply_if_enabled` (method) `topogpt3/inference_hrm.py:555` `def apply_if_enabled(self)` -- Patch QuaternionSpectralLayer to use the 3-multiply Gauss contract.
- `ModelAssembler.__init__` (method) `topogpt3/inference_hrm.py:567` `def __init__(self, settings, source_module, logger)`
- `ModelAssembler.assemble` (method) `topogpt3/inference_hrm.py:573` `def assemble(self, aligned_cfg, paths)` -- Build the TopoGPT2 graph, load weights into it, and return it in eval mode.
- `SeedSynchronizer.__init__` (method) `topogpt3/inference_hrm.py:604` `def __init__(self, settings, source_module, logger)`
- `SeedSynchronizer.apply` (method) `topogpt3/inference_hrm.py:610` `def apply(self)` -- Seed all relevant RNGs using the model package helper when available.
- `LatentChangeMetric.__init__` (method) `topogpt3/inference_hrm.py:627` `def __init__(self, epsilon_floor)`
- `LatentChangeMetric.relative_change` (method) `topogpt3/inference_hrm.py:632` `def relative_change(self, current, previous)` -- Return ||current - previous|| / max(||previous||, epsilon_floor).
- `GenerationReasoningSummary.absorb` (method) `topogpt3/inference_hrm.py:671` `def absorb(self, sample)` -- Fold a per-token sample into the running totals.
- `SparseHighLevelStateCache.__init__` (method) `topogpt3/inference_hrm.py:693` `def __init__(self, persist_tokens)`
- `SparseHighLevelStateCache.get_or_init` (method) `topogpt3/inference_hrm.py:700` `def get_or_init(self, reference)` -- Return the cached high-level state or a zeroed one when stale.
- `SparseHighLevelStateCache.commit` (method) `topogpt3/inference_hrm.py:716` `def commit(self, new_state)` -- Store a fresh high-level state and increment the cache age.
- `SparseHighLevelStateCache.invalidate` (method) `topogpt3/inference_hrm.py:721` `def invalidate(self)` -- Drop any cached state and reset the age counter.
- `HierarchicalRecursiveReasoner.__init__` (method) `topogpt3/inference_hrm.py:768` `def __init__(self, layers, final_norm, reasoning_config, logger)`
- `HierarchicalRecursiveReasoner.num_layers` (method) `topogpt3/inference_hrm.py:789` `def num_layers(self)` -- Return the number of trained transformer layers.
- `HierarchicalRecursiveReasoner.reason` (method) `topogpt3/inference_hrm.py:827` `def reason(self, z_initial, base_kvs, cached_refinement)` -- Run hierarchical recursive thinking for a single emission step.
- `LogitsSampler.__init__` (method) `topogpt3/inference_hrm.py:938` `def __init__(self, logger)`
- `LogitsSampler.sample` (method) `topogpt3/inference_hrm.py:941` `def sample(self, logits, token_history, temperature, top_k, repetition_penalty)` -- Return a sampled token id tensor of shape [B, 1] from raw logits [B, V].
- `SamplingPolicy.from_settings` (method) `topogpt3/inference_hrm.py:973` `def from_settings(cls, settings)` -- Construct a SamplingPolicy from inference settings.
- `GenerationReport.tokens_per_second` (method) `topogpt3/inference_hrm.py:995` `def tokens_per_second(self, elapsed_floor)` -- Return throughput in tokens/sec, clamped to avoid divide-by-zero.
- `HRMGenerationEngine.__init__` (method) `topogpt3/inference_hrm.py:1011` `def __init__(self, settings, logger)`
- `HRMGenerationEngine.run` (method) `topogpt3/inference_hrm.py:1048` `def run(self, model, tokenizer, prompt, policy)` -- Generate a completion for prompt and return a GenerationReport.
- `ResultRenderer.__init__` (method) `topogpt3/inference_hrm.py:1192` `def __init__(self, settings, logger)`
- `ResultRenderer.render` (method) `topogpt3/inference_hrm.py:1196` `def render(self, report)` -- Emit a banner with prompt, completion, throughput and reasoning stats.
- `HRMInferencePipeline.__init__` (method) `topogpt3/inference_hrm.py:1233` `def __init__(self, settings, logger)`
- `HRMInferencePipeline.execute` (method) `topogpt3/inference_hrm.py:1239` `def execute(self)` -- Run the full inference pipeline end-to-end and return the report.
- `CliArgumentParser.build_parser` (method) `topogpt3/inference_hrm.py:1287` `def build_parser()` -- Return the configured argparse.ArgumentParser.
- `CliArgumentParser.parse` (method) `topogpt3/inference_hrm.py:1448` `def parse(argv)` -- Parse argv (or sys.argv) and return a populated HRMInferenceSettings.
- `CliArgumentParser.main` (method) `topogpt3/inference_hrm.py:1494` `def main(argv)` -- CLI entry point.

## topogpt3/jlens.py
Depends on: `topogpt3/lens_model.py`
Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`
- `ActivationRecorder.__init__` (method) `topogpt3/jlens.py:87` `def __init__(self, blocks, at)`
- `ActivationRecorder.hook` (method) `topogpt3/jlens.py:105` `def hook(module, inputs, output)`
- `ActivationRecorder.valid_position_mask` (method) `topogpt3/jlens.py:132` `def valid_position_mask(seq_len)` -- Boolean mask over sequence positions to include in the Jacobian average.
- `ActivationRecorder.jacobian_for_prompt` (method) `topogpt3/jlens.py:187` `def jacobian_for_prompt(model, prompt, source_layers)` -- Compute the per-layer Jacobian estimator ``J_l`` for one prompt.
- `ActivationRecorder.fit` (method) `topogpt3/jlens.py:291` `def fit(model, prompts)` -- Fit ``J_l`` over a list of prompts and return a JacobianLens.
- `ActivationRecorder.write_checkpoint` (method) `topogpt3/jlens.py:378` `def write_checkpoint()`
- `JacobianLens.__init__` (method) `topogpt3/jlens.py:470` `def __init__(self, jacobians)`
- `JacobianLens.save` (method) `topogpt3/jlens.py:489` `def save(self, path)` -- Save to ``path``.
- `JacobianLens.load` (method) `topogpt3/jlens.py:504` `def load(cls, path)` -- Load a lens previously written by ``save``.
- `JacobianLens.from_pretrained` (method) `topogpt3/jlens.py:519` `def from_pretrained(cls, name_or_path)` -- Load a lens from a local file, a local directory, or a HuggingFace Hub ``repo_id``.
- `JacobianLens.merge` (method) `topogpt3/jlens.py:543` `def merge(cls, lenses)` -- Combine lenses fitted on disjoint prompt subsets into one (``n_prompts``-weighted mean of the inputs).
- `JacobianLens.transport` (method) `topogpt3/jlens.py:574` `def transport(self, residual, layer)` -- Map a residual at ``layer`` into the final-layer basis: ``J_l @ h``.
- `JacobianLens.apply` (method) `topogpt3/jlens.py:585` `def apply(self, model, prompt)` -- Run ``model`` on ``prompt`` and return lens logits at ``positions``.
- `JacobianLens.select` (method) `topogpt3/jlens.py:646` `def select(layer)`
- `SliceData.compute_slice` (method) `topogpt3/jlens.py:705` `def compute_slice(model, lens, prompt)` -- Compute a position x layer slice of top-K token predictions.
- `SliceData.text_slice` (method) `topogpt3/jlens.py:789` `def text_slice(slice_data, tokenizer, n_cols)` -- Render a SliceData as a readable text table showing decoded words.

## topogpt3/lens_model.py
Depends on: `topogpt3/model.py`
Imported by: `tests/test_jlens.py`, `tests/test_lens_model.py`, `topogpt3/__init__.py`, `topogpt3/__main__.py`, `topogpt3/jlens.py`
- `LensModel.encode` (method) `topogpt3/lens_model.py:40` `def encode(self, text)` -- Tokenize ``text`` to ``input_ids`` of shape ``[1, seq_len]`` on the model's input device.
- `LensModel.forward` (method) `topogpt3/lens_model.py:45` `def forward(self, input_ids)` -- Run the residual stack on ``input_ids`` (no LM head).
- `LensModel.unembed` (method) `topogpt3/lens_model.py:52` `def unembed(self, residual)` -- Map a residual-stream tensor ``[..., d_model]`` to logits ``[..., vocab_size]`` (final norm + LM head).
- `TopoGPT3LensConfig.from_topogpt2_config` (method) `topogpt3/lens_model.py:84` `def from_topogpt2_config(cls, cfg)` -- Construct a lens config from a TopoGPT2Config dataclass.
- `TopoGPT3LensConfig.probe_checkpoint` (method) `topogpt3/lens_model.py:104` `def probe_checkpoint(cls, checkpoint_dir)` -- Probe a checkpoint directory and infer lens config from state.json.
- `_TopoGPT3ResidualForward.__init__` (method) `topogpt3/lens_model.py:150` `def __init__(self, model)`
- `_TopoGPT3ResidualForward.forward` (method) `topogpt3/lens_model.py:154` `def forward(self, input_ids)`
- `TopoGPT3LensModel.__init__` (method) `topogpt3/lens_model.py:172` `def __init__(self, model, tokenizer)`
- `TopoGPT3LensModel.n_layers` (method) `topogpt3/lens_model.py:184` `def n_layers(self)`
- `TopoGPT3LensModel.d_model` (method) `topogpt3/lens_model.py:188` `def d_model(self)`
- `TopoGPT3LensModel.layers` (method) `topogpt3/lens_model.py:192` `def layers(self)`
- `TopoGPT3LensModel.tokenizer` (method) `topogpt3/lens_model.py:196` `def tokenizer(self)`
- `TopoGPT3LensModel.tokenizer` (method) `topogpt3/lens_model.py:200` `def tokenizer(self, tok)`
- `TopoGPT3LensModel.input_device` (method) `topogpt3/lens_model.py:204` `def input_device(self)`
- `TopoGPT3LensModel.input_device` (method) `topogpt3/lens_model.py:210` `def input_device(self, device)`
- `TopoGPT3LensModel.encode` (method) `topogpt3/lens_model.py:213` `def encode(self, text)` -- Tokenize text to input_ids of shape ``[1, seq_len]``.
- `TopoGPT3LensModel.forward` (method) `topogpt3/lens_model.py:228` `def forward(self, input_ids)` -- Run the residual stack on ``input_ids``.
- `TopoGPT3LensModel.unembed` (method) `topogpt3/lens_model.py:237` `def unembed(self, residual)` -- Map residual ``[..., d_model]`` to logits ``[..., vocab_size]``.
- `TopoGPT3LensModel.from_checkpoint` (method) `topogpt3/lens_model.py:246` `def from_checkpoint(cls, checkpoint_dir)` -- Build a TopoGPT3LensModel from a checkpoint directory.
- `TinyDecoder.__init__` (method) `topogpt3/lens_model.py:315` `def __init__(self, n_layers, d_model, vocab_size, seed)`
- `TinyDecoder.forward` (method) `topogpt3/lens_model.py:344` `def forward(self, token_ids, past_kvs)`
- `_ResidualBlock.__init__` (method) `topogpt3/lens_model.py:360` `def __init__(self, d_model)`
- `_ResidualBlock.forward` (method) `topogpt3/lens_model.py:366` `def forward(self, x, past_kv)`

## topogpt3/lora.py
Imported by: `tests/test_heritage.py`, `topogpt3/__init__.py`, `topogpt3/convert.py`, `topogpt3/train_lora.py`
- `LoRA.__init__` (method) `topogpt3/lora.py:17` `def __init__(self, in_features, out_features, rank)`
- `LoRA.forward` (method) `topogpt3/lora.py:25` `def forward(self, x)`
- `LoRA.lora_targets` (method) `topogpt3/lora.py:34` `def lora_targets(model, include_mlp)` -- Yield (name, nn.Linear) candidates.
- `LoRA.apply_lora` (method) `topogpt3/lora.py:54` `def apply_lora(model, rank, include_mlp)` -- Monkey-patch target linears with additive LoRA.
- `LoRA.lora_parameters` (method) `topogpt3/lora.py:73` `def lora_parameters(model)`
- `LoRA.freeze_non_lora` (method) `topogpt3/lora.py:80` `def freeze_non_lora(model)`
- `LoRA.save_lora` (method) `topogpt3/lora.py:88` `def save_lora(model, path)`
- `LoRA.load_lora` (method) `topogpt3/lora.py:99` `def load_lora(model, path, device)`
- `LoRA.merge_lora` (method) `topogpt3/lora.py:110` `def merge_lora(model, lora_path, save_path)` -- Merge LoRA deltas into base weights and save (fp16, no .lora. keys).


Next: [API_p2.md](API_p2.md)
