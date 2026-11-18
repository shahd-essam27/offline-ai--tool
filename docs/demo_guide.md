# Week 4 — Screen Demo Guide

**Status: Not yet recorded.** This guide is provided to record a real demonstration on your computer.

## Suggested 60–90 second demo

1. Open the root `README.md` and show the project structure.
2. Show `final_project/sample_notes.txt` (public sample only). **Never display `.env` or API keys.**
3. Run `ollama list`, confirming `qwen2.5:3b` is installed.
4. Run `python final_project/offline_note_summarizer.py final_project/sample_notes.txt`.
5. Point out the generated summary and that `local` is the default mode.
6. Optional: turn off Wi-Fi *after setup*, rerun locally, and show that it still responds.
7. Explain `--provider hosted` as opt-in only, without making a Gemini call if quota is unavailable.
8. Mention the previously recorded speed of 15.10 tokens/sec for 3B, and the need to verify generated facts.

Suggested closing line: "The tool summarizes notes locally with Ollama, keeping inference on-device by default. I selected Qwen2.5 3B for its memory fit and speed, and I leave hosted access optional."

Save a short MP4, e.g., `demo/week4_offline_first_demo.mp4`, and add a link to the root README when the recording exists. Keep video out of Git if too large; link an external hosting page if needed. Do not claim recorded until there is a working link.
