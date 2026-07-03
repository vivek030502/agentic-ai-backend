from app.workspace.workspace_manager import WorkspaceManager


manager = WorkspaceManager()

workspace = manager.prepare_workspace(
    repository_url="https://github.com/vivek030502/employee-service-agent.git"
)

print("=" * 80)
print("WORKSPACE")
print("=" * 80)

print(workspace.model_dump())