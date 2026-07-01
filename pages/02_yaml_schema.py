import streamlit as st

st.title("📂 AI Data Structuring & YAML Schemas")
st.markdown("""
**Concept** Large Language Models (LLMs) hallucinate or fail when fed unstructured, messy text.
This demonstration shows how I engineer legacy operational data into strict, hierarchical YAML/JSON taxonomies to guarantee AI accuracy and system interoperability.                    
""")

st.divider()

col1, col2 = st.columns(2)

with col1:
  st.subheader("❌ The Problem: Unstructured Legacy Data")
  st.caption("A typical messy PDF or Word document from a legacy Quality Manual.")
  st.error("""
**Acme Aerospace - Audit Finding 2026-A**
During the morning shift on Tuesday, the inspector noticed that the O-rings, in bin 4A were not stored at the right temperature. The manual says they should be between 65 and 75 degrees but it was 82 degrees in the storage room. Also, the batch number was rubbed off. This violates our preservation policy. We need to move them to the climate-controlled area and tell the supplier.
""")
  st.markdown("""
*Why AI fails here:*
* Critical variables (temperature, location, batch) are buried in prose.
* No standardized keys for an automated system to query.
* Highly prone to token-limit bloat and reasoning errors.
""")
  
with col2:
  st.subheader("✅ The Solution: Engineered YAML Schema")
  st.caption("The exact same data, architected for zero-hallucination AI ingestion ")

  # Fictional Dummy Data formatted as YAML
  yaml_code = """
acme_ncr_report:
  metadata:
    report_id: "NCR-2026-A
    timestamp: "2026-06-31T09:00:00Z"
    department: "Inventory Management"
  finding_details:
    component: "O-Ring"
    storage_location: "Bin 4A"
    batch_number: null # Critical missing data flagged
  compliance_parameters:
    standard_referenced: QMS-Preservation-Policy"
    required_temp_recorded_F: [65, 75]
    actual_temp_recorded_F: 82
    deviation_status: "CRITICAL"
  action_plan:
    immediate_containment: "Relocate to climate-controlled sector."
    external_action: "Notify supplier regarding batch labeling."
    """
  st.code(yaml_code, language="yaml")

  st.success("""
  *Why AI succeeds here:*
  * `batch_number: null` creates an explicit machine-readable flag.
  * Arrays `[65, 75]` allow mathematical validation.
  * Perfectly suited for API integrations and offline automated processing.
  """)

st.divider()
st.info("💡 **Business Impact:** By converting unstructured SOPs and manuals into schemas like this, businesses can deploy AI agents that retrieve procedures instantly, accurately, and without hallucinations.")
