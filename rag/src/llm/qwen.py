from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4]))
import config

_model = None
_tokenizer = None


def _load() -> None:
    global _model, _tokenizer
    if _model is not None:
        return
    from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
    import torch

    quant_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_compute_dtype=torch.float16,
        bnb_4bit_use_double_quant=True,
        bnb_4bit_quant_type="nf4",
    )
    _tokenizer = AutoTokenizer.from_pretrained(config.LLM_MODEL)
    _model = AutoModelForCausalLM.from_pretrained(
        config.LLM_MODEL,
        quantization_config=quant_config,
        device_map="auto",
        trust_remote_code=True,
    )
    _model.eval()


def generate(prompt: str) -> str:
    """Gọi Qwen3-4B (4-bit, thinking OFF) với prompt text, trả về raw string output."""
    _load()
    import torch

    messages = [{"role": "user", "content": prompt}]
    text = _tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
        enable_thinking=False,  # thinking OFF
    )
    inputs = _tokenizer(text, return_tensors="pt").to(_model.device)

    with torch.no_grad():
        output_ids = _model.generate(
            **inputs,
            max_new_tokens=config.LLM_MAX_NEW_TOKENS,
            temperature=config.LLM_TEMPERATURE,
            do_sample=False,
            pad_token_id=_tokenizer.eos_token_id,
        )

    # Chỉ decode phần generated (bỏ input tokens)
    generated = output_ids[0][inputs["input_ids"].shape[1]:]
    return _tokenizer.decode(generated, skip_special_tokens=True).strip()
