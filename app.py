import streamlit as st
from agents.coordinator import process_email_workflow
from tools.file_tools import list_reports

# RULE: This MUST be the very first Streamlit command in the file
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

st.sidebar.write("---")  # Visual divider line
st.sidebar.subheader("📁 Saved Reports History")

# Automatically pull and display files from the /reports folder
try:
    reports = list_reports(role="admin")  # Using "admin" role to pass the security layer check
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
        try:
            report, filepath = process_email_workflow(email_text)
            st.success("Workflow Complete")
            st.subheader("Generated Report")
            st.markdown(report)
            st.info(f"Saved to: {filepath}")
            
            # Instantly refreshes the sidebar history list so the new report shows up
            st.rerun()
            
        except Exception as e:
            st.error("Unable to generate report.")
            if "RESOURCE_EXHAUSTED" in str(e):
                st.warning("Gemini API quota exceeded. Please wait a moment and try again.")
            else:
                st.exception(e)