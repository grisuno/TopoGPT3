# `topogpt3`

> Source: [topogpt3/__init__.py:1](../../topogpt3/__init__.py#L1) | language `py` | coverage 100.0% | [API index](../index.md)

TopoGPT3: complex-valued spectral language model for code.

This package bundles:

- `[`topogpt3.model`](topogpt3.model.py.md)`: the base TopoGPT2 architecture (quaternion spectral
  layers, BPE tokenizer, helpers).
- `[`topogpt3.train`](topogpt3.train.py.md)`: the curriculum trainer with Grassmannian / Fisher /
  phase diagnostics.
- `[`topogpt3.inference`](topogpt3.inference.py.md)`: a standard autoregressive sampler that loads a
  trained safetensors checkpoint.
- `[`topogpt3.inference_hrm`](topogpt3.inference_hrm.py.md)`: a hierarchical recursive reasoning sampler
  that reuses the same checkpoint with no extra trained parameters.
- `[`topogpt3.lens_model`](topogpt3.lens_model.py.md)`: the Jacobian-lens model adapter (LensModel
  protocol + TopoGPT3LensModel wrapper).
- `[`topogpt3.jlens`](topogpt3.jlens.py.md)`: Jacobian lens fitting, application, and the
  ActivationRecorder / JacobianLens infrastructure.

Typical usage from a downstream project::

    from topogpt3 import InferenceSettings, InferencePipeline

    settings = InferenceSettings(
        checkpoint_dir="checkpoints_topogpt3",
        prompt="def fibonacci(",
        max_new_tokens=200,
    )
    InferencePipeline(settings).execute()

Jacobian lens usage::

    from topogpt3.lens_model import TopoGPT3LensModel
    from topogpt3.jlens import fit, JacobianLens

    model = TopoGPT3LensModel.from_checkpoint("checkpoints_topogpt3/last")
    lens = fit(model, prompts, source_layers=[0, 1, 2, 3, 4])
    lens_logits, model_logits, input_ids = lens.apply(model, "def hello(")
