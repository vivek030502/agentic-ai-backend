from pydantic import BaseModel


class RequirementAnalysis(BaseModel):
    """
    Structured analysis of a Jira requirement.
    """

    feature_name: str

    summary: str

    modules: list[str]

    tasks: list[str]

    estimated_files: list[str]

    technologies: list[str]