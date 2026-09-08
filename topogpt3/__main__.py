from __future__ import annotations

import sys


def main() -> None:
    """TopoGPT3 entry point. Delegates to subcommands."""
    if len(sys.argv) < 2:
        print(
            "TopoGPT3: complex-valued spectral language model\n"
            "\n"
            "Usage:\n"
            "  python3 -m topogpt3              this help\n"
            "  python3 -m topogpt3 infer         standard autoregressive inference\n"
            "  python3 -m topogpt3 infer-hrm     HRM recursive reasoning inference\n"
            "  python3 -m topogpt3 train         curriculum training\n"
            "  python3 -m topogpt3 api           start API server\n"
            "  python3 -m topogpt3 lens          test model loading\n"
            "  python3 -m topogpt3 jlens         Jacobian lens demo\n"
            "  python3 -m topogpt3 check         quick checkpoint validation\n"
            "  python3 -m topogpt3 train-lora      SFT with native LoRA adapters\n"
            "  python3 -m topogpt3 train-dpo       preference alignment (DPO)\n"
            "  python3 -m topogpt3 train-grpo      RLAIF (GRPO/CISPO, no critic)\n"
            "  python3 -m topogpt3 train-ppo       RLAIF (PPO + value head)\n"
            "  python3 -m topogpt3 train-distill   white-box distillation\n"
            "  python3 -m topogpt3 train-agent     agentic RL (multi-turn tools)\n"
            "  python3 -m topogpt3 convert         merge LoRA / export stubs\n"
            "  python3 -m topogpt3 export-chat     curriculum HF -> chat JSONL\n"
        )
        return
    subcommand = sys.argv[1]
    sys.argv = sys.argv[1:]
    if subcommand in ("jlens", "lens"):
        from .jlens import _demo_jlens
        _demo_jlens()
    elif subcommand == "check":
        from .lens_model import TopoGPT3LensModel
        m = TopoGPT3LensModel.from_checkpoint("checkpoints_topogpt3/last")
        print(f"OK: n_layers={m.n_layers}, d_model={m.d_model}")
    elif subcommand in ("api", "api_server"):
        from .api_server import main as api_main
        api_main()
    elif subcommand in ("infer", "inference"):
        from .inference import main as infer_main
        infer_main()
    elif subcommand in ("infer-hrm", "inference-hrm"):
        from .inference_hrm import main as hrm_main
        hrm_main()
    elif subcommand == "train":
        from .train import main as train_main
        train_main()
    elif subcommand == "train-lora":
        from .train_lora import main as m
        m()
    elif subcommand == "train-dpo":
        from .train_dpo import main as m
        m()
    elif subcommand == "train-grpo":
        from .train_grpo import main as m
        m()
    elif subcommand == "train-ppo":
        from .train_ppo import main as m
        m()
    elif subcommand == "train-distill":
        from .train_distill import main as m
        m()
    elif subcommand == "train-agent":
        from .train_agent import main as m
        m()
    elif subcommand == "convert":
        from .convert import main as m
        m()
    elif subcommand == "export-chat":
        from .export_chat import main as m
        m()
    else:
        print(f"Unknown subcommand: {subcommand}")


if __name__ == "__main__":
    main()
