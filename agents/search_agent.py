"""
Multi-LLM Search Agent
Main agent that combines search and LLM capabilities
"""
from typing import Dict, Optional
from config.api_config import APIConfig
from utils.search_engine import SearchEngine
from utils.llm_handler import LLMHandler

class SearchAgent:
    """Multi-LLM search agent for arxiv and Wikipedia"""
    
    def __init__(self):
        """Initialize the search agent"""
        self.api_config = APIConfig()
        self.search_engine = SearchEngine()
        self.llm_handler = None
    
    def setup_api_keys(self) -> bool:
        """
        Setup API keys by prompting user
        
        Returns:
            True if at least one API key is provided, False otherwise
        """
        print("\n" + "="*60)
        print("Multi-LLM Search Agent Setup")
        print("="*60)
        print("\nThis agent can use multiple LLM providers:")
        print("1. Groq (mixtral-8x7b) - Free with API key")
        print("2. Google Gemini (gemini-pro) - Free with API key")
        print("\nYou can provide one or both API keys.\n")
        
        # Ask for Groq API key
        groq_key = input("Enter your Groq API key (or press Enter to skip): ").strip()
        
        # Ask for Google API key
        google_key = input("Enter your Google API key (or press Enter to skip): ").strip()
        
        # Set the API keys
        self.api_config.set_api_keys(
            groq_key if groq_key else None,
            google_key if google_key else None
        )
        
        # Validate
        if not self.api_config.validate_keys():
            print("\nError: At least one API key is required!")
            return False
        
        # Initialize LLM handler
        self.llm_handler = LLMHandler(self.api_config)
        
        # Show active providers
        providers = self.api_config.get_active_providers()
        print(f"\n[OK] Setup complete. Active providers: {', '.join([p.value.upper() for p in providers])}")
        print("="*60 + "\n")
        
        return True
    
    def _format_search_context(self, search_results: Dict) -> str:
        """
        Format search results into context string for LLM
        
        Args:
            search_results: Results from combined_search
            
        Returns:
            Formatted context string
        """
        context_parts = []
        
        # Add arxiv results
        if search_results['arxiv']:
            context_parts.append("## ARXIV PAPERS:")
            for i, paper in enumerate(search_results['arxiv'], 1):
                context_parts.append(f"\n{i}. {paper['title']}")
                context_parts.append(f"   Authors: {', '.join(paper['authors'][:3])}")
                context_parts.append(f"   Published: {paper['published']}")
                context_parts.append(f"   Summary: {paper['summary'][:300]}...")
                context_parts.append(f"   URL: {paper['url']}")
        
        # Add Wikipedia results
        if search_results['wikipedia']:
            context_parts.append("\n## WIKIPEDIA ARTICLES:")
            for i, article in enumerate(search_results['wikipedia'], 1):
                context_parts.append(f"\n{i}. {article['title']}")
                context_parts.append(f"   {article['body'][:200]}...")
                context_parts.append(f"   URL: {article['url']}")
        
        return "\n".join(context_parts)
    
    def search_and_answer(self, query: str) -> Dict:
        """
        Search for information and generate answer using LLM
        
        Args:
            query: User query
            
        Returns:
            Dictionary containing search results and LLM response(s)
        """
        if not self.llm_handler:
            return {'error': 'Agent not properly initialized. Run setup_api_keys first.'}
        
        print(f"\nSearching for: {query}")
        print("-" * 60)
        
        # Perform combined search
        search_results = self.search_engine.combined_search(query)
        
        print(f"Found {len(search_results['arxiv'])} arxiv papers and {len(search_results['wikipedia'])} Wikipedia articles.")
        
        # Format context for LLM
        context = self._format_search_context(search_results)
        
        # Check if we have context to work with
        if not context.strip():
            print("[WARNING] No search results found. Context is empty.")
        else:
            print(f"[DEBUG] Context prepared ({len(context)} chars)")
        
        # Generate response(s)
        print("\nGenerating response(s)...", flush=True)
        import sys
        sys.stdout.flush()
        
        llm_responses = self.llm_handler.generate_response(query, context)
        
        print("\n[DEBUG] LLM response generation complete", flush=True)
        
        return {
            'query': query,
            'search_results': search_results,
            'llm_responses': llm_responses,
            'context': context
        }
    
    def display_results(self, results: Dict) -> None:
        """
        Display search and LLM results in a formatted way
        
        Args:
            results: Results from search_and_answer
        """
        if 'error' in results:
            print(f"\nError: {results['error']}")
            return
        
        print("\n" + "="*60)
        print("SEARCH RESULTS & AI ANALYSIS")
        print("="*60)
        
        print(f"\nQuery: {results['query']}\n")
        
        # Display search results summary
        print(f"Arxiv Papers Found: {len(results['search_results']['arxiv'])}")
        print(f"Wikipedia Articles Found: {len(results['search_results']['wikipedia'])}\n")
        
        # Display LLM responses
        print("-" * 60)
        print("AI GENERATED ANSWERS:")
        print("-" * 60)
        
        has_response = False
        for provider, response in results['llm_responses'].items():
            if response:
                print(f"\n[{provider.upper()}]:")
                print(response)
                print()
                has_response = True
            else:
                print(f"\n[{provider.upper()}]: Waiting for response...")
        
        if not has_response:
            print("\nNote: No AI responses were generated.")
            print("This may be due to invalid API keys or API service issues.")
