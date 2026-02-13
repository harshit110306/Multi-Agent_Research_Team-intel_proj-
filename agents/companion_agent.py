from agents.base_agent import BaseAgent

class CompanionAgent(BaseAgent):
    def __init__(self, name, memory, llm):
        super().__init__(name, memory)
        self.llm = llm

    def analyze_research(self):
        literature = self.memory.read("literature_summary")
        hypotheses = self.memory.read("hypotheses")
        accuracy = self.memory.read("model_accuracy")
        report = self.memory.read("final_report")

        prompt = f"""
        You are a Research Companion AI.

        Analyze the following research output:

        Literature:
        {literature}

        Hypotheses:
        {hypotheses}

        Model Accuracy:
        {accuracy}

        Report:
        {report}

        Provide:

        1. Suggestions for improvement
        2. Potential weaknesses
        3. Validation recommendations
        4. Possible source verification advice
        5. Guidance for next steps
        6. Simple explanation for beginner user
        """

        response = self.llm.generate(prompt)

        self.memory.write("companion_feedback", response)

        return response
    
    def ask(self, user_question):
        context = self.memory.show_all()

        prompt = f"""
        You are a personal AI research assistant.

        Based on this research context:
        {context}

        User question:
        {user_question}

        Provide a clear and helpful answer.
        """

        return self.llm.generate(prompt)
