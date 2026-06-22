from agents.email_agent import summarize_email

email = """
Client requires dashboard update by Friday.

Please:
- Fix bugs
- Schedule review meeting
"""

result = summarize_email(email)

print(result)