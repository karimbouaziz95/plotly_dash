import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np

app = dash.Dash()

np.random.seed(42)
random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

app.layout = html.Div([
        dcc.Graph(
                id = "scatter",
                figure={
                        "data": [go.Scatter(
                                x=random_x,
                                y=random_y,
                                mode="markers",
                                marker={
                                        "size":20,
                                        "color": "#0d1ce0",
                                        "symbol": "pentagon",
                                        "line": {"width":5}
                                }
                        )
                        ],
                        "layout": go.Layout(title="my scatter",
                                            xaxis={"title": "X Axis"})
                        }
                ),
        dcc.Graph(
                id = "scatter2",
                figure={
                        "data": [go.Scatter(
                                x=random_x,
                                y=random_y,
                                mode="markers",
                                marker={
                                        "size":20,
                                        "color": "#b52d00",
                                        "symbol": "pentagon",
                                        "line": {"width":5}
                                }
                        )
                        ],
                        "layout": go.Layout(title="my 2. scatter",
                                            xaxis={"title": "X Axis"})
                        }
                )
]
)

if __name__ == "__main__":
    app.run_server()
