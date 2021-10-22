#######
# Ziel: Verwende den Datensatz Iris und entwickle einen Distplot,
# der die Länge der Petals (Kronenblätter) vergleicht.
# Datei: '../DATA/iris.csv'
# Felder: 'sepal_length','sepal_width','petal_length','petal_width','class'
# Klassen: 'Iris-setosa','Iris-versicolor','Iris-virginica'
######

# Führe hier die Importe aus:
import pandas as pd
import plotly.offline as pyo
import plotly.figure_factory as ff



# Erzeuge ein DataFrame aus der .csv-Datei:
df = pd.read_csv("../DATA/iris.csv")
print(df)

# Definiere die Traces (Linien)

data = [df[df["class"] == name]["petal_length"] for name in df["class"].unique()]
labels = [name for name in df["class"].unique()]
print(data)
print(labels)

# HINWEIS:
# Dies gibt die Spalte petal_length einer bestimmten Blume zurück
#df[df['class']=='Iris-some-flower-class']['petal_length']



# Erzeuge eine Variable data:



# Erzeuge eine fig mit data & layout und plotte die fig
fig = ff.create_distplot(data, labels)
pyo.plot(fig)

