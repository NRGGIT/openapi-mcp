"""
Tool implementations for MCP server.
"""

import json
import os
from typing import Any, Dict, List, Optional

import httpx
from utils import get_api_headers, handle_api_error, format_response

# HTTP client for API calls
client = httpx.AsyncClient(timeout=30.0)


async def tool_post_v1_knowledge_models(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """
    POST: Creates a new knowledge model.
    
    Method: POST
    Path: /v1/knowledge-models
    """
    try:
        # Extract parameters
        path_params = {}
        query_params = {}
        headers = get_api_headers()
        request_body = None
        
        # Process input arguments
        for key, value in arguments.items():
            if key == "body":
                request_body = value
            elif "{" + key + "}" in "/v1/knowledge-models":
                path_params[key] = value
            else:
                query_params[key] = value
        
        # Build URL
        url_path = "/v1/knowledge-models"
        for param_name, param_value in path_params.items():
            url_path = url_path.replace("{" + param_name + "}", str(param_value))
        
        url = "" + url_path
        
        # Make request
        response = await client.post(url, headers=headers, params=query_params, json=request_body)
        
        # Handle response
        if response.status_code >= 400:
            return handle_api_error(response)
        
        return format_response(response)
        
    except Exception as e:
        return {"error": str(e), "tool": "post_v1_knowledge_models"}


async def tool_delete_v1_knowledge_models(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """
    Delete knowledge model
    
    Method: DELETE
    Path: /v1/knowledge-models/{knowledge_model_id}
    """
    try:
        # Extract parameters
        path_params = {}
        query_params = {}
        headers = get_api_headers()
        request_body = None
        
        # Process input arguments
        for key, value in arguments.items():
            if key == "body":
                request_body = value
            elif "{" + key + "}" in "/v1/knowledge-models/{knowledge_model_id}":
                path_params[key] = value
            else:
                query_params[key] = value
        
        # Build URL
        url_path = "/v1/knowledge-models/{knowledge_model_id}"
        for param_name, param_value in path_params.items():
            url_path = url_path.replace("{" + param_name + "}", str(param_value))
        
        url = "" + url_path
        
        # Make request
        response = await client.delete(url, headers=headers, params=query_params)
        
        # Handle response
        if response.status_code >= 400:
            return handle_api_error(response)
        
        return format_response(response)
        
    except Exception as e:
        return {"error": str(e), "tool": "delete_v1_knowledge_models"}


async def tool_patch_v1_knowledge_models(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """
    PATCH: Update knowledge model
    
    Method: PATCH
    Path: /v1/knowledge-models/{knowledge_model_id}
    """
    try:
        # Extract parameters
        path_params = {}
        query_params = {}
        headers = get_api_headers()
        request_body = None
        
        # Process input arguments
        for key, value in arguments.items():
            if key == "body":
                request_body = value
            elif "{" + key + "}" in "/v1/knowledge-models/{knowledge_model_id}":
                path_params[key] = value
            else:
                query_params[key] = value
        
        # Build URL
        url_path = "/v1/knowledge-models/{knowledge_model_id}"
        for param_name, param_value in path_params.items():
            url_path = url_path.replace("{" + param_name + "}", str(param_value))
        
        url = "" + url_path
        
        # Make request
        response = await client.patch(url, headers=headers, params=query_params, json=request_body)
        
        # Handle response
        if response.status_code >= 400:
            return handle_api_error(response)
        
        return format_response(response)
        
    except Exception as e:
        return {"error": str(e), "tool": "patch_v1_knowledge_models"}


async def tool_patch_v1_knowledge_models_settings(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """
    PATCH: Update knowledge model settings
    
    Method: PATCH
    Path: /v1/knowledge-models/{knowledge_model_id}/settings
    """
    try:
        # Extract parameters
        path_params = {}
        query_params = {}
        headers = get_api_headers()
        request_body = None
        
        # Process input arguments
        for key, value in arguments.items():
            if key == "body":
                request_body = value
            elif "{" + key + "}" in "/v1/knowledge-models/{knowledge_model_id}/settings":
                path_params[key] = value
            else:
                query_params[key] = value
        
        # Build URL
        url_path = "/v1/knowledge-models/{knowledge_model_id}/settings"
        for param_name, param_value in path_params.items():
            url_path = url_path.replace("{" + param_name + "}", str(param_value))
        
        url = "" + url_path
        
        # Make request
        response = await client.patch(url, headers=headers, params=query_params, json=request_body)
        
        # Handle response
        if response.status_code >= 400:
            return handle_api_error(response)
        
        return format_response(response)
        
    except Exception as e:
        return {"error": str(e), "tool": "patch_v1_knowledge_models_settings"}


async def tool_post_v1_knowledge_models_chat_sessions(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """
    POST: Create new chat session via API
    
    Method: POST
    Path: /v1/knowledge-models/{knowledge_model_id}/chat-sessions
    """
    try:
        # Extract parameters
        path_params = {}
        query_params = {}
        headers = get_api_headers()
        request_body = None
        
        # Process input arguments
        for key, value in arguments.items():
            if key == "body":
                request_body = value
            elif "{" + key + "}" in "/v1/knowledge-models/{knowledge_model_id}/chat-sessions":
                path_params[key] = value
            else:
                query_params[key] = value
        
        # Build URL
        url_path = "/v1/knowledge-models/{knowledge_model_id}/chat-sessions"
        for param_name, param_value in path_params.items():
            url_path = url_path.replace("{" + param_name + "}", str(param_value))
        
        url = "" + url_path
        
        # Make request
        response = await client.post(url, headers=headers, params=query_params, json=request_body)
        
        # Handle response
        if response.status_code >= 400:
            return handle_api_error(response)
        
        return format_response(response)
        
    except Exception as e:
        return {"error": str(e), "tool": "post_v1_knowledge_models_chat_sessions"}


async def tool_delete_v1_knowledge_models_chat_sessions(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """
    Delete chat session
    
    Method: DELETE
    Path: /v1/knowledge-models/{knowledge_model_id}/chat-sessions/{chat_session_id}
    """
    try:
        # Extract parameters
        path_params = {}
        query_params = {}
        headers = get_api_headers()
        request_body = None
        
        # Process input arguments
        for key, value in arguments.items():
            if key == "body":
                request_body = value
            elif "{" + key + "}" in "/v1/knowledge-models/{knowledge_model_id}/chat-sessions/{chat_session_id}":
                path_params[key] = value
            else:
                query_params[key] = value
        
        # Build URL
        url_path = "/v1/knowledge-models/{knowledge_model_id}/chat-sessions/{chat_session_id}"
        for param_name, param_value in path_params.items():
            url_path = url_path.replace("{" + param_name + "}", str(param_value))
        
        url = "" + url_path
        
        # Make request
        response = await client.delete(url, headers=headers, params=query_params)
        
        # Handle response
        if response.status_code >= 400:
            return handle_api_error(response)
        
        return format_response(response)
        
    except Exception as e:
        return {"error": str(e), "tool": "delete_v1_knowledge_models_chat_sessions"}


async def tool_patch_v1_knowledge_models_chat_sessions(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """
    Patch chat session
    
    Method: PATCH
    Path: /v1/knowledge-models/{knowledge_model_id}/chat-sessions/{chat_session_id}
    """
    try:
        # Extract parameters
        path_params = {}
        query_params = {}
        headers = get_api_headers()
        request_body = None
        
        # Process input arguments
        for key, value in arguments.items():
            if key == "body":
                request_body = value
            elif "{" + key + "}" in "/v1/knowledge-models/{knowledge_model_id}/chat-sessions/{chat_session_id}":
                path_params[key] = value
            else:
                query_params[key] = value
        
        # Build URL
        url_path = "/v1/knowledge-models/{knowledge_model_id}/chat-sessions/{chat_session_id}"
        for param_name, param_value in path_params.items():
            url_path = url_path.replace("{" + param_name + "}", str(param_value))
        
        url = "" + url_path
        
        # Make request
        response = await client.patch(url, headers=headers, params=query_params, json=request_body)
        
        # Handle response
        if response.status_code >= 400:
            return handle_api_error(response)
        
        return format_response(response)
        
    except Exception as e:
        return {"error": str(e), "tool": "patch_v1_knowledge_models_chat_sessions"}


async def tool_post_v1_knowledge_models_chat_sessions_messages(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """
    POST: Create new chat message
    
    Method: POST
    Path: /v1/knowledge-models/{knowledge_model_id}/chat-sessions/{chat_session_id}/messages
    """
    try:
        # Extract parameters
        path_params = {}
        query_params = {}
        headers = get_api_headers()
        request_body = None
        
        # Process input arguments
        for key, value in arguments.items():
            if key == "body":
                request_body = value
            elif "{" + key + "}" in "/v1/knowledge-models/{knowledge_model_id}/chat-sessions/{chat_session_id}/messages":
                path_params[key] = value
            else:
                query_params[key] = value
        
        # Build URL
        url_path = "/v1/knowledge-models/{knowledge_model_id}/chat-sessions/{chat_session_id}/messages"
        for param_name, param_value in path_params.items():
            url_path = url_path.replace("{" + param_name + "}", str(param_value))
        
        url = "" + url_path
        
        # Make request
        response = await client.post(url, headers=headers, params=query_params, json=request_body)
        
        # Handle response
        if response.status_code >= 400:
            return handle_api_error(response)
        
        return format_response(response)
        
    except Exception as e:
        return {"error": str(e), "tool": "post_v1_knowledge_models_chat_sessions_messages"}


async def tool_get_v1_knowledge_models_chat_sessions_messages(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """
    Get all messages from chat session
    
    Method: GET
    Path: /v1/knowledge-models/{knowledge_model_id}/chat-sessions/{chat_session_id}/messages
    """
    try:
        # Extract parameters
        path_params = {}
        query_params = {}
        headers = get_api_headers()
        request_body = None
        
        # Process input arguments
        for key, value in arguments.items():
            if key == "body":
                request_body = value
            elif "{" + key + "}" in "/v1/knowledge-models/{knowledge_model_id}/chat-sessions/{chat_session_id}/messages":
                path_params[key] = value
            else:
                query_params[key] = value
        
        # Build URL
        url_path = "/v1/knowledge-models/{knowledge_model_id}/chat-sessions/{chat_session_id}/messages"
        for param_name, param_value in path_params.items():
            url_path = url_path.replace("{" + param_name + "}", str(param_value))
        
        url = "" + url_path
        
        # Make request
        response = await client.get(url, headers=headers, params=query_params)
        
        # Handle response
        if response.status_code >= 400:
            return handle_api_error(response)
        
        return format_response(response)
        
    except Exception as e:
        return {"error": str(e), "tool": "get_v1_knowledge_models_chat_sessions_messages"}


async def tool_get_v1_knowledge_models_chat_sessions_messages(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """
    Get chat message
    
    Method: GET
    Path: /v1/knowledge-models/{knowledge_model_id}/chat-sessions/{chat_session_id}/messages/{message_id}
    """
    try:
        # Extract parameters
        path_params = {}
        query_params = {}
        headers = get_api_headers()
        request_body = None
        
        # Process input arguments
        for key, value in arguments.items():
            if key == "body":
                request_body = value
            elif "{" + key + "}" in "/v1/knowledge-models/{knowledge_model_id}/chat-sessions/{chat_session_id}/messages/{message_id}":
                path_params[key] = value
            else:
                query_params[key] = value
        
        # Build URL
        url_path = "/v1/knowledge-models/{knowledge_model_id}/chat-sessions/{chat_session_id}/messages/{message_id}"
        for param_name, param_value in path_params.items():
            url_path = url_path.replace("{" + param_name + "}", str(param_value))
        
        url = "" + url_path
        
        # Make request
        response = await client.get(url, headers=headers, params=query_params)
        
        # Handle response
        if response.status_code >= 400:
            return handle_api_error(response)
        
        return format_response(response)
        
    except Exception as e:
        return {"error": str(e), "tool": "get_v1_knowledge_models_chat_sessions_messages"}


async def tool_post_v1_knowledge_models_chat_sessions_messages_feedback(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """
    POST: Set feedback on bot message
    
    Method: POST
    Path: /v1/knowledge-models/{knowledge_model_id}/chat-sessions/{chat_session_id}/messages/{message_id}/feedback
    """
    try:
        # Extract parameters
        path_params = {}
        query_params = {}
        headers = get_api_headers()
        request_body = None
        
        # Process input arguments
        for key, value in arguments.items():
            if key == "body":
                request_body = value
            elif "{" + key + "}" in "/v1/knowledge-models/{knowledge_model_id}/chat-sessions/{chat_session_id}/messages/{message_id}/feedback":
                path_params[key] = value
            else:
                query_params[key] = value
        
        # Build URL
        url_path = "/v1/knowledge-models/{knowledge_model_id}/chat-sessions/{chat_session_id}/messages/{message_id}/feedback"
        for param_name, param_value in path_params.items():
            url_path = url_path.replace("{" + param_name + "}", str(param_value))
        
        url = "" + url_path
        
        # Make request
        response = await client.post(url, headers=headers, params=query_params, json=request_body)
        
        # Handle response
        if response.status_code >= 400:
            return handle_api_error(response)
        
        return format_response(response)
        
    except Exception as e:
        return {"error": str(e), "tool": "post_v1_knowledge_models_chat_sessions_messages_feedback"}


async def tool_get_v1_knowledge_models_files(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """
    GET: List files of the knowledge model
    
    Method: GET
    Path: /v1/knowledge-models/{knowledge_model_id}/files
    """
    try:
        # Extract parameters
        path_params = {}
        query_params = {}
        headers = get_api_headers()
        request_body = None
        
        # Process input arguments
        for key, value in arguments.items():
            if key == "body":
                request_body = value
            elif "{" + key + "}" in "/v1/knowledge-models/{knowledge_model_id}/files":
                path_params[key] = value
            else:
                query_params[key] = value
        
        # Build URL
        url_path = "/v1/knowledge-models/{knowledge_model_id}/files"
        for param_name, param_value in path_params.items():
            url_path = url_path.replace("{" + param_name + "}", str(param_value))
        
        url = "" + url_path
        
        # Make request
        response = await client.get(url, headers=headers, params=query_params)
        
        # Handle response
        if response.status_code >= 400:
            return handle_api_error(response)
        
        return format_response(response)
        
    except Exception as e:
        return {"error": str(e), "tool": "get_v1_knowledge_models_files"}


async def tool_post_v1_knowledge_models_files(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """
    POST: Upload a file to the knowledge model
    
    Method: POST
    Path: /v1/knowledge-models/{knowledge_model_id}/files
    """
    try:
        # Extract parameters
        path_params = {}
        query_params = {}
        headers = get_api_headers()
        request_body = None
        
        # Process input arguments
        for key, value in arguments.items():
            if key == "body":
                request_body = value
            elif "{" + key + "}" in "/v1/knowledge-models/{knowledge_model_id}/files":
                path_params[key] = value
            else:
                query_params[key] = value
        
        # Build URL
        url_path = "/v1/knowledge-models/{knowledge_model_id}/files"
        for param_name, param_value in path_params.items():
            url_path = url_path.replace("{" + param_name + "}", str(param_value))
        
        url = "" + url_path
        
        # Make request
        response = await client.post(url, headers=headers, params=query_params, json=request_body)
        
        # Handle response
        if response.status_code >= 400:
            return handle_api_error(response)
        
        return format_response(response)
        
    except Exception as e:
        return {"error": str(e), "tool": "post_v1_knowledge_models_files"}


async def tool_delete_v1_knowledge_models_files(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """
    Delete a file from a knowledge model
    
    Method: DELETE
    Path: /v1/knowledge-models/{knowledge_model_id}/files/{file_id}
    """
    try:
        # Extract parameters
        path_params = {}
        query_params = {}
        headers = get_api_headers()
        request_body = None
        
        # Process input arguments
        for key, value in arguments.items():
            if key == "body":
                request_body = value
            elif "{" + key + "}" in "/v1/knowledge-models/{knowledge_model_id}/files/{file_id}":
                path_params[key] = value
            else:
                query_params[key] = value
        
        # Build URL
        url_path = "/v1/knowledge-models/{knowledge_model_id}/files/{file_id}"
        for param_name, param_value in path_params.items():
            url_path = url_path.replace("{" + param_name + "}", str(param_value))
        
        url = "" + url_path
        
        # Make request
        response = await client.delete(url, headers=headers, params=query_params)
        
        # Handle response
        if response.status_code >= 400:
            return handle_api_error(response)
        
        return format_response(response)
        
    except Exception as e:
        return {"error": str(e), "tool": "delete_v1_knowledge_models_files"}


async def tool_patch_v1_knowledge_models_files_metadata(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """
    PATCH: Update metadata of the file
    
    Method: PATCH
    Path: /v1/knowledge-models/{knowledge_model_id}/files/{file_id}/metadata
    """
    try:
        # Extract parameters
        path_params = {}
        query_params = {}
        headers = get_api_headers()
        request_body = None
        
        # Process input arguments
        for key, value in arguments.items():
            if key == "body":
                request_body = value
            elif "{" + key + "}" in "/v1/knowledge-models/{knowledge_model_id}/files/{file_id}/metadata":
                path_params[key] = value
            else:
                query_params[key] = value
        
        # Build URL
        url_path = "/v1/knowledge-models/{knowledge_model_id}/files/{file_id}/metadata"
        for param_name, param_value in path_params.items():
            url_path = url_path.replace("{" + param_name + "}", str(param_value))
        
        url = "" + url_path
        
        # Make request
        response = await client.patch(url, headers=headers, params=query_params, json=request_body)
        
        # Handle response
        if response.status_code >= 400:
            return handle_api_error(response)
        
        return format_response(response)
        
    except Exception as e:
        return {"error": str(e), "tool": "patch_v1_knowledge_models_files_metadata"}


async def tool_post_v1_knowledge_models_internal_documents(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """
    POST: Create new internal document
    
    Method: POST
    Path: /v1/knowledge-models/{knowledge_model_id}/internal-documents
    """
    try:
        # Extract parameters
        path_params = {}
        query_params = {}
        headers = get_api_headers()
        request_body = None
        
        # Process input arguments
        for key, value in arguments.items():
            if key == "body":
                request_body = value
            elif "{" + key + "}" in "/v1/knowledge-models/{knowledge_model_id}/internal-documents":
                path_params[key] = value
            else:
                query_params[key] = value
        
        # Build URL
        url_path = "/v1/knowledge-models/{knowledge_model_id}/internal-documents"
        for param_name, param_value in path_params.items():
            url_path = url_path.replace("{" + param_name + "}", str(param_value))
        
        url = "" + url_path
        
        # Make request
        response = await client.post(url, headers=headers, params=query_params, json=request_body)
        
        # Handle response
        if response.status_code >= 400:
            return handle_api_error(response)
        
        return format_response(response)
        
    except Exception as e:
        return {"error": str(e), "tool": "post_v1_knowledge_models_internal_documents"}


async def tool_get_v1_knowledge_models_internal_documents(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """
    GET: List internal documents
    
    Method: GET
    Path: /v1/knowledge-models/{knowledge_model_id}/internal-documents
    """
    try:
        # Extract parameters
        path_params = {}
        query_params = {}
        headers = get_api_headers()
        request_body = None
        
        # Process input arguments
        for key, value in arguments.items():
            if key == "body":
                request_body = value
            elif "{" + key + "}" in "/v1/knowledge-models/{knowledge_model_id}/internal-documents":
                path_params[key] = value
            else:
                query_params[key] = value
        
        # Build URL
        url_path = "/v1/knowledge-models/{knowledge_model_id}/internal-documents"
        for param_name, param_value in path_params.items():
            url_path = url_path.replace("{" + param_name + "}", str(param_value))
        
        url = "" + url_path
        
        # Make request
        response = await client.get(url, headers=headers, params=query_params)
        
        # Handle response
        if response.status_code >= 400:
            return handle_api_error(response)
        
        return format_response(response)
        
    except Exception as e:
        return {"error": str(e), "tool": "get_v1_knowledge_models_internal_documents"}


async def tool_patch_v1_knowledge_models_internal_documents(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """
    PATCH: Update internal document
    
    Method: PATCH
    Path: /v1/knowledge-models/{knowledge_model_id}/internal-documents/{document_id}
    """
    try:
        # Extract parameters
        path_params = {}
        query_params = {}
        headers = get_api_headers()
        request_body = None
        
        # Process input arguments
        for key, value in arguments.items():
            if key == "body":
                request_body = value
            elif "{" + key + "}" in "/v1/knowledge-models/{knowledge_model_id}/internal-documents/{document_id}":
                path_params[key] = value
            else:
                query_params[key] = value
        
        # Build URL
        url_path = "/v1/knowledge-models/{knowledge_model_id}/internal-documents/{document_id}"
        for param_name, param_value in path_params.items():
            url_path = url_path.replace("{" + param_name + "}", str(param_value))
        
        url = "" + url_path
        
        # Make request
        response = await client.patch(url, headers=headers, params=query_params, json=request_body)
        
        # Handle response
        if response.status_code >= 400:
            return handle_api_error(response)
        
        return format_response(response)
        
    except Exception as e:
        return {"error": str(e), "tool": "patch_v1_knowledge_models_internal_documents"}


async def tool_delete_v1_knowledge_models_internal_documents(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """
    Delete internal document
    
    Method: DELETE
    Path: /v1/knowledge-models/{knowledge_model_id}/internal-documents/{document_id}
    """
    try:
        # Extract parameters
        path_params = {}
        query_params = {}
        headers = get_api_headers()
        request_body = None
        
        # Process input arguments
        for key, value in arguments.items():
            if key == "body":
                request_body = value
            elif "{" + key + "}" in "/v1/knowledge-models/{knowledge_model_id}/internal-documents/{document_id}":
                path_params[key] = value
            else:
                query_params[key] = value
        
        # Build URL
        url_path = "/v1/knowledge-models/{knowledge_model_id}/internal-documents/{document_id}"
        for param_name, param_value in path_params.items():
            url_path = url_path.replace("{" + param_name + "}", str(param_value))
        
        url = "" + url_path
        
        # Make request
        response = await client.delete(url, headers=headers, params=query_params)
        
        # Handle response
        if response.status_code >= 400:
            return handle_api_error(response)
        
        return format_response(response)
        
    except Exception as e:
        return {"error": str(e), "tool": "delete_v1_knowledge_models_internal_documents"}


async def tool_post_v1_knowledge_models_internal_documents_chunks(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """
    POST: Create new internal chunk
    
    Method: POST
    Path: /v1/knowledge-models/{knowledge_model_id}/internal-documents/{document_id}/chunks
    """
    try:
        # Extract parameters
        path_params = {}
        query_params = {}
        headers = get_api_headers()
        request_body = None
        
        # Process input arguments
        for key, value in arguments.items():
            if key == "body":
                request_body = value
            elif "{" + key + "}" in "/v1/knowledge-models/{knowledge_model_id}/internal-documents/{document_id}/chunks":
                path_params[key] = value
            else:
                query_params[key] = value
        
        # Build URL
        url_path = "/v1/knowledge-models/{knowledge_model_id}/internal-documents/{document_id}/chunks"
        for param_name, param_value in path_params.items():
            url_path = url_path.replace("{" + param_name + "}", str(param_value))
        
        url = "" + url_path
        
        # Make request
        response = await client.post(url, headers=headers, params=query_params, json=request_body)
        
        # Handle response
        if response.status_code >= 400:
            return handle_api_error(response)
        
        return format_response(response)
        
    except Exception as e:
        return {"error": str(e), "tool": "post_v1_knowledge_models_internal_documents_chunks"}


async def tool_get_v1_knowledge_models_internal_documents_chunks(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """
    GET: List internal chunks
    
    Method: GET
    Path: /v1/knowledge-models/{knowledge_model_id}/internal-documents/{document_id}/chunks
    """
    try:
        # Extract parameters
        path_params = {}
        query_params = {}
        headers = get_api_headers()
        request_body = None
        
        # Process input arguments
        for key, value in arguments.items():
            if key == "body":
                request_body = value
            elif "{" + key + "}" in "/v1/knowledge-models/{knowledge_model_id}/internal-documents/{document_id}/chunks":
                path_params[key] = value
            else:
                query_params[key] = value
        
        # Build URL
        url_path = "/v1/knowledge-models/{knowledge_model_id}/internal-documents/{document_id}/chunks"
        for param_name, param_value in path_params.items():
            url_path = url_path.replace("{" + param_name + "}", str(param_value))
        
        url = "" + url_path
        
        # Make request
        response = await client.get(url, headers=headers, params=query_params)
        
        # Handle response
        if response.status_code >= 400:
            return handle_api_error(response)
        
        return format_response(response)
        
    except Exception as e:
        return {"error": str(e), "tool": "get_v1_knowledge_models_internal_documents_chunks"}


async def tool_post_v1_knowledge_models_internal_documents_chunks_batch(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """
    POST: Batch create internal chunks
    
    Method: POST
    Path: /v1/knowledge-models/{knowledge_model_id}/internal-documents/{document_id}/chunks/batch
    """
    try:
        # Extract parameters
        path_params = {}
        query_params = {}
        headers = get_api_headers()
        request_body = None
        
        # Process input arguments
        for key, value in arguments.items():
            if key == "body":
                request_body = value
            elif "{" + key + "}" in "/v1/knowledge-models/{knowledge_model_id}/internal-documents/{document_id}/chunks/batch":
                path_params[key] = value
            else:
                query_params[key] = value
        
        # Build URL
        url_path = "/v1/knowledge-models/{knowledge_model_id}/internal-documents/{document_id}/chunks/batch"
        for param_name, param_value in path_params.items():
            url_path = url_path.replace("{" + param_name + "}", str(param_value))
        
        url = "" + url_path
        
        # Make request
        response = await client.post(url, headers=headers, params=query_params, json=request_body)
        
        # Handle response
        if response.status_code >= 400:
            return handle_api_error(response)
        
        return format_response(response)
        
    except Exception as e:
        return {"error": str(e), "tool": "post_v1_knowledge_models_internal_documents_chunks_batch"}


async def tool_get_v1_knowledge_models_internal_documents_chunks(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """
    Get internal chunk
    
    Method: GET
    Path: /v1/knowledge-models/{knowledge_model_id}/internal-documents/{document_id}/chunks/{chunk_id}
    """
    try:
        # Extract parameters
        path_params = {}
        query_params = {}
        headers = get_api_headers()
        request_body = None
        
        # Process input arguments
        for key, value in arguments.items():
            if key == "body":
                request_body = value
            elif "{" + key + "}" in "/v1/knowledge-models/{knowledge_model_id}/internal-documents/{document_id}/chunks/{chunk_id}":
                path_params[key] = value
            else:
                query_params[key] = value
        
        # Build URL
        url_path = "/v1/knowledge-models/{knowledge_model_id}/internal-documents/{document_id}/chunks/{chunk_id}"
        for param_name, param_value in path_params.items():
            url_path = url_path.replace("{" + param_name + "}", str(param_value))
        
        url = "" + url_path
        
        # Make request
        response = await client.get(url, headers=headers, params=query_params)
        
        # Handle response
        if response.status_code >= 400:
            return handle_api_error(response)
        
        return format_response(response)
        
    except Exception as e:
        return {"error": str(e), "tool": "get_v1_knowledge_models_internal_documents_chunks"}


async def tool_patch_v1_knowledge_models_internal_documents_chunks(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """
    PATCH: Update internal chunk
    
    Method: PATCH
    Path: /v1/knowledge-models/{knowledge_model_id}/internal-documents/{document_id}/chunks/{chunk_id}
    """
    try:
        # Extract parameters
        path_params = {}
        query_params = {}
        headers = get_api_headers()
        request_body = None
        
        # Process input arguments
        for key, value in arguments.items():
            if key == "body":
                request_body = value
            elif "{" + key + "}" in "/v1/knowledge-models/{knowledge_model_id}/internal-documents/{document_id}/chunks/{chunk_id}":
                path_params[key] = value
            else:
                query_params[key] = value
        
        # Build URL
        url_path = "/v1/knowledge-models/{knowledge_model_id}/internal-documents/{document_id}/chunks/{chunk_id}"
        for param_name, param_value in path_params.items():
            url_path = url_path.replace("{" + param_name + "}", str(param_value))
        
        url = "" + url_path
        
        # Make request
        response = await client.patch(url, headers=headers, params=query_params, json=request_body)
        
        # Handle response
        if response.status_code >= 400:
            return handle_api_error(response)
        
        return format_response(response)
        
    except Exception as e:
        return {"error": str(e), "tool": "patch_v1_knowledge_models_internal_documents_chunks"}


async def tool_delete_v1_knowledge_models_internal_documents_chunks(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """
    Delete internal chunk
    
    Method: DELETE
    Path: /v1/knowledge-models/{knowledge_model_id}/internal-documents/{document_id}/chunks/{chunk_id}
    """
    try:
        # Extract parameters
        path_params = {}
        query_params = {}
        headers = get_api_headers()
        request_body = None
        
        # Process input arguments
        for key, value in arguments.items():
            if key == "body":
                request_body = value
            elif "{" + key + "}" in "/v1/knowledge-models/{knowledge_model_id}/internal-documents/{document_id}/chunks/{chunk_id}":
                path_params[key] = value
            else:
                query_params[key] = value
        
        # Build URL
        url_path = "/v1/knowledge-models/{knowledge_model_id}/internal-documents/{document_id}/chunks/{chunk_id}"
        for param_name, param_value in path_params.items():
            url_path = url_path.replace("{" + param_name + "}", str(param_value))
        
        url = "" + url_path
        
        # Make request
        response = await client.delete(url, headers=headers, params=query_params)
        
        # Handle response
        if response.status_code >= 400:
            return handle_api_error(response)
        
        return format_response(response)
        
    except Exception as e:
        return {"error": str(e), "tool": "delete_v1_knowledge_models_internal_documents_chunks"}


async def tool_patch_v1_knowledge_models_widget(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """
    Patch knowledge model widget settings
    
    Method: PATCH
    Path: /v1/knowledge-models/{knowledge_model_id}/widget
    """
    try:
        # Extract parameters
        path_params = {}
        query_params = {}
        headers = get_api_headers()
        request_body = None
        
        # Process input arguments
        for key, value in arguments.items():
            if key == "body":
                request_body = value
            elif "{" + key + "}" in "/v1/knowledge-models/{knowledge_model_id}/widget":
                path_params[key] = value
            else:
                query_params[key] = value
        
        # Build URL
        url_path = "/v1/knowledge-models/{knowledge_model_id}/widget"
        for param_name, param_value in path_params.items():
            url_path = url_path.replace("{" + param_name + "}", str(param_value))
        
        url = "" + url_path
        
        # Make request
        response = await client.patch(url, headers=headers, params=query_params, json=request_body)
        
        # Handle response
        if response.status_code >= 400:
            return handle_api_error(response)
        
        return format_response(response)
        
    except Exception as e:
        return {"error": str(e), "tool": "patch_v1_knowledge_models_widget"}


async def tool_get_v1_knowledge_models_chunks(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """
    GET: List document chunks
    
    Method: GET
    Path: /v1/knowledge-models/{knowledge_model_id}/chunks
    """
    try:
        # Extract parameters
        path_params = {}
        query_params = {}
        headers = get_api_headers()
        request_body = None
        
        # Process input arguments
        for key, value in arguments.items():
            if key == "body":
                request_body = value
            elif "{" + key + "}" in "/v1/knowledge-models/{knowledge_model_id}/chunks":
                path_params[key] = value
            else:
                query_params[key] = value
        
        # Build URL
        url_path = "/v1/knowledge-models/{knowledge_model_id}/chunks"
        for param_name, param_value in path_params.items():
            url_path = url_path.replace("{" + param_name + "}", str(param_value))
        
        url = "" + url_path
        
        # Make request
        response = await client.get(url, headers=headers, params=query_params)
        
        # Handle response
        if response.status_code >= 400:
            return handle_api_error(response)
        
        return format_response(response)
        
    except Exception as e:
        return {"error": str(e), "tool": "get_v1_knowledge_models_chunks"}


async def tool_post_v1_knowledge_models_chunks_search(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """
    POST: Search for raw text chunks
    
    Method: POST
    Path: /v1/knowledge-models/{knowledge_model_id}/chunks/search
    """
    try:
        # Extract parameters
        path_params = {}
        query_params = {}
        headers = get_api_headers()
        request_body = None
        
        # Process input arguments
        for key, value in arguments.items():
            if key == "body":
                request_body = value
            elif "{" + key + "}" in "/v1/knowledge-models/{knowledge_model_id}/chunks/search":
                path_params[key] = value
            else:
                query_params[key] = value
        
        # Build URL
        url_path = "/v1/knowledge-models/{knowledge_model_id}/chunks/search"
        for param_name, param_value in path_params.items():
            url_path = url_path.replace("{" + param_name + "}", str(param_value))
        
        url = "" + url_path
        
        # Make request
        response = await client.post(url, headers=headers, params=query_params, json=request_body)
        
        # Handle response
        if response.status_code >= 400:
            return handle_api_error(response)
        
        return format_response(response)
        
    except Exception as e:
        return {"error": str(e), "tool": "post_v1_knowledge_models_chunks_search"}


async def tool_post_v1_knowledge_models_videos_import(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """
    POST: Add video document into Model
    
    Method: POST
    Path: /v1/knowledge-models/{knowledge_model_id}/videos/import
    """
    try:
        # Extract parameters
        path_params = {}
        query_params = {}
        headers = get_api_headers()
        request_body = None
        
        # Process input arguments
        for key, value in arguments.items():
            if key == "body":
                request_body = value
            elif "{" + key + "}" in "/v1/knowledge-models/{knowledge_model_id}/videos/import":
                path_params[key] = value
            else:
                query_params[key] = value
        
        # Build URL
        url_path = "/v1/knowledge-models/{knowledge_model_id}/videos/import"
        for param_name, param_value in path_params.items():
            url_path = url_path.replace("{" + param_name + "}", str(param_value))
        
        url = "" + url_path
        
        # Make request
        response = await client.post(url, headers=headers, params=query_params, json=request_body)
        
        # Handle response
        if response.status_code >= 400:
            return handle_api_error(response)
        
        return format_response(response)
        
    except Exception as e:
        return {"error": str(e), "tool": "post_v1_knowledge_models_videos_import"}


async def tool_get_v1_knowledge_models_videos(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """
    GET: List videos in the knowledge model
    
    Method: GET
    Path: /v1/knowledge-models/{knowledge_model_id}/videos
    """
    try:
        # Extract parameters
        path_params = {}
        query_params = {}
        headers = get_api_headers()
        request_body = None
        
        # Process input arguments
        for key, value in arguments.items():
            if key == "body":
                request_body = value
            elif "{" + key + "}" in "/v1/knowledge-models/{knowledge_model_id}/videos":
                path_params[key] = value
            else:
                query_params[key] = value
        
        # Build URL
        url_path = "/v1/knowledge-models/{knowledge_model_id}/videos"
        for param_name, param_value in path_params.items():
            url_path = url_path.replace("{" + param_name + "}", str(param_value))
        
        url = "" + url_path
        
        # Make request
        response = await client.get(url, headers=headers, params=query_params)
        
        # Handle response
        if response.status_code >= 400:
            return handle_api_error(response)
        
        return format_response(response)
        
    except Exception as e:
        return {"error": str(e), "tool": "get_v1_knowledge_models_videos"}


async def tool_patch_v1_knowledge_models_videos(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """
    Patch video document
    
    Method: PATCH
    Path: /v1/knowledge-models/{knowledge_model_id}/videos/{document_external_id}
    """
    try:
        # Extract parameters
        path_params = {}
        query_params = {}
        headers = get_api_headers()
        request_body = None
        
        # Process input arguments
        for key, value in arguments.items():
            if key == "body":
                request_body = value
            elif "{" + key + "}" in "/v1/knowledge-models/{knowledge_model_id}/videos/{document_external_id}":
                path_params[key] = value
            else:
                query_params[key] = value
        
        # Build URL
        url_path = "/v1/knowledge-models/{knowledge_model_id}/videos/{document_external_id}"
        for param_name, param_value in path_params.items():
            url_path = url_path.replace("{" + param_name + "}", str(param_value))
        
        url = "" + url_path
        
        # Make request
        response = await client.patch(url, headers=headers, params=query_params, json=request_body)
        
        # Handle response
        if response.status_code >= 400:
            return handle_api_error(response)
        
        return format_response(response)
        
    except Exception as e:
        return {"error": str(e), "tool": "patch_v1_knowledge_models_videos"}


async def tool_delete_v1_knowledge_models_videos(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """
    Delete video document
    
    Method: DELETE
    Path: /v1/knowledge-models/{knowledge_model_id}/videos/{document_external_id}
    """
    try:
        # Extract parameters
        path_params = {}
        query_params = {}
        headers = get_api_headers()
        request_body = None
        
        # Process input arguments
        for key, value in arguments.items():
            if key == "body":
                request_body = value
            elif "{" + key + "}" in "/v1/knowledge-models/{knowledge_model_id}/videos/{document_external_id}":
                path_params[key] = value
            else:
                query_params[key] = value
        
        # Build URL
        url_path = "/v1/knowledge-models/{knowledge_model_id}/videos/{document_external_id}"
        for param_name, param_value in path_params.items():
            url_path = url_path.replace("{" + param_name + "}", str(param_value))
        
        url = "" + url_path
        
        # Make request
        response = await client.delete(url, headers=headers, params=query_params)
        
        # Handle response
        if response.status_code >= 400:
            return handle_api_error(response)
        
        return format_response(response)
        
    except Exception as e:
        return {"error": str(e), "tool": "delete_v1_knowledge_models_videos"}


async def tool_post_v1_knowledge_models_chat_completions(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """
    POST: Generates text responses based on incoming messages.
    
    Method: POST
    Path: /v1/knowledge-models/{knowledge_model_id}/chat/completions/{extension}
    """
    try:
        # Extract parameters
        path_params = {}
        query_params = {}
        headers = get_api_headers()
        request_body = None
        
        # Process input arguments
        for key, value in arguments.items():
            if key == "body":
                request_body = value
            elif "{" + key + "}" in "/v1/knowledge-models/{knowledge_model_id}/chat/completions/{extension}":
                path_params[key] = value
            else:
                query_params[key] = value
        
        # Build URL
        url_path = "/v1/knowledge-models/{knowledge_model_id}/chat/completions/{extension}"
        for param_name, param_value in path_params.items():
            url_path = url_path.replace("{" + param_name + "}", str(param_value))
        
        url = "" + url_path
        
        # Make request
        response = await client.post(url, headers=headers, params=query_params, json=request_body)
        
        # Handle response
        if response.status_code >= 400:
            return handle_api_error(response)
        
        return format_response(response)
        
    except Exception as e:
        return {"error": str(e), "tool": "post_v1_knowledge_models_chat_completions"}


async def tool_post_v1_knowledge_models_chat_completions(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """
    POST: Generates text responses based on incoming messages.
    
    Method: POST
    Path: /v1/knowledge-models/{knowledge_model_id}/chat/completions
    """
    try:
        # Extract parameters
        path_params = {}
        query_params = {}
        headers = get_api_headers()
        request_body = None
        
        # Process input arguments
        for key, value in arguments.items():
            if key == "body":
                request_body = value
            elif "{" + key + "}" in "/v1/knowledge-models/{knowledge_model_id}/chat/completions":
                path_params[key] = value
            else:
                query_params[key] = value
        
        # Build URL
        url_path = "/v1/knowledge-models/{knowledge_model_id}/chat/completions"
        for param_name, param_value in path_params.items():
            url_path = url_path.replace("{" + param_name + "}", str(param_value))
        
        url = "" + url_path
        
        # Make request
        response = await client.post(url, headers=headers, params=query_params, json=request_body)
        
        # Handle response
        if response.status_code >= 400:
            return handle_api_error(response)
        
        return format_response(response)
        
    except Exception as e:
        return {"error": str(e), "tool": "post_v1_knowledge_models_chat_completions"}


async def tool_post_v1_knowledge_models_tools_translation(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """
    POST: English translation tool.
    
    Method: POST
    Path: /v1/knowledge-models/{knowledge_model_id}/tools/translation
    """
    try:
        # Extract parameters
        path_params = {}
        query_params = {}
        headers = get_api_headers()
        request_body = None
        
        # Process input arguments
        for key, value in arguments.items():
            if key == "body":
                request_body = value
            elif "{" + key + "}" in "/v1/knowledge-models/{knowledge_model_id}/tools/translation":
                path_params[key] = value
            else:
                query_params[key] = value
        
        # Build URL
        url_path = "/v1/knowledge-models/{knowledge_model_id}/tools/translation"
        for param_name, param_value in path_params.items():
            url_path = url_path.replace("{" + param_name + "}", str(param_value))
        
        url = "" + url_path
        
        # Make request
        response = await client.post(url, headers=headers, params=query_params, json=request_body)
        
        # Handle response
        if response.status_code >= 400:
            return handle_api_error(response)
        
        return format_response(response)
        
    except Exception as e:
        return {"error": str(e), "tool": "post_v1_knowledge_models_tools_translation"}

