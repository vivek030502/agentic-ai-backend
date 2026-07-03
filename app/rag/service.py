from typing import Any

from app.config.logger import app_logger
from app.rag.chroma_manager import ChromaManager
from app.rag.models import (
    SearchRequest,
    SearchResponse
)

from app.rag.api_models import (
    CollectionResponse,
    CollectionListResponse,
    CountDocumentsResponse,
    IndexDocumentsResponse
)


class RAGService:
    """
    Service layer for all RAG operations.

    Responsible for:

    - Collection lifecycle
    - Document indexing
    - Semantic retrieval

    This service hides ChromaDB implementation
    from API and Agent modules.
    """

    def __init__(self):

        self.manager = ChromaManager()

    # --------------------------------------------------
    # Collection
    # --------------------------------------------------

    def create_collection(
        self,
        collection_name: str
    ) -> CollectionResponse:

        app_logger.info(
            f"Creating collection : {collection_name}"
        )

        self.manager.create_collection(
            collection_name
        )

        return CollectionResponse(
            success=True,
            collection_name=collection_name,
            message="Collection created successfully."
        )

    def delete_collection(
        self,
        collection_name: str
    ) -> CollectionResponse:

        app_logger.info(
            f"Deleting collection : {collection_name}"
        )

        self.manager.delete_collection(
            collection_name
        )

        return CollectionResponse(
            success=True,
            collection_name=collection_name,
            message="Collection deleted successfully."
        )


    def list_collections(
        self
    ) -> CollectionListResponse:

        return CollectionListResponse(
            collections=self.manager.list_collections()
        )


    def count_documents(
        self,
        collection_name: str
    ) -> CountDocumentsResponse:

        return CountDocumentsResponse(
            collection_name=collection_name,
            count=self.manager.count_documents(collection_name)
        )

    # --------------------------------------------------
    # Documents
    # --------------------------------------------------

    def add_documents(
        self,
        collection_name: str,
        ids: list[str],
        documents: list[str],
        metadatas: list[dict[str, Any]]
    ) -> IndexDocumentsResponse:

        app_logger.info(
            f"Indexing {len(documents)} documents."
        )

        count = self.manager.add_documents(
            collection_name=collection_name,
            ids=ids,
            documents=documents,
            metadatas=metadatas
        )

        return IndexDocumentsResponse(
            success=True,
            indexed_documents=count,
            message=f"{count} documents indexed successfully."
        )

    # --------------------------------------------------
    # Search
    # --------------------------------------------------

    def search(
        self,
        request: SearchRequest
    ) -> SearchResponse:

        app_logger.info(
            f"Searching collection : {request.collection_name}"
        )

        return self.manager.search(
            request
        )
        