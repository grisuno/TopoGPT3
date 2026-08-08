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

.PHONY: help install install-min install-all test lint train infer infer-hrm jlens api api-auth eval eval-sample clean pi

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
	$(PY) -m topogpt3 inference \
		--checkpoint-dir $(CKPT) \
		--prompt "$(PROMPT)" \
		--max-new 200

infer-hrm: ## Hierarchical recursive reasoning inference
	$(PY) -m topogpt3 inference_hrm \
		--checkpoint-dir $(CKPT) \
		--prompt "$(PROMPT)" \
		--hr-h-iters 2 \
		--hr-l-iters 3 \
		--hr-l-window 2 \
		--max-new 200

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

# ── Pi Agent ─────────────────────────────────────────────────────────────────

PI_REPO := https://github.com/earendil-works/pi.git

pi: $(PI_DIR) ## Clone and build pi coding agent
	@echo "[pi] building..."
	cd $(PI_DIR) && npm install --ignore-scripts && npm run build
	@echo "[pi] ready. Run with: PI_BASE_URL=http://localhost:$(API_PORT)/v1 PI_API_KEY=sk-local make pi-run"

$(PI_DIR):
	git clone --depth 1 $(PI_REPO) $(PI_DIR)

pi-update: ## Update pi to latest (git pull + rebuild)
	@test -d $(PI_DIR) || { echo "Run 'make pi' first to clone pi."; exit 1; }
	cd $(PI_DIR) && git pull && npm install --ignore-scripts && npm run build

pi-run: ## Launch pi pointed at the local TopoGPT3 API server
	@test -d $(PI_DIR) || { echo "Run 'make pi' first to clone pi."; exit 1; }
	cd $(PI_DIR) && \
		TOPOGPT3_BASE_URL="http://$(API_HOST):$(API_PORT)/v1" \
		TOPOGPT3_API_KEY="$${TOPOGPT3_API_KEY:-sk-local}" \
		node packages/coding-agent/dist/cli.js

clean: ## Remove bytecode and cache files
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name '*.pyc' -delete 2>/dev/null || true
	find . -type d -name '.pytest_cache' -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name '.ruff_cache' -exec rm -rf {} + 2>/dev/null || true

clean-all: clean ## Also remove build artifacts and checkpoints
	rm -rf build/ dist/ *.egg-info/
	rm -rf checkpoints_topogpt3/last/step_*/
