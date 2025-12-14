"""
Streamlit Web Interface for Multi-LLM Search Agent
"""
try:
    import streamlit as st
except ImportError:
    print("Error: Streamlit not installed")
    print("Run: pip install streamlit")
    import sys
    sys.exit(1)

try:
    from agents.search_agent import SearchAgent
    from config.api_config import APIConfig
except ImportError as e:
    st.error(f"Error importing agent modules: {e}")
    st.info("Make sure you're in the project directory with the required modules")
    st.stop()

import sys
from io import StringIO

# Page configuration
st.set_page_config(
    page_title="Multi-LLM Search Agent",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        padding-top: 1rem;
    }
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
        font-size: 1.25rem;
    }
    .search-result {
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        border-left: 4px solid #1f77b4;
    }
    .groq-response {
        background-color: #f0f7ff;
        border-left-color: #1f77b4;
    }
    .google-response {
        background-color: #fff8f0;
        border-left-color: #ff7f0e;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'agent' not in st.session_state:
    st.session_state.agent = None
if 'setup_complete' not in st.session_state:
    st.session_state.setup_complete = False
if 'search_history' not in st.session_state:
    st.session_state.search_history = []


def setup_agent(groq_key: str, google_key: str) -> bool:
    """Initialize the search agent with API keys."""
    try:
        agent = SearchAgent()
        agent.api_config.set_api_keys(
            groq_key=groq_key if groq_key else None,
            google_key=google_key if google_key else None
        )
        
        if not groq_key and not google_key:
            st.error("❌ Please provide at least one API key (Groq or Google)")
            return False
        
        st.session_state.agent = agent
        st.session_state.setup_complete = True
        return True
    except Exception as e:
        st.error(f"❌ Setup failed: {str(e)}")
        return False


def perform_search(query: str) -> dict:
    """Perform search with the agent."""
    try:
        results = st.session_state.agent.search_and_answer(query)
        return results
    except Exception as e:
        st.error(f"❌ Search failed: {str(e)}")
        return None


def main():
    """Main Streamlit app."""
    
    # Header
    col1, col2 = st.columns([3, 1])
    with col1:
        st.title("🔍 Multi-LLM Search Agent")
    with col2:
        st.caption("v1.0.0")
    
    st.markdown("Search academic papers and general knowledge with AI-powered answers")
    st.divider()
    
    # Sidebar for setup
    with st.sidebar:
        st.header("⚙️ Configuration")
        st.markdown("---")
        
        st.subheader("API Keys")
        st.markdown("""
        Get your free API keys:
        - **Groq** (Fast): https://console.groq.com
        - **Google** (Optional): https://aistudio.google.com
        """)
        
        # API Key inputs
        groq_key = st.text_input(
            "🚀 Groq API Key",
            type="password",
            placeholder="gsk_...",
            help="Get free key at https://console.groq.com"
        )
        
        google_key = st.text_input(
            "🧠 Google API Key (Optional)",
            type="password",
            placeholder="AIza_...",
            help="Optional - Get at https://aistudio.google.com"
        )
        
        # Setup button
        if st.button("🔐 Setup API Keys", use_container_width=True):
            if setup_agent(groq_key, google_key):
                st.success("✅ Setup successful!")
                st.rerun()
        
        st.markdown("---")
        
        # Status
        if st.session_state.setup_complete and st.session_state.agent:
            st.success("✅ Ready to search!")
            st.caption(f"Active providers: {', '.join(str(p.value) for p in st.session_state.agent.api_config.get_active_providers())}")
        else:
            st.warning("⚠️ Please configure API keys to begin")
        
        st.markdown("---")
        st.subheader("About")
        st.markdown("""
        **Multi-LLM Search Agent**
        
        Combines:
        - 🔍 Arxiv (academic papers)
        - 📚 Wikipedia (general knowledge)
        - 🤖 Groq & Google LLMs
        
        **Features:**
        - Multiple search sources
        - AI-powered answers
        - Model fallback system
        - Free to use
        """)
        
        if st.button("📖 GitHub Repository", use_container_width=True):
            st.info("Visit: https://github.com/your-username/intellisearch3")
    
    # Main content
    if not st.session_state.setup_complete:
        st.info("👈 Please configure your API keys in the sidebar to get started")
        return
    
    # Search section
    st.subheader("🔎 Search")
    
    col1, col2 = st.columns([3, 1])
    with col1:
        query = st.text_input(
            "Enter your search query:",
            placeholder="e.g., What is machine learning?",
            label_visibility="collapsed"
        )
    with col2:
        search_button = st.button("🔍 Search", use_container_width=True, type="primary")
    
    # Search options
    col1, col2, col3 = st.columns(3)
    with col1:
        include_arxiv = st.checkbox("📄 Arxiv", value=True)
    with col2:
        include_wikipedia = st.checkbox("📚 Wikipedia", value=True)
    with col3:
        show_sources = st.checkbox("Show sources", value=True)
    
    st.divider()
    
    # Perform search
    if search_button and query:
        with st.spinner("🔍 Searching..."):
            results = perform_search(query)
        
        if results:
            # Add to history
            st.session_state.search_history.insert(0, query)
            
            # Display results
            st.subheader(f"Results for: \"{query}\"")
            
            # Results summary
            arxiv_count = len(results.get('search_results', {}).get('arxiv', []))
            wiki_count = len(results.get('search_results', {}).get('wikipedia', []))
            
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("📄 Arxiv Papers", arxiv_count)
            with col2:
                st.metric("📚 Wikipedia Articles", wiki_count)
            with col3:
                providers = results.get('providers_used', [])
                st.metric("🤖 LLM Responses", len(providers))
            
            st.markdown("---")
            
            # Tabs for different views
            tab1, tab2, tab3 = st.tabs(["📋 AI Answers", "📰 Search Sources", "📊 Details"])
            
            with tab1:
                st.subheader("AI Generated Answers")
                
                # Display LLM responses
                responses = results.get('llm_responses', {})
                
                if responses.get('groq'):
                    st.markdown("### 🚀 Groq Response")
                    st.markdown(f"""
                    <div class="search-result groq-response">
                    {responses['groq']}
                    </div>
                    """, unsafe_allow_html=True)
                
                if responses.get('google'):
                    st.markdown("### 🧠 Google Response")
                    st.markdown(f"""
                    <div class="search-result google-response">
                    {responses['google']}
                    </div>
                    """, unsafe_allow_html=True)
                
                if not responses.get('groq') and not responses.get('google'):
                    st.warning("No AI responses generated")
            
            with tab2:
                st.subheader("Search Sources")
                
                search_results = results.get('search_results', {})
                
                # Arxiv papers
                if include_arxiv and search_results.get('arxiv'):
                    st.markdown("#### 📄 Arxiv Papers")
                    for i, paper in enumerate(search_results['arxiv'], 1):
                        with st.expander(f"{i}. {paper.get('title', 'Untitled')}"):
                            if show_sources:
                                st.markdown(f"**Authors:** {paper.get('authors', 'N/A')}")
                                st.markdown(f"**Published:** {paper.get('published', 'N/A')}")
                                st.markdown(f"**Summary:** {paper.get('summary', 'N/A')[:200]}...")
                                if paper.get('arxiv_url'):
                                    st.markdown(f"[📖 Read Full Paper]({paper.get('arxiv_url')})")
                elif include_arxiv:
                    st.info("No Arxiv papers found for this query")
                
                # Wikipedia articles
                if include_wikipedia and search_results.get('wikipedia'):
                    st.markdown("#### 📚 Wikipedia Articles")
                    for i, article in enumerate(search_results['wikipedia'], 1):
                        with st.expander(f"{i}. {article.get('title', 'Untitled')}"):
                            if show_sources:
                                st.markdown(article.get('body', 'N/A')[:300] + "...")
                                if article.get('href'):
                                    st.markdown(f"[📖 Read Full Article]({article.get('href')})")
                elif include_wikipedia:
                    st.info("No Wikipedia articles found for this query")
            
            with tab3:
                st.subheader("Technical Details")
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown("**Query Information**")
                    st.json({
                        "query": query,
                        "sources_used": {
                            "arxiv": include_arxiv,
                            "wikipedia": include_wikipedia
                        }
                    })
                
                with col2:
                    st.markdown("**Providers Used**")
                    st.json({
                        "providers": results.get('providers_used', []),
                        "results_count": {
                            "arxiv": arxiv_count,
                            "wikipedia": wiki_count
                        }
                    })
            
            st.divider()
    
    # Search history
    if st.session_state.search_history:
        st.subheader("📜 Search History")
        for i, hist_query in enumerate(st.session_state.search_history[:5], 1):
            if st.button(f"{i}. {hist_query[:50]}...", use_container_width=True):
                query = hist_query
                search_button = True
    
    # Footer
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.caption("🔒 Your API keys are never stored")
    with col2:
        st.caption("📖 [Documentation](https://github.com/your-username/intellisearch3)")
    with col3:
        st.caption("⭐ Made with ❤️")


if __name__ == "__main__":
    main()
