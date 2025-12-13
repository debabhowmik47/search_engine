# Troubleshooting Guide

Common issues and solutions for the Multi-LLM Search Agent.

## Installation Issues

### Issue: "ModuleNotFoundError: No module named 'ddgs'"

**Cause:** Using system Python instead of virtual environment Python

**Solution:**

Windows:
```bash
.\.venv\Scripts\python.exe main.py
```

Or use the convenience script:
```bash
# Double-click run.bat
```

Linux/Mac:
```bash
source .venv/bin/activate
python main.py
```

Or use the convenience script:
```bash
bash run.sh
```

---

### Issue: "No module named 'groq'" or other import errors

**Cause:** Dependencies not installed

**Solution:**

1. **Activate virtual environment**

Windows:
```bash
.\.venv\Scripts\Activate.ps1
```

Linux/Mac:
```bash
source .venv/bin/activate
```

2. **Install requirements**
```bash
pip install -r requirements.txt
```

3. **Try again**
```bash
python main.py
```

---

### Issue: "python: command not found" (Linux/Mac)

**Cause:** Python not installed or not in PATH

**Solution:**

1. **Install Python**

Mac with Homebrew:
```bash
brew install python3
```

Linux (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install python3 python3-pip
```

2. **Create virtual environment with python3**
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

### Issue: "pip: command not found"

**Cause:** pip not installed with Python

**Solution:**

1. **Ensure pip is installed**

Windows:
```bash
python -m pip install --upgrade pip
```

Linux/Mac:
```bash
python3 -m pip install --upgrade pip
```

2. **Install requirements using pip module**
```bash
python -m pip install -r requirements.txt
```

---

## API Key Issues

### Issue: "Enter your Groq API key" prompt but no input accepted

**Cause:** Terminal encoding issue (rare)

**Solution:**

1. **Try running with explicit encoding**

Windows PowerShell:
```bash
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
python main.py
```

2. **Or restart terminal and try again**

---

### Issue: "Invalid API key" error

**Cause:** API key is incorrect or improperly copied

**Solution:**

1. **Verify API key format**
   - Groq keys: Start with `gsk_`
   - Google keys: Start with `AIza`

2. **Check for spaces**
   - Make sure no extra spaces before/after key
   - Copy directly from console, don't retype

3. **Regenerate key**

Groq:
- Go to https://console.groq.com
- Delete old key
- Create new key
- Copy entire new key

Google:
- Go to https://aistudio.google.com/app/apikey
- Delete old key
- Create new key
- Copy entire new key

4. **Try again with new key**

---

### Issue: "No API keys provided"

**Cause:** Both Groq and Google keys were skipped (both empty)

**Solution:**

At least one API key required. Run again:

```bash
python main.py
```

When prompted for Groq key:
- **Don't** press Enter immediately
- Paste your API key and press Enter

---

### Issue: "Rate limit exceeded"

**Groq:** Rarely happens with free tier (very generous limits)

**Google:** Free tier allows 60 requests/minute

**Solution:**

1. **Wait a minute and try again**

2. **If using Google API**
   - Use only Groq: Press Enter when Google key is prompted
   - Or wait 1 minute between queries

3. **For Groq quota issues**
   - Check https://console.groq.com
   - View your usage dashboard

---

## Search Issues

### Issue: "No search results found"

**Cause:** Query too specific or no matching papers/articles

**Solution:**

1. **Try broader search terms**
   - Bad: "quantum entanglement in superconducting qubits with phonon coupling"
   - Good: "quantum computing" or "superconducting qubits"

2. **Try simpler keywords**
   - Bad: "photosynthetic autotrophs mechanism"
   - Good: "photosynthesis"

3. **Check internet connection**
   - Make sure you're connected to internet
   - Some networks block API calls

---

### Issue: "Wikipedia search returns many results but Arxiv returns nothing"

**Cause:** Arxiv only has academic papers, not all topics covered

**Solution:**

This is normal! Arxiv focuses on academic research:
- ✓ Good for: physics, math, computer science, biology
- ✗ Not good for: celebrity gossip, sports scores, current events

Try searching academic topics instead.

---

## Response Issues

### Issue: "Waiting for response..." but no answer appears

**Cause:** 
1. API timeout (slow internet)
2. API service down
3. API key invalid despite appearing correct

**Solution:**

1. **Wait longer**
   - Groq usually responds in 2-5 seconds
   - First query might take 10 seconds
   - Slow internet might take 30 seconds

2. **Check internet connection**
   - Test: `ping google.com`
   - If no response, internet is down

3. **Check API status**

Groq:
- Status: https://console.groq.com/status
- Or check Twitter: @Groq

Google:
- Status: https://status.cloud.google.com

4. **Try different query**
   - Simple query: "machine learning"
   - Complex query: "quantum gravity string theory mathematical framework"

5. **Check error output**
   - Look for red error text
   - Note the error message
   - See "Common Error Messages" below

---

### Issue: "Response is cut off or incomplete"

**Cause:** Response length limit (rare)

**Solution:**

1. **Try more specific query**
   - This asks for shorter response

2. **Try simpler query**
   - Fewer search results = shorter response

---

### Issue: Response doesn't match the query

**Cause:** LLM used irrelevant search results or misunderstood

**Solution:**

1. **Try rephrasing query**
   - Bad: "how to compute derivative"
   - Good: "what is calculus derivative"

2. **Use quotes for exact terms**
   - "machine learning" (more specific)
   - vs "machine" (might return irrelevant results)

---

## Common Error Messages

### "HTTPError 401: Unauthorized"

**Meaning:** API key is invalid or wrong

**Fix:**
1. Generate new API key
2. Verify you copied entire key
3. Check for extra spaces

---

### "requests.exceptions.ConnectionError"

**Meaning:** Can't connect to internet or API server

**Fix:**
1. Check internet connection
2. Try again in a few seconds
3. Check if API service is down

---

### "TimeoutError: Connection timed out"

**Meaning:** API took too long to respond

**Fix:**
1. Check internet speed
2. Try simpler query
3. Wait and try again

---

### "TypeError: 'NoneType' object is not..."

**Meaning:** Unexpected error in code (rare)

**Fix:**
1. Note exact error message
2. Restart Python: `python main.py`
3. Try simple query: "hello world"

---

## Performance Issues

### Issue: Agent is slow

**Cause:** Multiple factors possible

**Solution:**

1. **Check internet speed**
   - Test: https://speedtest.net
   - Minimum required: 5 Mbps

2. **Try simpler queries**
   - Complex queries with many results slow down LLM

3. **Check system resources**
   - Close other heavy applications
   - Restart computer if needed

4. **Use Groq instead of Google**
   - Groq is much faster
   - Google can be slow with complex queries

---

### Issue: Memory usage is high

**Cause:** Storing many search results in memory

**Solution:**

1. **Restart the agent**
```bash
# Exit: type 'exit' or press Ctrl+C
# Restart:
python main.py
```

2. **Search fewer results**
   - Default is reasonable
   - Code: Edit `utils/search_engine.py` if needed

---

## Virtual Environment Issues

### Issue: ".venv is not recognized" (Windows)

**Cause:** Virtual environment not activated

**Solution:**

1. **Activate venv**

PowerShell:
```powershell
.\.venv\Scripts\Activate.ps1
```

CMD:
```cmd
.venv\Scripts\activate.bat
```

2. **Verify activated**
   - Should see `(.venv)` at start of command line
   - Like: `(.venv) C:\Users\Name\Desktop\intellisearch3>`

---

### Issue: "cannot be loaded because running scripts is disabled"

**Cause:** PowerShell execution policy (Windows security)

**Solution:**

1. **Allow script execution**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

2. **Or run without activation**
```powershell
.\.venv\Scripts\python.exe main.py
```

---

### Issue: Virtual environment corrupted

**Cause:** Files got corrupted or moved

**Solution:**

1. **Delete the venv**
```bash
rmdir /s .venv        # Windows
rm -rf .venv          # Linux/Mac
```

2. **Recreate it**
```bash
python -m venv .venv
```

3. **Activate and install**

Windows:
```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Linux/Mac:
```bash
source .venv/bin/activate
pip install -r requirements.txt
```

---

## GitHub/Git Issues

### Issue: "fatal: not a git repository"

**Cause:** Git not initialized in folder

**Solution:**
```bash
git init
```

---

### Issue: "remote origin already exists"

**Cause:** Trying to add remote twice

**Solution:**
```bash
git remote remove origin
git remote add origin https://github.com/yourname/intellisearch3.git
```

---

### Issue: Authentication fails when pushing to GitHub

**Cause:** Using old password or no token

**Solution:**

1. **Use token instead of password**
   - Go to: https://github.com/settings/tokens
   - Create new token
   - Use as password

2. **Or set up SSH**
   - More complex but more secure
   - See: https://docs.github.com/en/authentication/connecting-to-github-with-ssh

---

## Getting Help

### If issue not listed here:

1. **Check recent output**
   - Note any error messages
   - Copy full error text

2. **Check GitHub Issues**
   - Go to repository Issues tab
   - Search similar problems
   - Open new issue if not found

3. **Enable debug mode** (if available)
   ```python
   # Edit main.py to add debug output
   import logging
   logging.basicConfig(level=logging.DEBUG)
   ```

4. **Test with diagnostic script**
   ```bash
   python diagnose.py
   ```

---

## Quick Diagnostics

### Run diagnostic test:

```bash
python diagnose.py
```

This checks:
- ✓ API key validity
- ✓ Internet connection
- ✓ Search functionality
- ✓ LLM response

---

## System Requirements Verification

### Check Python version:
```bash
python --version
```
Should be 3.8 or higher (avoid 3.14 for Google API)

### Check pip:
```bash
pip --version
```

### Check installed packages:
```bash
pip list
```

Should include:
- ddgs
- groq
- google-generativeai (optional)
- requests
- arxiv

---

## Still Stuck?

**Before giving up:**

1. ✓ Restart terminal/PowerShell
2. ✓ Restart computer
3. ✓ Reinstall dependencies: `pip install -r requirements.txt`
4. ✓ Create fresh virtual environment
5. ✓ Check internet connection
6. ✓ Verify API keys with fresh copies

If still not working:
- Check GitHub Issues for your exact error
- Open new issue with:
  - Error message (full text)
  - Steps to reproduce
  - System info (Windows/Linux/Mac, Python version)
  - What you tried to fix it

Good luck! 🚀
