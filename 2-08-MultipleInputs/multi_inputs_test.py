import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

app = dash.Dash()
df = pd.read_csv("DATA/mpg.csv")

app.layout = html.Div([
    html.Div([
        html.Label("X axis"),
        dcc.Dropdown(
            id="xaxis",
            options=[{"label": i, "value": i} for i in df.columns],
            value="displacement"
        )
    ],
        style={"width": "48%", "display": "inline-block"}
    ),
    html.Div([
        html.Label("Y axis"),
        dcc.Dropdown(
            id="yaxis",
            options=[{"label": i, "value": i} for i in df.columns],
            value="acceleration"
        )
    ],
        style={"width": "48%", "float": "right", "display": "inline-block"}
    ),
    dcc.Graph(
        id="feature-graphic"
    )
],
    style={"padding": 10}
)


@app.callback(
    Output("feature-graphic", "figure"),
    [
        Input("xaxis", "value"),
        Input("yaxis", "value")
    ]
)
def update_graph(xaxis_name, yaxis_name):
    return {
        "data": [
            go.Scatter(
                x=df[xaxis_name],
                y=df[yaxis_name],
                text=df["name"],
                mode="markers",
                marker={
                    "size": 15,
                    "opacity": 0.5,
                    "line": {"width": 0.5, "color": "white"}
                }

            )
        ],
        "layout": go.Layout(
            xaxis={"title": xaxis_name.title()},
            yaxis={"title": yaxis_name.title()}

        )
    }


if __name__ == "__main__":
    app.run_server()
