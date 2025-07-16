"""
Resource implementations for MCP server.
"""

import json
import os
from typing import Any, Dict, List, Optional

import httpx
from utils import get_api_headers, handle_api_error, format_response, load_config

# Load configuration
config = load_config()
base_url = config.get("api", {}).get("base_url", "https://constructor.app/api/platform-kmapi")

# HTTP client for API calls
client = httpx.AsyncClient(timeout=30.0)


async def resource_get_alive_resource(uri: str) -> Dict[str, Any]:
    """
    Access to respond if authorized, do not respond on any error
    
    Method: GET
    Path: /alive
    URI: api:///alive
    """
    try:
        # Build URL
        url = f"/alive"
        headers = get_api_headers()
        
        # Make request
        
        response = await client.get(url, headers=headers)
        
        
        # Handle response
        if response.status_code >= 400:
            return handle_api_error(response)
        
        return format_response(response)
        
    except Exception as e:
        return {"error": str(e), "resource": "get_alive_resource"}


async def resource_get_v1_knowledge_models_resource(uri: str) -> Dict[str, Any]:
    """
    Access to list knowledge models
    
    Method: GET
    Path: /v1/knowledge-models
    URI: api:///v1/knowledge-models
    """
    try:
        # Build URL
        url = f"{base_url}/v1/knowledge-models"
        headers = get_api_headers()
        
        # Make request
        response = await client.get(url, headers=headers)
        
        # Handle response
        if response.status_code >= 400:
            return handle_api_error(response)
        
        return format_response(response)
        
    except Exception as e:
        return {"error": str(e), "resource": "get_v1_knowledge_models_resource"}


async def resource_get_v1_knowledge_models_by_id_resource(uri: str) -> Dict[str, Any]:
    """
    Access to get knowledge model
    
    Method: GET
    Path: /v1/knowledge-models/{knowledge_model_id}
    URI: api:///v1/knowledge-models/{knowledge_model_id}
    """
    try:
        # Extract knowledge_model_id from URI
        knowledge_model_id = uri.split('/')[-1]
        
        # Build URL
        url = f"{base_url}/v1/knowledge-models/{knowledge_model_id}"
        headers = get_api_headers()
        
        # Make request
        response = await client.get(url, headers=headers)
        
        # Handle response
        if response.status_code >= 400:
            return handle_api_error(response)
        
        return format_response(response)
        
    except Exception as e:
        return {"error": str(e), "resource": "get_v1_knowledge_models_by_id_resource"}


async def resource_get_v1_knowledge_models_settings_resource(uri: str) -> Dict[str, Any]:
    """
    Access to get knowledge model settings
    
    Method: GET
    Path: /v1/knowledge-models/{knowledge_model_id}/settings
    URI: api:///v1/knowledge-models/{knowledge_model_id}/settings
    """
    try:
        # Build URL
        url = f"/v1/knowledge-models/{knowledge_model_id}/settings"
        headers = get_api_headers()
        
        # Make request
        
        response = await client.get(url, headers=headers)
        
        
        # Handle response
        if response.status_code >= 400:
            return handle_api_error(response)
        
        return format_response(response)
        
    except Exception as e:
        return {"error": str(e), "resource": "get_v1_knowledge_models_settings_resource"}


async def resource_get_v1_knowledge_models_chat_sessions_resource(uri: str) -> Dict[str, Any]:
    """
    Access to get all chat sessions for given knowledge model
    
    Method: GET
    Path: /v1/knowledge-models/{knowledge_model_id}/chat-sessions
    URI: api:///v1/knowledge-models/{knowledge_model_id}/chat-sessions
    """
    try:
        # Build URL
        url = f"/v1/knowledge-models/{knowledge_model_id}/chat-sessions"
        headers = get_api_headers()
        
        # Make request
        
        response = await client.get(url, headers=headers)
        
        
        # Handle response
        if response.status_code >= 400:
            return handle_api_error(response)
        
        return format_response(response)
        
    except Exception as e:
        return {"error": str(e), "resource": "get_v1_knowledge_models_chat_sessions_resource"}


async def resource_get_v1_knowledge_models_chat_sessions_by_id_resource(uri: str) -> Dict[str, Any]:
    """
    Access to get chat session
    
    Method: GET
    Path: /v1/knowledge-models/{knowledge_model_id}/chat-sessions/{chat_session_id}
    URI: api:///v1/knowledge-models/{knowledge_model_id}/chat-sessions/{chat_session_id}
    """
    try:
        # Extract IDs from URI
        parts = uri.split('/')
        knowledge_model_id = parts[3]
        chat_session_id = parts[5]
        
        # Build URL
        url = f"{base_url}/v1/knowledge-models/{knowledge_model_id}/chat-sessions/{chat_session_id}"
        headers = get_api_headers()
        
        # Make request
        response = await client.get(url, headers=headers)
        
        # Handle response
        if response.status_code >= 400:
            return handle_api_error(response)
        
        return format_response(response)
        
    except Exception as e:
        return {"error": str(e), "resource": "get_v1_knowledge_models_chat_sessions_by_id_resource"}


async def resource_get_v1_knowledge_models_files_resource(uri: str) -> Dict[str, Any]:
    """
    Access to download a file from a knowledge model
    
    Method: GET
    Path: /v1/knowledge-models/{knowledge_model_id}/files/{file_id}
    URI: api:///v1/knowledge-models/{knowledge_model_id}/files/{file_id}
    """
    try:
        # Build URL
        url = f"/v1/knowledge-models/{knowledge_model_id}/files/{file_id}"
        headers = get_api_headers()
        
        # Make request
        
        response = await client.get(url, headers=headers)
        
        
        # Handle response
        if response.status_code >= 400:
            return handle_api_error(response)
        
        return format_response(response)
        
    except Exception as e:
        return {"error": str(e), "resource": "get_v1_knowledge_models_files_resource"}


async def resource_get_v1_knowledge_models_files_metadata_resource(uri: str) -> Dict[str, Any]:
    """
    Access to returns metadata of the file
    
    Method: GET
    Path: /v1/knowledge-models/{knowledge_model_id}/files/{file_id}/metadata
    URI: api:///v1/knowledge-models/{knowledge_model_id}/files/{file_id}/metadata
    """
    try:
        # Build URL
        url = f"/v1/knowledge-models/{knowledge_model_id}/files/{file_id}/metadata"
        headers = get_api_headers()
        
        # Make request
        
        response = await client.get(url, headers=headers)
        
        
        # Handle response
        if response.status_code >= 400:
            return handle_api_error(response)
        
        return format_response(response)
        
    except Exception as e:
        return {"error": str(e), "resource": "get_v1_knowledge_models_files_metadata_resource"}


async def resource_get_v1_knowledge_models_internal_documents_resource(uri: str) -> Dict[str, Any]:
    """
    Access to get internal document
    
    Method: GET
    Path: /v1/knowledge-models/{knowledge_model_id}/internal-documents/{document_id}
    URI: api:///v1/knowledge-models/{knowledge_model_id}/internal-documents/{document_id}
    """
    try:
        # Build URL
        url = f"/v1/knowledge-models/{knowledge_model_id}/internal-documents/{document_id}"
        headers = get_api_headers()
        
        # Make request
        
        response = await client.get(url, headers=headers)
        
        
        # Handle response
        if response.status_code >= 400:
            return handle_api_error(response)
        
        return format_response(response)
        
    except Exception as e:
        return {"error": str(e), "resource": "get_v1_knowledge_models_internal_documents_resource"}


async def resource_get_v1_knowledge_models_widget_resource(uri: str) -> Dict[str, Any]:
    """
    Access to get the knowledge model widget settings
    
    Method: GET
    Path: /v1/knowledge-models/{knowledge_model_id}/widget
    URI: api:///v1/knowledge-models/{knowledge_model_id}/widget
    """
    try:
        # Build URL
        url = f"/v1/knowledge-models/{knowledge_model_id}/widget"
        headers = get_api_headers()
        
        # Make request
        
        response = await client.get(url, headers=headers)
        
        
        # Handle response
        if response.status_code >= 400:
            return handle_api_error(response)
        
        return format_response(response)
        
    except Exception as e:
        return {"error": str(e), "resource": "get_v1_knowledge_models_widget_resource"}


async def resource_get_v1_knowledge_models_videos_transcription_resource(uri: str) -> Dict[str, Any]:
    """
    Access to get video transcription
    
    Method: GET
    Path: /v1/knowledge-models/{knowledge_model_id}/videos/{document_external_id}/transcription
    URI: api:///v1/knowledge-models/{knowledge_model_id}/videos/{document_external_id}/transcription
    """
    try:
        # Build URL
        url = f"/v1/knowledge-models/{knowledge_model_id}/videos/{document_external_id}/transcription"
        headers = get_api_headers()
        
        # Make request
        
        response = await client.get(url, headers=headers)
        
        
        # Handle response
        if response.status_code >= 400:
            return handle_api_error(response)
        
        return format_response(response)
        
    except Exception as e:
        return {"error": str(e), "resource": "get_v1_knowledge_models_videos_transcription_resource"}


async def resource_get_v1_knowledge_models_videos_resource(uri: str) -> Dict[str, Any]:
    """
    Access to get video document
    
    Method: GET
    Path: /v1/knowledge-models/{knowledge_model_id}/videos/{document_external_id}
    URI: api:///v1/knowledge-models/{knowledge_model_id}/videos/{document_external_id}
    """
    try:
        # Build URL
        url = f"/v1/knowledge-models/{knowledge_model_id}/videos/{document_external_id}"
        headers = get_api_headers()
        
        # Make request
        
        response = await client.get(url, headers=headers)
        
        
        # Handle response
        if response.status_code >= 400:
            return handle_api_error(response)
        
        return format_response(response)
        
    except Exception as e:
        return {"error": str(e), "resource": "get_v1_knowledge_models_videos_resource"}


async def resource_get_v1_language_models_resource(uri: str) -> Dict[str, Any]:
    """
    Access to list language models
    
    Method: GET
    Path: /v1/language_models
    URI: api:///v1/language_models
    """
    try:
        # Build URL
        url = f"/v1/language_models"
        headers = get_api_headers()
        
        # Make request
        
        response = await client.get(url, headers=headers)
        
        
        # Handle response
        if response.status_code >= 400:
            return handle_api_error(response)
        
        return format_response(response)
        
    except Exception as e:
        return {"error": str(e), "resource": "get_v1_language_models_resource"}
