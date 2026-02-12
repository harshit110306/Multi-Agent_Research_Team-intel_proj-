# ⚛ QuantumSage – AI Research Command Center

> A Cinematic Multi-Agent AI Research Platform for Document Review & Research Generation

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![LLM](https://img.shields.io/badge/LLM-Llama3.2-purple)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 🧠 Overview

QuantumSage is a futuristic AI-powered Research Operating System that:

- 📄 Reviews and analyzes research documents
- 📝 Generates structured research from a topic
- 🤖 Simulates a multi-agent research team
- 📊 Scores publication readiness
- 🧪 Suggests methodology improvements & roadmap
- ⚛ Provides a cinematic AI experience

---

# 🚀 Features

## 🔹 Multi-Agent Simulation
Simulates:
- 📚 Literature Expert
- 🧪 Methodology Expert
- 📊 Data Scientist
- 🏆 Publication Advisor
- 🧠 Research Companion

---

## 🔹 Document Review Mode
Upload:
- PDF
- DOCX
- TXT

QuantumSage:
- Extracts text
- Analyzes structure
- Detects research gaps
- Suggests improvements
- Provides roadmap
- Scores publication readiness

---

## 🔹 Research Generation Mode
Enter a topic and QuantumSage:
- Generates structured research
- Suggests datasets & models
- Recommends validation methods
- Provides experimental insights

---

## 🔹 Cinematic AI Interface
- 🌌 Animated sci-fi background
- ⚛ Research flow tracker
- 🤖 Multi-agent chat simulation
- 📊 Animated score bars
- 🎉 Confetti celebration for high scores

---

# 📂 Project Structure

```

QuantumSage/
│
├── app.py
├── agents/
├── llm/
├── memory/
├── storage/
├── static/
│   └── index.html
├── assets/
├── requirements.txt
└── README.md

````

---

# 🛠 Installation Guide

## 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/QuantumSage.git
cd QuantumSage
````

---

## 2️⃣ Create Virtual Environment (Recommended)

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

If you don’t have requirements.txt, install manually:

```bash
pip install fastapi uvicorn python-multipart PyPDF2 python-docx requests
```

---

# 🤖 LLM Setup

QuantumSage supports:

* Offline Mode (Llama 3.2 via Ollama)
* Optional Online Mode

---

## 🔹 Offline LLM Setup (Recommended)

### Install Ollama

Download from:
[https://ollama.com](https://ollama.com)

### Pull Llama Model

```bash
ollama pull llama3.2
```

### Start Ollama

```bash
ollama run llama3.2
```

Or keep Ollama running in background.

---

# ▶️ Run QuantumSage

```bash
uvicorn app:app --reload
```

Open browser:

```
http://127.0.0.1:8000
```

---

# 🌐 Optional Online LLM Setup

If using ScaleDown or OpenAI-compatible API:

1. Add API key inside your LLM controller
2. Pass provider="online"

You can modify:

```python
LLMController(provider="online")
```

---

# 🖼 Adding Demo Screenshots

Create folder:

```
assets/
```

Add:

* dashboard.png
* document_review.png
* research_output.png
* score.png
* demo.gif

Then reference in README:

```markdown
![Dashboard](assets/dashboard.png)
```

---

# 🎥 How to Record Demo GIF

Use:

* ScreenToGif (Windows)
* OBS Studio
* Kap (Mac)

Record:

* Upload document
* Show analysis
* Show score animation

Export as:

```
assets/demo.gif
```

---

# 🧠 System Architecture

```
User Input
   ↓
Document Extractor
   ↓
ScaleDown Compression (Optional)
   ↓
LLM Controller (Offline / Online)
   ↓
Multi-Agent Simulation
   ↓
Structured Research Output
   ↓
Cinematic UI Rendering
```

---

# 🔮 Future Enhancements

* 🔄 Real-time token streaming
* 📊 Research visualization graphs
* 📁 Export PDF reports
* 🌍 Cloud deployment
* 🔐 Authentication system
* 🤖 Voice AI interaction

---

# 👨‍💻 Author

Harshit Bodala

---

# ⭐ Support

If you like this project:

⭐ Star the repository
🍴 Fork it
🚀 Share it

---

# 📜 License

MIT License

```
