from app.analysis.requirement_workflow import RequirementWorkflow


workflow = RequirementWorkflow()

analysis = workflow.analyze_issue(
    "KAN-4"
)

print("=" * 80)
print("REQUIREMENT ANALYSIS")
print("=" * 80)

print(analysis.model_dump())