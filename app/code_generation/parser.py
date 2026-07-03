from app.code_generation.models import (
    CodeGenerationResponse,
    GeneratedFile,
)


class CodeParser:
    """
    Converts Gemini JSON
    into strongly typed objects.
    """

    def parse(
        self,
        response: dict,
    ) -> CodeGenerationResponse:

        files = []

        for item in response["files"]:

            files.append(

                GeneratedFile(

                    file_path=item["file_path"],

                    language=item["language"],

                    content=item["content"],

                )

            )

        return CodeGenerationResponse(
            files=files
        )