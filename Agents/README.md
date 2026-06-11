# Research Assistant Multi-Agent System

## Overview

The Research Assistant Multi-Agent System is an AI-powered application built using FastAPI, LangGraph, LangChain, and Groq LLM.

The system follows a multi-agent architecture where three specialized AI agents collaborate to transform a user-provided topic into detailed research notes, a concise summary, and a quiz.

Each agent is responsible for a specific task and passes its output to the next agent, demonstrating inter-agent communication and workflow orchestration.

---

# Features

* Topic-based research generation
* AI-powered content summarization
* Automatic quiz generation
* Multi-agent workflow
* LangGraph-based orchestration
* FastAPI Swagger interface
* Modular architecture
* Easy to extend with additional agents

---

# Multi-Agent Workflow

The application consists of three interconnected agents.

## Agent 1: Research Agent

### Responsibility

The Research Agent receives a topic from the user and generates comprehensive research notes.

### Tasks

* Topic analysis
* Information generation
* Concept extraction
* Structured content creation

### Output

* Introduction
* Definition
* Key Concepts
* Applications
* Advantages
* Challenges
* Future Scope

---

## Agent 2: Summary Agent

### Responsibility

The Summary Agent receives research content from the Research Agent and generates a concise summary.

### Tasks

* Extract key points
* Remove redundant information
* Create structured summaries
* Improve readability

### Output

* Short summary
* Important concepts
* Key takeaways

---

## Agent 3: Quiz Generator Agent

### Responsibility

The Quiz Generator Agent receives summarized content and generates multiple-choice questions.

### Tasks

* Content understanding
* Question generation
* Option generation
* Answer identification

### Output

* MCQs
* Correct answers

---

# System Architecture

User Input
↓
Research Agent
↓
Research Notes
↓
Summary Agent
↓
Summary
↓
Quiz Generator Agent
↓
MCQs + Answers

---

# Project Structure

```text
Agents/
│
├── research_agent/
│   ├── agents/
│   │   └── research_agent.py
│   ├── graph/
│   │   ├── state.py
│   │   ├── nodes.py
│   │   └── graph_builder.py
│   └── agent.yaml
│
├── summary_agent/
│   ├── agents/
│   │   └── summary_agent.py
│   ├── graph/
│   │   ├── state.py
│   │   ├── nodes.py
│   │   └── graph_builder.py
│   └── agent.yaml
│
├── quiz_generator_agent/
│   ├── agents/
│   │   └── quiz_generator_agent.py
│   ├── graph/
│   │   ├── state.py
│   │   ├── nodes.py
│   │   └── graph_builder.py
│   └── agent.yaml
│
├── main.py
├── requirements.txt
└── .env
```

---

# Technologies Used

## Backend

* Python
* FastAPI

## Agent Framework

* LangGraph
* LangChain

## Large Language Model

* Groq
* Llama 3.3 70B Versatile

## Configuration

* YAML
* Python Dotenv

---

# Installation

## Clone Repository

```bash
git clone <repository-url>
cd Agents
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Configuration

Create a .env file in the project root.

```env
GROQ_API_KEY=your_groq_api_key
```

---

# Running the Application

```bash
uvicorn main:app --reload
```

If port 8000 is unavailable:

```bash
uvicorn main:app --reload --port 8080
```

---

# Swagger Documentation

After running the application, open:

```text
http://127.0.0.1:8000/docs
```

or

```text
http://127.0.0.1:8080/docs
```

---

# API Endpoints

## Research Agent

### Endpoint

POST /research

### Request

```json
{
  "topic": "Artificial Intelligence"
}
```

### Response

```json
{
  "research_content": "Generated research notes..."
}
```

---

## Summary Agent

### Endpoint

POST /summarize

### Request

```json
{
  "research_content": "Generated research notes..."
}
```

### Response

```json
{
  "summary": "Generated summary..."
}
```

---

## Quiz Generator Agent

### Endpoint

POST /quiz

### Request

```json
{
  "summary": "Generated summary..."
}
```

### Response

```json
{
  "quiz": "Generated MCQs..."
}
```

---

# Benefits of Multi-Agent Architecture

* Modular design
* Easier maintenance
* Independent agent development
* Improved scalability
* Reusable agents
* Clear separation of responsibilities
* Better workflow management

---

# Future Enhancements

* Agent orchestration endpoint
* PDF report generation
* Research source citations
* Web search integration
* RAG-based retrieval
* Vector database support
* Multi-language support
* Agent monitoring dashboard

---

# Author
Siva Guru N
AI & Machine Learning Developer
Built using FastAPI, LangGraph, LangChain, and Groq LLM.
