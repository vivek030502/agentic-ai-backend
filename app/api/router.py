from fastapi import APIRouter

from app.api.routes.agent import router as agent_router
from app.api.routes.health import router as health_router
from app.api.routes.jira import router as jira_router
from app.api.routes.github import router as github_router
from app.api.routes.rag import router as rag_router
from app.api.routes.repository import router as repository_router
from app.api.routes.workspace import router as workspace_router
from app.api.routes.code_generation import (
    router as code_generation_router,
)

api_router = APIRouter()

api_router.include_router(
    health_router
)

api_router.include_router(
    agent_router
)

api_router.include_router(
    github_router
)

api_router.include_router(
    jira_router
)

api_router.include_router(
    rag_router
)

api_router.include_router(
    repository_router
)

api_router.include_router(
    workspace_router
)

api_router.include_router(
    code_generation_router
)