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
        html.H1("The multiplication double slider"),
        dcc.RangeSlider(
            id="product",
            marks={i: i for i in range(-10,11)},
            min=-10,
            max=10,
            step=1,
            value=[2,8]
        ),
        html.H3(id="result"),
        html.Button(
            id="calculate-button",
            children="Calculate!",
            n_clicks=0
        )
    ]
)

# Erzeuge ein Dash-Callback (Rückruf):

@app.callback(
    Output("result", "children"),
    [
        Input("calculate-button", "n_clicks")
    ],
    [
        State("product", "value")
    ]
)
def calculate_product(clicks, valeur):
    return "Le produit des deux nombres est: {}".format(valeur[0]*valeur[1])


# Füge den Server-Abschnitt hinzu:
if __name__ == "__main__":
    app.run_server()



