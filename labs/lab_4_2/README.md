# Lab 4.2 — Connect Python to the Ollama Local API

> **Week:** 4 — Local LLMs & Open-Source Tooling  
> **Milestone:** 2 — Connect Python to the Ollama Local API  
> **Status:** Practical work completed; documented from hands-on tests  
> **Goal:** Call a local LLM from Python using an OpenAI-compatible API, inspect responses, and handle expected errors.

## 1. Overview

This lab connects a Python application to a locally running Ollama server. Instead of typing prompts only inside the `ollama run` chat, the Python script accepts a user's question, sends it to Qwen2.5 3B, and displays the response. The script also inspects response metadata and handles missing-model and connection errors gracefully.

**Architecture:**

```text
User types a prompt
       |
       v
Python script (`api_practice.py`)
       |
       v
OpenAI-compatible Python client
       |
       v
http://localhost:11434/v1
       |
       v
Ollama local server
       |
       v
qwen2.5:3b (local inference)
       |
       v
Response text + metadata returned to Python
```

The `openai` library is used here as a **client library**, not as a request to OpenAI's hosted service. Local inference through Ollama does not require a paid OpenAI API key. The `api_key="ollama"` value is a placeholder for the compatible client.

## 2. Environment and requirements

**Development setup used:**

- OS: Windows 11 (25H2)
- Editor: Visual Studio Code
- Workspace: `E:\offline-ai-tool`
- Shared Python environment: `E:\offline-ai-tool\.venv`
- Local runtime: Ollama
- Model: `qwen2.5:3b` (approximately 1.9 GB on disk)
- API endpoint: `http://localhost:11434/v1`
- Python package: `openai==3.52.0`
- Model storage configured on E: at `E:\OllamaModels`

**Relevant repository files:**

```text
offline-ai-tool/
├── .gitignore
├── .venv/                  # Local only; do not commit
├── README.md              # Main milestone tracker
├── requirements.txt       # openai==3.52.0
└── labs/
    ├── lab_4_1/
    └── lab_4_2/
        ├── api_practice.py
        └── README.md
```

### Reproduce the Python environment

From the repository root in VS Code PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -c "import sys; print(sys.executable)"
```

The interpreter should point to the repository's `.venv\Scripts\python.exe`. If a virtual environment already exists, activate it rather than creating another. If PowerShell activation is restricted, use VS Code's interpreter selection or your machine's approved execution-policy workflow.

To run **only this lab**, even when opening `labs/lab_4_2` as the VS Code workspace, select the Python interpreter at `E:\offline-ai-tool\.venv\Scripts\python.exe`. A Python script does **not** need a separate `.venv` inside every lab folder. On another computer, recreate the environment from the root `requirements.txt`; do not commit the `.venv` directory.

### External prerequisite: Ollama and model

Install Ollama separately, ensure its server is running, and download the model using:

```powershell
ollama pull qwen2.5:3b
ollama list
```

Ollama itself and its model weights are **not** Python packages and therefore do not appear in `requirements.txt`.

## 3. README milestone tasks and evidence

| Task | Requirement | Evidence from this lab |
| --- | --- | --- |
| 2.1 | Understand architecture | Described the route from Python client to Ollama server and back. |
| 2.2 | Prepare Python | Verified root `.venv`, installed `openai==3.52.0`, created `requirements.txt`. |
| 2.3 | Check local server | PowerShell request to `/api/tags` returned the installed `qwen2.5:3b` model and metadata. |
| 2.4 | Build minimal Python client | OpenAI-compatible request to `qwen2.5:3b` succeeded and printed a model response. |
| 2.5 | Inspect response and handle errors | Printed generated text, `finish_reason`, and `usage`; handled missing-model and connection failures. |
| 2.6 | Compare terminal and Python calls | Ran the same quantization prompt through `ollama run` and `api_practice.py`; recorded results below. |

## 4. Implementation: what the Python script does

The implementation in `api_practice.py` was built and tested incrementally:

1. Import the `OpenAI`, `NotFoundError`, and `APIConnectionError` classes.
2. Read a prompt using Python's `input()` function.
3. Create a client with the local `base_url` and placeholder API key.
4. Call `client.chat.completions.create(...)` with the installed model identifier and user message.
5. Print the generated answer from `response.choices[0].message.content`.
6. Inspect `response.choices[0].finish_reason` and `response.usage`.
7. Catch missing-model (`NotFoundError`) and unavailable-server (`APIConnectionError`) exceptions and show helpful messages.

The exercise used `max_tokens=100` for the later response-length experiments. This limits **output tokens**, not the number of words or sentences, and can cut a reply off before it finishes.

**Run from the repository root:**

```powershell
python labs/lab_4_2/api_practice.py
```

The script prompts for a question, prints Qwen's reply, and then prints metadata. The script, not this README, is the source of the implementation.

## 5. API connectivity test

The native Ollama model-list endpoint was checked with:

```powershell
Invoke-RestMethod http://localhost:11434/api/tags
Invoke-RestMethod http://localhost:11434/api/tags | ConvertTo-Json -Depth 5
```

The response showed `qwen2.5:3b`, the `qwen2` family, approximately `3.1B` parameters, `Q4_K_M` quantization, and a reported `32768` context length. This tests API accessibility and model metadata retrieval; it does not itself perform text generation.

**Endpoint distinction:**

- `http://localhost:11434/api/tags`: Ollama's native model-list API.
- `http://localhost:11434/v1`: OpenAI-compatible base URL used by the Python client.

## 6. Response inspection and output limits

### Successful Python call

The first working Python request asked Qwen2.5 3B to explain an API in two sentences. Qwen produced text in the terminal after the script printed `response.choices[0].message.content`.

The script was then updated to accept dynamic prompts from the terminal rather than editing the prompt string for each run.

### Token usage observations

For the question **"What is an LLM? Answer in one sentence."**, two runs showed:

| Field | Run 1 | Run 2 |
| --- | ---: | ---: |
| Prompt tokens | 40 | 40 |
| Completion tokens | 27 | 31 |
| Total tokens | 67 | 71 |

Both completed below the `max_tokens=100` limit. Answers may differ between runs, so identical prompts do not guarantee identical completion lengths.

For a longer question about LLMs, the response showed `completion_tokens=100`, `prompt_tokens=35`, `total_tokens=135`, and `finish_reason=length`. This indicates that generation hit the configured output-token limit.

**Fields inspected:**

- `response.choices[0].message.content` — answer text
- `response.choices[0].finish_reason` — why generation ended (`stop` or `length`, among possible values)
- `response.usage` — prompt, completion, and total token counts when supplied by the API

## 7. Error-handling experiments

### A. Missing model

**Test:** Temporarily request `model-that-does-not-exist` while Ollama is reachable.

**Observed failure before handling:**

```text
openai.NotFoundError: Error code: 404
model 'model-that-does-not-exist' not found
```

**After adding a targeted handler:** The application printed a friendly message instead of a traceback, such as:

```text
model does not exist
```

The improved message suggests running `ollama list` to check available local models.

### B. Server unavailable

**Test:** Temporarily change the client URL to `http://localhost:11435/v1` (an unused test port) while using the valid `qwen2.5:3b` identifier.

**Observed after handling:**

```text
Cannot connect to Ollama. Make sure the local server is running
```

No traceback appeared. The correct base URL, `http://localhost:11434/v1`, and real model identifier were restored; the next request succeeded.

**Lesson:** An HTTP 404 for a missing model is different from a failure to connect to the server. Specific exception handlers provide clearer feedback.

## 8. Lab 4.2 — CLI vs Python API comparison

**Identical prompt in both cases:**

> Explain quantization in local LLMs in exactly two sentences.

**Model:** `qwen2.5:3b`

### CLI method

```powershell
ollama run qwen2.5:3b
```

The CLI response described reducing model-weight precision (e.g., 32-bit to 8-bit or 4-bit) to reduce memory footprint and often improve inference efficiency. It produced a single long sentence rather than exactly two sentences. The response also described minimal quality loss too confidently; quantization may degrade quality depending on the model and method.

### Python method

```powershell
python labs/lab_4_2/api_practice.py
```

Using the same prompt, Python returned an explanation of lower-precision model parameters and reduced resource requirements. It also produced one sentence rather than exactly two.

**Recorded Python response metadata:**

| Metric | Value |
| --- | ---: |
| Prompt tokens | 43 |
| Completion tokens | 73 |
| Total tokens | 116 |
| Output limit | 100 tokens |
| Finish reason | `stop` |

`stop` indicates that the reply ended normally rather than reaching the 100-token cap.

### Comparison summary

| Comparison | Ollama CLI | Python + OpenAI-compatible client |
| --- | --- | --- |
| Calls local model | Yes | Yes |
| Uses same model identifier | Yes | Yes |
| Requires paid OpenAI API key | No | No |
| Accepts a prompt | Interactive terminal | `input()` in the Python script |
| Displays response | Yes | Yes |
| Usage metadata recorded in this test | No | Yes |
| Targeted error handling implemented | Not in this lab's CLI test | Yes |
| Followed exactly-two-sentences instruction | No | No |

The experiments used the same prompt and model, but generation settings were **not fully matched** between the interfaces (the Python code had `max_tokens=100`). Therefore, wording differences cannot be attributed to the interface alone. The comparison demonstrates that both methods work and that Python offers richer programmatic control.

## 9. Key findings

- The same local Ollama model can be called interactively or through an OpenAI-compatible Python client.
- `base_url` determines where the client sends requests; the library name does not determine which provider runs the model.
- Local model requests need no paid OpenAI API key, but Ollama must be running and the requested model must be installed.
- A Python script needs to **print** response fields to display them in the terminal.
- `max_tokens` can limit output length, but it does not guarantee concise or complete answers.
- Structured response fields make token tracking and debugging possible.
- Specific error handlers improve the user experience for model-not-found and connection-failure cases.
- Identical prompts can produce slightly different outputs, and a model may ignore an exact sentence-count instruction.

## 10. Completion criteria

- [x] A Python script successfully calls a local model.
- [x] The application makes local calls without a paid API key.
- [x] The endpoint, model identifier, and client-library roles are understood.
- [x] Predictable missing-model and connection failures display useful errors rather than confusing tracebacks.

**Milestone status:** Hands-on tasks 2.1–2.6 completed and supported by terminal tests. Update the root project `README.md` milestone tracker only once, after reviewing this lab documentation.

## 11. Next steps

Continue to **Milestone 3 — LM Studio and GGUF Models**. For future improvements, consider testing more prompts, standardizing generation parameters for stronger comparisons, and adding a small test suite. These are optional improvements, not claims of work already completed.
