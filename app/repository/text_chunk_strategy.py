import uuid

from app.repository.chunk_strategy import ChunkStrategy
from app.repository.models import RepositoryChunk, RepositoryFile


class TextChunkStrategy(ChunkStrategy):
    """
    Default chunking strategy.

    Splits text using fixed-size overlapping chunks.
    """

    CHUNK_SIZE = 1500
    CHUNK_OVERLAP = 200

    def chunk(
        self,
        repository: str,
        branch: str,
        file: RepositoryFile
    ) -> list[RepositoryChunk]:

        content = file.content

        chunks = []

        start = 0
        chunk_index = 0

        while start < len(content):

            end = min(
                start + self.CHUNK_SIZE,
                len(content)
            )

            chunk_content = content[start:end]

            chunks.append(
                RepositoryChunk(
                    id=str(uuid.uuid4()),
                    repository=repository,
                    branch=branch,
                    file_path=file.path,
                    language=self.detect_language(file.extension),
                    chunk_index=chunk_index,
                    total_chunks=0,
                    content=chunk_content,
                    metadata={
                        "file_name": file.name,
                        "extension": file.extension,
                        "language": file.language
                    }
                )
            )

            chunk_index += 1

            start += (
                self.CHUNK_SIZE -
                self.CHUNK_OVERLAP
            )

        total = len(chunks)

        for chunk in chunks:
            chunk.total_chunks = total

        return chunks

    def detect_language(self, extension: str) -> str:

        mapping = {
            ".py": "python",
            ".java": "java",
            ".js": "javascript",
            ".ts": "typescript",
            ".vue": "vue",
            ".html": "html",
            ".css": "css",
            ".xml": "xml",
            ".json": "json",
            ".yml": "yaml",
            ".yaml": "yaml",
            ".sql": "sql",
            ".md": "markdown",
        }

        return mapping.get(extension.lower(), "text")