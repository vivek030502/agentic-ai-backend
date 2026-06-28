# Planner decides: What should I do?

from app.ai.parser.planner_parser import PlannerParser
from app.ai.prompt.planner_prompt import PlannerPrompt
from app.ai.service import AIService
from app.tools.registry import ToolRegistry


class Planner:
    """
    AI-powered planner responsible for converting
    user requests into executable plans.
    """

    def __init__(self):
        self.ai_service = AIService()
        self.registry = ToolRegistry()

    def create_plan(self, user_query: str):

        available_tools = (
            self.registry.get_available_tools()
        )

        system_prompt = (
            PlannerPrompt.build_system_prompt(
                available_tools
            )
        )

        user_prompt = (
            PlannerPrompt.build_user_prompt(
                user_query
            )
        )

        response = self.ai_service.generate(
            system_prompt,
            user_prompt
        )

        return PlannerParser.parse(
            response.content
        )