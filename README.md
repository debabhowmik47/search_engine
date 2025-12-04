📖 Overview

This Streamlit app lets you chat with a LangChain agent that can pull in real-time results from ArXiv, Wikipedia, and DuckDuckGo. Under the hood it uses:

Groq Cloud LLM via langchain_groq

LangChain tools for ArXiv, Wikipedia, and DuckDuckGo

StreamlitCallbackHandler to display the agent’s reasoning steps in real time

Whether you’re asking about the latest research paper, a quick encyclopedia lookup, or a general web search, the agent will plan, execute, and display each thought before presenting its answer.

✨ Features

Zero-shot reasoning
Uses LangChain’s REACT pattern to decide when to invoke each tool.

Live streaming of “thoughts”
See the agent’s chain-of-thought in the UI as it retrieves and processes information.

Multi-tool support:-

🔬 ArXiv (via ArxivAPIWrapper) for the latest academic papers

📚 Wikipedia (via WikipediaAPIWrapper) for concise summaries

🌐 DuckDuckGo for general web searches

🚀 Getting Started

Prerequisites
Python 3.10+

