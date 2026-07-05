from pathlib import Path

from app.code_generation.models import CodeGenerationResponse


class RepositoryFileWriter:
    """
    Writes generated files
    into the cloned repository.
    """

    def write(
        self,
        repository_path: str,
        response: CodeGenerationResponse,
    ) -> list[str]:

        written_files = []

        root = Path(repository_path)

        for generated in response.files:

            full_path = root / generated.file_path

            full_path.parent.mkdir(
                parents=True,
                exist_ok=True,
            )

            full_path.write_text(
                generated.content,
                encoding="utf-8",
            )

            written_files.append(str(full_path))

        return written_files