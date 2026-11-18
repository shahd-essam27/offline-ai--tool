"""Measure local Ollama generation speed without contacting a hosted API.

Run from the repository root:
    python tools/benchmark_ollama.py --model qwen2.5:3b --runs 2

Uses Ollama's native API counters instead of estimating tokens from wall time.
"""

import argparse
import json
import statistics
import urllib.error
import urllib.request
from pathlib import Path

DEFAULT_PROMPT = (
    "Explain what quantization does for a local language model in exactly two sentences."
)


def calculate_metrics(payload):
    """Return metrics from Ollama's nanosecond timings; tolerate zero-token replies."""
    generated = int(payload.get("eval_count") or 0)
    evaluation_ns = int(payload.get("eval_duration") or 0)
    total_ns = int(payload.get("total_duration") or 0)
    tokens_per_sec = (generated * 1e9 / evaluation_ns) if evaluation_ns > 0 else None
    return {
        "generated_tokens": generated,
        "generation_tokens_per_sec": round(tokens_per_sec, 2) if tokens_per_sec is not None else None,
        "total_seconds": round(total_ns / 1e9, 3),
        "answer": payload.get("response", ""),
    }


def run_once(model, prompt, endpoint="http://127.0.0.1:11434/api/generate"):
    """Call locally installed Ollama; stream=False includes final timing metrics."""
    request_body = json.dumps({
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {"num_predict": 120, "temperature": 0},
    }).encode("utf-8")
    request = urllib.request.Request(
        endpoint,
        data=request_body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=180) as response:
        return calculate_metrics(json.load(response))


def main():
    parser = argparse.ArgumentParser(description="Local Ollama speed benchmark")
    parser.add_argument("--model", default="qwen2.5:3b")
    parser.add_argument("--runs", type=int, default=2)
    parser.add_argument("--prompt", default=DEFAULT_PROMPT)
    parser.add_argument("--output", type=Path, help="Optional JSON output path")
    args = parser.parse_args()
    if args.runs < 1 or args.runs > 10:
        parser.error("--runs must be from 1 to 10")

    results = []
    try:
        for number in range(1, args.runs + 1):
            result = run_once(args.model, args.prompt)
            results.append(result)
            print(f"Run {number}: {result['generation_tokens_per_sec']} tokens/sec; "
                  f"{result['total_seconds']} s; {result['generated_tokens']} generated tokens")
    except urllib.error.HTTPError as exc:
        raise SystemExit(f"Ollama returned HTTP {exc.code}. Check 'ollama list' and the model name.") from None
    except (urllib.error.URLError, TimeoutError) as exc:
        raise SystemExit(f"Cannot reach local Ollama: {exc}. Start Ollama and retry.") from None

    valid_speeds = [r["generation_tokens_per_sec"] for r in results if r["generation_tokens_per_sec"] is not None]
    report = {
        "model": args.model,
        "prompt": args.prompt,
        "temperature": 0,
        "max_generated_tokens": 120,
        "results": results,
        "mean_generation_tokens_per_sec": round(statistics.mean(valid_speeds), 2) if valid_speeds else None,
    }
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"Saved to {args.output}")
    print("Mean generated tokens/sec:", report["mean_generation_tokens_per_sec"])
    print("Review answers manually for factual accuracy; speed alone is not quality.")


if __name__ == "__main__":
    main()
