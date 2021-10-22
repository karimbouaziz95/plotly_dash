#######
# Erstes Meilenstein-Projekt: Entwickle ein Börsenticker-Dashboard,
# dass es dem Nutzer entweder erlaubt, 
# ein Ticker-Symbol in ein Eingabefeld einzugeben oder Elemente aus einem
# Auswahlfeld (dropdown) auszuwählen, um dann mit pandas_datareader
# Börsendaten auszulesen und in einem Graphen darzustellen.
######

# ENTWIRF DAS LAYOUT DES GRAPHEN ZUERST UND ENTWICKLE DAS 
# CALLBACK IN DER NÄCHSTEN PHASE
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([
    html.H1('Aktienticker Dashboard'),
    html.H3('Aktiensymbol:'),
    dcc.Input(
        id='my_stock_ticker',
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

if __name__ == '__main__':
    app.run_server()
