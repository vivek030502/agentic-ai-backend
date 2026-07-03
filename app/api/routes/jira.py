from fastapi import APIRouter

from app.integrations.jira.models import (
    GetIssueRequest,
    GetIssueResponse,
)

from app.services.jira.jira_service import JiraService

router = APIRouter(
    prefix="/jira",
    tags=["Jira"],
)

service = JiraService()


@router.post(
    "/issue",
    response_model=GetIssueResponse,
)
def get_issue(
    request: GetIssueRequest,
):
    return service.get_issue(request)