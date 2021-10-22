import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(42)

random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

data = [go.Scatter(
        x = random_x,
        y = random_y,
        mode = "markers",
        marker = dict(size = 30, color = "rgb(24,0,220)")
    ),
    go.Scatter(
        x = random_y,
        y = random_x,
        mode = "markers",
        marker = dict(size = 30, color = "rgb(75,51,3)")
    )]

my_layout = go.Layout(
        title = "Everybody want ot live together",
        xaxis = dict(title = "XXXXX"),
        yaxis = dict(title = "YYYYY"),
        hovermode = "closest"
    )

fig = go.Figure(data = data, layout=my_layout)

pyo.plot(fig, filename="zeby.html")