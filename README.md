# SESTdigital SEO Content Agent

A Retrieval-Augmented Generation (RAG) prototype built for the SESTdigital AI Developer Case Study. This agent autonomously transforms internal knowledge (meeting transcripts and product documentation) into SEO-optimized website content.

## ✨ Features

* **Local RAG Pipeline:** Ingests internal PDFs, chunks the text, and stores vectors locally using ChromaDB for fast, secure retrieval.
* **Modern UI:** A custom-styled Streamlit interface featuring a "Midnight Aurora" aesthetic and real-time text streaming.
* **Autonomy:** The agent analyzes sales transcripts to identify customer pain points and matches them with the correct SESTdigital solutions (e.g., KI-Führerschein, KI-Workshops).
* **🌟 Bonus 1: Automatic Categorization:** The LLM is strictly prompted to categorize generated articles into SESTdigital's core buckets: *Strategy, Training,* or *Technology*.
* **🌟 Bonus 2: WordPress REST API Ready:** Includes a working integration to push drafted articles directly to a WordPress live site/sandbox using Application Passwords.

## 🏗️ Architecture & Tech Stack

* **Framework:** LangChain
* **LLM / Embeddings:** OpenAI (`gpt-4o`, `text-embedding-3-small` / `ada-002`)
* **Vector Database:** ChromaDB 
* **Frontend:** Streamlit
* **Document Processing:** `PyPDFDirectoryLoader`, `RecursiveCharacterTextSplitter`

## ⚙️ Local Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR-USERNAME/sestdigital-content-agent.git](https://github.com/YOUR-USERNAME/sestdigital-content-agent.git)
   cd sestdigital-content-agent