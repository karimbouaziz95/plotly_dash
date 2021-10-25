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
            min = -10,
            max = 10,
            value=[-6, 7],
            marks={i: i for i in range(-10, 11)}
        ),
        html.H1(
            id="result"
        )
    ],
    style={"width":"50%"}
)

# Erzeuge ein Dash-Callback (Rückruf):

@app.callback(
    Output("result", "children"),
    [
        Input("ranger", "value")
    ]
)
def update_result(valeur):
    return valeur[0]*valeur[1]


# Füge den Server-Abschnitt hinzu:

if __name__ == "__main__":
    app.run_server()


