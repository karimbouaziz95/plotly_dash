##########################
### Pandas Crashkurs ###########
##########################
# Wir werden in diesem Kurs Pandas mehr verwenden als NumPy,
# lasst uns daher einen schnellen Blick auf die wichtigsten Ideen von Pandas werfen!


import pandas as pd
import numpy as np


# CSV Dateien einlesen. Verwende den Befehl read_csv.
# Mehr Einzelheiten: https://pandas.pydata.org/pandas-docs/stable/io.html
df = pd.read_csv('../DATA/salaries.csv')

print(df)


# Du kannst Spalten mit eckigen Klammern auswählen:
print(df['Name'])


print(df['Salary'])


# Wähle multiple Spalten mit einer Liste von Spaltennamen.
# Da du eine Liste übergibst, werden doppelte eckige Klammern benötigt
print(df[['Name','Salary']])


# Vergleichbar mit NumPy kannst du min(), max(), mean(), etc. auf einem 
# Pandas DataFrame ausführen.
print(df['Age'].mean())


# Wie bei NumPy können wir konditionale Filter einsetzten, um Zeilen auszuwählen,
# die bestimmte Kriterien erfüllen, wie beispielsweise alle Zeilen mit Age (Alter) über 30
ser_of_bool = df['Age'] > 30
print(ser_of_bool)

# Verwende diesen Filter mit boolschen Werten, um Zeilen auszuwählen
age_filter = df['Age'] > 30

# Übergib diesen Filter dem DataFrame
print(df[age_filter])


# Das wird üblicherweise in einem Schritt erledigt:
df[df['Age'] > 30]


# Es gibt viele weitere Operationen, die du mit Pandas durchführen kannst!
# Vorerst werden wir jedoch nur ein paar weitere vorführen und den Rest 
# im weiteren Verlauf des Kurses vorstellen :)

df['Age'].unique() # Liste einzigartiger Werte für Age
df['Age'].nunique() # Anzahl einzigartiger Werte
df.info() # Allgemeine Informationen über deinen DataFrame
df.describe() # Statistiken zu deinem DataFrame
df.columns # Die Liste aller Spalten
df.index # Erzeuge eine Indexliste
# Du kannst eine NumPy-Matrix in einen DataFrame konvertieren mit:
mat = np.arange(50).reshape(5,10)
