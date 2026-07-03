from app.config.logger import app_logger
from app.integrations.jira.client import JiraClient
from app.integrations.jira.models import JiraUserResponse
from app.integrations.jira.models import (
    GetIssueRequest,
    GetIssueResponse,
)


class JiraService:
    """
    Service layer for Jira operations.
    """

    def __init__(self):
        self.client = JiraClient()

    def get_authenticated_user(
        self,
    ) -> JiraUserResponse:
        """
        Returns the currently authenticated Jira user.
        """

        app_logger.info(
            "Fetching authenticated Jira user."
        )

        api_response = self.client.get_authenticated_user()

        response = JiraUserResponse(
            account_id=api_response["accountId"],
            display_name=api_response["displayName"],
            email=api_response.get("emailAddress", ""),
            active=api_response["active"],
        )

        app_logger.info(
            "Authenticated Jira user retrieved successfully."
        )

        return response

    def get_issue(
        self,
        request: GetIssueRequest
    ) -> GetIssueResponse:
        """
        Fetch a Jira issue.
        """

        app_logger.info(
            f"Fetching Jira issue: {request.issue_key}"
        )

        api_response = self.client.get_issue(
            request.issue_key
        )

        fields = api_response["fields"]

        response = GetIssueResponse(
            issue_key=api_response["key"],
            summary=fields["summary"],
            description=self._extract_description(fields),
            status=fields["status"]["name"],
            issue_type=fields["issuetype"]["name"],
            project_key=fields["project"]["key"],
            assignee=(
                fields["assignee"]["displayName"]
                if fields["assignee"]
                else None
            ),
            reporter=(
                fields["reporter"]["displayName"]
                if fields["reporter"]
                else None
            ),
            priority=(
                fields["priority"]["name"]
                if fields["priority"]
                else None
            ),
        )

        app_logger.info(
            "Issue fetched successfully."
        )

        return response

    
    def _extract_description(
        self,
        fields: dict
    ) -> str:
        """
        Convert Jira ADF description into plain text.
        """

        description = fields.get("description")

        if not description:
            return ""

        result = []

        for block in description.get("content", []):

            for item in block.get("content", []):

                if item.get("type") == "text":
                    result.append(item["text"])

            result.append("\n")

        return "".join(result).strip()