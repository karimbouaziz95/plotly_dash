import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv("../DATA/mpg.csv")
print(df)
print(df.columns)
print(df["horsepower"])

data = [go.Scatter(
        x = df["horsepower"].unique().sort(),
        y = df["mpg"],
        text = df["name"],
        mode = "markers",
        marker = dict(size = df["weight"]/100,
                      color=df["cylinders"],
                      showscale = True)
        
    )]

layout = go.Layout(title= "Verbrauch")
fig = go.Figure(data = data, layout = layout)


pyo.plot(fig)
