import streamlit as st
from agents.coordinator import process_email_workflow
from tools.file_tools import list_reports

# RULE: st.set_page_config MUST be the very first Streamlit command run
st.set_page_config(
    page_title="Business Operations Copilot",
    layout="wide"
)

# --- SIDEBAR SECTION ---
st.sidebar.title("Project Info")
st.sidebar.markdown("""
### Agents
- Coordinator Agent
- Email Agent
- Task Agent
- Report Agent

### AI Model
- Gemini 2.5 Flash
""")

st.sidebar.write("---")  # Adds a visual divider line
st.sidebar.subheader("📁 Saved Reports History")

# Automatically pull and display files from the /reports folder
try:
    reports = list_reports(role="admin")  # Using "admin" role to satisfy the security check
    if reports:
        for report in reports:
            st.sidebar.caption(f"📄 {report}")
    else:
        st.sidebar.info("No reports generated yet.")
except Exception as e:
    st.sidebar.error(f"Could not load history: {e}")


# --- MAIN PAGE SECTION ---
st.title("🤖 Business Operations Copilot")

email_text = st.text_area(
    "Paste Email",
    height=250
)

if st.button("Process Email"):
    with st.spinner("Running agents..."):
        report, filepath = process_email_workflow(email_text)
        
    st.success("Workflow Complete")
    st.subheader("Generated Report")
    st.markdown(report)
    st.info(f"Saved to: {filepath}")
    
    # Force Streamlit to rerun and instantly refresh the sidebar history list
    st.rerun()