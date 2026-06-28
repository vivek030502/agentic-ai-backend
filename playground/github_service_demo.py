from pprint import pprint

from app.integrations.github.models import CreateRepositoryRequest
from app.services.github.github_service import GitHubService

service = GitHubService()

request = CreateRepositoryRequest(
    repository_name="service-layer-demo",
    visibility="private",
    description="Created using GitHubService"
)

response = service.create_repository(request)

print("=" * 80)
print("SERVICE RESPONSE")
print("=" * 80)

pprint(response)