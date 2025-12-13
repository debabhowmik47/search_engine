# Usage Examples

## Basic Usage

### Running the Agent Interactively

```bash
python main.py
```

Output:
```
============================================================
Multi-LLM Search Agent Setup
============================================================

This agent can use multiple LLM providers:
1. Groq (mixtral-8x7b) - Free with API key
2. Google Gemini (gemini-pro) - Free with API key

You can provide one or both API keys.

Enter your Groq API key (or press Enter to skip): gsk_xxxxxxxxxxxxx
Enter your Google API key (or press Enter to skip): AIzaxxxxxxxxxxxxx

[OK] Setup complete. Active providers: GROQ, GOOGLE
============================================================

Enter your queries below. Type 'quit' or 'exit' to stop.

[INPUT] Enter your search query: 
```

## Example Queries and Expected Results

### Example 1: Technology Question

**Query:**
```
What is machine learning and how does it work?
```

**Process:**
1. Searches arxiv for ML papers
2. Searches Wikipedia for ML articles
3. Groq generates quick answer
4. Google provides detailed analysis

**Expected Output:**
```
Query: What is machine learning and how does it work?

Arxiv Papers Found: 3
Wikipedia Articles Found: 2

[GROQ]:
Machine learning is a subset of artificial intelligence 
that enables systems to learn and improve from experience...

[GOOGLE]:
Machine learning represents a fundamental shift in how 
we approach problem-solving. Rather than explicitly 
programming rules...
```

### Example 2: Academic Research

**Query:**
```
What are recent developments in quantum computing?
```

**Results:**
- Multiple arxiv papers on quantum computing
- Wikipedia article on quantum computing
- LLM synthesis combining academic and general knowledge

### Example 3: General Knowledge

**Query:**
```
Tell me about climate change impacts
```

**Results:**
- Scientific papers on climate change
- Wikipedia articles on climate science
- AI-generated comprehensive answer

### Example 4: Technical Explanation

**Query:**
```
How does cryptocurrency blockchain work?
```

**Results:**
- Academic papers on blockchain
- Wikipedia articles explaining blockchain
- Multiple LLM perspectives on the technology

## Advanced Usage

### Using Only Groq API

```python
from agents.search_agent import SearchAgent

agent = SearchAgent()
# Provide only Groq key
agent.api_config.set_api_keys(groq_key="your-groq-key")
agent.llm_handler = LLMHandler(agent.api_config)

# Query will use only Groq
results = agent.search_and_answer("quantum computing")
```

### Using Only Google API

```python
from agents.search_agent import SearchAgent

agent = SearchAgent()
# Provide only Google key
agent.api_config.set_api_keys(google_key="your-google-key")
agent.llm_handler = LLMHandler(agent.api_config)

# Query will use only Google
results = agent.search_and_answer("machine learning")
```

### Programmatic Usage

```python
from agents.search_agent import SearchAgent
from config.api_config import APIConfig
from utils.llm_handler import LLMHandler

# Setup
agent = SearchAgent()
config = APIConfig()
config.set_api_keys(
    groq_key="your-groq-key",
    google_key="your-google-key"
)
agent.llm_handler = LLMHandler(config)

# Search and get results
results = agent.search_and_answer("your query here")

# Access individual components
papers = results['search_results']['arxiv']
articles = results['search_results']['wikipedia']
groq_response = results['llm_responses']['groq']
google_response = results['llm_responses']['google']
```

### Custom Search Configuration

```python
from agents.search_agent import SearchAgent

agent = SearchAgent()
agent.setup_api_keys()

# Modify search behavior before querying
query = "machine learning algorithms"
search_results = agent.search_engine.combined_search(
    query,
    arxiv_max=10,      # Get more papers
    wiki_max=5         # Keep fewer wiki articles
)

# Get context
context = agent._format_search_context(search_results)

# Generate response
responses = agent.llm_handler.generate_response(query, context)

print(f"Papers found: {len(search_results['arxiv'])}")
print(f"Articles found: {len(search_results['wikipedia'])}")
print(f"Responses: {list(responses.keys())}")
```

### Batch Processing Multiple Queries

```python
from agents.search_agent import SearchAgent

agent = SearchAgent()
agent.setup_api_keys()

queries = [
    "What is artificial intelligence?",
    "How does deep learning work?",
    "What are neural networks?",
    "What is natural language processing?"
]

results = []
for query in queries:
    print(f"Processing: {query}")
    result = agent.search_and_answer(query)
    results.append({
        'query': query,
        'papers': len(result['search_results']['arxiv']),
        'articles': len(result['search_results']['wikipedia']),
        'responses': result['llm_responses']
    })

# Display summary
for r in results:
    print(f"\nQuery: {r['query']}")
    print(f"  Papers: {r['papers']}, Articles: {r['articles']}")
    print(f"  LLM responses: {list(r['responses'].keys())}")
```

## Real-World Scenarios

### Scenario 1: Student Research

**Goal:** Understand a complex topic for essay writing

```
Query: "What are the main causes of climate change?"

Benefits:
- Get academic sources from arxiv
- Get general knowledge from Wikipedia  
- Get comprehensive explanation from LLMs
- Use in essay with sources cited
```

### Scenario 2: Professional Learning

**Goal:** Stay updated on industry trends

```
Query: "Latest developments in artificial intelligence"

Benefits:
- Recent papers show cutting-edge research
- Wikipedia provides foundational knowledge
- LLMs synthesize information
- Multiple perspectives from different LLMs
```

### Scenario 3: Decision Making

**Goal:** Understand technology for adoption

```
Query: "Advantages and disadvantages of blockchain"

Benefits:
- Academic papers provide technical details
- Wikipedia explains concepts clearly
- Groq gives quick overview
- Google provides nuanced analysis
```

### Scenario 4: Content Creation

**Goal:** Write informative article

```
Query: "How does machine learning transform healthcare?"

Benefits:
- Get research papers for citations
- Get background from Wikipedia
- Get narrative from Groq
- Get detailed analysis from Google
- Combine for comprehensive article
```

## Tips and Tricks

### 1. Specific Queries Work Better

```
# Bad query
"Tell me about technology"

# Good query
"How does quantum computing use quantum entanglement?"
```

### 2. Use Both APIs for Complex Topics

```python
# Get diverse perspectives
agent.setup_api_keys()  # Provide both keys
results = agent.search_and_answer("query")

# Compare Groq vs Google approaches
groq_answer = results['llm_responses']['groq']
google_answer = results['llm_responses']['google']
```

### 3. Save Useful Results

```python
import json

results = agent.search_and_answer("query")

# Save for later reference
with open("search_results.json", "w") as f:
    json.dump({
        'query': results['query'],
        'papers': results['search_results']['arxiv'],
        'articles': results['search_results']['wikipedia'],
        'responses': results['llm_responses']
    }, f, indent=2)
```

### 4. Focus on High-Quality Sources

```python
# Prioritize arxiv for research topics
search_results = agent.search_engine.combined_search(
    query,
    arxiv_max=10,  # More academic sources
    wiki_max=2     # Basic overview only
)

# Prioritize Wikipedia for general knowledge
search_results = agent.search_engine.combined_search(
    query,
    arxiv_max=2,   # Some academic sources
    wiki_max=10    # Comprehensive overview
)
```

## Performance Examples

### Example Response Times

| Query Type | Arxiv Papers | Wiki Articles | LLM Response | Total Time |
|-----------|-------------|---------------|-------------|-----------|
| Simple | 2s | 1s | 3s | ~6s |
| Complex | 3s | 2s | 8s | ~13s |
| Academic | 5s | 1s | 5s | ~11s |

### Example Output Size

- Arxiv papers: ~500 chars per paper
- Wikipedia articles: ~300 chars per article
- LLM response: ~1000 chars typical

## Troubleshooting Examples

### Issue: No arxiv papers found

```python
# Try different search terms
queries = [
    "neural networks",
    "deep learning architectures", 
    "convolutional neural networks"
]

for q in queries:
    results = agent.search_engine.search_arxiv(q, max_results=3)
    if results:
        print(f"Found papers with: {q}")
        break
```

### Issue: Rate limit on LLM

```python
import time

# Add delay between requests
queries = ["query1", "query2", "query3"]

for query in queries:
    results = agent.search_and_answer(query)
    time.sleep(2)  # 2 second delay
```

### Issue: Inconsistent results

```python
# Run search multiple times
for i in range(3):
    results = agent.search_and_answer("query")
    print(f"Attempt {i+1}: {len(results['search_results']['wikipedia'])} articles")
```

## Success Indicators

A good usage looks like:
- ✓ Clear, specific query
- ✓ Found relevant papers and articles
- ✓ Coherent LLM response
- ✓ Multiple source citations
- ✓ Consistent information

## Next Steps

After running queries:
1. Review search results for accuracy
2. Check LLM responses for completeness
3. Verify information in original sources
4. Save useful results for future reference
5. Refine queries for better results

---

For more information, see [API_INTEGRATION.md](API_INTEGRATION.md) and [README.md](README.md)
