import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(52)
x_values = np.linspace(0,1,100)
y_values = np.random.randn(100)

trace0 = go.Scatter(
        x = x_values,
        y = y_values+5,
        mode = "lines",
        name = "my lines"
    )

trace1 = go.Scatter(
        x = x_values,
        y = y_values,
        mode = "lines+markers",
        name = "my lines and markers"
    )

data = [trace0, trace1]

layout = go.Layout(title = "Line Chart")
fig = go.Figure(data = data, layout = layout)

pyo.plot(fig)