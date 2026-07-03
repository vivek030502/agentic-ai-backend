from pydantic import BaseModel


class ContextDocument(BaseModel):
    """
    One RAG document supplied to the LLM.
    """

    file_path: str

    content: str


class CodeGenerationContext(BaseModel):
    """
    Complete context passed into PromptBuilder.
    """

    repository: str

    branch: str

    jira_key: str

    jira_summary: str

    jira_description: str

    repository_summary: str

    suggested_files: list[str]

    rag_documents: list[ContextDocument]


class GeneratedFile(BaseModel):
    """
    One generated source file.
    """

    file_path: str

    language: str

    content: str


class CodeGenerationResponse(BaseModel):
    """
    Final parsed LLM output.
    """

    files: list[GeneratedFile]