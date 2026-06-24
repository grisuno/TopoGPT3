"""Smoke test for eval.sandbox.

Verifies all four defence layers:
  L1 (AST pre-check): blocked imports & dunder attrs are rejected
  L2 (builtin whitelist): open/exec/etc raise NameError in the child
  L3 (subprocess isolation): infinite loops are killed at OS level
  L4 (output capture): stdout/stderr from the candidate are returned
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from eval.sandbox import check_safety, safe_exec, SandboxConfig


def main():
    cfg = SandboxConfig(timeout=5.0)

    # L1: AST
    ok, reason = check_safety("import os\n", cfg)
    assert not ok and "os" in reason, f"L1 failed: {ok=} {reason=}"
    print(f"  [L1] import os            -> rejected ({reason})")

    ok, reason = check_safety("(1).__class__.__bases__\n", cfg)
    assert not ok and "__class__" in reason, f"L1 dunder failed: {ok=} {reason=}"
    print(f"  [L1] __class__ access     -> rejected ({reason})")

    # L2: builtin whitelist via safe_exec — must call the dangerous function
    # to trigger the NameError, otherwise the def is just bound silently.
    src = "def f():\n    return open('/etc/passwd').read()\nresult = f()\n"
    ok, msg, so, se, tb = safe_exec(src, cfg)
    assert not ok and "NameError" in msg, f"L2 open failed: {ok=} {msg=}"
    print(f"  [L2] open('/etc/passwd')  -> rejected at runtime ({msg})")

    # L2: imports of stdlib modules like typing should work
    src2 = "from typing import List\nx: List[int] = [1,2,3]\nresult = sum(x)\n"
    ok, msg, so, se, tb = safe_exec(src2, cfg)
    assert ok, f"L2 typing import failed: {ok=} {msg=}"
    print(f"  [L2] from typing import   -> allowed (result={so.strip()!r})")

    # L2: import of a BLOCKED module is rejected at the import guard
    src3 = "import os\nresult = os.listdir('.')\n"
    ok, msg, so, se, tb = safe_exec(src3, cfg)
    # AST pre-check should catch this; if it slips past, the import guard
    # in the child catches it.
    assert not ok, f"blocked import somehow passed: {ok=} {msg=}"
    assert ("sandbox_rejected" in msg) or ("blocked by the sandbox" in msg), \
        f"unexpected rejection msg: {msg=}"
    print(f"  [L2] import os            -> rejected ({msg[:60]}...)")

    # L2: __import__('os') at runtime is also caught by the import guard
    src4 = "result = __import__('os').listdir('.')\n"
    ok, msg, so, se, tb = safe_exec(src4, cfg)
    # AST may not catch this; the import guard in the child should.
    assert not ok, f"runtime __import__ slipped through: {ok=} {msg=}"
    print(f"  [L2] __import__('os')     -> rejected ({msg[:60]}...)")

    # L2: valid program passes
    src5 = "def f(x):\n    return x + 1\nresult = f(41)\n"
    ok, msg, so, se, tb = safe_exec(src5, cfg)
    assert ok, f"L2 simple failed: {ok=} {msg=}"
    print(f"  [L2] simple def           -> passed")

    # L2: print() in the candidate is captured
    src3 = "def f():\n    print('hi from sandbox')\n    return 1\nf()\n"
    ok, msg, so, se, tb = safe_exec(src3, cfg)
    assert "hi from sandbox" in so, f"L4 stdout capture failed: {so=}"
    print(f"  [L4] print() captured     -> {so.strip()!r}")

    # L3: infinite loop is killed at OS level
    src4 = "def f(x):\n    while True:\n        x += 1\nresult = f(0)\n"
    ok, msg, so, se, tb = safe_exec(src4, cfg)
    assert not ok and "SandboxTimeout" in msg, f"L3 timeout failed: {ok=} {msg=}"
    print(f"  [L3] infinite loop        -> killed by OS timeout ({msg})")

    # SyntaxError in candidate is caught pre-exec
    src5 = "def f(:\n"
    ok, msg, so, se, tb = safe_exec(src5, cfg)
    assert not ok and "sandbox_rejected" in msg, f"SyntaxError pre-check failed: {msg=}"
    print(f"  [L1] syntax error         -> rejected pre-exec ({msg})")

    # Runtime exception is surfaced
    src6 = "def f():\n    return 1/0\nf()\n"
    ok, msg, so, se, tb = safe_exec(src6, cfg)
    assert not ok and "ZeroDivisionError" in msg, f"runtime exc failed: {msg=}"
    print(f"  [L2] runtime ZeroDivision -> surfaced ({msg})")

    print("\nALL SANDBOX LAYERS VERIFIED")


if __name__ == "__main__":
    main()
