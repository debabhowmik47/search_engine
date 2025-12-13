#!/usr/bin/env python
"""Test script for Multi-LLM Search Agent"""

from agents.search_agent import SearchAgent

# Create agent
agent = SearchAgent()

# IMPORTANT: Replace this with your actual Groq API key from https://console.groq.com
GROQ_API_KEY = "gsk_YOUR_ACTUAL_API_KEY_HERE"

# Setup with your actual API key
print("="*60)
print("Testing Multi-LLM Search Agent")
print("="*60)
print("\nIMPORTANT: To get working responses:")
print("1. Get your Groq API key from: https://console.groq.com")
print("2. Replace 'gsk_YOUR_ACTUAL_API_KEY_HERE' in this script")
print("3. Run this script again\n")

print(f"Current API Key Status: {'[CONFIGURED]' if GROQ_API_KEY.startswith('gsk_') and len(GROQ_API_KEY) > 30 else '[NOT SET - USING PLACEHOLDER]'}\n")

agent.api_config.set_api_keys(groq_key=GROQ_API_KEY)

from utils.llm_handler import LLMHandler
agent.llm_handler = LLMHandler(agent.api_config)

# Test search
print("Searching for 'what is machine learning'...\n")
results = agent.search_and_answer("what is machine learning")

# Display results
print("\n" + "="*60)
agent.display_results(results)
