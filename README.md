# Week 4 — Local LLMs & Open-Source Tooling

> **Learning track:** Helwan Career Center — 12-Week Industry Roadmap  
> **Week:** 4  
> **Difficulty:** Intermediate  
> **Theme:** Run language models locally, understand hardware and model trade-offs, and build an offline-first AI tool.

## Project Objective

Learn to run open models on your own computer with **Ollama** and **LM Studio**, integrate local models into Python, compare their performance, and build an **Offline-First AI Tool** that can optionally use a hosted model.

**Project built:** An offline-first note-summarization CLI, using **Qwen2.5 3B through Ollama** by default and optional **Gemini hosted inference**. The working implementation, benchmark tooling, tests, and documentation are included in this repository. Unverified requirements are clearly marked below.

**Learning approach:** The first labs were built step by step. The mini-project and benchmarking tools were then prepared as a quick implementation, with code review and deeper independent rebuilding planned for later.

## Milestone Tracker

| Milestone | Focus | Roadmap requirement | Status |
| --- | --- | --- | --- |
| **0** | Understand all concepts | LO 4.1–4.5 and topics covered | ✅ Completed |
| **1** | Ollama setup and model comparison | Lab 4.1 | ✅ Completed |
| **2** | Local API with Python | Lab 4.2 | ✅ Completed |
| **3** | LM Studio and GGUF benchmark | Lab 4.3 | 🟡 In progress — benchmark pending |
| **4** | Hosted/local configuration | Lab 4.4 | 🟡 Implemented — matching-prompt comparison incomplete |
| **5** | Build the offline-first tool | Mini Project 4 | 🟡 Working locally — Wi-Fi-off test and acceptance review pending |
| **6** | Evaluation and portfolio documentation | Assignment outputs and portfolio note | 🟡 Benchmark/docs prepared — demo and final review pending |

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

**Evidence:** Week 4 conceptual discussions; `notes/` holds project notes. If you want standalone written quiz evidence later, add `notes/milestone_0_concepts.md`.

---

## Milestone 1 — Install Ollama and Chat with Two Models

**Maps to:** Lab 4.1

### Tasks

- [x] **Task 1.1 — Inspect your machine:** Record operating system, installed RAM, GPU/VRAM (if any), and available disk space.
- [x] **Task 1.2 — Install and verify Ollama:** Use official instructions appropriate for your OS. Confirm that it is available in your terminal.
- [x] **Task 1.3 — Select two models:** Choose one small and one mid-size model based on your hardware, task quality needs, and license. Record identifiers and download sizes. *Mid-size is relative to available hardware; do not force a model that cannot fit.*
- [x] **Task 1.4 — Pull the small model:** Download it and confirm that Ollama recognizes it.
- [x] **Task 1.5 — Chat from the terminal:** Send a small set of repeatable prompts and save observations.
- [x] **Task 1.6 — Pull and test the mid-size model:** Use the same prompts and note memory/performance differences.
- [x] **Task 1.7 — Compare results:** Record which model gave more useful answers and which ran more comfortably.

### Completion Criteria

- [x] Ollama works on my computer.
- [x] I can launch each of the two models from the terminal.
- [x] Both models respond to comparable prompts.
- [x] I have documented the chosen models, hardware, and qualitative differences.

**Evidence:** [`labs/lab_4_1/README.md`](labs/lab_4_1/README.md). Models tested: `qwen2.5:3b` and `qwen2.5:7b`.

---

## Milestone 2 — Connect Python to the Ollama Local API

**Maps to:** Lab 4.2

### Tasks

- [x] **Task 2.1 — Understand the architecture:** Sketch Python client → local HTTP endpoint → Ollama → model → response.
- [x] **Task 2.2 — Prepare Python:** Create or activate a virtual environment in VS Code; install only required packages; begin tracking dependencies in `requirements.txt`.
- [x] **Task 2.3 — Check the local server:** Confirm the Ollama API is reachable on your machine.
- [x] **Task 2.4 — Build a minimal Python client:** Use an OpenAI-compatible client with a local `base_url` and a locally installed model identifier.
- [x] **Task 2.5 — Inspect the response:** Display the answer, identify relevant response fields, and handle a failed connection or missing model cleanly.
- [x] **Task 2.6 — Test and document:** Compare terminal and Python calls for the same prompt.

### Completion Criteria

- [x] A Python script calls a local model successfully.
- [x] The application does not need a paid API key to make its local call.
- [x] I understand the role of the endpoint, model name, and client library.
- [x] A predictable failure displays a useful error rather than a confusing crash.

**Evidence:** [`labs/lab_4_2/api_practice.py`](labs/lab_4_2/api_practice.py) and [`labs/lab_4_2/README.md`](labs/lab_4_2/README.md).

---

## Milestone 3 — LM Studio and GGUF Benchmarking

**Maps to:** Lab 4.3

### Tasks

- [x] **Task 3.1 — Install LM Studio:** Confirm it opens and locate the model browser and chat interface.
- [ ] **Task 3.2 — Choose a GGUF model:** Inspect available quantizations, licenses, file sizes, and RAM/VRAM suitability. **Partially completed:** selected `Qwen2.5-3B-Instruct-GGUF`, `Q4_K_M`, approximately 1.93 GB; complete/record license inspection.
- [ ] **Task 3.3 — Download and run:** Start chatting locally with the selected model. Download was started; successful installation/inference has not been confirmed.
- [ ] **Task 3.4 — Benchmark:** Use repeatable prompts, note generation tokens/sec as reported by the tool, and distinguish it from initial loading or prompt-processing time where possible.
- [ ] **Task 3.5 — Compare:** Record quality, response speed, and resource use; explain how quantization may affect results.
- [ ] **Task 3.6 — Explore server mode:** Find LM Studio's local server interface and explain how it resembles the Ollama endpoint.

### Completion Criteria

- [ ] A downloaded GGUF model responds in LM Studio.
- [ ] I have at least one recorded tokens/sec measurement with the model and quantization specified.
- [ ] I can explain the memory/performance/quality trade-offs I observed.

**Evidence to add:** `benchmarks/lm_studio_results.md` with machine specs, model, quantization, test prompt(s), methodology, tokens/sec, and quality notes.

---

## Milestone 4 — Switch Week 3 Code Between Hosted and Local Models

**Maps to:** Lab 4.4

### Tasks

- [x] **Task 4.1 — Review Week 3 work:** Identify the Python code that currently sends prompts to a hosted model. If a microservice was not built in Week 3, first extract the smallest reusable request interface from the code you do have; document the difference from the roadmap's microservice requirement.
- [x] **Task 4.2 — Isolate configuration:** Decide how a single mode flag selects a hosted or local backend.
- [x] **Task 4.3 — Define a common request/response contract:** Keep the calling application independent of backend-specific details.
- [x] **Task 4.4 — Implement the local path:** Connect the existing request flow to Ollama.
- [x] **Task 4.5 — Preserve the hosted path:** Retain the Week 3 provider and its required credentials; never commit API keys.
- [ ] **Task 4.6 — Verify both configurations:** Run matching test prompts against each backend and record differences. Both backends have worked separately, but a later matching-prompt Gemini request returned HTTP 503; complete the controlled comparison when available. The two SDKs also have provider-specific calling methods, so this implementation uses a configuration flag and adapters rather than only changing `base_url`.

### Completion Criteria

- [x] A single configuration option selects hosted or local inference.
- [x] Switching does not require edits to the application's task logic.
- [x] Both paths have been tested (subject to hosted-service availability).
- [ ] No credentials are stored in source code or committed files. **Final repository/history security audit pending; `.env` is intended to be ignored.**

**Evidence:** [`labs/lab_4_4/model_router.py`](labs/lab_4_4/model_router.py) and [`labs/lab_4_4/README.md`](labs/lab_4_4/README.md).

---

## Milestone 5 — Mini Project 4: Offline-First AI Tool

**Maps to:** Weekly assignment

**Required outcome:** Build a CLI or small app that works fully offline using a local model through Ollama, with an optional flag for a hosted API to improve quality.

**Selected use case:** Offline-First Note Summarizer. It reads a local `.txt`/`.md` file and returns a summary, key points, and a suggested next action. Hosted Gemini mode is optional; Ollama is the default.

### Tasks

- [x] **Task 5.1 — Define the problem:** State the intended user, what the tool accepts, and what it should return.
- [ ] **Task 5.2 — Specify acceptance tests:** Define at least three realistic test cases and expected behavior before coding. Automated tests have been prepared, but three distinct acceptance scenarios have not been confirmed as passing together.
- [x] **Task 5.3 — Design components:** Sketch input → preprocessing → local/hosted inference → output. Keep inference separate from app logic.
- [ ] **Task 5.4 — Implement an offline-first CLI or small app:** Make the core task work with Ollama while the internet is disconnected (after models and dependencies are installed). **Implementation works locally; Wi-Fi-off verification pending.**
- [x] **Task 5.5 — Add the optional hosted flag:** Keep the local model as the normal/default option; require credentials only for hosted mode.
- [x] **Task 5.6 — Validate and handle errors:** Cover invalid inputs, unavailable model/server, and hosted configuration errors.
- [ ] **Task 5.7 — Perform real tests:** Run the acceptance cases locally and, where available, with hosted inference. One successful local end-to-end summary was demonstrated; full acceptance set and offline test pending.

### Completion Criteria

- [x] The app solves its stated task (successful local note summarization demonstrated).
- [ ] Core functionality works with internet disabled after initial setup. **Not yet tested with internet disabled.**
- [x] An optional flag can select the hosted backend.
- [ ] At least three documented acceptance tests pass. **Full test suite/acceptance evidence pending.**
- [ ] The code is written and understood by me. **The quick-build implementation still needs a complete personal code walkthrough.**

**Evidence:** [`final_project/`](final_project/) — executable CLI, package entry points, sample notes, README, and tests in [`tests/`](tests/).

**Run from project root:**

```powershell
python final_project/offline_note_summarizer.py final_project/sample_notes.txt
```

---

## Milestone 6 — Benchmark, Justify, Document, and Publish

**Maps to:** Required assignment outputs + portfolio note

### Tasks

- [x] **Task 6.1 — Benchmark local behavior:** Record model identifier, quantization (if applicable), tokens/sec, prompt(s), hardware, and test conditions. **3B result collected; earlier 7B observations available; a new 7B run timed out and must not be reported as successful.**
- [ ] **Task 6.2 — Evaluate output quality:** Define a simple task-specific rubric and apply it to a small, consistent evaluation set. A rubric has been prepared, but the full scored evaluation is pending.
- [x] **Task 6.3 — Justify model choice:** Explain trade-offs among hardware fit, license, quality, latency, privacy, and cost. Written justification is in `docs/model_choice.md`.
- [ ] **Task 6.4 — Compare local and hosted modes:** Note the practical advantages and limits of each using evidence rather than assumptions. Gemini's controlled comparison request returned HTTP 503.
- [ ] **Task 6.5 — Polish GitHub documentation:** Add requirements, setup, usage, folder descriptions, limitations, and reproducible testing instructions. Documentation files exist, but final repository review is pending.
- [ ] **Task 6.6 — Record a short demo:** Show the tool operating locally and explain what makes it offline-first. Guide prepared, recording pending.
- [ ] **Task 6.7 — Review before publishing:** Remove secrets, local virtual environments, unnecessary large model files, and personal/private example data; verify `.gitignore`. Final audit pending.

### Completion Criteria

- [x] Working local app and optional hosted mode are documented.
- [x] Benchmark note includes **model, tokens/sec, and quality** observations.
- [x] Model choice is justified in writing.
- [ ] A short screen demo is available.
- [ ] The repository can be understood and reproduced by someone else. **Final installation and verification review pending.**

**Benchmark evidence:** [`benchmarks/final_benchmark.md`](benchmarks/final_benchmark.md), [`benchmarks/local_3b_results.json`](benchmarks/local_3b_results.json), and [`docs/model_choice.md`](docs/model_choice.md).

**Qwen2.5 3B new benchmark:** Mean generation rate **13.87 tokens/sec** across two runs (13.17 and 14.56 tokens/sec). **Earlier Lab 4.1 rates:** 3B 15.10 and 7B 6.88 tokens/sec, measured under different test conditions. These figures are not guaranteed to be directly comparable. One newer 7B benchmark attempt timed out.

---

## Current Repository Structure

The following reflects the actual files and folders shown in the Week 4 VS Code project; omitted contents of `notes/` and `labs/` are not invented. Downloaded model weights are stored outside the repository.

```text
offline-ai-tool/
├── .venv/                           # Local Python environment — do not commit
├── .env                             # Local Gemini key — do not commit
├── .gitignore
├── README.md                        # This milestone tracker
├── README_MILESTONE_6.md            # Milestone 6 guide
├── requirements.txt
├── labs/
│   ├── lab_4_1/
│   │   └── README.md
│   ├── lab_4_2/
│   │   ├── api_practice.py
│   │   └── README.md
│   └── lab_4_4/
│       ├── model_router.py
│       └── README.md
├── notes/                            # Learning notes (individual files not listed)
├── final_project/
│   ├── __init__.py
│   ├── offline_note_summarizer.py
│   ├── sample_notes.txt
│   └── README.md
├── benchmarks/
│   ├── final_benchmark.md
│   └── local_3b_results.json
├── docs/
│   ├── demo_guide.md
│   ├── model_choice.md
│   └── release_checklist.md
├── tests/
│   ├── __init__.py
│   ├── test_benchmark_ollama.py
│   └── test_offline_note_summarizer.py
└── tools/
    ├── __init__.py
    └── benchmark_ollama.py
```

**Not yet evidenced as existing:** `labs/lab_4_3/`, `benchmarks/lm_studio_results.md`, `benchmarks/local_7b_results.json`, or a recorded demo. Do not add them to the tree until created.

**Important:** Keep `.env`, `.venv/`, `__pycache__/`, and downloaded model weights out of Git. Avoid committing private user notes or generated private outputs.

## How to Work Through the Remaining Milestones

1. Finish **Milestone 3** by running the GGUF model in LM Studio and recording a tokens/sec measurement.
2. Finish **Milestone 4** by documenting a successful same-prompt comparison (or the hosted provider's availability limitation) and auditing secrets.
3. Finish **Milestone 5** by testing the CLI with internet disabled, reviewing three acceptance cases, and studying the quick-build code.
4. Finish **Milestone 6** by scoring output quality, checking the repository's reproducibility/security, recording a short demo, and updating all relevant checkboxes.
5. Only change a checkbox to `[x]` when the corresponding evidence has been verified.

## Week 4 Learning Outcomes Coverage

| Roadmap learning outcome | Where demonstrated |
| --- | --- |
| **LO 4.1:** Install/run open models with Ollama and LM Studio; expose compatible endpoint | Milestones 0–3 (LM Studio run pending) |
| **LO 4.2:** Understand quantization and GGUF size/VRAM trade-offs | Milestones 0 and 3 |
| **LO 4.3:** Select a model for hardware, license, and quality | Milestones 0, 1, 3, and 6 |
| **LO 4.4:** Switch between local and hosted model via configuration/base URL | Milestones 2, 4, and 5 (provider-specific adapters used) |
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

**Current status:** Milestones 0–2 complete; Milestones 3–6 have implemented or documented work with the remaining verification tasks listed above.
