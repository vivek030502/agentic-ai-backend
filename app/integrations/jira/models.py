from pydantic import BaseModel


class JiraUserResponse(BaseModel):
    """
    Response model for authenticated Jira user.
    """

    account_id: str
    display_name: str
    email: str
    active: bool


class GetIssueRequest(BaseModel):
    """
    Request model for fetching a Jira issue.
    """

    issue_key: str


class GetIssueResponse(BaseModel):
    """
    Response model returned after fetching a Jira issue.
    """

    issue_key: str

    summary: str

    description: str

    status: str

    issue_type: str

    project_key: str

    assignee: str | None = None

    reporter: str | None = None

    priority: str | None = None