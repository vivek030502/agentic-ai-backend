from app.config.settings import settings
from app.integrations.base.http_client import BaseHttpClient
from app.integrations.github.models import CreateRepositoryRequest


class GitHubClient(BaseHttpClient):
    """
    Client responsible for communicating
    with the GitHub REST API.
    """

    def __init__(self):

        headers = {
            "Authorization": f"Bearer {settings.GITHUB_TOKEN}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }

        super().__init__(
            base_url=settings.GITHUB_BASE_URL,
            headers=headers,
        )

    def get_authenticated_user(self) -> dict:
        """
        Returns information about the authenticated GitHub user.
        """

        response = self.get("/user")

        return response.json()

    def create_repository(
        self,
        request: CreateRepositoryRequest
    ) -> dict:
        """
        Creates a new GitHub repository.

        Args:
            request: Repository creation request.

        Returns:
            GitHub API response as a dictionary.
        """

        payload = {
            "name": request.repository_name,
            "description": request.description,
            "private": request.visibility == "private"
        }

        response = self.post(
            endpoint="/user/repos",
            json_data=payload
        )

        return response.json()