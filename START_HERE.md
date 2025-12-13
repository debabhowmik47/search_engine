# 🚀 START HERE

Welcome to **Multi-LLM Search Agent**!

Choose your path based on what you want to do:

---

## ⚡ "I just want to run it!" (5 minutes)

**Follow these 4 steps:**

1. **Get free API key** (2 min)
   - Visit: https://console.groq.com
   - Sign up free (no credit card needed)
   - Get your API key (starts with `gsk_`)

2. **Install** (1 min)
   ```bash
   pip install -r requirements.txt
   ```

3. **Run** (30 sec)
   ```bash
   python main.py
   ```
   Or on Windows: Double-click `run.bat`

4. **Search!** (30 sec)
   - Paste your API key when prompted
   - Type a question
   - Get AI-powered answer!

**Done!** You're now using Multi-LLM Search Agent! 🎉

---

## 📖 "I want to learn more" (15 minutes)

**Read in this order:**

1. **[README.md](README.md)** (10 min)
   - Overview and features
   - Full setup guide
   - Usage examples
   - Configuration

2. **[QUICKSTART.md](QUICKSTART.md)** (5 min)
   - Fast 5-minute setup
   - Common commands
   - Troubleshooting basics

---

## 🔧 "I want to understand the code" (30 minutes)

**Study these in order:**

1. **[README.md](README.md#project-structure)** - Understand structure
2. **[API_INTEGRATION.md](API_INTEGRATION.md)** - Learn about APIs
3. **Code files**:
   - [agents/search_agent.py](agents/search_agent.py) - Main logic
   - [utils/search_engine.py](utils/search_engine.py) - Search
   - [utils/llm_handler.py](utils/llm_handler.py) - LLM integration

---

## ❓ "I'm having problems" (varies)

**See [TROUBLESHOOTING.md](TROUBLESHOOTING.md)**

Quick fixes:
1. Run: `python diagnose.py` - Auto-test your setup
2. Check: [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for your error
3. Still stuck? See [README.md#troubleshooting](README.md#troubleshooting)

---

## 💻 "I want to contribute" (1-2 hours)

**Follow this guide:**

1. Read: [.github/CONTRIBUTING.md](.github/CONTRIBUTING.md)
2. Fork the repo on GitHub
3. Make changes
4. Test: `python main.py`
5. Submit pull request!

---

## 📚 "I want complete documentation" (2 hours)

**Read all docs:**

| Time | Document | What's In It |
|------|----------|-------------|
| 15 min | [README.md](README.md) | Overview, setup, examples |
| 5 min | [QUICKSTART.md](QUICKSTART.md) | Fast setup |
| 10 min | [GETTING_API_KEYS.md](GETTING_API_KEYS.md) | Get API keys |
| 10 min | [USAGE_EXAMPLES.md](USAGE_EXAMPLES.md) | Real examples |
| 15 min | [API_INTEGRATION.md](API_INTEGRATION.md) | Technical details |
| 10 min | [TROUBLESHOOTING.md](TROUBLESHOOTING.md) | Fix issues |
| 15 min | [GITHUB_SETUP.md](GITHUB_SETUP.md) | Publish on GitHub |
| 5 min | [DOCS_INDEX.md](DOCS_INDEX.md) | Documentation index |

**Total**: 85 minutes of comprehensive documentation ✓

---

## 🎯 Feature Overview

### What This Does
- 🔍 Searches academic papers (Arxiv)
- 📚 Searches general knowledge (Wikipedia)
- 🤖 Gets AI answers from Groq (fast!) or Google (detailed)
- 💬 Interactive chat-like interface
- ⚡ Works on Windows, Linux, Mac

### Example Usage
```
You: "What is machine learning?"

Agent:
- Finds 3 Wikipedia articles
- Gets AI answer from Groq
- Shows you the results!
```

---

## 📋 What You Need

### To Get Started
- [x] Python 3.8+ (on your computer)
- [x] Free Groq API key (2 minutes to get)
- [x] Internet connection
- [x] That's it! ✓

### Optional
- [ ] Google API key (for more advanced answers)
- [ ] Text editor (to customize code)
- [ ] Git (to contribute)

---

## 🔑 Getting API Keys

### Groq (Free - Recommended)
1. Go to: https://console.groq.com
2. Click "Sign Up"
3. Create account (no credit card!)
4. Click "API Keys"
5. Click "Create New API Key"
6. Copy the key (starts with `gsk_`)
7. Done! Use this key when running the agent

**Total time**: 2 minutes

### Google (Optional - Free Limited)
1. Go to: https://aistudio.google.com/app/apikey
2. Click "Create API Key"
3. Copy the key
4. Use when running agent (or skip it)

**Total time**: 2 minutes

See [GETTING_API_KEYS.md](GETTING_API_KEYS.md) for detailed steps.

---

## 🚀 Quick Start Commands

### Windows
```bash
# Method 1: Just double-click run.bat

# Method 2: Command line
.\.venv\Scripts\python.exe main.py

# Method 3: After activating venv
.\.venv\Scripts\Activate.ps1
python main.py
```

### Linux/Mac
```bash
# Method 1: Use run script
bash run.sh

# Method 2: After activating venv
source .venv/bin/activate
python main.py
```

---

## 📁 Project Contents

### Main Files
- **main.py** - Run this! (entry point)
- **requirements.txt** - Dependencies

### Folders
- **agents/** - Search agent logic
- **config/** - Configuration files
- **utils/** - Utilities (search, LLM)
- **.github/** - GitHub files

### Scripts
- **run.bat** / **run.sh** - Easy startup
- **diagnose.py** - Test your setup
- **list_models.py** - Available Groq models

### Documentation
- **README.md** - Full guide
- **QUICKSTART.md** - Fast setup
- **GETTING_API_KEYS.md** - API keys
- **TROUBLESHOOTING.md** - Fix issues
- **USAGE_EXAMPLES.md** - Real examples
- **[and more...](DOCS_INDEX.md)**

---

## 💡 Pro Tips

### Tip 1: Use Groq for Speed
- Groq is the fastest option
- Free tier is very generous
- Perfect for quick searches

### Tip 2: Try Both APIs
- Groq for speed
- Google for complex reasoning
- Get two different perspectives!

### Tip 3: Search Wisely
- Specific searches work best
- Try: "machine learning" not "artificial intelligence theory"
- Arxiv = academic papers
- Wikipedia = general knowledge

### Tip 4: Check Your Limits
- Groq: Very generous (rarely hit limit)
- Google: 60 requests/minute free tier
- Can use both together for reliability

---

## ✅ Verification Checklist

Before you start:

- [ ] Python 3.8+ installed (check: `python --version`)
- [ ] Internet connection working
- [ ] Groq API key obtained (from https://console.groq.com)
- [ ] Ready to run the agent!

---

## 🎓 Learning Path

### Beginner
1. Get API key
2. Run: `python main.py`
3. Try a few searches
4. Read [QUICKSTART.md](QUICKSTART.md)

### Intermediate
1. Read [README.md](README.md)
2. Try different search types
3. Use both APIs
4. Customize settings in [config/settings.py](config/settings.py)

### Advanced
1. Read [API_INTEGRATION.md](API_INTEGRATION.md)
2. Study source code
3. Modify agents/search_agent.py
4. Consider contributing!

---

## 🤝 Contributing

Want to help? See [.github/CONTRIBUTING.md](.github/CONTRIBUTING.md)

Easy ways to contribute:
- Report bugs
- Improve documentation
- Add features
- Share on social media
- Give feedback

---

## ❓ Quick FAQ

### Q: Do I need to pay?
**A:** No! Groq API is completely free with generous limits.

### Q: Can I use it offline?
**A:** No, it needs internet for search and API calls.

### Q: Does it work on my OS?
**A:** Yes! Windows, Linux, Mac all supported.

### Q: Can I modify it?
**A:** Absolutely! MIT License - do what you want.

### Q: Is my API key safe?
**A:** Keys are never stored. Never commit `.env` files.

### Q: Why no results?
**A:** Check internet, verify API key, try simpler search term.

---

## 📞 Getting Help

### Common Issues
1. **ModuleNotFoundError**: Use venv Python: `.\.venv\Scripts\python.exe main.py`
2. **Invalid API key**: Verify copied entire key, no spaces
3. **No internet**: Check connection
4. **Rate limit**: Wait a minute, try again

### Resources
- 📖 **Documentation**: [DOCS_INDEX.md](DOCS_INDEX.md)
- 🐛 **Troubleshooting**: [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
- 🔍 **Examples**: [USAGE_EXAMPLES.md](USAGE_EXAMPLES.md)
- 🧪 **Test**: `python diagnose.py`

---

## 🎉 Ready to Get Started?

### Pick Your Path:

1. **⚡ Quick Start** (5 min)
   → Follow the "I just want to run it!" section above

2. **📖 Learn More** (15 min)
   → Read README.md and QUICKSTART.md

3. **🔧 Deep Dive** (30 min)
   → Study API_INTEGRATION.md and source code

4. **🤝 Contribute** (1-2 hours)
   → Fork, modify, submit PR!

---

## 🚀 Next Steps

1. **Get API key** - https://console.groq.com (2 min)
2. **Run the agent** - `python main.py` (30 sec)
3. **Search something!** - Ask a question
4. **Explore more** - Check documentation
5. **Help others** - Star on GitHub, share with friends!

---

## 📊 Project Statistics

- **Lines of Code**: ~1,200
- **Documentation**: ~6,000 lines
- **Python Versions Supported**: 3.8, 3.9, 3.10, 3.11, 3.12
- **Platforms Supported**: Windows, Linux, macOS
- **Features**: 20+ (search, LLM, configuration, etc.)
- **Setup Time**: 5 minutes
- **Learning Time**: 15-30 minutes

---

## 🏆 What Users Love

✨ **Fast Setup** - Running in 5 minutes
✨ **No Paywall** - Completely free
✨ **Easy to Use** - Simple command-line interface
✨ **Well Documented** - 85 minutes of documentation
✨ **Cross-Platform** - Works everywhere
✨ **Extensible** - Easy to modify and extend
✨ **Reliable** - Fallback mechanisms built-in

---

## 📝 Quick Links

### Get Started
- [QUICKSTART.md](QUICKSTART.md) - 5-minute setup
- [GETTING_API_KEYS.md](GETTING_API_KEYS.md) - Free API keys

### Learn & Use
- [README.md](README.md) - Full guide
- [USAGE_EXAMPLES.md](USAGE_EXAMPLES.md) - Real examples
- [API_INTEGRATION.md](API_INTEGRATION.md) - Technical details

### Fix Issues
- [TROUBLESHOOTING.md](TROUBLESHOOTING.md) - Common problems
- [DOCS_INDEX.md](DOCS_INDEX.md) - All documentation

### Contribute
- [.github/CONTRIBUTING.md](.github/CONTRIBUTING.md) - Contributor guide
- [GITHUB_SETUP.md](GITHUB_SETUP.md) - Publish on GitHub

---

**Welcome aboard! Let's search! 🚀**

---

## 📢 Tell Your Friends!

Have you tried the Multi-LLM Search Agent?

- ⭐ Star this repository on GitHub
- 📢 Share on social media
- 💬 Tell your friends
- 🤝 Contribute improvements
- 📝 Give feedback

Every share helps! Thank you! 💙

---

*Last Updated: December 2025*  
*Status: ✓ Ready to Use*  
*License: MIT*
