
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div([
    dcc.Input(id='my-in', value='initial value', type='text'),
    html.Div( id='my-div'),
])

@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='my-in', component_property='value')]
)
def update_output_div(input_value):
    return 'Deine Eingabe ist: "{}"'.format(input_value)

if __name__ == '__main__':
    app.run_server()
