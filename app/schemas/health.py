from pydantic import BaseModel


class HealthResponse(BaseModel):
    """
    Response schema for the Health Check API.

    This schema defines the structure of the response returned
    when checking the application's health status.
    """

    status: str
    application: str
    version: str
    environment: str