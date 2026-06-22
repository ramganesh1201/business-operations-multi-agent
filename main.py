from agents.coordinator import handle_request

sample_email = """
Client needs project update by Friday.
Prepare status report and schedule meeting.
"""

result = handle_request(sample_email)

print(result)