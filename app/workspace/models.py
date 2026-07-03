from pydantic import BaseModel, Field


class PrepareWorkspaceRequest(BaseModel):
    """
    Request for preparing a repository workspace.
    """

    repository: str = Field(
        ...,
        description="Repository name (e.g. employee-service-agent)"
    )

    branch: str = Field(
        default="main"
    )


class WorkspaceResponse(BaseModel):
    """
    Workspace preparation response.
    """

    success: bool

    repository: str

    branch: str

    local_path: str

    message: str