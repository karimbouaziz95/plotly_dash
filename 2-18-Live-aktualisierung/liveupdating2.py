#######
# Dieses Script macht regelmässig API-Aufrufe auf http://data-live.flightradar24.com
# um die gesamten, weltweiten, aktualisierten Flugdaten zu erhalten.
# ** Diese Version aktualisiert die weltweite Anzahl von Flügen kontinuierlich.**
######
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import requests

app = dash.Dash()

app.layout = html.Div([
    html.Div([
        html.Iframe(src = 'https://www.flightradar24.com', height = 500, width = 1200)
    ]),

    html.Div([
    html.Pre(
        id='counter_text',
        children='Active flights worldwide:'
    ),
    dcc.Interval(
        id='interval-component',
        interval=6000, # 6000 Millisekunden = 6 Sekunden
        n_intervals=0
    )])
])

@app.callback(Output('counter_text', 'children'),
              [Input('interval-component', 'n_intervals')])
def update_layout(n):
    url = "https://data-live.flightradar24.com/zones/fcgi/feed.js?faa=1\
           &mlat=1&flarm=1&adsb=1&gnd=1&air=1&vehicles=1&estimated=1&stats=1"
    # Ein falscher Header ist nötig, um auf die Seite zuzugreifen:
    res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    data = res.json()
    counter = 0
    for element in data["stats"]["total"]:
        counter += data["stats"]["total"][element]
    return 'Active flights worldwide: {}'.format(counter)

if __name__ == '__main__':
    app.run_server()
