from agents.base_agent import BaseAgent

class LiteratureAgent(BaseAgent):
    def __init__(self, name, memory, llm):
        super().__init__(name, memory)
        self.llm = llm

    def analyze_topic(self, topic):
        self.log("Analyzing literature using LLM...")

        prompt = f"""
        You are a research assistant.
        Provide a structured literature review summary on:
        {topic}

        Include:
        - Common methodologies
        - Dominant models
        - Identified limitations
        """

        summary = self.llm.generate(prompt)

        self.memory.write("literature_summary", summary)
        return summary
