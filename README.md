# 🤖 Multi-Agent AI Research System

<p align="center">

<img src="https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python">

<img src="https://img.shields.io/badge/LangChain-Agentic%20AI-green?style=for-the-badge">

<img src="https://img.shields.io/badge/Mistral-AI-orange?style=for-the-badge">

<img src="https://img.shields.io/badge/Tavily-Web%20Search-red?style=for-the-badge">

<img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge">

</p>


<p align="center">

An autonomous AI research assistant powered by  
<b>Multi-Agent Architecture + LangChain + Mistral AI</b>

</p>


---

# 🌟 Overview

**Multi-Agent AI Research System** is an intelligent research automation framework that uses multiple AI agents to search, analyze, summarize, and evaluate information from the web.

Instead of relying on a single LLM call, this system divides tasks among specialized agents:

- 🔎 Search Agent → Finds information
- 📖 Reader Agent → Extracts useful content
- ✍ Writer Agent → Generates reports
- 🧐 Critic Agent → Evaluates quality


The result is a structured, reliable, and AI-generated research report.


---

# ✨ Key Features

## 🔍 Research Automation

✔ Automated web research  
✔ Source collection  
✔ Website content extraction  


## 🤖 Multi-Agent Intelligence

✔ Specialized AI agents  
✔ Agent collaboration workflow  
✔ Modular architecture  


## 📝 Report Generation

✔ Structured reports  
✔ AI summarization  
✔ Research analysis  


## 🧠 AI Evaluation

✔ Quality scoring  
✔ Error detection  
✔ Improvement suggestions  


---

# 🏛 System Architecture


```
                  USER QUERY
                      |
                      |
                      ▼

              🔎 SEARCH AGENT
              (Tavily API)

                      |
                      ▼

              📖 READER AGENT
          (BeautifulSoup Scraper)

                      |
                      ▼

              ✍ WRITER AGENT
             (Mistral AI LLM)

                      |
                      ▼

              🧐 CRITIC AGENT
              (AI Evaluation)

                      |
                      ▼

             📄 FINAL REPORT
```


---

# 📂 Project Structure


```
MULTI-AGENTS-SYSTEM

│
├── DEEP_RESEARCH_AGENT.py
│        └── Main Application
│
├── pipeline.py
│        └── Agent Workflow Pipeline
│
├── agents.py
│        └── AI Agent Definitions
│
├── tools.py
│        └── Search & Scraping Tools
│
├── requirements.txt
│        └── Dependencies
│
├── LICENSE
│
├── .gitignore
│
└── README.md

```


---

# 🛠 Tech Stack


| Technology | Usage |
|------------|-------|
| Python | Core Development |
| LangChain | Agent Framework |
| Mistral AI | LLM Reasoning |
| Tavily API | Web Search |
| BeautifulSoup | Web Scraping |
| Requests | HTTP Handling |
| dotenv | Secret Management |


---

# 🧩 Agent Workflow


## 🔎 Search Agent

Responsibilities:

- Search web information
- Find useful sources
- Collect URLs


---

## 📖 Reader Agent

Responsibilities:

- Extract webpage content
- Clean HTML data
- Prepare research context


---

## ✍ Writer Agent

Responsibilities:

- Analyze gathered information
- Generate structured reports
- Summarize findings


---

## 🧐 Critic Agent

Responsibilities:

- Review generated report
- Find missing information
- Provide quality feedback


---

# ⚙ Installation


Clone repository:

```bash
git clone https://github.com/priteshbeladiya07/MULTI-AGENTS-SYSTEM.git
```


Navigate:

```bash
cd MULTI-AGENTS-SYSTEM
```


Install packages:

```bash
pip install -r requirements.txt
```


---

# 🔐 Environment Setup


Create `.env` file:


```env
MISTRAL_API_KEY=your_api_key

TAVILY_API_KEY=your_api_key
```


---

# ▶ Run Application


Start research agent:


```bash
python DEEP_RESEARCH_AGENT.py
```


or


```bash
python pipeline.py
```


---

# 🖥 Example Flow


### Input

```
Impact of Artificial Intelligence on Healthcare
```


### AI Processing


```
Question

 ↓

Search

 ↓

Read Sources

 ↓

Generate Report

 ↓

Critic Evaluation

 ↓

Final Answer
```


---

# 🚀 Future Roadmap


- [ ] Streamlit UI Dashboard
- [ ] LangGraph Integration
- [ ] Memory System
- [ ] PDF Export
- [ ] Citation Generator
- [ ] Multi-Language Research
- [ ] Agent Monitoring
- [ ] Multiple LLM Support


---

# 📚 Skills Demonstrated


Through this project:

- Multi-Agent AI Development
- LangChain Framework
- LLM Application Design
- Prompt Engineering
- AI Tool Calling
- Web Automation
- Research Automation


---

# 👨‍💻 Author


## Pritesh Beladiya


🎓 Electronics & Communication Engineering Student

💡 AI • Generative AI • LangChain • Agentic Systems


GitHub:

https://github.com/priteshbeladiya07


---

# 📜 License


Distributed under the MIT License.


---

<p align="center">

⭐ If you like this project, consider giving it a star!

<br>

Made with ❤️ using Python + LangChain + Mistral AI

</p>
