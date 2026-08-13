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
```
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

## 🔌 MCP Architecture

```text
┌──────────────────────────────┐
│          👤 USER             │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│        🧠 GEMINI AI          │
│       Agent Reasoning        │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│       🔌 MCP CLIENT          │
└──────────────┬───────────────┘
               │
               │ MCP
               ▼
┌──────────────────────────────┐
│       🛠️ MCP SERVER         │
│                              │
│ search_tickets               │
│ get_ticket                   │
│ update_ticket                │
│ create_ticket                │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│         🗄️ SQLITE           │
│          support.db          │
└──────────────────────────────┘
```

## 🗄️ Database Schema

The application uses a SQLite database named:

`support.db`

The database contains a `tickets` table.

| Column | Description |
|---|---|
| `id` | Unique ticket ID |
| `customer_name` | Customer name |
| `email` | Customer email |
| `subject` | Ticket subject |
| `description` | Ticket description |
| `priority` | Ticket priority |
| `status` | Ticket status |
| `assigned_to` | Assigned support agent |
| `created_at` | Ticket creation time |
| `updated_at` | Last update time |

---

## ▶️ Run the Application

From the project directory:

```powershell
uv run python main.py
```

Expected output:

```text
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
```

---

## 🧠 How the Autonomous Loop Works

The agent does not make only one Gemini request.

It can repeatedly reason, call an MCP tool, inspect the result, and decide whether another tool is required.

```text
👤 User Request
      ↓
🧠 Gemini
      ↓
🔎 MCP Tool
      ↓
🗄️ SQLite
      ↓
📤 Tool Result
      ↓
🧠 Gemini
      ↓
   Another Tool?
    ↙       ↘
  YES        NO
   ↓          ↓
🛠️ MCP     ✅ Final Answer
 Tool
   ↓
🗄️ SQLite
   ↓
📤 Result
   ↓
🧠 Gemini
   ↓
Continue
```

### Example

```text
👤 User
   ↓
"Resolve John's login issue"
   ↓
🧠 Gemini
   ↓
🔎 Search Tickets
   ↓
🗄️ SQLite
   ↓
📄 Get Ticket
   ↓
🗄️ SQLite
   ↓
🧠 Gemini
   ↓
✏️ Update Ticket
   ↓
🗄️ SQLite
   ↓
🔎 Verify
   ↓
🗄️ SQLite
   ↓
✅ Final Answer
```

---

## 🔐 Security

Never commit your Gemini API key.

Your `.gitignore` should contain:

```gitignore
.env
.venv/
__pycache__/
*.pyc
support.db
```

Your `.env` should contain:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

---

## 🎯 Learning Objectives

This project demonstrates:

```text
AI Agents
   ↓
Google Gemini
   ↓
Tool Calling
   ↓
Model Context Protocol
   ↓
Autonomous Workflow
   ↓
Business Operations
   ↓
SQLite Database
```

---

## 📌 Final Architecture

```text
╔══════════════════════════════════════════════════════════╗
║             🎧 CUSTOMER SUPPORT AI AGENT                 ║
║                                                          ║
║                 Gemini + MCP + SQLite                    ║
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
```

---


```

## Next Heading
