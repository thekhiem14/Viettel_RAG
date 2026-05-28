from __future__ import annotations

import sys
import time
from pathlib import Path
import os
sys.path.insert(0, str(Path(__file__).resolve().parents[4]))
import config

_llm = None
_tokenizer = None
_sampling_params = None


def _load() -> None:
    global _llm, _tokenizer, _sampling_params
    if _llm is not None:
        return
    from vllm import LLM, SamplingParams
    from transformers import AutoTokenizer
    os.environ["VLLM_ATTENTION_BACKEND"] = "XFORMERS"

    _llm = LLM(
        model=config.LLM_MODEL,
        quantization=config.LLM_QUANTIZATION,
        dtype="float16",
        gpu_memory_utilization=0.55,
        max_model_len=2048,
        max_num_seqs=1,
        tensor_parallel_size=1,
        enforce_eager=True,
        swap_space=0,
        trust_remote_code=True,
    )
    _tokenizer = AutoTokenizer.from_pretrained(config.LLM_MODEL)
    _sampling_params = SamplingParams(
        temperature=config.LLM_TEMPERATURE,
        max_tokens=config.LLM_MAX_NEW_TOKENS,
    )


def generate(prompt: str) -> str:
    """Sinh text từ prompt qua vLLM, trả về raw output string."""
    _load()

    messages = [{"role": "user", "content": prompt}]
    text = _tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
        enable_thinking=False,
    )

    t0 = time.perf_counter()
    outputs = _llm.generate([text], _sampling_params, use_tqdm=False)
    elapsed = time.perf_counter() - t0

    output = outputs[0].outputs[0]
    n_input_tokens = len(outputs[0].prompt_token_ids)
    n_output_tokens = len(output.token_ids)
    tps = round(n_output_tokens / elapsed, 1) if elapsed > 0 else 0

    if not getattr(config, "DISABLE_CONSOLE_LOG", False):
        print(f"[llm] input_tokens={n_input_tokens}  output_tokens={n_output_tokens}  {elapsed*1000:.0f}ms  {tps}tok/s")

    return output.text.strip()
