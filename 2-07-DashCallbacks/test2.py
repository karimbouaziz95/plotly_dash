from os import name
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go

app = dash.Dash()

df = pd.read_csv("DATA/gapminderDataFiveYear.csv")

year_options = [{"label": str(year), "value": year} for year in df["year"].unique()]
print(year_options)
filtered_df = df[df["year"] == 2007]
filtered_by_cont = filtered_df[filtered_df["continent"] == "Asia"]
print(filtered_by_cont)

app.layout = html.Div(
    [
        dcc.Graph(
            id="my-graph"
        ),
        dcc.Dropdown(
            id="year-picker",
            options=year_options,
            value=df["year"].unique().min()
        )
    ]
)

@app.callback(
    Output("my-graph", "figure"),
    [Input("year-picker", "value")]
)
def update_figure(selected_year):
    filtered_df = df[df["year"] == selected_year]
    traces = []
    for continent_name in filtered_df["continent"].unique():
        df_by_continent = filtered_df[filtered_df["continent"]==continent_name]
        traces.append(
            go.Scatter(
                x = df_by_continent["gdpPercap"],
                y = df_by_continent["lifeExp"],
                text = df_by_continent["country"],
                mode = "markers",
                name=continent_name,
                marker = {"size": 15},
                opacity= 0.2
                
            )
        )
    
    return{
        "data": traces,
        "layout": go.Layout(
            title="Lebensdauer gegen Gehalt",
            xaxis = dict(title="Einkommen in GPD", type="log"),
            yaxis = dict(title="Life Expactancy"),
            hovermode = "closest"
        )
    }
        


if __name__ == "__main__":
    app.run_server()