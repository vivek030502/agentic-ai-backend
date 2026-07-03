from typing import Any

import chromadb
from chromadb.api.models.Collection import Collection

from app.config.logger import app_logger
from app.config.settings import settings
from app.rag.embedding_service import EmbeddingService
from app.rag.exceptions import CollectionNotFoundException
from app.rag.models import SearchRequest, SearchResponse, SearchResult


class ChromaManager:
    """
    Responsible for all ChromaDB operations.

    Responsibilities

    - Create Collection
    - Delete Collection
    - List Collections
    - Store Documents
    - Semantic Search
    """

    def __init__(self):

        app_logger.info(
            f"Initializing ChromaDB : {settings.CHROMA_DB_PATH}"
        )

        self.client = chromadb.PersistentClient(
            path=settings.CHROMA_DB_PATH
        )

        self.embedding_service = EmbeddingService()

    # ----------------------------------------------------
    # Collection Operations
    # ----------------------------------------------------

    def create_collection(
        self,
        collection_name: str
    ) -> Collection:

        app_logger.info(
            f"Creating collection : {collection_name}"
        )

        return self.client.get_or_create_collection(
            name=collection_name
        )

    def delete_collection(
        self,
        collection_name: str
    ) -> None:

        app_logger.info(
            f"Deleting collection : {collection_name}"
        )

        self.client.delete_collection(
            name=collection_name
        )

    def collection_exists(
        self,
        collection_name: str
    ) -> bool:

        collections = self.client.list_collections()

        return any(
            collection.name == collection_name
            for collection in collections
        )

    def list_collections(
        self
    ) -> list[str]:

        collections = self.client.list_collections()

        return [
            collection.name
            for collection in collections
        ]

    def get_collection(
        self,
        collection_name: str
    ) -> Collection:

        if not self.collection_exists(collection_name):
            raise CollectionNotFoundException(
                f"Collection '{collection_name}' not found."
            )

        return self.client.get_collection(
            collection_name
        )

    # ----------------------------------------------------
    # Document Operations
    # ----------------------------------------------------

    def add_documents(
        self,
        collection_name: str,
        ids: list[str],
        documents: list[str],
        metadatas: list[dict[str, Any]]
    ) -> int:

        collection = self.create_collection(
            collection_name
        )

        embeddings = self.embedding_service.embed_batch(
            documents
        )

        collection.add(
            ids=ids,
            documents=documents,
            metadatas=metadatas,
            embeddings=embeddings
        )

        app_logger.info(
            f"{len(ids)} documents indexed."
        )

        return len(ids)

    def count_documents(
        self,
        collection_name: str
    ) -> int:

        collection = self.get_collection(
            collection_name
        )

        return collection.count()

    # ----------------------------------------------------
    # Search
    # ----------------------------------------------------

    def search(
        self,
        request: SearchRequest
    ) -> SearchResponse:

        collection = self.get_collection(
            request.collection_name
        )

        embedding = self.embedding_service.embed(
            request.query
        )

        response = collection.query(
            query_embeddings=[embedding],
            n_results=request.top_k
        )

        results: list[SearchResult] = []

        ids = response["ids"][0]
        docs = response["documents"][0]
        metas = response["metadatas"][0]
        distances = response["distances"][0]

        for idx in range(len(ids)):

            results.append(

                SearchResult(
                    id=ids[idx],
                    document=docs[idx],
                    metadata=metas[idx],
                    score=1 - distances[idx]
                )

            )

        return SearchResponse(
            query=request.query,
            results=results
        )