"""
API Configuration Module
Handles API key management for different LLM providers
"""
from typing import Dict, Optional
from enum import Enum

class LLMProvider(Enum):
    """Supported LLM providers"""
    GROQ = "groq"
    GOOGLE = "google"
    BOTH = "both"

class APIConfig:
    """Manages API keys and provider configuration"""
    
    def __init__(self):
        self.groq_api_key: Optional[str] = None
        self.google_api_key: Optional[str] = None
        self.active_provider: Optional[LLMProvider] = None
    
    def set_api_keys(self, groq_key: Optional[str] = None, google_key: Optional[str] = None) -> None:
        """
        Set API keys for the providers
        
        Args:
            groq_key: Groq API key
            google_key: Google API key
        """
        if groq_key:
            self.groq_api_key = groq_key
        if google_key:
            self.google_api_key = google_key
        
        # Determine active provider based on available keys
        self._determine_active_provider()
    
    def _determine_active_provider(self) -> None:
        """Determine which provider(s) are active based on available keys"""
        has_groq = bool(self.groq_api_key)
        has_google = bool(self.google_api_key)
        
        if has_groq and has_google:
            self.active_provider = LLMProvider.BOTH
        elif has_groq:
            self.active_provider = LLMProvider.GROQ
        elif has_google:
            self.active_provider = LLMProvider.GOOGLE
        else:
            self.active_provider = None
    
    def validate_keys(self) -> bool:
        """
        Validate that at least one API key is provided
        
        Returns:
            True if valid, False otherwise
        """
        return bool(self.groq_api_key or self.google_api_key)
    
    def get_active_providers(self) -> list:
        """Get list of active providers"""
        providers = []
        if self.groq_api_key:
            providers.append(LLMProvider.GROQ)
        if self.google_api_key:
            providers.append(LLMProvider.GOOGLE)
        return providers
