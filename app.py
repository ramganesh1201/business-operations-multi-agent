import streamlit as st

from agents.coordinator import process_email_workflow

st.sidebar.title("Project Info")

st.sidebar.markdown("""
### Agents

- Coordinator Agent
- Email Agent
- Task Agent
- Report Agent

### AI Model

Gemini 2.5 Flash
""")

st.set_page_config(
    page_title="Business Operations Copilot",
    layout="wide"
)

st.title("🤖 Business Operations Copilot")

email_text = st.text_area(
    "Paste Email",
    height=250
)

if st.button("Process Email"):

    with st.spinner("Running agents..."):

        report, filepath = process_email_workflow(
            email_text
        )

    st.success("Workflow Complete")

    st.subheader("Generated Report")

    st.markdown(report)

    st.info(f"Saved to: {filepath}")