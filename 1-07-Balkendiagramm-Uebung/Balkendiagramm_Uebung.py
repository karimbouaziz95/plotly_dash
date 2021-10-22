#######
# Ziel: Erzeuge ein gestaffeltes Balkendiagramm (Barchart) aus der
# Datei ../DATA/mocksurvey.csv. Beachte, dass Fragen im Index erscheinen
# (und für die x-Achse verwendet werden sollen, wohingegen Antworten
# Spaltenlabels vorliegen. 

# Bonuspunkte: mache ein horizontales Balkendiagramm
######

# Importe hier ausführen:
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go


# Erzeuge einen DataFrame aus der .csv Datei (verwende index_col=0):
df = pd.read_csv("DATA/mocksurvey.csv", index_col=0)
print(df)
print(df.index)
print(df["Neutral"])

# Erzeuge die Werte einzelner Balken mittels einer List Comprehension:
data = [
    go.Bar(
        x = df.index,
        y = df[question],
        name = question

    ) for question in df.columns
]


# Erzeuge ein Layout und setze dabei den Parameter barmode

layout = go.Layout(
        title="Questions and answers",
        barmode = "stack")


# Erzeuge eine fig mit data & layout und plotte die fig
fig = go.Figure(data = data, layout = layout)
pyo.plot(fig)