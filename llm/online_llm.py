from openai import OpenAI
from llm.base_llm import BaseLLM
from llm.scaledown_client import ScaleDownClient


class OnlineLLM(BaseLLM):
    def __init__(self, model_name="gpt-4o-mini", api_key=None, base_url=None, scaledown_key=None):

        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url
        )

        self.model_name = model_name

        # Optional ScaleDown
        self.scaledown = None
        if scaledown_key:
            self.scaledown = ScaleDownClient(scaledown_key)

    def generate(self, prompt, temperature=0.7):

        # 🔥 If ScaleDown enabled → compress first
        if self.scaledown:
            print("Compressing prompt using ScaleDown...")
            prompt = self.scaledown.compress(
                context="Research AI system context",
                prompt=prompt
            )

        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature
        )

        return response.choices[0].message.content
