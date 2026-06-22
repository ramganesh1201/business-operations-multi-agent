from agents.email_agent import summarize_email
from agents.task_agent import prioritize_tasks
from agents.report_agent import generate_report


def handle_request(email_text):
    email_result = summarize_email(email_text)

    task_result = prioritize_tasks(
        email_result["action_items"]
    )

    report = generate_report(
        email_result["summary"],
        task_result
    )

    return report