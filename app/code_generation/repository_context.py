from app.config.logger import app_logger
from app.rag.models import SearchRequest
from app.rag.service import RAGService


class RepositoryAnalysisContext:
    """
    Retrieves the most relevant repository files
    from ChromaDB.
    """

    def __init__(self):

        self.rag = RAGService()

    def retrieve(
        self,
        repository: str,
        query: str,
        top_k: int = 8,
    ) -> list[dict]:

        app_logger.info(
            f"Searching repository context for '{query}'"
        )

        response = self.rag.search(
            SearchRequest(
                collection_name=repository,
                query=query,
                top_k=top_k,
            )
        )

        results = []

        for item in response.results:

            results.append(
                {
                    "file_path": item.metadata.get(
                        "file_path",
                        ""
                    ),
                    "language": item.metadata.get(
                        "language",
                        ""
                    ),
                    "content": item.document,
                    "score": item.score,
                }
            )

        return results