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
    else:
        print(f"Unknown subcommand: {subcommand}")


if __name__ == "__main__":
    main()
