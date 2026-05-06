from app import translate

EXAMPLES = [
    ("I like soccer",   "English", "Spanish"),
    ("How are you?",    "English", "Spanish"),
    ("What time is it?","English", "Spanish"),
]

if __name__ == "__main__":
    print("Qwen2-0.5B Translation Examples")
    print("=" * 40)
    for text, src, tgt in EXAMPLES:
        result = translate(text, src, tgt)
        print(f"[{src}]  {text}")
        print(f"[{tgt}] {result}")
        print()
