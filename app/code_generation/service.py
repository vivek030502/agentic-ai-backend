from app.config.logger import app_logger

from app.code_generation.api_models import (
    CodeGenerationRequest,
    CodeGenerationResult,
)

from app.code_generation.context_builder import (
    ContextBuilder,
)

from app.code_generation.generator import (
    CodeGenerator,
)

from app.code_generation.parser import (
    CodeParser,
)


class CodeGenerationService:
    """
    Main orchestration service.

    Flow

        Jira
          ↓

        Analysis
          ↓

        RAG
          ↓

        Prompt
          ↓

        Gemini
          ↓

        Parser
    """

    def __init__(self):

        self.context_builder = ContextBuilder()

        self.generator = CodeGenerator()

        self.parser = CodeParser()

    def generate_code(
        self,
        request: CodeGenerationRequest,
    ) -> CodeGenerationResult:

        app_logger.info(
            "====================================="
        )

        app_logger.info(
            "Starting AI Code Generation"
        )

        app_logger.info(
            f"Repository : {request.repository}"
        )

        app_logger.info(
            f"Branch : {request.branch}"
        )

        app_logger.info(
            f"Jira : {request.jira_key}"
        )

        # ------------------------------------
        # Build Context
        # ------------------------------------

        context = self.context_builder.build(

            repository=request.repository,

            branch=request.branch,

            jira_key=request.jira_key,

        )

        app_logger.info(
            "Context created successfully."
        )

        # ------------------------------------
        # Call Gemini
        # ------------------------------------

        llm_response = self.generator.generate(
            context
        )

        app_logger.info(
            "LLM response received."
        )

        # ------------------------------------
        # Parse JSON
        # ------------------------------------

        parsed = self.parser.parse(
            llm_response
        )

        app_logger.info(
            f"{len(parsed.files)} files generated."
        )

        app_logger.info(
            "AI Code Generation Completed"
        )

        return CodeGenerationResult(

            success=True,

            repository=request.repository,

            branch=request.branch,

            jira_key=request.jira_key,

            total_files=len(parsed.files),

            files=parsed.files,

            message="Code generated successfully.",
        )