#######
# Dieses Balkendiagramm imitiert ein Histogramm, da die x-Achse
# kontinuierliche Zeit darstellt und die y-Achse
# über eine Frequenz summiert, die bereits Teil des Datensatzes ist
######
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('../DATA/FremontBridgeBicycles.csv')

# Konvertiere die Textspalte "Date" zu einer Datetime Series:
df['Date'] = pd.to_datetime(df['Date'])

# Füge eine Spalte für die Stunde hinzu:
df['Hour']=df['Date'].dt.time

# Lass Pandas die Daten aggregieren
df2 = df.groupby('Hour').sum()

trace1 = go.Bar(
    x=df2.index,
    y=df2['Fremont Bridge West Sidewalk'],
    name="Southbound",
    width=1  # Lösche den Raum zwischen aufeinanderfolgenden Balken
)
trace2 = go.Bar(
    x=df2.index,
    y=df2['Fremont Bridge East Sidewalk'],
    name="Northbound",
    width=1
)
data = [trace1, trace2]

layout = go.Layout(
    title='Fremont Bridge Bicycle Traffic by Hour',
    barmode='stack'
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='fremont_bridge.html')
