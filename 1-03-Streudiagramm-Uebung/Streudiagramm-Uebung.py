#######
# Ziel: Erzeuge ein Streudiagramm (scatter plot) mit 1000 zufälligen Datenpunkten.
# Die Werte der X-Achse sollen normalverteilt sein mit
# np.random.randn(1000)
# Die Werte der Y-Achse sollen gleichverteilt sein über [0,1) mit
# np.random.rand(1000)
######

# Führe hier die Importe aus:
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go



# Definiere eine Datenvariable
x = np.random.randn(1000)
y = np.random.rand(1000)

# Definiere das Layout
layout = go.Layout(
        title = "Scatter pot ubung",
        xaxis = {"title": "xxxxxx"},
        yaxis = {"title": "yyyyyy"},
        hovermode = "closest"
    )



# Erzeuge eine fig mit den Daten und dem Layout und plotte die fig
data = [go.Scatter(
        x = x,
        y = y,
        mode = "markers",
        marker = dict(color="#e3ae10")
        
    )]

fig = go.Figure(data = data, layout = layout)
pyo.plot(fig)

