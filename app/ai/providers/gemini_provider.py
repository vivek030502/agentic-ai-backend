# 


from litellm import completion

from app.ai.models import AIResponse
from app.ai.models import TokenUsage

from app.ai.providers.base_provider import BaseProvider

from app.config.logger import app_logger
from app.config.settings import settings


class GeminiProvider(BaseProvider):

    def generate(
        self,
        system_prompt: str,
        user_prompt: str,
        response_format=None,
    ) -> AIResponse:

        app_logger.info("Calling Gemini")

        kwargs = {

            "model": settings.LLM_MODEL,

            "api_key": settings.GEMINI_API_KEY,

            "messages": [

                {
                    "role": "system",
                    "content": system_prompt,
                },

                {
                    "role": "user",
                    "content": user_prompt,
                },

            ],

        }

        if response_format is not None:
            kwargs["response_format"] = response_format

        response = completion(**kwargs)

        return AIResponse(

            content=response.choices[0].message.content,

            provider="gemini",

            model=response.model,

            usage=TokenUsage(

                prompt_tokens=response.usage.prompt_tokens,

                completion_tokens=response.usage.completion_tokens,

                total_tokens=response.usage.total_tokens,

            ),

            finish_reason=response.choices[0].finish_reason,

        )