import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

colors = {"background": "#111111", "text": "#50DB44"}


app.layout = html.Div(children=[
    html.H1(children="Hello Dash",
            style={
                    "textAlign": "center",
                    "color": colors["text"]
            }
            ),
    html.H2(children="Ahla b zebi"),
    html.P(children="everybody wanna live together"),
    html.Div(children="Dashhhhhh"),

    dcc.Graph(
        id = "example-graph",
        figure={
            "data": [
                    {
                        "x": [1,2,3],
                        "y": [4,1,2],
                        "type": "bar",
                        "name": "SF"
                    },
                    {
                        "x": [1,2,3],
                        "y": [2,4,5],
                        "type": "bar",
                        "name": "Berlin"
                    }

            ],
            "layout": {
                        "title": "Dash Viz",
                        "plot_bgcolor": colors["background"],
                        "paper_bgcolor": colors["background"],
                        "font": {"color": colors["text"]}
                      }

        }
    )
    ],
    style={"backgroundColor": "#ffffff"}
    )

if __name__ == "__main__":
    app.run_server()