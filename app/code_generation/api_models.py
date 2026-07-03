from pydantic import BaseModel

from app.code_generation.models import GeneratedFile


class CodeGenerationRequest(BaseModel):
    """
    API request for AI code generation.
    """

    repository: str

    branch: str

    jira_key: str


class CodeGenerationResult(BaseModel):
    """
    API response.
    """

    success: bool

    repository: str

    branch: str

    jira_key: str

    total_files: int

    files: list[GeneratedFile]

    message: str