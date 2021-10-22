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

random_x = np.random.randn(1000)
random_y = np.random.rand(1000)

# Definiere das Layout
layout = go.Layout(
        title = "Streudiagramm Aufgabe",
        xaxis = dict(title = "XXXXXXXXX"),
        yaxis = dict(title = "YYYYYYYYYY"),
        hovermode = "closest"
    )

# Erzeuge eine fig mit den Daten und dem Layout und plotte die fig
fig = go.Figure(layout = layout)

fig.add_trace(go.Scatter(
            x = random_x,
            y = random_y,
            mode = "markers",
            
            
    ))

pyo.plot(fig, filename="versuch.html")