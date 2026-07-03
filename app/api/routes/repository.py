from fastapi import APIRouter

from app.repository.models import (
    RepositoryIndexRequest,
    RepositoryIndexResponse,
)
from app.repository.repository_indexer import RepositoryIndexer

router = APIRouter(
    prefix="/repository",
    tags=["Repository"],
)

indexer = RepositoryIndexer()


@router.post(
    "/index",
    response_model=RepositoryIndexResponse,
)
def index_repository(
    request: RepositoryIndexRequest,
):

    return indexer.index_repository(
        request
    )