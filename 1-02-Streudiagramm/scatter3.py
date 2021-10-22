#######
# Dies stellt 100 zufällige Datenpunkte zwischen 1 und 100 sowohl in
# horizontaler als auch in vertikaler Richtung dar (setze den Seed auf 42, 
# um die gleichen Punkte wie wir zu erhalten!)
######
import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np

np.random.seed(42)
random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

data = [go.Scatter(
    x = random_x,
    y = random_y,
    mode = 'markers',
    marker = dict(      # Ändere den Stil des Markers
        size = 12,
        color = 'rgb(51,204,153)',
        symbol = 'pentagon',
        line = dict(
            width = 2,
        )
    )
)]
layout = go.Layout(
    title = 'Random Data Scatterplot', # Titel des Graphen
    xaxis = dict(title = 'Some random x-values'), # Label der X-Achse
    yaxis = dict(title = 'Some random y-values'), # Label der Y-Achse
    hovermode ='closest' # Behandelt multiple Punkte auf der vertikalen Achse
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='scatter3.html')
