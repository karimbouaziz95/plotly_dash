#######
# Ein einfaches Balkendiagramm (Barchart) mit der Gesamtzahl gewonnener Medallien
# der Olympischen Winterspiele 2018 nach Land.
######
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('../DATA/2018WinterOlympics.csv')

data = [go.Bar(
    x=df['NOC'],  # NOC steht für National Olympic Committee (Nationales Olympisches Komitee)
    y=df['Total']
)]
layout = go.Layout(
    title='2018 Winter Olympic Medals by Country'
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bar1.html')
