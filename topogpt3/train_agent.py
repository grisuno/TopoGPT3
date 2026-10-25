"""Agentic RL for TopoGPT3 (multi-turn Tool-Use).

Rollout: prompt -> generate -> parse <tool_call> -> execute (run_python
sandbox + mock tools) -> append <tool_response> -> repeat (max_turns=3).
Reward: tool use + completion - repetition.
Loss: same GRPO/CISPO as train_grpo (no Critic -> quaternion-safe).
Observations (tool outputs) are masked out of the policy loss.
"""

from __future__ import annotations

import argparse
import copy
import os
import sys

import torch
import torch.nn.functional as F
from torch import optim
from torch.utils.data import DataLoader

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from safetensors.torch import load_file

from topogpt3.chat import apply_chat_template, parse_tool_calls
from topogpt3.checkpoint_meta import config_from_checkpoint
from topogpt3.datasets_chat import AgentRLDatasetJSONL
from topogpt3.model import BPETokenizer, TopoGPT2, TopoGPT2Config
from topogpt3.rewards import (
    execution_reward,
    grpo_advantages,
    grpo_loss,
    rep_penalty,
    tool_call_reward,
    verifier_reward,
)
from topogpt3.tools_agent import TOOLS, execute_tool
from topogpt3.trainer_utils_topo import Logger, is_main_process, setup_seed


def agent_reward(
    text: str,
    gt: str,
    used_tools: bool,
    tool_results: list | None = None,
    allowed_tools: set | None = None,
    require_tool: bool = False,
    verifier: str = "general",
) -> float:
    """Format + ground-truth + valid tool calls + sandboxed execution."""
    r = 0.0
    if used_tools:
        r += 0.5
    if gt and gt in text:
        r += 2.5 * (len(gt) / max(len(text), 1))
    if "</think>" in text:
        r += 0.5
    r -= rep_penalty(text)
    r += tool_call_reward(text, allowed_tools, require_tool)
    if verifier != "general":
        r += verifier_reward(text, verifier)
    if tool_results:
        r += execution_reward(tool_results)
    return max(min(r, 6.0), -6.0)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default="data/agent_rl.jsonl")
    ap.add_argument("--checkpoint", default="checkpoints_topogpt3/last")
    ap.add_argument("--out", default="out/topo_agent.pt")
    ap.add_argument("--epochs", type=int, default=1)
    ap.add_argument("--batch-size", type=int, default=2)
    ap.add_argument("--lr", type=float, default=3e-7)
    ap.add_argument("--num-generations", type=int, default=2)
    ap.add_argument("--max-gen-len", type=int, default=256)
    ap.add_argument("--max-len", type=int, default=768)
    ap.add_argument("--max-turns", type=int, default=3)
    ap.add_argument("--beta", type=float, default=0.1)
    ap.add_argument("--loss-type", default="cispo", choices=["grpo", "cispo"])
    ap.add_argument("--device", default="cuda" if torch.cuda.is_available() else "cpu")
    ap.add_argument(
        "--allowed-tools",
        default="apt_chain,run_python,calculate_math,run_command,read_facts",
    )
    ap.add_argument(
        "--verifier", default="general", choices=["general", "code", "json"]
    )
    args = ap.parse_args()
    setup_seed(1337)
    device = args.device
    tok = BPETokenizer()
    try:
        cfg, _meta = config_from_checkpoint(args.checkpoint, device="cpu")
    except FileNotFoundError:
        cfg = TopoGPT2Config()
    model = TopoGPT2(cfg)
    sf = os.path.join(args.checkpoint, "model.safetensors")
    if os.path.exists(sf):
        model.load_state_dict(load_file(sf, device="cpu"), strict=False)
    model = model.to(device)
    ref = copy.deepcopy(model).eval()
    for p in ref.parameters():
        p.requires_grad = False
    opt = optim.AdamW(model.parameters(), lr=args.lr)
    ds = AgentRLDatasetJSONL(args.data, tok, max_length=args.max_len)
    loader = DataLoader(
        ds, batch_size=args.batch_size, shuffle=True, collate_fn=lambda b: b
    )
    step = 0
    model.train()
    for ep in range(args.epochs):
        for batch in loader:
            step += 1
            # expand generations
            outs, rewards = [], []
            for item in batch:
                for _ in range(args.num_generations):
                    hist = [dict(m) for m in item["messages"]]
                    full = ""
                    turn_results: list = []
                    for _t in range(args.max_turns):
                        prompt = apply_chat_template(
                            hist,
                            tools=item.get("tools") or TOOLS,
                            add_generation_prompt=True,
                        )
                        ids = torch.tensor(
                            [tok.encode(prompt)[-args.max_len :]],
                            dtype=torch.long,
                            device=device,
                        )
                        with torch.no_grad():
                            gen = model.generate(
                                ids, max_new_tokens=args.max_gen_len, temperature=0.8
                            )
                        text = tok.decode(gen[0, ids.size(1) :].tolist())
                        full += text
                        calls = parse_tool_calls(text)
                        hist.append({"role": "assistant", "content": text})
                        if not calls:
                            break
                        import json as _j

                        for c in calls:
                            cargs = c.get("arguments", {})
                            if isinstance(cargs, str):
                                try:
                                    cargs = _j.loads(cargs)
                                except Exception:
                                    cargs = {}
                            res = execute_tool(c.get("name", ""), cargs)
                            if res is not None:
                                turn_results.append(res)
                            hist.append(
                                {"role": "tool", "content": _j.dumps(res or {})}
                            )
                    outs.append(full)
                    rewards.append(
                        agent_reward(
                            full,
                            item.get("gt", ""),
                            used_tools=("<tool_call>" in full),
                            tool_results=turn_results,
                            allowed_tools=set(args.allowed_tools.split(",")),
                            require_tool=bool(item.get("require_tool", False)),
                            verifier=args.verifier,
                        )
                    )
            # policy update on concatenated prompt+response (observations masked
            # implicitly: we train only on final full text ids here, compact form)
            R = torch.tensor(rewards, device=device)
            adv = grpo_advantages(R, args.num_generations).to(device)
            # tokenize full outputs for loss
            enc = [tok.encode(o)[: args.max_gen_len] for o in outs]
            L = max(len(x) for x in enc)
            out_ids = torch.tensor([x + [0] * (L - len(x)) for x in enc], device=device)
            mask = (out_ids != 0).float()
            logits, aux, _ = model(
                torch.cat(
                    [
                        torch.zeros(
                            out_ids.size(0), 1, dtype=torch.long, device=device
                        ),
                        out_ids,
                    ],
                    dim=1,
                )[:, :-1]
            )
            with torch.no_grad():
                rl, _, _ = ref(
                    torch.cat(
                        [
                            torch.zeros(
                                out_ids.size(0), 1, dtype=torch.long, device=device
                            ),
                            out_ids,
                        ],
                        dim=1,
                    )[:, :-1]
                )
            new_lp = (
                F.log_softmax(logits, -1).gather(2, out_ids.unsqueeze(-1)).squeeze(-1)
            )
            ref_lp = F.log_softmax(rl, -1).gather(2, out_ids.unsqueeze(-1)).squeeze(-1)
            old_lp = new_lp.detach()
            loss = grpo_loss(
                new_lp,
                old_lp,
                ref_lp,
                adv,
                mask,
                beta=args.beta,
                loss_type=args.loss_type,
            )
            loss = loss + 0.01 * aux
            opt.zero_grad()
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            opt.step()
            if step % 5 == 0:
                Logger(
                    f"ep{ep} step{step} agent_reward={R.mean().item():.3f} "
                    f"loss={loss.item():.4f}"
                )
    if is_main_process():
        os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)
        torch.save({k: v.half().cpu() for k, v in model.state_dict().items()}, args.out)
        Logger(f"saved Agent-RL -> {args.out}")


if __name__ == "__main__":
    main()
