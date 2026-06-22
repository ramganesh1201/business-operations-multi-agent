from agents.coordinator import process_email_workflow

email = """
Client requires dashboard update by Friday.
Fix bugs and schedule review.
"""

report, filepath = process_email_workflow(email)

print(report)

print(f"\nSaved to: {filepath}")