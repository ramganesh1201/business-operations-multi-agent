from agents.coordinator import process_email_workflow

email = """
Hello Team,

The client requires the dashboard update by Friday.

Please:
- Prepare a progress report
- Schedule a review meeting
- Resolve critical bugs

Regards,
Manager
"""

result = process_email_workflow(email)

print("\nFINAL REPORT\n")
print(result)