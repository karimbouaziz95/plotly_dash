import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import json

app = dash.Dash()

df = pd.read_csv('DATA/mpg.csv')
print(df.columns)
df['year'] = np.random.randint(-4, 5, len(df))*0.10 + df['model_year']
print(df)


app.layout = html.Div([
    html.Div(
        [
            dcc.Graph(
                id='mpg_scatter',
                figure={
                    'data': [go.Scatter(
                        x=df['year']+1900,
                        y=df['mpg'],
                        text=df['name'],
                        hoverinfo='text',
                        mode='markers'
                    )],
                    'layout': go.Layout(
                        title='mpg.csv dataset',
                        xaxis={'title': 'model year'},
                        yaxis={'title': 'miles per gallon'},
                        hovermode='closest'
                    )
                }
            )

        ],
        style={"display": "inline-block", "width": "50%", "float": "left"}
    ),
    html.Div(
        [
            dcc.Graph(
                id="steigung"
            )
        ],
        style={"display": "inline-block", "width": "35%"}
    )
])


@app.callback(
    Output("steigung", "figure"),
    [
        Input("mpg_scatter", "hoverData")
    ]
)
def show_me(hoverData):
    v_index = hoverData["points"][0]["pointIndex"]
    fig = {
        "data": [
            go.Scatter(
                x=[0, 1],
                y=[0, 60/df.iloc[v_index]["acceleration"]],
                mode="lines",
                line={"width": 2*df.iloc[v_index]["cylinders"]}
            )
        ],
        "layout": go.Layout(
            title="Acceleration",
            height = 300,
            yaxis = {'visible':False, 'range':[0,60/df['acceleration'].min()]}
        )
    }

    return fig


if __name__ == '__main__':
    app.run_server()
