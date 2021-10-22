#######
# Heatmaps für Sitka, Alaska,
# Santa Barbara, California and Yuma, Arizona Seite-an-Seite
# mit einer gemeinsamen Temperaturskala.
######
import plotly.offline as pyo
import plotly.graph_objs as go
from plotly import tools
import pandas as pd

df1 = pd.read_csv('../DATA/2010SitkaAK.csv')
df2 = pd.read_csv('../DATA/2010SantaBarbaraCA.csv')
df3 = pd.read_csv('../DATA/2010YumaAZ.csv')

trace1 = go.Heatmap(
    x=df1['DAY'],
    y=df1['LST_TIME'],
    z=df1['T_HR_AVG'],
    colorscale='Jet',
    zmin = 5, zmax = 40 # FÃ¼ge max/min-Farbwerte hinzu und mache jeden Plot konsistent
)
trace2 = go.Heatmap(
    x=df2['DAY'],
    y=df2['LST_TIME'],
    z=df2['T_HR_AVG'],
    colorscale='Jet',
    zmin = 5, zmax = 40
)
trace3 = go.Heatmap(
    x=df3['DAY'],
    y=df3['LST_TIME'],
    z=df3['T_HR_AVG'],
    colorscale='Jet',
    zmin = 5, zmax = 40
)

fig = tools.make_subplots(rows=1, cols=3,
    subplot_titles=('Sitka, AK','Santa Barbara, CA', 'Yuma, AZ'),
    shared_yaxes = True,  # Dies zeigt die Stunden nur auf der linken Seite an
)
fig.append_trace(trace1, 1, 1)
fig.append_trace(trace2, 1, 2)
fig.append_trace(trace3, 1, 3)

fig['layout'].update(      # Greife direkt auf das Layout zu!
    title='Hourly Temperatures, June 1-7, 2010'
)
pyo.plot(fig, filename='AllThree.html')
