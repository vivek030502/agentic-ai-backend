from typing import List

from pydantic import BaseModel, Field


class Dependency(BaseModel):
    """
    Represents a dependency used by the project.
    """

    name: str

    version: str | None = None


class ProjectFile(BaseModel):
    """
    Represents a file inside the repository.
    """

    path: str

    extension: str

    size: int

    content: str


class ProjectDirectory(BaseModel):
    """
    Represents a project directory.
    """

    path: str


class RepositoryContext(BaseModel):
    """
    Final repository analysis result.
    """

    repository_name: str

    repository_path: str

    language: str | None = None

    framework: str | None = None

    package_manager: str | None = None

    build_system: str | None = None

    entry_point: str | None = None

    dependencies: List[Dependency] = Field(default_factory=list)

    directories: List[ProjectDirectory] = Field(default_factory=list)

    files: List[ProjectFile] = Field(default_factory=list)