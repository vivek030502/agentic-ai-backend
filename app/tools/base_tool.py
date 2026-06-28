from abc import ABC, abstractmethod
from typing import Any


class BaseTool(ABC):
    """
    Base class for all tools.

    Every tool must implement the execute() method.
    """

    @property
    @abstractmethod
    def action(self) -> str:
        """
        Returns the action name handled by this tool.
        """
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        """
        Human-readable description of the tool.
        """
        pass

    @property
    def parameters(self) -> dict:
        """
        Expected parameters for this tool.

        Override in child classes.
        """
        return {}
    
    @abstractmethod
    def execute(self, parameters: dict):
        """
        Execute the tool.

        Returns:
            Any: Tool execution result.
        """
        pass