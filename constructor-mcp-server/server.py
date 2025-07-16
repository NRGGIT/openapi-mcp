#!/usr/bin/env python3
"""
constructor-knowledge-api - MCP Server
Generated from OpenAPI specification for ConstructorKnowledgeModel
"""

import asyncio
import os
import sys
from typing import Any, Dict, List, Optional

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, Resource, TextContent, ImageContent, EmbeddedResource
import mcp.server.stdio
import mcp.types as types

from tools import *
from resources import *
from utils import setup_logging, load_config

# Server configuration
SERVER_NAME = "constructor-knowledge-api"
SERVER_VERSION = "1.0.0"

# Initialize server
server = Server(SERVER_NAME)

# Setup logging
logger = setup_logging()

@server.list_tools()
async def handle_list_tools() -> List[Tool]:
    """List available tools."""
    tools = [

        Tool(
            name="post_v1_knowledge_models",
            description="POST: Creates a new knowledge model.",
            inputSchema={"properties": {}, "required": [], "type": "object"}
        ),

        Tool(
            name="delete_v1_knowledge_models",
            description="Delete knowledge model",
            inputSchema={"properties": {"knowledge_model_id": {"type": "string"}}, "required": ["knowledge_model_id"], "type": "object"}
        ),

        Tool(
            name="patch_v1_knowledge_models",
            description="PATCH: Update knowledge model",
            inputSchema={"properties": {"knowledge_model_id": {"type": "string"}}, "required": ["knowledge_model_id"], "type": "object"}
        ),

        Tool(
            name="patch_v1_knowledge_models_settings",
            description="PATCH: Update knowledge model settings",
            inputSchema={"properties": {"knowledge_model_id": {"type": "string"}}, "required": ["knowledge_model_id"], "type": "object"}
        ),

        Tool(
            name="post_v1_knowledge_models_chat_sessions",
            description="POST: Create new chat session via API",
            inputSchema={"properties": {"knowledge_model_id": {"type": "string"}}, "required": ["knowledge_model_id"], "type": "object"}
        ),

        Tool(
            name="delete_v1_knowledge_models_chat_sessions",
            description="Delete chat session",
            inputSchema={"properties": {"chat_session_id": {"type": "string"}, "knowledge_model_id": {"type": "string"}}, "required": ["chat_session_id", "knowledge_model_id"], "type": "object"}
        ),

        Tool(
            name="patch_v1_knowledge_models_chat_sessions",
            description="Patch chat session",
            inputSchema={"properties": {"chat_session_id": {"type": "string"}, "knowledge_model_id": {"type": "string"}}, "required": ["chat_session_id", "knowledge_model_id"], "type": "object"}
        ),

        Tool(
            name="post_v1_knowledge_models_chat_sessions_messages",
            description="POST: Create new chat message",
            inputSchema={"properties": {"chat_session_id": {"type": "string"}, "knowledge_model_id": {"type": "string"}}, "required": ["knowledge_model_id", "chat_session_id"], "type": "object"}
        ),

        Tool(
            name="get_v1_knowledge_models_chat_sessions_messages",
            description="Get all messages from chat session",
            inputSchema={"properties": {"chat_session_id": {"type": "string"}, "knowledge_model_id": {"type": "string"}, "limit": {"type": "string"}, "offset": {"type": "string"}}, "required": ["knowledge_model_id", "chat_session_id"], "type": "object"}
        ),

        Tool(
            name="get_v1_knowledge_models_chat_sessions_messages",
            description="Get chat message",
            inputSchema={"properties": {"chat_session_id": {"type": "string"}, "knowledge_model_id": {"type": "string"}, "message_id": {"type": "string"}}, "required": ["knowledge_model_id", "chat_session_id", "message_id"], "type": "object"}
        ),

        Tool(
            name="post_v1_knowledge_models_chat_sessions_messages_feedback",
            description="POST: Set feedback on bot message",
            inputSchema={"properties": {"chat_session_id": {"type": "string"}, "knowledge_model_id": {"type": "string"}, "message_id": {"type": "string"}}, "required": ["knowledge_model_id", "chat_session_id", "message_id"], "type": "object"}
        ),

        Tool(
            name="get_v1_knowledge_models_files",
            description="GET: List files of the knowledge model",
            inputSchema={"properties": {"knowledge_model_id": {"type": "string"}, "limit": {"type": "string"}, "offset": {"type": "string"}}, "required": ["knowledge_model_id"], "type": "object"}
        ),

        Tool(
            name="post_v1_knowledge_models_files",
            description="POST: Upload a file to the knowledge model",
            inputSchema={"properties": {"knowledge_model_id": {"type": "string"}}, "required": ["knowledge_model_id"], "type": "object"}
        ),

        Tool(
            name="delete_v1_knowledge_models_files",
            description="Delete a file from a knowledge model",
            inputSchema={"properties": {"file_id": {"type": "string"}, "knowledge_model_id": {"type": "string"}}, "required": ["file_id", "knowledge_model_id"], "type": "object"}
        ),

        Tool(
            name="patch_v1_knowledge_models_files_metadata",
            description="PATCH: Update metadata of the file",
            inputSchema={"properties": {"file_id": {"type": "string"}, "knowledge_model_id": {"type": "string"}}, "required": ["file_id", "knowledge_model_id"], "type": "object"}
        ),

        Tool(
            name="post_v1_knowledge_models_internal_documents",
            description="POST: Create new internal document",
            inputSchema={"properties": {"knowledge_model_id": {"type": "string"}}, "required": ["knowledge_model_id"], "type": "object"}
        ),

        Tool(
            name="get_v1_knowledge_models_internal_documents",
            description="GET: List internal documents",
            inputSchema={"properties": {"knowledge_model_id": {"type": "string"}, "limit": {"type": "string"}, "offset": {"type": "string"}}, "required": ["knowledge_model_id"], "type": "object"}
        ),

        Tool(
            name="patch_v1_knowledge_models_internal_documents",
            description="PATCH: Update internal document",
            inputSchema={"properties": {"document_id": {"type": "string"}, "knowledge_model_id": {"type": "string"}}, "required": ["document_id", "knowledge_model_id"], "type": "object"}
        ),

        Tool(
            name="delete_v1_knowledge_models_internal_documents",
            description="Delete internal document",
            inputSchema={"properties": {"document_id": {"type": "string"}, "knowledge_model_id": {"type": "string"}}, "required": ["document_id", "knowledge_model_id"], "type": "object"}
        ),

        Tool(
            name="post_v1_knowledge_models_internal_documents_chunks",
            description="POST: Create new internal chunk",
            inputSchema={"properties": {"document_id": {"type": "string"}, "knowledge_model_id": {"type": "string"}}, "required": ["document_id", "knowledge_model_id"], "type": "object"}
        ),

        Tool(
            name="get_v1_knowledge_models_internal_documents_chunks",
            description="GET: List internal chunks",
            inputSchema={"properties": {"document_id": {"type": "string"}, "knowledge_model_id": {"type": "string"}, "limit": {"type": "string"}, "offset": {"type": "string"}}, "required": ["document_id", "knowledge_model_id"], "type": "object"}
        ),

        Tool(
            name="post_v1_knowledge_models_internal_documents_chunks_batch",
            description="POST: Batch create internal chunks",
            inputSchema={"properties": {"document_id": {"type": "string"}, "knowledge_model_id": {"type": "string"}}, "required": ["document_id", "knowledge_model_id"], "type": "object"}
        ),

        Tool(
            name="get_v1_knowledge_models_internal_documents_chunks",
            description="Get internal chunk",
            inputSchema={"properties": {"chunk_id": {"type": "string"}, "document_id": {"type": "string"}, "knowledge_model_id": {"type": "string"}}, "required": ["chunk_id", "document_id", "knowledge_model_id"], "type": "object"}
        ),

        Tool(
            name="patch_v1_knowledge_models_internal_documents_chunks",
            description="PATCH: Update internal chunk",
            inputSchema={"properties": {"chunk_id": {"type": "string"}, "document_id": {"type": "string"}, "knowledge_model_id": {"type": "string"}}, "required": ["chunk_id", "document_id", "knowledge_model_id"], "type": "object"}
        ),

        Tool(
            name="delete_v1_knowledge_models_internal_documents_chunks",
            description="Delete internal chunk",
            inputSchema={"properties": {"chunk_id": {"type": "string"}, "document_id": {"type": "string"}, "knowledge_model_id": {"type": "string"}}, "required": ["chunk_id", "document_id", "knowledge_model_id"], "type": "object"}
        ),

        Tool(
            name="patch_v1_knowledge_models_widget",
            description="Patch knowledge model widget settings",
            inputSchema={"properties": {"knowledge_model_id": {"type": "string"}}, "required": ["knowledge_model_id"], "type": "object"}
        ),

        Tool(
            name="get_v1_knowledge_models_chunks",
            description="GET: List document chunks",
            inputSchema={"properties": {"content_type": {"description": "Filter by chunk content type", "type": "string"}, "document_id": {"description": "Filter by specific document ID", "type": "string"}, "document_type": {"description": "Filter by document type", "type": "string"}, "knowledge_model_id": {"type": "string"}, "limit": {"type": "string"}, "offset": {"type": "string"}, "sort": {"description": "Sort by field, e.g. \u0027chunk_index\u0027", "type": "string"}}, "required": ["knowledge_model_id"], "type": "object"}
        ),

        Tool(
            name="post_v1_knowledge_models_chunks_search",
            description="POST: Search for raw text chunks",
            inputSchema={"properties": {"knowledge_model_id": {"type": "string"}}, "required": ["knowledge_model_id"], "type": "object"}
        ),

        Tool(
            name="post_v1_knowledge_models_videos_import",
            description="POST: Add video document into Model",
            inputSchema={"properties": {"knowledge_model_id": {"type": "string"}}, "required": ["knowledge_model_id"], "type": "object"}
        ),

        Tool(
            name="get_v1_knowledge_models_videos",
            description="GET: List videos in the knowledge model",
            inputSchema={"properties": {"knowledge_model_id": {"type": "string"}, "limit": {"type": "string"}, "offset": {"type": "string"}}, "required": ["knowledge_model_id"], "type": "object"}
        ),

        Tool(
            name="patch_v1_knowledge_models_videos",
            description="Patch video document",
            inputSchema={"properties": {"document_external_id": {"type": "string"}, "knowledge_model_id": {"type": "string"}}, "required": ["document_external_id", "knowledge_model_id"], "type": "object"}
        ),

        Tool(
            name="delete_v1_knowledge_models_videos",
            description="Delete video document",
            inputSchema={"properties": {"document_external_id": {"type": "string"}, "knowledge_model_id": {"type": "string"}}, "required": ["document_external_id", "knowledge_model_id"], "type": "object"}
        ),

        Tool(
            name="post_v1_knowledge_models_chat_completions",
            description="POST: Generates text responses based on incoming messages.",
            inputSchema={"properties": {"X-KM-Extension": {"type": "string"}, "extension": {"type": "string"}, "knowledge_model_id": {"type": "string"}}, "required": ["knowledge_model_id", "extension"], "type": "object"}
        ),

        Tool(
            name="post_v1_knowledge_models_chat_completions",
            description="POST: Generates text responses based on incoming messages.",
            inputSchema={"properties": {"X-KM-Extension": {"type": "string"}, "extension": {"type": "string"}, "knowledge_model_id": {"type": "string"}}, "required": ["knowledge_model_id"], "type": "object"}
        ),

        Tool(
            name="post_v1_knowledge_models_tools_translation",
            description="POST: English translation tool.",
            inputSchema={"properties": {"knowledge_model_id": {"type": "string"}}, "required": ["knowledge_model_id"], "type": "object"}
        ),

    ]
    return tools

@server.list_resources()
async def handle_list_resources() -> List[Resource]:
    """List available resources."""
    resources = [

        Resource(
            uri="api:///alive",
            name="get_alive_resource",
            description="Access to respond if authorized, do not respond on any error",
            mimeType="application/json"
        ),

        Resource(
            uri="api:///v1/knowledge-models",
            name="get_v1_knowledge_models_resource",
            description="Access to list knowledge models",
            mimeType="application/json"
        ),

        Resource(
            uri="api:///v1/knowledge-models/{knowledge_model_id}",
            name="get_v1_knowledge_models_resource",
            description="Access to get knowledge model",
            mimeType="application/json"
        ),

        Resource(
            uri="api:///v1/knowledge-models/{knowledge_model_id}/settings",
            name="get_v1_knowledge_models_settings_resource",
            description="Access to get knowledge model settings",
            mimeType="application/json"
        ),

        Resource(
            uri="api:///v1/knowledge-models/{knowledge_model_id}/chat-sessions",
            name="get_v1_knowledge_models_chat_sessions_resource",
            description="Access to get all chat sessions for given knowledge model",
            mimeType="application/json"
        ),

        Resource(
            uri="api:///v1/knowledge-models/{knowledge_model_id}/chat-sessions/{chat_session_id}",
            name="get_v1_knowledge_models_chat_sessions_resource",
            description="Access to get chat session",
            mimeType="application/json"
        ),

        Resource(
            uri="api:///v1/knowledge-models/{knowledge_model_id}/files/{file_id}",
            name="get_v1_knowledge_models_files_resource",
            description="Access to download a file from a knowledge model",
            mimeType="application/json"
        ),

        Resource(
            uri="api:///v1/knowledge-models/{knowledge_model_id}/files/{file_id}/metadata",
            name="get_v1_knowledge_models_files_metadata_resource",
            description="Access to returns metadata of the file",
            mimeType="application/json"
        ),

        Resource(
            uri="api:///v1/knowledge-models/{knowledge_model_id}/internal-documents/{document_id}",
            name="get_v1_knowledge_models_internal_documents_resource",
            description="Access to get internal document",
            mimeType="application/json"
        ),

        Resource(
            uri="api:///v1/knowledge-models/{knowledge_model_id}/widget",
            name="get_v1_knowledge_models_widget_resource",
            description="Access to get the knowledge model widget settings",
            mimeType="application/json"
        ),

        Resource(
            uri="api:///v1/knowledge-models/{knowledge_model_id}/videos/{document_external_id}/transcription",
            name="get_v1_knowledge_models_videos_transcription_resource",
            description="Access to get video transcription",
            mimeType="application/json"
        ),

        Resource(
            uri="api:///v1/knowledge-models/{knowledge_model_id}/videos/{document_external_id}",
            name="get_v1_knowledge_models_videos_resource",
            description="Access to get video document",
            mimeType="application/json"
        ),

        Resource(
            uri="api:///v1/language_models",
            name="get_v1_language_models_resource",
            description="Access to list language models",
            mimeType="application/json"
        ),

    ]
    return resources

# Tool handlers

@server.call_tool()
async def handle_post_v1_knowledge_models(name: str, arguments: Dict[str, Any]) -> List[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    """Handle post_v1_knowledge_models tool."""
    if name != "post_v1_knowledge_models":
        raise ValueError(f"Unknown tool: {name}")
    
    try:
        result = await tool_post_v1_knowledge_models(arguments)
        return [TextContent(type="text", text=str(result))]
    except Exception as e:
        logger.error(f"Error in post_v1_knowledge_models: {e}")
        return [TextContent(type="text", text=f"Error: {str(e)}")]


@server.call_tool()
async def handle_delete_v1_knowledge_models(name: str, arguments: Dict[str, Any]) -> List[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    """Handle delete_v1_knowledge_models tool."""
    if name != "delete_v1_knowledge_models":
        raise ValueError(f"Unknown tool: {name}")
    
    try:
        result = await tool_delete_v1_knowledge_models(arguments)
        return [TextContent(type="text", text=str(result))]
    except Exception as e:
        logger.error(f"Error in delete_v1_knowledge_models: {e}")
        return [TextContent(type="text", text=f"Error: {str(e)}")]


@server.call_tool()
async def handle_patch_v1_knowledge_models(name: str, arguments: Dict[str, Any]) -> List[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    """Handle patch_v1_knowledge_models tool."""
    if name != "patch_v1_knowledge_models":
        raise ValueError(f"Unknown tool: {name}")
    
    try:
        result = await tool_patch_v1_knowledge_models(arguments)
        return [TextContent(type="text", text=str(result))]
    except Exception as e:
        logger.error(f"Error in patch_v1_knowledge_models: {e}")
        return [TextContent(type="text", text=f"Error: {str(e)}")]


@server.call_tool()
async def handle_patch_v1_knowledge_models_settings(name: str, arguments: Dict[str, Any]) -> List[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    """Handle patch_v1_knowledge_models_settings tool."""
    if name != "patch_v1_knowledge_models_settings":
        raise ValueError(f"Unknown tool: {name}")
    
    try:
        result = await tool_patch_v1_knowledge_models_settings(arguments)
        return [TextContent(type="text", text=str(result))]
    except Exception as e:
        logger.error(f"Error in patch_v1_knowledge_models_settings: {e}")
        return [TextContent(type="text", text=f"Error: {str(e)}")]


@server.call_tool()
async def handle_post_v1_knowledge_models_chat_sessions(name: str, arguments: Dict[str, Any]) -> List[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    """Handle post_v1_knowledge_models_chat_sessions tool."""
    if name != "post_v1_knowledge_models_chat_sessions":
        raise ValueError(f"Unknown tool: {name}")
    
    try:
        result = await tool_post_v1_knowledge_models_chat_sessions(arguments)
        return [TextContent(type="text", text=str(result))]
    except Exception as e:
        logger.error(f"Error in post_v1_knowledge_models_chat_sessions: {e}")
        return [TextContent(type="text", text=f"Error: {str(e)}")]


@server.call_tool()
async def handle_delete_v1_knowledge_models_chat_sessions(name: str, arguments: Dict[str, Any]) -> List[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    """Handle delete_v1_knowledge_models_chat_sessions tool."""
    if name != "delete_v1_knowledge_models_chat_sessions":
        raise ValueError(f"Unknown tool: {name}")
    
    try:
        result = await tool_delete_v1_knowledge_models_chat_sessions(arguments)
        return [TextContent(type="text", text=str(result))]
    except Exception as e:
        logger.error(f"Error in delete_v1_knowledge_models_chat_sessions: {e}")
        return [TextContent(type="text", text=f"Error: {str(e)}")]


@server.call_tool()
async def handle_patch_v1_knowledge_models_chat_sessions(name: str, arguments: Dict[str, Any]) -> List[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    """Handle patch_v1_knowledge_models_chat_sessions tool."""
    if name != "patch_v1_knowledge_models_chat_sessions":
        raise ValueError(f"Unknown tool: {name}")
    
    try:
        result = await tool_patch_v1_knowledge_models_chat_sessions(arguments)
        return [TextContent(type="text", text=str(result))]
    except Exception as e:
        logger.error(f"Error in patch_v1_knowledge_models_chat_sessions: {e}")
        return [TextContent(type="text", text=f"Error: {str(e)}")]


@server.call_tool()
async def handle_post_v1_knowledge_models_chat_sessions_messages(name: str, arguments: Dict[str, Any]) -> List[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    """Handle post_v1_knowledge_models_chat_sessions_messages tool."""
    if name != "post_v1_knowledge_models_chat_sessions_messages":
        raise ValueError(f"Unknown tool: {name}")
    
    try:
        result = await tool_post_v1_knowledge_models_chat_sessions_messages(arguments)
        return [TextContent(type="text", text=str(result))]
    except Exception as e:
        logger.error(f"Error in post_v1_knowledge_models_chat_sessions_messages: {e}")
        return [TextContent(type="text", text=f"Error: {str(e)}")]


@server.call_tool()
async def handle_get_v1_knowledge_models_chat_sessions_messages(name: str, arguments: Dict[str, Any]) -> List[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    """Handle get_v1_knowledge_models_chat_sessions_messages tool."""
    if name != "get_v1_knowledge_models_chat_sessions_messages":
        raise ValueError(f"Unknown tool: {name}")
    
    try:
        result = await tool_get_v1_knowledge_models_chat_sessions_messages(arguments)
        return [TextContent(type="text", text=str(result))]
    except Exception as e:
        logger.error(f"Error in get_v1_knowledge_models_chat_sessions_messages: {e}")
        return [TextContent(type="text", text=f"Error: {str(e)}")]


@server.call_tool()
async def handle_get_v1_knowledge_models_chat_sessions_messages(name: str, arguments: Dict[str, Any]) -> List[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    """Handle get_v1_knowledge_models_chat_sessions_messages tool."""
    if name != "get_v1_knowledge_models_chat_sessions_messages":
        raise ValueError(f"Unknown tool: {name}")
    
    try:
        result = await tool_get_v1_knowledge_models_chat_sessions_messages(arguments)
        return [TextContent(type="text", text=str(result))]
    except Exception as e:
        logger.error(f"Error in get_v1_knowledge_models_chat_sessions_messages: {e}")
        return [TextContent(type="text", text=f"Error: {str(e)}")]


@server.call_tool()
async def handle_post_v1_knowledge_models_chat_sessions_messages_feedback(name: str, arguments: Dict[str, Any]) -> List[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    """Handle post_v1_knowledge_models_chat_sessions_messages_feedback tool."""
    if name != "post_v1_knowledge_models_chat_sessions_messages_feedback":
        raise ValueError(f"Unknown tool: {name}")
    
    try:
        result = await tool_post_v1_knowledge_models_chat_sessions_messages_feedback(arguments)
        return [TextContent(type="text", text=str(result))]
    except Exception as e:
        logger.error(f"Error in post_v1_knowledge_models_chat_sessions_messages_feedback: {e}")
        return [TextContent(type="text", text=f"Error: {str(e)}")]


@server.call_tool()
async def handle_get_v1_knowledge_models_files(name: str, arguments: Dict[str, Any]) -> List[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    """Handle get_v1_knowledge_models_files tool."""
    if name != "get_v1_knowledge_models_files":
        raise ValueError(f"Unknown tool: {name}")
    
    try:
        result = await tool_get_v1_knowledge_models_files(arguments)
        return [TextContent(type="text", text=str(result))]
    except Exception as e:
        logger.error(f"Error in get_v1_knowledge_models_files: {e}")
        return [TextContent(type="text", text=f"Error: {str(e)}")]


@server.call_tool()
async def handle_post_v1_knowledge_models_files(name: str, arguments: Dict[str, Any]) -> List[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    """Handle post_v1_knowledge_models_files tool."""
    if name != "post_v1_knowledge_models_files":
        raise ValueError(f"Unknown tool: {name}")
    
    try:
        result = await tool_post_v1_knowledge_models_files(arguments)
        return [TextContent(type="text", text=str(result))]
    except Exception as e:
        logger.error(f"Error in post_v1_knowledge_models_files: {e}")
        return [TextContent(type="text", text=f"Error: {str(e)}")]


@server.call_tool()
async def handle_delete_v1_knowledge_models_files(name: str, arguments: Dict[str, Any]) -> List[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    """Handle delete_v1_knowledge_models_files tool."""
    if name != "delete_v1_knowledge_models_files":
        raise ValueError(f"Unknown tool: {name}")
    
    try:
        result = await tool_delete_v1_knowledge_models_files(arguments)
        return [TextContent(type="text", text=str(result))]
    except Exception as e:
        logger.error(f"Error in delete_v1_knowledge_models_files: {e}")
        return [TextContent(type="text", text=f"Error: {str(e)}")]


@server.call_tool()
async def handle_patch_v1_knowledge_models_files_metadata(name: str, arguments: Dict[str, Any]) -> List[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    """Handle patch_v1_knowledge_models_files_metadata tool."""
    if name != "patch_v1_knowledge_models_files_metadata":
        raise ValueError(f"Unknown tool: {name}")
    
    try:
        result = await tool_patch_v1_knowledge_models_files_metadata(arguments)
        return [TextContent(type="text", text=str(result))]
    except Exception as e:
        logger.error(f"Error in patch_v1_knowledge_models_files_metadata: {e}")
        return [TextContent(type="text", text=f"Error: {str(e)}")]


@server.call_tool()
async def handle_post_v1_knowledge_models_internal_documents(name: str, arguments: Dict[str, Any]) -> List[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    """Handle post_v1_knowledge_models_internal_documents tool."""
    if name != "post_v1_knowledge_models_internal_documents":
        raise ValueError(f"Unknown tool: {name}")
    
    try:
        result = await tool_post_v1_knowledge_models_internal_documents(arguments)
        return [TextContent(type="text", text=str(result))]
    except Exception as e:
        logger.error(f"Error in post_v1_knowledge_models_internal_documents: {e}")
        return [TextContent(type="text", text=f"Error: {str(e)}")]


@server.call_tool()
async def handle_get_v1_knowledge_models_internal_documents(name: str, arguments: Dict[str, Any]) -> List[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    """Handle get_v1_knowledge_models_internal_documents tool."""
    if name != "get_v1_knowledge_models_internal_documents":
        raise ValueError(f"Unknown tool: {name}")
    
    try:
        result = await tool_get_v1_knowledge_models_internal_documents(arguments)
        return [TextContent(type="text", text=str(result))]
    except Exception as e:
        logger.error(f"Error in get_v1_knowledge_models_internal_documents: {e}")
        return [TextContent(type="text", text=f"Error: {str(e)}")]


@server.call_tool()
async def handle_patch_v1_knowledge_models_internal_documents(name: str, arguments: Dict[str, Any]) -> List[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    """Handle patch_v1_knowledge_models_internal_documents tool."""
    if name != "patch_v1_knowledge_models_internal_documents":
        raise ValueError(f"Unknown tool: {name}")
    
    try:
        result = await tool_patch_v1_knowledge_models_internal_documents(arguments)
        return [TextContent(type="text", text=str(result))]
    except Exception as e:
        logger.error(f"Error in patch_v1_knowledge_models_internal_documents: {e}")
        return [TextContent(type="text", text=f"Error: {str(e)}")]


@server.call_tool()
async def handle_delete_v1_knowledge_models_internal_documents(name: str, arguments: Dict[str, Any]) -> List[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    """Handle delete_v1_knowledge_models_internal_documents tool."""
    if name != "delete_v1_knowledge_models_internal_documents":
        raise ValueError(f"Unknown tool: {name}")
    
    try:
        result = await tool_delete_v1_knowledge_models_internal_documents(arguments)
        return [TextContent(type="text", text=str(result))]
    except Exception as e:
        logger.error(f"Error in delete_v1_knowledge_models_internal_documents: {e}")
        return [TextContent(type="text", text=f"Error: {str(e)}")]


@server.call_tool()
async def handle_post_v1_knowledge_models_internal_documents_chunks(name: str, arguments: Dict[str, Any]) -> List[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    """Handle post_v1_knowledge_models_internal_documents_chunks tool."""
    if name != "post_v1_knowledge_models_internal_documents_chunks":
        raise ValueError(f"Unknown tool: {name}")
    
    try:
        result = await tool_post_v1_knowledge_models_internal_documents_chunks(arguments)
        return [TextContent(type="text", text=str(result))]
    except Exception as e:
        logger.error(f"Error in post_v1_knowledge_models_internal_documents_chunks: {e}")
        return [TextContent(type="text", text=f"Error: {str(e)}")]


@server.call_tool()
async def handle_get_v1_knowledge_models_internal_documents_chunks(name: str, arguments: Dict[str, Any]) -> List[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    """Handle get_v1_knowledge_models_internal_documents_chunks tool."""
    if name != "get_v1_knowledge_models_internal_documents_chunks":
        raise ValueError(f"Unknown tool: {name}")
    
    try:
        result = await tool_get_v1_knowledge_models_internal_documents_chunks(arguments)
        return [TextContent(type="text", text=str(result))]
    except Exception as e:
        logger.error(f"Error in get_v1_knowledge_models_internal_documents_chunks: {e}")
        return [TextContent(type="text", text=f"Error: {str(e)}")]


@server.call_tool()
async def handle_post_v1_knowledge_models_internal_documents_chunks_batch(name: str, arguments: Dict[str, Any]) -> List[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    """Handle post_v1_knowledge_models_internal_documents_chunks_batch tool."""
    if name != "post_v1_knowledge_models_internal_documents_chunks_batch":
        raise ValueError(f"Unknown tool: {name}")
    
    try:
        result = await tool_post_v1_knowledge_models_internal_documents_chunks_batch(arguments)
        return [TextContent(type="text", text=str(result))]
    except Exception as e:
        logger.error(f"Error in post_v1_knowledge_models_internal_documents_chunks_batch: {e}")
        return [TextContent(type="text", text=f"Error: {str(e)}")]


@server.call_tool()
async def handle_get_v1_knowledge_models_internal_documents_chunks(name: str, arguments: Dict[str, Any]) -> List[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    """Handle get_v1_knowledge_models_internal_documents_chunks tool."""
    if name != "get_v1_knowledge_models_internal_documents_chunks":
        raise ValueError(f"Unknown tool: {name}")
    
    try:
        result = await tool_get_v1_knowledge_models_internal_documents_chunks(arguments)
        return [TextContent(type="text", text=str(result))]
    except Exception as e:
        logger.error(f"Error in get_v1_knowledge_models_internal_documents_chunks: {e}")
        return [TextContent(type="text", text=f"Error: {str(e)}")]


@server.call_tool()
async def handle_patch_v1_knowledge_models_internal_documents_chunks(name: str, arguments: Dict[str, Any]) -> List[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    """Handle patch_v1_knowledge_models_internal_documents_chunks tool."""
    if name != "patch_v1_knowledge_models_internal_documents_chunks":
        raise ValueError(f"Unknown tool: {name}")
    
    try:
        result = await tool_patch_v1_knowledge_models_internal_documents_chunks(arguments)
        return [TextContent(type="text", text=str(result))]
    except Exception as e:
        logger.error(f"Error in patch_v1_knowledge_models_internal_documents_chunks: {e}")
        return [TextContent(type="text", text=f"Error: {str(e)}")]


@server.call_tool()
async def handle_delete_v1_knowledge_models_internal_documents_chunks(name: str, arguments: Dict[str, Any]) -> List[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    """Handle delete_v1_knowledge_models_internal_documents_chunks tool."""
    if name != "delete_v1_knowledge_models_internal_documents_chunks":
        raise ValueError(f"Unknown tool: {name}")
    
    try:
        result = await tool_delete_v1_knowledge_models_internal_documents_chunks(arguments)
        return [TextContent(type="text", text=str(result))]
    except Exception as e:
        logger.error(f"Error in delete_v1_knowledge_models_internal_documents_chunks: {e}")
        return [TextContent(type="text", text=f"Error: {str(e)}")]


@server.call_tool()
async def handle_patch_v1_knowledge_models_widget(name: str, arguments: Dict[str, Any]) -> List[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    """Handle patch_v1_knowledge_models_widget tool."""
    if name != "patch_v1_knowledge_models_widget":
        raise ValueError(f"Unknown tool: {name}")
    
    try:
        result = await tool_patch_v1_knowledge_models_widget(arguments)
        return [TextContent(type="text", text=str(result))]
    except Exception as e:
        logger.error(f"Error in patch_v1_knowledge_models_widget: {e}")
        return [TextContent(type="text", text=f"Error: {str(e)}")]


@server.call_tool()
async def handle_get_v1_knowledge_models_chunks(name: str, arguments: Dict[str, Any]) -> List[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    """Handle get_v1_knowledge_models_chunks tool."""
    if name != "get_v1_knowledge_models_chunks":
        raise ValueError(f"Unknown tool: {name}")
    
    try:
        result = await tool_get_v1_knowledge_models_chunks(arguments)
        return [TextContent(type="text", text=str(result))]
    except Exception as e:
        logger.error(f"Error in get_v1_knowledge_models_chunks: {e}")
        return [TextContent(type="text", text=f"Error: {str(e)}")]


@server.call_tool()
async def handle_post_v1_knowledge_models_chunks_search(name: str, arguments: Dict[str, Any]) -> List[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    """Handle post_v1_knowledge_models_chunks_search tool."""
    if name != "post_v1_knowledge_models_chunks_search":
        raise ValueError(f"Unknown tool: {name}")
    
    try:
        result = await tool_post_v1_knowledge_models_chunks_search(arguments)
        return [TextContent(type="text", text=str(result))]
    except Exception as e:
        logger.error(f"Error in post_v1_knowledge_models_chunks_search: {e}")
        return [TextContent(type="text", text=f"Error: {str(e)}")]


@server.call_tool()
async def handle_post_v1_knowledge_models_videos_import(name: str, arguments: Dict[str, Any]) -> List[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    """Handle post_v1_knowledge_models_videos_import tool."""
    if name != "post_v1_knowledge_models_videos_import":
        raise ValueError(f"Unknown tool: {name}")
    
    try:
        result = await tool_post_v1_knowledge_models_videos_import(arguments)
        return [TextContent(type="text", text=str(result))]
    except Exception as e:
        logger.error(f"Error in post_v1_knowledge_models_videos_import: {e}")
        return [TextContent(type="text", text=f"Error: {str(e)}")]


@server.call_tool()
async def handle_get_v1_knowledge_models_videos(name: str, arguments: Dict[str, Any]) -> List[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    """Handle get_v1_knowledge_models_videos tool."""
    if name != "get_v1_knowledge_models_videos":
        raise ValueError(f"Unknown tool: {name}")
    
    try:
        result = await tool_get_v1_knowledge_models_videos(arguments)
        return [TextContent(type="text", text=str(result))]
    except Exception as e:
        logger.error(f"Error in get_v1_knowledge_models_videos: {e}")
        return [TextContent(type="text", text=f"Error: {str(e)}")]


@server.call_tool()
async def handle_patch_v1_knowledge_models_videos(name: str, arguments: Dict[str, Any]) -> List[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    """Handle patch_v1_knowledge_models_videos tool."""
    if name != "patch_v1_knowledge_models_videos":
        raise ValueError(f"Unknown tool: {name}")
    
    try:
        result = await tool_patch_v1_knowledge_models_videos(arguments)
        return [TextContent(type="text", text=str(result))]
    except Exception as e:
        logger.error(f"Error in patch_v1_knowledge_models_videos: {e}")
        return [TextContent(type="text", text=f"Error: {str(e)}")]


@server.call_tool()
async def handle_delete_v1_knowledge_models_videos(name: str, arguments: Dict[str, Any]) -> List[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    """Handle delete_v1_knowledge_models_videos tool."""
    if name != "delete_v1_knowledge_models_videos":
        raise ValueError(f"Unknown tool: {name}")
    
    try:
        result = await tool_delete_v1_knowledge_models_videos(arguments)
        return [TextContent(type="text", text=str(result))]
    except Exception as e:
        logger.error(f"Error in delete_v1_knowledge_models_videos: {e}")
        return [TextContent(type="text", text=f"Error: {str(e)}")]


@server.call_tool()
async def handle_post_v1_knowledge_models_chat_completions(name: str, arguments: Dict[str, Any]) -> List[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    """Handle post_v1_knowledge_models_chat_completions tool."""
    if name != "post_v1_knowledge_models_chat_completions":
        raise ValueError(f"Unknown tool: {name}")
    
    try:
        result = await tool_post_v1_knowledge_models_chat_completions(arguments)
        return [TextContent(type="text", text=str(result))]
    except Exception as e:
        logger.error(f"Error in post_v1_knowledge_models_chat_completions: {e}")
        return [TextContent(type="text", text=f"Error: {str(e)}")]


@server.call_tool()
async def handle_post_v1_knowledge_models_chat_completions(name: str, arguments: Dict[str, Any]) -> List[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    """Handle post_v1_knowledge_models_chat_completions tool."""
    if name != "post_v1_knowledge_models_chat_completions":
        raise ValueError(f"Unknown tool: {name}")
    
    try:
        result = await tool_post_v1_knowledge_models_chat_completions(arguments)
        return [TextContent(type="text", text=str(result))]
    except Exception as e:
        logger.error(f"Error in post_v1_knowledge_models_chat_completions: {e}")
        return [TextContent(type="text", text=f"Error: {str(e)}")]


@server.call_tool()
async def handle_post_v1_knowledge_models_tools_translation(name: str, arguments: Dict[str, Any]) -> List[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    """Handle post_v1_knowledge_models_tools_translation tool."""
    if name != "post_v1_knowledge_models_tools_translation":
        raise ValueError(f"Unknown tool: {name}")
    
    try:
        result = await tool_post_v1_knowledge_models_tools_translation(arguments)
        return [TextContent(type="text", text=str(result))]
    except Exception as e:
        logger.error(f"Error in post_v1_knowledge_models_tools_translation: {e}")
        return [TextContent(type="text", text=f"Error: {str(e)}")]



# Resource handlers

@server.read_resource()
async def handle_get_alive_resource(uri: str) -> str:
    """Handle get_alive_resource resource."""
    if uri != "api:///alive":
        raise ValueError(f"Unknown resource: {uri}")
    
    try:
        result = await resource_get_alive_resource(uri)
        return str(result)
    except Exception as e:
        logger.error(f"Error reading get_alive_resource: {e}")
        raise


@server.read_resource()
async def handle_get_v1_knowledge_models_resource(uri: str) -> str:
    """Handle get_v1_knowledge_models_resource resource."""
    if uri != "api:///v1/knowledge-models":
        raise ValueError(f"Unknown resource: {uri}")
    
    try:
        result = await resource_get_v1_knowledge_models_resource(uri)
        return str(result)
    except Exception as e:
        logger.error(f"Error reading get_v1_knowledge_models_resource: {e}")
        raise


@server.read_resource()
async def handle_get_v1_knowledge_models_resource(uri: str) -> str:
    """Handle get_v1_knowledge_models_resource resource."""
    if uri != "api:///v1/knowledge-models/{knowledge_model_id}":
        raise ValueError(f"Unknown resource: {uri}")
    
    try:
        result = await resource_get_v1_knowledge_models_resource(uri)
        return str(result)
    except Exception as e:
        logger.error(f"Error reading get_v1_knowledge_models_resource: {e}")
        raise


@server.read_resource()
async def handle_get_v1_knowledge_models_settings_resource(uri: str) -> str:
    """Handle get_v1_knowledge_models_settings_resource resource."""
    if uri != "api:///v1/knowledge-models/{knowledge_model_id}/settings":
        raise ValueError(f"Unknown resource: {uri}")
    
    try:
        result = await resource_get_v1_knowledge_models_settings_resource(uri)
        return str(result)
    except Exception as e:
        logger.error(f"Error reading get_v1_knowledge_models_settings_resource: {e}")
        raise


@server.read_resource()
async def handle_get_v1_knowledge_models_chat_sessions_resource(uri: str) -> str:
    """Handle get_v1_knowledge_models_chat_sessions_resource resource."""
    if uri != "api:///v1/knowledge-models/{knowledge_model_id}/chat-sessions":
        raise ValueError(f"Unknown resource: {uri}")
    
    try:
        result = await resource_get_v1_knowledge_models_chat_sessions_resource(uri)
        return str(result)
    except Exception as e:
        logger.error(f"Error reading get_v1_knowledge_models_chat_sessions_resource: {e}")
        raise


@server.read_resource()
async def handle_get_v1_knowledge_models_chat_sessions_resource(uri: str) -> str:
    """Handle get_v1_knowledge_models_chat_sessions_resource resource."""
    if uri != "api:///v1/knowledge-models/{knowledge_model_id}/chat-sessions/{chat_session_id}":
        raise ValueError(f"Unknown resource: {uri}")
    
    try:
        result = await resource_get_v1_knowledge_models_chat_sessions_resource(uri)
        return str(result)
    except Exception as e:
        logger.error(f"Error reading get_v1_knowledge_models_chat_sessions_resource: {e}")
        raise


@server.read_resource()
async def handle_get_v1_knowledge_models_files_resource(uri: str) -> str:
    """Handle get_v1_knowledge_models_files_resource resource."""
    if uri != "api:///v1/knowledge-models/{knowledge_model_id}/files/{file_id}":
        raise ValueError(f"Unknown resource: {uri}")
    
    try:
        result = await resource_get_v1_knowledge_models_files_resource(uri)
        return str(result)
    except Exception as e:
        logger.error(f"Error reading get_v1_knowledge_models_files_resource: {e}")
        raise


@server.read_resource()
async def handle_get_v1_knowledge_models_files_metadata_resource(uri: str) -> str:
    """Handle get_v1_knowledge_models_files_metadata_resource resource."""
    if uri != "api:///v1/knowledge-models/{knowledge_model_id}/files/{file_id}/metadata":
        raise ValueError(f"Unknown resource: {uri}")
    
    try:
        result = await resource_get_v1_knowledge_models_files_metadata_resource(uri)
        return str(result)
    except Exception as e:
        logger.error(f"Error reading get_v1_knowledge_models_files_metadata_resource: {e}")
        raise


@server.read_resource()
async def handle_get_v1_knowledge_models_internal_documents_resource(uri: str) -> str:
    """Handle get_v1_knowledge_models_internal_documents_resource resource."""
    if uri != "api:///v1/knowledge-models/{knowledge_model_id}/internal-documents/{document_id}":
        raise ValueError(f"Unknown resource: {uri}")
    
    try:
        result = await resource_get_v1_knowledge_models_internal_documents_resource(uri)
        return str(result)
    except Exception as e:
        logger.error(f"Error reading get_v1_knowledge_models_internal_documents_resource: {e}")
        raise


@server.read_resource()
async def handle_get_v1_knowledge_models_widget_resource(uri: str) -> str:
    """Handle get_v1_knowledge_models_widget_resource resource."""
    if uri != "api:///v1/knowledge-models/{knowledge_model_id}/widget":
        raise ValueError(f"Unknown resource: {uri}")
    
    try:
        result = await resource_get_v1_knowledge_models_widget_resource(uri)
        return str(result)
    except Exception as e:
        logger.error(f"Error reading get_v1_knowledge_models_widget_resource: {e}")
        raise


@server.read_resource()
async def handle_get_v1_knowledge_models_videos_transcription_resource(uri: str) -> str:
    """Handle get_v1_knowledge_models_videos_transcription_resource resource."""
    if uri != "api:///v1/knowledge-models/{knowledge_model_id}/videos/{document_external_id}/transcription":
        raise ValueError(f"Unknown resource: {uri}")
    
    try:
        result = await resource_get_v1_knowledge_models_videos_transcription_resource(uri)
        return str(result)
    except Exception as e:
        logger.error(f"Error reading get_v1_knowledge_models_videos_transcription_resource: {e}")
        raise


@server.read_resource()
async def handle_get_v1_knowledge_models_videos_resource(uri: str) -> str:
    """Handle get_v1_knowledge_models_videos_resource resource."""
    if uri != "api:///v1/knowledge-models/{knowledge_model_id}/videos/{document_external_id}":
        raise ValueError(f"Unknown resource: {uri}")
    
    try:
        result = await resource_get_v1_knowledge_models_videos_resource(uri)
        return str(result)
    except Exception as e:
        logger.error(f"Error reading get_v1_knowledge_models_videos_resource: {e}")
        raise


@server.read_resource()
async def handle_get_v1_language_models_resource(uri: str) -> str:
    """Handle get_v1_language_models_resource resource."""
    if uri != "api:///v1/language_models":
        raise ValueError(f"Unknown resource: {uri}")
    
    try:
        result = await resource_get_v1_language_models_resource(uri)
        return str(result)
    except Exception as e:
        logger.error(f"Error reading get_v1_language_models_resource: {e}")
        raise



async def main():
    """Main entry point."""
    # Load configuration
    config = load_config()
    
    # Validate API key
    api_key = os.getenv("API_KEY")
    if not api_key:
        logger.error("API_KEY environment variable is required")
        sys.exit(1)
    
    logger.info(f"Starting {SERVER_NAME} v{SERVER_VERSION}")
    logger.info(f"API Base URL: https://constructor.app/api/platform-kmapi")
    logger.info(f"Tools: 35")
    logger.info(f"Resources: 13")
    
    # Run the server
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())