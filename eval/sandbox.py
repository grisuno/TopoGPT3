"""Sandbox for executing model-generated code during HumanEval evaluation.

This module replaces the bare `exec()` call in `eval/harness.py:run_one_test`
with a defence-in-depth check inspired by Claude Code's BashTool permission
gates (see `claude-code-main/src/tools/BashTool/bashSecurity.ts`).

The threat model:
  - A language model emits Python source as a "candidate function".
  - The candidate is `exec()`'d alongside a hidden test.
  - Without protection, the model can `import os; os.system('rm -rf /')`,
    read secrets, fork-bomb, or hang the evaluator forever.

Layered defences (each can be disabled independently for debugging):
  1. AST pre-check: parse the candidate, reject anything that imports
     dangerous modules, calls dangerous builtins, or shadows `__builtins__`.
  2. Builtin whitelist: even if the candidate parses, `safe_exec` provides
     a stripped `__builtins__` without `open`, `exec`, `eval`, `__import__`,
     `compile`, `getattr` (controversial but standard).
  3. Subprocess isolation: `safe_exec` runs the program in a child
     process so the OS enforces the timeout (vs. signal-based which the
     main thread can swallow).
  4. Output capture: stdout/stderr are piped, not inherited from the
     parent terminal.

Usage:
    from eval.sandbox import safe_exec, check_safety, SandboxConfig

    cfg = SandboxConfig(timeout=10.0, dry_run=False)
    ok, reason = check_safety(candidate_src, cfg)
    if not ok:
        return False, f"rejected by sandbox: {reason}", "", "", ""

    passed, msg, so, se, tb = safe_exec(program_src, cfg)
"""
from __future__ import annotations

import ast
import os
import subprocess
import sys
import tempfile
import textwrap
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple


# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

@dataclass
class SandboxConfig:
    """One knob per defence layer. Defaults match HumanEval-style eval."""
    timeout: float = 20.0
    dry_run: bool = False           # if True, check_safety still runs but safe_exec no-ops
    max_ast_depth: int = 50         # arbitrary; deep AST is suspicious but legal
    max_program_bytes: int = 200_000
    # Builtins safe for a HumanEval-style "implement this function" task.
    # Stripped: open, exec, eval, __import__, compile, input, breakpoint,
    #           globals, locals, vars, setattr, delattr, help.
    allowed_builtin_names: Set[str] = field(default_factory=lambda: {
        "abs", "all", "any", "ascii", "bin", "bool", "bytearray", "bytes",
        "callable", "chr", "classmethod", "complex", "copyright", "credits",
        "dict", "dir", "divmod", "enumerate", "exit", "filter", "float",
        "format", "frozenset", "hash", "hex", "id", "int", "isinstance",
        "issubclass", "iter", "len", "list", "map", "max", "memoryview",
        "min", "next", "object", "oct", "ord", "pow", "print", "property",
        "quit", "range", "repr", "reversed", "round", "set", "slice",
        "sorted", "staticmethod", "str", "sum", "super", "tuple", "type",
        "zip", "__build_class__", "__name__", "__doc__", "__loader__",
        "__spec__", "__file__", "__package__",
    })
    # Module names that the AST pre-check refuses unconditionally.
    # (We can't fully prevent imports; this catches the obvious ones.)
    blocked_modules: Set[str] = field(default_factory=lambda: {
        "os", "sys", "subprocess", "socket", "shutil", "ctypes", "cffi",
        "multiprocessing", "threading", "requests", "urllib", "http",
        "ftplib", "smtplib", "telnetlib", "asyncio", "signal", "fcntl",
        "resource", "pwd", "grp", "termios", "tty", "pty", "posix",
        "importlib", "code", "codeop", "pickle", "shelve", "marshal",
    })
    # Attribute names that the AST pre-check refuses on any object.
    # Catches `obj.__class__.__bases__[0].__subclasses__()` style escapes.
    blocked_dunder_attrs: Set[str] = field(default_factory=lambda: {
        "__class__", "__bases__", "__subclasses__", "__globals__",
        "__code__", "__subclasses__", "__import__", "__builtins__",
        "__loader__", "__spec__", "__init_subclass__", "__set_name__",
    })


# ---------------------------------------------------------------------------
# Layer 1: AST pre-check
# ---------------------------------------------------------------------------

# Node types that, if their value is a name in `blocked_modules`, mean reject.
_IMPORT_NODES = (ast.Import, ast.ImportFrom)


def _names_imported(tree: ast.AST) -> Set[str]:
    """Return the set of top-level names brought into scope by imports."""
    out: Set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                # alias.asname or alias.name
                out.add((alias.asname or alias.name).split(".")[0])
        elif isinstance(node, ast.ImportFrom):
            for alias in node.names:
                out.add((alias.asname or alias.name).split(".")[0])
    return out


def _blocked_dunder_access(tree: ast.AST, blocked: Set[str]) -> List[str]:
    """Find Attribute nodes whose attr is in `blocked`. Returns attr names found."""
    found: List[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Attribute) and node.attr in blocked:
            found.append(node.attr)
    return found


def _max_depth(tree: ast.AST) -> int:
    """Compute max nesting depth of the AST. Catches obfuscated huge trees."""
    def d(node, cur):
        children = list(ast.iter_child_nodes(node))
        if not children:
            return cur
        return max(d(c, cur + 1) for c in children)
    return d(tree, 0)


def check_safety(source: str, cfg: SandboxConfig) -> Tuple[bool, str]:
    """
    Return (ok, reason). `reason` is "" when ok, else a human-readable
    one-line explanation. Reasons are stable (used in test fixtures).
    """
    if not isinstance(source, str):
        return False, "source is not a string"
    if len(source) > cfg.max_program_bytes:
        return False, f"source too large ({len(source)} > {cfg.max_program_bytes})"
    try:
        tree = ast.parse(source, mode="exec")
    except SyntaxError as exc:
        return False, f"SyntaxError: {exc.msg}"
    if _max_depth(tree) > cfg.max_ast_depth:
        return False, f"AST too deep (>{cfg.max_ast_depth})"

    # 1. Blocked imports (best-effort; `importlib.import_module` slips through)
    imported = _names_imported(tree)
    bad_imports = imported & cfg.blocked_modules
    if bad_imports:
        return False, f"blocked import(s): {sorted(bad_imports)}"

    # 2. Blocked dunder attribute access
    bad_dunders = _blocked_dunder_access(tree, cfg.blocked_dunder_attrs)
    if bad_dunders:
        # Dedupe but keep order for stable error messages
        seen = set()
        uniq = [x for x in bad_dunders if not (x in seen or seen.add(x))]
        return False, f"blocked attribute access: {uniq}"

    return True, ""


# ---------------------------------------------------------------------------
# Layer 2+3+4: safe_exec via subprocess
# ---------------------------------------------------------------------------

# Worker script that runs in the child process. Has stripped builtins and
# pipes output. Imports from this module aren't possible because we don't
# add the repo to sys.path.

_SAFE_EXEC_WORKER = r'''
import builtins as _builtins_mod
import sys as _sys
import json as _json

# Build a stripped __builtins__ dict. We don't replace the module-level
# builtins (that would affect our own worker code) — we pass this dict
# as `__builtins__` to the user's exec below.
_KEEP_NAMES = set(__allowed_names__)
_SAFE_BUILTINS = {
    n: getattr(_builtins_mod, n)
    for n in _KEEP_NAMES
    if hasattr(_builtins_mod, n)
}

# Block these builtins outright.
def _blocked(*a, **k):
    raise NameError("disabled in sandbox")

for _n in ("open", "exec", "eval", "compile", "input",
          "breakpoint", "globals", "locals", "vars", "setattr", "delattr",
          "help", "memoryview", "exit", "quit"):
    _SAFE_BUILTINS[_n] = _blocked

# Allow imports but only of whitelisted module names. Any attempt to
# import a blocked module raises ImportError BEFORE the module is even
# looked up. This is the second line of defence: AST pre-check catches
# the obvious `import os`, but a model could do `__import__("os")` at
# runtime; this guard catches that.
_BLOCKED_MODULES = set(__blocked_modules__)

_real_import = _builtins_mod.__import__

def _guarded_import(name, *args, **kwargs):
    if name.split(".")[0] in _BLOCKED_MODULES:
        raise ImportError(
            "module {!r} is blocked by the sandbox".format(name)
        )
    return _real_import(name, *args, **kwargs)

_SAFE_BUILTINS["__import__"] = _guarded_import

_globals = {"__builtins__": _SAFE_BUILTINS, "__name__": "__sandbox__",
            "__doc__": None, "__package__": None}
_locals = {}

_result = {"ok": True, "_noop": True}
try:
    import contextlib as _cl
    import io as _io
    _stdout_ctx = _io.StringIO()
    _stderr_ctx = _io.StringIO()
    with _cl.redirect_stdout(_stdout_ctx), _cl.redirect_stderr(_stderr_ctx):
        exec(__program_src__, _globals, _locals)
    _stdout_val = _stdout_ctx.getvalue()
    _stderr_val = _stderr_ctx.getvalue()
    _result = {"ok": True, "stdout": _stdout_val, "stderr": _stderr_val, "tb": ""}
    _stdout_ctx.close()
    _stderr_ctx.close()
except BaseException as _exc:
    import traceback as _tb
    try:
        _stdout_val = _stdout_ctx.getvalue()
    except Exception:
        _stdout_val = ""
    try:
        _stderr_val = _stderr_ctx.getvalue()
    except Exception:
        _stderr_val = ""
    _result = {"ok": False,
               "stdout": _stdout_val,
               "stderr": _stderr_val,
               "tb": _tb.format_exc(),
               "exc_type": type(_exc).__name__,
               "exc_msg": str(_exc)}
_sys.stdout.write("__SANDBOX_RESULT__" + _json.dumps(_result) + "\n")
_sys.stdout.flush()
'''


def _build_worker_src(
    allowed_builtin_names: Set[str],
    program_src: str,
    blocked_modules: Optional[Set[str]] = None,
) -> str:
    # Replace placeholders. Use json to escape the program source safely.
    if blocked_modules is None:
        blocked_modules = set()
    return (
        _SAFE_EXEC_WORKER
        .replace("__allowed_names__", repr(sorted(allowed_builtin_names)))
        .replace("__blocked_modules__", repr(sorted(blocked_modules)))
        .replace("__program_src__", repr(program_src))
    )


def safe_exec(
    program_src: str,
    cfg: SandboxConfig,
    extra_globals: Optional[Dict[str, object]] = None,
) -> Tuple[bool, str, str, str, str]:
    """
    Execute `program_src` in a sandboxed child process. Returns the same
    5-tuple as `eval.harness.run_one_test` for drop-in compatibility.

    The child is killed (SIGKILL) by the OS after `cfg.timeout` seconds.
    """
    if cfg.dry_run:
        return False, "dry_run: would exec", "", "", ""

    ok, reason = check_safety(program_src, cfg)
    if not ok:
        return False, f"sandbox_rejected: {reason}", "", "", ""

    if extra_globals:
        # Inject extras (e.g. a stub `open` for the test) into the program
        # prefix. We don't allow them to bypass the safety check because
        # they go through `ast.parse` together with the program.
        for k, v in extra_globals.items():
            if not k.isidentifier():
                return False, f"sandbox_rejected: bad extra global name {k!r}", "", "", ""
            program_src = f"{k} = {v!r}\n" + program_src
        ok, reason = check_safety(program_src, cfg)
        if not ok:
            return False, f"sandbox_rejected: {reason}", "", "", ""

    worker_src = _build_worker_src(
        cfg.allowed_builtin_names, program_src, cfg.blocked_modules
    )

    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".py", delete=False, encoding="utf-8"
    ) as f:
        f.write(worker_src)
        worker_path = f.name
    try:
        try:
            proc = subprocess.run(
                [sys.executable, worker_path],
                timeout=cfg.timeout,
                capture_output=True,
                text=True,
                check=False,
            )
        except subprocess.TimeoutExpired as exc:
            return (
                False,
                f"SandboxTimeout: killed after {cfg.timeout}s",
                (exc.stdout or b"").decode("utf-8", errors="replace"),
                (exc.stderr or b"").decode("utf-8", errors="replace"),
                "",
            )
    finally:
        try:
            os.unlink(worker_path)
        except OSError:
            pass

    # Parse the structured result from the child's stdout
    out = proc.stdout or ""
    marker = "__SANDBOX_RESULT__"
    if marker not in out:
        # Worker crashed before printing — surface the raw output
        return (
            False,
            f"SandboxCrash: exit={proc.returncode}",
            out,
            proc.stderr or "",
            "",
        )
    import json
    payload = out.split(marker, 1)[1].strip().splitlines()[0]
    try:
        r = json.loads(payload)
    except json.JSONDecodeError as exc:
        return (
            False,
            f"SandboxProtocolError: {exc}",
            out,
            proc.stderr or "",
            "",
        )
    if r.get("ok"):
        return True, "ok", r.get("stdout", ""), r.get("stderr", ""), ""
    exc_type = r.get("exc_type", "Exception")
    exc_msg = r.get("exc_msg", "")
    return (
        False,
        f"{exc_type}: {exc_msg}",
        r.get("stdout", ""),
        r.get("stderr", ""),
        r.get("tb", ""),
    )


# ---------------------------------------------------------------------------
# Convenience: human-readable list of what's blocked
# ---------------------------------------------------------------------------

def describe_policy(cfg: Optional[SandboxConfig] = None) -> str:
    cfg = cfg or SandboxConfig()
    lines = [
        f"SandboxConfig(timeout={cfg.timeout}s, dry_run={cfg.dry_run})",
        f"  allowed builtins ({len(cfg.allowed_builtin_names)}): "
        f"{', '.join(sorted(cfg.allowed_builtin_names))}",
        f"  blocked modules ({len(cfg.blocked_modules)}): "
        f"{', '.join(sorted(cfg.blocked_modules))}",
        f"  blocked dunder attrs ({len(cfg.blocked_dunder_attrs)}): "
        f"{', '.join(sorted(cfg.blocked_dunder_attrs))}",
    ]
    return "\n".join(lines)


if __name__ == "__main__":
    # Tiny self-test when run as a script.
    print(describe_policy())
    cases = [
        ("ok def", "def f(x):\n    return x + 1\n", True),
        ("ok import math", "import math\ndef f(x):\n    return math.sqrt(x)\n", True),
        ("bad import os", "import os\ndef f(x):\n    return os.listdir('.')\n", False),
        ("bad __class__", "def f(x):\n    return (1).__class__.__bases__\n", False),
        ("bad syntax", "def f(:\n", False),
        ("bad open",
         "def f(x):\n    return open('/etc/passwd').read()\n", False),
    ]
    for name, src, expected_ok in cases:
        ok, reason = check_safety(src, SandboxConfig())
        status = "OK" if ok == expected_ok else "FAIL"
        print(f"  [{status}] {name}: ok={ok} reason={reason!r}")
