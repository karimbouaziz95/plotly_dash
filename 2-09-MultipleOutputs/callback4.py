#######
# Dies verwendet den kleinen Datensatz wheels.csv
# um multiple Ausgaben zu demonstrieren.
######
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd

app = dash.Dash()

df = pd.read_csv('../DATA/wheels.csv')

app.layout = html.Div([
    dcc.RadioItems(
        id='wheels',
        options=[{'label': i, 'value': i} for i in df['wheels'].unique()],
        value=1
    ),
    html.Div(id='wheels-output'),

    html.Hr(),  # Füge eine horizontale Linie hinzu
    dcc.RadioItems(
        id='colors',
        options=[{'label': i, 'value': i} for i in df['color'].unique()],
        value='blue'
    ),
    html.Div(id='colors-output')
], style={'fontFamily':'helvetica', 'fontSize':18})

@app.callback(
    Output('wheels-output', 'children'),
    [Input('wheels', 'value')])
def update_a(wheels_value):
    return 'Deine Auswahl: "{}"'.format(wheels_value)

@app.callback(
    Output('colors-output', 'children'),
    [Input('colors', 'value')])
def update_b(colors_value):
    return 'Deine Auswahl: "{}"'.format(colors_value)

if __name__ == '__main__':
    app.run_server()
