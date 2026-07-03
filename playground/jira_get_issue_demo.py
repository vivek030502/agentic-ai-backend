from app.integrations.jira.models import GetIssueRequest
from app.services.jira.jira_service import JiraService


service = JiraService()

request = GetIssueRequest(
    issue_key="KAN-4"
)

response = service.get_issue(request)

print("=" * 80)
print("JIRA ISSUE")
print("=" * 80)

print(response.model_dump())