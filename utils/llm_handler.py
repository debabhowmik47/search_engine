"""
LLM Handler Module
Manages different LLM providers and generates responses
"""
from typing import Optional, Dict, List
from groq import Groq
from config.api_config import APIConfig, LLMProvider

# Google Generative AI - Optional import due to Python 3.14 compatibility issues
try:
    import google.generativeai as genai
    GOOGLE_AVAILABLE = True
except (ImportError, TypeError):
    GOOGLE_AVAILABLE = False
    genai = None

class LLMHandler:
    """Handles LLM interactions with different providers"""
    
    def __init__(self, api_config: APIConfig):
        """
        Initialize LLM Handler
        
        Args:
            api_config: APIConfig instance with API keys
        """
        self.api_config = api_config
        self.groq_client = None
        self.google_model = None
        
        self._initialize_clients()
    
    def _initialize_clients(self) -> None:
        """Initialize LLM clients based on available API keys"""
        if self.api_config.groq_api_key:
            self.groq_client = Groq(api_key=self.api_config.groq_api_key)
        
        if self.api_config.google_api_key and GOOGLE_AVAILABLE:
            genai.configure(api_key=self.api_config.google_api_key)
            self.google_model = genai.GenerativeModel('gemini-pro')
        elif self.api_config.google_api_key and not GOOGLE_AVAILABLE:
            print("Warning: Google API key provided but google.generativeai is not available")
            print("         due to Python 3.14 compatibility issues.")
            print("         Groq will be used instead.")
    
    def generate_response_groq(self, prompt: str, context: str = "") -> Optional[str]:
        """
        Generate response using Groq
        
        Args:
            prompt: User prompt
            context: Additional context from search results
            
        Returns:
            Generated response or None if error
        """
        # List of Groq models to try (in order of preference)
        # These are the currently available models on Groq
        models_to_try = [
            "llama-3.3-70b-versatile",  # Latest and most capable
            "llama-3.1-8b-instant",     # Smaller but faster
        ]
        
        try:
            if not self.groq_client:
                print("\n[WARNING] Groq client not initialized")
                import sys
                sys.stdout.flush()
                return None
            
            full_prompt = f"{context}\n\nQuestion: {prompt}" if context else prompt
            
            # Try different models until one works
            last_error = None
            for model in models_to_try:
                try:
                    print(f"\n[DEBUG] Sending request to Groq API using model: {model}", flush=True)
                    message = self.groq_client.chat.completions.create(
                        messages=[
                            {
                                "role": "user",
                                "content": full_prompt
                            }
                        ],
                        model=model,
                        temperature=0.7,
                        max_tokens=1024,
                        timeout=30.0
                    )
                    
                    if not message or not message.choices:
                        print("[ERROR] Empty response from Groq API", flush=True)
                        continue
                        
                    response = message.choices[0].message.content
                    print(f"[DEBUG] Received response from Groq using model {model} ({len(response)} chars)", flush=True)
                    return response
                except Exception as e:
                    last_error = e
                    print(f"[DEBUG] Model {model} failed: {type(e).__name__}", flush=True)
                    continue
            
            # If all models failed
            if last_error:
                print(f"\n[ERROR] Groq API error: {type(last_error).__name__}: {last_error}", flush=True)
            return None
            
        except Exception as e:
            import traceback
            print(f"\n[ERROR] Unexpected Groq error: {type(e).__name__}: {e}", flush=True)
            print(f"[ERROR] Full traceback:", flush=True)
            traceback.print_exc()
            return None
    
    def generate_response_google(self, prompt: str, context: str = "") -> Optional[str]:
        """
        Generate response using Google Gemini
        
        Args:
            prompt: User prompt
            context: Additional context from search results
            
        Returns:
            Generated response or None if error
        """
        try:
            if not self.google_model:
                return None
            
            full_prompt = f"{context}\n\nQuestion: {prompt}" if context else prompt
            
            response = self.google_model.generate_content(full_prompt)
            return response.text
        except Exception as e:
            print(f"Error generating response with Google: {e}")
            return None
    
    def generate_combined_response(self, prompt: str, context: str = "") -> Dict[str, Optional[str]]:
        """
        Generate response using both LLMs
        
        Args:
            prompt: User prompt
            context: Additional context from search results
            
        Returns:
            Dictionary with responses from both providers
        """
        responses = {}
        
        if self.api_config.groq_api_key:
            responses['groq'] = self.generate_response_groq(prompt, context)
        
        if self.api_config.google_api_key:
            responses['google'] = self.generate_response_google(prompt, context)
        
        return responses
    
    def generate_response(self, prompt: str, context: str = "") -> Dict[str, Optional[str]]:
        """
        Generate response based on available providers
        
        Args:
            prompt: User prompt
            context: Additional context from search results
            
        Returns:
            Dictionary with response(s) based on active provider(s)
        """
        provider = self.api_config.active_provider
        
        if provider == LLMProvider.BOTH:
            return self.generate_combined_response(prompt, context)
        elif provider == LLMProvider.GROQ:
            return {'groq': self.generate_response_groq(prompt, context)}
        elif provider == LLMProvider.GOOGLE:
            return {'google': self.generate_response_google(prompt, context)}
        else:
            return {'error': 'No valid API provider configured'}
