import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv("../DATA/mpg.csv")

print(df)
print(min(df["mpg"].unique()))

data = [go.Histogram(
        x = df["mpg"],
        xbins=dict(start=0,end=50,size = 1))
    ]
    
layout = go.Layout(
        title = "Histogram")

fig = go.Figure(data =data, layout=layout)
pyo.plot(fig)