from pydantic import BaseModel, Field


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

    repository_path: str

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

    # files: list[GeneratedFile]
    files: list[GeneratedFile] = Field(
        default_factory=list
    )

class JiraAnalysis(BaseModel):
    """
    Structured analysis of a Jira issue.
    """

    issue_key: str

    summary: str

    description: str

    issue_type: str

    status: str

    priority: str

    project: str

    assignee: str

    reporter: str

    implementation_plan: list[str] = Field(default_factory=list)

    impacted_modules: list[str] = Field(default_factory=list)

    suggested_files: list[str] = Field(default_factory=list)

    search_keywords: list[str] = Field(default_factory=list)