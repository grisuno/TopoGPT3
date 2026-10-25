# `scripts/serve_fallback.sh`

> Source: [scripts/serve_fallback.sh:1](../../scripts/serve_fallback.sh#L1) | language `sh` | coverage 50.0% | [API index](../index.md)

Serve TopoGPT3 (code) + TopoExploit (red-team) as OpenAI-compatible fallback endpoints for LazyOwn / TopoSwarm.

No changes needed in those repositories: they only need an OpenAI-compatible base URL.  TopoGPT3    -> http://127.0.0.1:8800/v1 TopoExploit -> http://127.0.0.1:8801/v1  Env: TOPOGPT3_REPO   (default /home/grisun0/src_note/py/TopoGPT3) TOPOEXPLOIT_REPO (default /home/grisun0/src_note/py/TopoExploit/repo/TopoExploit) TOPOGPT3_PORT (8800), TOPOEXPLOIT_PORT (8801) TOPOGPT3_API_KEYS (empty => no auth; set e.g. "sk-local" to require Bearer) SERVE_DEVICE ("cpu" | "cuda")

## Contents

- **Functions:** [`start_one`](#start_one)

## Functions

<a id="start_one"></a>

### `start_one`

`function` | [scripts/serve_fallback.sh:24](../../scripts/serve_fallback.sh#L24)

```bash
start_one()
```

---
