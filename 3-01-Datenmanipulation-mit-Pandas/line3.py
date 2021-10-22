#######
# Dieses Liniendiagramm verwendet Pandas, um den U.S. Census Bureau
# Datensatz auf lediglich die sechs New England-Staaten zu begrenzen.
######
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# Lese eine .csv-Datei in einen Pandas DataFrame:
df = pd.read_csv('../DATA/nst-est2017-alldata.csv')
# Nimm nur die sechs New England-Staaten
df2 = df[df['DIVISION']=='1']
# Setze den Index auf den Namen der Staaten
df2.set_index('NAME', inplace=True)
# Nimm nur die Spalte mit der Bevölkerungsstatistik
df2 = df2[[col for col in df2.columns if col.startswith('POP')]]

# Übergib die Daten direkt an pyo.plot 
# (verwende eine List Comprehension, um Linien zu bauen)
pyo.plot([go.Scatter(
    x = df2.columns,
    y = df2.loc[name],
    mode = 'markers+lines',
    name = name
) for name in df2.index], filename='line3.html')
