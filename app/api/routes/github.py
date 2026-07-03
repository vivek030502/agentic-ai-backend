from fastapi import APIRouter

from app.integrations.github.models import (
    CreateRepositoryRequest,
    CreateRepositoryResponse,
    CreateBranchRequest,
    CreateBranchResponse,
)

from app.services.github.github_service import GitHubService

router = APIRouter(
    prefix="/github",
    tags=["GitHub"],
)

service = GitHubService()


@router.post(
    "/repository",
    response_model=CreateRepositoryResponse,
)
def create_repository(
    request: CreateRepositoryRequest,
):
    return service.create_repository(request)


@router.post(
    "/branch",
    response_model=CreateBranchResponse,
)
def create_branch(
    request: CreateBranchRequest,
):
    return service.create_branch(request)