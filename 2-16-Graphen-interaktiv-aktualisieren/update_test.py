import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import numpy as np
import plotly.graph_objs as go

app = dash.Dash()

df = pd.read_csv("DATA/mpg.csv")

df["year"] = np.random.randint(-4, 5, len(df))*0.1 + df["model_year"]

app.layout = html.Div(
    [
        html.Div(
            [
                dcc.Graph(
                    id="mpg-scatter",
                    figure={
                        "data": [
                            go.Scatter(
                                x=df["year"]+1900,
                                y=df["mpg"],
                                text=df["name"],
                                hoverinfo="text",
                                mode="markers"
                            )
                        ],
                        "layout": go.Layout(
                            title="mpg.csv dataset",
                            xaxis={"title": "model year"},
                            yaxis={"title": "mpg"}
                        )
                    }
                )
            ],
            style={"width": "50%", "display": "inline-block"}
        ),
        html.Div(
            [
                dcc.Graph(
                    id="mpg-line",
                    figure={
                        "data": [
                            go.Scatter(
                                x=[0, 1],
                                y=[0, 1],
                                mode="lines"
                            )
                        ],
                        "layout": go.Layout(
                            title="Beschleunigung",
                            margin={"l": 0}
                        )
                    }
                ),
                dcc.Markdown(
                    id="mpg-stats"
                )

            ],
            style={"width": "30%", "display": "inline-block", "height": "50%"}
        )
    ]
)


@app.callback(
    Output("mpg-line", "figure"),

    [
        Input("mpg-scatter", "hoverData")
    ]
)
def callback_graph(hoverData):
    v_index = hoverData["points"][0]["pointIndex"]
    fig = {
        "data": [
            go.Scatter(
                x=[0, 1],
                y=[0, 60/df.iloc[v_index]["acceleration"]],
                mode="lines",
                line={"width": 2*df.iloc[v_index]["cylinders"]}
            )
        ],
        "layout": go.Layout(
            title=df.iloc[v_index]["name"],
            xaxis={"visible": False},
            yaxis={"visible": False, "range": [
                0, 60/df["acceleration"].min()]},
            margin={"l": 0},
            height=300
        )
    }

    return fig


@app.callback(
    Output("mpg-stats", "children"),
    [
        Input("mpg-scatter", "hoverData")
    ]
)
def callback_stats(hoverData):
    v_index = hoverData["points"][0]["pointIndex"]
    stats = """
        {} cylinders
        {} displacement
        0 to 60 mph in {} Sekunden
    """.format(df.iloc[v_index]["cylinders"],
               df.iloc[v_index]["displacement"],
               df.iloc[v_index]["acceleration"])
    return stats


if __name__ == "__main__":
    app.run_server()
