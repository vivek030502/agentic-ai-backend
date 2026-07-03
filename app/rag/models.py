from typing import Any

from pydantic import BaseModel, Field


class DocumentMetadata(BaseModel):
    """
    Metadata associated with a document.
    """

    repository: str

    branch: str

    file_path: str

    language: str

    file_type: str


class Document(BaseModel):
    """
    Represents a repository document before indexing.
    """

    id: str

    content: str

    metadata: DocumentMetadata


class IndexedDocument(BaseModel):
    """
    Document ready for ChromaDB.
    """

    id: str

    document: str

    metadata: dict[str, Any]


class SearchRequest(BaseModel):
    """
    Semantic search request.
    """

    collection_name: str = Field(
        ...,
        description="ChromaDB collection name"
    )

    query: str = Field(
        ...,
        description="Semantic search query"
    )

    top_k: int = Field(
        default=5,
        ge=1,
        le=20
    )


class SearchResult(BaseModel):
    """
    Single semantic search result.
    """

    id: str

    score: float

    document: str

    metadata: dict[str, Any]


class SearchResponse(BaseModel):
    """
    Semantic search response.
    """

    query: str

    results: list[SearchResult]