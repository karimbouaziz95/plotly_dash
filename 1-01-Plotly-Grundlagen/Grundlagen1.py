#######
# Dieses Script erzeugt einen statischen Plot mit Matplotlib
######
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Erzeuge Pseudodaten
df = pd.DataFrame(np.random.randn(100,4),columns='A B C D'.split())
df.plot()
plt.show()
print(df)
#######
# Führe im Terminal aus:  python basic1.py
# Schliesse das Fenster des Plots, um das Script zu beenden
######
