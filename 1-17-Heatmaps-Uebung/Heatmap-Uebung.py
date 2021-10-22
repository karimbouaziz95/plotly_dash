#######
# Ziel: Verwende den Datensatz "flights" aus der
# Datei flights.csv im Verzeichnis DATA
# und erzeuge eine Heatmap mit den folgenden Parametern:
# x-Achse="year"
# y-Achse="month"
# z-Achse (Farbe)="passengers"
######

# Führe hier die Importe aus:
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go


# Erzeuge ein DataFrame aus der .csv-Datei  "flights"
df = pd.read_csv('../DATA/flights.csv')
print(min(df["passengers"].unique()))

# Erzeuge eine Variable data:
data = [go.Heatmap(
        x = df["year"],
        y = df["month"],
        z = df["passengers"],
        colorscale = "Jet",
        zmin = 100,
        zmax = 650
    )]


# Definiere das Layout
layout = go.Layout(title="Number of passengers")

# Erzeuge eine fig mit data & layout und plotte die fig
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)



