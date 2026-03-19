# config.py
import os
from dotenv import load_dotenv

def load_environment():
    """Loads environment variables from the .env file."""
    load_dotenv()
    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError("OPENAI_API_KEY is missing. Please check your .env file.")
    print("✅ Environment variables loaded.")