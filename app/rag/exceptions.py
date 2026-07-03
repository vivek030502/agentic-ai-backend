class RAGException(Exception):
    """
    Base exception for RAG module.
    """

    pass


class CollectionAlreadyExistsException(RAGException):
    """
    Raised when collection already exists.
    """

    pass


class CollectionNotFoundException(RAGException):
    """
    Raised when collection does not exist.
    """

    pass


class EmbeddingException(RAGException):
    """
    Raised when embedding generation fails.
    """

    pass