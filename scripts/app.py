import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(BASE_DIR, "data", "cleaned_spacex_data.csv")

df = pd.read_csv(data_path)


# Load data
#df = pd.read_csv("data/cleaned_spacex_data.csv")

# Create Dash app
app = dash.Dash(__name__)

# Create charts
fig1 = px.pie(
    df,
    names="success",
    title="Launch Success Distribution"
)

fig2 = px.scatter(
    df,
    x="flight_number",
    y="success",
    title="Success vs Flight Number"
)

# Layout
app.layout = html.Div([
    html.H1("SpaceX Launch Dashboard"),
    dcc.Graph(figure=fig1),
    dcc.Graph(figure=fig2)
])

# Run the app
if __name__ == "__main__":
    app.run_server(host="127.0.0.1", port=8050, debug=True)
