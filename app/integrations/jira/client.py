import base64

from app.config.settings import settings
from app.integrations.base.http_client import BaseHttpClient


class JiraClient(BaseHttpClient):
    """
    Client responsible for communicating
    with the Jira REST API.
    """

    def __init__(self):

        credentials = (
            f"{settings.JIRA_EMAIL}:{settings.JIRA_API_TOKEN}"
        )

        encoded_credentials = base64.b64encode(
            credentials.encode()
        ).decode()

        headers = {
            "Authorization": f"Basic {encoded_credentials}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        super().__init__(
            base_url=settings.JIRA_BASE_URL,
            headers=headers,
        )

    def get_authenticated_user(self) -> dict:
        """
        Returns the authenticated Jira user.

        Returns:
            Raw Jira API response.
        """

        response = self.get(
            endpoint="/rest/api/3/myself"
        )

        return response.json()

    def get_issue(
        self,
        issue_key: str
    ) -> dict:
        """
        Fetch a Jira issue.

        Returns:
            Raw Jira API response.
        """

        response = self.get(
            endpoint=f"/rest/api/3/issue/{issue_key}"
        )

        return response.json()