#######
# Erstes Meilenstein-Projekt: Entwickle ein Boersenticker-Dashboard,
# dass es dem Nutzer entweder erlaubt, 
# ein Ticker-Symbol in ein Eingabefeld einzugeben oder Elemente aus einem
# Auswahlfeld (dropdown) auszuwaehlen, um dann mit pandas_datareader
# Boersendaten auszulesen und in einem Graphen darzustellen.
######

# ERGAENZE DIE BOERSENSYMBOL-EINGABE UM DIE AUSWAHL MULTIPLER BOERSEN
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas_datareader.data as web # Benoetigt mindestens v0.6.0
from datetime import datetime
import pandas as pd

app = dash.Dash()

nsdq = pd.read_csv('DATA/NASDAQcompanylist.csv')
nsdq.set_index('Symbol', inplace=True)
options = []
for tic in nsdq.index:
    options.append({'label':'{} {}'.format(tic,nsdq.loc[tic]['Name']), 'value':tic})

app.layout = html.Div([
    html.H1('Aktienticker Dashboard'),
    html.Div([
        html.H3('Auswahl des Aktiensymbols:', style={'paddingRight':'30px'}),
        dcc.Dropdown(
            id='my_ticker_symbol',
            options=options,
            value=['TSLA'],
            multi=True
        )
    ], style={'display':'inline-block', 'verticalAlign':'top', 'width':'30%'}),
    html.Div([
        html.H3('Auswahl des Start- und Enddatums:'),
        dcc.DatePickerRange(
            id='my_date_picker',
            min_date_allowed=datetime(2015, 1, 1),
            max_date_allowed=datetime.today(),
            start_date=datetime(2018, 1, 1),
            end_date=datetime.today()
        )
    ], style={'display':'inline-block'}),
    html.Div([
        html.Button(
            id='submit-button',
            n_clicks=0,
            children='Anzeigen',
            style={'fontSize':24, 'marginLeft':'30px'}
        ),
    ], style={'display':'inline-block'}),
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
    [Input('submit-button', 'n_clicks')],
    [State('my_ticker_symbol', 'value'),
    State('my_date_picker', 'start_date'),
    State('my_date_picker', 'end_date')])
def update_graph(n_clicks, stock_ticker, start_date, end_date):
    start = datetime.strptime(start_date[:10], '%Y-%m-%d')
    end = datetime.strptime(end_date[:10], '%Y-%m-%d')
    traces = []
    for tic in stock_ticker:
        df = web.DataReader(tic,'stooq',start,end)
        traces.append({'x':df.index, 'y': df['Close'], 'name':tic})
    fig = {
        'data': traces,
        'layout': {'title':', '.join(stock_ticker)+' Closing Prices'}
    }
    return fig

if __name__ == '__main__':
    app.run_server()
