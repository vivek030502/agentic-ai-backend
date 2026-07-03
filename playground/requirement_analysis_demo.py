from app.analysis.requirement_analyzer import RequirementAnalyzer


summary = "Implement Login API"

description = """
Create a login endpoint.

Validate email and password.

Generate JWT token.

Return authentication response.

Handle invalid credentials.
"""

analyzer = RequirementAnalyzer()

response = analyzer.analyze(
    summary,
    description,
)

print("=" * 80)
print("REQUIREMENT ANALYSIS")
print("=" * 80)

print(response.model_dump())