from app.integrations.github.models import (
    CreateRepositoryRequest,
)

request = CreateRepositoryRequest(
    repository_name="employee-service",
    visibility="secret",
    description="Enterprise AI Demo"
)

print(request)

print()

print(request.model_dump())