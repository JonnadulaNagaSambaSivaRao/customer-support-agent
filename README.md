# 🎧 Customer Support AI Agent

<p align="center">

  <img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white" />

  <img src="https://img.shields.io/badge/Gemini-AI-4285F4?style=for-the-badge&logo=google&logoColor=white" />

  <img src="https://img.shields.io/badge/MCP-Model%20Context%20Protocol-8A2BE2?style=for-the-badge" />

  <img src="https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white" />

  <img src="https://img.shields.io/badge/uv-Package%20Manager-DE5FE9?style=for-the-badge" />

  <img src="https://img.shields.io/badge/Cursor-IDE-000000?style=for-the-badge&logo=cursor&logoColor=white" />

</p>

<p align="center">

  <b>🤖 Autonomous Customer Support Agent powered by Gemini, MCP & SQLite</b>

</p>

<p align="center">

  Search 🔎 → Retrieve 📄 → Analyze 🧠 → Update ✏️ → Verify ✅

</p>

---

# 🌟 Project Overview

The **Customer Support AI Agent** is an autonomous AI application that uses:

- 🧠 **Google Gemini** for reasoning and decision-making
- 🔌 **Model Context Protocol (MCP)** for tool communication
- 🗄️ **SQLite** for persistent ticket storage
- 🐍 **Python** for application logic
- ⚡ **uv** for fast Python environment and dependency management
- 🖥️ **Cursor** for development and MCP integration

The agent can perform **multi-step customer support operations automatically**.

✨ Features
Feature	Description
🔎 Search Tickets	Search by customer, status, priority or keyword
📄 Get Ticket	Retrieve complete ticket information
✏️ Update Ticket	Update status, priority or assignee
➕ Create Ticket	Create new customer-support tickets
🧠 AI Reasoning	Gemini decides which tools are required
🔄 Multi-Step Tasks	Execute several tools automatically
🗄️ SQLite Backend	Store tickets in a real database
🔌 MCP Integration	Expose database operations as MCP tools
💬 CLI Chatbot	Continue chatting until exit
🖥️ Cursor Support	Connect MCP tools to Cursor


🧰 Technology Stack


┌─────────────────────────────────────┐
│         CUSTOMER SUPPORT AI         │
├─────────────────────────────────────┤
│                                     │
│ 🧠 Google Gemini                    │
│ 🔌 Model Context Protocol            │
│ 🐍 Python 3.12                       │
│ 🗄️ SQLite                           │
│ ⚡ uv                                │
│ 🖥️ Cursor                           │
│                                     │
└─────────────────────────────────────┘



📁 Project Structure
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



🔄 How the Agent Works

The agent follows an autonomous tool-calling cycle.

                 👤 USER
                    │
                    ▼
       "Find John's high priority ticket"
                    │
                    ▼
              🧠 GEMINI
                    │
             Need information?
                    │
                    ▼
              🔧 MCP TOOL
                    │
                    ▼
             🗄️ SQLite
                    │
             Database result
                    │
                    ▼
              🧠 GEMINI
                    │
             Need another tool?
                /       \
              YES        NO
               │          │
               ▼          ▼
          🔧 MCP Tool   ✅ Final Answer
               │
               ▼
          🗄️ SQLite
               │
               └──────────────► 🧠 GEMINI



The architecture is:



                 👤 USER
                    │
                    ▼
             ┌─────────────┐
             │   main.py   │
             │ CLI Chatbot │
             └──────┬──────┘
                    │
                    ▼
             ┌─────────────┐
             │  agent.py   │
             │   Gemini    │
             │             │
             │ Agent Loop  │
             └──────┬──────┘
                    │
                    ▼
             ┌─────────────┐
             │ MCP Client  │
             └──────┬──────┘
                    │
                    │ MCP
                    ▼
             ┌─────────────┐
             │mcp_support  │
             │    .py      │
             └──────┬──────┘
                    │
                    ▼
             ┌─────────────┐
             │   SQLite    │
             │ support.db  │
             └─────────────┘
             

 🧠 Autonomous Agent Loop

  This allows:

Gemini
  ↓
MCP Tool
  ↓
Result
  ↓
Gemini
  ↓
Another MCP Tool
  ↓
Result
  ↓
Gemini
  ↓
Final Answer


🗄️ Database Schema

The SQLite database contains a tickets table.

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

.

🔌 MCP Architecture
                  ┌─────────────────┐
                  │     Cursor      │
                  │   / AI Client   │
                  └────────┬────────┘
                           │
                           │ MCP
                           ▼
                  ┌─────────────────┐
                  │ mcp_support.py  │
                  │                 │
                  │ MCP Server      │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │     SQLite      │
                  │   support.db   │
                  └─────────────────┘


For the autonomous Gemini application:

                  ┌─────────────────┐
                  │      User       │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │    Gemini AI    │
                  │                 │
                  │ Agent Reasoning │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │    MCP Client   │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │   MCP Server    │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │     SQLite      │
                  └─────────────────┘



✅ Customer Support Agent
User
 ↓
Gemini
 ↓
Search Ticket
 ↓
Database
 ↓
Gemini
 ↓
Get Ticket
 ↓
Database
 ↓
Gemini
 ↓
Update Ticket
 ↓
Database
 ↓
Gemini
 ↓
Final Answer


⭐ Final Result


╔══════════════════════════════════════════════════════════╗
║                                                          ║
║          🎧 CUSTOMER SUPPORT AI AGENT                    ║
║                                                          ║
║              Gemini + MCP + SQLite                       ║
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
<p align="center">
💙 Built with Python + Gemini + MCP + SQLite

🤖 Think → 🔎 Search → 📄 Retrieve → ✏️ Update → ✅ Verify

</p> <p align="center">
