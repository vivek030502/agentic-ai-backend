import json

from app.ai.service import AIService
from app.analysis.models import RequirementAnalysis
from app.analysis.prompts import (
    SYSTEM_PROMPT,
    USER_PROMPT,
)


class RequirementAnalyzer:
    """
    Uses Gemini to analyze Jira requirements.
    """

    def __init__(self):
        self.ai = AIService()

    def analyze(
        self,
        summary: str,
        description: str,
    ) -> RequirementAnalysis:

        prompt = USER_PROMPT.format(
            summary=summary,
            description=description,
        )

        response = self.ai.generate(
            SYSTEM_PROMPT,
            prompt,
        )

        data = json.loads(response.content)

        return RequirementAnalysis(**data)