from pprint import pprint

from app.integrations.github.client import GitHubClient
from app.integrations.github.models import CreateRepositoryRequest

client = GitHubClient()

request = CreateRepositoryRequest(
    repository_name="employee-service-demo",
    visibility="private",
    description="Created by Agentic AI POC"
)

response = client.create_repository(request)

print("=" * 80)
print("REPOSITORY CREATED")
print("=" * 80)

pprint(response)