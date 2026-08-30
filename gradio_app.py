#!/usr/bin/env python3
"""TopoGPT3 Gradio Interface for Hugging Face Spaces.

Drop-in Gradio app exposing both standard and HRM inference modes.
Designed for deployment on Hugging Face Spaces with automatic checkpoint
download from the Hub.

Usage:
    python gradio_app.py                          # local launch
    gradio_app.py  (as HF Spaces entry point)     # auto-detected
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

import torch
import gradio as gr

from topogpt3 import (
    HRMInferencePipeline,
    HRMInferenceSettings,
    InferencePipeline,
    InferenceSettings,
    RecursiveReasoningConfig,
    __version__,
)

DEFAULT_CHECKPOINT_DIR = "checkpoints_topogpt3"
HF_REPO = "grisiscomeback/TopoGPT3"
HF_CHECKPOINT_SUBPATH = "checkpoints_topogpt3/last"


def ensure_checkpoint() -> str:
    """Return the path to the checkpoint directory, downloading if needed."""
    ckpt_dir = Path(DEFAULT_CHECKPOINT_DIR)
    if ckpt_dir.exists() and any(ckpt_dir.iterdir()):
        return str(ckpt_dir)

    # Try downloading from Hugging Face Hub
    try:
        from huggingface_hub import snapshot_download
        print(f"Downloading checkpoint from {HF_REPO}...")
        snapshot_download(
            repo_id=HF_REPO,
            repo_type="model",
            local_dir=DEFAULT_CHECKPOINT_DIR,
            allow_patterns=[f"{HF_CHECKPOINT_SUBPATH}/*"],
        )
        print("Checkpoint downloaded successfully.")
        return str(ckpt_dir)
    except Exception as e:
        print(f"Warning: Could not download checkpoint: {e}")
        print("Please ensure the checkpoint is available at:", ckpt_dir)
        return str(ckpt_dir)


def run_standard_inference(
    prompt: str,
    max_new_tokens: int,
    temperature: float,
    top_k: int,
    repetition_penalty: float,
    auto_continue: bool,
) -> str:
    """Run standard autoregressive inference."""
    if not prompt.strip():
        return "Error: Please enter a prompt."

    settings = InferenceSettings(
        prompt=prompt,
        checkpoint_dir=ensure_checkpoint(),
        checkpoint_name="last",
        max_new_tokens=int(max_new_tokens),
        temperature=float(temperature),
        top_k=int(top_k),
        repetition_penalty=float(repetition_penalty),
        auto_continue=auto_continue,
        device="cuda" if torch.cuda.is_available() else "cpu",
    )
    report = InferencePipeline(settings).execute()
    completion = report.output
    if completion.startswith(prompt):
        completion = completion[len(prompt):]
    stats = (
        f"\n\n---\n"
        f"Tokens: {report.prompt_tokens} prompt + {report.new_tokens} new | "
        f"Time: {report.elapsed_seconds:.2f}s | "
        f"Speed: {report.tokens_per_second(1e-3):.1f} tok/s"
    )
    return completion + stats


def run_hrm_inference(
    prompt: str,
    max_new_tokens: int,
    temperature: float,
    top_k: int,
    repetition_penalty: float,
    high_level_iters: int,
    low_level_iters: int,
    low_level_window: int,
    thinking: bool,
    auto_continue: bool,
) -> str:
    """Run hierarchical recursive reasoning inference."""
    if not prompt.strip():
        return "Error: Please enter a prompt."

    h_iters = 4 if thinking else int(high_level_iters)
    l_iters = 8 if thinking else int(low_level_iters)

    reasoning = RecursiveReasoningConfig(
        max_high_level_iters=h_iters,
        max_low_level_iters=l_iters,
        low_level_window=int(low_level_window),
    )
    settings = HRMInferenceSettings(
        prompt=prompt,
        checkpoint_dir=ensure_checkpoint(),
        checkpoint_name="last",
        max_new_tokens=int(max_new_tokens),
        temperature=float(temperature),
        top_k=int(top_k),
        repetition_penalty=float(repetition_penalty),
        reasoning=reasoning,
        auto_continue=auto_continue,
        device="cuda" if torch.cuda.is_available() else "cpu",
    )
    report = HRMInferencePipeline(settings).execute()
    completion = report.output
    if completion.startswith(prompt):
        completion = completion[len(prompt):]
    stats = (
        f"\n\n---\n"
        f"Tokens: {report.prompt_tokens} prompt + {report.new_tokens} new | "
        f"Time: {report.elapsed_seconds:.2f}s | "
        f"Speed: {report.tokens_per_second(1e-3):.1f} tok/s"
    )
    return completion + stats


def build_ui() -> gr.Blocks:
    """Construct the Gradio Blocks interface."""
    device_label = "GPU" if torch.cuda.is_available() else "CPU"

    with gr.Blocks(
        title=f"TopoGPT3 v{__version__} — Code Generation",
        css="""
        .main-title { text-align: center; margin-bottom: 0.5em; }
        .subtitle { text-align: center; color: #666; font-size: 0.9em; }
        """,
    ) as demo:
        gr.HTML(f"""
        <div class="main-title">
            <h1>TopoGPT3</h1>
            <p class="subtitle">
                Complex-Valued Spectral Language Model for Code
                &nbsp;|&nbsp; v{__version__} &nbsp;|&nbsp; Device: {device_label}
            </p>
        </div>
        """)

        with gr.Tabs():
            # ---- Tab 1: Standard Inference ----
            with gr.Tab("Standard Inference", id="standard"):
                with gr.Row():
                    with gr.Column(scale=3):
                        prompt_std = gr.Textbox(
                            label="Prompt",
                            placeholder="def fibonacci(n):\n",
                            lines=4,
                            value="def fibonacci(n):\n",
                        )
                    with gr.Column(scale=1):
                        max_new_std = gr.Slider(
                            minimum=1, maximum=2048, value=256, step=1,
                            label="Max New Tokens",
                        )
                        temp_std = gr.Slider(
                            minimum=0.01, maximum=2.0, value=0.3, step=0.01,
                            label="Temperature",
                        )
                        top_k_std = gr.Slider(
                            minimum=0, maximum=200, value=50, step=1,
                            label="Top-K",
                        )
                        rep_pen_std = gr.Slider(
                            minimum=0.5, maximum=3.0, value=1.1, step=0.05,
                            label="Repetition Penalty",
                        )
                        auto_cont_std = gr.Checkbox(
                            label="Auto-continue", value=False,
                        )

                run_std = gr.Button("Generate", variant="primary")
                output_std = gr.Textbox(
                    label="Generated Code", lines=16,
                )

                run_std.click(
                    fn=run_standard_inference,
                    inputs=[
                        prompt_std, max_new_std, temp_std,
                        top_k_std, rep_pen_std, auto_cont_std,
                    ],
                    outputs=output_std,
                )

            # ---- Tab 2: HRM Inference ----
            with gr.Tab("HRM (Hierarchical Recursive Reasoning)", id="hrm"):
                gr.Markdown(
                    "The HRM sampler reuses the same checkpoint with **no extra "
                    "trained parameters**. It performs iterative latent refinement "
                    "via a high-level slow loop and a low-level fast loop."
                )
                with gr.Row():
                    with gr.Column(scale=3):
                        prompt_hrm = gr.Textbox(
                            label="Prompt",
                            placeholder="def fibonacci(n):\n",
                            lines=4,
                            value="def fibonacci(n):\n",
                        )
                    with gr.Column(scale=1):
                        max_new_hrm = gr.Slider(
                            minimum=1, maximum=2048, value=256, step=1,
                            label="Max New Tokens",
                        )
                        temp_hrm = gr.Slider(
                            minimum=0.01, maximum=2.0, value=0.3, step=0.01,
                            label="Temperature",
                        )
                        top_k_hrm = gr.Slider(
                            minimum=0, maximum=200, value=50, step=1,
                            label="Top-K",
                        )
                        rep_pen_hrm = gr.Slider(
                            minimum=0.5, maximum=3.0, value=1.1, step=0.05,
                            label="Repetition Penalty",
                        )
                        h_iters = gr.Slider(
                            minimum=1, maximum=8, value=2, step=1,
                            label="High-Level Iterations",
                        )
                        l_iters = gr.Slider(
                            minimum=1, maximum=12, value=3, step=1,
                            label="Low-Level Iterations",
                        )
                        l_window = gr.Slider(
                            minimum=1, maximum=6, value=2, step=1,
                            label="Low-Level Window",
                        )
                        thinking = gr.Checkbox(
                            label="Thinking Mode (deeper reasoning)",
                            value=False,
                        )
                        auto_cont_hrm = gr.Checkbox(
                            label="Auto-continue", value=False,
                        )

                run_hrm = gr.Button("Generate (HRM)", variant="primary")
                output_hrm = gr.Textbox(
                    label="Generated Code", lines=16,
                )

                run_hrm.click(
                    fn=run_hrm_inference,
                    inputs=[
                        prompt_hrm, max_new_hrm, temp_hrm,
                        top_k_hrm, rep_pen_hrm, h_iters, l_iters,
                        l_window, thinking, auto_cont_hrm,
                    ],
                    outputs=output_hrm,
                )

            # ---- Tab 3: Examples ----
            with gr.Tab("Examples"):
                gr.Markdown("### Quick prompts to try")
                gr.Markdown("""
| Prompt | Max Tokens | Temp | Top-K | Rep Pen | Auto-Cont |
|--------|-----------|------|-------|---------|-----------|
| `def fibonacci(n):\n    ` | 256 | 0.3 | 50 | 1.1 | No |
| `def binary_search(arr, target):\n    ` | 300 | 0.3 | 50 | 1.1 | No |
| `class Node:\n    def __init__(self, val):\n        ` | 200 | 0.2 | 50 | 1.1 | No |
| `def quicksort(arr):\n    if len(arr) <= 1:\n        return arr\n    pivot = arr[0]\n    ` | 400 | 0.4 | 50 | 1.1 | Yes |
| `import os\n\ndef list_files(path):\n    ` | 200 | 0.3 | 50 | 1.1 | No |
| `# Conway's Game of Life\nimport numpy as np\n\n` | 512 | 0.3 | 50 | 1.1 | Yes |
                """)
                gr.Markdown(
                    "Copy any prompt into the Standard or HRM tab and click Generate."
                )

            # ---- Tab 4: About ----
            with gr.Tab("About"):
                gr.Markdown(f"""
                ## TopoGPT3 v{__version__}

                A **24.5M parameter** complex-valued autoregressive language model
                for code, instrumented with spectral and geometric diagnostics
                over training dynamics.

                ### Architecture
                - Autoregressive transformer with complex-valued spectral operators
                - Quaternion-inspired layers for parameter efficiency
                - Gauss-style complex multiplication (3 real muls per contraction)
                - Sliding window attention with configurable window size
                - Latent memory tokens for context compression
                - Mixture of Experts (MoE) with SwiGLU routing

                ### Inference Modes
                1. **Standard**: Top-k sampling with repetition penalty
                2. **HRM**: Hierarchical recursive reasoning with no extra parameters

                ### Links
                - [GitHub](https://github.com/grisuno/TopoGPT3)
                - [HuggingFace Checkpoint](https://huggingface.co/grisiscomeback/TopoGPT3)
                - [Paper](https://doi.org/10.5281/zenodo.20388757)

                ### License
                AGPL v3
                """)

    return demo


if __name__ == "__main__":
    ensure_checkpoint()
    demo = build_ui()
    demo.launch(server_name="0.0.0.0", server_port=7860)
