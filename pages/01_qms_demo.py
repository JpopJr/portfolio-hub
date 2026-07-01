import streamlit as st
import pandas as pd

# Header Section
st.title("⚙️ Acme Aerospace: QMS Automation Dashboard")
st.markdown("""
**Concept** Transforming legacy AS9100 quality manuals and PDF inspection reports into a live, AI-ready structured database.
*Built by Jose I. Popoca Jr. as a demonstration of manufacturing data automation.*              
""")

st.divider()

# Top Level Metrics (The Executive View)
st.subheader("Current Compliance Metrics (Q3)")
col1, col2, col3, col4 = st.columns(4)

col1.metric(label="Open Non-Conformance (NCR)", value="3", delta="-2 from last month")
col2.metric(label="Internal Audit Score", value="98.2%", delta="0.5%")
col3.metric(label="Supplier Defect Rate", value="0.4%", delta="-0.1%", delta_color="inverse")
col4.metric(label="SOPs Digitized for AI", value="42", delta="12 added")

st.divider()

# The Data Table (Simulated Structured Data extraction)
st.subheader("Recent Inspection Logs (Structured)")
st.caption("Legacy paper logs converted into clean, machine-readable JSON formats.")

# Mock Data for Acme Aerospace
mock_data = {
  "Reports ID": ["NCR-1042", "AUD-8891", "INSP-3321", "NCR-1043"],
  "Date": ["2026-06-25", "2026-06-28", "2026-06-29", "2026-06-30"],
  "Department": ["Machining", "Assembly", "Final QA", "Shipping"],
  "Standard": ["AS9100: 7.1.3", "AS9100: 8.2.2", "ISO 9001: 9.1", "AS9100: 8.5.4"],
  "Status": ["Under Review", "Passed", "Passed", "Corrective Action"],
  "AI Extracted Root Cause": ["Tooling wear out of tolerance", "N/A", "N/A", "Improper packaging material"]
}

df = pd.DataFrame(mock_data)

# Display as an interactive dataframe
st.dataframe(df, use_container_width=True, hide_index=True)

# Mock AI Output Section to show modern capability
st.subheader("🤖 AI Process Analysis")
st.info("""
**Prompt:** Analyze NCR-1043 against AS9100 Section 8.5.4 (Preservation).
        
**Automated Finding** The use of standard cardboard in Shipping violates the specific electrostatic discharge (ESD) packaging requirements outlined in the modernized SOP. Recommended action: Flag supplier and update packing bill of materials (BOM).
""")