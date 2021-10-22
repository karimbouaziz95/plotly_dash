#######
# Dieses Liniendiagramm (line chart) zeigt die Population von sechs New England Staaten
# vom U.S. Census Bureau an.
# DIESER PLOT VERWENDET PANDAS ZUR EXTRAKTION DER ERWÜNSCHTEN 
# DATEN AUS DER QUELLE
######
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('../DATA/nst-est2017-alldata.csv')
# Alternativ:
# df = pd.read_csv('https://www2.census.gov/programs-surveys/popest/datasets/2010-2017/national/totals/nst-est2017-alldata.csv')

# Nimm nur die sechs New England Staaten:
df2 = df[df['DIVISION']=='1']
# Setze den Index auf Staatennamen:
df2.set_index('NAME', inplace=True)
# Nimm nur die Spalte mit der Population:
df2 = df2[[col for col in df2.columns if col.startswith('POP')]]

traces=[go.Scatter(
    x = df2.columns,
    y = df2.loc[name],
    mode = 'markers+lines',
    name = name
) for name in df2.index]

layout = go.Layout(
    title = 'Population Estimates of the Six New England States'
)

fig = go.Figure(data=traces,layout=layout)
pyo.plot(fig, filename='line3.html')
