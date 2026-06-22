def summarize_email(email_text):
    return {
        "summary": f"Summary of: {email_text[:50]}",
        "action_items": [
            "Follow up with client",
            "Prepare report"
        ]
    }