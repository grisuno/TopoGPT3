# Subsystem: root

## app.py
- Layer: utility
- Doc: Drop-in entry point that demonstrates how to use the topogpt3 package.  This file lives outside the package on purpose. 
- Language: py
- Symbols:
  - `run_inference` (function, line 46) `def run_inference(prompt, checkpoint_dir, checkpoint_name, max_new_tokens, temperature, top_k, repetition_penalty, device)`
  - `run_inference_hrm` (function, line 71) `def run_inference_hrm(prompt, checkpoint_dir, checkpoint_name, max_new_tokens, temperature, top_k, repetition_penalty, high_level_iters, low_level_iters, low_level_window, device)`
  - `run_training` (function, line 105) `def run_training(scale, start_tier, device, prepare_data)`
  - `_build_parser` (function, line 121) `def _build_parser()`
  - `main` (function, line 159) `def main(argv)`
- Depends on: `topogpt3.c`

## convert_weights.py
- Layer: utility
- Doc: TopoGPT3 Weight Converter: safetensors -> flat float32 binary.  Usage: python convert_weights.py [--input model.safetens
- Language: py
- Symbols:
  - `convert` (function, line 102) `def convert(input_path, output_path)`
  - `main` (function, line 160) `def main()`

## convert_weights_minios.py
- Layer: utility
- Doc: Convert TopoGPT3 safetensors weights to float16 binary for MiniOS.  Produces a compact weight file (~47MB vs 94MB float3
- Language: py
- Symbols:
  - `main` (function, line 85) `def main()`

## encode_tokens.py
- Layer: utility
- Doc: Tokenize text using GPT-2 BPE and output binary token IDs.  Usage: python tokenize.py "text to tokenize" -o tokens.bin e
- Language: py
- Symbols:
  - `main` (function, line 19) `def main()`

## gradio_app.py
- Layer: infrastructure
- Doc: TopoGPT3 Gradio Interface for Hugging Face Spaces.  Drop-in Gradio app exposing both standard and HRM inference modes. D
- Language: py
- Symbols:
  - `ensure_checkpoint` (function, line 35) `def ensure_checkpoint()`
  - `run_standard_inference` (function, line 59) `def run_standard_inference(prompt, max_new_tokens, temperature, top_k, repetition_penalty, auto_continue)`
  - `run_hrm_inference` (function, line 95) `def run_hrm_inference(prompt, max_new_tokens, temperature, top_k, repetition_penalty, high_level_iters, low_level_iters, low_level_window, thinking, auto_continue)`
  - `build_ui` (function, line 144) `def build_ui()`
- Depends on: `topogpt3.c`

## install.sh
- Layer: utility
- Language: sh

## synthetic_dataset.py
- Layer: data_access
- Doc: Synthetic Dataset Generator for TopoGPT2.  Generates high-quality code instruction-tuning data from existing source file
- Language: py
- Symbols:
  - `LLMBackend` (class, line 61) `class LLMBackend`
  - `GroqBackend` (class, line 71) `class GroqBackend(LLMBackend)`
  - `OpenRouterBackend` (class, line 121) `class OpenRouterBackend(LLMBackend)`
  - `OllamaBackend` (class, line 177) `class OllamaBackend(LLMBackend)`
  - `build_backend` (method, line 227) `def build_backend(provider, model)`
  - `validate_sample` (method, line 330) `def validate_sample(sample)`
  - `ProcessedManifest` (class, line 364) `class ProcessedManifest`
  - `SyntheticDatasetGenerator` (class, line 399) `class SyntheticDatasetGenerator`
  - `build_logger` (method, line 614) `def build_logger(level)`
  - `parse_args` (method, line 625) `def parse_args()`
  - `load_paths` (method, line 652) `def load_paths(paths_arg, paths_file, max_files)`
  - `main` (method, line 667) `def main()`
  - `generate` (method, line 64) `def generate(self, prompt)`
  - `name` (method, line 67) `def name(self)`
  - `__init__` (method, line 78) `def __init__(self, model, api_key, max_tokens, temperature, timeout)`
  - `name` (method, line 95) `def name(self)`
  - `generate` (method, line 98) `def generate(self, prompt)`
  - `__init__` (method, line 132) `def __init__(self, model, api_key, max_tokens, temperature, timeout)`
  - `name` (method, line 151) `def name(self)`
  - `generate` (method, line 154) `def generate(self, prompt)`
  - `__init__` (method, line 184) `def __init__(self, model, host, max_tokens, temperature, timeout)`
  - `name` (method, line 198) `def name(self)`
  - `generate` (method, line 201) `def generate(self, prompt)`
  - `load` (method, line 374) `def load(path)`
  - `save` (method, line 387) `def save(self, path)`
  - `__init__` (method, line 418) `def __init__(self, backend, output_path, manifest_path, logger, max_workers, max_file_chars)`
  - `_jsonl_writer` (method, line 447) `def _jsonl_writer(self)`
  - `_enqueue_sample` (method, line 465) `def _enqueue_sample(self, sample)`
  - `_flush_writer` (method, line 468) `def _flush_writer(self)`
  - `_read_file` (method, line 477) `def _read_file(self, path)`
  - `_build_prompt` (method, line 490) `def _build_prompt(self, content, lang)`
  - `_generate_sample` (method, line 496) `def _generate_sample(self, content, lang)`
  - `process_file` (method, line 533) `def process_file(self, path)`
  - `process_batch` (method, line 568) `def process_batch(self, paths)`
  - `finish` (method, line 590) `def finish(self)`
- Imported by: `topogpt3/model.py`

## topogpt3.c
- Layer: utility
- Language: c
- Symbols:
  - `FILE` (struct, line 24)
  - `LayerWeights` (struct, line 176)
  - `ModelWeights` (struct, line 224)
  - `tg_exp` (function, line 114) `static float tg_exp(float x)`
  - `tg_tanh` (function, line 128) `static float tg_tanh(float x)`
  - `tg_sin` (function, line 135) `static float tg_sin(float x)`
  - `tg_cos` (function, line 144) `static float tg_cos(float x)`
  - `tg_fabs` (function, line 148) `static float tg_fabs(float x)`
  - `tg_log` (function, line 152) `static float tg_log(float x)`
  - `tg_fmax` (function, line 164) `static float tg_fmax(float a, float b)`
  - `tg_fmin` (function, line 168) `static float tg_fmin(float a, float b)`
  - `load_vocab` (function, line 255) `static void load_vocab(const char *path)`
  - `build_torus_graph` (function, line 296) `static void build_torus_graph(void)`
  - `precompute_rope` (function, line 327) `static void precompute_rope(void)`
  - `matvec` (function, line 359) `static void matvec(const float *W, const float *x, float *y, int rows, int cols)`
  - `matvec_bias` (function, line 370) `static void matvec_bias(const float *W, const float *b, const float *x, float *y,
               ...`
  - `rmsnorm` (function, line 382) `static void rmsnorm(const float *x, const float *w, float *y, int d)`
  - `softmax` (function, line 391) `static void softmax(float *x, int n)`
  - `gelu` (function, line 400) `static void gelu(float *x, int n)`
  - `silu` (function, line 410) `static void silu(float *x, int n)`
  - `swiglu` (function, line 418) `static void swiglu(const float *gate_w, const float *up_w, const float *down_w,
                 ...`
  - `quat_normalize` (function, line 435) `static void quat_normalize(float *q)`
  - `quat_hamilton` (function, line 440) `static void quat_hamilton(const float *a, const float *b, float *c)`
  - `quat_linear` (function, line 448) `static void quat_linear(const float *Ww, const float *Wx, const float *Wy, const float *Wz,
     ...`
  - `ifft_radix2` (function, line 505) `static void ifft_radix2(float *real, float *imag, int n)`
  - `rfft` (function, line 513) `static void rfft(const float *x, float *Xr, float *Xi, int n)`
  - `irfft` (function, line 522) `static void irfft(const float *Xr, const float *Xi, float *x, int n)`
  - `filter1d` (function, line 537) `static void filter1d(const float *x, const float *kr, const float *ki,
                      floa...`
  - `ifft2d` (function, line 580) `static void ifft2d(float *data_r, float *data_i, int h, int w)`
  - `rfft2d_real` (function, line 602) `static void rfft2d_real(const float *data, float *out_r, float *out_i,
                         i...`
  - `irfft2d` (function, line 629) `static void irfft2d(const float *in_r, const float *in_i, float *out,
                     int h,...`
  - `cmul` (function, line 664) `static void cmul(float ar, float ai, float cr, float di, float *rr, float *ri)`
  - `spectral_contract` (function, line 670) `static void spectral_contract(const float *Wr, const float *Wi,
                               co...`
  - `quat_spectral_layer_2d` (function, line 695) `static void quat_spectral_layer_2d(
    const float *x, float *y,
    const float *kr_w, const fl...`
  - `spectral_ae_encode` (function, line 785) `static void spectral_ae_encode(const float *x, float *z, const LayerWeights *lw)`
  - `spectral_ae_decode` (function, line 793) `static void spectral_ae_decode(const float *z, float *x, const LayerWeights *lw)`
  - `process_torus_grid` (function, line 800) `static void process_torus_grid(const float *grid, float *out, const LayerWeights *lw)`
  - `torus_soft_assign` (function, line 821) `static void torus_soft_assign(const float *phi1, const float *phi2,
                             ...`
  - `message_passing` (function, line 843) `static void message_passing(const float *node_feat, float *out,
                             cons...`
  - `torus_brain_forward` (function, line 888) `static void torus_brain_forward(const float *x, float *out, float *recon_loss,
                  ...`
  - `attention_forward` (function, line 978) `static void attention_forward(const float *x, float *out, int layer_idx, int pos, int total_kv_co...`
  - `moe_forward` (function, line 1078) `static void moe_forward(const float *x, float *out, const LayerWeights *lw)`
  - `forward` (function, line 1128) `static void forward(const int *token_ids, int seq_len, float *logits_out)`
  - `tokenize_string` (function, line 1195) `static int tokenize_string(const char *text, int *tokens, int max_tokens)`
  - `apply_temperature` (function, line 1210) `static void apply_temperature(float *logits, int n, float temp)`
  - `apply_repetition_penalty` (function, line 1216) `static void apply_repetition_penalty(float *logits, int n, const int *tokens,
                   ...`
  - `apply_top_k` (function, line 1229) `static void apply_top_k(float *logits, int n, int k)`
  - `sample` (function, line 1248) `static int sample(const float *logits, int n)`
  - `load_weights` (function, line 1282) `static int load_weights(const char *path)`
  - `load_weights_fp16` (function, line 1452) `static int load_weights_fp16(const char *path)`
  - `load_weights_auto` (function, line 1583) `static int load_weights_auto(const char *path)`
  - `time_now_ms` (function, line 1600) `static double time_now_ms(void)`
  - `decode_token` (function, line 1614) `static void decode_token(int tid)`
  - `load_token_file` (function, line 1629) `static int load_token_file(const char *path, int *out_ids, int max_ids)`
  - `decode_token_tiktoken` (function, line 1652) `static void decode_token_tiktoken(int tid)`
  - `generate_tokens` (function, line 1661) `static void generate_tokens(int *prompt_tokens, int n_prompt, int max_new_tokens,
               ...`
  - `generate` (function, line 1725) `static void generate(const char *prompt, int max_new_tokens, float temperature,
                 ...`
  - `interactive_mode` (function, line 1736) `static void interactive_mode(void)`
  - `print_help` (function, line 1850) `static void print_help(void)`
  - `main` (function, line 1885) `int main(int argc, char **argv)`
  - `printf` (function, line 28) `extern int printf(const char *, ...);`
  - `fprintf` (function, line 29) `extern int fprintf(FILE *, const char *, ...);`
  - `sprintf` (function, line 30) `extern int sprintf(char *, const char *, ...);`
  - `snprintf` (function, line 31) `extern int snprintf(char *, unsigned long, const char *, ...);`
  - `puts` (function, line 32) `extern int puts(const char *);`
  - `putchar` (function, line 33) `extern int putchar(int);`
  - `fputc` (function, line 34) `extern int fputc(int, FILE *);`
  - `fputs` (function, line 35) `extern int fputs(const char *, FILE *);`
  - `fopen` (function, line 36) `extern FILE *fopen(const char *, const char *);`
  - `fclose` (function, line 37) `extern int fclose(FILE *);`
  - `fread` (function, line 38) `extern unsigned long fread(void *, unsigned long, unsigned long, FILE *);`
  - `fwrite` (function, line 39) `extern unsigned long fwrite(const void *, unsigned long, unsigned long, FILE *);`
  - `fseek` (function, line 40) `extern int fseek(FILE *, long, int);`
  - `ftell` (function, line 41) `extern long ftell(FILE *);`
  - `fflush` (function, line 42) `extern int fflush(FILE *);`
  - `malloc` (function, line 47) `extern void *malloc(unsigned long);`
  - `free` (function, line 48) `extern void free(void *);`
  - `memcpy` (function, line 49) `extern void *memcpy(void *, const void *, unsigned long);`
  - `memset` (function, line 50) `extern void *memset(void *, int, unsigned long);`
  - `strcmp` (function, line 51) `extern int strcmp(const char *, const char *);`
  - `strncmp` (function, line 52) `extern int strncmp(const char *, const char *, unsigned long);`
  - `strlen` (function, line 53) `extern unsigned long strlen(const char *);`
  - `strstr` (function, line 54) `extern char *strstr(const char *, const char *);`
  - `stdin` (variable, line 25) `extern FILE *stdin;`
  - `stdout` (variable, line 26) `extern FILE *stdout;`
  - `stderr` (variable, line 27) `extern FILE *stderr;`
  - `NULL` (macro, line 43) `#define NULL`
  - `SEEK_SET` (macro, line 44) `#define SEEK_SET`
  - `SEEK_CUR` (macro, line 45) `#define SEEK_CUR`
  - `SEEK_END` (macro, line 46) `#define SEEK_END`
  - `VOCAB_SIZE` (macro, line 65) `#define VOCAB_SIZE`
  - `D_MODEL` (macro, line 66) `#define D_MODEL`
  - `N_HEADS` (macro, line 67) `#define N_HEADS`
  - `N_KV_HEADS` (macro, line 68) `#define N_KV_HEADS`
  - `GQA_GROUPS` (macro, line 69) `#define GQA_GROUPS`
  - `D_HEAD` (macro, line 70) `#define D_HEAD`
  - `D_QUAT` (macro, line 71) `#define D_QUAT`
  - `N_LAYERS` (macro, line 72) `#define N_LAYERS`
  - `MAX_SEQ_LEN` (macro, line 73) `#define MAX_SEQ_LEN`
  - `N_EXPERTS` (macro, line 74) `#define N_EXPERTS`
  - `MOE_TOP_K` (macro, line 75) `#define MOE_TOP_K`
  - `N_NODES` (macro, line 76) `#define N_NODES`
  - `N_RADIAL` (macro, line 77) `#define N_RADIAL`
  - `N_ANGULAR` (macro, line 78) `#define N_ANGULAR`
  - `N_EDGE_TYPES` (macro, line 79) `#define N_EDGE_TYPES`
  - `N_EDGES` (macro, line 80) `#define N_EDGES`
  - `SPECTRAL_LATENT_DIM` (macro, line 81) `#define SPECTRAL_LATENT_DIM`
  - `D_LAT_Q` (macro, line 82) `#define D_LAT_Q`
  - `TORUS_GRID_H` (macro, line 83) `#define TORUS_GRID_H`
  - `TORUS_GRID_W` (macro, line 84) `#define TORUS_GRID_W`
  - `FREQ_W` (macro, line 85) `#define FREQ_W`
  - `N_SPECTRAL_LAYERS` (macro, line 86) `#define N_SPECTRAL_LAYERS`
  - `EXPERT_INNER` (macro, line 87) `#define EXPERT_INNER`
  - `READOUT_INNER` (macro, line 88) `#define READOUT_INNER`
  - `EOS_TOKEN` (macro, line 89) `#define EOS_TOKEN`
  - `EMBED_INNER` (macro, line 90) `#define EMBED_INNER`
  - `PI` (macro, line 91) `#define PI`
  - `EPS_RMS` (macro, line 92) `#define EPS_RMS`
  - `TORUS_TEMP` (macro, line 93) `#define TORUS_TEMP`
  - `MAX_TOKENS` (macro, line 94) `#define MAX_TOKENS`
  - `MAX_PROMPT_LEN` (macro, line 95) `#define MAX_PROMPT_LEN`
  - `MAX_LINE` (macro, line 96) `#define MAX_LINE`
  - `TOK_TAB_SIZE` (macro, line 97) `#define TOK_TAB_SIZE`
  - `TOK_VOCAB_SIZE` (macro, line 98) `#define TOK_VOCAB_SIZE`
  - `SKIP_TENSOR` (macro, line 1300) `#define SKIP_TENSOR()`
  - `READ_TENSOR` (macro, line 1310) `#define READ_TENSOR(dest, count)`
  - `SKIP_TENSOR16` (macro, line 1470) `#define SKIP_TENSOR16()`
  - `READ_TENSOR16` (macro, line 1480) `#define READ_TENSOR16(dest, count)`
- Imported by: `app.py`, `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`, `gradio_app.py`
