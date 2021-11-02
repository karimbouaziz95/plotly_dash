import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import requests
from requests import models

app = dash.Dash()

app.layout = html.Div(
    [
        html.Pre(
            id="block_1",
            children="Aktuelle Flüge welt"
        ),
        dcc.Graph(
            id="my-graph",
            style={"width": 1200}
        ),
        dcc.Interval(
            id="my_intervall",
            interval=5000,
            n_intervals=0
        )
    ]
)
counter_list = []


@app.callback(
    Output("block_1", "children"),
    [
        Input("my_intervall", "n_intervals")
    ]
)
def update_flight(n):
    url = "https://data-live.flightradar24.com/zones/fcgi/feed.js?faa=1\
           &mlat=1&flarm=1&adsb=1&gnd=1&air=1&vehicles=1&estimated=1&stats=1"
    res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    data = res.json()
    counter = 0

    for element in data["stats"]["total"]:
        counter += data["stats"]["total"][element]

    counter_list.append(counter)

    return "Aktuelle weltweite Flüge: {}".format(counter)


@app.callback(
    Output("my-graph", "figure"),
    [
        Input("my_intervall", "n_intervals")
    ]
)
def update_graph(n):
    fig = go.Figure(
        data=[go.Scatter(
            x=list(range(0, len(counter_list))),
            y = counter_list,
            mode = "markers+lines"
        )
        ]
    )
    return fig

if __name__ == "__main__":
    app.run_server()