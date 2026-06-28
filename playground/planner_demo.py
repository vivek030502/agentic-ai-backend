# from app.agent.planner import Planner
# from app.agent.state import AgentState


# planner = Planner()

# state = AgentState(
#     query="Create GitHub repository and create Jira story"
# )

# updated_state = planner.create_plan(state)

# print(updated_state.model_dump())


from app.agent.planner import Planner

planner = Planner()

plan = planner.create_plan(
    """
    Create a GitHub repository named employee-service
    and create a Jira ticket for backend development.
    """
)

print("=" * 80)
print("EXECUTION PLAN")
print("=" * 80)

for index, step in enumerate(plan.steps, start=1):

    print(f"\nStep {index}")

    print(f"Action     : {step.action}")

    print(f"Parameters : {step.parameters}")