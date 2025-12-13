# Getting Your API Keys

## Groq API Key (Recommended - Free)

### Step 1: Sign Up
1. Go to https://console.groq.com
2. Click "Sign Up" or "Get Started"
3. Create a free account
4. Verify your email

### Step 2: Get API Key
1. After login, navigate to "API Keys" section
2. Click "Create New API Key"
3. Copy the entire API key (starts with `gsk_`)
4. Save it somewhere safe

### Step 3: Use in Agent
When you run `python main.py`:
```
Enter your Groq API key (or press Enter to skip): gsk_xxxxxxxxxxxxxxxxxxxxx
Enter your Google API key (or press Enter to skip): [press Enter to skip]
```
Paste your copied API key and press Enter.

## Google API Key (Optional - Limited Free Tier)

### Step 1: Visit Google AI Studio
1. Go to https://aistudio.google.com/app/apikey
2. Click "Create API Key"
3. Select a Google Cloud project or create new one
4. Copy the generated API key

### Step 2: Use in Agent
When you run `python main.py`:
```
Enter your Groq API key (or press Enter to skip): gsk_xxxxxxxxxxxxxxxxxxxxx
Enter your Google API key (or press Enter to skip): AIza_xxxxxxxxxxxxxxxxxxxxx
```

## How to Run

### Method 1: Interactive Mode
```bash
python main.py
```
Then paste your API key when prompted.

### Method 2: Test with Script
Edit `test_agent.py` and replace:
```python
GROQ_API_KEY = "gsk_YOUR_ACTUAL_API_KEY_HERE"
```
With your actual key, then run:
```bash
python test_agent.py
```

## Troubleshooting

### Error: "Invalid API Key"
- Double-check you copied the entire key
- Make sure there are no extra spaces
- Verify the key is still active in your API console

### Error: "Invalid request"
- Check if your API key format is correct
- Groq keys start with `gsk_`
- Google keys start with `AIza`

### No responses showing
- Verify your API key is valid
- Check your internet connection
- Try a simpler query

## Free Tier Limits

### Groq
- Generous free tier
- No credit card required
- Good for testing

### Google Gemini
- 60 requests per minute
- Limited free quota
- Requires Google account

## Getting Started

1. Get a **Groq API key** from https://console.groq.com (takes 2 minutes)
2. Run the agent: `python main.py`
3. Paste your key when prompted
4. Start searching!

---

The agent will then search Arxiv and Wikipedia, and use your API key to generate AI-powered answers!
