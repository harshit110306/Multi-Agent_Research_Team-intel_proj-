from agents.base_agent import BaseAgent

class DebateAgent(BaseAgent):
    def __init__(self, name, memory, llm):
        super().__init__(name, memory)
        self.llm = llm

    def evaluate(self):
        accuracy = self.memory.read("model_accuracy")

        prompt = f"""
        The model achieved accuracy of {accuracy}.
        Evaluate whether this performance is acceptable for research publication.
        Provide justification.
        """

        decision = self.llm.generate(prompt)

        self.memory.write("debate_decision", decision)
        return decision
