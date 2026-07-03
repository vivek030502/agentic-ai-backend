import json

from app.ai.service import AIService
from app.analysis.repository.prompts import (
    SYSTEM_PROMPT,
    USER_PROMPT,
)
from app.analysis.repository.models import (
    RepositoryContext,
)


class RepositoryAnalyzer:
    """
    Uses the LLM to understand the repository.

    This class does NOT scan the repository.
    It only converts RepositoryContext into an
    architectural summary.
    """

    def __init__(self):

        self.ai = AIService()

    def analyze(
        self,
        context: RepositoryContext,
    ) -> str:
        """
        Returns a repository architecture summary.
        """

        structure = []

        for directory in context.directories:
            structure.append(f"[DIR] {directory.path}")

        for file in context.files:
            structure.append(f"[FILE] {file.path}")

        dependencies = ", ".join(
            dependency.name
            for dependency in context.dependencies
        )

        prompt = USER_PROMPT.format(
            repository_name=context.repository_name,
            language=context.language or "",
            framework=context.framework or "",
            dependencies=dependencies,
            structure="\n".join(structure),
        )

        response = self.llm.chat(
            system_prompt=SYSTEM_PROMPT,
            user_prompt=prompt,
        )

        return self._parse(response)

    def _parse(
        self,
        response: str,
    ) -> str:
        """
        Convert LLM JSON response into
        formatted text.
        """

        try:

            data = json.loads(response)

            lines = []

            if "architecture" in data:
                lines.append(
                    f"Architecture: {data['architecture']}"
                )

            if "layers" in data:

                lines.append("")

                lines.append("Layers:")

                for layer in data["layers"]:
                    lines.append(
                        f"- {layer}"
                    )

            if "modules" in data:

                lines.append("")

                lines.append("Modules:")

                for module in data["modules"]:
                    lines.append(
                        f"- {module}"
                    )

            if "entry_points" in data:

                lines.append("")

                lines.append("Entry Points:")

                for entry in data["entry_points"]:
                    lines.append(
                        f"- {entry}"
                    )

            if "coding_conventions" in data:

                lines.append("")

                lines.append("Coding Conventions:")

                for convention in data["coding_conventions"]:
                    lines.append(
                        f"- {convention}"
                    )

            if "best_location" in data:

                lines.append("")

                lines.append(
                    f"Best Location: {data['best_location']}"
                )

            if "risks" in data:

                lines.append("")

                lines.append("Risks:")

                for risk in data["risks"]:
                    lines.append(
                        f"- {risk}"
                    )

            return "\n".join(lines)

        except Exception:

            return response