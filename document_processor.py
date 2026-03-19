# document_processor.py
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_and_chunk_documents(directory_path="./data"):
    """Loads all PDFs from a directory and splits them into smaller chunks."""
    print(f"📂 Loading documents from {directory_path}...")
    loader = PyPDFDirectoryLoader(directory_path)
    docs = loader.load()
    
    if not docs:
        print("⚠️ No documents found. Make sure PDFs are in the data folders.")
        return []

    print(f"📄 Found {len(docs)} document pages. Chunking text...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, 
        chunk_overlap=200
    )
    chunks = text_splitter.split_documents(docs)
    print(f"✂️ Split documents into {len(chunks)} chunks.")
    
    return chunks