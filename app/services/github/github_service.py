from app.config.logger import app_logger
from app.integrations.github.client import GitHubClient
from app.integrations.github.models import (
    CreateRepositoryRequest,
    CreateRepositoryResponse,
    CreateBranchRequest,
    CreateBranchResponse,
)


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
    ) -> CreateRepositoryResponse:
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

        # Call GitHub client
        api_response = self.client.create_repository(request)

         # Map API response -> Pydantic response model
        response = CreateRepositoryResponse(
            success=True,
            repository_name=request.repository_name,
            repository_url=api_response["html_url"],
            visibility="private" if api_response["private"] else "public",
            description=api_response.get("description", ""),
            default_branch=api_response.get("default_branch", "main"),
            message="Repository created successfully"
        )

        app_logger.info(
            "Repository created successfully."
        )

        return response

    def create_branch(
        self,
        request: CreateBranchRequest
    ) -> CreateBranchResponse:
        """
        Create a new GitHub branch from a source branch.
        """

        self._validate_branch_request(request)

        app_logger.info(
            f"Creating branch '{request.branch_name}' in repo '{request.repository_name}' "
            f"from '{request.source_branch}'"
        )

        api_response = self.client.create_branch(request)

        branch_url = api_response.get(
            "url",
            self._build_branch_url(
                repository_name=request.repository_name,
                branch_name=request.branch_name
            )
        )

        response = CreateBranchResponse(
            success=True,
            repository_name=request.repository_name,
            branch_name=request.branch_name,
            source_branch=request.source_branch,
            branch_url=branch_url,
            message="Branch created successfully"
        )

        app_logger.info("Branch created successfully.")

        return response

    def _validate_repository_request(
        self,
        request: CreateRepositoryRequest
    ):
        """
        Business validation before calling GitHub.
        """

        if len(request.repository_name.strip()) < 3:
            raise ValueError(
                "Repository name must contain at least 3 characters."
            )

        if " " in request.repository_name:
            raise ValueError(
                "Repository name must not contain spaces."
            )

    def _validate_branch_request(
        self,
        request: CreateBranchRequest
    ) -> None:
        """
        Business validation for branch creation.
        """

        if len(request.repository_name.strip()) < 3:
            raise ValueError("Repository name must be at least 3 characters.")

        if len(request.branch_name.strip()) < 1:
            raise ValueError("Branch name cannot be empty.")

        if request.branch_name == request.source_branch:
            raise ValueError("Branch name and source branch cannot be same.")

        if " " in request.branch_name:
            raise ValueError("Branch name must not contain spaces.")

    def _build_branch_url(
        self,
        repository_name: str,
        branch_name: str
    ) -> str:
        """
        Build GitHub branch URL.
        """

        owner = self.client.get_authenticated_user()["login"]

        return (
            f"https://github.com/"
            f"{owner}/{repository_name}"
            f"/tree/{branch_name}"
        )