from fastapi import FastAPI, Form, UploadFile, File
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

import PyPDF2
from docx import Document

from memory.shared_memory import SharedMemory
from llm.llm_controller import LLMController

from agents.literature_agent import LiteratureAgent
from agents.hypothesis_agent import HypothesisAgent
from agents.model_agent import ModelAgent
from agents.debate_agent import DebateAgent
from agents.report_agent import ReportAgent
from agents.companion_agent import CompanionAgent

from storage.session_manager import SessionManager

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


# -----------------------------
# Home Page
# -----------------------------
@app.get("/")
def home():
    return FileResponse("static/index.html")


# -----------------------------
# List Saved Sessions
# -----------------------------
@app.get("/sessions")
def list_sessions():
    manager = SessionManager()
    return manager.list_sessions()


# -----------------------------
# Load Specific Session
# -----------------------------
@app.get("/sessions/{filename}")
def load_session(filename: str):
    manager = SessionManager()
    return manager.load_session(filename)


# -----------------------------
# EXISTING RESEARCH WORKFLOW (UNCHANGED)
# -----------------------------
@app.post("/run")
def run_research(
    topic: str = Form(...),
    provider: str = Form("offline"),
    api_key: str = Form(None),
    base_url: str = Form(None),
    model_name: str = Form(None),
    scaledown_key: str = Form(None),
):

    memory = SharedMemory()

    llm = LLMController(
        provider=provider,
        api_key=api_key,
        base_url=base_url,
        model_name=model_name,
        scaledown_key=scaledown_key
    )

    agents = {
        "literature": LiteratureAgent("LiteratureAgent", memory, llm),
        "hypothesis": HypothesisAgent("HypothesisAgent", memory, llm),
        "model": ModelAgent("ModelAgent", memory),
        "debate": DebateAgent("DebateAgent", memory, llm),
        "report": ReportAgent("ReportAgent", memory, llm),
        "companion": CompanionAgent("CompanionAgent", memory, llm),
    }

    # Run workflow
    agents["literature"].analyze_topic(topic)
    agents["hypothesis"].generate()
    agents["model"].train_model()
    agents["debate"].evaluate()
    report = agents["report"].generate_report()
    companion_feedback = agents["companion"].analyze_research()

    # Save session
    session_manager = SessionManager()
    session_manager.save_session(memory, topic)

    return {
        "report": report,
        "companion_feedback": companion_feedback
    }

# =====================================================
# 🔥 NEW PRIMARY FEATURE — DOCUMENT ANALYSIS
# =====================================================

def extract_text_from_file(uploaded_file: UploadFile):

    filename = uploaded_file.filename.lower()

    if filename.endswith(".txt"):
        return uploaded_file.file.read().decode("utf-8")

    elif filename.endswith(".pdf"):
        reader = PyPDF2.PdfReader(uploaded_file.file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text

    elif filename.endswith(".docx"):
        doc = Document(uploaded_file.file)
        return "\n".join([para.text for para in doc.paragraphs])

    else:
        return "Unsupported file format."


@app.post("/analyze_document")
def analyze_document(
    file: UploadFile = File(...),
    provider: str = Form("offline"),
    api_key: str = Form(None),
    base_url: str = Form(None),
    model_name: str = Form(None),
    scaledown_key: str = Form(None),
):

    memory = SharedMemory()

    # Extract document text
    extracted_text = extract_text_from_file(file)

    llm = LLMController(
        provider=provider,
        api_key=api_key,
        base_url=base_url,
        model_name=model_name,
        scaledown_key=scaledown_key
    )

    prompt = f"""
    Analyze the following research document:

    {extracted_text}

    Provide:
    - Executive Summary
    - Strengths
    - Weaknesses
    - Methodology evaluation
    - Validation suggestions
    - Publication readiness score (0-100)
    - Improvement roadmap
    """

    analysis = llm.generate(prompt)

    # Save document session
    memory.write("document_analysis", analysis)
    session_manager = SessionManager()
    session_manager.save_session(memory, file.filename)

    return {
        "analysis": analysis
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
