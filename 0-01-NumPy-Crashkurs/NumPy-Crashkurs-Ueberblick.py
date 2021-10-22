############################
### Numpy Crashkurs #####
############################
import numpy as np

my_list = [0,1,2,3,4]

arr = np.array(my_list)

print(arr)


# arange Integers (Ganzzahlen), nimmt start,stop, und Schrittgrösse an

a = np.arange(0,10)
print(a)

a= np.arange(0,10,2)
print(a)

# Erzeuge ein Array von Nullen

a = np.zeros((5,5))
print(a)

# Erzeuge ein Array von Einsen

a = np.ones((2,4))
print(a)

# Erzeuge ein Array zufälliger Integers (gleichverteilt zwischen den Grenzen)

a = np.random.randint(0,10)
print(a)

# Erzeuge eine 2D-Matrix zufälliger Integers

a = np.random.randint(0,10,(3,3))
print(a)

# Erzeuge ein Array mit linearen Abständen
a = np.linspace(0,10,6)
print(a)


a = np.linspace(0,10,101)
print(a)

################################
#### Numpy Operationen #########
##############################

# Das Setzen eines Seeds (Startwerts) erlaubt es dir, die gleichen "Zufallszahlen" wie wir zu erhalten
# Das ist sehr schön zum testen, damit die Ergebnisse verglichen werden können
np.random.seed(101) # Betrachte das Video für Einzelheiten
arr = np.random.randint(0,100,10)
print(arr)
# Wenn du dies wieder aufrufst, wirst du einen anderen Satz zufälliger Integers erhalten
# als bei deinem ersten Aufruf. Jedoch werden beide Sätze dieselben sein, wie wenn
# jemand anders die beiden Aufrufe durchführt, der den gleichen Seed gesetzt hat.
arr2 = np.random.randint(0,100,10)
print(arr2)


# Einfache Operationen

print(arr.max())

print(arr.min())

print(arr.mean())

# Der Index des Minimums
print(arr.argmin())

print(arr.argmax())

print(arr.reshape(2,5))

########################
#### Indizierung ############
########################

# Du kannst .reshape() verwenden, um die Form eines 1D-Arrays in 2D, 3D, etc. zu konvertieren.
# Beachte dabei, dass wir hauptsächlich mit Tabellendaten in 2D arbeiten werden.
mat = np.arange(0,100).reshape(10,10)
print(mat)

row = 0
col = 1

# Eine  individuelle Nummer auswählen:
print(mat[row,col])

# Wähle eine ganze Spalte (alle Zeilenwerte der Spalte "col")
print(mat[:,col])

# Wähle eine ganze Zeile (alle Spaltenwerte der Zeile "col")
print(mat[row,:])


#######################
##### Masking (Maskierung) ####
#######################
# Maskierung erlaubt dir die Verwendung bedingter Filter, um Elemente auszulesen
# Wir werden die Anwendung dieser Idee in Pandas betrachten

print(mat > 50)


print(mat[mat>50])


# Das ist alles für NumPy! NumPy ist eine wirklich grosse Bibliothek, die weitaus
# mehr tut, als wir hier zeigen können. Für unsere Anwendungsfälle in der Visualisierung
# sind das aber alle von uns benötigten Grundlagen. Wir werden später weitere
# Konzepte von Numpy vorstellen.
