# Quick Start Guide - 5 Minutes

Get the Multi-LLM Search Agent running in 5 minutes!

## Step 1: Get API Key (2 minutes)

### Groq (Free - Recommended)
1. Go to https://console.groq.com
2. Sign up (free, no credit card needed)
3. Click **API Keys**
4. Click **Create New API Key**
5. Copy the key (starts with `gsk_`)

Done! You have an API key.

## Step 2: Install Software (2 minutes)

### Windows
1. Open PowerShell in the project folder
2. Run: `pip install -r requirements.txt`

### Linux/Mac
1. Open Terminal in the project folder
2. Run: `pip install -r requirements.txt`

Done! Dependencies installed.

## Step 3: Run the Agent (1 minute)

### Windows - Easiest Way
Just **double-click `run.bat`**

### Windows - Command Line
```bash
.\.venv\Scripts\python.exe main.py
```

### Linux/Mac
```bash
bash run.sh
```

## Step 4: Use It!

When you see the prompt:
```
Enter your Groq API key (or press Enter to skip): 
```

Paste your API key from Step 1, then press Enter.

Skip Google key by pressing Enter again.

Then search!
```
[INPUT] Enter your search query: What is machine learning?
```

## That's It!

The agent will:
1. Search Wikipedia and Arxiv
2. Get AI answer from Groq
3. Show you the results

### Example Output
```
Query: What is machine learning?

Arxiv Papers Found: 0
Wikipedia Articles Found: 3

AI GENERATED ANSWERS:

[GROQ]:
Machine learning is a field of study in artificial intelligence...
```

## Common Commands

### Run the agent
```bash
.\.venv\Scripts\python.exe main.py      # Windows
source .venv/bin/activate && python main.py  # Linux/Mac
```

### Test your setup
```bash
.\.venv\Scripts\python.exe diagnose.py
```

### See available models
```bash
.\.venv\Scripts\python.exe list_models.py
```

## Troubleshooting

### "ModuleNotFoundError: No module named 'ddgs'"
- Use the correct Python: `.\.venv\Scripts\python.exe main.py`
- Don't use bare `python`

### "Invalid API Key"
- Copy the entire key with no spaces
- Key should start with `gsk_`

### No response showing
- Check internet connection
- Try a simpler query
- Verify API key is valid

## Next Steps

- See [README.md](README.md) for full documentation
- See [USAGE_EXAMPLES.md](USAGE_EXAMPLES.md) for examples
- See [API_INTEGRATION.md](API_INTEGRATION.md) for advanced setup

## Need Help?

Check the documentation files in the project folder:
- **README.md** - Complete guide
- **GETTING_API_KEYS.md** - API key setup
- **API_INTEGRATION.md** - API details
- **USAGE_EXAMPLES.md** - Example usage

---

**You're ready to go!** 🚀

Double-click `run.bat` (Windows) or `bash run.sh` (Linux/Mac) to start!
