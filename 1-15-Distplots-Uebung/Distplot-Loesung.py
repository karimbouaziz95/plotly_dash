#######
# Ziel: Verwende den Datensatz Iris und entwickle einen Distplot,
# der die Länge der Petals (Kronenblätter) vergleicht.
# Datei: '../data/iris.csv'
# Felder: 'sepal_length','sepal_width','petal_length','petal_width','class'
# Klassen: 'Iris-setosa','Iris-versicolor','Iris-virginica'
######

# Führe hier die Importe aus:
import plotly.offline as pyo
import plotly.figure_factory as ff
import pandas as pd

# Erzeuge ein DataFrame aus der .csv-Datei:
df = pd.read_csv('../DATA/iris.csv')

# Definiere die Traces (Linien)
trace0 = df[df['class']=='Iris-setosa']['petal_length']
trace1 = df[df['class']=='Iris-versicolor']['petal_length']
trace2 = df[df['class']=='Iris-virginica']['petal_length']

# Erzeuge eine Variable data:
hist_data = [trace0, trace1, trace2]
group_labels = ['Iris Setosa','Iris Versicolor','Iris Virginica']

# Erzeuge eine fig mit data & layout und plotte die fig
fig = ff.create_distplot(hist_data, group_labels)
pyo.plot(fig, filename='solution7.html')

########
# Grossartig! Dies zeigt, dass eine Blume mit einer Petal-Länge
# zwischen 1-2cm fast immer eine Iris Setosa ist!
######
