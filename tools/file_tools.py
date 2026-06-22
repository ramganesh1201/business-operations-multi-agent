import os
from security.auth import can_access

REPORT_DIR = "reports"

def save_report(report_text, filename="report.txt", role="admin"):
    # Check permissions before writing
    if not can_access(role, "write"):
        raise PermissionError("Access denied: You do not have permission to write reports.")
        
    os.makedirs(REPORT_DIR, exist_ok=True)
    filepath = os.path.join(REPORT_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(report_text)
    return filepath

def list_reports(role="admin"):
    # Check permissions before reading
    if not can_access(role, "read"):
        raise PermissionError("Access denied: You do not have permission to view reports.")
        
    os.makedirs(REPORT_DIR, exist_ok=True)
    return os.listdir(REPORT_DIR)