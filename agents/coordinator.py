from agents.email_agent import summarize_email
from agents.task_agent import prioritize_tasks
from agents.report_agent import generate_report

from tools.file_tools import save_report


def process_email_workflow(email_text):

    email_data = summarize_email(email_text)

    priorities = prioritize_tasks(
        email_data["action_items"]
    )

    report = generate_report(
        email_data["summary"],
        priorities
    )

    filepath = save_report(
        report,
        "weekly_report.txt"
    )

    return report, filepath