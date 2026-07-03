from app.services.jira.jira_service import JiraService


service = JiraService()

response = service.get_authenticated_user()

print("=" * 80)
print("CONNECTED TO JIRA")
print("=" * 80)

print(response.model_dump())