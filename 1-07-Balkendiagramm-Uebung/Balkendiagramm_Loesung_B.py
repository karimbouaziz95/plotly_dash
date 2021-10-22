#######
# Ziel: Erzeuge ein gestaffeltes Balkendiagramm (Barchart) aus der
# Datei ../data/mocksurvey.csv. Beachte, dass Fragen im Index erscheinen
# (und für die x-Achse verwendet werden sollen, wohingegen Antworten
# Spaltenlabels vorliegen. Bonuspunkte: mache ein horizontales Balkendiagramm
######

# Importe hier ausführen:
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# Erzeuge einen DataFrame aus der .csv Datei:
df = pd.read_csv('../DATA/mocksurvey.csv',index_col=0)

# Erzeuge die Werte einzelner Balken mittels einer List Comprehension:
data = [go.Bar(
    y = df.index,     # Invertiere deine Zuweisungen zu der x- und y-Achse
    x = df[response],
    orientation='h',  # diese Zeile macht es horizontal!
    name=response
) for response in df.columns]

# Erzeuge ein Layout und setze dabei den Parameter barmode
layout = go.Layout(
    title='Mock Survey Results',
    barmode='stack'
)

# Erzeuge eine fig mit data & layout und plotte die fig.
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='solution3b.html')
