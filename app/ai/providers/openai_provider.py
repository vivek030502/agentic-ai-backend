from app.ai.providers.base_provider import BaseProvider
from app.config.logger import app_logger


class OpenAIProvider(BaseProvider):
    """
    Mock OpenAI provider.

    Later, this class will call the real OpenAI API.
    """

    def generate(self, system_prompt: str, user_prompt: str) -> str:

        app_logger.info("Calling Mock OpenAI Provider")

        app_logger.debug(f"System Prompt: {system_prompt}")
        app_logger.debug(f"User Prompt: {user_prompt}")

        # Temporary mocked response
        return """
        CREATE_GITHUB_REPOSITORY
        CREATE_JIRA_TICKET
        """