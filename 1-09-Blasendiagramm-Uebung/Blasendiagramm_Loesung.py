#######
# Ziel: Erzeuge ein Blasendiagramm (bubble chart), welches drei Felder des 
# Datensatzes mpg.csv vergleicht. Felder beinhalten: 'mpg', 'cylinders', 'displacement'
# 'horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'name'
######

# Führe hier die Importe aus:
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# Erzeuge ein DataFrame aus der .csv-Datei:
df = pd.read_csv('../DATA/mpg.csv')

# Erzeuge data durch die Auswahl von Feldern für x, y und die Grösse der Marker
data = [go.Scatter(
    x=df['displacement'],
    y=df['acceleration'],
    text=df['name'],
    mode='markers',
    marker=dict(size=df['weight']/500)
)]

# Erzeuge ein Layout mit Titel und Achsenbeschriftungen
layout = go.Layout(
    title='Vehicle acceleration vs. displacement',
    xaxis = dict(title = 'displacement'),
    yaxis = dict(title = 'acceleration = seconds to reach 60mph'),
    hovermode='closest'
)

# Erzeuge eine fig mit data & layout und plotte die fig
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='solution4.html')
#######
# Was ist passiert? Weshalb geht der Trend nach unten?
# Bedenke, Beschleunigung ist die Anzahl von Sekunden von 0 auf 60 mph,
# weniger Sekunden bedeuten also eine höhere Beschleunigung!
######
