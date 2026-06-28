# This is the brain. It coordinates everything.

from app.agent.executor import Executor
from app.agent.planner import Planner
from app.agent.state import AgentState, AgentStatus
from app.config.logger import app_logger


class AgentCore:
    """
    Main orchestration class for the Agent.

    Coordinates the complete lifecycle of an agent execution:
    - Create execution state
    - Generate execution plan
    - Execute planned actions
    - Return final state
    """

    def __init__(self):
        self.planner = Planner()
        self.executor = Executor()

    def run(self, query: str) -> AgentState:
        """
        Execute an agent request.

        Args:
            query: User's natural language instruction.

        Returns:
            AgentState: Final execution state.
        """

        app_logger.info("=" * 60)
        app_logger.info("Starting Agent Execution")
        app_logger.info(f"User Query: {query}")

        # Create execution state
        state = AgentState(query=query)

        try:

            app_logger.info("Agent state created.")

            # Generate execution plan using AI
            plan = self.planner.create_plan(state.query)

            # Store the generated plan inside the agent state
            state.plan = plan.steps

            app_logger.info("Execution plan generated successfully.")

            for index, step in enumerate(state.plan, start=1):
                app_logger.info(
                    f"Step {index}: {step.action} | Parameters: {step.parameters}"
                )

            # Execute the generated plan
            state = self.executor.execute(state)

            app_logger.info("Agent execution completed successfully.")

            return state

        except Exception as ex:

            app_logger.exception(f"Agent execution failed: {str(ex)}")

            # Update the existing execution state instead of creating a new one.
            # This preserves the execution plan, completed steps, tool results,
            # and other debugging information.

            state.status = AgentStatus.FAILED
            state.error = str(ex)
            state.final_response = "Agent execution failed."

            return state