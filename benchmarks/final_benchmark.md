# Week 4 — Local LLM Benchmark and Evaluation

**Status:** Historical benchmark recorded; new controlled benchmark and application end-to-end trial pending.

## Hardware and conditions

- Windows laptop; Intel Core i7-1165G7, 16 GB RAM, NVIDIA MX350 (2 GB dedicated VRAM).
- Ollama model inference, largely CPU-bound on the previously observed 7B run.
- Models: `qwen2.5:3b` and `qwen2.5:7b` (Ollama local install).
- 3B was observed using Q4_K_M, ~1.9 GB; 7B ~4.7 GB, confirm its exact quantization via `ollama show qwen2.5:7b` before recording it.

## Earlier Lab 4.1 runs (observed, not rerun for Milestone 6)

| Model | Generated tokens | Generation speed | Total runtime | Observations |
|---|---:|---:|---:|---|
| `qwen2.5:3b` | 94 | **15.10 tokens/sec** | 7.25 s | More responsive for laptop use |
| `qwen2.5:7b` | 198 | **6.88 tokens/sec** | 30.91 s | Slower, longer output in this run |

**Caution:** Not a controlled head-to-head latency comparison because generation lengths and settings differed. Token speeds were reported by Ollama, not estimated from total runtime.

## Previous quality observations

- Both models answered the 17-sheep reasoning problem correctly (9 remain).
- Both passed six tested cases for a second-largest-distinct-integer coding question.
- Both received roughly 4/5 accuracy and 5/5 clarity in an earlier attention explanation review.
- Qwen2.5 3B also produced several incorrect GGUF definitions during later Lab 4.4 trials. This illustrates hallucination risk.
- Gemini succeeded in earlier hosted tests, but the later matching GGUF prompt ended in HTTP 503, so there is **no completed matched-prompt Gemini comparison** yet.

## New reproducible local benchmark — run on your laptop

From repository root, with Ollama running and the model installed:

```powershell
python tools/benchmark_ollama.py --model qwen2.5:3b --runs 2 --output benchmarks/local_3b_results.json
python tools/benchmark_ollama.py --model qwen2.5:7b --runs 2 --output benchmarks/local_7b_results.json
```

The script uses Ollama `/api/generate` with `stream=false` to collect `eval_count`, `eval_duration` and `total_duration`. It calculates **generated tokens/sec = eval_count × 1e9 / eval_duration (nanoseconds)**. Runs use a fixed prompt, `temperature=0`, and at most 120 generated tokens. Cache/warmup, power mode, model loading and CPU/GPU offloading can still affect results.

| Model | New mean tokens/sec | Key correct facts | Hallucinations | Followed instructions? |
|---|---|---|---|---|
| Qwen2.5 3B | Pending | Pending | Pending | Pending |
| Qwen2.5 7B | Pending | Pending | Pending | Pending |

## Mini-project end-to-end evaluation (pending actual execution)

Test `final_project/sample_notes.txt` and rate summaries with the same rubric. Record whether the application runs with Wi-Fi disabled *after dependencies and models are installed*.

| Criterion | Score guide |
|---|---|
| Accuracy | 0 = made-up key claims; 1 = mixed; 2 = faithful |
| Coverage | 0 = major details missing; 1 = partial; 2 = key details present |
| Concision | 0 = rambling; 1 = okay; 2 = concise |
| Instructions | 0 = wrong output; 1 = partial; 2 = requested structure |

**Total:** /8, assessed manually for each model. Save anonymized sample output and note any factual errors.

## LM Studio / GGUF and hosted comparison

- LM Studio benchmark: **pending Milestone 3**; do not invent tokens/sec.
- Hosted matched-prompt result: **blocked by prior HTTP 503**. Don't count the failure as a quality comparison.
