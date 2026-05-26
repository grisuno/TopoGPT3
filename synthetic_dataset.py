#!/usr/bin/env python3
"""
Synthetic Dataset Generator for TopoGPT2.

Generates high-quality code instruction-tuning data from existing source files
using a multi-stage LLM pipeline:

    file → analysis → spec → chain-of-thought → vague question → JSONL

Each sample (JSONL line) contains:
{
    "instruction":  "vague natural question",
    "thinking":     "chain-of-thought reasoning",
    "spec":         "detailed spec-driven prompt",
    "todo":         ["task 1", "task 2", ...],
    "response":     "```language\noriginal clean code\n```",
    "file_path":    "src/foo/bar.py",
    "lang":         "python",
    "checksum":     "sha256 of original code",
}

Pipeline is designed for efficiency:
- One LLM call per file (master prompt, one-shot)
- Streaming JSONL writes (never holds full dataset in memory)
- SHA256 dedup across the full corpus
- Resumable: tracks processed files in a manifest
- Batch-friendly: process N files per run

Backend: Groq API (Llama-3.3-70B, fastest/cheapest) or OpenRouter.
"""
import os
import sys
import json
import time
import hashlib
import logging
import argparse
import tempfile
from pathlib import Path
from typing import Dict, List, Optional, Any, Iterator
from dataclasses import dataclass, field
from datetime import datetime
from threading import Thread
from queue import Queue, Empty
from concurrent.futures import ThreadPoolExecutor, as_completed

import torch
import numpy as np

try:
    import tiktoken
    _HAS_TIKTOKEN = True
except ImportError:
    _HAS_TIKTOKEN = False


# ============================================================================
# LLM BACKENDS
# ============================================================================

class LLMBackend:
    """Abstract LLM backend. Subclass for each provider."""

    def generate(self, prompt: str, **kwargs) -> str:
        raise NotImplementedError

    def name(self) -> str:
        return self.__class__.__name__


class GroqBackend(LLMBackend):
    """Groq API backend using requests.

    Supports models: llama-3.3-70b-versatile, deepseek-r1.
    Set GROQ_API_KEY env var.
    """

    def __init__(self, model: str = "llama-3.3-70b-versatile",
                 api_key: Optional[str] = None,
                 max_tokens: int = 8192,
                 temperature: float = 0.2,
                 timeout: int = 120):
        import requests
        self.model = model
        self.api_key = api_key or os.environ.get("GROQ_API_KEY", "")
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.timeout = timeout
        self._session = requests.Session()
        self._session.headers.update({
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        })

    def name(self) -> str:
        return f"groq-{self.model}"

    def generate(self, prompt: str, **kwargs) -> str:
        import requests
        temperature = kwargs.get("temperature", self.temperature)
        max_tokens = kwargs.get("max_tokens", self.max_tokens)

        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": temperature,
            "max_tokens": max_tokens,
        }
        resp = self._session.post(
            "https://api.groq.com/openai/v1/chat/completions",
            json=payload,
            timeout=self.timeout,
        )
        if resp.status_code != 200:
            raise RuntimeError(
                f"Groq API error {resp.status_code}: {resp.text[:500]}"
            )
        return resp.json()["choices"][0]["message"]["content"]


class OpenRouterBackend(LLMBackend):
    """OpenRouter unified API backend.

    Supports any OpenRouter model:
        anthropic/claude-3.5-sonnet,
        openai/gpt-4o,
        deepseek/deepseek-chat,
        google/gemini-2.0-flash-thinking,
    Set OPENROUTER_API_KEY env var.
    """

    def __init__(self, model: str = "anthropic/claude-3.5-sonnet",
                 api_key: Optional[str] = None,
                 max_tokens: int = 8192,
                 temperature: float = 0.2,
                 timeout: int = 180):
        import requests
        self.model = model
        self.api_key = api_key or os.environ.get("OPENROUTER_API_KEY", "")
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.timeout = timeout
        self._session = requests.Session()
        self._session.headers.update({
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/grisiscomeback",
            "X-Title": "TopoGPT2 Synthetic Data",
        })

    def name(self) -> str:
        return f"openrouter-{self.model}"

    def generate(self, prompt: str, **kwargs) -> str:
        import requests
        temperature = kwargs.get("temperature", self.temperature)
        max_tokens = kwargs.get("max_tokens", self.max_tokens)

        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": temperature,
            "max_tokens": max_tokens,
        }
        resp = self._session.post(
            "https://openrouter.ai/api/v1/chat/completions",
            json=payload,
            timeout=self.timeout,
        )
        if resp.status_code != 200:
            raise RuntimeError(
                f"OpenRouter API error {resp.status_code}: {resp.text[:500]}"
            )
        return resp.json()["choices"][0]["message"]["content"]


class OllamaBackend(LLMBackend):
    """Ollama local inference backend.

    Supports any local model: llama3.1:8b, granite4.1:3b, etc.
    Connects to Ollama server at OLLAMA_HOST (default: http://localhost:11434).
    """

    def __init__(self, model: str = "granite4.1:3b",
                 host: str = "http://localhost:11434",
                 max_tokens: int = 8192,
                 temperature: float = 0.2,
                 timeout: int = 300):
        import requests
        self.model = model
        self.host = host.rstrip("/")
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.timeout = timeout
        self._session = requests.Session()
        self._session.headers.update({"Content-Type": "application/json"})

    def name(self) -> str:
        return f"ollama-{self.model}"

    def generate(self, prompt: str, **kwargs) -> str:
        import requests
        temperature = kwargs.get("temperature", self.temperature)
        max_tokens = kwargs.get("max_tokens", self.max_tokens)

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": temperature,
                "num_predict": max_tokens,
            },
        }
        resp = self._session.post(
            f"{self.host}/api/generate",
            json=payload,
            timeout=self.timeout,
        )
        if resp.status_code != 200:
            raise RuntimeError(
                f"Ollama API error {resp.status_code}: {resp.text[:500]}"
            )
        return resp.json()["response"]


def build_backend(provider: str, model: str) -> LLMBackend:
    """Factory for LLM backends."""
    if provider == "groq":
        return GroqBackend(model=model)
    elif provider == "openrouter":
        return OpenRouterBackend(model=model)
    elif provider == "ollama":
        return OllamaBackend(model=model)
    else:
        raise ValueError(f"Unknown provider: {provider}")


# ============================================================================
# MASTER PROMPT
# ============================================================================

_LANGUAGE_HINTS: Dict[str, str] = {
    ".py": "Python",
    ".c": "C",
    ".h": "C header",
    ".cpp": "C++",
    ".cc": "C++",
    ".go": "Go",
    ".rs": "Rust",
    ".js": "JavaScript",
    ".ts": "TypeScript",
    ".tsx": "TypeScript React",
    ".rb": "Ruby",
    ".java": "Java",
    ".kt": "Kotlin",
    ".swift": "Swift",
    ".cs": "C#",
    ".lua": "Lua",
    ".sh": "Bash shell",
    ".bash": "Bash shell",
    ".r": "R",
    ".scala": "Scala",
    ".clj": "Clojure",
    ".ex": "Elixir",
    ".exs": "Elixir",
    ".erl": "Erlang",
    ".fs": "F#",
    ".hs": "Haskell",
    ".md": "Markdown documentation",
    ".sql": "SQL",
    ".html": "HTML",
    ".css": "CSS",
    ".scss": "SCSS",
    ".xml": "XML",
    ".yaml": "YAML",
    ".yml": "YAML",
    ".toml": "TOML",
    ".json": "JSON",
    ".lua": "Lua",
    ".vim": "Vim script",
    ".asm": "Assembly",
    ".s": "Assembly",
    ".tex": "LaTeX",
}

_SPEC_PROMPT_TEMPLATE = """You are an expert synthetic data generator for training LLMs on code tasks.

Given a source file, generate a high-quality instruction-tuning example following the exact structure below.

--- ORIGINAL SOURCE FILE ---
{file_content}
--- END OF FILE ---

Follow these steps carefully and return ONLY valid JSON (no markdown, no code fences, no explanation outside the JSON):

1. **VAGUE QUESTION**: Create a natural, intermediate-level question that a developer might ask that would lead to building exactly this file. The question should be curious but NOT reveal the solution. Avoid being too specific.

2. **CHAIN OF THOUGHT**: Write a detailed, step-by-step reasoning showing HOW to think through building this. Show the architectural decisions, tradeoffs considered, and implementation strategy. This is your internal reasoning exposed.

3. **SPEC-DRIVEN PROMPT**: Write a comprehensive, professional spec for building this. Include: objectives, functional/non-functional requirements, constraints, expected interfaces, key classes/functions, edge cases.

4. **TASK BREAKDOWN (todo list)**: List the ordered implementation tasks (classes to define, functions to write, tests to add, etc.) that follow the spec.

5. **RESPONSE**: The complete, clean, well-formatted original code. Preserve exact functionality. Add helpful comments where needed.

Return exactly this JSON structure (no keys beyond these, no markdown formatting):
{{
  "instruction": "vague natural question here?",
  "thinking": "detailed chain of thought reasoning here...",
  "spec": "comprehensive spec-driven development prompt here...",
  "todo": ["task 1", "task 2", "task 3", ...],
  "response": "```{lang}\ncomplete original code here\n```"
}}

CRITICAL RULES:
- Return ONLY the JSON object. No markdown fences, no ```json block, no explanatory text.
- The "response" field MUST contain the exact original code (cleaned up, same functionality).
- The "todo" list should have 4-12 tasks.
- The "instruction" must be a question ending with "?"
- All fields must be non-empty strings or non-empty lists.
- Language for response code fence: {lang}
"""


# ============================================================================
# QUALITY VALIDATION
# ============================================================================

def validate_sample(sample: Dict[str, Any]) -> tuple[bool, str]:
    """Validate that a generated sample meets quality bar.

    Returns (is_valid, reason).
    """
    required_fields = ["instruction", "thinking", "spec", "todo", "response"]
    for field in required_fields:
        if field not in sample or not sample[field]:
            return False, f"Missing or empty field: {field}"

    if not isinstance(sample["todo"], list) or len(sample["todo"]) < 2:
        return False, f"todo must be list with >= 2 items, got {type(sample['todo'])}"

    if len(sample["response"]) < 50:
        return False, "response too short"

    instruction = sample["instruction"]
    if not instruction.endswith("?") or len(instruction) < 15:
        return False, f"instruction too short or not a question: {instruction[:50]}"

    if len(sample["thinking"]) < 100:
        return False, "thinking too short (< 100 chars)"

    if len(sample["spec"]) < 100:
        return False, "spec too short (< 100 chars)"

    return True, "ok"


# ============================================================================
# SYNTHETIC DATASET GENERATOR
# ============================================================================

@dataclass
class ProcessedManifest:
    """Tracks processed files for resumability."""
    output_path: str
    seen_hashes: set = field(default_factory=set)
    processed_files: List[str] = field(default_factory=list)
    failed_files: List[str] = field(default_factory=list)
    total_samples: int = 0
    started_at: str = field(default_factory=lambda: datetime.now().isoformat())

    @staticmethod
    def load(path: str) -> 'ProcessedManifest':
        if not os.path.exists(path):
            return ProcessedManifest(output_path="")
        with open(path, 'r', encoding='utf-8') as f:
            d = json.load(f)
        m = ProcessedManifest(output_path=d.get("output_path", ""))
        m.seen_hashes = set(d.get("seen_hashes", []))
        m.processed_files = d.get("processed_files", [])
        m.failed_files = d.get("failed_files", [])
        m.total_samples = d.get("total_samples", 0)
        m.started_at = d.get("started_at", "")
        return m

    def save(self, path: str):
        with open(path, 'w', encoding='utf-8') as f:
            json.dump({
                "output_path": self.output_path,
                "seen_hashes": list(self.seen_hashes),
                "processed_files": self.processed_files,
                "failed_files": self.failed_files,
                "total_samples": self.total_samples,
                "started_at": self.started_at,
            }, f, indent=2)


class SyntheticDatasetGenerator:
    """Generates synthetic instruction-tuning data from source files.

    Pipeline (one LLM call per file):
        file → MASTER_PROMPT → LLM → validate → dedup → JSONL

    Features:
    - Streaming JSONL writes (bounded RAM)
    - SHA256 dedup across corpus
    - Resumable (manifest tracks progress)
    - Threaded request batching for throughput
    - Configurable quality thresholds
    """

    MAX_FILE_SIZE = 48_000   # chars passed to LLM (truncate if bigger)
    MAX_LINES_SHOWN = 600    # for logging
    RETRY_ATTEMPTS = 3
    RETRY_DELAY = 5          # seconds between retries

    def __init__(self,
                 backend: LLMBackend,
                 output_path: str,
                 manifest_path: str,
                 logger: logging.Logger,
                 max_workers: int = 4,
                 max_file_chars: int = MAX_FILE_SIZE):
        self.backend = backend
        self.output_path = output_path
        self.manifest_path = manifest_path
        self.logger = logger
        self.max_workers = max_workers
        self.max_file_chars = max_file_chars

        os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)

        self.manifest = ProcessedManifest.load(manifest_path)
        if not self.manifest.output_path:
            self.manifest.output_path = output_path

        self._write_queue: Queue = Queue(maxsize=500)
        self._writer_done = False
        self._writer_thread = Thread(target=self._jsonl_writer, daemon=True)
        self._writer_thread.start()

    # ------------------------------------------------------------------
    # JSONL writing (background thread)
    # ------------------------------------------------------------------

    def _jsonl_writer(self):
        """Background thread that drains the queue and writes JSONL lines."""
        with open(self.output_path, "a", encoding="utf-8") as f:
            while True:
                try:
                    item = self._write_queue.get(timeout=1.0)
                except Empty:
                    if self._writer_done:
                        break
                    continue
                if item is None:
                    self._write_queue.task_done()
                    break
                line = json.dumps(item, ensure_ascii=False)
                f.write(line + "\n")
                f.flush()
                self._write_queue.task_done()

    def _enqueue_sample(self, sample: Dict[str, Any]):
        self._write_queue.put(sample)

    def _flush_writer(self):
        self._writer_done = True
        self._write_queue.put(None)
        self._writer_thread.join(timeout=10.0)

    # ------------------------------------------------------------------
    # File processing
    # ------------------------------------------------------------------

    def _read_file(self, path: str) -> tuple[str, str]:
        """Read file content and detect language. Truncate if needed."""
        try:
            with open(path, 'r', encoding='utf-8', errors='replace') as f:
                content = f.read()
        except OSError as e:
            return "", ""

        lang = _LANGUAGE_HINTS.get(Path(path).suffix.lower(), "code")
        if len(content) > self.max_file_chars:
            content = content[:self.max_file_chars]
        return content, lang

    def _build_prompt(self, content: str, lang: str) -> str:
        return _SPEC_PROMPT_TEMPLATE.format(
            file_content=content,
            lang=lang,
        )

    def _generate_sample(self, content: str, lang: str) -> Optional[Dict[str, Any]]:
        """Call LLM with retry logic."""
        prompt = self._build_prompt(content, lang)
        last_error = ""

        for attempt in range(self.RETRY_ATTEMPTS):
            try:
                raw = self.backend.generate(prompt)
                raw = raw.strip()

                sample = json.loads(raw)

                is_valid, reason = validate_sample(sample)
                if not is_valid:
                    self.logger.warning(
                        f"Validation failed for {lang} file: {reason}")
                    return None

                sample["lang"] = lang
                sample["checksum"] = hashlib.sha256(
                    content.encode("utf-8", errors="replace")
                ).hexdigest()[:16]
                return sample

            except json.JSONDecodeError as e:
                last_error = f"JSON decode error: {e} | raw[:200]: {raw[:200]}"
                self.logger.warning(f"Attempt {attempt+1} failed: {last_error}")
            except Exception as e:
                last_error = str(e)
                self.logger.warning(f"Attempt {attempt+1} failed: {last_error}")

            if attempt < self.RETRY_ATTEMPTS - 1:
                time.sleep(self.RETRY_DELAY * (attempt + 1))

        self.logger.error(f"All {self.RETRY_ATTEMPTS} attempts failed: {last_error}")
        return None

    def process_file(self, path: str) -> bool:
        """Process a single file. Returns True if a sample was written."""
        content, lang = self._read_file(path)
        if not content:
            return False

        code_hash = hashlib.sha256(
            content.encode("utf-8", errors="replace")
        ).hexdigest()[:16]
        if code_hash in self.manifest.seen_hashes:
            self.logger.debug(f"SHA256 dedup skip: {path}")
            return False

        self.logger.info(f"Generating from: {path}")
        sample = self._generate_sample(content, lang)
        if sample is None:
            self.manifest.failed_files.append(path)
            return False

        sample["file_path"] = path
        self._enqueue_sample(sample)

        self.manifest.seen_hashes.add(code_hash)
        self.manifest.processed_files.append(path)
        self.manifest.total_samples += 1
        self.manifest.save(self.manifest_path)

        if self.manifest.total_samples % 50 == 0:
            self.logger.info(
                f"Progress: {self.manifest.total_samples:,} samples, "
                f"{len(self.manifest.processed_files):,} files processed, "
                f"{len(self.manifest.failed_files):,} failed")

        return True

    def process_batch(self, paths: list[str]) -> Dict[str, int]:
        """Process a batch of files in parallel using thread pool."""
        results = {"processed": 0, "skipped": 0, "failed": 0}

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            future_to_path = {
                executor.submit(self.process_file, p): p for p in paths
            }
            for future in as_completed(future_to_path):
                path = future_to_path[future]
                try:
                    ok = future.result()
                    if ok:
                        results["processed"] += 1
                    else:
                        results["skipped"] += 1
                except Exception as e:
                    self.logger.error(f"Exception processing {path}: {e}")
                    results["failed"] += 1

        return results

    def finish(self) -> Dict[str, Any]:
        """Signal end of processing and flush writer."""
        self._flush_writer()
        stats = {
            "output_path": self.output_path,
            "total_samples": self.manifest.total_samples,
            "processed_files": len(self.manifest.processed_files),
            "failed_files": len(self.manifest.failed_files),
            "dedup_skipped": sum(1 for p in self.manifest.processed_files
                                  if self.manifest.seen_hashes and True),
            "manifest_path": self.manifest_path,
        }
        self.logger.info(
            f"Dataset generation complete. "
            f"Samples: {stats['total_samples']:,} | "
            f"Files processed: {stats['processed_files']:,} | "
            f"Failed: {stats['failed_files']:,}")
        return stats


# ============================================================================
# STANDALONE CLI
# ============================================================================

def build_logger(level: str = "INFO") -> logging.Logger:
    logger = logging.getLogger("SyntheticDS")
    logger.setLevel(getattr(logging, level.upper(), logging.INFO))
    if not logger.handlers:
        h = logging.StreamHandler(sys.stdout)
        h.setFormatter(logging.Formatter(
            "%(asctime)s %(levelname)s %(message)s"))
        logger.addHandler(h)
    return logger


def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate synthetic code instruction-tuning dataset")
    parser.add_argument("--paths", type=str, default="",
                        help="Comma-separated list of file paths to process")
    parser.add_argument("--paths-file", type=str, default="",
                        help="File containing one absolute path per line")
    parser.add_argument("--output", type=str, default="data/synthetic_dataset.jsonl",
                        help="Output JSONL path")
    parser.add_argument("--manifest", type=str, default="data/synthetic_manifest.json",
                        help="Resumability manifest path")
    parser.add_argument("--provider", type=str, default="groq",
                        choices=["groq", "openrouter"],
                        help="LLM provider")
    parser.add_argument("--model", type=str, default="llama-3.3-70b-versatile",
                        help="Model name for the provider")
    parser.add_argument("--max-workers", type=int, default=4,
                        help="Parallel file processing threads")
    parser.add_argument("--max-files", type=int, default=0,
                        help="Max files to process (0 = all)")
    parser.add_argument("--log", type=str, default="INFO",
                        choices=["DEBUG", "INFO", "WARNING", "ERROR"])
    parser.add_argument("--api-key", type=str, default="",
                        help="API key (or set GROQ_API_KEY / OPENROUTER_API_KEY env)")
    return parser.parse_args()


def load_paths(paths_arg: str, paths_file: str, max_files: int
               ) -> List[str]:
    """Load file paths from CLI args or file."""
    if paths_file:
        with open(paths_file, 'r', encoding='utf-8') as f:
            paths = [line.strip() for line in f if line.strip()]
    elif paths_arg:
        paths = [p.strip() for p in paths_arg.split(',') if p.strip()]
    else:
        raise ValueError("Provide --paths or --paths-file")
    if max_files > 0:
        paths = paths[:max_files]
    return paths


def main():
    args = parse_args()
    logger = build_logger(args.log)

    if not args.api_key:
        if args.provider == "groq":
            key = os.environ.get("GROQ_API_KEY", "")
        else:
            key = os.environ.get("OPENROUTER_API_KEY", "")
        if not key:
            logger.error(f"No API key. Set GROQ_API_KEY or OPENROUTER_API_KEY env var.")
            sys.exit(1)

    backend = build_backend(args.provider, args.model)
    logger.info(f"Using backend: {backend.name()}")

    paths = load_paths(args.paths, args.paths_file, args.max_files)
    logger.info(f"Files to process: {len(paths):,}")

    gen = SyntheticDatasetGenerator(
        backend=backend,
        output_path=args.output,
        manifest_path=args.manifest,
        logger=logger,
        max_workers=args.max_workers,
    )

    logger.info(f"Processing with {args.max_workers} workers...")
    for i in range(0, len(paths), 100):
        batch = paths[i:i+100]
        results = gen.process_batch(batch)
        logger.info(
            f"Batch {i//100+1}: processed={results['processed']} "
            f"skipped={results['skipped']} failed={results['failed']}")

    stats = gen.finish()
    print(f"\nDone. {stats['total_samples']:,} samples -> {stats['output_path']}")


if __name__ == "__main__":
    main()