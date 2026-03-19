# rag_pipeline.py
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

def create_vector_store(chunks):
    """Converts text chunks into embeddings and stores them locally using Chroma."""
    print("🧠 Building local vector database...")
    vector_store = Chroma.from_documents(
        documents=chunks, 
        embedding=OpenAIEmbeddings()
    )
    return vector_store

def generate_seo_article(vector_store):
    """Creates the RAG chain and asks the LLM to generate the article (Streaming)."""
    # Set up the retriever to find the top 5 most relevant chunks
    retriever = vector_store.as_retriever(search_kwargs={"k": 5})
    
    # Initialize the LLM
    llm = ChatOpenAI(model="gpt-4o", temperature=0.7)

    # Define the exact instructions for the agent
    template = """
    You are an expert SEO Content Strategist for SESTdigital. 
    Use the following pieces of retrieved context (which include sales meeting transcripts and product brochures) to write an SEO-optimized article proposal.
    
    Context: {context}
    
    Identify a core customer problem from the transcripts and propose an article that offers a SESTdigital product/service as the solution.
    
    Your output MUST strictly follow this format:
    1. SEO Title: (Catchy and optimized)
    2. Category: (You MUST choose exactly ONE of these options: Strategy, Training, or Technology)
    3. Target Keywords: (A list of 5 relevant SEO keywords)
    4. Outline: (Brief bullet points outlining the article)
    5. First Draft: (A 300-400 word introduction and main body draft written in German, matching the company's tone)

    Answer:
    """
    prompt = PromptTemplate.from_template(template)

    print("✍️ Generating SEO article proposal based on internal knowledge...")
    rag_chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    # We trigger the generation with a guiding query
    query = "Analyze the documents for customer pain points and matching SESTdigital solutions to write an SEO article."
    
    return rag_chain.stream(query)