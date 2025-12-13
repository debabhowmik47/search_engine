#!/usr/bin/env python
"""Check available Groq models"""

from groq import Groq

print("Enter your Groq API key: ", end='', flush=True)
api_key = input().strip()

client = Groq(api_key=api_key)

print("\nFetching available models...")
try:
    models = client.models.list()
    print(f"\nAvailable models ({len(models.data)} total):")
    for model in models.data:
        print(f"  - {model.id}")
except Exception as e:
    print(f"Error: {e}")
