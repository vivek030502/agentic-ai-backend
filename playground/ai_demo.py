from app.ai.service import AIService

service = AIService()

response = service.generate(
    system_prompt="You are an AI Planner.",
    user_prompt="Create GitHub repository and create Jira ticket."
)

print(response)