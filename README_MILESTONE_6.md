# Milestone 6 — Benchmark, Justify, Document, and Publish

**Status:** Evaluation materials ready; live benchmarks, screen demo and final verification remain pending.

This milestone delivers the Week 4 roadmap's benchmark note, model justification, reproducible evaluation helper and screen-demo instructions for the Offline-First Note Summarizer.

## Files

- `benchmarks/final_benchmark.md`: recorded earlier 3B/7B speed results and quality observations, plus a new test rubric.
- `tools/benchmark_ollama.py`: local-only benchmark runner using Ollama's API timing counters.
- `tests/test_benchmark_ollama.py`: offline unit tests for throughput calculations.
- `docs/model_choice.md`: selection rationale, license/privacy/cost trade-offs.
- `docs/demo_guide.md`: short screen-recording instructions; not a video.
- `docs/release_checklist.md`: honest finalization checklist.

## Quick start

From `E:\offline-ai-tool`, activate your existing `.venv`, ensure Ollama and Qwen2.5 models are installed, then run:

```powershell
python -m unittest discover -s tests -p "test_*.py" -v
python tools/benchmark_ollama.py --model qwen2.5:3b --runs 2 --output benchmarks/local_3b_results.json
```

The benchmark runner contacts `http://127.0.0.1:11434`, **not Gemini**. Its JSON results are generated only after a real local model run.

The script uses a fixed short quantization prompt for comparability and measures generated tokens/sec from Ollama's duration counters. Review model responses manually for factual correctness.

## Outstanding

Live benchmark results, fully offline mini-project run, LM Studio 4.3, hosted matching comparison and an actual demo video have not been performed by this package. No API calls or real model inference have been fabricated.
