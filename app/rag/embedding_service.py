from sentence_transformers import SentenceTransformer

from app.config.logger import app_logger
from app.rag.exceptions import EmbeddingException
from app.config.settings import settings


class EmbeddingService:
    """
    Generates vector embeddings for repository documents.

    Uses a local SentenceTransformer model to avoid
    API costs and improve indexing speed.
    """

    MODEL_NAME = settings.EMBEDDING_MODEL

    def __init__(self):

        app_logger.info(
            f"Loading embedding model: {self.MODEL_NAME}"
        )

        self.model = SentenceTransformer(
            self.MODEL_NAME
        )

        app_logger.info(
            "Embedding model loaded successfully."
        )

    def embed(
        self,
        text: str
    ) -> list[float]:
        """
        Generate embedding for a single text.
        """

        try:

            embedding = self.model.encode(
                text,
                normalize_embeddings=True
            )

            return embedding.tolist()

        except Exception as ex:

            raise EmbeddingException(str(ex))

    def embed_batch(
        self,
        texts: list[str]
    ) -> list[list[float]]:
        """
        Generate embeddings for multiple texts.
        """

        try:

            embeddings = self.model.encode(
                texts,
                normalize_embeddings=True
            )

            return embeddings.tolist()

        except Exception as ex:

            raise EmbeddingException(str(ex))