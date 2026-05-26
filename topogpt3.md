# TopoGPT3: Exploring Complex-Valued Representations in Small Code Models

## Abstract

In this work I trained a 24.5 million parameter autoregressive language model using complex-valued spectral operators and monitored its training dynamics with several additional diagnostics. The goal was to test whether complex representations could help a small model learn structured code more efficiently.

The model was trained on a curriculum of code datasets. During training I tracked dominant singular values, phase alignment between kernels, accumulated angular drift, and separation in the empirical Fisher spectrum. The results show that the model reached reasonable validation performance while exhibiting stable low-rank structure and coherent phase evolution in its dominant kernels.

I do not claim any deep theoretical breakthrough. These measurements simply provide a clearer picture of how optimization proceeds in this architecture beyond scalar loss. The findings suggest that complex-valued spectral layers deserve further study for compact code models.

## 1. Introduction

Most work on code generation focuses on scaling model size. I took a different approach: I wanted to see if better representations could allow a much smaller model to learn meaningful programming patterns.

Programming languages have strong internal structure — recursion, composition, scope rules, and repeated motifs. I suspected this structure might be captured more efficiently with complex-valued parameters that naturally encode phase relationships.

To explore this I built TopoGPT3, a 24.5M parameter model that uses complex spectral operators. During training I added instrumentation to observe how the dominant learned kernels evolve. This paper reports what I actually measured.

## 2. Model and Training Setup

TopoGPT3 is an autoregressive transformer with complex-valued spectral layers and quaternion-inspired elements for parameter efficiency. I implemented a practical Gauss-style optimization for complex multiplication that reduces the operation to three real multiplications per contraction.

The model was trained on a four-tier curriculum: CodeAlpaca, Code Feedback, Magicoder Evol, and a small Python subset from The Stack. Training used mixed precision on a single GPU. I saved checkpoints regularly and logged both standard metrics and the additional diagnostics described below.

## 3. Optimization Measurements

Instead of looking only at loss and accuracy, I tracked the behavior of the dominant spectral kernels.

At regular intervals I extracted the kernel tensor, performed truncated SVD to obtain the leading 16 modes, and normalized them. For these normalized dominant kernels $\tilde{K}_t$ at consecutive steps I computed:

- Accumulated phase:
  $$
  \gamma = \sum_t \arg \langle \tilde{K}_t | \tilde{K}_{t+1} \rangle
  $$

- Net angular drift:
  $$
  W = \frac{1}{2\pi} \sum_t \Delta\arg \langle \tilde{K}_t | \tilde{K}_{t+1} \rangle
  $$

I also estimated the separation in the empirical Fisher spectrum:
$$
\Delta_F = \lambda_r - \lambda_{r+1}
$$
where $r=16$ corresponds to the dominant subspace.

During the first tier (CodeAlpaca), the dominant singular values remained quite stable, evolving only slightly between approximately 2.34 and 2.40. The Fisher gap $\Delta_F$ became consistently positive, ranging from $7.87 \times 10^{-4}$ to $1.54 \times 10^{-3}$. The phase $\gamma$ showed coherent swings of several radians, and the net drift $W$ reached values up to +0.55 and -0.49.

These measurements indicate that while the model was learning, the dominant kernels were not simply increasing in magnitude. Their evolution also exhibited persistent directional structure in phase space.

Across long optimization intervals, the angular drift statistics remained bounded and showed coherent accumulation rather than behaving like unconstrained random fluctuations. The trajectories repeatedly returned toward a limited range while preserving directional persistence over thousands of optimization steps.

I do not interpret this behavior as evidence of formal topological invariants. I treat it only as an empirical indication that the dominant functional subspace evolves in a structured and partially correlated manner during training.

## 4. Experimental Results

After two epochs on CodeAlpaca the model achieved:

- Training loss: 2.168
- Training accuracy: 60.08%
- Validation loss: 2.199
- Validation accuracy: 60.12%
- Validation perplexity: 9.02
- Holdout perplexity: 9.07

At the end of this tier the optimization measurements showed:

- Dominant subspace rank remained stable at $r=16$
- Leading singular values: approximately [2.383, 2.246]
- Fisher gap $\Delta_F$: $1.347 \times 10^{-3}$
- Maximum observed $|W|$: around 0.55

The combination of stable low-rank structure, positive spectral separation, and non-trivial phase drift suggests that the complex spectral layers allowed the model to organize its representations in a more structured way than I would have expected from the parameter count alone. The model reached decent code modeling performance with modest compute while maintaining stable internal organization throughout training.

## 5. Interpretation

The most useful outcome of this experiment is practical. A 24.5M parameter model can learn basic code structure while showing clear low-rank organization and coherent phase evolution in its kernels.

I do not interpret the phase drift or winding numbers as formal topological invariants. They are simply diagnostics that reveal directional consistency in how the dominant representations evolve.
One unexpected observation was that the accumulated angular drift statistics appeared to organize around a relatively stable distribution during extended training intervals. The trajectories did not resemble pure random walks in phase space. Instead they exhibited bounded fluctuations with recurring directional persistence while the optimization remained stable.

This behavior may simply reflect correlated movement inside a constrained low-rank optimization manifold rather than any deeper geometric phenomenon. Even so, the measurements were useful because they exposed structure that was not visible from scalar loss alone.

The positive Fisher gap indicates that a relatively stable functional subspace emerges during training.

These observations suggest that complex-valued spectral operators may offer a more efficient way to encode the structured patterns present in source code. The results do not prove superiority over real-valued baselines of similar size — that comparison remains to be done carefully — but they justify continued exploration of this direction.

### 5.1 Emergent Geometric Transport

Beyond scalar optimization metrics, the dominant kernel subspace exhibited persistent directional transport throughout training.

While instantaneous phase measurements fluctuated in both directions, the accumulated winding statistic W showed a sustained positive drift across optimization steps. This behavior suggests that the dominant spectral subspace evolves coherently along a preferred trajectory on the underlying Grassmannian manifold.

Importantly, this transport persisted even after language modeling loss had largely plateaued. The observation indicates that internal geometric organization continues beyond immediate improvements in predictive performance.

We do not interpret the winding statistic as a strict topological invariant. Rather, it functions as a diagnostic for accumulated geometric transport and directional consistency in representation evolution.

The coexistence of:

- stable dominant rank,
- positive Fisher spectral separation,
- bounded singular value growth,
- and persistent winding accumulation

suggests that optimization in the complex-valued model may proceed through structured low-dimensional flows rather than purely stochastic parameter diffusion.

## 5.2 Inference-Time Hierarchical Reasoning Dynamics

To explore whether additional iterative reasoning improves generation quality in the small complex-valued model, I implemented an inference-time hierarchical refinement mechanism (HRM) that performs repeated low-level and high-level latent updates during autoregressive decoding.

The mechanism introduces no new trainable parameters. Instead, it reuses the existing network activations through recurrent latent refinement passes:

- low-level refinement iterations: $L$
- high-level reasoning iterations: $H$
- short latent persistence window
- cached hidden-state reuse across decoding steps

For the experiment shown here I used:

- $L = 3$
- $H = 2$
- persistence window = 4
- local reasoning window = 2

The purpose was to test whether additional internal iterative transport on the learned representation manifold could improve coherence or algorithmic structure during generation.

### Baseline Decoding

Using standard autoregressive sampling on the prompt:

    #include <stdio.h>

the model generated a partially coherent continuation involving prime-number summation logic. The output demonstrated:

- valid local syntax,
- preservation of code formatting,
- semantically related procedural structure,
- but inconsistent function semantics and incomplete correctness.

Generation speed was approximately:

- 7.7 tokens/s

with:

- 200 generated tokens in 25.9 seconds.

### HRM-Enhanced Decoding

I then enabled hierarchical refinement during inference while keeping the underlying trained weights unchanged.

The resulting generation remained qualitatively similar to the baseline output. Local coherence and formatting were preserved, but algorithmic correctness did not substantially improve at the current training stage.

The refined decoding produced:

- 234 tokens in 111 seconds,
- approximately 2.1 tokens/s.

The runtime diagnostics reported:

- average high-level iterations: 1.19
- average low-level iterations: 5.65
- high-level convergence events: 0
- safety halts: 228
- hidden-state cache reuses: 234

These measurements suggest that the latent refinement dynamics were active, but the learned representation manifold had not yet developed sufficiently strong internal structure for iterative reasoning to yield large qualitative gains.

Importantly, inference-time refinement did not destabilize decoding. The generations remained syntactically continuous and semantically related to the prompt despite repeated latent transport operations.

### Interpretation

At the current stage of training, HRM appears to function primarily as a latent consistency refinement process rather than a source of emergent reasoning capability.

The absence of high-level convergence events indicates that the iterative dynamics rarely settled into stable attractor states during decoding. Instead, the refinement process continued operating near the safety limits imposed by the controller.

This behavior is consistent with the training diagnostics observed simultaneously:

- language modeling loss had largely plateaued,
- Fisher spectral separation remained positive,
- dominant singular modes stayed stable,
- and winding accumulation continued increasing gradually.

Together, these observations suggest that the model already possesses structured low-rank internal organization, but its representations may still lack the depth required for effective iterative reasoning.

One plausible interpretation is that HRM becomes more useful only after the dominant representation manifold acquires stronger algorithmic abstractions during later curriculum stages.

Another possibility is that the refinement dynamics themselves require explicit training objectives rather than purely inference-time application.

At minimum, these experiments show that:

- iterative latent transport can be layered on top of a compact complex-valued transformer without retraining,
- the internal dynamics remain numerically stable,
- and the additional instrumentation exposes reasoning-time behavior beyond token probabilities alone.

Although the qualitative gains were limited in this early experiment, the approach provides a useful framework for studying geometric refinement dynamics during inference in compact language models.

## 6. Limitations

This is a small-scale exploratory study. The model is only 24.5M parameters and was trained on a limited curriculum. Many effects observed here may depend on specific implementation details, initialization, or optimizer choices.

The phase and angular drift measurements are useful diagnostics but not rigorous mathematical invariants. Larger ablations, real-valued controls, and broader benchmarks are still needed before drawing stronger conclusions.

Early generations demonstrated syntactic continuity and local semantic consistency, although algorithmic correctness remained limited at this scale and training duration

## 7. Conclusion

I built and trained a small complex-valued language model for code and instrumented its training with phase and spectral measurements. The model achieved reasonable performance while exhibiting stable low-rank structure and coherent phase dynamics.

The main takeaway is modest but encouraging: complex spectral representations appear promising for building more efficient code models at small scale. The additional diagnostics helped me see structure in the optimization process that would have been invisible using loss alone.

I plan to continue refining the instrumentation and running more controlled comparisons.

grisun0  
May 2026
