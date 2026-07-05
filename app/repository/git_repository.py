from app.workspace.git_client import GitWorkspaceClient


class GitRepository:

    def __init__(self):

        self.git = GitWorkspaceClient()

    def commit_and_push(
        self,
        repository_path: str,
        branch: str,
        commit_message: str,
    ):

        committed = self.git.commit(
            repository_path,
            commit_message,
        )

        if committed:

            self.git.push(
                repository_path,
                branch,
            )

        return committed