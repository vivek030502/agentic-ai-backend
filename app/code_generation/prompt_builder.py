from app.code_generation.models import CodeGenerationContext
from app.code_generation.prompts import SYSTEM_PROMPT


class PromptBuilder:
    """
    Converts all available context
    into one prompt.
    """

    def build(
        self,
        context: CodeGenerationContext
    ) -> str:

        prompt = f"""
Repository:
{context.repository}

Branch:
{context.branch}

Jira Key:
{context.jira_key}

Summary:
{context.jira_summary}

Description:
{context.jira_description}

Repository Analysis:
{context.repository_summary}

Files To Generate:
"""

        for file in context.suggested_files:
            prompt += f"\n- {file}"

        prompt += "\n\nRelevant Existing Code:\n"

        for document in context.rag_documents:

            prompt += f"""

==============================
FILE : {document.file_path}
==============================

{document.content}

"""

        prompt += """

Generate complete implementation.

Return ONLY JSON.

"""

        return SYSTEM_PROMPT + "\n\n" + prompt