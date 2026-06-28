# 🤖 Agentic AI Backend

An enterprise-grade **Agentic AI Backend** built with **Python**, **FastAPI**, **Google Gemini**, and a modular tool architecture. The system understands natural language, generates execution plans using an LLM, dynamically selects tools, executes real-world actions, and returns structured responses.

---

# 🚀 Project Overview

Traditional AI systems answer questions.

**Agentic AI** goes a step further.

Instead of only generating text, it can:

* Understand user intent
* Plan multiple execution steps
* Select appropriate tools
* Execute real-world operations
* Return structured execution results

This project demonstrates how enterprise AI agents are designed using clean architecture and scalable engineering principles.

---

# ✨ Current Features

* ✅ Google Gemini LLM Integration
* ✅ AI-powered Planner
* ✅ JSON Response Parsing
* ✅ Dynamic Tool Registry
* ✅ Agent State Management
* ✅ Execution Engine
* ✅ GitHub REST API Integration
* ✅ Automatic GitHub Repository Creation
* ✅ Layered Enterprise Architecture
* ✅ Centralized Logging
* ✅ Configuration Management using Environment Variables

---

# 🏗️ High-Level Architecture

```text
                User Query
                     │
                     ▼
              Agent Core
                     │
                     ▼
             Gemini AI Provider
                     │
                     ▼
              AI Planner
                     │
                     ▼
             Execution Plan
                     │
                     ▼
               Executor
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
    GitHub Tool            Jira Tool (Upcoming)
          │
          ▼
    GitHub Service
          │
          ▼
     GitHub Client
          │
          ▼
     GitHub REST API
```

---

# 🛠️ Technology Stack

| Category        | Technology        |
| --------------- | ----------------- |
| Language        | Python 3.12+      |
| API Framework   | FastAPI           |
| AI Provider     | Google Gemini     |
| HTTP Client     | Requests          |
| Configuration   | Pydantic Settings |
| Logging         | Loguru            |
| Version Control | Git & GitHub      |
| Testing         | Pytest            |
| Database        | MySQL (Upcoming)  |

---

# 📂 Project Structure

```text
agentic-ai-backend/
│
├── app/
│   ├── agent/
│   ├── ai/
│   ├── config/
│   ├── integrations/
│   ├── models/
│   ├── prompts/
│   ├── services/
│   ├── tools/
│   └── utils/
│
├── playground/
├── tests/
├── docs/
├── README.md
├── requirements.txt
├── .env.example
└── run.py
```

---

# ⚙️ Setup Instructions

## 1. Clone the Repository

```bash
git clone https://github.com/<YOUR_USERNAME>/agentic-ai-backend.git

cd agentic-ai-backend
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv .venv
```

### Linux / macOS

```bash
python3 -m venv .venv
```

---

## 3. Activate Virtual Environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Configure Environment Variables

Copy the sample environment file.

### Windows

```bash
copy .env.example .env
```

### Linux / macOS

```bash
cp .env.example .env
```

Update the following values:

* GEMINI_API_KEY
* GITHUB_TOKEN

---

# ▶️ Running the Project

## Verify Configuration

```bash
python -m playground.settings_demo
```

---

## Verify Gemini

```bash
python -m playground.gemini_demo
```

---

## Verify GitHub Connection

```bash
python -m playground.github_user_demo
```

---

## Create GitHub Repository

```bash
python -m playground.github_create_repo_demo
```

---

## Execute the Complete Agent

```bash
python -m playground.agent_demo
```

---

# 🧠 Current Workflow

```text
Natural Language Query

        │

        ▼

Gemini AI

        │

        ▼

Execution Planning

        │

        ▼

Tool Selection

        │

        ▼

Business Service

        │

        ▼

GitHub REST API

        │

        ▼

Repository Created
```

---

# 📈 Roadmap

## Phase 1

* [x] Project Setup
* [x] Configuration Module
* [x] Logging
* [x] Agent State
* [x] Gemini Integration
* [x] Prompt Engineering
* [x] AI Planner
* [x] JSON Parser
* [x] Executor
* [x] Tool Registry
* [x] GitHub Integration

## Phase 2

* [ ] Jira Integration
* [ ] Multi-Step Planning
* [ ] Tool Discovery
* [ ] Memory Management
* [ ] REST API Endpoints
* [ ] MySQL Integration
* [ ] Authentication
* [ ] Docker Support

## Phase 3

* [ ] Background Jobs
* [ ] Multi-Agent Collaboration
* [ ] Slack Integration
* [ ] Jenkins Integration
* [ ] GitLab Integration
* [ ] CI/CD Pipeline
* [ ] Kubernetes Deployment

---

# 🤝 Contributing

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push your branch.
5. Create a Pull Request.

---

# 📄 License

This project is currently intended for educational, research, and enterprise proof-of-concept purposes.

---

# 👨‍💻 Author

**Vivek Tiwari**

Enterprise Agentic AI Backend using Python, FastAPI, Google Gemini, and modular enterprise architecture.
