#######
# Dieses Histogramm zeigt an, wie oft der Reddit-Button gedrückt wurde
# im Zeitraum der zwei Monate ihres sozialen Experimentes.
######
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('../DATA/thebutton_presses.csv')

data = [go.Histogram(
    x=df['press time'],
    nbinsx=60
)]

layout = go.Layout(
    title="Number of presses per timeslot"
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='button_presses2.html')
