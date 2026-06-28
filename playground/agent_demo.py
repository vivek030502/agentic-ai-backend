from app.agent.core import AgentCore

agent = AgentCore()

state = agent.run(
    """
    Create a private GitHub repository named
    employee-service-agent
    with description
    Backend created by my Agentic AI.
    """
)

print("=" * 80)
print("FINAL RESPONSE")
print("=" * 80)

print(state.final_response)

print()

print(state.tool_results)