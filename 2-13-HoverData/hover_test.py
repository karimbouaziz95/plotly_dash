import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import json
import base64

def encode_image(image_file):
    encoded = base64.b64encode(open(image_file, "rb").read())
    return "data:image/png;base64,{}".format(encoded.decode())

app = dash.Dash()

df = pd.read_csv(r"C:/Users/NajahKarimBouaziz/Desktop/Neuer Ordner/plotly_dash/DATA/wheels.csv")

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
                                    "color": "#3c00ff",
                                    "line": {"width": 2}
                                }
                            )
                        ],
                        "layout": go.Layout(
                            title="Wheels and colors"
                        )
                    }
                )
            ],
            style={"width": "30%", "float": "left"}
        ),
        html.Div(
            [
                html.Img(
                    id="hover-image",
                    src="children",
                    height=300
                )
            ],
            style={"paddingTop": "50"}
        ),
    ]
)

@app.callback(
    Output("hover-image", "src"),
    [
        Input("wheels-plot", "hoverData")
    ]
)
def callback_image(hoverData):
    wheel = hoverData["points"][0]["y"]
    color = hoverData["points"][0]["x"]
    path = "C:/Users/NajahKarimBouaziz/Desktop/Neuer Ordner/plotly_dash/DATA/Images/"
    return encode_image(path+df[(df["wheel"] == wheel) & (df["color"] == color)]["image"].values[0])
    

if __name__ == "__main__":
    app.run_server()
