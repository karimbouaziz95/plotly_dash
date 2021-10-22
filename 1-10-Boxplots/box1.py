#######
# Dieser einfache Boxplot platziert die Box neben den
# ursprünglichen Datenpunkten auf dem selben Graphen.
######
import plotly.offline as pyo
import plotly.graph_objs as go

# Erzeuge ein Array mit 20 Datenpunkten, mit 20 als Medianwert
y = [1,14,14,15,16,18,18,19,19,20,20,23,24,26,27,27,28,29,33,54]

data = [
    go.Box(
        y=y,
        boxpoints='all', # Zeige die ursprünglichen Datenpunkte an
        jitter=0.3,      # Verteile sie, so dass sie alle sichtbar sind
        pointpos=-1.8    # Versetze sie auf die linke Seite der Box
    )
]
pyo.plot(data, filename='box1.html')
