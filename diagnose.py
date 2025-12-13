#!/usr/bin/env python
"""Quick test script to diagnose API issues"""

import sys
import os

# Ensure output is not buffered
os.environ['PYTHONUNBUFFERED'] = '1'

from agents.search_agent import SearchAgent
from utils.llm_handler import LLMHandler

print("="*70)
print("GROQ API DIAGNOSTIC TEST")
print("="*70)

# Get API key from user
print("\nEnter your Groq API key (starts with 'gsk_'): ", end='', flush=True)
api_key = input().strip()

if not api_key or not api_key.startswith('gsk_'):
    print("\n[ERROR] Invalid API key format. Must start with 'gsk_'")
    sys.exit(1)

print("\n[INFO] Testing API key validity...")
print(f"[INFO] Key length: {len(api_key)} characters")

# Create agent
agent = SearchAgent()
agent.api_config.set_api_keys(groq_key=api_key)

print("\n[INFO] Initializing Groq client...")
agent.llm_handler = LLMHandler(agent.api_config)

# Simple test query
query = "What is machine learning?"

print(f"\n[INFO] Testing search for: '{query}'")
print("-" * 70)

results = agent.search_and_answer(query)

print("\n" + "="*70)
print("RESULTS")
print("="*70)
agent.display_results(results)

print("\n" + "="*70)
if any(results['llm_responses'].values()):
    print("[SUCCESS] API is working! Responses received.")
else:
    print("[FAILED] No responses received. Check error messages above.")
print("="*70)
