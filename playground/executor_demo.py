from app.agent.executor import Executor
from app.agent.planner import Planner
from app.agent.state import AgentState

state = AgentState(
    query="Create GitHub repository and create Jira story"
)

planner = Planner()
executor = Executor()

state = planner.create_plan(state)
state = executor.execute(state)

print(state.model_dump())