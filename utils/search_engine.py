"""
Search Engine Module
Uses DuckDuckGo to search arxiv and Wikipedia
"""
from ddgs import DDGS
from typing import List, Dict, Optional
import arxiv as arxiv_lib

class SearchEngine:
    """Handles searching on arxiv and Wikipedia"""
    
    def __init__(self):
        self.ddgs = DDGS()
    
    def search_arxiv(self, query: str, max_results: int = 5) -> List[Dict]:
        """
        Search arxiv papers using arxiv API
        
        Args:
            query: Search query
            max_results: Maximum number of results
            
        Returns:
            List of paper information
        """
        try:
            papers = []
            search = arxiv_lib.Search(
                query=query,
                max_results=max_results,
                sort_by=arxiv_lib.SortCriterion.Relevance
            )
            
            for i, paper in enumerate(search.results()):
                if i >= max_results:
                    break
                papers.append({
                    'title': paper.title,
                    'authors': [author.name for author in paper.authors][:3],  # First 3 authors
                    'published': paper.published.strftime('%Y-%m-%d'),
                    'summary': paper.summary[:300],  # Truncate summary
                    'url': paper.entry_id,
                    'source': 'arxiv'
                })
            
            return papers
        except Exception as e:
            # arxiv API may have issues, but we'll continue with other sources
            return []
    
    def search_wikipedia(self, query: str, max_results: int = 5) -> List[Dict]:
        """
        Search Wikipedia using DuckDuckGo
        
        Args:
            query: Search query
            max_results: Maximum number of results
            
        Returns:
            List of Wikipedia article information
        """
        try:
            results = []
            # Using DuckDuckGo to search Wikipedia
            search_query = f"site:wikipedia.org {query}"
            ddgs_results = self.ddgs.text(search_query, max_results=max_results)
            
            for result in ddgs_results:
                results.append({
                    'title': result.get('title', ''),
                    'body': result.get('body', ''),
                    'url': result.get('href', ''),
                    'source': 'wikipedia'
                })
            
            return results
        except Exception as e:
            print(f"Error searching Wikipedia: {e}")
            return []
    
    def combined_search(self, query: str, arxiv_max: int = 3, wiki_max: int = 3) -> Dict:
        """
        Perform combined search on both arxiv and Wikipedia
        
        Args:
            query: Search query
            arxiv_max: Maximum arxiv results
            wiki_max: Maximum Wikipedia results
            
        Returns:
            Dictionary containing results from both sources
        """
        return {
            'arxiv': self.search_arxiv(query, arxiv_max),
            'wikipedia': self.search_wikipedia(query, wiki_max),
            'query': query
        }
