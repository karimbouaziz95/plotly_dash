import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv(r"C:\Users\NajahKarimBouaziz\Desktop\Neuer Ordner\Plotly-Dashboards-mit-Dash-v2_00\Plotly-Dashboards-mit-Dash-v2_00\DATA\nst-est2017-alldata.csv")

df2 = df[df["DIVISION"] == "1"]

df2.set_index("NAME", inplace=True)

df2 = df2[[col for col in df2.columns if col.startswith("POP")]] 

print(df)
print(df2)
print(df2.columns)

traces = [go.Scatter(
        x = df2.columns,
        y = df2.loc[name],
        mode = "markers+lines",
        name = name
    ) for name in df2.index]

layout = go.Layout(title = "Population")
fig = go.Figure(data=traces, layout=layout)


pyo.plot(fig)