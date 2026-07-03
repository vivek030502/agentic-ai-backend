from app.repository.models import RepositoryChunk, RepositoryFile
from app.repository.text_chunk_strategy import TextChunkStrategy


class ChunkBuilder:
    """
    Converts RepositoryFile objects into RepositoryChunks.
    """

    def __init__(self):

        self.strategy = TextChunkStrategy()

    def build_chunks(
        self,
        repository: str,
        branch: str,
        files: list[RepositoryFile]
    ) -> list[RepositoryChunk]:

        chunks = []

        for file in files:

            chunks.extend(
                self.strategy.chunk(
                    repository,
                    branch,
                    file
                )
            )

        return chunks