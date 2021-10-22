#######
# Ziel: Verwende den Datensatz "flights" aus der
# Datei flights.csv im Verzeichnis DATA
# und erzeuge eine Heatmap mit den folgenden Parametern:
# x-Achse="year"
# y-Achse="month"
# z-Achse (Farbe)="passengers"
######

# Führe hier die Importe aus:
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd 

# Erzeuge ein DataFrame aus der .csv-Datei  "flights"
df = pd.read_csv('../DATA/flights.csv')

# Erzeuge eine Variable data:
data = [go.Heatmap(
    x=df['year'],
    y=df['month'],
    z=df['passengers']
)]

# Definiere das Layout
layout = go.Layout(
    title='Flights'
)
# Erzeuge eine fig mit data & layout und plotte die fig
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='solution8.html')

#######
# Ausgezeichnet! Dies zeigt zwei verschiedene Trends - eine Steigerung der
# Passagierzahl über die Jahre und eine grössere Anzahl von 
# Passagieren in den Sommermonaten.
######
