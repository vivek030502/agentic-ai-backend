# from app.ai.service import AIService

# service = AIService()

# response = service.generate(
#     system_prompt="You are an AI Planner.",
#     user_prompt="Create GitHub repository and Jira ticket."
# )

# print("=" * 60)
# print("AI RESPONSE")
# print("=" * 60)

# print("Provider :", response.provider)
# print("Model    :", response.model)
# print("Content  :")
# print(response.content)

# print("\nToken Usage")
# print(response.usage.model_dump())


from app.ai.service import AIService

service = AIService()

response = service.generate(
    system_prompt="""
You are an AI Planning Assistant.

Answer in one short paragraph.
""",
    user_prompt="""
Explain what GitHub is in 50 words.
"""
)

print("=" * 60)
print("Provider :", response.provider)
print("Model    :", response.model)

print("\nContent\n")
print(response.content)

print("\nToken Usage")
print(response.usage.model_dump())