import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv("../DATA/2018WinterOlympics.csv")

print(df)

trace_gold = go.Bar(
        x = df["NOC"],
        y = df["Gold"],
        name = "Gold",
        marker = {"color": "#FFD700"}
    )

trace_silver = go.Bar(
        x = df["NOC"],
        y = df["Silver"],
        name = "Silver",
        marker = {"color": "#C0C0C0"}
    )

trace_bronze = go.Bar(
        x = df["NOC"],
        y = df["Bronze"],
        name = "Bronze",
        marker = {"color": "#bf8970"}
    )


data = [trace_gold, trace_silver, trace_bronze]

layout = go.Layout(title = "Medals winners 2018 olympics",
                   barmode ="stack")
fig = go.Figure(layout = layout, data = data)

pyo.plot(fig)