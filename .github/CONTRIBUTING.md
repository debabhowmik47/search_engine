# Contributing to Multi-LLM Search Agent

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

## Code of Conduct

- Be respectful and constructive
- Welcome diversity of thought
- Focus on ideas, not individuals
- Report harmful behavior

## Getting Started

### 1. Fork the Repository
- Click "Fork" button on GitHub
- Clone your fork locally

### 2. Create Feature Branch
```bash
git checkout -b feature/your-feature-name
```

### 3. Make Changes
- Write clear, focused commits
- Follow Python PEP 8 style guide
- Add type hints where possible

### 4. Test Your Changes
```bash
# Test with sample queries
python main.py

# Run diagnostics
python diagnose.py
```

### 5. Commit with Clear Messages
```bash
git commit -m "Add feature: brief description"
```

### 6. Push and Create Pull Request
- Push to your fork
- Open pull request against `main`
- Describe changes clearly

---

## Areas for Contribution

### High Priority
- [ ] Web interface (Flask/FastAPI)
- [ ] Additional search sources
- [ ] Caching mechanism
- [ ] Better error messages

### Medium Priority
- [ ] Docker support
- [ ] API documentation
- [ ] Performance optimization
- [ ] More unit tests

### Low Priority
- [ ] Additional LLM providers
- [ ] Export formats (PDF, HTML)
- [ ] Chat history
- [ ] Custom themes

---

## Code Style Guide

### Python Code
Follow PEP 8:
```python
# Good
def get_search_results(query: str, limit: int = 5) -> dict:
    """Get search results for a query."""
    pass

# Bad
def getSearchResults(query,limit=5):
    pass
```

### Function Documentation
```python
def search_and_answer(self, query: str) -> dict:
    """
    Search and generate AI answer.
    
    Args:
        query: User search query
        
    Returns:
        Dictionary with search results and AI response
        
    Raises:
        ValueError: If query is empty
        APIError: If API call fails
    """
    pass
```

### Variable Names
- Use descriptive names: `search_results` not `sr`
- Use `_prefix` for private: `_internal_method()`
- Use UPPER_CASE for constants: `MAX_RETRIES = 3`

---

## Testing

### Running Tests
```bash
# Test the agent
python test_agent.py

# Test diagnostics
python diagnose.py

# List available models
python list_models.py
```

### Adding Tests
1. Create test files in `tests/` directory (when added)
2. Name files: `test_*.py`
3. Use assertions for validation

Example:
```python
def test_search_arxiv():
    engine = SearchEngine()
    results = engine.search_arxiv("machine learning")
    assert isinstance(results, list)
    assert len(results) >= 0
```

---

## Documentation

### Update Documentation When:
- Adding new features
- Changing API
- Adding dependencies
- Fixing major bugs

### Files to Update
- [README.md](../README.md) - Major features
- [USAGE_EXAMPLES.md](../USAGE_EXAMPLES.md) - Usage changes
- [API_INTEGRATION.md](../API_INTEGRATION.md) - API changes
- [TROUBLESHOOTING.md](../TROUBLESHOOTING.md) - Common issues

### Documentation Format
```markdown
# Section Title

Brief description of feature.

## Sub-section

More details here.

### Code Example

```python
# Code here
```
```

---

## Pull Request Process

### Before Submitting
- [ ] Code follows PEP 8 style
- [ ] All functions have docstrings
- [ ] Changes tested locally
- [ ] Documentation updated
- [ ] No API keys in code
- [ ] .gitignore properly configured

### PR Description Template
```markdown
## Description
Brief description of changes.

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement

## Testing Done
- Tested with queries: ...
- Tested with APIs: ...
- Tested on: Windows/Linux/Mac

## Related Issues
Fixes #(issue number) if applicable

## Screenshots
If applicable, add screenshots
```

### Review Process
- Maintainers review code
- Address feedback constructively
- Rebase if needed: `git rebase main`
- Once approved, we merge!

---

## Commit Message Format

### Good Commit Messages
```
Add feature: Brief description (under 50 chars)

More detailed explanation here if needed.
- Point 1
- Point 2

Fixes #123
```

### Bad Commit Messages
```
update
fix stuff
changes
```

### Commit Types
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation only
- `refactor:` Code reorganization
- `perf:` Performance improvement
- `test:` Adding tests

Example:
```
git commit -m "feat: add support for multiple search engines"
git commit -m "fix: handle API timeouts gracefully"
git commit -m "docs: update README with examples"
```

---

## Development Setup

### 1. Clone Repository
```bash
git clone https://github.com/your-username/intellisearch3.git
cd intellisearch3
```

### 2. Create Virtual Environment
```bash
python -m venv .venv

# Windows
.\.venv\Scripts\Activate.ps1

# Linux/Mac
source .venv/bin/activate
```

### 3. Install Development Dependencies
```bash
pip install -r requirements.txt

# Optional: development tools
pip install black pylint pytest
```

### 4. Make Changes
- Create feature branch
- Write code
- Test thoroughly

### 5. Format Code (Optional)
```bash
# Format with black
black *.py agents/ config/ utils/

# Check with pylint
pylint agents/ config/ utils/
```

---

## Project Structure

```
intellisearch3/
├── agents/              # Main agent logic
│   ├── __init__.py
│   └── search_agent.py  # SearchAgent class
├── config/              # Configuration
│   ├── __init__.py
│   ├── api_config.py    # API management
│   └── settings.py      # Settings
├── utils/               # Utilities
│   ├── __init__.py
│   ├── search_engine.py # Search logic
│   └── llm_handler.py   # LLM integration
├── main.py              # Entry point
├── requirements.txt     # Dependencies
└── [documentation]
```

### Key Classes

**SearchAgent** (`agents/search_agent.py`)
- Main orchestrator
- Combines search + LLM
- Manages API keys

**SearchEngine** (`utils/search_engine.py`)
- Arxiv search
- Wikipedia search (via DuckDuckGo)
- Combined search

**LLMHandler** (`utils/llm_handler.py`)
- Groq API integration
- Google Gemini integration
- Model fallback logic

**APIConfig** (`config/api_config.py`)
- Key management
- Provider detection

---

## Known Issues

See [TROUBLESHOOTING.md](../TROUBLESHOOTING.md) for known issues.

If you find a new issue:
1. Check existing issues first
2. Provide clear reproduction steps
3. Include Python version and OS
4. Share error messages

---

## Performance Considerations

When contributing:

### Optimization Tips
- Cache results when possible
- Minimize API calls
- Use generators for large results
- Profile code: `python -m cProfile main.py`

### Testing Performance
```bash
# Time a single query
time python main.py
# [type query]
# [type exit]

# Check memory usage
python -m memory_profiler main.py
```

---

## Security

### Security Considerations
- Never commit API keys
- Validate user input
- Use HTTPS for external calls
- Report security issues privately

### Reporting Security Issues
- Don't create public issues for security
- Email maintainer directly
- Provide detailed description
- Include reproduction steps

---

## Documentation Standards

### README Sections
- Overview and features
- Installation instructions
- Quick start guide
- Usage examples
- Project structure
- Troubleshooting
- Contributing guidelines

### Example Documentation
```markdown
## Feature Name

Brief description of what it does.

### Usage

```python
# Code example
```

### Parameters

| Name | Type | Description |
|------|------|-------------|
| param1 | str | Description |

### Returns

Description of return value.

### Example

```
Input: ...
Output: ...
```
```

---

## Licensing

By contributing, you agree that your contributions will be licensed under the MIT License.

---

## Getting Help

### Questions?
- Check documentation in [DOCS_INDEX.md](../DOCS_INDEX.md)
- Search existing issues
- Create new discussion

### Issues?
- Check [TROUBLESHOOTING.md](../TROUBLESHOOTING.md)
- Search existing issues
- Open new issue with details

### Want to Discuss?
- Open an issue for discussion
- Fork and experiment
- Share feedback

---

## Community

We're building this together! Thank you for:
- Reporting bugs
- Suggesting features
- Fixing issues
- Improving documentation
- Sharing the project

---

## Recognition

Contributors will be recognized in:
- This file (Contributors section - to be added)
- README.md (contributors section)
- Release notes

---

## Questions?

Feel free to:
1. Check existing documentation
2. Search GitHub issues
3. Open a discussion
4. Open an issue

---

**Thank you for contributing! We're excited to have you! 🎉**

Last Updated: December 2025
