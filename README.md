# Multi-LLM Search Agent

A powerful AI-powered search agent that combines DuckDuckGo/Wikipedia with Groq and Google LLMs to provide comprehensive answers from academic and general knowledge sources.

## Features

### Search Capabilities
- 🔍 **Arxiv Integration**: Search academic papers and research documents
- 📚 **Wikipedia Integration**: Search general knowledge articles via DuckDuckGo
- 🎯 **Combined Search**: Get results from both sources simultaneously

### LLM Support
- 🚀 **Groq API**: Lightning-fast inference with Llama 3 models
- 🧠 **Google Gemini**: Advanced reasoning (optional)
- 🔄 **Multi-Provider**: Use one or both LLMs for comprehensive answers

### User-Friendly
- 💬 **Interactive CLI**: Chat-like interface for queries
- 🌐 **Web Interface**: Beautiful Streamlit UI (NEW!)
- 📊 **Formatted Output**: Clean, organized result display
- ⚡ **Fast Responses**: Groq delivers results in seconds

## Quick Start - Two Ways to Use

### Option 1: Web Interface (Easiest!)

```bash
streamlit run app.py
```

Opens beautiful web UI in your browser. Perfect for non-technical users!

**Features:**
- 🎨 Clean, modern design
- 📊 Tabbed results display
- 🔐 Secure API key input
- 📜 Search history
- 📱 Responsive layout

See [STREAMLIT_GUIDE.md](STREAMLIT_GUIDE.md) for details.

### Option 2: Command Line (Powerful!)

```bash
python main.py
```

Traditional CLI with full control and advanced options.

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Internet connection (for API calls)

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/intellisearch3.git
cd intellisearch3
```

### Step 2: Create Virtual Environment

**Windows (PowerShell):**
```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```bash
python -m venv .venv
.venv\Scripts\activate.bat
```

**Linux/Mac:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

Or use the setup script:
- **Windows**: Double-click `setup.bat`
- **Linux/Mac**: `bash setup.sh`

## Getting API Keys

### Groq API Key (Free - Recommended)

1. Visit: https://console.groq.com
2. Click "Sign Up" and create a free account
3. Navigate to **API Keys** section
4. Click **Create New API Key**
5. Copy the entire key (starts with `gsk_`)
6. Keep it safe - you'll use it when running the agent

**Free Tier**: Generous limits, no credit card required!

### Google Gemini API Key (Optional - Free Limited)

1. Visit: https://aistudio.google.com/app/apikey
2. Click "Create API Key"
3. Select/create a Google Cloud project
4. Copy the generated key (starts with `AIza`)

**Free Tier**: 60 requests/minute, requires Google account

## Quick Start

### Method 1: Web Interface (Recommended for Most Users)

```bash
streamlit run app.py
```

This opens a beautiful web interface in your browser:
- Visual search interface
- Tabbed results display
- Search history
- No command-line needed!

See [STREAMLIT_GUIDE.md](STREAMLIT_GUIDE.md) for full instructions.

### Method 2: Windows CLI (Quick)
1. Double-click **`run.bat`**
2. Paste your Groq API key when prompted
3. Press Enter to skip Google key (or paste it if you have one)
4. Type your search query!

### Method 3: Command Line

**Windows:**
```bash
.\.venv\Scripts\python.exe main.py
```

**Linux/Mac:**
```bash
source .venv/bin/activate
python main.py
```

### Method 4: Activate Virtual Environment

**Windows PowerShell:**
```bash
.\.venv\Scripts\Activate.ps1
python main.py
```

**Windows CMD:**
```bash
.venv\Scripts\activate.bat
python main.py
```

**Linux/Mac:**
```bash
source .venv/bin/activate
python main.py
```

## Usage Examples

### Example 1: Technology Question
```
[INPUT] Enter your search query: What is machine learning?

Searching for: What is machine learning?
Found 0 arxiv papers and 3 Wikipedia articles.

SEARCH RESULTS & AI ANALYSIS

Arxiv Papers Found: 0
Wikipedia Articles Found: 3

AI GENERATED ANSWERS:

[GROQ]:
Machine learning (ML) is a field of study in artificial 
intelligence concerned with the development and study of 
statistical algorithms that can learn from data and generalize 
to unseen data...
```

### Example 2: Research Query
```
[INPUT] Enter your search query: Recent advances in quantum computing

Searching for: Recent advances in quantum computing
Found 2 arxiv papers and 2 Wikipedia articles.

SEARCH RESULTS & AI ANALYSIS

Arxiv Papers Found: 2
Wikipedia Articles Found: 2

AI GENERATED ANSWERS:

[GROQ]:
Quantum computing is experiencing rapid advancement with several 
key breakthroughs. Recent developments include improvements in 
quantum error correction and the introduction of larger qubit systems...
```

## Project Structure

```
intellisearch3/
├── agents/
│   ├── __init__.py
│   └── search_agent.py          # Main agent orchestrator
├── config/
│   ├── __init__.py
│   ├── api_config.py            # API key management
│   └── settings.py              # Configuration settings
├── utils/
│   ├── __init__.py
│   ├── search_engine.py         # Arxiv & Wikipedia search
│   └── llm_handler.py           # Groq & Google LLM integration
├── main.py                      # Entry point
├── requirements.txt             # Python dependencies
├── setup.sh                     # Linux/Mac setup
├── setup.bat                    # Windows setup
├── run.sh                       # Linux/Mac run script
├── run.bat                      # Windows run script
├── README.md                    # This file
└── .gitignore                   # Git ignore rules
```

## Configuration

### models/settings.py

Customize search and response settings:

```python
ARXIV_MAX_RESULTS = 3           # Number of arxiv papers
WIKIPEDIA_MAX_RESULTS = 3       # Number of wiki articles
GROQ_MODEL = "llama-3.3-70b-versatile"  # Groq model
TEMPERATURE = 0.7               # Response creativity (0-1)
MAX_TOKENS = 1024               # Max response length
```

### Changing Models

The agent automatically tries:
1. `llama-3.3-70b-versatile` (latest, most capable)
2. `llama-3.1-8b-instant` (faster fallback)

Models are tried in order until one works.

## Troubleshooting

### Error: "ModuleNotFoundError: No module named 'ddgs'"

**Solution**: Use the virtual environment Python:
```bash
.\.venv\Scripts\python.exe main.py  # Windows
source .venv/bin/activate && python main.py  # Linux/Mac
```

Don't use bare `python main.py`

### Error: "Invalid API Key"

1. Verify the key is completely copied (no spaces)
2. Check key format:
   - Groq keys start with `gsk_`
   - Google keys start with `AIza`
3. Regenerate key if needed in API console

### No Responses Generated

1. Check internet connection
2. Verify API key is valid and active
3. Try a simpler query
4. Check API rate limits

### Slow Responses

- Groq is fast, but initial requests may take longer
- Network latency affects speed
- Complex queries take longer to process
- Try with smaller max_results

## Advanced Usage

### Using Environment Variables

Create a `.env` file (don't commit this!):
```env
GROQ_API_KEY=gsk_your_key_here
GOOGLE_API_KEY=AIza_your_key_here
```

Then in Python:
```python
import os
from dotenv import load_dotenv

load_dotenv()
groq_key = os.getenv("GROQ_API_KEY")
google_key = os.getenv("GOOGLE_API_KEY")
```

### Programmatic Usage

```python
from agents.search_agent import SearchAgent
from config.api_config import APIConfig

# Create agent
agent = SearchAgent()
agent.api_config.set_api_keys(groq_key="your_key")
agent.llm_handler = LLMHandler(agent.api_config)

# Search and get answer
results = agent.search_and_answer("your query")
agent.display_results(results)

# Access components individually
papers = results['search_results']['arxiv']
articles = results['search_results']['wikipedia']
response = results['llm_responses']['groq']
```

### Custom Search Configuration

```python
# Search with custom limits
results = agent.search_engine.combined_search(
    query="machine learning",
    arxiv_max=10,     # More papers
    wiki_max=5        # Fewer articles
)
```

## API Rate Limits

### Groq
- Free tier: Generous limits
- No credit card required
- Check console for current limits: https://console.groq.com

### Google Gemini
- Free tier: 60 requests/minute
- Paid tier: Higher limits
- Monitor usage at: https://aistudio.google.com

## Security Notes

⚠️ **IMPORTANT**: Never commit your API keys!

1. Keys are NOT stored in code
2. They're only used at runtime (when you paste them)
3. `.gitignore` excludes `.env` files
4. Never share your API keys publicly

If you accidentally commit a key:
1. Regenerate it in the API console immediately
2. Rewrite git history: `git filter-branch`

## Contributing

Contributions welcome! Areas for improvement:
- [ ] Support for more search sources
- [ ] Additional LLM providers
- [ ] Web interface
- [ ] Caching mechanism
- [ ] Response saving/export
- [ ] More sophisticated prompting

## License

MIT License - Feel free to use, modify, and distribute

## Support

### Getting Help

1. Check **GETTING_API_KEYS.md** for API setup
2. Check **USAGE_EXAMPLES.md** for examples
3. See **API_INTEGRATION.md** for API details
4. Run **diagnose.py** to test your setup

### Documentation Files

- **README.md** (this file) - Overview and setup
- **QUICKSTART.md** - 5-minute quick start
- **GETTING_API_KEYS.md** - Detailed API key setup
- **USAGE_EXAMPLES.md** - Practical usage examples
- **API_INTEGRATION.md** - API details and troubleshooting

## Tested Environment

- Python: 3.8 - 3.12
- OS: Windows, Linux, macOS
- Groq API: Active and tested
- Google Gemini: Supported (with fallbacks)

## Changelog

### v1.0.0 (December 2025)
- Initial release
- Groq and Google LLM support
- Arxiv and Wikipedia integration
- Interactive CLI interface
- Comprehensive documentation

## Author

Created with love for researchers and knowledge seekers! ❤️

---

## Quick Command Reference

```bash
# Setup
python -m venv .venv              # Create virtual environment
.venv\Scripts\activate            # Activate (Windows)
source .venv/bin/activate         # Activate (Linux/Mac)
pip install -r requirements.txt   # Install dependencies

# Run
.\.venv\Scripts\python.exe main.py    # Windows PowerShell
.venv\Scripts\python.exe main.py      # Windows CMD
python main.py                        # After activating venv
bash run.sh                           # Linux/Mac
run.bat                               # Windows (double-click)

# Test
.\.venv\Scripts\python.exe diagnose.py  # Verify setup
.\.venv\Scripts\python.exe list_models.py  # Check available models

# Clean
rm -r .venv           # Remove virtual environment
rm -r __pycache__     # Remove cache files
rm -r .pytest_cache   # Remove test cache
```

## Future Features

- [ ] Web UI with Flask/Django
- [ ] Docker containerization
- [ ] CI/CD with GitHub Actions
- [ ] Automated testing
- [ ] Result caching
- [ ] Chat history
- [ ] Export to PDF/HTML
- [ ] Custom prompt templates
- [ ] Multi-language support

---

**Made with ❤️ for knowledge seekers**

Start exploring now:
```bash
.\.venv\Scripts\python.exe main.py
```

