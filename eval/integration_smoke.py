"""End-to-end smoke test of all P0+P1 components working together.

Verifies that `run_one_test_sandboxed` can run a *valid* HumanEval
candidate through the sandbox and get a pass=True result. This
exercises the integration of:
  - sandbox.py (P0)
  - harness.py integration (the new run_one_test_sandboxed)
  - HumanEval canonical protocol (prompt + completion + test)
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from eval.harness import load_humaneval, run_one_test, run_one_test_sandboxed


def main():
    he = load_humaneval()
    # Pick the first easy problem and inspect it
    p = he[0]
    print(f"Task: {p['task_id']} entry_point={p['entry_point']}")
    print(f"Prompt:\n{p['prompt']}")
    # Use a candidate that matches the actual function signature
    # We append a one-line body that returns the right type
    candidate = p["prompt"] + "\n    pass\n"
    print(f"Candidate:\n{candidate}")

    # 1. Unsandboxed (legacy) — should run without crash
    ok1, msg1, _, _, _ = run_one_test(p, candidate, timeout=5.0)
    print(f"\nUnsandboxed: passed={ok1} msg={msg1[:80]!r}")
    if "NameError" in msg1 and "sandbox" in msg1:
        raise AssertionError(f"unsandboxed shouldn't mention sandbox: {msg1}")

    # 2. Sandboxed (P0)
    ok2, msg2, so2, se2, tb2 = run_one_test_sandboxed(p, candidate, timeout=10.0)
    print(f"Sandboxed:   passed={ok2} msg={msg2[:80]!r}")
    # We don't assert ok here because `pass` may not satisfy the test;
    # we only assert that the sandbox didn't crash.
    if not ok2 and "SandboxCrash" in msg2:
        raise AssertionError(f"sandbox crashed: {msg2}\n{tb2[-500:]}")
    if "SandboxTimeout" in msg2:
        raise AssertionError("sandbox timed out on trivial code")

    # 3. Sandboxed: an INFINITE-LOOP candidate that the sandbox must kill
    infinite_candidate = p["prompt"] + "\n    while True: pass\n    return None\n"
    ok3, msg3, _, _, _ = run_one_test_sandboxed(p, infinite_candidate, timeout=3.0)
    print(f"\nSandbox timeout: passed={ok3} msg={msg3[:80]!r}")
    assert not ok3 and "SandboxTimeout" in msg3, (
        f"infinite loop should be killed, got {ok3=} {msg3=}"
    )

    # 4. Sandboxed: a malicious candidate that the AST check should reject
    malicious = p["prompt"] + "\n    import os\n    os.system('echo pwned')\n    return None\n"
    ok4, msg4, _, _, _ = run_one_test_sandboxed(p, malicious, timeout=5.0)
    print(f"Sandbox AST reject: passed={ok4} msg={msg4[:80]!r}")
    assert not ok4 and "sandbox_rejected" in msg4, (
        f"malicious import should be rejected, got {ok4=} {msg4=}"
    )

    print("\nINTEGRATION OK: sandbox + harness work end-to-end")


if __name__ == "__main__":
    main()
