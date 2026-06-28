from app.config.logger import app_logger
from app.tools.base_tool import BaseTool


class JiraTool(BaseTool):
    """
    Mock Jira Tool.

    Later this class will call the real Jira REST API.
    """

    @property
    def action(self) -> str:
        return "CREATE_JIRA_TICKET"

    @property
    def description(self) -> str:
        return (
            "Creates a Jira issue in the configured project."
        )

    @property
    def parameters(self) -> dict:
        return {
            "project": "string",
            "issue_type": "Story | Task | Bug",
            "summary": "string",
            "description": "string"
        }


    def execute(self, parameters: dict):

        project = parameters.get(
            "project",
            "AI"
        )

        summary = parameters.get("summary", "Default Jira Story")

        issue_type = parameters.get(
            "issue_type",
            "Story"
        )

        description = parameters.get(
            "description",
            ""
        )

        app_logger.info(
            f"Creating Jira ticket: {summary}"
        )

        return {
            "success": True,
            "ticket": "AI-101",
            "project": project,
            "issue_type": issue_type,
            "summary": summary,
            "description": description,
            "message": "Jira ticket created successfully."
        }