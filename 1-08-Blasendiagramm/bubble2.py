#######
# Ein Blasendiagramm (bubble chart) ist einfach ein 
# Streudiagramm (scatter plot) mit der Möglichkeit, unterschiedliche
# Markergrössen in Abhängigkeit der Daten zu definieren.
######
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('../DATA/mpg.csv')

# Füge dem DataFrame Spalten hinzu, um das Jahr des Modells in einen
# String zu konvertieren und mit dem Namen zu verbinden, 
# so dass der Hilfstext beides anzeigt:
df['text1']=pd.Series(df['model_year'],dtype=str)
df['text2']="'"+df['text1']+" "+df['name']

data = [go.Scatter(
            x=df['horsepower'],
            y=df['mpg'],
            text=df['text2'],  # Verwende die neue Spalte für Hilfstexte
            mode='markers',
            marker=dict(size=1.5*df['cylinders'])
    )]
layout = go.Layout(
    title='Vehicle mpg vs. horsepower',
    hovermode='closest'
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bubble2.html')
