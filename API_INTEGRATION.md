# API Integration Guide

## Overview

The Multi-LLM Search Agent supports integration with two different LLM providers:
1. **Groq** - Fast, open-source models via Groq API
2. **Google Gemini** - Advanced reasoning via Google's Generative AI API

## Groq API Integration

### Setup

1. **Get API Key**
   - Visit: https://console.groq.com
   - Sign up for free account
   - Go to API Keys section
   - Create new API key
   - Copy and save the key

2. **Integration in Agent**
   ```python
   from groq import Groq
   
   client = Groq(api_key="your-groq-api-key")
   ```

### Usage

```python
from agents.search_agent import SearchAgent

agent = SearchAgent()
agent.api_config.set_api_keys(groq_key="your-key")
agent.llm_handler = LLMHandler(agent.api_config)

response = agent.llm_handler.generate_response_groq(
    prompt="Your question",
    context="Search results context"
)
```

### Models Available

- **mixtral-8x7b-32768** (current)
- Other models via Groq console

### Features

- ✓ Fast inference
- ✓ Open-source models
- ✓ No rate limits mentioned
- ✓ Free tier available
- ✓ Good for real-time applications

## Google Generative AI Integration

### Setup

1. **Get API Key**
   - Visit: https://aistudio.google.com/app/apikey
   - Click "Create API Key"
   - Select/create Google Cloud project
   - Copy the generated key

2. **Integration in Agent**
   ```python
   import google.generativeai as genai
   
   genai.configure(api_key="your-google-key")
   model = genai.GenerativeModel('gemini-pro')
   ```

### Usage

```python
from agents.search_agent import SearchAgent

agent = SearchAgent()
agent.api_config.set_api_keys(google_key="your-key")
agent.llm_handler = LLMHandler(agent.api_config)

response = agent.llm_handler.generate_response_google(
    prompt="Your question",
    context="Search results context"
)
```

### Models Available

- **gemini-pro** (current)
- **gemini-pro-vision** (with image analysis)
- Other models via Google AI Studio

### Features

- ✓ Advanced reasoning
- ✓ Multi-modal support
- ✓ Context understanding
- ✓ Free tier available
- ✓ Suitable for complex queries

### Known Issues

- Python 3.14 compatibility issue (handled gracefully)
- May fall back to Groq if Google API unavailable

## Using Both APIs

### Configuration

```python
from agents.search_agent import SearchAgent

agent = SearchAgent()
agent.api_config.set_api_keys(
    groq_key="your-groq-key",
    google_key="your-google-key"
)
agent.llm_handler = LLMHandler(agent.api_config)
```

### Getting Combined Responses

```python
responses = agent.llm_handler.generate_response(
    prompt="Your question",
    context="Search results"
)

# Returns: {'groq': 'answer1', 'google': 'answer2'}
```

### Benefits

- Compare answers from different LLMs
- Get diverse perspectives
- Better fact-checking
- Comprehensive analysis

## API Rate Limits

### Groq

- Check console for current limits
- Generally generous free tier
- Monitor usage in dashboard

### Google

- Free tier: Reasonable limits
- Paid tier: Higher limits available
- Check: https://aistudio.google.com

## Error Handling

### Groq API Errors

```python
try:
    response = agent.llm_handler.generate_response_groq(prompt, context)
except Exception as e:
    print(f"Groq API error: {e}")
    # Fallback to another provider
```

### Google API Errors

```python
try:
    response = agent.llm_handler.generate_response_google(prompt, context)
except Exception as e:
    print(f"Google API error: {e}")
    # Fallback to Groq
```

## Security Best Practices

### 1. Never Commit API Keys
```bash
# Add to .gitignore
.env
.env.local
api_keys.py
```

### 2. Use Environment Variables
```python
import os
from dotenv import load_dotenv

load_dotenv()
groq_key = os.getenv("GROQ_API_KEY")
google_key = os.getenv("GOOGLE_API_KEY")
```

### 3. Example .env File
```
GROQ_API_KEY=your_groq_key_here
GOOGLE_API_KEY=your_google_key_here
```

### 4. Load in Application
```python
from config.api_config import APIConfig
import os
from dotenv import load_dotenv

load_dotenv()
api_config = APIConfig()
api_config.set_api_keys(
    groq_key=os.getenv("GROQ_API_KEY"),
    google_key=os.getenv("GOOGLE_API_KEY")
)
```

## Cost Estimation

### Groq (Free)
- Generally no costs for free tier
- Check console for pricing

### Google Gemini (Free + Paid)
- Free tier: 60 requests per minute
- Paid tier: $0.00075 per 1K input tokens, $0.003 per 1K output tokens
- Monitor usage to stay within limits

## API Monitoring

### Groq Console
- Dashboard: https://console.groq.com
- View API usage
- Manage keys
- Check logs

### Google AI Studio
- Dashboard: https://aistudio.google.com
- Monitor usage
- Manage API keys
- View quotas

## Troubleshooting

### Issue: "Invalid API key"
**Solution:**
1. Verify key is correctly copied (no spaces)
2. Check key hasn't expired
3. Regenerate key if needed

### Issue: "Rate limit exceeded"
**Solution:**
1. Wait before making requests
2. Implement request queuing
3. Consider paid tier
4. Use both APIs to distribute load

### Issue: "API unavailable"
**Solution:**
1. Check API status page
2. Verify internet connection
3. Try again in a few minutes
4. Use fallback provider

### Issue: "Python compatibility"
**Solution:**
1. Use Python 3.11 or 3.12 (not 3.14)
2. Agent handles Google API gracefully
3. Falls back to Groq automatically

## Advanced Integration

### Custom Response Formatting

```python
def format_groq_response(response: str) -> str:
    """Custom formatting for Groq responses"""
    return f"[GROQ] {response}"

def format_google_response(response: str) -> str:
    """Custom formatting for Google responses"""
    return f"[GOOGLE] {response}"
```

### Streaming Responses (Future)

```python
# Support for streaming responses can be added
# to reduce latency for large responses
```

### Custom Prompts

```python
SYSTEM_PROMPT = """You are an expert assistant answering 
questions based on search results from academic papers 
and Wikipedia articles."""

response = agent.llm_handler.generate_response_groq(
    prompt=user_query,
    context=search_results,
    system_prompt=SYSTEM_PROMPT
)
```

## API Comparison

| Feature | Groq | Google |
|---------|------|--------|
| Speed | Very Fast | Fast |
| Reasoning | Good | Excellent |
| Cost | Free | Free (limited) |
| Setup | Easy | Easy |
| Python 3.14 | Works | Has issues |
| Free Quota | Generous | Moderate |
| Model Variety | Limited | Good |

## References

- **Groq API**: https://console.groq.com/docs
- **Google AI**: https://ai.google.dev/docs
- **Groq Models**: https://console.groq.com/docs/models
- **Google Models**: https://ai.google.dev/models/gemini

## Support

For API-specific issues:
- Groq: support@groq.com
- Google: https://support.google.com/aistudio
