from app.integrations.jira.models import GetIssueResponse


class JiraAnalyzer:
    """
    Converts a Jira story into a structured format
    that is easier for the LLM to consume.
    """

    def analyze(
        self,
        issue: GetIssueResponse,
    ) -> dict:

        return {
            "issue_key": issue.issue_key,
            "summary": issue.summary,
            "description": issue.description,
            "issue_type": issue.issue_type,
            "status": issue.status,
            "priority": issue.priority,
            "project": issue.project_key,
            "assignee": issue.assignee,
            "reporter": issue.reporter,
        }