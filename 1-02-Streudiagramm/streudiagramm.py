import plotly.offline as pyo
import numpy as np
import plotly.graph_objs as go

np.random.seed(42)

random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

data = [go.Scatter(
    x = random_x,
    y = random_y,
    mode = "markers",
    marker = {"size": 30, "color": "rgb(51,204,153)", "symbol": "pentagon"})]

layout = go.Layout(
    title = "I´m the title",
    xaxis = {"title": "Je suis l'axe des abscisses"},
    yaxis = {"title": "Je suis l'axe des ordonnees"},
    hovermode = "closest"
    )

fig = go.Figure(data = data, layout = layout)

pyo.plot(fig)