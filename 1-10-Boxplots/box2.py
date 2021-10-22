#######
# Dieser einfache Boxplot zeigt nur
# Datenpunkte über- und oberhalb der Box an.
######
import plotly.offline as pyo
import plotly.graph_objs as go

# Erzeuge ein Array mit 20 Datenpunkten, mit 20 als Medianwert
y = [1,14,14,15,16,18,18,19,19,20,20,23,24,26,27,27,28,29,33,54]

data = [
    go.Box(
        y=y,
        boxpoints='outliers' # Zeige nur Datenpunkte ausserhalb der Box an
    )
]
pyo.plot(data, filename='box2.html')
