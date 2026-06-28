from pydantic import BaseModel, Field


class TokenUsage(BaseModel):
    """
    Token usage information returned by the LLM.
    """

    prompt_tokens: int = 0
    completion_tokens: int = 0
    total_tokens: int = 0


class AIResponse(BaseModel):
    """
    Standard response returned by every AI provider.
    """

    content: str

    provider: str

    model: str

    usage: TokenUsage = Field(default_factory=TokenUsage)

    finish_reason: str | None = None