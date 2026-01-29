# 🤖 Agentic AI Job Copilot (LangGraph + LLM + Semantic Search)

An end-to-end **agentic AI system** that discovers real job postings, understands job descriptions using LLMs, semantically matches them to your resume, and automatically prioritizes roles for application.

This project demonstrates a modern **multi-agent architecture** built with LangGraph, combining:

* LLM-based structured understanding
* Weighted rule-based scoring
* Semantic embeddings similarity
* Autonomous decision-making (APPLY / MAYBE / SKIP)

Designed for AI Engineer, ML Engineer, and Data Scientist roles.

---

## 🚀 Key Features

* 🔍 **Job Discovery Agent**
  Fetches real job postings from a live API.

* 🧠 **LLM-Based JD Understanding**
  Uses an LLM to extract structured information from job descriptions:

  * Required skills
  * Role type
  * Seniority level

* ⚖️ **Weighted Skill Matching (v2 Matcher)**
  Matches resume skills to JD requirements with:

  * Critical skill weighting
  * Synonym normalization
  * Skill gap detection

* 🎯 **Role-Aware Prioritization**
  Automatically boosts scores for target roles:

  * AI Engineer
  * ML Engineer
  * Data Scientist

* 🧬 **Semantic Embeddings Ranking**
  Uses sentence-transformer embeddings to compute semantic similarity between:

  * Resume text
  * Job description text

* 🤖 **Supervisor Agent (Decision Maker)**
  Combines multiple signals into a hybrid final score:

  ```
  final_score = 0.7 * rule_based_score + 0.3 * semantic_similarity_score
  ```

  Automatically classifies jobs as:

  * APPLY
  * MAYBE
  * SKIP

---

## 🏗️ System Architecture

```text
Resume Agent
     ↓
Job Search Agent  ──▶ Real Job API
     ↓
Supervisor Agent (Brain)
     ├─ LLM JD Extractor
     ├─ Weighted Skill Matcher (v2)
     ├─ Role-Based Boosting
     ├─ Semantic Embeddings Similarity
     ↓
Ranked Jobs (APPLY / MAYBE / SKIP)
```

The Supervisor Agent orchestrates reasoning and decision-making, while perception modules (LLM + embeddings) provide deep understanding of job requirements.

---

## 📊 Hybrid Scoring Logic

Each job is evaluated using two complementary signals:

### 1. Rule-Based + LLM Signal (70%)

* LLM-extracted required skills
* Weighted critical skills (Python, ML, DL, PyTorch, etc.)
* Role match bonus for AI/ML/Data Scientist roles

### 2. Semantic Similarity Signal (30%)

* Sentence embeddings of resume and JD
* Cosine similarity to capture meaning-level match

This hybrid approach improves robustness and accuracy over keyword-only systems.

---

## 🧩 Tech Stack

* **LangGraph** — Multi-agent orchestration
* **LangChain** — LLM + tooling
* **HuggingFace Inference API** — LLM (Mistral Instruct)
* **sentence-transformers** — Semantic embeddings
* **Python** — Core system logic
* **dotenv** — Environment configuration

---

## 📁 Project Structure

```text
job_agent/
├── langgraph_main.py        # LangGraph workflow
├── supervisor_agent.py     # Main decision-making agent
├── job_search_agent.py     # Job discovery agent
├── resume_agent.py         # Resume parsing agent
├── llm_jd_extractor.py     # LLM-based JD understanding
├── matcher.py              # v2 weighted skill matcher
├── embeddings.py           # Semantic embeddings + similarity
├── utils.py                # Cleaning + normalization utilities
├── state.py                # Shared agent state schema
├── .env.jobbot             # Environment variables
└── README.md               # Project documentation
```

---

## ⚙️ Setup & Installation

### 1. Clone the repo

```bash
git clone https://github.com/your-username/agentic-job-copilot.git
cd agentic-job-copilot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
pip install sentence-transformers
```

### 3. Configure environment

Create a `.env.jobbot` file:

```env
HUGGINGFACEHUB_API_TOKEN=your_hf_token
LANGCHAIN_TRACING_V2=false
LANGCHAIN_API_KEY=
```

Make sure this file is explicitly loaded in your main entry point.

---

## ▶️ Run the System

```bash
python langgraph_main.py
```

You will see ranked results like:

```text
APPLY | 65% | Senior Independent AI Engineer / Architect | A.Team
MAYBE | 48% | Sr/Staff AI Engineer | Company
SKIP  | 10% | Marketing Manager | Company
```

---

## 🧠 Why This Project Is Different

Unlike basic job bots, this system:

* Uses LLMs for true JD understanding
* Applies weighted, role-aware scoring
* Incorporates semantic similarity
* Separates perception from decision-making
* Implements a real multi-agent architecture

This mirrors how modern enterprise ATS and recruiter AI tools are designed.

---

## 🚧 Roadmap

* ✨ Auto cover letter generation agent
* 👤 Human-in-the-loop approval flow
* 📄 Job-fit explanations & summaries
* 🤖 Semi-automated application assistant
* 📊 Dashboard for tracking applications

---

## 👤 Author

Built by Golugoodboy
Agentic AI | LangGraph | LLM Systems | Applied AI Engineering

---

## ⭐ If You Like This Project

Star the repo and feel free to fork or contribute!

This project is intended as a learning + portfolio showcase for modern agentic AI system design.
