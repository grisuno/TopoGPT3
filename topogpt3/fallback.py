"""Local-fallback profiles, apt_chain tooling and deterministic reranking.

Everything here is model-side: LazyOwn/TopoSwarm only need to point their
OpenAI-compatible client at ``/v1``. No changes in those repositories.
"""

from __future__ import annotations

import ast
import json
import re
from collections.abc import Sequence
from dataclasses import dataclass
from typing import Any

from .chat import parse_tool_calls, split_reasoning_content

MAX_TOOL_TEXT = 8192
_APT_CHAIN_RE = re.compile(r"<tool_call>\s*(\{.*?\})\s*</tool_call>", re.DOTALL)

APT_CHAIN_TOOL: dict[str, Any] = {
    "type": "function",
    "function": {
        "name": "apt_chain",
        "description": (
            "Run a YAML-administered APT chain in LazyOwn against an authorized "
            "target. Supports dry-run, step filters, playbooks and JSON output."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "chain": {
                    "type": "string",
                    "description": "Chain name, e.g. apt_chain or apt_rocke.",
                    "default": "apt_chain",
                },
                "target": {
                    "type": "string",
                    "description": "Authorized IP, hostname or CIDR.",
                },
                "playbook": {"type": "string"},
                "steps": {
                    "type": "string",
                    "description": "Comma-separated step ids.",
                },
                "vars": {
                    "type": "object",
                    "additionalProperties": {"type": "string"},
                },
                "dry_run": {"type": "boolean", "default": True},
                "json": {"type": "boolean", "default": True},
                "replan": {"type": "boolean"},
                "timeout_s": {
                    "type": "integer",
                    "minimum": 1,
                    "maximum": 1800,
                },
                "no_checkpoint": {"type": "boolean"},
            },
            "required": ["target"],
            "additionalProperties": False,
        },
    },
}

RUN_COMMAND_TOOL: dict[str, Any] = {
    "type": "function",
    "function": {
        "name": "run_command",
        "description": "Run one bounded LazyOwn shell command (no shell metacharacters).",
        "parameters": {
            "type": "object",
            "properties": {
                "command": {"type": "string"},
                "timeout_s": {
                    "type": "integer",
                    "minimum": 1,
                    "maximum": 600,
                },
            },
            "required": ["command"],
            "additionalProperties": False,
        },
    },
}

READ_FACTS_TOOL: dict[str, Any] = {
    "type": "function",
    "function": {
        "name": "read_facts",
        "description": "Read the current LazyOwn facts/objectives for the session.",
        "parameters": {
            "type": "object",
            "properties": {"limit": {"type": "integer", "minimum": 1, "maximum": 200}},
            "additionalProperties": False,
        },
    },
}

LAZYOWN_TOOLS = [APT_CHAIN_TOOL, RUN_COMMAND_TOOL, READ_FACTS_TOOL]

_TOOL_REQUIRED = {
    "apt_chain": ["target"],
    "run_command": ["command"],
    "read_facts": [],
}


@dataclass(frozen=True)
class Profile:
    name: str
    system: str
    tools: tuple[dict[str, Any], ...] = ()
    temperature: float = 0.2
    top_k: int = 40
    repetition_penalty: float = 1.0
    max_tokens: int = 256
    stop: tuple[str, ...] = ()
    prefer_code: bool = False
    require_tool: bool = False
    verifier: str = "general"
    best_of: int = 1
    min_new_tokens: int = 0

    def tool_names(self) -> set[str]:
        return {
            t.get("function", {}).get("name", "")
            for t in self.tools
            if isinstance(t, dict)
        }


BASE_SYSTEM = "Local fallback assistant. Be concise and deterministic."

TOOL_SYSTEM = (
    BASE_SYSTEM
    + " Use tools with "
    + '<tool_call>{"name": "TOOL", "arguments": {...}}'
    + " One tool per turn."
)

EXPLOIT_SYSTEM = (
    "Local red-team fallback. Authorized targets only. Prefer the apt_chain "
    "tool. " + TOOL_SYSTEM
)

PROFILES: dict[str, Profile] = {
    "topogpt3": Profile(
        name="topogpt3",
        system=BASE_SYSTEM,
        temperature=0.3,
        max_tokens=256,
    ),
    "topogpt3-code": Profile(
        name="topogpt3-code",
        system=(
            BASE_SYSTEM
            + " Return only code inside one fenced block. No prose, no placeholders."
        ),
        temperature=0.0,
        top_k=1,
        max_tokens=384,
        prefer_code=True,
        verifier="code",
    ),
    "topogpt3-tools": Profile(
        name="topogpt3-tools",
        system=TOOL_SYSTEM,
        tools=tuple(LAZYOWN_TOOLS),
        temperature=0.0,
        top_k=1,
        max_tokens=192,
        require_tool=True,
        verifier="tool",
        min_new_tokens=24,
    ),
    "topoexploit": Profile(
        name="topoexploit",
        system=EXPLOIT_SYSTEM,
        tools=tuple(LAZYOWN_TOOLS),
        temperature=0.1,
        top_k=20,
        max_tokens=320,
        verifier="tool",
        best_of=2,
        min_new_tokens=32,
    ),
    "topoexploit-apt-chain": Profile(
        name="topoexploit-apt-chain",
        system=(
            EXPLOIT_SYSTEM
            + " For this request emit one apt_chain tool call with a valid chain "
            + "and target. Set dry_run=true unless the user authorized execution."
        ),
        tools=(APT_CHAIN_TOOL,),
        temperature=0.0,
        top_k=1,
        max_tokens=160,
        require_tool=True,
        verifier="apt_chain",
        best_of=4,
        min_new_tokens=24,
    ),
}

ALIASES = {
    "topogpt3": "topogpt3",
    "topoexploit": "topoexploit",
    "topogpt3-code": "topogpt3-code",
    "topogpt3-tools": "topogpt3-tools",
    "topoexploit-apt-chain": "topoexploit-apt-chain",
    "code": "topogpt3-code",
    "tools": "topogpt3-tools",
    "apt-chain": "topoexploit-apt-chain",
    "apt_chain": "topoexploit-apt-chain",
    "fallback": "topogpt3",
    "local": "topogpt3",
}


def resolve_profile(model: str | None) -> Profile:
    key = (model or "topogpt3").strip().lower()
    key = ALIASES.get(key, key)
    return PROFILES.get(key, PROFILES["topogpt3"])


def models_payload(default_checkpoint: str = "") -> list[dict[str, Any]]:
    created = 0
    out = []
    for name, profile in PROFILES.items():
        out.append(
            {
                "id": name,
                "object": "model",
                "created": created,
                "owned_by": "topogpt3",
                "metadata": {
                    "profile": name,
                    "tools": sorted(profile.tool_names()),
                    "temperature": profile.temperature,
                    "max_tokens": profile.max_tokens,
                    "best_of": profile.best_of,
                    "checkpoint": default_checkpoint,
                },
            }
        )
    return out


def _valid_target(value: str) -> bool:
    return bool(
        value and len(value) <= 255 and re.fullmatch(r"[A-Za-z0-9_.:/\-\[\]]+", value)
    )


def validate_tool_call(
    call: dict[str, Any], allowed: set[str] | None = None
) -> tuple[bool, str]:
    name = str(call.get("name", ""))
    if allowed is not None and name not in allowed:
        return False, f"tool not allowed: {name}"
    args = call.get("arguments", call.get("parameters", {}))
    if isinstance(args, str):
        try:
            args = json.loads(args)
        except json.JSONDecodeError:
            return False, "arguments are not valid JSON"
    if not isinstance(args, dict):
        return False, "arguments must be an object"

    required = _TOOL_REQUIRED.get(name)
    if required is None:
        return False, f"unknown tool: {name}"
    for key in required:
        if not str(args.get(key, "")).strip():
            return False, f"missing required argument: {key}"

    if name == "apt_chain":
        chain = str(args.get("chain", "apt_chain")).strip()
        if not re.fullmatch(r"[A-Za-z0-9_.\-]{1,64}", chain):
            return False, "invalid chain name"
        if not _valid_target(str(args.get("target", "")).strip()):
            return False, "invalid target"
        steps = args.get("steps")
        if steps is not None and not re.fullmatch(r"[A-Za-z0-9_,.\-]*", str(steps)):
            return False, "invalid steps filter"
        variables = args.get("vars", {})
        if variables is not None and not isinstance(variables, dict):
            return False, "vars must be an object"
        timeout = args.get("timeout_s")
        if timeout is not None and not (1 <= int(timeout) <= 1800):
            return False, "timeout_s out of range"
    elif name == "run_command":
        command = str(args.get("command", ""))
        if len(command) > 2000 or re.search(r"[;&|<>`$()\x00-\x1f]", command):
            return False, "command contains forbidden characters"
    return True, "ok"


def _extract_code(text: str) -> str:
    blocks = re.findall(r"```(?:python|py)?\s*(.*?)```", text, re.DOTALL)
    return blocks[0] if blocks else text


def _json_valid(text: str) -> bool:
    stripped = text.strip()
    if stripped.startswith("```"):
        stripped = re.sub(r"^```[a-zA-Z]*\s*", "", stripped)
        stripped = re.sub(r"\s*```$", "", stripped)
    try:
        json.loads(stripped)
        return True
    except json.JSONDecodeError:
        return False


def _repetition(text: str, n: int = 4) -> float:
    toks = re.findall(r"\w+|[^\w\s]", text.lower())
    grams = [tuple(toks[i : i + n]) for i in range(len(toks) - n + 1)]
    if not grams:
        return 0.0
    return (len(grams) - len(set(grams))) / len(grams)


def score_candidate(
    text: str,
    profile: Profile,
    prompt: str = "",
    allowed_tools: set[str] | None = None,
) -> tuple[float, dict[str, Any]]:
    """Deterministic, dependency-free candidate score (higher is better)."""
    text = text or ""
    score = 0.0
    details: dict[str, Any] = {"tool_calls": 0, "valid_tools": 0}

    if not text.strip():
        return -100.0, {"reason": "empty"}

    calls = parse_tool_calls(text)
    details["tool_calls"] = len(calls)
    names = profile.tool_names()
    allowed = allowed_tools if allowed_tools is not None else names

    if names or profile.require_tool:
        for call in calls:
            ok, reason = validate_tool_call(call, allowed)
            if ok:
                details["valid_tools"] += 1
                score += 6.0
            else:
                details.setdefault("errors", []).append(reason)
                score -= 4.0
        if calls:
            score += 2.0 * details["valid_tools"]
            if profile.require_tool and len(calls) == 1:
                score += 1.0
        elif profile.require_tool:
            score -= 8.0
        if profile.require_tool:
            outside = _APT_CHAIN_RE.sub("", text).strip()
            if outside and not any(
                w in outside.lower() for w in ("authorized", "ok", "ready")
            ):
                score -= min(3.0, len(outside) / 200.0)

    if profile.prefer_code or profile.verifier == "code":
        code = _extract_code(text)
        if "```" in text:
            score += 1.0
        try:
            ast.parse(code)
            score += 6.0
            details["code_parses"] = True
        except SyntaxError:
            score -= 6.0
            details["code_parses"] = False
        lowered = code.lower()
        if any(token in lowered for token in ("todo", "pass  #", "your code here")):
            score -= 2.0

    if profile.verifier == "json":
        if _json_valid(text):
            score += 6.0
            details["json_valid"] = True
        else:
            score -= 6.0
            details["json_valid"] = False

    stripped = text.strip()
    if 10 <= len(stripped) <= 2000:
        score += 1.0
    if len(stripped) > 4000:
        score -= 2.0
    if "\x00" in text:
        score -= 20.0
    score -= 4.0 * _repetition(text)
    if prompt and stripped.lower() == prompt.strip().lower():
        score -= 5.0

    details["score"] = score
    return score, details


def select_best(
    candidates: Sequence[str],
    profile: Profile,
    prompt: str = "",
    allowed_tools: set[str] | None = None,
) -> tuple[int, str, float, dict[str, Any]]:
    best_i, best_text, best_score, best_details = 0, "", -1e18, {}
    for i, text in enumerate(candidates):
        score, details = score_candidate(text, profile, prompt, allowed_tools)
        if score > best_score:
            best_i, best_text, best_score, best_details = i, text, score, details
    return best_i, best_text, best_score, best_details


def tool_calls_payload(text: str) -> list[dict[str, Any]]:
    """Convert parsed calls into OpenAI ``tool_calls`` response objects."""
    out = []
    for i, call in enumerate(parse_tool_calls(text)):
        args = call.get("arguments", {})
        if not isinstance(args, str):
            args = json.dumps(args, separators=(",", ":"))
        out.append(
            {
                "id": f"call_{i:04d}",
                "type": "function",
                "function": {"name": call.get("name", ""), "arguments": args},
            }
        )
    return out


def split_response(text: str) -> dict[str, Any]:
    parts = split_reasoning_content(text)
    parts["tool_calls"] = tool_calls_payload(text)
    return parts


def rank_candidates(
    candidates: Sequence[str],
    profile: Profile,
    prompt: str = "",
    allowed_tools: set[str] | None = None,
) -> list[tuple[float, int, str, dict[str, Any]]]:
    """Score and sort candidates (best first) preserving original indices."""
    scored = []
    for i, text in enumerate(candidates):
        score, details = score_candidate(text, profile, prompt, allowed_tools)
        scored.append((score, i, text, details))
    scored.sort(key=lambda item: (-item[0], item[1]))
    return scored


def synthesize_tool_call(profile: Profile, prompt: str) -> dict[str, Any] | None:
    """Deterministic last-resort call for require_tool profiles.

    The base checkpoints are not instruction-tuned, so a constrained profile
    may finish without emitting a valid call. For fallback deployments the
    API synthesizes a conservative call from the prompt instead of failing.
    """
    if not profile.tool_names():
        return None
    target = ""
    ip_match = re.search(r"\b(?:\d{1,3}\.){3}\d{1,3}(?:/\d{1,2})?\b", prompt or "")
    if ip_match:
        target = ip_match.group(0)
    else:
        match = re.search(
            r"\b(?:against|target(?:ing|ed)?|on|host)\s+"
            r"([A-Za-z0-9_.:/\-\[\]]+)",
            prompt or "",
            re.IGNORECASE,
        )
        if match:
            target = match.group(1).strip(".,;: ")
    if not target or not _valid_target(target):
        return None

    if "apt_chain" in profile.tool_names():
        chain = "apt_chain"
        book = re.search(r"\b(apt_[a-z0-9_]+)\b", prompt, re.IGNORECASE)
        playbook = book.group(1) if book else ""
        if playbook and playbook != chain:
            return {
                "name": "apt_chain",
                "arguments": {
                    "chain": playbook,
                    "target": target,
                    "dry_run": True,
                    "json": True,
                },
            }
        return {
            "name": "apt_chain",
            "arguments": {"target": target, "dry_run": True, "json": True},
        }

    if "run_command" in profile.tool_names():
        command = re.search(
            r"(?:run|execute|cmd)\s*:?\s*([A-Za-z0-9_ ./:\-=]+)", prompt, re.IGNORECASE
        )
        if command:
            return {
                "name": "run_command",
                "arguments": {"command": command.group(1).strip(), "timeout_s": 60},
            }
    return None
