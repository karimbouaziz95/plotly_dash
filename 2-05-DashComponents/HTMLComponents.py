#######
# Hier werden Dash HTML Components beispielhaft vorgestellt.
# Ergänze die Beispiele um Komponenten, die du nützlich findest.
######
import dash
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([
    'This is the outermost Div',
    html.Div(
        'This is an inner Div',
        style={'color':'blue', 'border':'2px blue solid', 'borderRadius':5,
        'padding':10, 'width':220}
    ),
    html.Div(
        'This is another inner Div',
        style={'color':'green', 'border':'2px green solid',
        'margin':10, 'width':220}
    ),
],
# CSS-Layout für das äusserste Div:
style={'width':500, 'height':200, 'color':'red', 'border':'2px red dotted'})

if __name__ == '__main__':
    app.run_server()
