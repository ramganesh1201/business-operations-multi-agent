from mcp.server.fastmcp import FastMCP
import os

mcp = FastMCP("BusinessFileServer")

REPORT_DIR = "reports"

@mcp.tool()
def list_reports():
    """List available reports"""
    if not os.path.exists(REPORT_DIR):
        return []
    return os.listdir(REPORT_DIR)

@mcp.tool()
def read_report(filename: str):
    """Read a report"""
    path = os.path.join(REPORT_DIR, filename)
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

if __name__ == "__main__":
    print("Starting BusinessFileServer MCP...")
    mcp.run()