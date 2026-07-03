from fastapi import APIRouter

from app.agent.core import AgentCore
from app.schemas.agent import AgentRequest, AgentResponse
from app.agent.state import AgentStatus

router = APIRouter(
    prefix="/agent",
    tags=["Agent"],
)

agent = AgentCore()


@router.post(
    "/run",
    response_model=AgentResponse
)
def run_agent(request: AgentRequest):

    state = agent.run(request.query)

    return AgentResponse(
        success=state.status == AgentStatus.COMPLETED,
        message=state.final_response or ""
    )