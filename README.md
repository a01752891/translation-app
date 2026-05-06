# Language Translator — Qwen2-0.5B

**[▶ Live Demo](https://a01752891.github.io/translation-app/)** — runs entirely in the browser, no API keys needed.

A small translation app powered by [Qwen2-0.5B-Instruct](https://huggingface.co/Qwen/Qwen2-0.5B-Instruct). No external API keys required — the model can run in your browser or locally on your machine.

## Web Demo (GitHub Pages)

Open **https://a01752891.github.io/translation-app/** in any browser. The model downloads automatically (~400 MB on first visit, cached after).

## Supported Languages
English, Spanish, Portuguese, French, German

## Local Setup

```bash
pip install -r requirements.txt
```

## Run the web app

```bash
python app.py
```

Open the URL shown in the terminal (usually `http://127.0.0.1:7860`).

## Run the example translations

```bash
python test_examples.py
```

Expected output:
```
[English]  I like soccer
[Spanish]  Me gusta el fútbol

[English]  How are you?
[Spanish]  ¿Cómo estás?

[English]  What time is it?
[Spanish]  ¿Qué hora es?
```

## Notes
- First run downloads the model (~1 GB). Subsequent runs use the cached version.
- CPU is supported; GPU (CUDA) is used automatically if available for faster inference.
