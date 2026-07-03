from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field


class RepositoryFile(BaseModel):
    """
    Represents a file discovered inside a repository.
    """

    path: str = Field(
        ...,
        description="Relative file path."
    )

    name: str = Field(
        ...,
        description="File name."
    )

    extension: str = Field(
        ...,
        description="File extension."
    )

    language: str = Field(
        default="text",
        description="Detected programming language."
    )

    size: int = Field(
        default=0,
        description="File size in bytes."
    )

    content: str = Field(
        default="",
        description="Complete file content."
    )


class RepositoryChunk(BaseModel):
    """
    Represents one chunk of a repository file.
    """

    id: str

    repository: str

    branch: str

    file_path: str

    language: str

    chunk_index: int

    total_chunks: int

    content: str

    metadata: dict[str, Any]


class RepositoryIndexRequest(BaseModel):
    """
    Request to index a repository.
    """

    repository: str

    branch: str = "main"

    local_path: str


class RepositoryIndexResponse(BaseModel):
    """
    Repository indexing summary.
    """

    success: bool

    repository: str

    total_files: int

    indexed_files: int

    total_chunks: int

    collection_name: str

    started_at: datetime

    completed_at: datetime

    message: str