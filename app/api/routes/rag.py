from fastapi import APIRouter

from app.rag.api_models import (
    AddDocumentsRequest,
    CollectionListResponse,
    CollectionResponse,
    CountDocumentsRequest,
    CountDocumentsResponse,
    CreateCollectionRequest,
    DeleteCollectionRequest,
    IndexDocumentsResponse,
)

from app.rag.models import (
    SearchRequest,
    SearchResponse,
)

from app.rag.service import RAGService

router = APIRouter(
    prefix="/rag",
    tags=["RAG"],
)

service = RAGService()


@router.post(
    "/collection/create",
    response_model=CollectionResponse,
)
def create_collection(
    request: CreateCollectionRequest,
):

    return service.create_collection(
        request.collection_name
    )


@router.delete(
    "/collection/delete",
    response_model=CollectionResponse,
)
def delete_collection(
    request: DeleteCollectionRequest,
):

    return service.delete_collection(
        request.collection_name
    )


@router.get(
    "/collections",
    response_model=CollectionListResponse,
)
def list_collections():

    return service.list_collections()


@router.post(
    "/documents",
    response_model=IndexDocumentsResponse,
)
def add_documents(
    request: AddDocumentsRequest,
):

    return service.add_documents(
        collection_name=request.collection_name,
        ids=request.ids,
        documents=request.documents,
        metadatas=request.metadatas,
    )


@router.post(
    "/collection/count",
    response_model=CountDocumentsResponse,
)
def count_documents(
    request: CountDocumentsRequest,
):

    return service.count_documents(
        request.collection_name
    )


@router.post(
    "/search",
    response_model=SearchResponse,
)
def search(
    request: SearchRequest,
):

    return service.search(request)