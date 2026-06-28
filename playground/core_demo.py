from app.agent.core import AgentCore

agent = AgentCore()

state = agent.run(
    "Create GitHub repository and create Jira story"
)

print(state.model_dump())