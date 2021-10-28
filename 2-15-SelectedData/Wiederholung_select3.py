import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import json
import pandas as pd
from dash.dependencies import Output, Input
import numpy as np

app = dash.Dash()

np.random.seed(10)
x1 = np.linspace(0.1, 5, 50)
x2 = np.linspace(5.1, 10, 50)
y = np.random.randint(0, 50, 50)

df1 = pd.DataFrame({"x": x1, "y": y})
df2 = pd.DataFrame({"x": x1, "y": y})
df3 = pd.DataFrame({"x": x2, "y": y})

df = pd.concat([df1, df2, df3])
print(df)

app.layout = html.Div(
    [
        html.Div(
            [
                dcc.Graph(
                    id="plotter",
                    figure={
                        "data": [
                            go.Scatter(
                                x=df["x"],
                                y=df["y"],
                                mode="markers",
                                marker={
                                    "size": 8,
                                    "opacity": 0.7,
                                    "line": {"width": 1, "color": "#36ffeb"},
                                    "color": "#ff0000"
                                }
                            )
                        ],
                        "layout": go.Layout(
                            title="Random Scatterplot",
                            hovermode = "closest"
                        )
                    }
                )
            ],
            style={"display": "inline-block", "width": "50%", "float": "left"}
        ),
        html.Div(
            [
                html.Pre(
                    id="density",
                    children="Rit ki njarabkom ya3tik 3asba fi sormek"
                )
            ],
            style={"display": "inline-block", "width": "35%", "paddingTop": 35}
        )
    ]
)

@app.callback(
    Output("density", "children"),
    [
        Input("plotter", "selectedData")
    ]
)
def update_json(selectedData):
    return json.dumps(selectedData, indent=2)


if __name__ == "__main__":
    app.run_server()
