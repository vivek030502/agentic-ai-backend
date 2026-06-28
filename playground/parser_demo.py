from app.ai.parser.planner_parser import PlannerParser

sample_response = """
{
    "steps": [
        {
            "action": "CREATE_GITHUB_REPOSITORY",
            "parameters": {
                "repository_name": "employee-service"
            }
        },
        {
            "action": "CREATE_JIRA_TICKET",
            "parameters": {
                "summary": "Backend Development"
            }
        }
    ]
}
"""

plan = PlannerParser.parse(sample_response)

print("=" * 80)
print("PLANNER RESPONSE")
print("=" * 80)

print(plan)

print("\nSteps:")

for step in plan.steps:
    print(f"- {step.action}")
    print(f"  Parameters: {step.parameters}")