from app.config.logger import app_logger
from app.integrations.github.models import CreateRepositoryRequest
from app.services.github.github_service import GitHubService
from app.tools.base_tool import BaseTool


class GitHubTool(BaseTool):
    """
    Tool responsible for GitHub operations.

    Receives parameters from the AI Planner,
    validates them and delegates business logic
    to GitHubService.
    """

    def __init__(self):
        self.github_service = GitHubService()

    @property
    def action(self) -> str:
        return "CREATE_GITHUB_REPOSITORY"

    @property
    def description(self) -> str:
        return "Creates a GitHub repository."

    @property
    def parameters(self) -> dict:

        return {
            "repository_name": "string",
            "visibility": "public | private",
            "description": "string"
        }

    def execute(self, parameters):

        app_logger.info("GitHub Tool Started")

        request = CreateRepositoryRequest(

            repository_name=parameters.get(
                "repository_name"
            ),

            visibility=parameters.get(
                "visibility",
                "public"
            ),

            description=parameters.get(
                "description",
                ""
            )
        )

        response = self.github_service.create_repository(
            request
        )

        app_logger.info("GitHub Tool Completed")

        return response