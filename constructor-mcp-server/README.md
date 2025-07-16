# constructor-knowledge-api

MCP Server for ConstructorKnowledgeModel



## Overview

This MCP server provides access to the ConstructorKnowledgeModel API (version 0.1.0) through the Model Context Protocol. It exposes 35 tools and 13 resources for AI agents to interact with the API.

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up environment variables:
```bash
export API_KEY="your-api-key-here"
```

## Usage

### Running the Server

```bash
python server.py
```

### Configuration

The server can be configured through environment variables:

- `API_KEY`: Required. Your API key for authentication.
- `LOG_LEVEL`: Optional. Logging level (default: INFO).

## Available Tools


### post_v1_knowledge_models

POST: Creates a new knowledge model.

**Method:** POST  
**Path:** /v1/knowledge-models

**Input Schema:**
```json
{
  "properties": {},
  "required": [],
  "type": "object"
}
```


### delete_v1_knowledge_models

Delete knowledge model

**Method:** DELETE  
**Path:** /v1/knowledge-models/{knowledge_model_id}

**Input Schema:**
```json
{
  "properties": {
    "knowledge_model_id": {
      "type": "string"
    }
  },
  "required": [
    "knowledge_model_id"
  ],
  "type": "object"
}
```


### patch_v1_knowledge_models

PATCH: Update knowledge model

**Method:** PATCH  
**Path:** /v1/knowledge-models/{knowledge_model_id}

**Input Schema:**
```json
{
  "properties": {
    "knowledge_model_id": {
      "type": "string"
    }
  },
  "required": [
    "knowledge_model_id"
  ],
  "type": "object"
}
```


### patch_v1_knowledge_models_settings

PATCH: Update knowledge model settings

**Method:** PATCH  
**Path:** /v1/knowledge-models/{knowledge_model_id}/settings

**Input Schema:**
```json
{
  "properties": {
    "knowledge_model_id": {
      "type": "string"
    }
  },
  "required": [
    "knowledge_model_id"
  ],
  "type": "object"
}
```


### post_v1_knowledge_models_chat_sessions

POST: Create new chat session via API

**Method:** POST  
**Path:** /v1/knowledge-models/{knowledge_model_id}/chat-sessions

**Input Schema:**
```json
{
  "properties": {
    "knowledge_model_id": {
      "type": "string"
    }
  },
  "required": [
    "knowledge_model_id"
  ],
  "type": "object"
}
```


### delete_v1_knowledge_models_chat_sessions

Delete chat session

**Method:** DELETE  
**Path:** /v1/knowledge-models/{knowledge_model_id}/chat-sessions/{chat_session_id}

**Input Schema:**
```json
{
  "properties": {
    "chat_session_id": {
      "type": "string"
    },
    "knowledge_model_id": {
      "type": "string"
    }
  },
  "required": [
    "chat_session_id",
    "knowledge_model_id"
  ],
  "type": "object"
}
```


### patch_v1_knowledge_models_chat_sessions

Patch chat session

**Method:** PATCH  
**Path:** /v1/knowledge-models/{knowledge_model_id}/chat-sessions/{chat_session_id}

**Input Schema:**
```json
{
  "properties": {
    "chat_session_id": {
      "type": "string"
    },
    "knowledge_model_id": {
      "type": "string"
    }
  },
  "required": [
    "chat_session_id",
    "knowledge_model_id"
  ],
  "type": "object"
}
```


### post_v1_knowledge_models_chat_sessions_messages

POST: Create new chat message

**Method:** POST  
**Path:** /v1/knowledge-models/{knowledge_model_id}/chat-sessions/{chat_session_id}/messages

**Input Schema:**
```json
{
  "properties": {
    "chat_session_id": {
      "type": "string"
    },
    "knowledge_model_id": {
      "type": "string"
    }
  },
  "required": [
    "knowledge_model_id",
    "chat_session_id"
  ],
  "type": "object"
}
```


### get_v1_knowledge_models_chat_sessions_messages

Get all messages from chat session

**Method:** GET  
**Path:** /v1/knowledge-models/{knowledge_model_id}/chat-sessions/{chat_session_id}/messages

**Input Schema:**
```json
{
  "properties": {
    "chat_session_id": {
      "type": "string"
    },
    "knowledge_model_id": {
      "type": "string"
    },
    "limit": {
      "type": "string"
    },
    "offset": {
      "type": "string"
    }
  },
  "required": [
    "knowledge_model_id",
    "chat_session_id"
  ],
  "type": "object"
}
```


### get_v1_knowledge_models_chat_sessions_messages

Get chat message

**Method:** GET  
**Path:** /v1/knowledge-models/{knowledge_model_id}/chat-sessions/{chat_session_id}/messages/{message_id}

**Input Schema:**
```json
{
  "properties": {
    "chat_session_id": {
      "type": "string"
    },
    "knowledge_model_id": {
      "type": "string"
    },
    "message_id": {
      "type": "string"
    }
  },
  "required": [
    "knowledge_model_id",
    "chat_session_id",
    "message_id"
  ],
  "type": "object"
}
```


### post_v1_knowledge_models_chat_sessions_messages_feedback

POST: Set feedback on bot message

**Method:** POST  
**Path:** /v1/knowledge-models/{knowledge_model_id}/chat-sessions/{chat_session_id}/messages/{message_id}/feedback

**Input Schema:**
```json
{
  "properties": {
    "chat_session_id": {
      "type": "string"
    },
    "knowledge_model_id": {
      "type": "string"
    },
    "message_id": {
      "type": "string"
    }
  },
  "required": [
    "knowledge_model_id",
    "chat_session_id",
    "message_id"
  ],
  "type": "object"
}
```


### get_v1_knowledge_models_files

GET: List files of the knowledge model

**Method:** GET  
**Path:** /v1/knowledge-models/{knowledge_model_id}/files

**Input Schema:**
```json
{
  "properties": {
    "knowledge_model_id": {
      "type": "string"
    },
    "limit": {
      "type": "string"
    },
    "offset": {
      "type": "string"
    }
  },
  "required": [
    "knowledge_model_id"
  ],
  "type": "object"
}
```


### post_v1_knowledge_models_files

POST: Upload a file to the knowledge model

**Method:** POST  
**Path:** /v1/knowledge-models/{knowledge_model_id}/files

**Input Schema:**
```json
{
  "properties": {
    "knowledge_model_id": {
      "type": "string"
    }
  },
  "required": [
    "knowledge_model_id"
  ],
  "type": "object"
}
```


### delete_v1_knowledge_models_files

Delete a file from a knowledge model

**Method:** DELETE  
**Path:** /v1/knowledge-models/{knowledge_model_id}/files/{file_id}

**Input Schema:**
```json
{
  "properties": {
    "file_id": {
      "type": "string"
    },
    "knowledge_model_id": {
      "type": "string"
    }
  },
  "required": [
    "file_id",
    "knowledge_model_id"
  ],
  "type": "object"
}
```


### patch_v1_knowledge_models_files_metadata

PATCH: Update metadata of the file

**Method:** PATCH  
**Path:** /v1/knowledge-models/{knowledge_model_id}/files/{file_id}/metadata

**Input Schema:**
```json
{
  "properties": {
    "file_id": {
      "type": "string"
    },
    "knowledge_model_id": {
      "type": "string"
    }
  },
  "required": [
    "file_id",
    "knowledge_model_id"
  ],
  "type": "object"
}
```


### post_v1_knowledge_models_internal_documents

POST: Create new internal document

**Method:** POST  
**Path:** /v1/knowledge-models/{knowledge_model_id}/internal-documents

**Input Schema:**
```json
{
  "properties": {
    "knowledge_model_id": {
      "type": "string"
    }
  },
  "required": [
    "knowledge_model_id"
  ],
  "type": "object"
}
```


### get_v1_knowledge_models_internal_documents

GET: List internal documents

**Method:** GET  
**Path:** /v1/knowledge-models/{knowledge_model_id}/internal-documents

**Input Schema:**
```json
{
  "properties": {
    "knowledge_model_id": {
      "type": "string"
    },
    "limit": {
      "type": "string"
    },
    "offset": {
      "type": "string"
    }
  },
  "required": [
    "knowledge_model_id"
  ],
  "type": "object"
}
```


### patch_v1_knowledge_models_internal_documents

PATCH: Update internal document

**Method:** PATCH  
**Path:** /v1/knowledge-models/{knowledge_model_id}/internal-documents/{document_id}

**Input Schema:**
```json
{
  "properties": {
    "document_id": {
      "type": "string"
    },
    "knowledge_model_id": {
      "type": "string"
    }
  },
  "required": [
    "document_id",
    "knowledge_model_id"
  ],
  "type": "object"
}
```


### delete_v1_knowledge_models_internal_documents

Delete internal document

**Method:** DELETE  
**Path:** /v1/knowledge-models/{knowledge_model_id}/internal-documents/{document_id}

**Input Schema:**
```json
{
  "properties": {
    "document_id": {
      "type": "string"
    },
    "knowledge_model_id": {
      "type": "string"
    }
  },
  "required": [
    "document_id",
    "knowledge_model_id"
  ],
  "type": "object"
}
```


### post_v1_knowledge_models_internal_documents_chunks

POST: Create new internal chunk

**Method:** POST  
**Path:** /v1/knowledge-models/{knowledge_model_id}/internal-documents/{document_id}/chunks

**Input Schema:**
```json
{
  "properties": {
    "document_id": {
      "type": "string"
    },
    "knowledge_model_id": {
      "type": "string"
    }
  },
  "required": [
    "document_id",
    "knowledge_model_id"
  ],
  "type": "object"
}
```


### get_v1_knowledge_models_internal_documents_chunks

GET: List internal chunks

**Method:** GET  
**Path:** /v1/knowledge-models/{knowledge_model_id}/internal-documents/{document_id}/chunks

**Input Schema:**
```json
{
  "properties": {
    "document_id": {
      "type": "string"
    },
    "knowledge_model_id": {
      "type": "string"
    },
    "limit": {
      "type": "string"
    },
    "offset": {
      "type": "string"
    }
  },
  "required": [
    "document_id",
    "knowledge_model_id"
  ],
  "type": "object"
}
```


### post_v1_knowledge_models_internal_documents_chunks_batch

POST: Batch create internal chunks

**Method:** POST  
**Path:** /v1/knowledge-models/{knowledge_model_id}/internal-documents/{document_id}/chunks/batch

**Input Schema:**
```json
{
  "properties": {
    "document_id": {
      "type": "string"
    },
    "knowledge_model_id": {
      "type": "string"
    }
  },
  "required": [
    "document_id",
    "knowledge_model_id"
  ],
  "type": "object"
}
```


### get_v1_knowledge_models_internal_documents_chunks

Get internal chunk

**Method:** GET  
**Path:** /v1/knowledge-models/{knowledge_model_id}/internal-documents/{document_id}/chunks/{chunk_id}

**Input Schema:**
```json
{
  "properties": {
    "chunk_id": {
      "type": "string"
    },
    "document_id": {
      "type": "string"
    },
    "knowledge_model_id": {
      "type": "string"
    }
  },
  "required": [
    "chunk_id",
    "document_id",
    "knowledge_model_id"
  ],
  "type": "object"
}
```


### patch_v1_knowledge_models_internal_documents_chunks

PATCH: Update internal chunk

**Method:** PATCH  
**Path:** /v1/knowledge-models/{knowledge_model_id}/internal-documents/{document_id}/chunks/{chunk_id}

**Input Schema:**
```json
{
  "properties": {
    "chunk_id": {
      "type": "string"
    },
    "document_id": {
      "type": "string"
    },
    "knowledge_model_id": {
      "type": "string"
    }
  },
  "required": [
    "chunk_id",
    "document_id",
    "knowledge_model_id"
  ],
  "type": "object"
}
```


### delete_v1_knowledge_models_internal_documents_chunks

Delete internal chunk

**Method:** DELETE  
**Path:** /v1/knowledge-models/{knowledge_model_id}/internal-documents/{document_id}/chunks/{chunk_id}

**Input Schema:**
```json
{
  "properties": {
    "chunk_id": {
      "type": "string"
    },
    "document_id": {
      "type": "string"
    },
    "knowledge_model_id": {
      "type": "string"
    }
  },
  "required": [
    "chunk_id",
    "document_id",
    "knowledge_model_id"
  ],
  "type": "object"
}
```


### patch_v1_knowledge_models_widget

Patch knowledge model widget settings

**Method:** PATCH  
**Path:** /v1/knowledge-models/{knowledge_model_id}/widget

**Input Schema:**
```json
{
  "properties": {
    "knowledge_model_id": {
      "type": "string"
    }
  },
  "required": [
    "knowledge_model_id"
  ],
  "type": "object"
}
```


### get_v1_knowledge_models_chunks

GET: List document chunks

**Method:** GET  
**Path:** /v1/knowledge-models/{knowledge_model_id}/chunks

**Input Schema:**
```json
{
  "properties": {
    "content_type": {
      "description": "Filter by chunk content type",
      "type": "string"
    },
    "document_id": {
      "description": "Filter by specific document ID",
      "type": "string"
    },
    "document_type": {
      "description": "Filter by document type",
      "type": "string"
    },
    "knowledge_model_id": {
      "type": "string"
    },
    "limit": {
      "type": "string"
    },
    "offset": {
      "type": "string"
    },
    "sort": {
      "description": "Sort by field, e.g. \u0027chunk_index\u0027",
      "type": "string"
    }
  },
  "required": [
    "knowledge_model_id"
  ],
  "type": "object"
}
```


### post_v1_knowledge_models_chunks_search

POST: Search for raw text chunks

**Method:** POST  
**Path:** /v1/knowledge-models/{knowledge_model_id}/chunks/search

**Input Schema:**
```json
{
  "properties": {
    "knowledge_model_id": {
      "type": "string"
    }
  },
  "required": [
    "knowledge_model_id"
  ],
  "type": "object"
}
```


### post_v1_knowledge_models_videos_import

POST: Add video document into Model

**Method:** POST  
**Path:** /v1/knowledge-models/{knowledge_model_id}/videos/import

**Input Schema:**
```json
{
  "properties": {
    "knowledge_model_id": {
      "type": "string"
    }
  },
  "required": [
    "knowledge_model_id"
  ],
  "type": "object"
}
```


### get_v1_knowledge_models_videos

GET: List videos in the knowledge model

**Method:** GET  
**Path:** /v1/knowledge-models/{knowledge_model_id}/videos

**Input Schema:**
```json
{
  "properties": {
    "knowledge_model_id": {
      "type": "string"
    },
    "limit": {
      "type": "string"
    },
    "offset": {
      "type": "string"
    }
  },
  "required": [
    "knowledge_model_id"
  ],
  "type": "object"
}
```


### patch_v1_knowledge_models_videos

Patch video document

**Method:** PATCH  
**Path:** /v1/knowledge-models/{knowledge_model_id}/videos/{document_external_id}

**Input Schema:**
```json
{
  "properties": {
    "document_external_id": {
      "type": "string"
    },
    "knowledge_model_id": {
      "type": "string"
    }
  },
  "required": [
    "document_external_id",
    "knowledge_model_id"
  ],
  "type": "object"
}
```


### delete_v1_knowledge_models_videos

Delete video document

**Method:** DELETE  
**Path:** /v1/knowledge-models/{knowledge_model_id}/videos/{document_external_id}

**Input Schema:**
```json
{
  "properties": {
    "document_external_id": {
      "type": "string"
    },
    "knowledge_model_id": {
      "type": "string"
    }
  },
  "required": [
    "document_external_id",
    "knowledge_model_id"
  ],
  "type": "object"
}
```


### post_v1_knowledge_models_chat_completions

POST: Generates text responses based on incoming messages.

**Method:** POST  
**Path:** /v1/knowledge-models/{knowledge_model_id}/chat/completions/{extension}

**Input Schema:**
```json
{
  "properties": {
    "X-KM-Extension": {
      "type": "string"
    },
    "extension": {
      "type": "string"
    },
    "knowledge_model_id": {
      "type": "string"
    }
  },
  "required": [
    "knowledge_model_id",
    "extension"
  ],
  "type": "object"
}
```


### post_v1_knowledge_models_chat_completions

POST: Generates text responses based on incoming messages.

**Method:** POST  
**Path:** /v1/knowledge-models/{knowledge_model_id}/chat/completions

**Input Schema:**
```json
{
  "properties": {
    "X-KM-Extension": {
      "type": "string"
    },
    "extension": {
      "type": "string"
    },
    "knowledge_model_id": {
      "type": "string"
    }
  },
  "required": [
    "knowledge_model_id"
  ],
  "type": "object"
}
```


### post_v1_knowledge_models_tools_translation

POST: English translation tool.

**Method:** POST  
**Path:** /v1/knowledge-models/{knowledge_model_id}/tools/translation

**Input Schema:**
```json
{
  "properties": {
    "knowledge_model_id": {
      "type": "string"
    }
  },
  "required": [
    "knowledge_model_id"
  ],
  "type": "object"
}
```



## Available Resources


### get_alive_resource

Access to respond if authorized, do not respond on any error

**URI:** api:///alive  
**Method:** GET  
**Path:** /alive


### get_v1_knowledge_models_resource

Access to list knowledge models

**URI:** api:///v1/knowledge-models  
**Method:** GET  
**Path:** /v1/knowledge-models


### get_v1_knowledge_models_resource

Access to get knowledge model

**URI:** api:///v1/knowledge-models/{knowledge_model_id}  
**Method:** GET  
**Path:** /v1/knowledge-models/{knowledge_model_id}


### get_v1_knowledge_models_settings_resource

Access to get knowledge model settings

**URI:** api:///v1/knowledge-models/{knowledge_model_id}/settings  
**Method:** GET  
**Path:** /v1/knowledge-models/{knowledge_model_id}/settings


### get_v1_knowledge_models_chat_sessions_resource

Access to get all chat sessions for given knowledge model

**URI:** api:///v1/knowledge-models/{knowledge_model_id}/chat-sessions  
**Method:** GET  
**Path:** /v1/knowledge-models/{knowledge_model_id}/chat-sessions


### get_v1_knowledge_models_chat_sessions_resource

Access to get chat session

**URI:** api:///v1/knowledge-models/{knowledge_model_id}/chat-sessions/{chat_session_id}  
**Method:** GET  
**Path:** /v1/knowledge-models/{knowledge_model_id}/chat-sessions/{chat_session_id}


### get_v1_knowledge_models_files_resource

Access to download a file from a knowledge model

**URI:** api:///v1/knowledge-models/{knowledge_model_id}/files/{file_id}  
**Method:** GET  
**Path:** /v1/knowledge-models/{knowledge_model_id}/files/{file_id}


### get_v1_knowledge_models_files_metadata_resource

Access to returns metadata of the file

**URI:** api:///v1/knowledge-models/{knowledge_model_id}/files/{file_id}/metadata  
**Method:** GET  
**Path:** /v1/knowledge-models/{knowledge_model_id}/files/{file_id}/metadata


### get_v1_knowledge_models_internal_documents_resource

Access to get internal document

**URI:** api:///v1/knowledge-models/{knowledge_model_id}/internal-documents/{document_id}  
**Method:** GET  
**Path:** /v1/knowledge-models/{knowledge_model_id}/internal-documents/{document_id}


### get_v1_knowledge_models_widget_resource

Access to get the knowledge model widget settings

**URI:** api:///v1/knowledge-models/{knowledge_model_id}/widget  
**Method:** GET  
**Path:** /v1/knowledge-models/{knowledge_model_id}/widget


### get_v1_knowledge_models_videos_transcription_resource

Access to get video transcription

**URI:** api:///v1/knowledge-models/{knowledge_model_id}/videos/{document_external_id}/transcription  
**Method:** GET  
**Path:** /v1/knowledge-models/{knowledge_model_id}/videos/{document_external_id}/transcription


### get_v1_knowledge_models_videos_resource

Access to get video document

**URI:** api:///v1/knowledge-models/{knowledge_model_id}/videos/{document_external_id}  
**Method:** GET  
**Path:** /v1/knowledge-models/{knowledge_model_id}/videos/{document_external_id}


### get_v1_language_models_resource

Access to list language models

**URI:** api:///v1/language_models  
**Method:** GET  
**Path:** /v1/language_models



## Authentication

This server uses X-KM-AccessKey header for authentication. Make sure to set your API key in the `API_KEY` environment variable.

## Error Handling

The server includes comprehensive error handling for:
- API authentication errors
- Network timeouts
- Invalid parameters
- Server errors

All errors are logged and returned in a structured format.

## Development

### Project Structure

- `server.py` - Main MCP server implementation
- `tools.py` - Tool implementations
- `resources.py` - Resource implementations  
- `utils.py` - Utility functions
- `config.json` - Server configuration
- `requirements.txt` - Python dependencies

### Adding New Tools/Resources

To add new tools or resources, modify the respective files and update the server registration in `server.py`.

## License

Generated by mcpgen - AI-powered MCP server generator.