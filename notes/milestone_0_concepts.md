# Milestone 0 — Local LLM Concepts

**Project:** Week 4 — Local LLMs & Open-Source Tooling  
**Reference:** Helwan Career Center, 12-Week Industry Roadmap, Week 4 (pages 12–13)  
**Purpose:** Record the concepts learned in our discussions and knowledge checks before starting the practical labs.

> **Progress note:** These are study notes, not proof that every checklist/quiz is finished. We explicitly completed the Ollama Task 0.2 questions and demonstrated understanding of memory budgeting and local-versus-hosted trade-offs. The separate LM Studio Task 0.3 and licensing Task 0.8 quiz scores were not explicitly confirmed in our conversation.

## 1. Local vs. Hosted LLMs

### My understanding

- A **hosted LLM** receives prompts from my application over the internet, processes them using the provider's hardware, and returns a response. Response time may depend on network conditions, provider load, and generation speed.
- A **local LLM** is a model downloaded and run on my own computer. Once the software and model are installed, inference can work without the internet. The performance depends on my available hardware and the model I choose.
- Local inference can keep prompts on my device, although I still need to protect local files and make sure the app itself does not send data elsewhere.
- A local model is **not automatically faster** than a hosted model.

**Our practice scenario:** For an offline private journaling assistant, I selected a **small local model through Ollama**, because it can work without internet and can keep prompts local. I also recognized the trade-off: smaller models may have lower quality, and my laptop does the processing.

## 2. Ollama: Commands, API, and Modelfiles

**Ollama** is a tool for downloading and running local models and exposing them through a local API.

| Command | Meaning |
|---|---|
| `ollama pull qwen2.5:3b` | Download the specified model without opening a chat |
| `ollama run qwen2.5:3b` | Run an interactive chat with the model (download first if needed) |
| `ollama list` | Show models already downloaded |
| `ollama serve` | Start the local Ollama API server |

On Windows, the Ollama background app may already have its API server running, so starting another server is not always necessary.

A **Modelfile** describes a customized model setup. Important instructions include:

- `FROM` — selects an existing base model.
- `SYSTEM` — defines instructions guiding how the model should behave.
- `PARAMETER` — configures settings such as temperature.

A Modelfile with a system prompt does **not** by itself retrain the model or update its original weights.

**Our knowledge check:** I correctly answered that **`ollama pull qwen2.5:3b`** downloads the model without opening an interactive chat. I later confirmed completion of the command and Modelfile questions in Task 0.2.

## 3. LM Studio and GGUF

**LM Studio** is a desktop tool for discovering, downloading, loading, chatting with, and serving local models through a graphical interface. It also supports developer-oriented features such as a local server.

The basic flow is:

1. Browse for a model and inspect available versions.
2. Choose and download a compatible model file, often **GGUF**.
3. Load the model and test it in the chat interface.
4. Optionally start its local API server so Python code can send it requests.

**GGUF** is a model file format used by compatible local inference tools. It can store quantized model weights and relevant metadata. GGUF itself is **not** the same thing as quantization.

LM Studio typically exposes an OpenAI-compatible local endpoint such as `http://localhost:1234/v1`; Ollama typically uses `http://localhost:11434/v1`.

**Benchmark concept:** Output speed is commonly measured in **tokens per second**. As a simplified example, 100 generated tokens over 10 seconds of generation time is 10 tokens/second. Actual benchmarking should state how the measurement was made, and may also record time to first token and response quality.

## 4. Quantization, Model Size, and GGUF

**Quantization** reduces the precision used to store model weights, often making a model smaller and more practical to run locally. We compared FP16 (16-bit), 8-bit, 4-bit, and 2-bit representations.

- Fewer bits generally mean less weight storage and potentially lower memory needs.
- Aggressive quantization can affect accuracy and answer quality, but a modern 4-bit model can still perform well.
- Quantization reduces the size of the *weights*; it does not eliminate other runtime memory requirements.

### Rough weight-size formula

For a **dense model** and a simplified fixed-bit representation:

\[
\text{Weight size in decimal GB} \approx \frac{\text{Parameters in billions} \times \text{Bits per weight}}{8}
\]

Example: an 8B model at 4-bit precision:

\[
8 \times 4 \div 8 = 4\ \text{GB (weights only)}
\]

At FP16:

\[
8 \times 16 \div 8 = 16\ \text{GB (weights only)}
\]

Actual GGUF file sizes vary due to quantization formats, metadata, and other overhead. This simple formula does not cover every architecture.

### Runtime memory

\[
\text{Approximate required memory} = \text{model weights} + \text{KV cache} + \text{runtime overhead}
\]

The **KV cache** stores attention-related information for the active context. Longer context windows can require more memory. Runtime overhead includes additional buffers and other allocations.

**Our knowledge check:** I chose the **4-bit** version of an 8B model rather than FP16, because it is more realistic with 16 GB installed RAM and about 7 GB available at the time. I compared estimated runtime memory against **available**, not merely installed, RAM.

## 5. Model Families, Variants, and Licensing

The roadmap introduces six model families:

- **Llama** — Meta
- **Qwen** — Alibaba
- **Gemma** — Google
- **Mistral** — Mistral AI
- **Phi** — Microsoft
- **gpt-oss** — OpenAI

Important terms:

- **Model family:** a related group of models.
- **Parameter count:** for example, 3B means approximately 3 billion parameters.
- **Base model:** mainly trained for text prediction/continuation, not necessarily assistant-style instruction following.
- **Instruction-tuned model:** additionally trained to follow user instructions, often better suited to chat applications.
- **Quantized variant:** stores weights at reduced precision to save memory.

**Our practice scenario:** For a small laptop-based coding assistant, I chose a **3B, 4-bit, coding-oriented, instruction-tuned model** over a 70B FP16 general model or a 7B base model. My reasons were hardware fit, task specialization, and instruction-following capability.

### Licensing

- **Open-weight** means model weights are available, but it does not automatically guarantee unrestricted reuse or full open-source compliance.
- A **model license** can define permissions and obligations for commercial use, modification, and redistribution.
- Check the **exact model/version's** license and model card before selecting it for a public or commercial project. Models in the same family can have different license terms.
- A model that works technically may still be inappropriate for a planned deployment if its license does not permit that use.

We discussed Qwen2.5 3B and 7B as an example of why the *exact variant's* license matters. The current official license should be rechecked before shipping or redistributing a project.

## 6. My Laptop: RAM, VRAM, and Model Budgeting

### My hardware (from Task Manager)

| Component | Specification |
|---|---|
| CPU | Intel Core i7-1165G7 (11th Gen) |
| Installed RAM | 16 GB |
| Integrated GPU | Intel Iris Xe Graphics |
| Dedicated GPU | NVIDIA GeForce MX350 |
| Dedicated VRAM | 2 GB |
| Shared GPU memory | Up to approximately 7.9 GB (borrowed from system RAM) |
| Available system RAM during one check | Approximately 7–8 GB |

**Important:** Shared GPU memory is part of system RAM, **not extra physical RAM**. I cannot add 16 + 2 + 7.9 GB as if they were all independent.

With only 2 GB of dedicated VRAM, I should initially expect CPU-heavy inference, with partial GPU acceleration only if supported. A model may run from system RAM even when it cannot fit entirely into VRAM; that does not guarantee good speed.

### My 8B model calculation

1. **4-bit weights:** `8 × 4 / 8 = 4 GB` approximately.
2. **Required runtime memory:** approximately `4 GB + KV cache + runtime overhead`.
3. **Available memory:** around 7 GB at the time of our scenario.
4. **Decision:** compare realistic estimated requirements to currently available RAM, retain headroom for Windows, and test cautiously.
5. **FP16 comparison:** about 16 GB for weights alone, so not practical with only about 7 GB available.

These figures are planning estimates. Actual model loading, context length, CPU/GPU offloading, memory pressure, and speed should be measured during labs.

### Provisional models for Lab 4.1

- **Small:** Qwen2.5 3B, quantized.
- **Mid-size:** Qwen2.5 7B, quantized, if memory and performance permit.

Using two different sizes from one family allows a more focused quality/speed comparison. Choices remain provisional until installation and testing.

## 7. Local APIs, `localhost`, and OpenAI Compatibility

A **local API** lets my Python application communicate with a model server on the same computer.

- `localhost` refers to my own computer, commonly via `127.0.0.1`.
- A **port** identifies the network service; Ollama's usual port is `11434`.
- `base_url` tells an API client where to send requests.
- Ollama's usual OpenAI-compatible endpoint is `http://localhost:11434/v1`.
- LM Studio's commonly used endpoint is `http://localhost:1234/v1`.

An **OpenAI-compatible API** means an API supports a similar interface or request/response structure to supported OpenAI API features. It can let an existing Python client talk to different providers with less code rewriting.

**Crucial distinction learned from our discussion:** Compatibility **does not automatically switch models**. My application must select the backend and model. Automatic fallback to a hosted provider requires extra program logic, working internet, credentials, and a privacy decision.

**Our knowledge check:** I correctly answered that if Python contacts Ollama when its server is not running **and there is no fallback logic**, the expected result is generally a **connection error**, not automatic switching.

## 8. Local vs. Hosted: Deployment Trade-offs

| Factor | Local inference | Hosted API |
|---|---|---|
| Privacy | Prompts can stay on device | Prompts sent to provider |
| Offline use | Possible after setup | Generally requires internet |
| Hardware | My own computer runs the model | Provider runs the model |
| Cost | Hardware, storage, electricity; no per-token provider fee | May charge per token or request |
| Quality | Depends on model/variant and task; hardware restricts feasible choices | Can provide access to powerful models |
| Latency | Depends on local hardware, model, and context | Depends on network and provider/model processing |

### Our final reasoning question

**Application A — Private offline journal:** I chose **local inference**, because prompts can remain private, everything can run offline after installation, and I avoid per-token API fees. The trade-offs are the laptop's memory and speed and the quality of the model I can run.

**Application B — Advanced coding assistant:** I chose **hosted inference**, because I can access a more capable model without running it on my laptop. The trade-offs are internet dependence, possible per-token cost, and sending prompts to the provider. Hosted latency also depends on provider processing, not only internet speed.

## 9. Roadmap Learning Outcomes (LO 4.1–4.5)

| Learning outcome | My conceptual understanding | Practical demonstration planned |
|---|---|---|
| **LO 4.1** — Run models with Ollama and LM Studio, expose endpoint | Understand each tool and local APIs | Labs 4.1–4.3 |
| **LO 4.2** — Quantization/GGUF/VRAM | Can estimate 4-bit vs FP16 weight size and explain runtime overhead | Labs 4.1 and 4.3 |
| **LO 4.3** — Choose models | Compare task, size, quantization, RAM/VRAM, quality, license | Labs 4.1/4.3 and mini project |
| **LO 4.4** — Change hosted/local backend | Understand `base_url`, selected model, and configuration; compatibility is not fallback | Labs 4.2 and 4.4 |
| **LO 4.5** — Explain deployment trade-offs | Chose local journal vs hosted coding assistant for clear reasons | Mini project justification |

## 10. Personal Summary and Next Steps

### Concepts I can explain

- The difference between local and hosted inference.
- Why RAM, VRAM, and available memory affect which models can run.
- Why 4-bit quantization makes larger models more manageable, with possible quality trade-offs.
- How Ollama, LM Studio, and `localhost` fit into a local Python application.
- Why OpenAI-compatible endpoints simplify integration without creating automatic fallback.
- Why a license, not just technical performance, matters when choosing a model.

### Evidence from our discussions

- Correct selection of local inference for a private offline journal.
- Correct choice of a compact quantized instruction-tuned model for limited hardware.
- Correct use of `ollama pull` for download-only behavior.
- Correct explanation of a connection error when local Ollama is offline and no fallback exists.
- Correct 8B 4-bit weight estimate and rejection of FP16 for the available-RAM scenario.
- Correct local-versus-hosted selection for two application scenarios.

### Remaining progress checks

- [x] Discussed Ollama commands and Modelfiles; Task 0.2 explicitly confirmed complete.
- [ ] Confirm the separate **Task 0.3 LM Studio quiz** result (not explicitly provided).
- [ ] Confirm the separate **Task 0.8 model licensing quiz** result (not explicitly provided).
- [x] Completed Task 0.9's memory-budgeting and local-versus-hosted reasoning exercises.
- [ ] Update README checklist once the remaining confirmations are complete.
- [ ] Start Milestone 1 / Lab 4.1: install Ollama, download two models, and compare their responses.

---

*These notes reflect our Week 4 lessons and the roadmap. They do not claim that the hands-on labs have been completed.*
