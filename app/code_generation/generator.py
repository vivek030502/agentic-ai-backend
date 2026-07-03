import json

from app.ai.providers.gemini_provider import GeminiProvider
from app.code_generation.prompt_builder import PromptBuilder
from app.code_generation.models import (
    CodeGenerationContext,
)


class CodeGenerator:
    """
    Calls Gemini
    to generate source code.
    """

    def __init__(self):

        self.builder = PromptBuilder()

        self.llm = GeminiProvider()

    def generate(
        self,
        context: CodeGenerationContext,
    ) -> dict:

        prompt = self.builder.build(
            context
        )

        response = self.ai.generate(
            system_prompt,
            user_prompt,
        )

        return json.loads(response)