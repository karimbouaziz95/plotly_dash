#######
# Ein sehr einfacher Eingabe/Ausgabe Callback.
######
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div([
    dcc.Input(
        id='number-in',
        value=1,
        style={'fontSize':28}
    ),
    html.H1(id='number-out')
])

@app.callback(
    Output('number-out', 'children'),
    [Input('number-in', 'value')])
def update_output(number):
    return number

if __name__ == '__main__':
    app.run_server()
