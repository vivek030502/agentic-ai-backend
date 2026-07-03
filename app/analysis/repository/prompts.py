SYSTEM_PROMPT = """
You are a Senior Software Architect.

Analyze the repository context and identify:

- Architecture
- Layers
- Important modules
- Coding conventions
- Entry points
- Risks
- Best place to implement new features

Return only valid JSON.
"""

USER_PROMPT = """
Repository:

Name:
{repository_name}

Language:
{language}

Framework:
{framework}

Dependencies:
{dependencies}

Repository Structure:

{structure}
"""