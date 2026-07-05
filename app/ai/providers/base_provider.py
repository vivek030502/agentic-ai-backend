# from abc import ABC, abstractmethod
# from app.ai.models import AIResponse


# class BaseProvider(ABC):
#     """
#     Abstract base class for all LLM providers.

#     Every AI provider (OpenAI, Gemini, Ollama, Claude, etc.)
#     must implement the same interface.

#     This allows the rest of the application to remain
#     provider-independent.
#     """

#     @abstractmethod
#     def generate(self, system_prompt: str, user_prompt: str) -> AIResponse:
#         """
#         Generate a response from the LLM.

#         Args:
#             system_prompt: Instructions that define the AI's behavior.
#             user_prompt: The user's request.

#         Returns:
#             The model's generated response.
#         """
#         pass


from abc import ABC
from abc import abstractmethod

from app.ai.models import AIResponse


class BaseProvider(ABC):

    @abstractmethod
    def generate(
        self,
        system_prompt: str,
        user_prompt: str,
        response_format=None,
    ) -> AIResponse:
        pass