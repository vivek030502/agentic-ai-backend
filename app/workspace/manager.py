from pathlib import Path

from app.config.logger import app_logger
from app.config.settings import settings
from app.integrations.github.client import GitHubClient
from app.workspace.git_client import GitWorkspaceClient


class WorkspaceManager:
    """
    Responsible for preparing local Git workspaces.
    """

    def __init__(self):

        self.git = GitWorkspaceClient()

        self.github = GitHubClient()

        self.workspace_root = Path(
            settings.WORKSPACE_DIRECTORY
        )

        self.workspace_root.mkdir(
            parents=True,
            exist_ok=True
        )

    def prepare_repository(
        self,
        repository: str,
        branch: str
    ) -> str:

        repository_path = (
            self.workspace_root / repository
        )

        repository_path = str(
            repository_path
        )

        if not self.git.repository_exists(
            repository_path
        ):

            app_logger.info(
                "Repository not found locally."
            )

            user = self.github.get_authenticated_user()

            repository_url = (
                f"https://github.com/"
                f"{user['login']}/"
                f"{repository}.git"
            )

            self.git.clone_repository(
                repository_url,
                repository_path
            )

        else:

            app_logger.info(
                "Repository already exists."
            )

        self.git.fetch(
            repository_path
        )

        self.git.checkout_branch(
            repository_path,
            branch
        )

        self.git.pull(
            repository_path
        )

        app_logger.info(
            f"Workspace ready: {repository_path}"
        )

        return repository_path