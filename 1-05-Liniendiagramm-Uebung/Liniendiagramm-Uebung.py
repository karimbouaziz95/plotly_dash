#######
# Ziel: Verwende die Datei 2010YumaAZ.csv und entwickle ein Liniendiagramm (line chart)
# dass die Temperaturaufzeichnungen von sieben Tagen in einem Graphen darstellt.
# Du kannst eine Schleife verwenden, um jedem Tag eine eigene Linie zuzuweisen.
######

# Importe hier ausführen:
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go


# Erzeuge ein Pandas DataFrame aus 2010YumaAZ.csv
df = pd.read_csv('../DATA/2010YumaAZ.csv')
days = ['TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY','MONDAY']

print(df)

# Verwende eine Schleife (oder List Comprehension), um Linien für die Liste data zu erstellen
data = []

for day in days:
    # Was gehört in diesen Aufruf von Scatter?
    trace = go.Scatter(
            x = df[df["DAY"] == day]["LST_TIME"],
            y = df[df["DAY"] == day]["T_HR_AVG"],
            name = day,
            mode = "markers+lines"
        )
    data.append(trace)

# Definiere das Layout

layout = go.Layout(
        title = "Temperaturschwankungen",
        xaxis = {"title": "Zeit in hh:mm"},
        yaxis = {"title": "Temperatur in °C"},
        hovermode = "closest")


# Erzeuge eine fig mit den Daten und dem Layout und plotte die fig
fig = go.Figure(data = data, layout = layout)
pyo.plot(fig)


