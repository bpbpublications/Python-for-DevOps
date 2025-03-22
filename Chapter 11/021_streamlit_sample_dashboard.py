# Script: 021_streamlit_sample_dashboard.py

import streamlit as st
import pandas as pd

# Sample data
df = pd.DataFrame({
    "Category": ["A", "B", "C"],  # Categories for the bar chart
    "Value": [10, 20, 30]  # Values corresponding to each category
})

# Create Streamlit app and display a bar chart
st.title("Sample Dashboard")
st.bar_chart(df.set_index('Category'))  # Use Category as the index for the bar chart
