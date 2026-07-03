from fastapi import APIRouter

from app.config.logger import app_logger
from app.config.settings import settings
from app.schemas.health import HealthResponse

router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get(
    "",
    response_model=HealthResponse,
    summary="Health Check",
    description="Returns application health status."
)
def health():

    app_logger.info("Health endpoint called.")

    return {
        "status": "UP",
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "environment": settings.APP_ENV
    }