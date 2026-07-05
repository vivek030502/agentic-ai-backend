from pathlib import Path

from git import Repo, GitCommandError

from app.config.logger import app_logger


class GitWorkspaceClient:
    """
    Wrapper around GitPython.

    Responsible only for executing Git commands.
    """

    def repository_exists(
        self,
        repository_path: str
    ) -> bool:

        return Path(repository_path).exists()

    def clone_repository(
        self,
        repository_url: str,
        destination: str
    ) -> None:

        app_logger.info(
            f"Cloning repository: {repository_url}"
        )

        Repo.clone_from(
            repository_url,
            destination
        )

    def open_repository(
        self,
        repository_path: str
    ) -> Repo:

        return Repo(repository_path)

    def fetch(
        self,
        repository_path: str
    ) -> None:

        app_logger.info("Fetching latest changes")

        repo = self.open_repository(
            repository_path
        )

        repo.remotes.origin.fetch()

    def checkout_branch(
        self,
        repository_path: str,
        branch: str
    ) -> None:

        repo = self.open_repository(
            repository_path
        )

        app_logger.info(
            f"Checkout branch: {branch}"
        )

        try:

            repo.git.checkout(branch)

        except GitCommandError:

            app_logger.info(
                "Branch not found locally. Creating tracking branch."
            )

            repo.git.checkout(
                "-b",
                branch,
                f"origin/{branch}"
            )

    def pull(
        self,
        repository_path: str
    ) -> None:

        app_logger.info(
            "Pull latest changes"
        )

        repo = self.open_repository(
            repository_path
        )

        repo.remotes.origin.pull()

    def create_branch(
        self,
        repository_path: str,
        branch: str
    ) -> None:

        repo = self.open_repository(
            repository_path
        )

        app_logger.info(
            f"Creating branch: {branch}"
        )

        repo.git.checkout("-b", branch)

    def commit(
        self,
        repository_path: str,
        message: str,
    ) -> bool:

        repo = self.open_repository(
            repository_path
        )

        repo.git.add(A=True)

        if not repo.is_dirty(untracked_files=True):

            app_logger.info(
                "No changes to commit."
            )

            return False

        repo.index.commit(message)

        app_logger.info(
            "Commit created."
        )

        return True

    def push(
        self,
        repository_path: str,
        branch: str,
    ) -> None:

        repo = self.open_repository(
            repository_path
        )

        app_logger.info(
            f"Pushing branch {branch}"
        )

        repo.remotes.origin.push(
            refspec=f"{branch}:{branch}"
        )