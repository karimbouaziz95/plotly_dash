##################################################################
####### Crash Course Übungen
#########################################################

#########################################################
# Vervollständige die folgenden, nummerierten Aufgaben.
# Wirf einen Blick in das Lösungsvideo bei Schwierigkeiten!
#######################################################

#######
# AUFGABE 1: Importiere Pandas und NumPy
######
import numpy as np
import pandas as pd


#######
# AUFGABE 2: Setze NumPy's Zufallszahlengenerator auf den Seed 101
######
np.random.seed(101)

#######
# AUFGABE 3: Erzeuge eine NumPy-Matrix mit 100 Zeilen und 5 Spalten bestehend
#                     aus zufälligen Integers zwischen 1 und 100. (Beachte hierbei,
#                     dass die obere Grenze exklusive sein kann).
######
mat = np.random.randint(1,100,(100,5))
print(mat)

#######
# AUFGABE 4: Verwende jetzt pd.DataFrame() um diesen NumPy-Array als DataFrame einzulesen.
#                     übergib dazu einfach das NumPy-Array in die Funktion pd.DataFrame, um ein
#                     DataFrame zu erhalten. Pandas kennzeichnet die Spalten automatisch mit 0-4
######

df = pd.DataFrame(data = mat)
print(df)
#######
# AUFGABE 5: Verwende mit dem von dir gerade erzeugten Dataframe [df.columns = [...]]
#                    (https://stackoverflow.com/questions/11346283/renaming-columns-in-pandas)
#                    um die Spalten in Pandas umzubennen in ['f1','f2','f3','f4','label'].
######

df.columns = ["f1", "f2", "f3", "f4", "label"]
print(df)

#######
# AUFGABE 6: Bisher waren die Aufgaben hoffentlich einfach zu lösen..
#         In dieser letzten Aufgabe wird dir erlauben, schnell zu sehen, ob du in
#         Pandas auf dem richtigen Level stehst! Mache das folgende:
#         Erzeuge ein DataFrame mit den Spalten ['A','B','C','D'], bei dem jede Spalte
#         50 Zeilen mit Zufallszahlen besitzt. Die Zufallszahlen sollen
#         zwischen 0 und 100 liegen. (Hinweis: Verwende NumPy, um die Zahlen zu erzeugen
#         und übergebe sie dann pd.DataFrame(), beachte hierbei die Parameter 
#         für diesen Aufruf.)
######

dff = pd.DataFrame(data = np.random.randint(0,100,(50,4)), columns="A B C D".split())
print(dff)






