from abc import ABC, abstractmethod

from app.repository.models import RepositoryChunk, RepositoryFile


class ChunkStrategy(ABC):
    """
    Base interface for all chunking strategies.
    """

    @abstractmethod
    def chunk(
        self,
        repository: str,
        branch: str,
        file: RepositoryFile
    ) -> list[RepositoryChunk]:
        """
        Split a repository file into chunks.
        """
        pass