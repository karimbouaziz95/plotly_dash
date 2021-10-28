import dash
from pandas.core.algorithms import mode
import plotly.graph_objs as go
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import json
from dash.dependencies import Output, Input
import base64

def encode_image(image_file):
    encoded = base64.b64encode(open(image_file, 'rb').read())
    return 'data:image/png;base64,{}'.format(encoded.decode())

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
                html.Img(
                    id="ausgabe-image",
                    src="children",
                    height= 300
                )
            ],
            style={"paddingTop": 20}
        )
    ],
)

@app.callback(
    Output("ausgabe-image", "src"),
    [
        Input("my-graph", "clickData")
    ]
)
def update_image(hoverData):
    wheel = hoverData["points"][0]["y"]
    color = hoverData["points"][0]["x"]
    path = "DATA/images/"
    return encode_image(path+df[(df["color"] == color) & (df["wheels"] == wheel)]["image"].values[0])


if __name__ == "__main__":
    app.run_server()
    