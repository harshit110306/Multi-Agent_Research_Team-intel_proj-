from agents.base_agent import BaseAgent

class ReportAgent(BaseAgent):
    def __init__(self, name, memory, llm):
        super().__init__(name, memory)
        self.llm = llm

    def generate_report(self):
        literature = self.memory.read("literature_summary")
        hypotheses = self.memory.read("hypotheses")
        accuracy = self.memory.read("model_accuracy")
        decision = self.memory.read("debate_decision")

        prompt = f"""
        Generate a structured IEEE-style research paper draft.

        Literature:
        {literature}

        Hypotheses:
        {hypotheses}

        Model Accuracy:
        {accuracy}

        Debate Conclusion:
        {decision}
        """

        report = self.llm.generate(prompt)

        self.memory.write("final_report", report)
        return report
