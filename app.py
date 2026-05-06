import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import gradio as gr

MODEL_NAME = "Qwen/Qwen2-0.5B-Instruct"

device = "cuda" if torch.cuda.is_available() else "cpu"
dtype = torch.float16 if torch.cuda.is_available() else torch.float32

print(f"Loading {MODEL_NAME} on {device}...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, torch_dtype=dtype).to(device)
print("Model ready!\n")


def translate(text: str, source_lang: str, target_lang: str) -> str:
    if not text.strip():
        return ""

    messages = [
        {
            "role": "user",
            "content": (
                f"Translate the following {source_lang} text to {target_lang}. "
                f"Reply with ONLY the translation, no explanations.\n\n"
                f"Text: {text}"
            ),
        }
    ]

    prompt = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )
    inputs = tokenizer(prompt, return_tensors="pt").to(device)

    with torch.no_grad():
        output_ids = model.generate(
            **inputs,
            max_new_tokens=150,
            do_sample=False,
            pad_token_id=tokenizer.eos_token_id,
        )

    new_ids = output_ids[0][inputs["input_ids"].shape[1]:]
    return tokenizer.decode(new_ids, skip_special_tokens=True).strip()


EXAMPLES = [
    ["I like soccer", "English", "Spanish"],
    ["How are you?", "English", "Spanish"],
    ["What time is it?", "English", "Spanish"],
]

with gr.Blocks(title="Qwen2-0.5B Translator") as demo:
    gr.Markdown("# Language Translator — Qwen2-0.5B")
    gr.Markdown("Translate text between languages using the Qwen2-0.5B model (no external API keys required).")

    with gr.Row():
        src = gr.Dropdown(
            choices=["English", "Spanish", "Portuguese", "French", "German"],
            value="English",
            label="Source Language",
        )
        tgt = gr.Dropdown(
            choices=["Spanish", "Portuguese", "English", "French", "German"],
            value="Spanish",
            label="Target Language",
        )

    txt_in = gr.Textbox(label="Text to translate", lines=3, placeholder="Enter text here...")
    btn = gr.Button("Translate", variant="primary")
    txt_out = gr.Textbox(label="Translation", lines=3, interactive=False)

    btn.click(fn=translate, inputs=[txt_in, src, tgt], outputs=txt_out)

    gr.Examples(
        examples=EXAMPLES,
        inputs=[txt_in, src, tgt],
        label="Example phrases",
    )

if __name__ == "__main__":
    demo.launch()
