"""Chat template + special tokens for TopoGPT3.

Identity preserved: TopoGPT3 keeps its tiktoken GPT-2 BPE tokenizer.
These helpers work at the *string* level, so no vocab retraining is needed.
`<tool_call>`, `<tool_response>`, `<think>` and `<|bufferN|>` are plain text
markers that the existing BPE encodes as ordinary subwords; the SFT mask,
the API parser and the agent rollout understand them structurally.
"""
from __future__ import annotations

import json
import random
import re
from typing import Any, Dict, List, Optional

BOS = "<|im_start|>"
EOS = "<|im_end|>"
THINK_OPEN = "<think>"
THINK_CLOSE = "</think>"
TOOL_CALL_OPEN = "<tool_call>"
TOOL_CALL_CLOSE = "</tool_call>"
TOOL_RESPONSE_OPEN = "<tool_response>"
TOOL_RESPONSE_CLOSE = "</tool_response>"

# Reserved buffer tokens for future extensions (HRM / spectral warnings).
BUFFER_TOKENS = [f"<|buffer{i}|>" for i in range(1, 9)]

# Spectral/HRM-aware buffers native to TopoGPT3 identity:
SPECTRAL_WARNING_TOKEN = "<spectral_drift_warning>"
HRM_THINK_TOKEN_OPEN = THINK_OPEN

SYSTEM_PROMPTS = [
    "You are TopoGPT3, a compact complex-valued code assistant. Provide correct, clean code.",
    "You are a knowledgeable code AI. Try your best to provide accurate programs.",
    "You are TopoGPT3, a small but geometrically-grounded coding model.",
    "Eres TopoGPT3, un asistente de código compacto y preciso.",
]

THINK_RE = re.compile(r"<think>(.*?)</think>", re.DOTALL)
TOOL_CALL_RE = re.compile(r"<tool_call>(.*?)</tool_call>", re.DOTALL)


def pre_processing_chat(conversations: List[Dict[str, Any]],
                        add_system_ratio: float = 0.2) -> List[Dict[str, Any]]:
    """Randomly prepend a system prompt (skip when tools present)."""
    if any(c.get("tools") for c in conversations):
        return conversations
    if conversations and conversations[0].get("role") != "system":
        if random.random() < add_system_ratio:
            return [{"role": "system", "content": random.choice(SYSTEM_PROMPTS)}] + conversations
    return conversations


def post_processing_chat(prompt: str, empty_think_ratio: float = 0.2) -> str:
    if "<think>\n\n</think>\n\n" in prompt and random.random() > empty_think_ratio:
        prompt = prompt.replace("<think>\n\n</think>\n\n", "")
    return prompt


def _fmt_tool_defs(tools: Optional[List[Dict[str, Any]]]) -> str:
    if not tools:
        return ""
    lines = ["# Tools", "", "You may call these tools with:"]
    lines.append(f"{TOOL_CALL_OPEN}{{\"name\": ..., \"arguments\": ...}}{TOOL_CALL_CLOSE}")
    for t in tools:
        fn = t.get("function", t) if isinstance(t, dict) else {}
        lines.append(f"- {fn.get('name')}: {fn.get('description', '')}")
    return "\n".join(lines) + "\n\n"


def apply_chat_template(messages: List[Dict[str, Any]],
                        tools: Optional[List[Dict[str, Any]]] = None,
                        add_generation_prompt: bool = False,
                        open_thinking: bool = False) -> str:
    """Render messages with tool definitions, thinking and tool-call blocks.

    Supports roles: system/user/assistant/tool + reasoning_content,
    tool_calls (list or json str), open_thinking switch.
    """
    out: List[str] = []
    sys_tools = tools
    for m in messages:
        role = m.get("role", "user")
        if role == "system" and m.get("tools"):
            sys_tools = json.loads(m["tools"]) if isinstance(m["tools"], str) else m["tools"]
            content = m.get("content", "")
            out.append(f"{BOS}system\n{content}\n{_fmt_tool_defs(sys_tools)}{EOS}\n")
        elif role == "system":
            out.append(f"{BOS}system\n{m.get('content', '')}\n{EOS}\n")
        elif role == "user":
            out.append(f"{BOS}user\n{m.get('content', '')}\n{EOS}\n")
        elif role == "assistant":
            reasoning = m.get("reasoning_content", "")
            content = m.get("content", "")
            tc = m.get("tool_calls", "")
            if isinstance(tc, (list, dict)):
                tc = json.dumps(tc)
            body = ""
            if reasoning:
                body += f"{THINK_OPEN}{reasoning}{THINK_CLOSE}\n"
            body += content or ""
            if tc:
                body += f"\n{TOOL_CALL_OPEN}{tc}{TOOL_CALL_CLOSE}"
            out.append(f"{BOS}assistant\n{body}\n{EOS}\n")
        elif role == "tool":
            out.append(f"{BOS}tool\n{TOOL_RESPONSE_OPEN}{m.get('content', '')}{TOOL_RESPONSE_CLOSE}\n{EOS}\n")
    if sys_tools and not any("Tools" in p for p in out):
        out.insert(0, f"{BOS}system\n{_fmt_tool_defs(sys_tools)}{EOS}\n")
    if add_generation_prompt:
        out.append(f"{BOS}assistant\n")
        if open_thinking:
            out[-1] += f"{THINK_OPEN}"
    return post_processing_chat("".join(out))


def parse_tool_calls(text: str) -> List[Dict[str, Any]]:
    calls = []
    for m in TOOL_CALL_RE.findall(text):
        try:
            calls.append(json.loads(m.strip()))
        except Exception:
            continue
    return calls


def parse_thinking(text: str) -> Dict[str, str]:
    m = THINK_RE.search(text)
    if not m:
        return {"thinking": "", "answer": text}
    return {"thinking": m.group(1).strip(),
            "answer": THINK_RE.sub("", text).strip()}


def split_reasoning_content(text: str) -> Dict[str, Any]:
    """Split generated text into reasoning_content / content / tool_calls (API)."""
    th = parse_thinking(text)
    tcs = parse_tool_calls(text)
    content = th["answer"]
    for m in TOOL_CALL_RE.finditer(text):
        content = content.replace(m.group(0), "")
    return {"reasoning_content": th["thinking"], "content": content.strip(),
            "tool_calls": tcs}
