import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Startup Analytics Dashboard",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 Startup Analytics Dashboard")

st.markdown("""
### Advanced Startup Ecosystem Analytics
Analyze funding, valuation, revenue, profitability and market trends.
""")

st.image(
    "https://images.unsplash.com/photo-1559136555-9303baea8ebd",
    use_container_width=True
)

st.success("Use the sidebar to navigate through analytics modules.")
