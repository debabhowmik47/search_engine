"""
Main Entry Point for Multi-LLM Search Agent
"""
import sys
from agents.search_agent import SearchAgent

def main():
    """Main function to run the search agent"""
    agent = SearchAgent()
    
    # Setup API keys
    if not agent.setup_api_keys():
        sys.exit(1)
    
    # Interactive search loop
    print("\nEnter your queries below. Type 'quit' or 'exit' to stop.\n")
    
    while True:
        try:
            user_query = input("\n[INPUT] Enter your search query: ").strip()
            
            if user_query.lower() in ['quit', 'exit', 'q']:
                print("\nThank you for using Multi-LLM Search Agent!")
                break
            
            if not user_query:
                print("Please enter a valid query.")
                continue
            
            # Search and generate answer
            results = agent.search_and_answer(user_query)
            
            # Display results
            agent.display_results(results)
            
        except KeyboardInterrupt:
            print("\n\nInterrupted by user.")
            break
        except Exception as e:
            print(f"\nError: {e}")
            print("Please try again with a different query.\n")

if __name__ == "__main__":
    main()
