import dash
from dash.html.Tr import Tr
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.layout = html.Div(
    [
        html.Label("Dropdown"),
        dcc.Dropdown(
            options=[
                {"label": "Berlin", "value": "BER"},
                {"label": "München", "value": "MUC"},
                {"label": "Hamburg", "value": "HAM"}
            ],
            value="HAM",
            multi=True
        ),
        html.Label("Slider"),
        dcc.Slider(
            min = -5,
            max = 10,
            step = 1,
            value = 1,
            marks={i: i for i in range(-5,11)}
        ),
        html.P(html.Label("Radio")),
        dcc.RadioItems(
            options=[
                {"label": "Berlin", "value": "BER"},
                {"label": "München", "value": "MUC"},
                {"label": "Hamburg", "value": "HAM"}
            ],
            value="BER"
        )
    ]
)

if __name__ == "__main__":
    app.run_server()