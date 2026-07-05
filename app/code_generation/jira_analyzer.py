# from app.integrations.jira.models import GetIssueResponse
# from app.code_generation.models import JiraAnalysis


# class JiraAnalyzer:
#     """
#     Converts a Jira story into a strongly typed object
#     used throughout the code generation pipeline.
#     """

#     def analyze(
#         self,
#         issue: GetIssueResponse,
#     ) -> JiraAnalysis:

#         return JiraAnalysis(
#             issue_key=issue.issue_key,
#             summary=issue.summary,
#             description=issue.description,
#             issue_type=issue.issue_type,
#             status=issue.status,
#             priority=issue.priority,
#             project=issue.project_key,
#             assignee=issue.assignee,
#             reporter=issue.reporter,
#             suggested_files=[],
#         )




from app.ai.service import AIService
from app.ai.json_parser import JsonResponseParser

from app.integrations.jira.models import GetIssueResponse

from app.code_generation.models import JiraAnalysis

from app.code_generation.jira_prompts import (
    SYSTEM_PROMPT,
    USER_PROMPT,
)


class JiraAnalyzer:

    def __init__(self):

        self.ai = AIService()

        self.parser = JsonResponseParser()

    def analyze(
        self,
        issue: GetIssueResponse,
    ) -> JiraAnalysis:

        prompt = USER_PROMPT.format(

            issue_key=issue.issue_key,

            summary=issue.summary,

            description=issue.description,

            issue_type=issue.issue_type,

            priority=issue.priority,

        )

        response = self.ai.generate(

            system_prompt=SYSTEM_PROMPT,

            user_prompt=prompt,

            response_format=JiraAnalysis,

        )

        return self.parser.parse(
            response.content,
            JiraAnalysis,
        )