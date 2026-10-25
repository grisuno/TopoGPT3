#!/usr/bin/env bash
# Serve TopoGPT3 (code) + TopoExploit (red-team) as OpenAI-compatible
# fallback endpoints for LazyOwn / TopoSwarm. No changes needed in those
# repositories: they only need an OpenAI-compatible base URL.
#
#   TopoGPT3    -> http://127.0.0.1:8800/v1
#   TopoExploit -> http://127.0.0.1:8801/v1
#
# Env:
#   TOPOGPT3_REPO   (default /home/grisun0/src_note/py/TopoGPT3)
#   TOPOEXPLOIT_REPO (default /home/grisun0/src_note/py/TopoExploit/repo/TopoExploit)
#   TOPOGPT3_PORT (8800), TOPOEXPLOIT_PORT (8801)
#   TOPOGPT3_API_KEYS (empty => no auth; set e.g. "sk-local" to require Bearer)
#   SERVE_DEVICE ("cpu" | "cuda")
set -euo pipefail

TOPOGPT3_REPO="${TOPOGPT3_REPO:-/home/grisun0/src_note/py/TopoGPT3}"
TOPOEXPLOIT_REPO="${TOPOEXPLOIT_REPO:-/home/grisun0/src_note/py/TopoExploit/repo/TopoExploit}"
TOPOGPT3_PORT="${TOPOGPT3_PORT:-8800}"
TOPOEXPLOIT_PORT="${TOPOEXPLOIT_PORT:-8801}"
TOPOGPT3_API_KEYS="${TOPOGPT3_API_KEYS:-}"
SERVE_DEVICE="${SERVE_DEVICE:-cpu}"

start_one() {
  local name="$1" repo="$2" ckpt="$3" port="$4"
  if curl -sf "http://127.0.0.1:${port}/health" >/dev/null 2>&1; then
    echo "[serve_fallback] ${name} already up on :${port}"
    return 0
  fi
  echo "[serve_fallback] starting ${name} on :${port} (${ckpt})"
  (
    cd "${repo}"
    TOPOGPT3_API_KEYS="${TOPOGPT3_API_KEYS}" TOPOGPT3_DEVICE="${SERVE_DEVICE}" \
      nohup python3 -m topogpt3 api_server \
        --checkpoint "${ckpt}" --host 127.0.0.1 --port "${port}" \
        ${TOPOGPT3_API_KEYS:+--keys "${TOPOGPT3_API_KEYS}"} \
        >>"/tmp/${name}.log" 2>&1 &
    echo $! > "/tmp/${name}.pid"
  )
  for _ in $(seq 1 60); do
    curl -sf "http://127.0.0.1:${port}/health" >/dev/null 2>&1 && break
    sleep 0.5
  done
  curl -sf "http://127.0.0.1:${port}/health" >/dev/null 2>&1 \
    && echo "[serve_fallback] ${name} healthy" \
    || { echo "[serve_fallback] ${name} FAILED (see /tmp/${name}.log)"; return 1; }
}

start_one topogpt3 "${TOPOGPT3_REPO}" "checkpoints_topogpt3/last" "${TOPOGPT3_PORT}"
start_one topoexploit "${TOPOEXPLOIT_REPO}" "checkpoints_topoexploit/last" "${TOPOEXPLOIT_PORT}"

echo "[serve_fallback] endpoints:"
echo "  code/red-team fallback : http://127.0.0.1:${TOPOGPT3_PORT}/v1  (profiles: topogpt3, topogpt3-code, topogpt3-tools)"
echo "  red-team + apt_chain   : http://127.0.0.1:${TOPOEXPLOIT_PORT}/v1 (profiles: topoexploit, topoexploit-apt-chain)"
