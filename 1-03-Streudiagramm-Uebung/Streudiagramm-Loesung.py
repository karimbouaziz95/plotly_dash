#######
# Ziel: Erzeuge ein Streudiagramm (scatter plot) mit 1000 zufälligen Datenpunkten.
# Die Werte der X-Achse sollen normalverteilt sein mit
# np.random.randn(1000)
# Die Werte der Y-Achse sollen gleichverteilt sein über [0,1) mit
# np.random.rand(1000)
######

# Führe hier die Importe aus:
import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np

# Erhalte x und y Werte
random_x = np.random.randn(1000) # normal distribution
random_y = np.random.rand(1000)  # uniform distribution

# Definiere eine Datenvariable
data = [go.Scatter(
    x = random_x,
    y = random_y,
    mode = 'markers',
)]

# Definiere das Layout inklusive Titel und Achsenlabels
layout = go.Layout(
    title = 'Random Data Scatterplot', # Titel des Graphen
    xaxis = dict(title = 'Normal distribution'), # Label der X-Achse
    yaxis = dict(title = 'Uniform distribution'), # Label der Y-Achse
    hovermode ='closest' # Behandelt multiple Punkte auf der vertikalen Achse
)

# Erzeuge eine fig mit den Daten und dem Layout und plotte die fig
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='solution1.html')
