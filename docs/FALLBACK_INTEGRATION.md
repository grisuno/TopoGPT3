# Fallback integration: TopoGPT3 / TopoExploit for LazyOwn + TopoSwarm

Los checkpoints de TopoGPT3 (codigo) y TopoExploit (red-team) se sirven con
el mismo servidor OpenAI-compatible. **No se modifica nada en LazyOwn ni en
TopoSwarm**: ambos consumen la API via `base_url`.

## Endpoints

| Modelo | Repo | Endpoint | Perfiles |
|---|---|---|---|
| TopoGPT3 | `src_note/py/TopoGPT3` | `http://127.0.0.1:8800/v1` | `topogpt3`, `topogpt3-code`, `topogpt3-tools` |
| TopoExploit | `TopoExploit/repo/TopoExploit` | `http://127.0.0.1:8801/v1` | `topoexploit`, `topoexploit-apt-chain` |

Arranque:

```bash
bash scripts/serve_fallback.sh        # levanta ambos (o solo el que falte)
curl -s http://127.0.0.1:8800/health  # {"status":"ok"}
```

Auth: `TOPOGPT3_API_KEYS=sk-local` (Bearer) o vacio/`--no-auth` en local.

## Contrato OpenAI implementado

- `POST /v1/chat/completions`: historial completo (system/user/assistant/**tool**),
  `tools` top-level renderizado en el prompt, `reasoning_content`,
  `tool_calls` (`<tool_call>{"name","arguments"}</tool_call>`
  -> OpenAI deltas), `finish_reason` (`stop|length|tool_calls`), `usage`.
- `POST /v1/completions`: completions puros con anti-EOS temprano.
- Parametros por request: `temperature`, `top_k`, `repetition_penalty`,
  `max_tokens`, `seed` (determinismo), `n` (elegir N de `best_of`),
  `best_of` (candidatos + reranker), `min_new_tokens` (suprime EOS temprano),
  `response_format`/`so_args` (JSON Schema / regex / EBNF via xgrammar),
  `stream`.
- Reranking determinista (`best_of`): puntua JSON/tool-call/code-fence/AST,
  repeticion y limites; devuelve `n` mejores con `score`.

### Perfiles (`model` o `profile`)

| Perfil | Uso | Decoding | Herramientas |
|---|---|---|---|
| `topogpt3` | chat generico | temp 0.3 | - |
| `topogpt3-code` | generacion de codigo | greedy, AST verifier | - |
| `topogpt3-tools` | fallback agentico | greedy + rerank | apt_chain, run_command, read_facts |
| `topoexploit` | analisis red-team | temp 0.1, best_of 2 | apt_chain, run_command, read_facts |
| `topoexploit-apt-chain` | cadena APT completa | greedy, best_of 4, require_tool | apt_chain |

`/v1/models` lista los perfiles con sus metadatos (tools, sampling).

## apt_chain

El modelo emite:

```
<tool_call>{"name": "apt_chain", "arguments": {"chain": "apt_chain", "target": "10.10.11.78", "dry_run": true, "json": true}}</tool_call>
```

Validacion server-side (`topogpt3/fallback.validate_tool_call`): target
obligatorio y seguro (IP/host/CIDR), chain `^[A-Za-z0-9_.-]+$`,
`timeout_s<=1800`, sin metacaracteres en `run_command`. La **ejecucion es
de LazyOwn** (MCP `lazyown_apt_chain` / ChainRunner); el modelo solo emite
y valida la llamada. Si el perfil exige tool call y el checkpoint no la
emite, la API sintetiza una llamada conservadora (`dry_run=true`) marcada
con `synthetic_tool_call: true`.

Ejemplo con curl (sin auth):

```bash
curl -s http://127.0.0.1:8801/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{
    "profile":"topoexploit-apt-chain",
    "messages":[{"role":"user","content":"Run the full chain against 10.10.11.78"}],
    "seed":7
  }'
```

Respuesta: `choices[0].message.tool_calls[0].function.name == "apt_chain"`.

## Integracion LazyOwn (sin tocar su codigo)

El `LlmPool` del loop consume miembros OpenAI-compatible; para completions
basta un backend `llamacpp`/`openai` apuntando al `base_url` de arriba, o el
fallover `ai_fallback` de LazyOwn con `META_PROPOSER_API_URL`. Para el
worker agentico (function calling), apuntar a `:8801/v1` con perfil
`topoexploit` (streaming emite `tool_calls`).

## Integracion TopoSwarm (sin tocar su codigo)

```bash
export META_PROPOSER_API_URL=http://127.0.0.1:8801/v1
export META_PROPOSER_MODEL=topoexploit
```

## Calidad del modelo (estado actual y pipeline)

Los checkpoints estan **undertrained** (T3: HumanEval pass@1 ~4%;
TopoExploit: 36-82 pasos). El repo trae todo el pipeline para subir acc:

```bash
# 1) datos: dedup + filtros + teacher verificado
python -m topogpt3.data_pipeline --input raw.jsonl --out clean.jsonl --stage clean
python -m topogpt3.data_pipeline --input prompts.jsonl --out sft.jsonl \
  --stage teacher --teacher-url http://localhost:11434/v1 \
  --teacher-model llama3.1 --domain exploit --verify python

# 2) SFT chat/tools (apt_chain incluido en TOOLS)
python -m topogpt3 train_agent --data sft.jsonl --checkpoint checkpoints_topoexploit/last

# 3) RL con verificador/ejecucion sandboxed
python -m topogpt3 train_grpo --data sft.jsonl --checkpoint checkpoints_topoexploit/last

# 4) eval por tarea
make eval-tasks          # apt_chain 20 casos
make eval                # HumanEval pass@1

# 5) tokenizer: auditoria y resize para reentrenar
python -m topogpt3.tokenizer_tools --audit checkpoints_topogpt3/last
```

Arreglos aplicados a ambos forks: offset absoluto de RoPE con KV-cache
(sliding window ya no resetea posiciones), gradiente de la temperatura de
atencion, recarga de EWC en resume, nombres de tier ExploitGym en modo
merged, auto-deteccion de escala (`state.json` + shapes), presets
large/xlarge en T3, streaming con KV-cache (antes re-forward completo).
