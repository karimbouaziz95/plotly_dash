#######
# Ziel: Erzeuge ein Histogramm zur Darstellung des Feldes 'length'
# aus dem Datensatz Abalone (../data/abalone.csv).
# Setze den Bereich (range) auf 0 bis 1, mit einer Klassengrösse (bin size) von 0.02
######

# Führe hier die Importe aus:
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# Erzeuge ein DataFrame aus der .csv-Datei:
df = pd.read_csv('../DATA/abalone.csv')

# Erzeuge eine Variable data:
data = [go.Histogram(
    x=df['length'],
    xbins=dict(start=0,end=1,size=.02),
)]

# Füge ein Layout hinzu
layout = go.Layout(
    title="Shell lengths from the Abalone dataset"
)

# Erzeuge eine fig mit data & layout und plotte die fig
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='solution6.html')
