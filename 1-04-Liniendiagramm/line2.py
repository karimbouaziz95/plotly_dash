#######
# Dieses Liniendiagramm (line chart) zeigt die Population von sechs New England Staaten
# vom U.S. Census Bureau an.
######
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# Eine .csv-Datei in ein Pandas-DataFrame einlesen:
df = pd.read_csv('../DATA/population.csv', index_col=0)

# create traces
traces = [go.Scatter(
    x = df.columns,
    y = df.loc[name],
    mode = 'markers+lines',
    name = name
) for name in df.index]

layout = go.Layout(
    title = 'Population Estimates of the Six New England States'
)

fig = go.Figure(data=traces,layout=layout)
pyo.plot(fig, filename='line2.html')
