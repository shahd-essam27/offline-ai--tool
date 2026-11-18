# Week 4 — Model Choice and Decision Framework

## Selected default: Ollama `qwen2.5:3b`

The mini-project uses Qwen2.5 3B as its default local model. The observed quantized download was ~1.9 GB, and its previous generated-token rate was **15.10 tokens/sec**. On the same laptop, the 7B alternative gave **6.88 tokens/sec** in the earlier test. That makes 3B a pragmatic choice for fast, privacy-preserving note summaries on 16 GB RAM with limited 2 GB VRAM.

## Why use a quantized model?

Q4_K_M compresses weights relative to higher-precision weights, enabling models to fit into smaller memory budgets. The trade-off can include loss of quality; file size alone does not predict factual accuracy.

## Local vs hosted

| Decision factor | Local Ollama | Hosted Gemini |
|---|---|---|
| Privacy | Input stays on the computer if no other network sharing is used | Input sent to the provider |
| Internet | Not required for inference once installed | Required |
| API quota / per-call billing | No external token fees; electricity/hardware costs remain | Quotas and potentially charges apply |
| Speed | Depends on laptop, model and load | Depends on network and provider capacity |
| Quality | Small 3B sometimes hallucinates | Can be strong but not guaranteed; failed request 503 in later test |
| Availability | Depends on local Ollama process | Depends on hosted service availability |

**Privacy safety:** The app never silently falls back to hosted mode. It must be explicitly selected.

## License caution

Model files are not committed to this repository. Before commercial reuse or redistribution, check the exact installed model variant, its publisher and license; don't infer permission from the generic model-family name alone.

## Known limitations

- Smaller models can produce false answers, as GGUF-definition trials demonstrated.
- A single benchmark trial doesn't establish statistical quality superiority.
- A new controlled head-to-head test, complete local offline run, LM Studio benchmark and demo remain pending.
