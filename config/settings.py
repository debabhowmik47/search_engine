"""
Configuration file for Multi-LLM Search Agent
You can optionally store API keys here (not recommended for security)
"""

# Groq API Configuration
GROQ_API_KEY = None  # Set to your Groq API key or use input prompt

# Google API Configuration
GOOGLE_API_KEY = None  # Set to your Google API key or use input prompt

# Search Configuration
ARXIV_MAX_RESULTS = 3  # Maximum number of arxiv papers to search
WIKIPEDIA_MAX_RESULTS = 3  # Maximum number of Wikipedia articles to search

# LLM Configuration
GROQ_MODEL = "llama-3.3-70b-versatile"  # Groq model to use (automatically falls back to llama-3.1-8b-instant if unavailable)
TEMPERATURE = 0.7  # Temperature for response generation (0-1)
MAX_TOKENS = 1024  # Maximum tokens in response
