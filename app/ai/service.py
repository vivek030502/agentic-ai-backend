from app.ai.providers.factory import ProviderFactory
from app.config.settings import settings
from app.ai.models import AIResponse


class AIService:
    """
    Central service responsible for interacting with the configured AI provider.
    """

    def __init__(self):
        # Later, this will be selected dynamically
        # based on configuration (OpenAI, Gemini, Ollama, etc.)
        self.provider = ProviderFactory.create(
            settings.LLM_PROVIDER
        )

    def generate(self, system_prompt: str, user_prompt: str) -> AIResponse:
        """
        Generate a response using the configured provider.
        """
        return self.provider.generate(system_prompt, user_prompt)