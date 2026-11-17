# Lab 4.1 — Run and Compare Two Local LLMs with Ollama

> **Week 4: Local LLMs & Open-Source Tooling**  
> **Milestone 1: Install Ollama and Chat with Two Models**  
> **Status:** Model installation, prompts, code tests and a first performance run completed; the measurements below reflect **one run per model**, not statistical averages.

## Objective

Run two quantized instruction-following models locally with Ollama and compare answer quality, Python code correctness, model footprint, generation throughput, and runtime behavior on the same laptop.

## Hardware and environment

| Item | Configuration |
|---|---|
| OS | Windows 11 25H2 |
| CPU | Intel Core i7-1165G7 |
| System RAM | 16 GB |
| Integrated GPU | Intel Iris Xe Graphics (shared system RAM) |
| Dedicated GPU | NVIDIA GeForce MX350, 2 GB dedicated VRAM |
| Project location | `E:\offline-ai-tool` |
| Ollama model store | `E:\OllamaModels` via `OLLAMA_MODELS` |
| Ollama version | 0.40.16 |
| Small model | `qwen2.5:3b` — 3.1B-class, Q4_K_M, ~1.9 GB download |
| Mid-size model | `qwen2.5:7b` — 7B-class, Q4_K_M, ~4.7 GB download |

The 7B model's runtime footprint reported by `ollama ps` was **5.2 GB** with **4096 context** and **96% CPU / 4% GPU**. This is the model's loaded footprint/processor distribution as reported by Ollama, **not** a measurement of total system RAM use or dedicated VRAM usage.

## Setup and verification

The models were pulled using Ollama, after setting the model storage path to `E:\OllamaModels` to avoid filling the nearly-full C: drive.

```powershell
ollama --version
ollama list
ollama pull qwen2.5:3b
ollama pull qwen2.5:7b
```

For each chat experiment, use a clean chat session (exit with `/bye`); unload the other model using `ollama stop <model>` when benchmarking to reduce contention. `ollama ps` checks which model is currently loaded.

## Evaluation prompts and qualitative findings

Both models received the **same wording** for each of the following prompts. Qualitative ratings are reviewer judgments based on this small sample.

### Test 1 — Technical explanation

**Prompt:**

> Explain the attention mechanism in Transformers to a beginner. Use a simple example, avoid mathematical equations, and keep your answer under 150 words.

| Criterion | Qwen2.5 3B | Qwen2.5 7B |
|---|---|---|
| Technical accuracy (suggested) | 4/5 | 4/5 |
| Beginner clarity (suggested) | 5/5 | 5/5 |
| Instruction following (suggested) | 5/5 | 5/5 |
| Main analogy | Spotlight on important parts of a story | Finding references to a character named Alex |
| Observation | Concise, intuitive; oversimplifies attention as selecting relevant question parts | More elaborated example; misleading suggestion that standard self-attention need not look across the sequence |

**Interpretation:** Both answers were understandable; the larger model did not clearly improve technical precision on this single prompt.

### Test 2 — Python coding

**Prompt:**

> Write a Python function that takes a list of integers and returns the second-largest distinct number. Handle duplicate values and lists with fewer than two distinct numbers. Explain your approach briefly.

Both generated functions removed duplicates with `set()`, sorted values in descending order, and returned the second entry or `None` where fewer than two unique values existed. Both had general-case time complexity approximately **O(n log n)**; this is a valid solution, though a one-pass algorithm could avoid sorting.

| Input | Expected | 3B observed | 7B observed |
|---|---:|---:|---:|
| `[10, 20, 20, 30]` | `20` | `20` | `20` |
| `[10, 20]` | `10` | `10` | `10` |
| `[5, 5, 5]` | `None` | `None` | `None` |
| `[-10, -3, -7]` | `-7` | `-7` | `-7` |
| `[]` | `None` | `None` | `None` |
| `[100, 100, 99, 98]` | `99` | `99` | `99` |

**Result:** **6/6 test cases passed for each model.** These tests do not prove correctness for every possible input.

### Test 3 — Logical reasoning

**Prompt:**

> A farmer has 17 sheep. All but 9 run away. How many sheep does the farmer have left? Explain your answer briefly.

| Result | Qwen2.5 3B | Qwen2.5 7B |
|---|---|---|
| Answer | 9 sheep (correct) | 9 sheep (correct) |
| Explanation | Correct but somewhat wordy | Correct and concise |

## Performance benchmark

**Common prompt:**

> Explain five practical differences between running a language model locally and using a hosted API. Give one sentence for each difference.

**Method:** Each model was run using `ollama run <model> --verbose` and the same prompt, on the same laptop, in separate runs. The other model was unloaded for benchmarking. The two answers had different token counts, so **total duration is not a pure measure of throughput**. Model and runner state may be warm; results are not an average over repeated trials.

### Exact recorded metrics

| Metric | Qwen2.5 3B | Qwen2.5 7B |
|---|---:|---:|
| Model download size | ~1.9 GB | ~4.7 GB |
| Total duration | **7.2509013 s** | **30.9071122 s** |
| Load duration | 2.5716 ms | 155.1521 ms |
| Prompt evaluation count | 53 tokens | 53 tokens |
| Prompt evaluation duration | 1.017241 s | 1.970278 s |
| Prompt evaluation rate | 52.10 tokens/s | 26.90 tokens/s |
| Generated tokens (`eval count`) | 94 | 198 |
| Generation duration (`eval duration`) | 6.227096 s | 28.761813 s |
| Generation rate (`eval rate`) | **15.10 tokens/s** | **6.88 tokens/s** |
| `ollama ps` loaded size | Not recorded | 5.2 GB |
| `ollama ps` CPU / GPU placement | Not recorded | 96% / 4% |
| `ollama ps` context setting | Not recorded | 4096 tokens |
| `ollama ps` runner | Not recorded | `llamacpp` |

> **Metric caution:** Total duration, load duration, prompt evaluation duration, and evaluation duration may include different accounting boundaries; do not reconstruct total duration by simply summing the individual numbers. The precise values above are transcribed from Ollama's `--verbose` output.

### Graph 1 — Total response duration

![Total response duration for Qwen2.5 3B (7.25 s) and Qwen2.5 7B (30.91 s)](benchmark_total_duration.png)

The 7B response took **about 4.26×** as long in this run, but it also generated **198 versus 94 tokens**.

### Graph 2 — Generation speed

![Generation speed: Qwen2.5 3B at 15.10 tokens/sec and Qwen2.5 7B at 6.88 tokens/sec](benchmark_generation_speed.png)

Qwen2.5 3B produced tokens **about 2.19× as fast** as Qwen2.5 7B during the recorded generation phases.

### Graph 3 — Generated output length

![Generated tokens: 94 for Qwen2.5 3B and 198 for Qwen2.5 7B](benchmark_output_tokens.png)

The longer 7B response is one reason its **total duration** is not directly comparable without controlling output length.

## Conclusions and trade-offs

- **Quality on these tasks:** Both models explained attention reasonably, generated code passing all six checks, and answered the reasoning question correctly. No clear accuracy advantage for 7B was observed on this small benchmark.
- **Speed on this laptop:** 3B generated at 15.10 tokens/s versus 6.88 tokens/s for 7B; for simple, latency-sensitive tasks, 3B was more responsive.
- **Memory and compute:** 7B showed a 5.2 GB loaded footprint at 4096 context and ran **mostly on CPU** (96% CPU, 4% GPU), consistent with the 2 GB dedicated GPU memory constraint.
- **Storage:** The 7B download occupied substantially more disk space than the 3B download. Model downloads were configured to use the E: drive.
- **Limitations:** Each model was benchmarked once on this prompt; the outputs differed in length; full-system RAM and VRAM metrics were not captured for both models. A more rigorous study would repeat runs, keep sampling parameters/context consistent, compare median throughput, and use a larger question set.

## Reproducing this lab

1. Install Ollama for your operating system; point `OLLAMA_MODELS` at a drive with adequate free space before downloading large weights.
2. Pull `qwen2.5:3b` and `qwen2.5:7b` and check with `ollama list`.
3. In the terminal, run each model with `ollama run <model>`, send the three exact evaluation prompts above, and test any generated Python function independently.
4. For timing, use `ollama run <model> --verbose` with the shared benchmark prompt, unload the other model with `ollama stop <model>`, and inspect placement with `ollama ps`.
5. Record your own output, metrics, and hardware information. Results will vary across machines, settings, and model versions.

## Evidence and milestone status

- [x] 1.1 Inspect hardware and available disk space
- [x] 1.2 Install and verify Ollama
- [x] 1.3 Select small and mid-size models
- [x] 1.4 Pull the small model
- [x] 1.5 Chat and evaluate the small model
- [x] 1.6 Pull and evaluate the mid-size model
- [x] 1.7 Compare qualitative results and measured performance

**Lab 4.1 complete.** The root project's `README.md` should be updated once at the end of the milestone, per the project workflow. The independent local Python API exercise belongs to Lab 4.2, not Lab 4.1.
