# Streamlit Web Interface

Beautiful web interface for the Multi-LLM Search Agent using Streamlit.

## Features

✨ **Web Interface**
- 🎨 Clean, modern design
- 📱 Responsive layout
- 🔐 Secure API key input
- 📜 Search history

✨ **Interactive**
- Real-time search results
- Multiple search sources
- Tabbed interface
- Source attribution

✨ **User-Friendly**
- No command-line needed
- Intuitive controls
- Quick setup
- Visual feedback

---

## Installation

### Step 1: Install Streamlit

```bash
# If not already installed
pip install streamlit>=1.28.0

# Or install all dependencies
pip install -r requirements.txt
```

### Step 2: Get API Keys

Same as before:

1. **Groq** (Free): https://console.groq.com
   - Sign up
   - Create API Key
   - Copy key (starts with `gsk_`)

2. **Google** (Optional): https://aistudio.google.com
   - Create API Key
   - Copy key (starts with `AIza_`)

---

## Running the Streamlit App

### Option 1: Command Line

```bash
streamlit run app.py
```

This will:
1. Start local server (usually http://localhost:8501)
2. Open browser automatically
3. Show web interface

### Option 2: Using Python Directly

```bash
python -m streamlit run app.py
```

### Option 3: From Virtual Environment

```bash
# Windows
.\.venv\Scripts\streamlit.exe run app.py

# Linux/Mac
source .venv/bin/activate
streamlit run app.py
```

---

## Using the Web Interface

### Step 1: Configure API Keys

1. Look at left sidebar
2. Enter your Groq API key (required)
3. Enter Google API key (optional)
4. Click "🔐 Setup API Keys"
5. Wait for success message

### Step 2: Search

1. Enter your query in the search box
   - Example: "What is machine learning?"
2. Choose sources:
   - ✓ Arxiv (academic papers)
   - ✓ Wikipedia (general knowledge)
3. Click "🔍 Search"

### Step 3: View Results

Results displayed in tabs:

**📋 AI Answers Tab**
- Groq response
- Google response (if available)
- Full AI-generated text

**📰 Search Sources Tab**
- Arxiv papers found
- Wikipedia articles found
- Links to original sources

**📊 Details Tab**
- Technical information
- Query metadata
- Provider information

---

## Features Explained

### Sidebar Configuration
- **API Keys**: Secure input fields (hidden)
- **Status**: Shows if setup is complete
- **About**: Project information
- **GitHub Link**: Quick access to repository

### Main Interface
- **Search Box**: Enter any question
- **Source Selection**: Choose what to search
- **Results Display**: Multiple views of results
- **Search History**: Quick access to previous searches

### Results Display

#### AI Answers Tab
- Shows responses from each LLM provider
- Color-coded (Groq = blue, Google = orange)
- Full formatted text
- Easy to read

#### Search Sources Tab
- Lists all papers and articles found
- Expandable for details
- Links to original sources
- Author and date information

#### Details Tab
- JSON view of results
- Technical metadata
- Provider information
- Count statistics

---

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Enter` | Submit search |
| `Ctrl+L` | Clear sidebar |
| Click tab | Switch views |
| Click history | Re-run search |

---

## Configuration

### Change Search Limits

Edit `app.py` and modify:

```python
# In the search function
results = st.session_state.agent.search_and_answer(
    query=query,
    arxiv_max=5,      # Change max Arxiv results
    wiki_max=5        # Change max Wikipedia results
)
```

### Customize Appearance

Edit CSS in the `st.markdown("""<style>...""")` section

Example: Change colors
```python
.groq-response {
    background-color: #f0f7ff;  # Change this color
}
```

---

## Troubleshooting

### "streamlit: command not found"

**Solution**: Install Streamlit or use python -m:
```bash
pip install streamlit
# Or
python -m streamlit run app.py
```

### "ModuleNotFoundError: No module named 'streamlit'"

**Solution**: Install dependencies:
```bash
pip install -r requirements.txt
```

### "Invalid API key"

**Solution**:
1. Verify key is completely copied (no spaces)
2. Check key format:
   - Groq: starts with `gsk_`
   - Google: starts with `AIza`
3. Regenerate key if needed
4. Clear browser cache and restart app

### Page doesn't update after search

**Solution**:
- Wait a few seconds
- Check API response in browser console
- Verify internet connection
- Try simpler query

### Slow response

**Solutions**:
- Check internet speed
- Try simpler query
- Use Groq (faster than Google)
- Reduce search result limits

---

## Advanced Usage

### Running on Port 8000

```bash
streamlit run app.py --server.port 8000
```

### Disable Browser Auto-Open

```bash
streamlit run app.py --logger.level=error --client.showErrorDetails=false
```

### Deploy to Streamlit Cloud (Optional)

1. Push code to GitHub
2. Go to: https://streamlit.io/cloud
3. Connect GitHub repository
4. Select branch and file (`app.py`)
5. Add secrets (API keys) in Settings
6. Deploy!

**Add Secrets to Streamlit Cloud:**

Create `.streamlit/secrets.toml`:
```toml
GROQ_API_KEY = "your-groq-key"
GOOGLE_API_KEY = "your-google-key"
```

(This file is in .gitignore, never committed)

---

## Development Mode

### Hot Reloading

Streamlit automatically reloads when you change code:

1. Edit `app.py`
2. Save file
3. Browser shows "Source file changed" message
4. Click "Rerun" or wait for auto-rerun

### Debug Mode

Add this to `app.py`:
```python
st.write("DEBUG:", st.session_state)
```

---

## Performance Tips

1. **Cache Results** (future improvement)
   ```python
   @st.cache_data
   def cached_search(query):
       return perform_search(query)
   ```

2. **Reduce Results**
   - Limit Arxiv results
   - Limit Wikipedia results

3. **Use Groq**
   - Faster than Google
   - Generous free tier

4. **Disable Some Sources**
   - Uncheck Arxiv for faster results
   - Focus on Wikipedia for general topics

---

## Comparison: CLI vs Web

| Feature | CLI | Web |
|---------|-----|-----|
| Setup | Terminal commands | Web form |
| Input | Type in terminal | Text box |
| Output | Text format | Formatted tabs |
| History | Manual | Automatic |
| Visual | Basic | Beautiful |
| Ease | Intermediate | Easy |
| Speed | Fast | Fast |

---

## Security Notes

### API Keys
- ✅ Keys are **never stored**
- ✅ Never sent to our servers
- ✅ Only used for API calls
- ✅ Session-based (cleared on restart)

### Best Practices
- Don't share API keys
- Don't take screenshots with keys visible
- Regenerate if accidentally exposed
- Use `.env` file locally (not committed)

---

## Customization Examples

### Change Title and Icon

```python
st.set_page_config(
    page_title="My Search Agent",
    page_icon="🔎",
)
```

### Change Layout

```python
st.set_page_config(
    layout="centered"  # or "wide"
)
```

### Add Custom CSS

```python
st.markdown("""
<style>
    body {
        background-color: #f0f0f0;
    }
</style>
""", unsafe_allow_html=True)
```

### Add Logo

```python
st.image("logo.png", width=200)
```

---

## Future Enhancements

Potential improvements:
- [ ] Result caching
- [ ] Export results (PDF, CSV)
- [ ] Chat history persistence
- [ ] Dark mode toggle
- [ ] Advanced search filters
- [ ] Result ranking
- [ ] Custom prompts
- [ ] Multi-language support

---

## File Structure

```
intellisearch3/
├── app.py                    # ← Streamlit web app
├── main.py                   # ← CLI version
├── agents/
├── config/
├── utils/
└── requirements.txt          # ← Updated with streamlit
```

---

## Browser Compatibility

✅ Works on:
- Chrome/Chromium
- Firefox
- Safari
- Edge
- Mobile browsers (limited)

---

## Support

### Getting Help

1. Check this guide
2. Check main [README.md](../README.md)
3. See [TROUBLESHOOTING.md](../TROUBLESHOOTING.md)
4. Run diagnostic: `python diagnose.py`

### Reporting Issues

Include:
- Browser and OS
- Streamlit version: `streamlit --version`
- Error message (exact text)
- Steps to reproduce

---

## Next Steps

### Use the Web Interface

```bash
streamlit run app.py
```

Then:
1. Open http://localhost:8501
2. Enter API keys
3. Search!

### Deploy Online

Push to GitHub, then deploy to Streamlit Cloud (free tier available)

### Customize Further

Edit `app.py` to match your needs

---

**Happy searching! 🔍**

For more help, see [README.md](../README.md) and [DOCS_INDEX.md](../DOCS_INDEX.md)
