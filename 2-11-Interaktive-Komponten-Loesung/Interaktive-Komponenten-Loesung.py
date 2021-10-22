#######
# Erzeuge ein Dashboard, dass zwei oder mehr Eingabewerte annimmt
# und deren Produkt als Ausgabe zurückgibt.
######

# Führe hier die Importe aus:
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Führe die Anwendung aus:
app = dash.Dash()

# Erzeuge ein Dash-Layout mit Eingabekomponenten und zumindest einer
# Ausgabe. Weise jeder Komponente eine ID zu:
app.layout = html.Div([
    dcc.RangeSlider(       # Dies ist der input
        id='range-slider',
        min=-5,
        max=6,
        marks={i:str(i) for i in range(-5, 7)},
        value=[-3, 4]
    ),
    html.H1(id='product')  # Dies ist der output
], style={'width':'50%'})

# Erzeuge ein Dash-Callback (Rückruf):
@app.callback(
    Output('product', 'children'),
    [Input('range-slider', 'value')])
def update_value(value_list):
    return value_list[0]*value_list[1]

# Füge den Server-Abschnitt hinzu:
if __name__ == '__main__':
    app.run_server()
