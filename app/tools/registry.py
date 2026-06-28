from app.tools.base_tool import BaseTool
from app.tools.github_tool import GitHubTool
from app.tools.jira_tool import JiraTool


class ToolRegistry:
    """
    Registers and provides access to all available tools.
    """

    def __init__(self):
        self._tools: dict[str, BaseTool] = {}

        self.register(GitHubTool())
        self.register(JiraTool())

    def register(self, tool: BaseTool) -> None:
        """
        Register a tool by its action.
        Raises:
            ValueError: If another tool with the same action
            is already registered.
        """
        if tool.action in self._tools:
            raise ValueError(
                f"Tool already registered for action: {tool.action}"
            )
        self._tools[tool.action] = tool

    def get_tool(self, action: str) -> BaseTool | None:
        """
        Return the tool responsible for the given action.
        """
        return self._tools.get(action)

    def list_actions(self) -> list[str]:
        """
        Return all registered actions.
        """
        return list(self._tools.keys())

    def get_available_tools(self) -> list[dict]:
        """
        Returns metadata for all registered tools.

        This metadata is used by the AI Planner to dynamically
        discover the capabilities of the system.
        """

        available_tools = []

        for tool in self._tools.values():

            available_tools.append(
                {
                    "action": tool.action,
                    "description": tool.description,
                    "parameters": tool.parameters
                }
            )

        return available_tools