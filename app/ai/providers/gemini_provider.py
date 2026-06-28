from litellm import completion

from app.ai.models import AIResponse, TokenUsage
from app.ai.providers.base_provider import BaseProvider
from app.config.logger import app_logger
from app.config.settings import settings


class GeminiProvider(BaseProvider):
    """
    Gemini LLM provider implementation using LiteLLM.
    """

    def generate(
        self,
        system_prompt: str,
        user_prompt: str
    ) -> AIResponse:

        app_logger.info("Calling Gemini API...")

        try:

            response = completion(
                model=settings.LLM_MODEL,
                api_key=settings.GEMINI_API_KEY,
                messages=[
                    {
                        "role": "system",
                        "content": system_prompt
                    },
                    {
                        "role": "user",
                        "content": user_prompt
                    }
                ]
            )

            return AIResponse(
                content=response.choices[0].message.content,
                provider="gemini",
                model=response.model,
                usage=TokenUsage(
                    prompt_tokens=response.usage.prompt_tokens,
                    completion_tokens=response.usage.completion_tokens,
                    total_tokens=response.usage.total_tokens
                ),
                finish_reason=response.choices[0].finish_reason
            )

        except Exception as ex:

            app_logger.exception(ex)

            raise