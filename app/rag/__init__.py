"""
RAG Module

Responsible for:

- Repository indexing
- Embedding generation
- ChromaDB management
- Retrieval
"""

from app.rag.chroma_manager import ChromaManager
from app.rag.embedding_service import EmbeddingService

__all__ = [
    "ChromaManager",
    "EmbeddingService",
]