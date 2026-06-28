from app.ai.prompt.planner_prompt import PlannerPrompt
from app.ai.service import AIService

service = AIService()

system_prompt = PlannerPrompt.get_system_prompt()

user_prompt = PlannerPrompt.build_user_prompt(
    "Create a GitHub repository named employee-service and create a Jira ticket for backend development."
)

response = service.generate(
    system_prompt=system_prompt,
    user_prompt=user_prompt
)

print("=" * 80)
print("RAW LLM RESPONSE")
print("=" * 80)

print(response.content)

print("\n")

print("=" * 80)
print("MODEL INFORMATION")
print("=" * 80)

print(f"Provider : {response.provider}")
print(f"Model    : {response.model}")
print(f"Usage    : {response.usage.model_dump()}")