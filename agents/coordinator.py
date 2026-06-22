from agents.email_agent import summarize_email
from agents.task_agent import prioritize_tasks
from agents.report_agent import generate_report


def process_email_workflow(email_text):

    print("Step 1: Summarizing email...")

    summary = summarize_email(email_text)

    print("Step 2: Prioritizing tasks...")

    priorities = prioritize_tasks(summary)

    print("Step 3: Generating report...")

    report = generate_report(summary, priorities)

    return report