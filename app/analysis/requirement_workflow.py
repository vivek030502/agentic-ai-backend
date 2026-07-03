from app.analysis.requirement_analyzer import RequirementAnalyzer
from app.analysis.models import RequirementAnalysis
from app.integrations.jira.models import GetIssueRequest
from app.services.jira.jira_service import JiraService


class RequirementWorkflow:
    """
    End-to-end workflow that fetches a Jira issue
    and analyzes it using AI.
    """

    def __init__(self):
        self.jira_service = JiraService()
        self.analyzer = RequirementAnalyzer()

    def analyze_issue(
        self,
        issue_key: str,
    ) -> RequirementAnalysis:

        issue = self.jira_service.get_issue(
            GetIssueRequest(
                issue_key=issue_key
            )
        )

        return self.analyzer.analyze(
            summary=issue.summary,
            description=issue.description,
        )