from agents.email_agent import summarize_email
from agents.task_agent import prioritize_tasks
from agents.report_agent import generate_report

from tools.file_tools import save_report


def process_email_workflow(email_text):

    summary = summarize_email(email_text)

    priorities = prioritize_tasks(summary)

    report = generate_report(summary, priorities)

    filepath = save_report(
        report,
        "weekly_report.txt"
    )

    return report, filepath