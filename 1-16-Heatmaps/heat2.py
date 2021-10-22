#######
# Heatmap der Temperatur f�r Yuma, Arizona
######
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('../DATA/2010YumaAZ.csv')

data = [go.Heatmap(
    x=df['DAY'],
    y=df['LST_TIME'],
    z=df['T_HR_AVG'],
    colorscale='Jet'
)]

layout = go.Layout(
    title='Hourly Temperatures, June 1-7, 2010 in<br>\
    Yuma, AZ USA'
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='Yuma.html')
