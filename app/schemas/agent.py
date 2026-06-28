from pydantic import BaseModel, Field


class AgentRequest(BaseModel):
    """
    Request schema for the AI Agent.
    """

    query: str = Field(
        ...,
        min_length=5,
        max_length=1000,
        description="Natural language instruction for the AI agent."
    )


class AgentResponse(BaseModel):
    """
    Standard response returned by the AI Agent.
    """

    success: bool
    message: str