import os

REPORT_DIR = "reports"


def save_report(report_text, filename="report.txt"):
    os.makedirs(REPORT_DIR, exist_ok=True)

    filepath = os.path.join(REPORT_DIR, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(report_text)

    return filepath


def list_reports():
    os.makedirs(REPORT_DIR, exist_ok=True)

    return os.listdir(REPORT_DIR)