from agents.base_agent import BaseAgent

class HypothesisAgent(BaseAgent):
    def __init__(self, name, memory, llm):
        super().__init__(name, memory)
        self.llm = llm

    def generate(self):
        literature = self.memory.read("literature_summary")

        prompt = f"""
        Based on this literature review:

        {literature}

        Generate 3 innovative and testable research hypotheses.
        """

        hypotheses = self.llm.generate(prompt)

        self.memory.write("hypotheses", hypotheses)
        return hypotheses
