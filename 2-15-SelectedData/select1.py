#######
# Dies erzeugt ein 3x3 Streudiagramm von wheels.csv und sendet das
# Ergebnis einer Auswahl (Selection) auf den Screen als JSON-Objekt.
######
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import json

app = dash.Dash()

df = pd.read_csv('../DATA/wheels.csv')

app.layout = html.Div([
    html.Div([
    dcc.Graph(
        id='wheels-plot',
        figure={
            'data': [
                go.Scatter(
                    x = df['color'],
                    y = df['wheels'],
                    dy = 1,
                    mode = 'markers',
                    marker = {
                        'size': 12,
                        'color': 'rgb(51,204,153)',
                        'line': {'width': 2}
                        }
                )
            ],
            'layout': go.Layout(
                title = 'Wheels & Colors Scatterplot',
                xaxis = {'title': 'Color'},
                yaxis = {'title': '# of Wheels','nticks':3},
                hovermode='closest'
            )
        }
    )], style={'width':'50%', 'display':'inline-block'}),

    html.Div([
    html.Pre(id='selection', style={'paddingTop':25})
    ], style={'width':'30%', 'display':'inline-block', 'verticalAlign':'top'})
])

@app.callback(
    Output('selection', 'children'),
    [Input('wheels-plot', 'selectedData')])
def callback_image(selectedData):
    return json.dumps(selectedData, indent=2)

if __name__ == '__main__':
    app.run_server()
