import dash
from pandas.core.algorithms import mode
import plotly.graph_objs as go
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import json
from dash.dependencies import Output, Input

app = dash.Dash()

df = pd.read_csv("DATA/wheels.csv")

app.layout = html.Div(
    [
        html.Div(
            [
                dcc.Graph(
                    id="my-graph",
                    figure={
                        "data": [
                            go.Scatter(
                                x = df["color"],
                                y = df["wheels"],
                                dy = 1,
                                mode="markers",
                                marker = {
                                    "size": 12,
                                    "color": "#e800cd",
                                    "line": {"width": 2, "color": "#0027e8"}
                                }
                            )
                        ],
                        "layout": go.Layout(
                            title="Wheels and colors",
                            xaxis = {"title": "Colors"},
                            yaxis = {"title": "# der Räder"},
                            hovermode="closest"
                        )
                    },
                )
            ],
            style={"width": "40%", "float": "left"}
        ),
        html.Div(
            [
                html.Pre(
                    id="ausgabe-feld",

                )
            ],
            style={"paddingLeft": 10}
        )
    ],
)

@app.callback(
    Output("ausgabe-feld", "children"),
    [
        Input("my-graph", "hoverData")
    ]
)
def to_update(hoverData):
    return json.dumps(hoverData, indent=2)


if __name__ == "__main__":
    app.run_server()
