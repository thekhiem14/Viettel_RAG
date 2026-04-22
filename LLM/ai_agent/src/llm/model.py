from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
import torch


MODEL_ID = "Qwen/Qwen3-4B"

THINK_START = "<think>"
THINK_END   = "</think>"


class QwenModel:
    def __init__(self, model_id: str = MODEL_ID):
        print(f"Đang load model: {model_id}")

        bnb_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_use_double_quant=True,
            bnb_4bit_compute_dtype=torch.float16,
        )

        self.tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_id,
            quantization_config=bnb_config,
            device_map="auto",
            trust_remote_code=True,
        )
        self.model.eval()
        print("Model ready.")

    def generate(
        self,
        prompt: str,
        thinking: bool = False,
        max_new_tokens: int = 512,
    ) -> str:
        """
        Gọi Qwen3 với prompt đã build sẵn.
        thinking=False → thêm /no_think vào system message (nhanh hơn, dùng cho call_document).
        thinking=True  → để model tự reason (dùng cho call_api).
        """
        system_content = "Bạn là trợ lý AI trả lời câu hỏi bằng tiếng Việt."
        if not thinking:
            system_content += " /no_think"

        messages = [
            {"role": "system", "content": system_content},
            {"role": "user",   "content": prompt},
        ]

        text = self.tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True,
        )
        inputs = self.tokenizer(text, return_tensors="pt").to(self.model.device)

        with torch.no_grad():
            output_ids = self.model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                do_sample=False,
                temperature=None,
                top_p=None,
            )

        # Chỉ lấy phần sinh mới
        new_ids = output_ids[0][inputs['input_ids'].shape[1]:]
        raw = self.tokenizer.decode(new_ids, skip_special_tokens=True).strip()

        # Loại bỏ thinking block nếu có
        if THINK_END in raw:
            raw = raw.split(THINK_END, 1)[-1].strip()

        return raw
