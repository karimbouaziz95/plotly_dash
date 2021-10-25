import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Output, Input
import base64

app = dash.Dash()

df = pd.read_csv("DATA/wheels.csv")
print("****************************************")
print(df[(df["wheels"] == 1) & (df["color"] == "red")]["image"].values[0])
print("****************************************")


def encode_image(image_file):
    encoded = base64.b64encode(open(image_file, "rb").read())
    return "data:image/png;base64,{}".format(encoded.decode())

app.layout = html.Div(
    [
        dcc.RadioItems(
            id="wheels",
            options=[{"label": str(i), "value": i}
                     for i in df["wheels"].unique()],
            value=1
        ),
        html.Div(
            id="wheels-output"
        ),
        html.Hr(),
        dcc.RadioItems(
            id="colors",
            options=[{"label": str(i), "value": i}
                     for i in df["color"].unique()],
            value="blue"
        ),
        html.Div(
            id="colors-output"
        ),
        html.Img(
            id="display-image",
            src="children",
            height=300
        )
    ]
)


@app.callback(
    Output("wheels-output", "children"),
    [
        Input("wheels", "value")
    ]
)
def update_a(wheels_value):
    return "Deine Auswahl ist: '{}'".format(wheels_value)


@app.callback(
    Output("colors-output", "children"),
    [
        Input("colors", "value")
    ]
)
def update_b(colors_value):
    return "Deine Auswahl ist: '{}'".format(colors_value)


@app.callback(
    Output("display-image", "src"),
    [
        Input("wheels", "value"),
        Input("colors", "value")
    ]
)
def update_image(wheel, color):
    path = "DATA/images/"
    image = df[(df["wheels"] == wheel) & (df["color"] == color)]["image"].values[0]
    return encode_image(path+image)

if __name__ == "__main__":
    app.run_server()
