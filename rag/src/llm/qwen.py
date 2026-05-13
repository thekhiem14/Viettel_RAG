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
    from transformers import AutoModelForCausalLM, AutoTokenizer
    import torch

    has_cuda = torch.cuda.is_available()

    if has_cuda:
        model_kwargs = dict(
            torch_dtype=torch.bfloat16,
            device_map="auto",
        )
    else:
        # CPU fallback — chạy chậm hơn nhưng không crash
        model_kwargs = dict(
            torch_dtype=torch.float32,
            device_map="cpu",
        )

    _tokenizer = AutoTokenizer.from_pretrained(config.LLM_MODEL)
    _model = AutoModelForCausalLM.from_pretrained(
        config.LLM_MODEL,
        trust_remote_code=True,
        **model_kwargs,
    )
    _model.eval()


def generate(prompt: str) -> str:
    """Gọi Qwen3-4B (thinking OFF) với prompt text, trả về raw string output."""
    _load()
    import time
    import torch

    device = "cuda" if torch.cuda.is_available() else "cpu"
    messages = [{"role": "user", "content": prompt}]
    text = _tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
        enable_thinking=False,
    )

    t0 = time.perf_counter()
    inputs = _tokenizer(text, return_tensors="pt").to(device)
    n_input_tokens = inputs["input_ids"].shape[1]
    ms_tokenize = round((time.perf_counter() - t0) * 1000)

    t1 = time.perf_counter()
    with torch.no_grad():
        output_ids = _model.generate(
            **inputs,
            max_new_tokens=config.LLM_MAX_NEW_TOKENS,
            temperature=config.LLM_TEMPERATURE,
            do_sample=False,
            pad_token_id=_tokenizer.eos_token_id,
        )
    ms_generate = round((time.perf_counter() - t1) * 1000)

    generated = output_ids[0][n_input_tokens:]
    n_output_tokens = generated.shape[0]
    tps = round(n_output_tokens / (ms_generate / 1000), 1) if ms_generate > 0 else 0

    print(f"[llm] tokenize={ms_tokenize}ms  input_tokens={n_input_tokens}  generate={ms_generate}ms  output_tokens={n_output_tokens}  {tps}tok/s")

    return _tokenizer.decode(generated, skip_special_tokens=True).strip()