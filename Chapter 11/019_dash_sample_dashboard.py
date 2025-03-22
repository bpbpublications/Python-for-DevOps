# Script: 019_dash_sample_dashboard.py

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

# Sample data
df = pd.DataFrame({
    "Category": ["A", "B", "C"],  # Categories for the bar chart
    "Value": [10, 20, 30]  # Values corresponding to each category
})

# Create Dash app
app = dash.Dash(__name__)

# Define layout
app.layout = html.Div([
    dcc.Graph(
        figure=px.bar(df, x="Category", y="Value", title="Sample Dashboard")  # Bar chart with Plotly Express
    )
])

# Run app
if __name__ == '__main__':
    app.run_server(debug=True)  # Run the Dash app in debug mode
