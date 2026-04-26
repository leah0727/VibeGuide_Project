# 🧭 VibeGuide: Agentic AI Concierge
### A Personalized Recommendation System via RAG, Scraping MCP, and Multi-Agent Reasoning

---

## 📖 Project Overview

VibeGuide is a state-of-the-art intelligent concierge designed to bridge the gap between static user preferences and the dynamic real world. By integrating **Retrieval-Augmented Generation (RAG)** for personalization and a **Selenium-based Scraping MCP** for real-time data, VibeGuide delivers high-fidelity, context-aware itineraries curated by **Gemini 1.5 Flash**.

---

## 🛠 System Architecture & Workflow

The system operates through a collaborative **Multi-Agent pipeline**. Below is the step-by-step logic of how a single user request is processed:

| Step | Agent | Technology | Action / Output |
|------|-------|------------|-----------------|
| 1 | TasteProfiler | RAG (Local DB) | Retrieves user's historical "Vibe" (e.g., Industrial chic). |
| 2 | LocalScout | MCP (Selenium) | Launches a headless browser to scrape live Google Maps data. |
| 3 | Concierge | Gemini 1.5 | Reasons & synthesizes the final personalized Markdown plan. |
| 4 | Exporter | File-System MCP | Saves the final itinerary as a `.md` file to the local directory. |

---

## 📂 Project Structure

To maintain a modular and scalable "Agentic" design, the project is organized as follows:

```
vibeguide/
├── app.py           # Frontend — Streamlit interface that visualizes the agentic workflow
├── main.py          # Orchestrator — Manages logic flow between agents and Gemini
├── engine.py        # Memory (RAG) — Handles retrieval of user preferences from local metadata
├── scout_agent.py   # Eyes (MCP) — Selenium scraper logic for Google Maps interaction
├── data/            # Directory containing personal taste profiles (e.g., my_places.txt)
└── plan_*.md        # Automatically generated output files for the user
```

---

## 🚀 Core Pillar Descriptions

### 1. RAG (Retrieval-Augmented Generation)

- **The Problem:** Vanilla LLMs don't know the user's personal "Vibe" or saved places.
- **The Solution:** We utilize a RAG layer that injects specific aesthetic data (industrial, moody, minimalist) into the prompt. This ensures the output is tailored specifically to the user's history, not just general popularity.

### 2. MCP (Model Context Protocol) via Live Scraping

- **The Problem:** Static search APIs often lack direct map links or real-time UI data.
- **The Solution:** We implemented a **Scraping MCP**. The agent "acts" as a human by opening a browser, searching Google Maps, and extracting live URLs and venue names. This demonstrates the **Tool-Use** capability where the model controls external software to gain new knowledge.

### 3. Multi-Agent Reasoning

- **The Problem:** Complex tasks like "finding a place that matches a specific mood in a new city" are prone to hallucinations in single-prompt setups.
- **The Solution:** By splitting the task into specialized agents:
  - **Agent A** focuses on *Who* the user is (RAG).
  - **Agent B** focuses on *What* is available (Scraper).
  - **Agent C** focuses on *Why* they match (Gemini Reasoning).

---

## ⚙️ Technical Specification

| Component | Stack |
|-----------|-------|
| LLM Brain | Google Gemini 1.5 Flash |
| UI Framework | Streamlit |
| Web Automation | Selenium (ChromeDriver) |
| Search Engine | Google Maps (Direct Scraping) |
| Data Format | JSON (Input) / Markdown (Output) |

---

## 🎓 Academic Value (GenAI Perspective)

This project serves as a proof-of-concept for **Active AI Agents**. It demonstrates:

1. **Autonomous Tool Interaction** — Moving beyond text-in/text-out to browser control.
2. **Context-Awareness** — Blending long-term personal memory with short-term world state.
3. **Modular MAS Design** — Proving that specialized agents outperform monolithic prompts in complex, real-world utility tasks.
