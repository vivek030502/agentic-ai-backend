from datetime import datetime

from app.config.logger import app_logger
from app.rag.service import RAGService
from app.repository.chunk_builder import ChunkBuilder
from app.repository.models import (
    RepositoryIndexRequest,
    RepositoryIndexResponse,
)
from app.repository.scanner import RepositoryScanner


class RepositoryIndexer:
    """
    Complete repository indexing pipeline.

    Repository
        ↓
    Scanner
        ↓
    Chunk Builder
        ↓
    ChromaDB
    """

    def __init__(self):

        self.scanner = RepositoryScanner()

        self.chunk_builder = ChunkBuilder()

        self.rag = RAGService()

    def index_repository(
        self,
        request: RepositoryIndexRequest
    ) -> RepositoryIndexResponse:

        started = datetime.utcnow()

        app_logger.info(
            f"Indexing repository {request.repository}"
        )

        # -------------------------------------------------
        # Scan Repository
        # -------------------------------------------------

        # files = self.scanner.scan(
        #     request.local_path
        # )
        directories, files = self.scanner.scan(
            request.local_path
        )

        # -------------------------------------------------
        # Build Chunks
        # -------------------------------------------------

        chunks = self.chunk_builder.build_chunks(
            repository=request.repository,
            branch=request.branch,
            files=files
        )

        # -------------------------------------------------
        # Create Collection
        # -------------------------------------------------

        try:

            self.rag.create_collection(
                request.repository
            )

        except Exception:
            pass

        # -------------------------------------------------
        # Index
        # -------------------------------------------------

        ids = []

        documents = []

        metadatas = []

        for chunk in chunks:

            ids.append(chunk.id)

            documents.append(chunk.content)

            metadatas.append(
                {
                    **chunk.metadata,
                    "repository": chunk.repository,
                    "branch": chunk.branch,
                    "file_path": chunk.file_path,
                    "chunk_index": chunk.chunk_index,
                    "total_chunks": chunk.total_chunks,
                }
            )

        self.rag.add_documents(
            collection_name=request.repository,
            ids=ids,
            documents=documents,
            metadatas=metadatas
        )

        completed = datetime.utcnow()

        return RepositoryIndexResponse(
            success=True,
            repository=request.repository,
            total_files=len(files),
            indexed_files=len(files),
            total_chunks=len(chunks),
            collection_name=request.repository,
            started_at=started,
            completed_at=completed,
            message="Repository indexed successfully."
        )