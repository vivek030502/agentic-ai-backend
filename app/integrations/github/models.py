from typing import Literal

from pydantic import BaseModel, Field


class CreateRepositoryRequest(BaseModel):
    """
    Request model for creating a GitHub repository.
    """

    repository_name: str = Field(
        ...,
        description="Repository name"
    )

    visibility: Literal[
        "public",
        "private"
    ] = Field(
        default="public"
    )

    description: str = Field(
        default=""
    )

class CreateRepositoryResponse(BaseModel):
    """
    Response model returned after repository creation.
    """

    success: bool

    repository_name: str

    repository_url: str

    visibility: Literal[
        "public",
        "private"
    ]

    description: str = ""

    default_branch: str = "main"

    message: str

class CreateBranchRequest(BaseModel):
    """
    Request model for creating a GitHub branch.
    """

    repository_name: str

    branch_name: str

    source_branch: str = "main"

class CreateBranchResponse(BaseModel):
    """
    Response model returned after branch creation.
    """

    success: bool

    repository_name: str

    branch_name: str

    source_branch: str

    branch_url: str | None = None

    message: str