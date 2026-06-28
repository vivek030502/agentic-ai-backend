from app.config.settings import settings

print("=" * 50)
print("LLM Configuration")
print("=" * 50)

print(f"Provider : {settings.LLM_PROVIDER}")
print(f"Model    : {settings.LLM_MODEL}")
print(f"API Key  : {settings.GEMINI_API_KEY[:10]}...")