from fastapi import FastAPI

from app.api.router import api_router
from app.config.logger import app_logger
from app.config.settings import settings
from app.api.routes.repository import (
    router as repository_router
)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)


@app.on_event("startup")
async def startup():

    app_logger.info("Starting Agentic AI Backend...")


app.include_router(api_router)

api_router.include_router(
    repository_router
)