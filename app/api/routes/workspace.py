from fastapi import APIRouter

from app.workspace.models import (
    PrepareWorkspaceRequest,
    WorkspaceResponse,
)
from app.workspace.service import WorkspaceService

router = APIRouter(
    prefix="/workspace",
    tags=["Workspace"]
)

service = WorkspaceService()


@router.post(
    "/prepare",
    response_model=WorkspaceResponse
)
def prepare_workspace(
    request: PrepareWorkspaceRequest,
):

    return service.prepare(request)