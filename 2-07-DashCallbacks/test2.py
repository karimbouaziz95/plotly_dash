import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output

app = dash.Dash()

df = pd.read_csv("DATA/gapminderDataFiveYear.csv")

year_options = [{"label": str(item), "value": item}
                for item in df["year"].unique()]
print(year_options)

app.layout = html.Div(
    [
        dcc.Graph(
            id="graph"
        ),
        dcc.Dropdown(
            id="year-picker",
            options=year_options,
            value=df["year"].min()
        )
    ]
)


@app.callback(
    Output("graph", "figure"),
    [Input("year-picker", "value")]
)
def update_figure(selected_year):
    filtered_df = df[df["year"] == selected_year]
    traces = []
    
    for continent_name in filtered_df["continent"].unique():
        df_by_continent = filtered_df[filtered_df["continent"] == continent_name]
        traces.append(
            go.Scatter(
                x = df_by_continent["gdpPercap"],
                y = df_by_continent["lifeExp"],
                text = df_by_continent["country"],
                mode = "markers",
                marker = {"size": 15},
                opacity=0.7,
                name = continent_name
            )
        )
    return {
        "data": traces,
        "layout": go.Layout(
            title="myy layout",
            xaxis={"type": "log", "title": "GPD per capital"},
            yaxis = {"title": "Lebenserwartung"}
        )
    }


if __name__ == "__main__":
    app.run_server()
