#######
# Erzeuge ein Dashboard, dass zwei oder mehr Eingabewerte annimmt
# und deren Produkt als Ausgabe zurückgibt.
######

# Führe hier die Importe aus:
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input, State

# Führe die Anwendung aus:
app = dash.Dash()

# Erzeuge ein Dash-Layout mit Eingabekomponenten und zumindest einer
# Ausgabe. Weise jeder Komponente eine ID zu:

app.layout = html.Div(
    [
        html.P("The multiplication double Slider"),
        dcc.RangeSlider(
            id="ranger",
            min=-10,
            max=10,
            value=[-6, 7],
            marks={i: i for i in range(-10, 11)}
        ),
        html.Button(
            id='submit-button',
            n_clicks=0,
            children='Submit',
            style={'fontSize': 28}
        ),
        html.H1(
            id="result"
        )
    ]
)
# Erzeuge ein Dash-Callback (Rückruf):

@app.callback(
    Output("result", "children"),
    [
        Input("submit-button", "n_clicks")
    ],
    [
        State("ranger", "value")
    ]
)
def update_result(clicks, valeur):
    return "{} is the result after {} clicks".format(valeur[0]*valeur[1], clicks)

# Füge den Server-Abschnitt hinzu:

if __name__ == "__main__":
    app.run_server()
