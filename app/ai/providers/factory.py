from app.ai.providers.gemini_provider import GeminiProvider


class ProviderFactory:
    """
    Factory responsible for creating the configured AI provider.
    """

    @staticmethod
    def create(provider_name: str):

        provider_name = provider_name.lower()

        if provider_name == "gemini":
            return GeminiProvider()

        raise ValueError(
            f"Unsupported provider: {provider_name}"
        )