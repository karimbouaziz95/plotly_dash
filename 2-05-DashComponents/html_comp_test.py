import dash
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([
    "Äußere Div",
    html.Div(
        "innere Div",
        style={"color": "blue",
               "border": "2px blue solid",
               "borderRadius": 5}
    ),
    html.Div(
        "2. innere Div",
        style={"color": "green",
               "border": "2px green solid",
               "borderRadius": 11,
               "width": 200,
               "margin": 10}
    )
],

    style={"width": 500,
           "height": 200,
           "color": "red",
           "border": "2px red dotted"}
)

if __name__ == "__main__":
    app.run_server()
