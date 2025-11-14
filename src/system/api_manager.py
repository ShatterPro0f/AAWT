"""
API Manager for AAWT
Handles integration with multiple AI providers: OpenAI, Anthropic, Google, HuggingFace, and Ollama.
Includes rate limiting, caching, cost tracking, and async processing.
"""

import hashlib
import json
import logging
import time
import requests
from typing import Dict, Any, Optional, List
from datetime import datetime, timedelta
from threading import Lock
from queue import Queue
import threading

logger = logging.getLogger(__name__)


class APIManager:
    """Manages all external API interactions."""
    
    def __init__(self, settings_manager, database_manager):
        """
        Initialize API manager.
        
        Args:
            settings_manager: Settings manager instance
            database_manager: Database manager instance
        """
        self.settings = settings_manager
        self.database = database_manager
        
        # Rate limiting
        self._rate_limits = {}
        self._rate_lock = Lock()
        
        # Request queue for async processing
        self._request_queue = Queue()
        self._worker_thread = None
        self._running = False
        
        # API pricing (per 1K tokens)
        self._pricing = {
            'openai': {
                'gpt-3.5-turbo': {'input': 0.0015, 'output': 0.002},
                'gpt-4': {'input': 0.03, 'output': 0.06},
                'gpt-4-turbo': {'input': 0.01, 'output': 0.03}
            },
            'anthropic': {
                'claude-3-opus': {'input': 0.015, 'output': 0.075},
                'claude-3-sonnet': {'input': 0.003, 'output': 0.015},
                'claude-3-haiku': {'input': 0.00025, 'output': 0.00125}
            },
            'google': {
                'gemini-pro': {'input': 0.00025, 'output': 0.0005}
            },
            'ollama': {
                'default': {'input': 0, 'output': 0}  # Local, free
            }
        }
        
        logger.info("API Manager initialized")
    
    def _get_api_key(self, provider: str) -> Optional[str]:
        """Get API key for provider."""
        key_map = {
            'openai': 'api.openai_key',
            'anthropic': 'api.anthropic_key',
            'google': 'api.google_key',
            'huggingface': 'api.huggingface_key'
        }
        
        if provider in key_map:
            return self.settings.get(key_map[provider])
        return None
    
    def _get_ollama_url(self) -> str:
        """Get Ollama server URL."""
        return self.settings.get('api.ollama_url', 'http://localhost:11434')
    
    def _check_rate_limit(self, provider: str) -> bool:
        """
        Check if rate limit allows a new request.
        
        Args:
            provider: API provider name
        
        Returns:
            True if request is allowed
        """
        with self._rate_lock:
            now = time.time()
            window = self.settings.get('api.rate_limit_window', 3600)
            limit = self.settings.get('api.rate_limit_requests', 60)
            
            if provider not in self._rate_limits:
                self._rate_limits[provider] = []
            
            # Remove old requests outside window
            self._rate_limits[provider] = [
                t for t in self._rate_limits[provider] 
                if now - t < window
            ]
            
            # Check limit
            if len(self._rate_limits[provider]) >= limit:
                logger.warning(f"Rate limit exceeded for {provider}")
                return False
            
            # Add current request
            self._rate_limits[provider].append(now)
            return True
    
    def _generate_cache_key(self, provider: str, model: str, prompt: str, **kwargs) -> str:
        """Generate cache key for request."""
        key_data = f"{provider}:{model}:{prompt}:{json.dumps(kwargs, sort_keys=True)}"
        return hashlib.sha256(key_data.encode()).hexdigest()
    
    def _get_cached_response(self, cache_key: str) -> Optional[Dict]:
        """Get cached API response."""
        if not self.settings.get('api.enable_api_caching', True):
            return None
        
        cached = self.database.get_cached_content('api_response', cache_key)
        if cached:
            logger.debug(f"Cache hit for key: {cache_key[:16]}...")
            return cached
        
        return None
    
    def _cache_response(self, cache_key: str, response: Dict):
        """Cache API response."""
        if not self.settings.get('api.enable_api_caching', True):
            return
        
        ttl_days = self.settings.get('api.cache_expiration_days', 7)
        self.database.cache_content('api_response', cache_key, response, ttl_days=ttl_days)
    
    def _calculate_cost(self, provider: str, model: str, input_tokens: int, output_tokens: int) -> float:
        """Calculate cost for API call."""
        if provider in self._pricing and model in self._pricing[provider]:
            pricing = self._pricing[provider][model]
            cost = (input_tokens / 1000 * pricing['input']) + (output_tokens / 1000 * pricing['output'])
            return cost
        return 0.0
    
    def call_openai(self, prompt: str, model: str = 'gpt-3.5-turbo', 
                   max_tokens: int = 500, temperature: float = 0.7,
                   system_prompt: Optional[str] = None, **kwargs) -> Dict[str, Any]:
        """
        Call OpenAI API.
        
        Args:
            prompt: User prompt
            model: Model name
            max_tokens: Maximum tokens to generate
            temperature: Sampling temperature
            system_prompt: Optional system prompt
        
        Returns:
            Response dictionary
        """
        start_time = time.time()
        
        # Check rate limit
        if not self._check_rate_limit('openai'):
            return {'success': False, 'error': 'Rate limit exceeded'}
        
        # Check cache
        cache_key = self._generate_cache_key('openai', model, prompt, temperature=temperature)
        cached = self._get_cached_response(cache_key)
        if cached:
            return cached
        
        # Get API key
        api_key = self._get_api_key('openai')
        if not api_key:
            return {'success': False, 'error': 'OpenAI API key not configured'}
        
        try:
            # Prepare messages
            messages = []
            if system_prompt:
                messages.append({'role': 'system', 'content': system_prompt})
            messages.append({'role': 'user', 'content': prompt})
            
            # Make request
            headers = {
                'Authorization': f'Bearer {api_key}',
                'Content-Type': 'application/json'
            }
            
            data = {
                'model': model,
                'messages': messages,
                'max_tokens': max_tokens,
                'temperature': temperature
            }
            
            timeout = self.settings.get('api.request_timeout', 30)
            response = requests.post(
                'https://api.openai.com/v1/chat/completions',
                headers=headers,
                json=data,
                timeout=timeout
            )
            
            response_time = time.time() - start_time
            
            if response.status_code == 200:
                result = response.json()
                
                # Extract response
                text = result['choices'][0]['message']['content']
                usage = result.get('usage', {})
                input_tokens = usage.get('prompt_tokens', 0)
                output_tokens = usage.get('completion_tokens', 0)
                cost = self._calculate_cost('openai', model, input_tokens, output_tokens)
                
                response_data = {
                    'success': True,
                    'text': text,
                    'input_tokens': input_tokens,
                    'output_tokens': output_tokens,
                    'cost': cost,
                    'model': model
                }
                
                # Cache response
                self._cache_response(cache_key, response_data)
                
                # Log usage
                self.database.log_api_usage(
                    api_type='openai',
                    endpoint=model,
                    response_time=response_time,
                    success=True,
                    status_code=200,
                    tokens_used=input_tokens + output_tokens,
                    cost=cost,
                    request_hash=cache_key
                )
                
                return response_data
            else:
                error_msg = f"OpenAI API error: {response.status_code}"
                logger.error(error_msg)
                
                self.database.log_api_usage(
                    api_type='openai',
                    endpoint=model,
                    response_time=response_time,
                    success=False,
                    status_code=response.status_code,
                    error_message=error_msg
                )
                
                return {'success': False, 'error': error_msg}
                
        except Exception as e:
            logger.error(f"OpenAI API call failed: {e}")
            return {'success': False, 'error': str(e)}
    
    def call_anthropic(self, prompt: str, model: str = 'claude-3-sonnet-20240229',
                      max_tokens: int = 500, temperature: float = 0.7,
                      system_prompt: Optional[str] = None, **kwargs) -> Dict[str, Any]:
        """Call Anthropic (Claude) API."""
        start_time = time.time()
        
        if not self._check_rate_limit('anthropic'):
            return {'success': False, 'error': 'Rate limit exceeded'}
        
        cache_key = self._generate_cache_key('anthropic', model, prompt, temperature=temperature)
        cached = self._get_cached_response(cache_key)
        if cached:
            return cached
        
        api_key = self._get_api_key('anthropic')
        if not api_key:
            return {'success': False, 'error': 'Anthropic API key not configured'}
        
        try:
            headers = {
                'x-api-key': api_key,
                'anthropic-version': '2023-06-01',
                'Content-Type': 'application/json'
            }
            
            data = {
                'model': model,
                'max_tokens': max_tokens,
                'temperature': temperature,
                'messages': [{'role': 'user', 'content': prompt}]
            }
            
            if system_prompt:
                data['system'] = system_prompt
            
            timeout = self.settings.get('api.request_timeout', 30)
            response = requests.post(
                'https://api.anthropic.com/v1/messages',
                headers=headers,
                json=data,
                timeout=timeout
            )
            
            response_time = time.time() - start_time
            
            if response.status_code == 200:
                result = response.json()
                text = result['content'][0]['text']
                usage = result.get('usage', {})
                input_tokens = usage.get('input_tokens', 0)
                output_tokens = usage.get('output_tokens', 0)
                cost = self._calculate_cost('anthropic', model, input_tokens, output_tokens)
                
                response_data = {
                    'success': True,
                    'text': text,
                    'input_tokens': input_tokens,
                    'output_tokens': output_tokens,
                    'cost': cost,
                    'model': model
                }
                
                self._cache_response(cache_key, response_data)
                
                self.database.log_api_usage(
                    api_type='anthropic',
                    endpoint=model,
                    response_time=response_time,
                    success=True,
                    status_code=200,
                    tokens_used=input_tokens + output_tokens,
                    cost=cost,
                    request_hash=cache_key
                )
                
                return response_data
            else:
                error_msg = f"Anthropic API error: {response.status_code}"
                logger.error(error_msg)
                
                self.database.log_api_usage(
                    api_type='anthropic',
                    endpoint=model,
                    response_time=response_time,
                    success=False,
                    status_code=response.status_code,
                    error_message=error_msg
                )
                
                return {'success': False, 'error': error_msg}
                
        except Exception as e:
            logger.error(f"Anthropic API call failed: {e}")
            return {'success': False, 'error': str(e)}
    
    def call_ollama(self, prompt: str, model: str = 'llama2',
                   system_prompt: Optional[str] = None, **kwargs) -> Dict[str, Any]:
        """
        Call Ollama (local LLM) API.
        
        Args:
            prompt: User prompt
            model: Model name (e.g., 'llama2', 'mistral', 'codellama')
            system_prompt: Optional system prompt
        
        Returns:
            Response dictionary
        """
        start_time = time.time()
        
        cache_key = self._generate_cache_key('ollama', model, prompt)
        cached = self._get_cached_response(cache_key)
        if cached:
            return cached
        
        try:
            ollama_url = self._get_ollama_url()
            
            # Prepare request
            data = {
                'model': model,
                'prompt': prompt,
                'stream': False
            }
            
            if system_prompt:
                data['system'] = system_prompt
            
            timeout = self.settings.get('api.request_timeout', 30)
            response = requests.post(
                f'{ollama_url}/api/generate',
                json=data,
                timeout=timeout
            )
            
            response_time = time.time() - start_time
            
            if response.status_code == 200:
                result = response.json()
                text = result.get('response', '')
                
                response_data = {
                    'success': True,
                    'text': text,
                    'input_tokens': 0,  # Ollama doesn't provide token counts
                    'output_tokens': 0,
                    'cost': 0.0,  # Local, free
                    'model': model
                }
                
                self._cache_response(cache_key, response_data)
                
                self.database.log_api_usage(
                    api_type='ollama',
                    endpoint=model,
                    response_time=response_time,
                    success=True,
                    status_code=200,
                    tokens_used=0,
                    cost=0.0,
                    request_hash=cache_key
                )
                
                return response_data
            else:
                error_msg = f"Ollama API error: {response.status_code}"
                logger.error(error_msg)
                
                self.database.log_api_usage(
                    api_type='ollama',
                    endpoint=model,
                    response_time=response_time,
                    success=False,
                    status_code=response.status_code,
                    error_message=error_msg
                )
                
                return {'success': False, 'error': error_msg}
                
        except requests.exceptions.ConnectionError:
            error_msg = "Cannot connect to Ollama. Is it running?"
            logger.error(error_msg)
            return {'success': False, 'error': error_msg}
        except Exception as e:
            logger.error(f"Ollama API call failed: {e}")
            return {'success': False, 'error': str(e)}
    
    def call_google(self, prompt: str, model: str = 'gemini-pro', **kwargs) -> Dict[str, Any]:
        """Call Google Generative AI API."""
        start_time = time.time()
        
        if not self._check_rate_limit('google'):
            return {'success': False, 'error': 'Rate limit exceeded'}
        
        cache_key = self._generate_cache_key('google', model, prompt)
        cached = self._get_cached_response(cache_key)
        if cached:
            return cached
        
        api_key = self._get_api_key('google')
        if not api_key:
            return {'success': False, 'error': 'Google API key not configured'}
        
        try:
            url = f'https://generativelanguage.googleapis.com/v1/models/{model}:generateContent?key={api_key}'
            
            data = {
                'contents': [{
                    'parts': [{'text': prompt}]
                }]
            }
            
            timeout = self.settings.get('api.request_timeout', 30)
            response = requests.post(url, json=data, timeout=timeout)
            
            response_time = time.time() - start_time
            
            if response.status_code == 200:
                result = response.json()
                text = result['candidates'][0]['content']['parts'][0]['text']
                
                response_data = {
                    'success': True,
                    'text': text,
                    'input_tokens': 0,
                    'output_tokens': 0,
                    'cost': 0.0,
                    'model': model
                }
                
                self._cache_response(cache_key, response_data)
                
                self.database.log_api_usage(
                    api_type='google',
                    endpoint=model,
                    response_time=response_time,
                    success=True,
                    status_code=200,
                    request_hash=cache_key
                )
                
                return response_data
            else:
                error_msg = f"Google API error: {response.status_code}"
                logger.error(error_msg)
                
                self.database.log_api_usage(
                    api_type='google',
                    endpoint=model,
                    response_time=response_time,
                    success=False,
                    status_code=response.status_code,
                    error_message=error_msg
                )
                
                return {'success': False, 'error': error_msg}
                
        except Exception as e:
            logger.error(f"Google API call failed: {e}")
            return {'success': False, 'error': str(e)}
    
    def call_ai(self, prompt: str, provider: Optional[str] = None, model: Optional[str] = None,
               system_prompt: Optional[str] = None, **kwargs) -> Dict[str, Any]:
        """
        Universal AI call method that routes to the appropriate provider.
        
        Args:
            prompt: User prompt
            provider: Provider name (openai, anthropic, google, ollama) or None for default
            model: Model name or None for default
            system_prompt: Optional system prompt
        
        Returns:
            Response dictionary
        """
        # Use default provider if not specified
        if not provider:
            provider = self.settings.get('api.default_provider', 'openai')
        
        # Use default model if not specified
        if not model:
            model = self.settings.get('api.default_model', 'gpt-3.5-turbo')
        
        # Route to appropriate provider
        if provider == 'openai':
            return self.call_openai(prompt, model, system_prompt=system_prompt, **kwargs)
        elif provider == 'anthropic':
            return self.call_anthropic(prompt, model, system_prompt=system_prompt, **kwargs)
        elif provider == 'google':
            return self.call_google(prompt, model, **kwargs)
        elif provider == 'ollama':
            return self.call_ollama(prompt, model, system_prompt=system_prompt, **kwargs)
        else:
            return {'success': False, 'error': f'Unknown provider: {provider}'}
    
    def test_connection(self, provider: str) -> Dict[str, Any]:
        """
        Test connection to an API provider.
        
        Args:
            provider: Provider name
        
        Returns:
            Test result dictionary
        """
        test_prompt = "Say 'Hello' if you can read this."
        
        try:
            result = self.call_ai(test_prompt, provider=provider)
            if result.get('success'):
                return {
                    'success': True,
                    'message': f'{provider} connection successful',
                    'response': result.get('text', '')[:100]
                }
            else:
                return {
                    'success': False,
                    'message': f'{provider} connection failed',
                    'error': result.get('error', 'Unknown error')
                }
        except Exception as e:
            return {
                'success': False,
                'message': f'{provider} connection failed',
                'error': str(e)
            }
    
    def get_usage_stats(self, days: int = 30) -> Dict:
        """Get API usage statistics."""
        return self.database.get_api_usage_stats(days)
    
    def get_available_providers(self) -> List[str]:
        """Get list of available providers."""
        providers = []
        
        if self._get_api_key('openai'):
            providers.append('openai')
        if self._get_api_key('anthropic'):
            providers.append('anthropic')
        if self._get_api_key('google'):
            providers.append('google')
        
        # Always include Ollama as an option
        providers.append('ollama')
        
        return providers
