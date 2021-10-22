#######
# Erstes Meilenstein-Projekt: Entwickle ein Börsenticker-Dashboard,
# dass es dem Nutzer entweder erlaubt, 
# ein Ticker-Symbol in ein Eingabefeld einzugeben oder Elemente aus einem
# Auswahlfeld (dropdown) auszuwählen, um dann mit pandas_datareader
# Börsendaten auszulesen und in einem Graphen darzustellen.
######

# FÜGE EINEN PANDAS DATAREADER UND DATETIME ZUM AUSGABEGRAPHEN HINZU
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas_datareader.data as web # Benötigt mindestens v0.6.0
from datetime import datetime

app = dash.Dash()

app.layout = html.Div([
    html.H1('Aktienticker Dashboard'),
    html.H3('Aktiensymbol:'),
    dcc.Input(
        id='my_ticker_symbol',
        value='TSLA' # Setzt einen Standardwert (default)
    ),
    dcc.Graph(
        id='my_graph',
        figure={
            'data': [
                {'x': [1,2], 'y': [3,1]}
            ]
        }
    )
])
@app.callback(
    Output('my_graph', 'figure'),
    [Input('my_ticker_symbol', 'value')])
def update_graph(stock_ticker):
    start = datetime(2018, 1, 1)
    end = datetime(2018, 12, 31)
    df = web.DataReader(stock_ticker,'stooq',start,end)
    fig = {
        'data': [
            {'x': df.index, 'y': df['Close']}
        ],
        'layout': {'title':stock_ticker}
    }
    return fig

if __name__ == '__main__':
    app.run_server()
