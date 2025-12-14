"""
FastAPI Web Interface for Multi-LLM Search Agent
Alternative to Streamlit for Python 3.14 compatibility
"""
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from typing import Optional, List
import uvicorn
from agents.search_agent import SearchAgent
from config.api_config import APIConfig

# Initialize FastAPI
app = FastAPI(
    title="Multi-LLM Search Agent",
    description="Web interface for searching with AI-powered answers",
    version="1.0.0"
)

# Store agent in memory
agent = None
agent_ready = False


class APIKeyRequest(BaseModel):
    groq_key: Optional[str] = None
    google_key: Optional[str] = None


class SearchRequest(BaseModel):
    query: str
    include_arxiv: bool = True
    include_wikipedia: bool = True


class SearchResponse(BaseModel):
    success: bool
    query: str
    arxiv_papers: int
    wikipedia_articles: int
    responses: dict
    error: Optional[str] = None


@app.get("/", response_class=HTMLResponse)
async def root():
    """Serve the web interface"""
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>🔍 Multi-LLM Search Agent</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                padding: 20px;
                color: #333;
            }
            
            .container {
                max-width: 1200px;
                margin: 0 auto;
                background: white;
                border-radius: 12px;
                box-shadow: 0 20px 60px rgba(0,0,0,0.3);
                overflow: hidden;
            }
            
            header {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 30px;
                text-align: center;
            }
            
            header h1 {
                font-size: 2.5em;
                margin-bottom: 10px;
            }
            
            header p {
                opacity: 0.9;
                font-size: 1.1em;
            }
            
            .content {
                display: grid;
                grid-template-columns: 300px 1fr;
                gap: 0;
            }
            
            .sidebar {
                background: #f7f9fc;
                padding: 30px;
                border-right: 1px solid #e0e6ed;
            }
            
            .main {
                padding: 30px;
            }
            
            .section {
                margin-bottom: 30px;
            }
            
            .section h3 {
                color: #667eea;
                margin-bottom: 15px;
                font-size: 1.1em;
            }
            
            .form-group {
                margin-bottom: 15px;
            }
            
            label {
                display: block;
                margin-bottom: 5px;
                font-weight: 600;
                color: #555;
                font-size: 0.9em;
            }
            
            input[type="text"],
            input[type="password"],
            textarea {
                width: 100%;
                padding: 10px;
                border: 1px solid #ddd;
                border-radius: 6px;
                font-size: 1em;
                font-family: inherit;
            }
            
            input:focus,
            textarea:focus {
                outline: none;
                border-color: #667eea;
                box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
            }
            
            button {
                width: 100%;
                padding: 12px;
                background: #667eea;
                color: white;
                border: none;
                border-radius: 6px;
                font-size: 1em;
                font-weight: 600;
                cursor: pointer;
                transition: background 0.3s;
            }
            
            button:hover {
                background: #5568d3;
            }
            
            button:active {
                transform: scale(0.98);
            }
            
            .status {
                padding: 12px;
                border-radius: 6px;
                margin: 15px 0;
                font-size: 0.9em;
            }
            
            .status.success {
                background: #d4edda;
                color: #155724;
                border: 1px solid #c3e6cb;
            }
            
            .status.error {
                background: #f8d7da;
                color: #721c24;
                border: 1px solid #f5c6cb;
            }
            
            .status.warning {
                background: #fff3cd;
                color: #856404;
                border: 1px solid #ffeaa7;
            }
            
            .search-box {
                margin-bottom: 20px;
            }
            
            .search-box textarea {
                min-height: 100px;
                resize: vertical;
            }
            
            .search-options {
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 10px;
                margin: 15px 0;
            }
            
            .checkbox-group {
                display: flex;
                align-items: center;
                gap: 8px;
            }
            
            .checkbox-group input {
                width: auto;
                cursor: pointer;
            }
            
            .results {
                margin-top: 30px;
            }
            
            .result-summary {
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 15px;
                margin-bottom: 20px;
            }
            
            .metric {
                background: #f7f9fc;
                padding: 15px;
                border-radius: 6px;
                text-align: center;
            }
            
            .metric-value {
                font-size: 2em;
                font-weight: bold;
                color: #667eea;
            }
            
            .metric-label {
                color: #888;
                font-size: 0.9em;
                margin-top: 5px;
            }
            
            .response-box {
                background: #f7f9fc;
                border-left: 4px solid #667eea;
                padding: 20px;
                border-radius: 6px;
                margin: 15px 0;
            }
            
            .response-box.groq {
                border-left-color: #667eea;
            }
            
            .response-box.google {
                border-left-color: #f57c00;
            }
            
            .response-title {
                font-weight: 600;
                color: #333;
                margin-bottom: 10px;
            }
            
            .response-content {
                line-height: 1.6;
                color: #555;
            }
            
            .loading {
                display: none;
                text-align: center;
                padding: 20px;
            }
            
            .loading.active {
                display: block;
            }
            
            .spinner {
                border: 4px solid #f3f3f3;
                border-top: 4px solid #667eea;
                border-radius: 50%;
                width: 40px;
                height: 40px;
                animation: spin 1s linear infinite;
                margin: 0 auto 10px;
            }
            
            @keyframes spin {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }
            
            .about {
                background: #f7f9fc;
                padding: 15px;
                border-radius: 6px;
                font-size: 0.9em;
                line-height: 1.6;
                color: #666;
            }
            
            .about p {
                margin-bottom: 10px;
            }
            
            a {
                color: #667eea;
                text-decoration: none;
            }
            
            a:hover {
                text-decoration: underline;
            }
            
            @media (max-width: 768px) {
                .content {
                    grid-template-columns: 1fr;
                }
                
                .sidebar {
                    border-right: none;
                    border-bottom: 1px solid #e0e6ed;
                }
                
                header h1 {
                    font-size: 1.8em;
                }
                
                .result-summary {
                    grid-template-columns: 1fr;
                }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <header>
                <h1>🔍 Multi-LLM Search Agent</h1>
                <p>Search academic papers & knowledge with AI-powered answers</p>
            </header>
            
            <div class="content">
                <div class="sidebar">
                    <div class="section">
                        <h3>🔐 API Configuration</h3>
                        
                        <div class="form-group">
                            <label for="groq-key">Groq API Key</label>
                            <input type="password" id="groq-key" placeholder="gsk_..." />
                            <small style="color: #888;">Get free key at <a href="https://console.groq.com" target="_blank">console.groq.com</a></small>
                        </div>
                        
                        <div class="form-group">
                            <label for="google-key">Google API Key (Optional)</label>
                            <input type="password" id="google-key" placeholder="AIza_..." />
                            <small style="color: #888;">Optional - Get at <a href="https://aistudio.google.com" target="_blank">aistudio.google.com</a></small>
                        </div>
                        
                        <button onclick="setupAPI()">🔐 Setup API Keys</button>
                        
                        <div id="status" style="display: none;"></div>
                    </div>
                    
                    <div class="section">
                        <h3>ℹ️ About</h3>
                        <div class="about">
                            <p><strong>Multi-LLM Search Agent</strong></p>
                            <p>Searches academic papers (Arxiv) and general knowledge (Wikipedia) with AI-powered answers from Groq or Google.</p>
                            <p>✓ Free forever<br>
                            ✓ No credit card<br>
                            ✓ Multiple LLMs</p>
                        </div>
                    </div>
                </div>
                
                <div class="main">
                    <div class="search-box">
                        <h3>🔎 Search</h3>
                        <textarea id="query" placeholder="Enter your search query... (e.g., What is machine learning?)" disabled></textarea>
                        
                        <div class="search-options">
                            <div class="checkbox-group">
                                <input type="checkbox" id="arxiv" checked disabled />
                                <label for="arxiv">📄 Arxiv</label>
                            </div>
                            <div class="checkbox-group">
                                <input type="checkbox" id="wikipedia" checked disabled />
                                <label for="wikipedia">📚 Wikipedia</label>
                            </div>
                        </div>
                        
                        <button id="search-btn" onclick="search()" disabled>🔍 Search</button>
                    </div>
                    
                    <div id="loading" class="loading">
                        <div class="spinner"></div>
                        <p>Searching...</p>
                    </div>
                    
                    <div id="results" class="results" style="display: none;">
                        <div class="result-summary">
                            <div class="metric">
                                <div class="metric-value" id="arxiv-count">0</div>
                                <div class="metric-label">Arxiv Papers</div>
                            </div>
                            <div class="metric">
                                <div class="metric-value" id="wiki-count">0</div>
                                <div class="metric-label">Wikipedia Articles</div>
                            </div>
                            <div class="metric">
                                <div class="metric-value" id="response-count">0</div>
                                <div class="metric-label">AI Responses</div>
                            </div>
                        </div>
                        
                        <div id="responses-container"></div>
                    </div>
                </div>
            </div>
        </div>
        
        <script>
            let isSetup = false;
            
            function showStatus(message, type = 'success') {
                const status = document.getElementById('status');
                status.className = `status ${type}`;
                status.textContent = message;
                status.style.display = 'block';
            }
            
            async function setupAPI() {
                const groqKey = document.getElementById('groq-key').value;
                const googleKey = document.getElementById('google-key').value;
                
                if (!groqKey && !googleKey) {
                    showStatus('❌ Please provide at least one API key', 'error');
                    return;
                }
                
                try {
                    const response = await fetch('/api/setup', {
                        method: 'POST',
                        headers: {'Content-Type': 'application/json'},
                        body: JSON.stringify({
                            groq_key: groqKey || null,
                            google_key: googleKey || null
                        })
                    });
                    
                    const data = await response.json();
                    
                    if (data.success) {
                        isSetup = true;
                        showStatus('✅ Setup successful! Ready to search.', 'success');
                        document.getElementById('query').disabled = false;
                        document.getElementById('search-btn').disabled = false;
                        document.getElementById('arxiv').disabled = false;
                        document.getElementById('wikipedia').disabled = false;
                    } else {
                        showStatus(`❌ Setup failed: ${data.error}`, 'error');
                    }
                } catch (error) {
                    showStatus(`❌ Error: ${error.message}`, 'error');
                }
            }
            
            async function search() {
                if (!isSetup) {
                    showStatus('⚠️ Please setup API keys first', 'warning');
                    return;
                }
                
                const query = document.getElementById('query').value;
                const includeArxiv = document.getElementById('arxiv').checked;
                const includeWikipedia = document.getElementById('wikipedia').checked;
                
                if (!query.trim()) {
                    showStatus('⚠️ Please enter a search query', 'warning');
                    return;
                }
                
                document.getElementById('loading').classList.add('active');
                document.getElementById('results').style.display = 'none';
                
                try {
                    const response = await fetch('/api/search', {
                        method: 'POST',
                        headers: {'Content-Type': 'application/json'},
                        body: JSON.stringify({
                            query,
                            include_arxiv: includeArxiv,
                            include_wikipedia: includeWikipedia
                        })
                    });
                    
                    const data = await response.json();
                    
                    if (data.success) {
                        displayResults(data);
                    } else {
                        showStatus(`❌ Search failed: ${data.error}`, 'error');
                    }
                } catch (error) {
                    showStatus(`❌ Error: ${error.message}`, 'error');
                } finally {
                    document.getElementById('loading').classList.remove('active');
                }
            }
            
            function displayResults(data) {
                document.getElementById('arxiv-count').textContent = data.arxiv_papers;
                document.getElementById('wiki-count').textContent = data.wikipedia_articles;
                document.getElementById('response-count').textContent = Object.keys(data.responses).filter(k => data.responses[k]).length;
                
                let html = '';
                
                if (data.responses.groq) {
                    html += `
                        <div class="response-box groq">
                            <div class="response-title">🚀 Groq Response</div>
                            <div class="response-content">${escapeHtml(data.responses.groq)}</div>
                        </div>
                    `;
                }
                
                if (data.responses.google) {
                    html += `
                        <div class="response-box google">
                            <div class="response-title">🧠 Google Response</div>
                            <div class="response-content">${escapeHtml(data.responses.google)}</div>
                        </div>
                    `;
                }
                
                if (!html) {
                    html = '<div class="status warning">⚠️ No responses generated</div>';
                }
                
                document.getElementById('responses-container').innerHTML = html;
                document.getElementById('results').style.display = 'block';
            }
            
            function escapeHtml(text) {
                const map = {
                    '&': '&amp;',
                    '<': '&lt;',
                    '>': '&gt;',
                    '"': '&quot;',
                    "'": '&#039;'
                };
                return text.replace(/[&<>"']/g, m => map[m]);
            }
        </script>
    </body>
    </html>
    """


@app.post("/api/setup")
async def setup_api(request: APIKeyRequest):
    """Setup API keys"""
    global agent, agent_ready
    
    try:
        if not request.groq_key and not request.google_key:
            return JSONResponse({
                "success": False,
                "error": "Please provide at least one API key"
            }, status_code=400)
        
        agent = SearchAgent()
        agent.api_config.set_api_keys(
            groq_key=request.groq_key,
            google_key=request.google_key
        )
        
        # Initialize LLM handler
        from utils.llm_handler import LLMHandler
        agent.llm_handler = LLMHandler(agent.api_config)
        
        agent_ready = True
        return {"success": True, "message": "Setup successful"}
    
    except Exception as e:
        return JSONResponse({
            "success": False,
            "error": str(e)
        }, status_code=400)


@app.post("/api/search", response_model=SearchResponse)
async def search_endpoint(request: SearchRequest):
    """Perform search"""
    global agent, agent_ready
    
    if not agent_ready or agent is None:
        raise HTTPException(status_code=400, detail="API not configured. Please setup API keys first.")
    
    try:
        # Perform search and get results
        print(f"[SEARCH] Query: {request.query}")
        results = agent.search_and_answer(request.query)
        
        # Handle errors from search_and_answer
        if 'error' in results:
            return SearchResponse(
                success=False,
                query=request.query,
                arxiv_papers=0,
                wikipedia_articles=0,
                responses={},
                error=results['error']
            )
        
        arxiv_count = len(results.get('search_results', {}).get('arxiv', []))
        wiki_count = len(results.get('search_results', {}).get('wikipedia', []))
        
        responses = {
            'groq': results.get('llm_responses', {}).get('groq'),
            'google': results.get('llm_responses', {}).get('google')
        }
        
        print(f"[SEARCH] Results - Arxiv: {arxiv_count}, Wikipedia: {wiki_count}")
        
        return SearchResponse(
            success=True,
            query=request.query,
            arxiv_papers=arxiv_count,
            wikipedia_articles=wiki_count,
            responses=responses
        )
    
    except Exception as e:
        print(f"[ERROR] Search failed: {str(e)}")
        import traceback
        traceback.print_exc()
        return SearchResponse(
            success=False,
            query=request.query,
            arxiv_papers=0,
            wikipedia_articles=0,
            responses={},
            error=str(e)
        )


@app.get("/health")
async def health():
    """Health check endpoint"""
    return {"status": "ok", "agent_ready": agent_ready}


if __name__ == "__main__":
    print("\n" + "="*60)
    print("🚀 Multi-LLM Search Agent Web Interface")
    print("="*60)
    print("\n📱 Server starting on: http://localhost:8000")
    print("🌐 Open your browser and visit: http://localhost:8000")
    print("\n💡 Tips:")
    print("   • Get Groq key: https://console.groq.com")
    print("   • Use Python 3.8-3.12 (not 3.14)")
    print("   • API keys are never stored\n")
    
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8000,
        log_level="info"
    )
