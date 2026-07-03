from app.integrations.github.models import CreateBranchRequest
from app.services.github.github_service import GitHubService


service = GitHubService()

request = CreateBranchRequest(
    repository_name="WeatherApp",
    branch_name="feature/weather-app-login-api",
    source_branch="main"
)

response = service.create_branch(request)

print("=" * 80)
print("BRANCH CREATED")
print("=" * 80)

print(response.model_dump())