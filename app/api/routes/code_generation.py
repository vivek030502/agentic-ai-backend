from fastapi import APIRouter

from app.code_generation.api_models import (
    CodeGenerationRequest,
    CodeGenerationResult,
)

from app.code_generation.service import (
    CodeGenerationService,
)

router = APIRouter(
    prefix="/code",
    tags=["Code Generation"],
)

service = CodeGenerationService()


@router.post(
    "/generate",
    response_model=CodeGenerationResult,
)
def generate_code(
    request: CodeGenerationRequest,
):

    return service.generate_code(
        request
    )