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
from app.repository.file_writer import RepositoryFileWriter
from app.repository.git_repository import GitRepository


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

        self.writer = RepositoryFileWriter()

        self.git = GitRepository()

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

        written_files = self.writer.write(
            repository_path=context.repository_path,
            response=parsed,
        )

        committed = self.git.commit_and_push(
            repository_path=context.repository_path,
            branch=request.branch,
            commit_message=f"{request.jira_key}: AI generated implementation",
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

            message=(
                "Code generated, committed and pushed successfully."
                if committed
                else "Code generated successfully. No new changes to commit."
            ),
        )