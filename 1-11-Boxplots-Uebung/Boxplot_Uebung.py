#######
# Ziel: Erzeuge einen DataFrame aus dem Abalone Datensatz (../DATA/abalone.csv).
# Nimm zwei zufällige, unabhängige Stichproben verschiedener Grössen aus dem Feld 'rings'.
# Hinweis: np.random.choice(df['rings'],10,replace=False) nimmt 10 Zufallswerte
# Verwende Boxplots um zu zeigen, dass die Stichproben aus der gleichen Verteilung stammen.
######

# Führe hier die Importe aus:
import numpy as np
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go


# Erzeuge ein DataFrame aus der .csv-Datei:
    
df = pd.read_csv("../DATA/abalone.csv")

print(df)
print(df.columns)

# Nimm zwei zufällige Stichproben verschiedener Grössen:
a = np.random.choice(df['rings'],30,replace=False)
b = np.random.choice(df['rings'],100,replace=False)



# Erzeuge eine Variable data mit zwei Boxplots:
data = [go.Box(
        y = a,
        name = "A"),
    go.Box(
        y = b,
        name = "B")
    ]


# Füge ein Layout hinzu
layout = go.Layout(
    title = "Comparison of two samples taken from the same population")

# Erzeuge eine fig mit data & layout und plotte die fig
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)

