import ollama
from llm.base_llm import BaseLLM

class OfflineLLM(BaseLLM):
    def __init__(self, model_name="llama3.2:latest"):
        self.model_name = model_name

    def generate(self, prompt, temperature=0.7):
        response = ollama.chat(
            model=self.model_name,
            messages=[{"role": "user", "content": prompt}],
            options={"temperature": temperature}
        )
        return response["message"]["content"]
