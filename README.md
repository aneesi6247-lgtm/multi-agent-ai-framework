# Multi-Agent AI Framework

A collection of LLM-powered agents built on the [Agno](https://github.com/agno-agi/agno) framework, exploring autonomous video analysis, persistent memory, and coordinated multi-agent translation.

## Projects

### 🎥 YouTube Intelligence Agent
Analyzes any YouTube video and produces structured timestamps, topic summaries, and key insights. Deployed as a Streamlit web app with real-time response streaming.

```bash
streamlit run deploy_with_stream.py
```

- Generates precise `[start_time, end_time, summary]` segments
- Classifies content type (tutorial, review, lecture, etc.)
- Processed 100+ videos during development/testing

**Files:** `Youtube_video_analyzer.py`, `deploy_with_stream.py`

### 🧠 Persistent Memory Agent
A stateful agent using SQLite to retain conversational context across sessions, enabling multi-turn dialogue without losing prior context between runs.

**Files:** `Memory.py`

### 🌐 Multilingual Translation Team
Three specialized agents (English, German, Urdu) coordinated in parallel by a `Team` orchestrator, each translating input into its target language, with DuckDuckGo search augmentation for context.

**Files:** `Language_team.py`

### 🔎 General Research Agent
A baseline agent wired up with web search tools for open-ended Q&A and current-events lookups.

**Files:** `agent.py`



## Stack

Agno Framework · OpenAI API (GPT models) · SQLite · DuckDuckGo Search · Streamlit · Python

