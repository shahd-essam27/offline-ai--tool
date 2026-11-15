# Week 4 — Local LLMs & Open-Source Tooling

> **Learning track:** Helwan Career Center — 12-Week Industry Roadmap  
> **Week:** 4  
> **Difficulty:** Intermediate  
> **Theme:** Run language models locally, understand hardware and model trade-offs, and build an offline-first AI tool.

## Project Objective

Learn to run open models on your own computer with **Ollama** and **LM Studio**, integrate local models into Python, compare their performance, and build an **Offline-First AI Tool** that can optionally use a hosted model.

**Learning approach:** Build every lab yourself. Use the tasks below as instructions, record findings, and ask for hints or code review when needed. This README intentionally avoids complete implementations.

## Milestone Tracker

| Milestone | Focus | Roadmap requirement | Status |
| --- | --- | --- | --- |
| **0** | Understand all concepts | LO 4.1–4.5 and topics covered | ⬜ Not started |
| **1** | Ollama setup and model comparison | Lab 4.1 | ⬜ Not started |
| **2** | Local API with Python | Lab 4.2 | ⬜ Not started |
| **3** | LM Studio and GGUF benchmark | Lab 4.3 | ⬜ Not started |
| **4** | Hosted/local configuration | Lab 4.4 | ⬜ Not started |
| **5** | Build the offline-first tool | Mini Project 4 | ⬜ Not started |
| **6** | Evaluation and portfolio documentation | Assignment outputs and portfolio note | ⬜ Not started |

---

## Milestone 0 — Understand All Concepts

**Goal:** Understand the *why* and *how* before installing or building anything.

### Tasks

- [x] **Task 0.1 — Local LLM foundations:** Explain what a local LLM is, what inference means, and how local inference differs from a hosted API.
- [x] **Task 0.2 — Ollama basics:** Learn what Ollama does and what pulling a model, `run`, `serve`, its local API, and a Modelfile mean.
- [x] **Task 0.3 — LM Studio basics:** Explain its graphical model browser, downloader, chat interface, and local server mode; compare it with Ollama.
- [x] **Task 0.4 — Model formats and quantization:** Understand FP16, 8-bit, 4-bit, GGUF, and the effect of quantization on size, memory, speed, and quality (no derivations needed).
- [x] **Task 0.5 — Model families:** Research Llama, Qwen, Gemma, Mistral, Phi, and gpt-oss. Learn how to compare model size, task suitability, and licensing rather than memorizing rankings.
- [x] **Task 0.6 — Hardware budgeting:** Learn the difference between RAM, VRAM, disk space, CPU, and GPU; understand why model size and context length affect feasibility.
- [x] **Task 0.7 — OpenAI-compatible endpoints:** Understand `localhost`, ports, `base_url`, model identifiers, and why an application can target different providers using similar request formats.
- [x] **Task 0.8 — Model selection and deployment trade-offs:** Compare privacy, cost, latency, offline access, response quality, and license restrictions.
- [x] **Task 0.9 — Knowledge check:** Explain LO 4.1 through LO 4.5 in your own words and answer a short self-quiz.

### Completion Criteria

- [x] I can explain every topic above without relying on copied definitions.
- [x] I can describe how a prompt travels through a local application to a model and back.
- [x] I can explain why a 4-bit GGUF model may fit hardware that cannot run an FP16 version.
- [x] I can state when local inference is preferable and when hosted inference is preferable.
- [x] I can describe how I would select a model for a given task and machine.

**Evidence:** `notes/milestone_0_concepts.md` (your own explanations, comparison, and quiz answers).

---

## Milestone 1 — Install Ollama and Chat with Two Models

**Maps to:** Lab 4.1

### Tasks

- [ ] **Task 1.1 — Inspect your machine:** Record operating system, installed RAM, GPU/VRAM (if any), and available disk space.
- [ ] **Task 1.2 — Install and verify Ollama:** Use official instructions appropriate for your OS. Confirm that it is available in your terminal.
- [ ] **Task 1.3 — Select two models:** Choose one small and one mid-size model based on your hardware, task quality needs, and license. Record identifiers and download sizes. *Mid-size is relative to available hardware; do not force a model that cannot fit.*
- [ ] **Task 1.4 — Pull the small model:** Download it and confirm that Ollama recognizes it.
- [ ] **Task 1.5 — Chat from the terminal:** Send a small set of repeatable prompts and save observations.
- [ ] **Task 1.6 — Pull and test the mid-size model:** Use the same prompts and note memory/performance differences.
- [ ] **Task 1.7 — Compare results:** Record which model gave more useful answers and which ran more comfortably.

### Completion Criteria

- [ ] Ollama works on my computer.
- [ ] I can launch each of the two models from the terminal.
- [ ] Both models respond to comparable prompts.
- [ ] I have documented the chosen models, hardware, and qualitative differences.

**Evidence:** `labs/lab_4_1/README.md` with setup notes, prompt examples, observations, and optional screenshots.  
**Checkpoint:** Do not move on until both models have been tested, or a hardware limitation has been documented and discussed.

---

## Milestone 2 — Connect Python to the Ollama Local API

**Maps to:** Lab 4.2

### Tasks

- [ ] **Task 2.1 — Understand the architecture:** Sketch Python client → local HTTP endpoint → Ollama → model → response.
- [ ] **Task 2.2 — Prepare Python:** Create or activate a virtual environment in VS Code; install only required packages; begin tracking dependencies in `requirements.txt`.
- [ ] **Task 2.3 — Check the local server:** Confirm the Ollama API is reachable on your machine.
- [ ] **Task 2.4 — Build a minimal Python client:** Use an OpenAI-compatible client with a local `base_url` and a locally installed model identifier.
- [ ] **Task 2.5 — Inspect the response:** Display the answer, identify relevant response fields, and handle a failed connection or missing model cleanly.
- [ ] **Task 2.6 — Test and document:** Compare terminal and Python calls for the same prompt.

### Completion Criteria

- [ ] A Python script calls a local model successfully.
- [ ] The application does not need a paid API key to make its local call.
- [ ] I understand the role of the endpoint, model name, and client library.
- [ ] A predictable failure displays a useful error rather than a confusing crash.

**Evidence:** Your own script under `labs/lab_4_2/`, plus short usage and test notes.

---

## Milestone 3 — LM Studio and GGUF Benchmarking

**Maps to:** Lab 4.3

### Tasks

- [ ] **Task 3.1 — Install LM Studio:** Confirm it opens and locate the model browser and chat interface.
- [ ] **Task 3.2 — Choose a GGUF model:** Inspect available quantizations, licenses, file sizes, and RAM/VRAM suitability.
- [ ] **Task 3.3 — Download and run:** Start chatting locally with the selected model.
- [ ] **Task 3.4 — Benchmark:** Use repeatable prompts, note generation tokens/sec as reported by the tool, and distinguish it from initial loading or prompt-processing time where possible.
- [ ] **Task 3.5 — Compare:** Record quality, response speed, and resource use; explain how quantization may affect results.
- [ ] **Task 3.6 — Explore server mode:** Find LM Studio's local server interface and explain how it resembles the Ollama endpoint.

### Completion Criteria

- [ ] A downloaded GGUF model responds in LM Studio.
- [ ] I have at least one recorded tokens/sec measurement with the model and quantization specified.
- [ ] I can explain the memory/performance/quality trade-offs I observed.

**Evidence:** `benchmarks/lm_studio_results.md` with machine specs, model, quantization, test prompt(s), methodology, tokens/sec, and quality notes.

---

## Milestone 4 — Switch Week 3 Code Between Hosted and Local Models

**Maps to:** Lab 4.4

### Tasks

- [ ] **Task 4.1 — Review Week 3 work:** Identify the Python code that currently sends prompts to a hosted model. If a microservice was not built in Week 3, first extract the smallest reusable request interface from the code you do have; document the difference from the roadmap's microservice requirement.
- [ ] **Task 4.2 — Isolate configuration:** Decide how a single mode flag selects a hosted or local backend.
- [ ] **Task 4.3 — Define a common request/response contract:** Keep the calling application independent of backend-specific details.
- [ ] **Task 4.4 — Implement the local path:** Connect the existing request flow to Ollama.
- [ ] **Task 4.5 — Preserve the hosted path:** Retain the Week 3 provider and its required credentials; never commit API keys.
- [ ] **Task 4.6 — Verify both configurations:** Run matching test prompts against each backend and record differences. Where client compatibility permits, change only the `base_url` and configuration values; note provider-specific incompatibilities honestly.

### Completion Criteria

- [ ] A single configuration option selects hosted or local inference.
- [ ] Switching does not require edits to the application's task logic.
- [ ] Both paths have been tested (subject to hosted-service availability).
- [ ] No credentials are stored in source code or committed files.

**Evidence:** Refactored Week 3 code or a clearly labeled adaptation in `labs/lab_4_4/`, with configuration and test instructions.

---

## Milestone 5 — Mini Project 4: Offline-First AI Tool

**Maps to:** Weekly assignment

**Required outcome:** Build a CLI or small app that works fully offline using a local model through Ollama, with an optional flag for a hosted API to improve quality.

> Pick your own use case. The roadmap offers examples (offline note summarizer, private journaling assistant, on-device code explainer, local FAQ bot), but you do **not** have to select any of those.

### Tasks

- [ ] **Task 5.1 — Define the problem:** State the intended user, what the tool accepts, and what it should return.
- [ ] **Task 5.2 — Specify acceptance tests:** Define at least three realistic test cases and expected behavior before coding.
- [ ] **Task 5.3 — Design components:** Sketch input → preprocessing → local/hosted inference → output. Keep inference separate from app logic.
- [ ] **Task 5.4 — Implement an offline-first CLI or small app:** Make the core task work with Ollama while the internet is disconnected (after models and dependencies are installed).
- [ ] **Task 5.5 — Add the optional hosted flag:** Keep the local model as the normal/default option; require credentials only for hosted mode.
- [ ] **Task 5.6 — Validate and handle errors:** Cover invalid inputs, unavailable model/server, and hosted configuration errors.
- [ ] **Task 5.7 — Perform real tests:** Run the acceptance cases locally and, where available, with hosted inference.

### Completion Criteria

- [ ] The app solves its stated task.
- [ ] Core functionality works with internet disabled after initial setup.
- [ ] An optional flag can select the hosted backend.
- [ ] At least three documented acceptance tests pass.
- [ ] The code is written and understood by me.

**Evidence:** Working code in `final_project/`, instructions, example input/output, and test notes.

---

## Milestone 6 — Benchmark, Justify, Document, and Publish

**Maps to:** Required assignment outputs + portfolio note

### Tasks

- [ ] **Task 6.1 — Benchmark local behavior:** Record model identifier, quantization (if applicable), tokens/sec, prompt(s), hardware, and test conditions.
- [ ] **Task 6.2 — Evaluate output quality:** Define a simple task-specific rubric and apply it to a small, consistent evaluation set.
- [ ] **Task 6.3 — Justify model choice:** Explain trade-offs among hardware fit, license, quality, latency, privacy, and cost.
- [ ] **Task 6.4 — Compare local and hosted modes:** Note the practical advantages and limits of each using evidence rather than assumptions.
- [ ] **Task 6.5 — Polish GitHub documentation:** Add requirements, setup, usage, folder descriptions, limitations, and reproducible testing instructions.
- [ ] **Task 6.6 — Record a short demo:** Show the tool operating locally and explain what makes it offline-first.
- [ ] **Task 6.7 — Review before publishing:** Remove secrets, local virtual environments, unnecessary large model files, and personal/private example data; verify `.gitignore`.

### Completion Criteria

- [ ] Working local app and optional hosted mode are documented.
- [ ] Benchmark note includes **model, tokens/sec, and quality**.
- [ ] Model choice is justified in writing.
- [ ] A short screen demo is available.
- [ ] The repository can be understood and reproduced by someone else.

**Evidence:** `benchmarks/final_benchmark.md`, `docs/model_choice.md`, demo link, and completed README.

---

## Suggested Repository Structure

```text
week4-local-llms/
├── README.md
├── .gitignore
├── requirements.txt              # Create once dependencies are selected
├── notes/
│   └── milestone_0_concepts.md
├── labs/
│   ├── lab_4_1/
│   ├── lab_4_2/
│   ├── lab_4_3/
│   └── lab_4_4/
├── final_project/
│   └── README.md
├── benchmarks/
│   ├── lm_studio_results.md
│   └── final_benchmark.md
└── docs/
    └── model_choice.md
```

This is a **proposed** structure, not a claim that these files already exist. Add files when you reach the corresponding task. Keep the virtual environment, API credentials, and downloaded model weights out of Git.

## How to Work Through the Milestones

1. Complete **one task at a time**, starting with Milestone 0, Task 0.1.
2. Explain the relevant concept or demonstrate the result yourself.
3. Ask for **a hint, a review, or debugging help** when stuck; request a complete solution only when you want one.
4. Update the task checkbox once its evidence and completion criteria are satisfied.
5. Advance only after a milestone's completion checklist is met.

## Week 4 Learning Outcomes Coverage

| Roadmap learning outcome | Where demonstrated |
| --- | --- |
| **LO 4.1:** Install/run open models with Ollama and LM Studio; expose compatible endpoint | Milestones 0–3 |
| **LO 4.2:** Understand quantization and GGUF size/VRAM trade-offs | Milestones 0 and 3 |
| **LO 4.3:** Select a model for hardware, license, and quality | Milestones 0, 1, 3, and 6 |
| **LO 4.4:** Switch between local and hosted model via configuration/base URL | Milestones 2, 4, and 5 |
| **LO 4.5:** Explain local vs hosted trade-offs | Milestones 0, 5, and 6 |

## Source and Learning Resources

The requirements above are based on **Week 4 — Local LLMs & Open-Source Tooling**, pages 12–13 of the *Helwan Career Center — 12-Week Industry Roadmap*. The milestone breakdown, checklists, folder structure, and proposed evidence are additional project-management guidance.

- [Ollama documentation](https://docs.ollama.com/)
- [Ollama model library](https://ollama.com/library)
- [Ollama OpenAI compatibility](https://docs.ollama.com/openai)
- [LM Studio](https://lmstudio.ai/)
- [LM Studio documentation](https://lmstudio.ai/docs)

The roadmap also recommends freeCodeCamp's Ollama course and Arabic material from Abu Bakr Soliman (bakrianoo).

---

**Current starting point:** Milestone 0 → Task 0.1: Local LLM foundations.
