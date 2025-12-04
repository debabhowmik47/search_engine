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

A valid Groq API key (you can obtain one from Groq Cloud)

(Optional) A .env file containing GROQ_API_KEY=<your_key>

Installation
Clone this repo:

bash

git clone https://github.com/your-username/langchain-streamlit-search.git

cd langchain-streamlit-search

Create and activate a virtual env, then install dependencies:

bash

python -m venv venv

source venv/bin/activate      # on Windows: venv\Scripts\activate

pip install -r requirements.txt

(Optional) Copy .env.example to .env and set:

bash

GROQ_API_KEY=your_groq_api_key_here

🎮 Usage

Run the Streamlit app:

bash

streamlit run app.py

In the sidebar, paste your Groq API Key.

Type any query into the chat input, e.g. “What’s the newest paper on machine learning interpretability?”

Watch the agent’s thoughts and actions stream by, then read the final answer.

🛠️ How It Works
User input is captured via st.chat_input.

A ChatGroq LLM client is instantiated with streaming enabled.

We initialize a ZERO_SHOT_REACT_DESCRIPTION agent with three tools:

ArxivQueryRun

WikipediaQueryRun

DuckDuckGoSearchRun

During each user turn, the agent’s intermediate reasoning is displayed in real time using StreamlitCallbackHandler.

The final result is appended to the chat history for context.

🤝 Contributing
Fork the repo

Create a feature branch (git checkout -b feature/new-tool)

Commit your changes (git commit -m "Add new tool integration")

