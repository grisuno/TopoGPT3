# Essential Concepts

Core ideas behind TopoGPT3, explained in plain language.

Project URL: [https://github.com/grisuno/TopoGPT3](https://github.com/grisuno/TopoGPT3)

---

## 1. Complex-Valued Spectral Operators

Standard neural networks use real numbers for weights. TopoGPT3 uses complex numbers, which have both a magnitude and a phase (angle).

**Why complex numbers?**

Source code has strong internal structure: recursion, nesting, scope rules, and repeated patterns. Complex numbers naturally encode relationships through phase, which may capture these structural patterns more compactly than real-valued weights.

**Practical implementation:**

Instead of four real multiplications per complex multiplication, TopoGPT3 uses a Gauss-style optimization that reduces this to three real multiplications, making the approach computationally practical.

## 2. Quaternion-Inspired Layers

Quaternions are a number system that extends complex numbers. TopoGPT3 borrows ideas from quaternion algebra to build layers that are more parameter-efficient than standard real-valued layers of the same capacity.

The result is a transformer that packs more representational structure into fewer parameters.

## 3. Grassmannian Diagnostics

During training, TopoGPT3 does more than track loss and accuracy. It periodically inspects the dominant learned kernels (the most important weight patterns) using truncated Singular Value Decomposition (SVD).

From this inspection, it computes:

- **Phase alignment**: How the angle of dominant kernels changes between optimization steps.
- **Angular drift (W)**: A winding-like statistic that measures accumulated directional transport in phase space.
- **Fisher spectral gap (Delta_F)**: The separation between the dominant and subdominant modes of the empirical Fisher information matrix.
- **Dominant rank (r)**: The effective dimensionality of the most important learned subspace.

These diagnostics reveal how the model's internal organization evolves, even when scalar loss has plateaued.

## 4. Hierarchical Recursive Reasoning (HRM)

HRM is an inference-time mechanism that adds iterative latent refinement without any new trained parameters.

**How it works:**

1. After the standard forward pass produces a token, HRM performs additional low-level and high-level latent updates.
2. The existing transformer layers are reused as the step function for these updates.
3. A short persistence window caches hidden states across decoding steps.
4. Halting is controlled by the empirical stabilization of the latent state.

HRM is intended to study whether iterative transport on the learned representation manifold improves generation quality.

## 5. Four-Tier Curriculum Training

Training proceeds through a curriculum that gradually increases complexity:

1. **CodeAlpaca**: Short, simple code instructions.
2. **Code Feedback (filtered)**: Refined instruction-following examples.
3. **Magicoder Evol Instruct**: More complex and evolved instructions.
4. **Tiny subset of The Stack**: Real multilingual code from public repositories.

Each tier has disjoint train, validation, and holdout splits. The holdout is never seen during training and is used to measure true generalization.

## 6. Checkpoint Compatibility

The model is always built with the maximum sequence length across all tiers. This means positional embeddings have a fixed shape, and checkpoints can be restarted from any tier without shape mismatches.

Checkpoints are saved as:

- `model.safetensors`: model weights
- `optimizer.pt`: optimizer state
- `state.json`: training state (tier, step, metrics)

## 7. Parameter Count and Scale

The default `small` scale has approximately 24.5 million parameters. This is tiny compared to modern code models (which often have billions), but it is intentional. The research question is whether better representations can compensate for smaller scale.

Available scales:

- `micro`: smallest, for CPU testing
- `small`: default (~24.5M), balanced for single-GPU training
- `medium`: larger, for more capacity
- `gpt2`: matches GPT-2 dimensions as a reference

## 8. BPE Tokenizer

TopoGPT3 uses `tiktoken` for Byte Pair Encoding tokenization. This provides compatibility with modern tokenization standards and efficient vocabulary handling.

## Key Takeaway

TopoGPT3 is a research vehicle for asking: "If we use complex-valued spectral representations and study their geometric evolution, can a tiny model learn code structure more efficiently than its real-valued counterpart?" The diagnostics are the main contribution; the model itself is an experimental platform.

---

**License**: GPL v3 | **Author**: grisun0
