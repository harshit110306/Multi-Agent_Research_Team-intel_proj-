from memory.shared_memory import SharedMemory
from llm.llm_controller import LLMController

from agents.literature_agent import LiteratureAgent
from agents.hypothesis_agent import HypothesisAgent
from agents.model_agent import ModelAgent
from agents.debate_agent import DebateAgent
from agents.report_agent import ReportAgent
from agents.companion_agent import CompanionAgent
from agents.manager_agent import ManagerAgent
from storage.session_manager import SessionManager

def main():

    print("\n==== Personal AI Research Companion ====\n")

    # -----------------------------
    # 1️⃣ Select LLM Mode
    # -----------------------------
    provider = input("Select LLM provider (offline / online): ").strip().lower()

    if provider == "online":
        api_key = input("Enter ScaleDown API Key: ").strip()
        base_url = input("Enter ScaleDown Base URL: ").strip()
        model_name = input("Enter Model Name (example: gpt-4o-mini): ").strip()
        llm = LLMController(
            provider="online",
            api_key=api_key,
            base_url=base_url,
            model_name=model_name
        )
    else:
        llm = LLMController(provider="offline")

    # -----------------------------
    # 2️⃣ Initialize Memory
    # -----------------------------
    memory = SharedMemory()

    # -----------------------------
    # 3️⃣ Initialize Agents
    # -----------------------------
    agents = {
        "literature": LiteratureAgent("LiteratureAgent", memory, llm),
        "hypothesis": HypothesisAgent("HypothesisAgent", memory, llm),
        "model": ModelAgent("ModelAgent", memory),
        "debate": DebateAgent("DebateAgent", memory, llm),
        "report": ReportAgent("ReportAgent", memory, llm),
        "companion": CompanionAgent("CompanionAgent", memory, llm),
    }

    manager = ManagerAgent(agents)

    # -----------------------------
    # 4️⃣ Take Research Topic
    # -----------------------------
    topic = input("\nEnter your research topic: ")

    # -----------------------------
    # 5️⃣ Run Research Workflow
    # -----------------------------
    report = manager.run(topic)

    print("\n===== FINAL RESEARCH REPORT =====\n")
    print(report)

    # -----------------------------
    # 6️⃣ Companion Feedback
    # -----------------------------
    print("\n===== COMPANION ANALYSIS =====\n")
    companion_feedback = agents["companion"].analyze_research()
    print(companion_feedback)

    # -----------------------------
    # Save Session 
    # -----------------------------
    from storage.session_manager import SessionManager

    session_manager = SessionManager()
    file_path = session_manager.save_session(memory, topic)

    print(f"\n Session saved to: {file_path}")


    # -----------------------------
    # 7️⃣ Interactive Q&A Mode
    # -----------------------------
    print("\nYou can now ask questions about your research.")
    print("Type 'exit' to stop.\n")

    while True:
        question = input("Ask Companion: ")

        if question.lower() == "exit":
            print("\nSession ended. Goodbye 👋")
            break

        answer = agents["companion"].ask(question)

        print("\nCompanion Response:\n")
        print(answer)


if __name__ == "__main__":
    main()