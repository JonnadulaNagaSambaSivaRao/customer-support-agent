# 🎧 Customer Support AI Agent

<p align="center">

<img src="https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white">

<img src="https://img.shields.io/badge/Google-Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white">

<img src="https://img.shields.io/badge/MCP-Model%20Context%20Protocol-8A2BE2?style=for-the-badge">

<img src="https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white">

<img src="https://img.shields.io/badge/uv-Package%20Manager-DE5FE9?style=for-the-badge">

<img src="https://img.shields.io/badge/Cursor-IDE-000000?style=for-the-badge&logo=cursor&logoColor=white">

</p>

<p align="center">

<b>🤖 Autonomous Customer Support Agent powered by Gemini, MCP & SQLite</b>

</p>

<p align="center">

🔎 Search → 📄 Retrieve → 🧠 Analyze → ✏️ Update → ✅ Verify

</p>

---

## 📌 Table of Contents

- [🌟 Project Overview](#-project-overview)
- [✨ Features](#-features)
- [🏗️ Architecture](#️-architecture)
- [🔄 Agent Workflow](#-agent-workflow)
- [🧰 Technology Stack](#-technology-stack)
- [📁 Project Structure](#-project-structure)
- [🗄️ Database Schema](#️-database-schema)
- [💬 Example Usage](#-example-usage)
- [🔄 Multi-Step Task Example](#-multi-step-task-example)
- [🖥️ Cursor MCP Integration](#️-cursor-mcp-integration)
- [🧠 How the Autonomous Loop Works](#-how-the-autonomous-loop-works)
- [🛠️ Troubleshooting](#️-troubleshooting)
- [🔐 Security](#-security)
- [🚀 Future Improvements](#-future-improvements)


---

# 🌟 Project Overview

The **Customer Support AI Agent** is an autonomous customer-support application that combines **Google Gemini**, **Model Context Protocol (MCP)**, and **SQLite**.

The application allows users to interact with a customer-support database using natural language.

Instead of manually deciding which database operation to perform, Gemini can reason about the request and select the appropriate MCP tool.

### Example

A user can simply ask:

```text
Find John's open tickets and resolve his high-priority login issue.



👤 User
   ↓
🧠 Gemini
   ↓
🔎 Search Tickets
   ↓
🗄️ SQLite
   ↓
🧠 Gemini
   ↓
📄 Get Ticket Details
   ↓
🗄️ SQLite
   ↓
🧠 Gemini
   ↓
✏️ Update Ticket
   ↓
🗄️ SQLite
   ↓
🧠 Gemini
   ↓
✅ Final Answer

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔎 Search Tickets | Search tickets by customer, email, keyword, status, or priority |
| 📄 Get Ticket | Retrieve complete ticket details |
| ✏️ Update Ticket | Update status, priority, or assignee |
| ➕ Create Ticket | Create new customer-support tickets |
| 🧠 Gemini Reasoning | Gemini decides which tools are required |
| 🔄 Multi-Step Tasks | Execute multiple MCP tools automatically |
| 🗄️ SQLite Backend | Persist support tickets in a real database |
| 🔌 MCP Integration | Expose database operations as MCP tools |
| 💬 CLI Chatbot | Continue chatting until `exit` |
| 🖥️ Cursor Support | Connect the MCP server to Cursor |
| 🔐 Environment Variables | Keep API keys outside source code |

---

## 🏗️ Architecture

The project contains three major layers:

```text
┌─────────────────────────────────────────────┐
│                  👤 USER                    │
│                                             │
│        Natural Language Request             │
└──────────────────────┬──────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────┐
│               🧠 GEMINI AI                  │
│                                             │
│        Reasoning + Tool Selection           │
└──────────────────────┬──────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────┐
│               🔌 MCP CLIENT                 │
│                                             │
│       Communicates with MCP Server          │
└──────────────────────┬──────────────────────┘
                       │
                       │ MCP
                       ▼
┌─────────────────────────────────────────────┐
│               🛠️ MCP SERVER                │
│                                             │
│  search_tickets                             │
│  get_ticket                                 │
│  update_ticket                              │
│  create_ticket                              │
└──────────────────────┬──────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────┐
│               🗄️ SQLite                    │
│                                             │
│              support.db                     │
│                  tickets                    │
└─────────────────────────────────────────────┘

---

##🔄 Agent Workflow

The agent follows an autonomous tool-calling cycle.

                 👤 USER
                    │
                    ▼
          "Find John's open tickets"
                    │
                    ▼
              🧠 GEMINI
                    │
                    ▼
          Need database information?
                    │
                    ▼
              🔎 SEARCH TOOL
                    │
                    ▼
                🗄️ SQLITE
                    │
                    ▼
             Search Result
                    │
                    ▼
              🧠 GEMINI
                    │
             Need more information?
                /          \
              YES           NO
               │             │
               ▼             ▼
        📄 GET TICKET    ✅ FINAL ANSWER
               │
               ▼
           🗄️ SQLITE
               │
               ▼
          Ticket Details
               │
               ▼
           🧠 GEMINI
               │
               ▼
        Need another tool?
               │
               ▼
        ✏️ UPDATE TICKET
               │
               ▼
           🗄️ SQLITE
               │
               ▼
           🧠 GEMINI
               │
               ▼
         ✅ FINAL ANSWER

---

##🧰 Technology Stack

| Technology       | Purpose                               |
| ---------------- | ------------------------------------- |
| 🐍 Python 3.12+  | Application development               |
| 🧠 Google Gemini | AI reasoning and tool selection       |
| 🔌 MCP           | AI-to-tool communication              |
| 🗄️ SQLite       | Ticket database                       |
| ⚡ uv             | Python package/environment management |
| 🖥️ Cursor       | Development and MCP integration       |
| 🔐 python-dotenv | Environment variable management       |

---

##📁 Project Structure

The multi-file version of the project is organized as follows:

customer-support-agent/
│
├── 📁 .cursor/
│   └── mcp.json
│
├── 📁 .venv/
│
├── 🔐 .env
├── 🚫 .gitignore
├── 📦 pyproject.toml
├── 📖 README.md
│
├── 🤖 agent.py
├── 🖥️ main.py
├── 🔌 mcp_support.py
├── 🗄️ init_db.py
│
└── 💾 support.db

---

##🗄️ Database Schema

The application uses a SQLite database named:

support.db

The database contains a tickets table.

tickets
│
├── id
├── customer_name
├── email
├── subject
├── description
├── priority
├── status
├── assigned_to
├── created_at
└── updated_at
---

##▶️ Run the Application

From the project directory:

uv run python main.py

Expected output:

=================================================================
        🎧 CUSTOMER SUPPORT AI AGENT
=================================================================

The agent can:
  🔎 Search tickets
  📄 Retrieve ticket details
  ✏️ Update tickets
  ➕ Create tickets
  🔄 Perform multi-step tasks

Type 'exit' to quit.
=================================================================

✅ MCP server connected

👤 You:

---

##🧠 How the Autonomous Loop Works

The agent does not simply make one Gemini request.

It runs a loop:
User Request
     │
     ▼
   Gemini
     │
     ▼
Does Gemini need a tool?
     │
   YES
     │
     ▼
 MCP Tool
     │
     ▼
 SQLite
     │
     ▼
 Tool Result
     │
     ▼
   Gemini
     │
     ├───────────────┐
     │               │
     ▼               ▼
 Another Tool      No Tool
     │               │
     ▼               ▼
   SQLite        Final Answer
     │
     ▼
   Gemini

🔍 Example: Search → Retrieve → Update → Verify

A typical support workflow can look like:
👤 User
 │
 │ "Resolve John's login issue"
 ▼
🧠 Gemini
 │
 ▼
🔎 Search Tickets
 │
 ▼
🗄️ SQLite
 │
 ▼
📄 Get Ticket
 │
 ▼
🗄️ SQLite
 │
 ▼
🧠 Gemini
 │
 ▼
✏️ Update Ticket
 │
 ▼
🗄️ SQLite
 │
 ▼
🧠 Gemini
 │
 ▼
🔎 Verify
 │
 ▼
🗄️ SQLite
 │
 ▼
✅ Final Answer

---

##🔐 Security

Never commit your Gemini API key.

Your .gitignore should include:
.env
.venv/
__pycache__/
*.pyc
support.db

---

##🎯 Learning Objectives

This project demonstrates:
                    AI AGENTS
                       │
          ┌────────────┼────────────┐
          │            │            │
          ▼            ▼            ▼
       Gemini         MCP         SQLite
          │            │            │
          └────────────┼────────────┘
                       │
                       ▼
                Tool Calling
                       │
                       ▼
              Autonomous Workflow
                       │
                       ▼
              Business Operations

---

##📌 Final Architecture
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║             🎧 CUSTOMER SUPPORT AI AGENT                 ║
║                                                          ║
║                  Gemini + MCP + SQLite                   ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║   👤 User                                                ║
║      │                                                   ║
║      ▼                                                   ║
║   🧠 Gemini                                              ║
║      │                                                   ║
║      ▼                                                   ║
║   🔌 MCP Client                                          ║
║      │                                                   ║
║      ▼                                                   ║
║   🛠️ MCP Tools                                           ║
║      │                                                   ║
║      ▼                                                   ║
║   🗄️ SQLite                                              ║
║      │                                                   ║
║      ▼                                                   ║
║   🔄 Result → Gemini → Next Tool                         ║
║      │                                                   ║
║      ▼                                                   ║
║   ✅ Final Answer                                        ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝

---

# ⭐ Final Result

The project demonstrates a complete autonomous customer-support workflow:

```text
🤖 Think
   ↓
🔎 Search
   ↓
📄 Retrieve
   ↓
🧠 Analyze
   ↓
✏️ Update
   ↓
🔍 Verify
   ↓
✅ Final Answer
</p> <p align="center">
