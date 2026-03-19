# app.py
import streamlit as st
import os
from config import load_environment
from document_processor import load_and_chunk_documents
from rag_pipeline import create_vector_store, generate_seo_article
from wordpress_api import post_draft_to_wordpress
# ─── Page Configuration ───
st.set_page_config(
    page_title="SESTdigital SEO Content Agent",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── Custom CSS for a Colorful UI ───
st.markdown("""
<style>
    /* Gradient text for the main header */
    .agent-header {
        background: linear-gradient(135deg, #FF6B6B 0%, #4ECDC4 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.8rem;
        font-weight: 900;
        margin-bottom: 0px;
    }
    
    /* Subtitle styling */
    .agent-subtitle {
        color: #8A92B2;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }

    /* Style all buttons to look like modern app buttons */
    .stButton>button {
        background: linear-gradient(135deg, #6c63ff 0%, #3f51b5 100%);
        color: white;
        border: none;
        border-radius: 8px;
        font-weight: bold;
        transition: all 0.3s ease;
        border: 1px solid #8A92B2;
    }
    
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 15px rgba(108, 99, 255, 0.5);
        border-color: #4ECDC4;
        color: white;
    }
    
    /* Custom container for the generated text */
    .output-container {
        background: linear-gradient(145deg, #1A1A2E 0%, #16213E 100%);
        border-left: 5px solid #FF6B6B;
        border-right: 1px solid #3d3d5c;
        border-top: 1px solid #3d3d5c;
        border-bottom: 1px solid #3d3d5c;
        padding: 25px;
        border-radius: 10px;
        margin-top: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        color: #E0E0FF;
        line-height: 1.6;
    }
</style>
""", unsafe_allow_html=True)

# ─── Initialize Session State ───
if "vector_store" not in st.session_state:
    st.session_state.vector_store = None
if "article_draft" not in st.session_state:
    st.session_state.article_draft = None

# ─── Sidebar ───
with st.sidebar:
    st.markdown("### ⚙️ System Status")
    
    load_environment()
    if os.getenv("OPENAI_API_KEY"):
        st.success("🟢 API Key Active")
    else:
        st.error("🔴 Missing API Key")
    
    st.divider()
    
    st.markdown("### 📚 Knowledge Base")
    if st.session_state.vector_store is not None:
        st.success("🟢 Documents Indexed & Ready")
    else:
        st.warning("🟡 Not indexed yet.")
        
    if st.button("🔄 Index Documents", use_container_width=True):
        with st.spinner("Processing PDFs..."):
            try:
                chunks = load_and_chunk_documents("./data")
                if chunks:
                    st.session_state.vector_store = create_vector_store(chunks)
                    st.success(f"✅ Indexed {len(chunks)} chunks!")
                else:
                    st.error("❌ No PDFs found.")
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")

# ─── Main Content ───
st.markdown('<p class="agent-header">SESTdigital Content Agent</p>', unsafe_allow_html=True)
st.markdown('<p class="agent-subtitle">Transforming internal meeting transcripts into SEO-optimized content.</p>', unsafe_allow_html=True)
st.divider()

if st.session_state.vector_store is None:
    st.info("👈 Start by clicking **Index Documents** in the sidebar to build the AI's memory.")
else:
    st.markdown("### 🎯 Generate SEO Article")
    st.write("Click below to let the agent analyze the transcripts and stream the article proposal live.")
    
    if st.button("🚀 Stream SEO Proposal", type="primary"):
        # a visual container for the output
        st.markdown('<div class="output-container">', unsafe_allow_html=True)
        
        # to write the stream into
        stream_container = st.empty()
        
        try:
            # Fetch the stream from our LangChain pipeline
            response_stream = generate_seo_article(st.session_state.vector_store)
            
            # st.write_stream automatically types it out and returns the final full string!
            full_response = stream_container.write_stream(response_stream)
            
            # Save it to session state so the download button can use it
            st.session_state.article_draft = full_response
            
        except Exception as e:
            st.error(f"❌ Generation failed: {str(e)}")
            
        st.markdown('</div>', unsafe_allow_html=True)

    # ─── Download Button (Only shows after generation) ───
    if st.session_state.article_draft:
        st.divider()
        col1, col2, col3 = st.columns([1, 2, 2])
        
        with col2:
            st.download_button(
                "⬇️ Download Strategy (.txt)",
                data=st.session_state.article_draft,
                file_name="SESTdigital_SEO_Strategy.txt",
                mime="text/plain",
                use_container_width=True
            )
            
        with col3:
            if st.button("🌐 Push to WordPress (Draft)", use_container_width=True):
                with st.spinner("Connecting to WordPress API..."):
                    #parse the exact title and category from the text first.
                    wp_response = post_draft_to_wordpress(
                        title="SESTdigital SEO Draft", 
                        content=st.session_state.article_draft,
                        category="Strategy" 
                    )
                    
                    if wp_response["status"] == "mock_success":
                        st.info(f"ℹ️ {wp_response['message']}")
                    elif wp_response["status"] == "success":
                        st.success(f"✅ Draft created successfully! Link: {wp_response.get('url')}")
                    else:
                        st.error(f"❌ Failed to post: {wp_response.get('message')}")