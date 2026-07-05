from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field


# ==========================================================
# Dependency
# ==========================================================

class Dependency(BaseModel):
    """
    Represents a project dependency.
    """

    name: str
    version: str | None = None


# ==========================================================
# Repository Directory
# ==========================================================

class RepositoryDirectory(BaseModel):
    """
    Represents a directory inside the repository.
    """

    path: str


# ==========================================================
# Repository File
# ==========================================================

class RepositoryFile(BaseModel):
    """
    Represents a file discovered inside a repository.
    """

    path: str

    name: str

    extension: str

    language: str = "text"

    size: int = 0

    content: str = ""


# ==========================================================
# Repository Detection
# ==========================================================

class RepositoryDetection(BaseModel):

    language: str | None = None

    framework: str | None = None

    package_manager: str | None = None

    build_system: str | None = None

    entry_point: str | None = None


# ==========================================================
# Repository Analysis Context
# ==========================================================

class RepositoryAnalysisContext(BaseModel):

    repository_name: str

    repository_path: str

    language: str | None = None

    framework: str | None = None

    package_manager: str | None = None

    build_system: str | None = None

    entry_point: str |None = None

    dependencies: list[Dependency] = Field(default_factory=list)

    directories: list[RepositoryDirectory] = Field(default_factory=list)

    files: list[RepositoryFile] = Field(default_factory=list)


# ==========================================================
# Repository Chunk
# ==========================================================

class RepositoryChunk(BaseModel):

    id: str

    repository: str

    branch: str

    file_path: str

    language: str

    chunk_index: int

    total_chunks: int

    content: str

    metadata: dict[str, Any]


# ==========================================================
# Repository Index Request
# ==========================================================

class RepositoryIndexRequest(BaseModel):

    repository: str

    branch: str = "main"

    local_path: str


# ==========================================================
# Repository Index Response
# ==========================================================

class RepositoryIndexResponse(BaseModel):

    success: bool

    repository: str

    total_files: int

    indexed_files: int

    total_chunks: int

    collection_name: str

    started_at: datetime

    completed_at: datetime

    message: str