import streamlit as st

# 1. Page Configuration (Must be the first Streamlit command)
st.set_page_config(
  page_title="Jose I. Popoca Jr. | Systems Architect",
  page_icon="🏗️",
  layout="wide"
)

# 2. Define the pages
qms_demo = st.Page("pages/01_qms_demo.py", title="QMS Automation Demo", icon="⚙️")
# We will uncomment these as we build them:
yaml_schema = st.Page("pages/02_yaml_schema.py", title="YAML Data Structuring", icon="📂")

# 3. Group them into the sidebar menu
pg = st.navigation({
  "Freelance Portfolio (Upwork)": [qms_demo, yaml_schema]
})

# 4. Execute the router
pg.run()