from app.ai.service import AIService
from app.code_generation.prompt_builder import PromptBuilder
from app.code_generation.models import (
    CodeGenerationContext,
    CodeGenerationResponse,
)
from app.code_generation.prompts import SYSTEM_PROMPT


class CodeGenerator:
    """
    Calls the configured LLM
    to generate source code.
    """

    def __init__(self):

        self.builder = PromptBuilder()

        self.ai = AIService()

    def generate(
        self,
        context: CodeGenerationContext,
    ) -> str:

        # prompt = self.builder.build(
        #     context
        # )

        # response = self.ai.generate(
        #     system_prompt="",
        #     user_prompt=prompt,
        # )

        # return response.content

        user_prompt = self.builder.build(
            context
        )

        response = self.ai.generate(

            system_prompt=SYSTEM_PROMPT,

            user_prompt=user_prompt,

            response_format=CodeGenerationResponse,

        )

        return response.content