#######
# Ziel: Baue ein Dashboard, dass OldFaithful.csv aus dem Verzeichnis
# DATA importiert und ein Streudiagramm (Scatterplot) anzeigt.
# Die Feldnamen sind:
# 'D' = Datum der Aufzeichnungen im Monat (im August),
# 'X' = Dauer der derzeitigen Eruption in Minuten (gerundet auf 0.1 Minuten),
# 'Y' = Wartezeit bis zur nächsten Eruption in Minuten(gerundet auf die nächste Minute).
######

# Führe hier die Importe aus:
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go


# Führe die Anwendung aus:
app = dash.Dash()

# Erzeuge ein DataFrame aus der .csv-Datei:
df = pd.read_csv("DATA/OldFaithful.csv")
print(df)


# Erzeuge ein Dash Layout, dass eine Graph-Komponente enthält:
app.layout = html.Div(
    children=[
        dcc.Graph(
            id="once again aufgabe",
            figure={
                "data": [
                    go.Scatter(
                        x=df["X"],
                        y=df["Y"],
                        mode="markers"
                    )
                ],
                "layout": go.Layout(
                    title="once again aufgabe",
                    xaxis=dict(title="XXXXXXXX"),
                    yaxis=dict(title="YYYYYYYY"),
                    hovermode="closest"
                )
            }
        )
    ]
)


# Füge den Server-Abschnitt hinzu:
if __name__ == "__main__":
    app.run_server()
