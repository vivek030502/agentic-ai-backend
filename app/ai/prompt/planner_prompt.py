import json


class PlannerPrompt:
    """
    Responsible for building prompts for the AI Planner.
    """

    @staticmethod
    def build_system_prompt(
        available_tools: list[dict]
    ) -> str:
        """
        Build the system prompt dynamically using
        registered tool metadata.
        """

        tool_information = json.dumps(
            available_tools,
            indent=4
        )

        return f"""
You are an Enterprise AI Planning Agent.

Your responsibility is to convert the user's request into an execution plan.

You MUST use ONLY the tools listed below.

If no suitable tool exists,
return an empty execution plan.

Rules:

1. Return ONLY valid JSON.
2. Do NOT explain your reasoning.
3. Do NOT use markdown.
4. Do NOT invent actions.
5. Every action must exactly match one of the available tools.

Available Tools:

{tool_information}

Output Format:

{{
    "steps": [
        {{
            "action": "...",
            "parameters": {{}}
        }}
    ]
}}
"""

    @staticmethod
    def build_user_prompt(
        user_query: str
    ) -> str:

        return f"""
User Request:

{user_query}
"""