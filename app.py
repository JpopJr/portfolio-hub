import streamlit as st

# 1. Define the pages pointing to the files in your 'pages' folder
portfolio_demo_1 = st.Page("pages/01_qms-demo.py", title="QMS Automation Demo", icon="⚙️")
portfolio_demo_2 = st.Page("pages/02_yaml_schema.py", title="YAML Data Structuring", icon="📂")
career_dashboard = st.Page("pages/03_career_dash.py", title="My Career Analytics", icon="📈")

# 2. Group them into menu sections for the sidebar
pg = st.navigation({
  "Freelance Portfolio (Upwork)": [portfolio_demo_1, portfolio_demo_2],
  "Internal Tools (Career Engine)": [career_dashboard]
})

# 3. Run the application
pg.run