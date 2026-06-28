# Responsible for: Reading .env, Validating configuration, Providing configuration to the entire application

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    # Application
    APP_NAME: str
    APP_VERSION: str
    APP_ENV: str
    DEBUG: bool

    # Server
    HOST: str
    PORT: int

    # GitHub
    GITHUB_BASE_URL: str
    GITHUB_TOKEN: str 

    # Jira
    JIRA_BASE_URL: str
    JIRA_EMAIL: str 
    JIRA_API_TOKEN: str

    # LLM
    # llm_provider: str = "openai"
    # llm_model: str = "gpt-4.1-mini"
    # openai_api_key: str
    LLM_PROVIDER: str = "gemini"
    LLM_MODEL: str = "gemini/gemini-2.5-flash"
    GEMINI_API_KEY: str

    # Logging
    LOG_LEVEL: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        extra="ignore"
    )

# Create the Settings object only once.
# Every time get_settings() is called, Python returns the same
# cached object instead of creating a new one.
# This avoids repeatedly reading the .env file.
# Cache the Settings instance so the .env file is loaded only once.
@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
