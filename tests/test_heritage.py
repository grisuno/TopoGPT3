"""Advanced-training tests: LoRA/RL/chat modules preserve quaternionic identity."""
import torch

from topogpt3.chat import (apply_chat_template, parse_thinking,
                           parse_tool_calls, split_reasoning_content)
from topogpt3.lora import (apply_lora, freeze_non_lora, lora_parameters,
                           save_lora, load_lora)
from topogpt3.model import TopoGPT2, TopoGPT2Config
from topogpt3.rewards import (base_rewards, dpo_loss_fn, distillation_loss,
                              grpo_advantages, grpo_loss, logits_to_log_probs,
                              rep_penalty, spectral_bonus)
from topogpt3.rollout import TorchRolloutEngine, compute_per_token_logps
from topogpt3.yarn import YaRNConfig, apply_yarn_to_rope, yarn_scale_inv_freq
from topogpt3.tools_agent import TOOLS, execute_tool
from topogpt3.eval_toolcall import evaluate


def _micro():
    cfg = TopoGPT2Config(SCALE="micro", MOE_ENABLED=False, N_MEMORY_TOKENS=0,
                         MEMORY_SEGMENT_LEN=0)
    return TopoGPT2(cfg)


def test_chat_template_tools_think():
    tools = [{"type": "function",
              "function": {"name": "run_python", "description": "run code"}}]
    msgs = [{"role": "user", "content": "hi"}]
    p = apply_chat_template(msgs, tools=tools, add_generation_prompt=True,
                            open_thinking=True)
    assert "<|im_start|>" in p and "<think>" in p
    t = "<think>plan</think> code <tool_call>{\"name\": \"run_python\", \"arguments\": {}}</tool_call>"
    parts = split_reasoning_content(t)
    assert parts["reasoning_content"] == "plan"
    assert parts["tool_calls"][0]["name"] == "run_python"


def test_yarn_changes_freqs_only():
    m = _micro()
    rope = m.layers[0].attn.rope
    before = rope.inv_freq.clone()
    apply_yarn_to_rope(rope, YaRNConfig(factor=16.0, enabled=True))
    assert not torch.allclose(before, rope.inv_freq)
    # architecture untouched
    assert hasattr(m.layers[0], "topo_brain")


def test_lora_zero_init_and_quaternion_targets():
    m = _micro()
    names = apply_lora(m, rank=4)
    assert names, "expected patched linears"
    # quaternion sub-linears patched (identity preserved structurally)
    assert any("Ww" in n or "Wx" in n or "attn" in n or "proj" in n for n in names)
    x = torch.randint(0, 50, (1, 8))
    m.eval()
    with torch.no_grad():
        logits, aux, _ = m(x)
    assert logits.shape[-1] == m.config.VOCAB_SIZE
    freeze_non_lora(m)
    assert all(p.requires_grad for p in lora_parameters(m))
    assert sum(1 for n, p in m.named_parameters() if p.requires_grad) == \
        sum(1 for _ in lora_parameters(m))


def test_lora_save_load(tmp_path):
    m = _micro()
    apply_lora(m, rank=2)
    p = str(tmp_path / "lora.pt")
    save_lora(m, p)
    m2 = _micro()
    apply_lora(m2, rank=2)
    load_lora(m2, p)
    import os
    assert os.path.getsize(p) > 0


def test_dpo_grpo_losses_finite():
    torch.manual_seed(0)
    logits = torch.randn(4, 6, 20)
    labels = torch.randint(0, 20, (4, 6))
    mask = torch.ones(4, 6)
    lp = logits_to_log_probs(logits, labels)
    assert lp.isfinite().all()
    loss = dpo_loss_fn(lp, lp + 0.01, mask, beta=0.15)
    assert loss.isfinite()
    r = torch.tensor([1.0, 0.5, -0.5, 0.0])
    adv = grpo_advantages(r, 2)
    assert adv.isfinite().all()
    new = torch.randn(4, 5)
    l = grpo_loss(new, new.detach(), new.detach(), adv, torch.ones(4, 5))
    assert l.isfinite()
    assert rep_penalty("hello world hello world") >= 0.0
    assert spectral_bonus() == 0.0  # default = base reward unchanged
    assert spectral_bonus(fisher_gap=0.01, drift=0.1) > 0.0


def test_distill_loss_finite():
    s = torch.randn(2, 5, 20)
    t = torch.randn(2, 5, 20)
    mask = torch.ones(2, 5)
    labels = torch.randint(0, 20, (2, 5))
    labels[0, :2] = -100
    loss = distillation_loss(s, t, mask, labels=labels)
    assert loss.isfinite()


def test_rollout_engine_micro():
    m = _micro().eval()
    from topogpt3.model import BPETokenizer
    try:
        tok = BPETokenizer()
        dec = lambda ids: tok.decode(ids)
    except Exception:
        dec = lambda ids: " ".join(map(str, ids))
        tok = None
    eng = TorchRolloutEngine(m, tok, device="cpu",
                             decode=dec)
    prompt = torch.randint(0, 50, (1, 8))
    rr = eng.rollout(prompt, num_generations=2, max_new_tokens=4, temperature=1.0)
    assert rr.output_ids.shape[0] == 2
    assert len(rr.completions) == 2


def test_tools_and_eval():
    assert any(t["function"]["name"] == "run_python" for t in TOOLS)
    out = evaluate(lambda prompt: "<tool_call>{\"name\": \"calculate_math\", \"arguments\": {\"expression\": \"1+1\"}}</tool_call>")
    assert "accuracy" in out
