class BaseLLM:
    def generate(self, prompt, temperature=0.7):
        raise NotImplementedError("Subclasses must implement this method.")
