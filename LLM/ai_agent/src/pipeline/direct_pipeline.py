from src.llm.model import QwenModel


PROMPT_TEMPLATE = """\
{question}"""


class DirectPipeline:
    """
    Pipeline cho call_api: gọi thẳng local model, không qua retrieval.
    Thinking được bật để model có thể reason tốt hơn.
    """

    def __init__(self, llm: QwenModel):
        self.llm = llm

    def run(self, question: str) -> str:
        prompt = PROMPT_TEMPLATE.format(question=question)
        return self.llm.generate(prompt, thinking=True, max_new_tokens=1024)
