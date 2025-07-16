"""
Utility functions for MCP server.
"""

import json
import logging
import os
from typing import Any, Dict, Optional

import httpx

def setup_logging() -> logging.Logger:
    """Setup logging configuration."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    return logging.getLogger(__name__)

def load_config() -> Dict[str, Any]:
    """Load server configuration."""
    try:
        with open("config.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def get_api_headers() -> Dict[str, str]:
    """Get headers for API requests."""
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "MCP-Server/1.0"
    }
    
    api_key = os.getenv("API_KEY")
    if api_key:
        headers["X-KM-AccessKey"] = f"Bearer {api_key}"
    
    return headers

def handle_api_error(response: httpx.Response) -> Dict[str, Any]:
    """Handle API error responses."""
    try:
        error_data = response.json()
    except:
        error_data = {"message": response.text}
    
    return {
        "error": True,
        "status_code": response.status_code,
        "message": error_data.get("message", "API request failed"),
        "details": error_data
    }

def format_response(response: httpx.Response) -> Dict[str, Any]:
    """Format successful API response."""
    try:
        data = response.json()
    except:
        data = {"content": response.text}
    
    return {
        "success": True,
        "status_code": response.status_code,
        "data": data
    }