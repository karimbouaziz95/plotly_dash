import plotly.offline as pyo
import plotly.graph_objs as go

y = [1,14,14,15,16,18,18,19,19,20,20,23,24,26,27,27,28,29,33,54]

snodgrass = [.209,.205,.196,.210,.202,.207,.224,.223,.220,.201]
twain = [.225,.262,.217,.240,.230,.229,.235,.217]

data0 = [go.Box(
        y=y,
        boxpoints = "outliers",
        jitter=0,
        pointpos = 0
       
    )]

data = [go.Box(
        y = snodgrass,
        name = "snodgrass"
    ),
        go.Box(
        y = twain,
        name ="MT"
    )
    ]

layout = go.Layout(
    title = 'Comparison of three-letter-word frequencies<br>\
    between Quintus Curtius Snodgrass and Mark Twain'
)
fig = go.Figure(data=data, layout=layout)

pyo.plot(fig)