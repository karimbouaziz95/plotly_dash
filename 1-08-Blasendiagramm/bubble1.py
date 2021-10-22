#######
# Ein Blasendiagramm (bubble chart) ist einfach ein 
# Streudiagramm (scatter plot) mit der Möglichkeit, unterschiedliche
# Markergrössen in Abhängigkeit der Daten zu definieren.
######
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('../DATA/mpg.csv')

data = [go.Scatter(          # Beginne mit einem normalen Streudiagramm
    x=df['horsepower'],
    y=df['mpg'],
    text=df['name'],
    mode='markers',
    marker=dict(size=1.5*df['cylinders']) # Setze die Markergrösse
)]

layout = go.Layout(
    title='Vehicle mpg vs. horsepower',
    xaxis = dict(title = 'horsepower'), # x-Achsenbeschriftung
    yaxis = dict(title = 'mpg'),        # y-Achsenbeschriftung
    hovermode='closest'
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bubble1.html')
