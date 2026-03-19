# SESTdigital SEO Content Agent

A Retrieval-Augmented Generation (RAG) prototype built for the SESTdigital AI Developer Case Study. This agent autonomously transforms internal knowledge (meeting transcripts and product documentation) into SEO-optimized website content.

## ✨ Features

* **Local RAG Pipeline:** Ingests internal PDFs, chunks the text, and stores vectors locally using ChromaDB for fast, secure retrieval.
* **Modern UI:** A custom-styled Streamlit interface featuring a "Midnight Aurora" aesthetic and real-time text streaming.
* **Autonomy:** The agent analyzes sales transcripts to identify customer pain points and matches them with the correct SESTdigital solutions (e.g., KI-Führerschein, KI-Workshops).
* **🌟 Automatic Categorization:** The LLM is strictly prompted to categorize generated articles into SESTdigital's core buckets: *Strategy, Training,* or *Technology*.
* **🌟 WordPress REST API Ready:** Includes a working integration to push drafted articles directly to a WordPress live site/sandbox using Application Passwords.

## 🏗️ Architecture & Tech Stack

* **Framework:** LangChain
* **LLM / Embeddings:** OpenAI (`gpt-4o`, `text-embedding-3-small` / `ada-002`)
* **Vector Database:** ChromaDB 
* **Frontend:** Streamlit
* **Document Processing:** `PyPDFDirectoryLoader`, `RecursiveCharacterTextSplitter`

## ⚙️ Local Installation & Setup

1. **Clone the repository:**
   ```bash
    git clone https://github.com/mnabeelasad/sestdigital-prototype.git
    cd sestdigital-prototype

2. **Set up a virtual environment:**

# Windows
python -m venv venv
.\venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate

2. **Set up a virtual environment:**

# Windows
python -m venv venv
.\venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate

3. **Install dependencies:**

pip install -r requirements.txt

4. **Configure Environment Variables (.env):**

# REQUIRED: Your OpenAI API Key
OPENAI_API_KEY=sk-your-openai-api-key-here

# OPTIONAL: WordPress Integration
WP_URL=[https://your-wordpress-site.com](https://your-wordpress-site.com)
WP_USER=your_wp_admin_username
WP_APP_PASSWORD=your_24_character_application_password

5. **Run the Application:**

streamlit run app.py