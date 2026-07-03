from app.workspace.manager import WorkspaceManager
from app.workspace.models import (
    PrepareWorkspaceRequest,
    WorkspaceResponse,
)


class WorkspaceService:

    def __init__(self):

        self.manager = WorkspaceManager()

    def prepare(
        self,
        request: PrepareWorkspaceRequest,
    ) -> WorkspaceResponse:

        path = self.manager.prepare_repository(
            request.repository,
            request.branch,
        )

        return WorkspaceResponse(
            success=True,
            repository=request.repository,
            branch=request.branch,
            local_path=path,
            message="Workspace prepared successfully."
        )