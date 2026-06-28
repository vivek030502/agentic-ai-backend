import json

from app.ai.planner_models import PlannerResponse


class PlannerParser:
    """
    Converts raw LLM JSON into validated PlannerResponse objects.
    """

    @staticmethod
    def parse(response: str) -> PlannerResponse:
        """
        Parse and validate the LLM response.

        Args:
            response: Raw JSON string returned by the LLM.

        Returns:
            PlannerResponse: Validated execution plan.
        """

        data = json.loads(response)

        return PlannerResponse.model_validate(data)