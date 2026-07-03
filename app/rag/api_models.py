from typing import Any

from pydantic import BaseModel, Field

class CreateCollectionRequest(BaseModel):
    collection_name: str = Field(
        ...,
        description="Collection name"
    )


class DeleteCollectionRequest(BaseModel):
    collection_name: str


class AddDocumentsRequest(BaseModel):
    collection_name: str

    ids: list[str]

    documents: list[str]

    metadatas: list[dict[str, Any]]


class CountDocumentsRequest(BaseModel):
    collection_name: str


class CollectionResponse(BaseModel):

    success: bool

    collection_name: str

    message: str


class CollectionListResponse(BaseModel):

    collections: list[str]


class CountDocumentsResponse(BaseModel):

    collection_name: str

    count: int


class IndexDocumentsResponse(BaseModel):

    success: bool

    indexed_documents: int

    message: str