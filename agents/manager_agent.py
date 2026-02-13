class ManagerAgent:
    def __init__(self, agents):
        self.agents = agents

    def run(self, topic, verification=False, suggestions=False):
        print("\n--- Research Workflow Started ---\n")

        # Phase 1: Literature Review
        self.agents["literature"].analyze_topic(topic)

        # Phase 2: Hypothesis Generation
        self.agents["hypothesis"].generate()

        # Phase 3: Model Training
        self.agents["model"].train_model()

        # Phase 4: Debate Evaluation
        self.agents["debate"].evaluate()

        # Phase 5: Report Generation
        report = self.agents["report"].generate_report()

        # Optional Phase 6: Verification
        if verification and "verification" in self.agents:
            self.agents["verification"].verify()

        # Optional Phase 7: Suggestions
        if suggestions and "suggestion" in self.agents:
            self.agents["suggestion"].suggest_improvements()
        
        if "companion" in self.agents:
            companion_feedback = self.agents["companion"].analyze_research()
            print("\n===== COMPANION FEEDBACK =====\n")
            print(companion_feedback)


        print("\n--- Research Completed ---\n")

        return report
