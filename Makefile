# TopoGPT3 Makefile — convenience targets for every common task.
# Run `make help` to see all targets.

CKPT            := checkpoints_topogpt3/last
API_PORT        := 8800
API_HOST        := 127.0.0.1
API_KEYS        ?= sk-dev-key-change-me
PROMPT          ?= def fibonacci(n):
EVAL_OUT        := eval/results.jsonl
PY              := python
PI_DIR          := .pi

.PHONY: help install install-min install-all test lint train infer infer-continue infer-hrm infer-think jlens api api-auth eval eval-sample clean pi pi-setup pi-run pi-update c-convert c-build c-run c-run-i c-vocab

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-18s\033[0m %s\n", $$1, $$2}'

# ── Installation ─────────────────────────────────────────────────────────────

install-min: ## Install base package (no extras)
	$(PY) -m pip install -e .

install: ## Install package with all extras
	$(PY) -m pip install -e ".[train,lens,api,dev]"

install-api: ## Install package with API extras only
	$(PY) -m pip install -e ".[api]"

# ── Development ──────────────────────────────────────────────────────────────

test: ## Run full test suite
	$(PY) -m pytest tests/ -v --tb=short -q

test-jlens: ## Run Jacobian lens tests only
	$(PY) -m pytest tests/test_lens_model.py tests/test_jlens.py -v --tb=short

lint: ## Lint and format check (ruff)
	ruff check topogpt3/ tests/ eval/
	ruff format --check topogpt3/ tests/ eval/

fmt: ## Auto-format code with ruff
	ruff format topogpt3/ tests/ eval/
	ruff check --fix topogpt3/ tests/ eval/

# ── Training ─────────────────────────────────────────────────────────────────

train: ## Run full curriculum training
	$(PY) -m topogpt3 train

train-tier2: ## Start training from tier 2
	$(PY) -m topogpt3 train --start-tier 2

eval-holdout: ## Evaluate on combined holdout
	$(PY) -m topogpt3 train --eval-holdout

# ── Inference ────────────────────────────────────────────────────────────────

infer: ## Standard autoregressive inference
	$(PY) -m topogpt3.inference \
		--ckpt-dir $(CKPT) \
		--prompt "$(PROMPT)" \
		--max-new 200

infer-continue: ## Inference with auto-continuation
	$(PY) -m topogpt3.inference \
		--ckpt-dir $(CKPT) \
		--prompt "$(PROMPT)" \
		--max-new 512 \
		--auto-continue

infer-hrm: ## Hierarchical recursive reasoning inference
	$(PY) -m topogpt3.inference_hrm \
		--ckpt-dir $(CKPT) \
		--prompt "$(PROMPT)" \
		--hrm-h-iters 2 \
		--hrm-l-iters 3 \
		--hrm-l-window 2 \
		--max-new 200

infer-think: ## HRM thinking mode with auto-continuation
	$(PY) -m topogpt3.inference_hrm \
		--ckpt-dir $(CKPT) \
		--prompt "$(PROMPT)" \
		--hrm-h-iters 2 \
		--hrm-l-iters 3 \
		--hrm-l-window 2 \
		--max-new 512 \
		--thinking \
		--auto-continue

# ── Jacobian Lens ────────────────────────────────────────────────────────────

jlens: ## Jacobian lens demo (fit 4 prompts, override with PROMPT=)
	$(PY) -m topogpt3 jlens \
		--checkpoint $(CKPT) \
		--prompts 4 \
		--prompt "$(PROMPT)" \
		--max-seq-len 128

# ── API Server (agent harness) ───────────────────────────────────────────────

api: ## Start API server (no auth — DEV ONLY)
	$(PY) -m topogpt3.api_server \
		--checkpoint $(CKPT) \
		--port $(API_PORT) \
		--host $(API_HOST) \
		--no-auth

api-auth: ## Start API server with authentication
	@test -n "$$TOPOGPT3_API_KEYS" || { \
		echo "ERROR: Set TOPOGPT3_API_KEYS env var first."; \
		echo "  export TOPOGPT3_API_KEYS=\"sk-my-secret-key-12345\""; \
		exit 1; \
	}
	$(PY) -m topogpt3.api_server \
		--checkpoint $(CKPT) \
		--port $(API_PORT) \
		--host $(API_HOST)

api-verbose: ## Start API server with verbose debug logging
	$(PY) -m topogpt3.api_server \
		--checkpoint $(CKPT) \
		--port $(API_PORT) \
		--host $(API_HOST) \
		--verbose

# ── HumanEval Benchmark ──────────────────────────────────────────────────────

eval: ## Run HumanEval benchmark (all 164 problems)
	$(PY) -m eval.harness \
		--ckpt-dir checkpoints_topogpt3 \
		--ckpt-name last \
		--out $(EVAL_OUT) \
		--temperature 0.0 \
		--max-new-tokens 512

eval-hrm: ## Run HumanEval benchmark with HRM sampler
	$(PY) -m eval.harness \
		--ckpt-dir checkpoints_topogpt3 \
		--ckpt-name last \
		--out eval/results_hrm.jsonl \
		--mode hrm \
		--temperature 0.0 \
		--max-new-tokens 512

eval-sample: ## Run HumanEval on a single problem (set PROBLEM_ID=HumanEval/0)
	$(PY) -m eval.harness \
		--ckpt-dir checkpoints_topogpt3 \
		--ckpt-name last \
		--out $(EVAL_OUT) \
		--limit 1 \
		--temperature 0.0

# ── C Inference Engine (MiniOS / static ELF) ─────────────────────────────────

C_COMPILER    ?= gcc
C_FLAGS       := -O2 -static -Wall -Wextra
WEIGHTS_FILE  := topogpt3.weights

c-convert: ## Convert safetensors to binary weights for C engine
	$(PY) convert_weights.py -i $(CKPT)/model.safetensors -o $(WEIGHTS_FILE)

c-vocab: ## Generate vocab.bin for token decoding in C engine
	$(PY) -c "import tiktoken,struct;enc=tiktoken.get_encoding('gpt2');f=open('vocab.bin','wb');f.write(b'VOCB');f.write(struct.pack('<I',50257));[f.write(struct.pack('<H',len(s:=enc.decode([i]).encode('utf-8')))+s) for i in range(50257)];f.close();print('vocab.bin: 50257 tokens')"

c-build: ## Build static ELF binary (topogpt3.elf)
	$(C_COMPILER) $(C_FLAGS) -o topogpt3.elf topogpt3.c -lm

c-run: ## Run C engine in headless mode (PROMPT="def main(")
	./topogpt3.elf -T tokens.bin -n 256

c-run-i: ## Run C engine in interactive mode
	./topogpt3.elf -i

c-all: c-convert c-vocab c-build ## Convert weights + build vocab + build binary

c-tokenize: ## Tokenize PROMPT to tokens.bin (requires tiktoken)
	$(PY) encode_tokens.py "$(PROMPT)" -o tokens.bin

# ── MiniOS cross-compile (requires miniCC + ld in PATH) ──────────────────────

MINIGCC      ?= /home/grisun0/src_note/c/boot/repo/miniGCC/minigcc
MINIOS_LD    ?= /home/grisun0/src_note/c/boot/repo/ld/ld

c-minios: ## Cross-compile for MiniOS (generates topogpt3.minios.elf)
	$(MINIGCC) topogpt3.c > topogpt3.s
	$(MINIOS_LD) -f elf topogpt3.s -o topogpt3.minios.elf

# ── Pi Agent ─────────────────────────────────────────────────────────────────

PI_REPO := https://github.com/earendil-works/pi.git

pi: $(PI_DIR) ## Clone, build, and configure pi for local TopoGPT3
	cd $(PI_DIR) && npm install --ignore-scripts && npm run build
	@$(MAKE) pi-setup

$(PI_DIR):
	git clone --depth 1 $(PI_REPO) $(PI_DIR)

pi-setup: ## Configure pi to use the local TopoGPT3 API (writes ~/.pi/agent/models.json)
	@mkdir -p "$$HOME/.pi/agent"
	@echo '{' > "$$HOME/.pi/agent/models.json"
	@echo '  "providers": {' >> "$$HOME/.pi/agent/models.json"
	@echo '    "topogpt3": {' >> "$$HOME/.pi/agent/models.json"
	@echo '      "baseUrl": "http://$(API_HOST):$(API_PORT)/v1",' >> "$$HOME/.pi/agent/models.json"
	@echo '      "api": "openai-completions",' >> "$$HOME/.pi/agent/models.json"
	@echo '      "apiKey": "$$TOPOGPT3_API_KEY",' >> "$$HOME/.pi/agent/models.json"
	@echo '      "compat": {' >> "$$HOME/.pi/agent/models.json"
	@echo '        "supportsDeveloperRole": false,' >> "$$HOME/.pi/agent/models.json"
	@echo '        "supportsReasoningEffort": false' >> "$$HOME/.pi/agent/models.json"
	@echo '      },' >> "$$HOME/.pi/agent/models.json"
	@echo '      "models": [' >> "$$HOME/.pi/agent/models.json"
	@echo '        {' >> "$$HOME/.pi/agent/models.json"
	@echo '          "id": "topogpt3",' >> "$$HOME/.pi/agent/models.json"
	@echo '          "name": "TopoGPT3 (Local)",' >> "$$HOME/.pi/agent/models.json"
	@echo '          "reasoning": false,' >> "$$HOME/.pi/agent/models.json"
	@echo '          "input": ["text"],' >> "$$HOME/.pi/agent/models.json"
	@echo '          "contextWindow": 512,' >> "$$HOME/.pi/agent/models.json"
	@echo '          "maxTokens": 512,' >> "$$HOME/.pi/agent/models.json"
	@echo '          "cost": { "input": 0, "output": 0, "cacheRead": 0, "cacheWrite": 0 }' >> "$$HOME/.pi/agent/models.json"
	@echo '        }' >> "$$HOME/.pi/agent/models.json"
	@echo '      ]' >> "$$HOME/.pi/agent/models.json"
	@echo '    }' >> "$$HOME/.pi/agent/models.json"
	@echo '  }' >> "$$HOME/.pi/agent/models.json"
	@echo '}' >> "$$HOME/.pi/agent/models.json"
	@echo "[pi] wrote ~/.pi/agent/models.json"

pi-update: ## Update pi to latest (git pull + rebuild)
	@test -d $(PI_DIR) || { echo "Run 'make pi' first to clone pi."; exit 1; }
	cd $(PI_DIR) && git pull && npm install --ignore-scripts && npm run build

pi-run: ## Launch pi pointed at the local TopoGPT3 API server
	@test -d $(PI_DIR) || { echo "Run 'make pi' first to clone pi."; exit 1; }
	cd $(PI_DIR) && \
		TOPOGPT3_API_KEY="$${TOPOGPT3_API_KEY:-sk-local}" \
		node packages/coding-agent/dist/cli.js \
			--provider topogpt3 \
			--model topogpt3 \
			--api-key "$${TOPOGPT3_API_KEY:-sk-local}" \
			--system-prompt "You are a coding assistant. Write concise, correct code. Reply briefly."

clean: ## Remove bytecode, cache files, and C build artifacts
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name '*.pyc' -delete 2>/dev/null || true
	find . -type d -name '.pytest_cache' -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name '.ruff_cache' -exec rm -rf {} + 2>/dev/null || true
	rm -f topogpt3.elf topogpt3.minios.elf topogpt3.o $(WEIGHTS_FILE) vocab.bin tokens.bin

clean-all: clean ## Also remove build artifacts and checkpoints
	rm -rf build/ dist/ *.egg-info/
	rm -rf checkpoints_topogpt3/last/step_*/
