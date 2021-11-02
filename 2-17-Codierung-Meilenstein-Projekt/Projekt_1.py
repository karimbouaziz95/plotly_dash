import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from datetime import datetime
from pandas._config.config import options
import pandas_datareader.data as web
import pandas as pd


app = dash.Dash()
df = web.DataReader("TSLA", "stooq", datetime(
    2018, 1, 1), datetime(2018, 12, 31))
print(df)
print(df.index)
print(df["Close"])

nsdq = pd.read_csv("DATA/NASDAQcompanylist.csv")
nsdq.set_index("Symbol", inplace=True)
print(nsdq.iloc[2])

options = []
for tic in nsdq.index:
    options.append({"label": "{} {}".format(tic, nsdq.loc[tic]["Name"]), "value": tic})

app.layout = html.Div(
    [
        html.H1("Aktienticker Dashboard"),
        html.Div(
            [
                html.H3("Aktiensymbol:", style={"paddingRight": "30px"}),
                dcc.Dropdown(
                    id="my_stick_ticker",
                    value=["TSLA"],
                    options=options,
                    multi=True,
                ),
            ],
            style={"display": "inline-block", "verticalAlign": "top", "width": "30%"}
        ),
        html.Div(
            [
                html.H3("Start- und Enddatum:"),
                dcc.DatePickerRange(
                    id="my_date_picker",
                    min_date_allowed=datetime(2015, 1, 1),
                    max_date_allowed=datetime.today(),
                    start_date=datetime(2019, 1, 1),
                    end_date=datetime.today()
                )
            ],
            style={"display": "inline-block"}
        ),

        html.Div(
            [
                html.Button(
                    id="submit_button",
                    n_clicks=0,
                    children="Anzeigen!",
                    style={"fontSize": 24, "marginLeft": "30px"}
                )
            ],
            style={"display": "inline-block"}
            
        ),

        dcc.Graph(
            id="my_graph",
            figure={
                "data": [
                    {
                        "x": [1, 2, 3],
                        "y": [5, 9, 1]
                    }
                ]
            }
        )
    ]
)


@app.callback(
    Output("my_graph", "figure"),
    [
        Input("submit_button", "n_clicks")
    ],
    [
        State("my_stick_ticker", "value"),
        State("my_date_picker", "start_date"),
        State("my_date_picker", "end_date")
    ]
)
def update_graph(n_clicks, stock_ticker, start_date, end_date):
    start = datetime.strptime(start_date[:10], "%Y-%m-%d")
    end = datetime.strptime(end_date[:10], "%Y-%m-%d")
    
    traces = []
    
    for tic in stock_ticker:
        df = web.DataReader(tic, "stooq", start, end)
        traces.append(
            {
                "x": df.index,
                "y": df["Close"],
                "name": tic
            }
        )
    
    fig = {
        "data": traces,
        "layout": {"title": stock_ticker}
    }

    return fig


if __name__ == "__main__":
    app.run_server()
