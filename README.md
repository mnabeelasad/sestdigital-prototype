# SESTdigital SEO Content Agent

A Retrieval-Augmented Generation (RAG) prototype built for the SESTdigital AI Developer Case Study. This agent autonomously transforms internal knowledge (meeting transcripts and product documentation) into SEO-optimized website content.

### 📸 Project Snapshots
**The Streamlit Agent Interface:**
<img width="1915" height="984" alt="image" src="https://github.com/user-attachments/assets/c7d1865e-141b-45f3-b1ae-1ffc740549e8" />



## ✨ Features

* **Local RAG Pipeline:** Ingests internal PDFs, chunks the text, and stores vectors locally using ChromaDB for fast, secure retrieval.
* **Modern UI:** A custom-styled Streamlit interface featuring a "Midnight Aurora" aesthetic and real-time text streaming.
* **Autonomy:** The agent analyzes sales transcripts to identify customer pain points and matches them with the correct SESTdigital solutions (e.g., KI-Führerschein, KI-Workshops).
* **🌟 Automatic Categorization:** The LLM is strictly prompted to categorize generated articles into SESTdigital's core buckets: *Strategy, Training,* or *Technology*.
* **🌟 WordPress REST API Ready:** Includes a working integration to push drafted articles directly to a WordPress live site/sandbox using Application Passwords.
  
Autonomous WordPress Publishing:
<img width="1916" height="940" alt="image" src="https://github.com/user-attachments/assets/34696214-8099-4c29-9b6f-061e89c2d781" />


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
