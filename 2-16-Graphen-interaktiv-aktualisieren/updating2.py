#######
# Dies zeigt den Datensatz mpg.csv als ausgespreiztes Streudiagramm
# welches hoverData via Callback an einen anderen Graphen schickt.
######
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
from numpy import random

app = dash.Dash()

df = pd.read_csv('../DATA/mpg.csv')

# Füge zum ausspreizen einen zufälligen "jitter" (Verschiebung) zu model_year hinzu
df['year'] = df['model_year'] + random.randint(-4,5,len(df))*0.10

app.layout = html.Div([
    html.Div([   # Dieses Div enthält unser Streudiagramm
    dcc.Graph(
        id='mpg_scatter',
        figure={
            'data': [go.Scatter(
                x = df['year']+1900,  # Die "gejitterten" Daten
                y = df['mpg'],
                text = df['name'],
                hoverinfo = 'text',
                mode = 'markers'
            )],
            'layout': go.Layout(
                title = 'mpg.csv dataset',
                xaxis = {'title': 'model year'},
                yaxis = {'title': 'miles per gallon'},
                hovermode='closest'
            )
        }
    )], style={'width':'50%','display':'inline-block'}),
    html.Div([  # Dieses Div enthält unseren Ausgabegraphen
    dcc.Graph(
        id='mpg_line',
        figure={
            'data': [go.Scatter(
                x = [0,1],
                y = [0,1],
                mode = 'lines'
            )],
            'layout': go.Layout(
                title = 'Beschleunigung',
                margin = {'l':0}
            )
        }
    )
    ], style={'width':'20%', 'height':'50%','display':'inline-block'})
])

@app.callback(
    Output('mpg_line', 'figure'),
    [Input('mpg_scatter', 'hoverData')])
def callback_graph(hoverData):
    v_index = hoverData['points'][0]['pointIndex']
    fig = {
        'data': [go.Scatter(
            x = [0,1],
            y = [0,60/df.iloc[v_index]['acceleration']],
            mode='lines',
            line={'width':2*df.iloc[v_index]['cylinders']}
        )],
        'layout': go.Layout(
            title = df.iloc[v_index]['name'],
            xaxis = {'visible':False},
            yaxis = {'visible':False, 'range':[0,60/df['acceleration'].min()]},
            margin = {'l':0},
            height = 300
        )
    }
    return fig

if __name__ == '__main__':
    app.run_server()
