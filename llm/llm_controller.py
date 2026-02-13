from llm.offline_llm import OfflineLLM
from llm.online_llm import OnlineLLM


class LLMController:
    def __init__(self, provider="offline", model_name=None, api_key=None, base_url=None):

        self.provider = provider

        if provider == "online":
            print("Using Online LLM")
            self.llm = OnlineLLM(
                model_name=model_name or "gpt-4o-mini",
                api_key=api_key,
                base_url=base_url
            )
        else:
            print("Using Offline LLM")
            self.llm = OfflineLLM(
                model_name=model_name or "llama3.2:latest"
            )

    # 🔥 THIS METHOD WAS MISSING
    def generate(self, prompt, temperature=0.7):
        try:
            return self.llm.generate(prompt, temperature)
        except Exception as e:
            print("LLM error:", e)

            # Fallback if online fails
            if self.provider == "online":
                print("Switching to offline fallback...")
                self.llm = OfflineLLM()
                return self.llm.generate(prompt, temperature)
            else:
                raise e
class LLMController:
    def __init__(self, provider="offline", model_name=None,
                 api_key=None, base_url=None, scaledown_key=None):

        self.provider = provider

        if provider == "online":
            self.llm = OnlineLLM(
                model_name=model_name or "gpt-4o-mini",
                api_key=api_key,
                base_url=base_url,
                scaledown_key=scaledown_key
            )
        else:
            self.llm = OfflineLLM(
                model_name=model_name or "llama3.2:latest"
            )

    def generate(self, prompt, temperature=0.7):
        return self.llm.generate(prompt, temperature)

