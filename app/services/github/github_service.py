from app.config.logger import app_logger
from app.integrations.github.client import GitHubClient
from app.integrations.github.models import CreateRepositoryRequest


class GitHubService:
    """
    Service layer for GitHub operations.

    Responsible for:
    - Business logic
    - Validation
    - Orchestration
    - Calling GitHubClient
    """

    def __init__(self):
        self.client = GitHubClient()

    def create_repository(
        self,
        request: CreateRepositoryRequest
    ) -> dict:
        """
        Create a GitHub repository.

        Args:
            request: Repository creation request.

        Returns:
            GitHub API response.
        """

        self._validate_repository_request(request)

        app_logger.info(
            f"Creating repository: {request.repository_name}"
        )

        response = self.client.create_repository(request)

        app_logger.info(
            "Repository created successfully."
        )

        return response

    def _validate_repository_request(
        self,
        request: CreateRepositoryRequest
    ):
        """
        Business validation before calling GitHub.
        """

        if len(request.repository_name) < 3:
            raise ValueError(
                "Repository name must contain at least 3 characters."
            )