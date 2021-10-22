####################
## BEACHTE: FORTGESCHRITTENE LÖSUNG DIE NUR REINE DF AUFRUFE VERWENDET
## DIES IST FÜR FORTGESCHRITTENERE PANDAS-ANWENDER ZUR BETRACHTUNG! :)

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

# Definiere die Variable data
data = [{
    'x': df['LST_TIME'],
    'y': df[df['DAY']==day]['T_HR_AVG'],
    'name': day
} for day in df['DAY'].unique()]

# Definiere das Layout
layout = go.Layout(
    title='Daily temperatures from June 1-7, 2010 in Yuma, Arizona',
    hovermode='closest'
)

# Erzeuge eine fig mit den Daten und dem Layout und plotte die fig
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='solution2b.html')
