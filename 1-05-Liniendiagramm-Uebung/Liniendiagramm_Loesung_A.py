#######
# Ziel: Verwende die Datei 2010YumaAZ.csv und entwickle ein Liniendiagramm (line chart)
# dass die Temperaturaufzeichnungen von sieben Tagen in einem Graphen darstellt.
# Du kannst eine Schleife verwenden, um jedem Tag eine eigene Linie zuzuweisen.
######

# Importe hier ausführen:
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# Erzeuge ein Pandas DataFrame aus 2010YumaAZ.csv
df = pd.read_csv('../DATA/2010YumaAZ.csv')
days = ['TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY','MONDAY']

# Verwende eine Schleife (oder List Comprehension), um Linien für die Liste data zu erstellen
data = []

for day in days:
    trace = go.Scatter(x=df['LST_TIME'],
                       y=df[df['DAY']==day]['T_HR_AVG'],
                       mode='lines',
                       name=day)
    data.append(trace)

# Definiere das Layout
layout = go.Layout(
    title='Daily temperatures from June 1-7, 2010 in Yuma, Arizona',
    hovermode='closest'
)

# Erzeuge eine fig mit den Daten und dem Layout und plotte die fig
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='solution2a.html')
