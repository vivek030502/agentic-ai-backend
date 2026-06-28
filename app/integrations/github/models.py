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