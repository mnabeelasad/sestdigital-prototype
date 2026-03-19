# SESTdigital SEO Content Agent

A Retrieval-Augmented Generation (RAG) prototype built for the SESTdigital AI Developer Case Study. This agent autonomously transforms internal knowledge (meeting transcripts and product documentation) into SEO-optimized website content.

### 📸 Project Snapshots
**The Streamlit Agent Interface:**
<img width="1920" height="1037" alt="image" src="https://github.com/user-attachments/assets/10c215ba-a017-48a9-9a21-d590d9181886" />

Autonomous WordPress Publishing:**
![WordPress Integration](<img width="1914" height="923" alt="image" src="https://github.com/user-attachments/assets/d81780d9-b7cf-490c-9951-74f7aeb393a0" />)


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

**2. Set up a virtual environment:**
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

**3. Install dependencies:**
```bash
pip install -r requirements.txt
```

**4. Configure Environment Variables (.env):**
Create a new file named exactly `.env` in the root folder of the project.

```text
# REQUIRED: Your OpenAI API Key
OPENAI_API_KEY=sk-your-openai-api-key-here

# OPTIONAL (For Bonus 2): WordPress Integration
WP_URL=[https://your-wordpress-site.com](https://your-wordpress-site.com)
WP_USER=your_wp_admin_username
WP_APP_PASSWORD=your_24_character_application_password
```

**5. Run the Application:**
```bash
streamlit run app.py
```
