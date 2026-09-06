# Subsystem: root

## app.py
- Layer: utility
- Language: py
- Symbols:
  - `run_inference` (function, line 46) `def run_inference(prompt, checkpoint_dir, checkpoint_name, max_new_tokens, temperature, top_k, repetition_penalty, device)`
  - `run_inference_hrm` (function, line 71) `def run_inference_hrm(prompt, checkpoint_dir, checkpoint_name, max_new_tokens, temperature, top_k, repetition_penalty, high_level_iters, low_level_iters, low_level_window, device)`
  - `run_training` (function, line 105) `def run_training(scale, start_tier, device, prepare_data)`
  - `_build_parser` (function, line 121) `def _build_parser()`
  - `main` (function, line 159) `def main(argv)`
- Depends on: `topogpt3/__init__.py`

## convert_weights.py
- Layer: utility
- Language: py
- Symbols:
  - `convert` (function, line 102) `def convert(input_path, output_path)`
  - `main` (function, line 160) `def main()`

## convert_weights_minios.py
- Layer: utility
- Language: py
- Symbols:
  - `main` (function, line 85) `def main()`

## encode_tokens.py
- Layer: utility
- Language: py
- Symbols:
  - `main` (function, line 19) `def main()`

## gradio_app.py
- Layer: infrastructure
- Language: py
- Symbols:
  - `ensure_checkpoint` (function, line 35) `def ensure_checkpoint()`
  - `run_standard_inference` (function, line 59) `def run_standard_inference(prompt, max_new_tokens, temperature, top_k, repetition_penalty, auto_continue)`
  - `run_hrm_inference` (function, line 95) `def run_hrm_inference(prompt, max_new_tokens, temperature, top_k, repetition_penalty, high_level_iters, low_level_iters, low_level_window, thinking, auto_continue)`
  - `build_ui` (function, line 144) `def build_ui()`
- Depends on: `topogpt3/__init__.py`

## install.sh
- Layer: utility
- Language: sh

## synthetic_dataset.py
- Layer: data_access
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
  - `tg_exp` (function, line 113) `static float tg_exp(float x)`
  - `tg_tanh` (function, line 127) `static float tg_tanh(float x)`
  - `tg_sin` (function, line 134) `static float tg_sin(float x)`
  - `tg_cos` (function, line 143) `static float tg_cos(float x)`
  - `tg_fabs` (function, line 147) `static float tg_fabs(float x)`
  - `tg_log` (function, line 151) `static float tg_log(float x)`
  - `tg_fmax` (function, line 163) `static float tg_fmax(float a, float b)`
  - `tg_fmin` (function, line 167) `static float tg_fmin(float a, float b)`
  - `load_vocab` (function, line 254) `static void load_vocab(const char *path)`
  - `build_torus_graph` (function, line 295) `static void build_torus_graph(void)`
  - `precompute_rope` (function, line 326) `static void precompute_rope(void)`
  - `matvec` (function, line 358) `static void matvec(const float *W, const float *x, float *y, int rows, int cols)`
  - `matvec_bias` (function, line 369) `static void matvec_bias(const float *W, const float *b, const float *x, float *y,
               ...`
  - `rmsnorm` (function, line 381) `static void rmsnorm(const float *x, const float *w, float *y, int d)`
  - `softmax` (function, line 390) `static void softmax(float *x, int n)`
  - `gelu` (function, line 399) `static void gelu(float *x, int n)`
  - `silu` (function, line 409) `static void silu(float *x, int n)`
  - `swiglu` (function, line 417) `static void swiglu(const float *gate_w, const float *up_w, const float *down_w,
                 ...`
  - `quat_normalize` (function, line 434) `static void quat_normalize(float *q)`
  - `quat_hamilton` (function, line 439) `static void quat_hamilton(const float *a, const float *b, float *c)`
  - `quat_linear` (function, line 448) `static void quat_linear(const float *Ww, const float *Wx, const float *Wy, const float *Wz,
     ...`
  - `ifft_radix2` (function, line 504) `static void ifft_radix2(float *real, float *imag, int n)`
  - `rfft` (function, line 513) `static void rfft(const float *x, float *Xr, float *Xi, int n)`
  - `irfft` (function, line 522) `static void irfft(const float *Xr, const float *Xi, float *x, int n)`
  - `filter1d` (function, line 536) `static void filter1d(const float *x, const float *kr, const float *ki,
                      floa...`
  - `ifft2d` (function, line 579) `static void ifft2d(float *data_r, float *data_i, int h, int w)`
  - `rfft2d_real` (function, line 602) `static void rfft2d_real(const float *data, float *out_r, float *out_i,
                         i...`
  - `irfft2d` (function, line 629) `static void irfft2d(const float *in_r, const float *in_i, float *out,
                     int h,...`
  - `cmul` (function, line 664) `static void cmul(float ar, float ai, float cr, float di, float *rr, float *ri)`
  - `spectral_contract` (function, line 670) `static void spectral_contract(const float *Wr, const float *Wi,
                               co...`
  - `quat_spectral_layer_2d` (function, line 694) `static void quat_spectral_layer_2d(
    const float *x, float *y,
    const float *kr_w, const fl...`
  - `spectral_ae_encode` (function, line 784) `static void spectral_ae_encode(const float *x, float *z, const LayerWeights *lw)`
  - `spectral_ae_decode` (function, line 792) `static void spectral_ae_decode(const float *z, float *x, const LayerWeights *lw)`
  - `process_torus_grid` (function, line 799) `static void process_torus_grid(const float *grid, float *out, const LayerWeights *lw)`
  - `torus_soft_assign` (function, line 820) `static void torus_soft_assign(const float *phi1, const float *phi2,
                             ...`
  - `message_passing` (function, line 842) `static void message_passing(const float *node_feat, float *out,
                             cons...`
  - `torus_brain_forward` (function, line 887) `static void torus_brain_forward(const float *x, float *out, float *recon_loss,
                  ...`
  - `attention_forward` (function, line 977) `static void attention_forward(const float *x, float *out, int layer_idx, int pos, int total_kv_co...`
  - `moe_forward` (function, line 1077) `static void moe_forward(const float *x, float *out, const LayerWeights *lw)`
  - `forward` (function, line 1127) `static void forward(const int *token_ids, int seq_len, float *logits_out)`
  - `tokenize_string` (function, line 1194) `static int tokenize_string(const char *text, int *tokens, int max_tokens)`
  - `apply_temperature` (function, line 1209) `static void apply_temperature(float *logits, int n, float temp)`
  - `apply_repetition_penalty` (function, line 1215) `static void apply_repetition_penalty(float *logits, int n, const int *tokens,
                   ...`
  - `apply_top_k` (function, line 1228) `static void apply_top_k(float *logits, int n, int k)`
  - `sample` (function, line 1247) `static int sample(const float *logits, int n)`
  - `load_weights` (function, line 1281) `static int load_weights(const char *path)`
  - `load_weights_fp16` (function, line 1451) `static int load_weights_fp16(const char *path)`
  - `load_weights_auto` (function, line 1583) `static int load_weights_auto(const char *path)`
  - `time_now_ms` (function, line 1600) `static double time_now_ms(void)`
  - `decode_token` (function, line 1613) `static void decode_token(int tid)`
  - `load_token_file` (function, line 1629) `static int load_token_file(const char *path, int *out_ids, int max_ids)`
  - `decode_token_tiktoken` (function, line 1652) `static void decode_token_tiktoken(int tid)`
  - `generate_tokens` (function, line 1660) `static void generate_tokens(int *prompt_tokens, int n_prompt, int max_new_tokens,
               ...`
  - `generate` (function, line 1724) `static void generate(const char *prompt, int max_new_tokens, float temperature,
                 ...`
  - `interactive_mode` (function, line 1735) `static void interactive_mode(void)`
  - `print_help` (function, line 1849) `static void print_help(void)`
  - `main` (function, line 1884) `int main(int argc, char **argv)`
  - `NULL` (macro, line 43)
  - `SEEK_SET` (macro, line 44)
  - `SEEK_CUR` (macro, line 45)
  - `SEEK_END` (macro, line 46)
  - `VOCAB_SIZE` (macro, line 64)
  - `D_MODEL` (macro, line 66)
  - `N_HEADS` (macro, line 67)
  - `N_KV_HEADS` (macro, line 68)
  - `GQA_GROUPS` (macro, line 69)
  - `D_HEAD` (macro, line 70)
  - `D_QUAT` (macro, line 71)
  - `N_LAYERS` (macro, line 72)
  - `MAX_SEQ_LEN` (macro, line 73)
  - `N_EXPERTS` (macro, line 74)
  - `MOE_TOP_K` (macro, line 75)
  - `N_NODES` (macro, line 76)
  - `N_RADIAL` (macro, line 77)
  - `N_ANGULAR` (macro, line 78)
  - `N_EDGE_TYPES` (macro, line 79)
  - `N_EDGES` (macro, line 80)
  - `SPECTRAL_LATENT_DIM` (macro, line 81)
  - `D_LAT_Q` (macro, line 82)
  - `TORUS_GRID_H` (macro, line 83)
  - `TORUS_GRID_W` (macro, line 84)
  - `FREQ_W` (macro, line 85)
  - `N_SPECTRAL_LAYERS` (macro, line 86)
  - `EXPERT_INNER` (macro, line 87)
  - `READOUT_INNER` (macro, line 88)
  - `EOS_TOKEN` (macro, line 89)
  - `EMBED_INNER` (macro, line 90)
  - `PI` (macro, line 91)
  - `EPS_RMS` (macro, line 92)
  - `TORUS_TEMP` (macro, line 93)
  - `MAX_TOKENS` (macro, line 94)
  - `MAX_PROMPT_LEN` (macro, line 95)
  - `MAX_LINE` (macro, line 96)
  - `TOK_TAB_SIZE` (macro, line 97)
  - `TOK_VOCAB_SIZE` (macro, line 98)
  - `SKIP_TENSOR` (macro, line 1300)
  - `READ_TENSOR` (macro, line 1310)
  - `SKIP_TENSOR16` (macro, line 1470)
  - `READ_TENSOR16` (macro, line 1480)
- Imported by: `eval/diag_static.py`, `eval/governor_smoke.py`, `eval/harness.py`, `eval/noise_sweep.py`, `eval/repair.py`, `eval/samplers.py`, `eval/smoke.py`
