import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import json

app = dash.Dash()

df = pd.read_csv("DATA/wheels.csv")

app.layout = html.Div(
    [
        html.Div(
            [
                dcc.Graph(
                    id="wheels-plot",
                    figure={
                        "data": [
                            go.Scatter(
                                x=df["color"],
                                y=df["wheels"],
                                dy=1,
                                mode="markers",
                                marker={
                                    "size": 12,
                                    "color": "#f57d1b",
                                    "line": {"width": 2}
                                }
                            )
                        ],
                        "layout": go.Layout(
                            title="Wheels and Color diagramm",
                            xaxis={"title": "color"},
                            yaxis={"title": "# of Wheels"},
                            hovermode="closest"
                        )
                    }
                )
            ],
            style={"width": "50%", "display": "inline-block"}
        ),
        html.Div(
            [
                html.Pre(
                    id="ausgabe",
                    style={"paddingTop": 25}
                )
            ],
            style={"width": "30%", "display": "inline-block"}
        )
    ]
)


@app.callback(
    Output("ausgabe", "children"),
    [
        Input("wheels-plot", "selectedData")
    ]
)
def update_text(selected_data):
    return json.dumps(selected_data, indent=2)


if __name__ == "__main__":
    app.run_server()
