from agents.email_agent import summarize_email

email = """
Hi Team,

The client needs the dashboard update by Friday.
Please prepare a progress report and schedule a review meeting.

Thanks,
Manager
"""

result = summarize_email(email)

print(result)