# Script: 020_panel_sample_dashboard.py

import panel as pn
import pandas as pd
import matplotlib.pyplot as plt

# Sample data
df = pd.DataFrame({
    "Category": ["A", "B", "C"],  # Categories for the bar chart
    "Value": [10, 20, 30]  # Values corresponding to each category
})

# Create Panel dashboard
pn.extension()

# Create a bar chart using Matplotlib
fig, ax = plt.subplots()
df.plot(kind='bar', x='Category', y='Value', ax=ax, title='Sample Dashboard')

# Create a Panel object for the chart
dashboard = pn.panel(fig)

# Show dashboard
dashboard.servable()  # Make the dashboard servable
