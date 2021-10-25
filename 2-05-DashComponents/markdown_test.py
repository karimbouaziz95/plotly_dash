import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

markdown_text = """
## NBA and Basketball

The [NBA] (https://de.wikipedia.org/wiki/National_Basketball_Association) is the American Basketball Association
It is the most known basketball league in the world 
and it is very entertaining.

Many thinks that the best player in the league is [Lebron James] (https://en.wikipedia.org/wiki/LeBron_James), but 
i actually think that [Steph Curry] (https://en.wikipedia.org/wiki/Stephen_Curry) is taking the game to another level

"""

app.layout = html.Div(
    [
        dcc.Markdown(children=markdown_text)
    ]
)

if __name__ == "__main__":
    app.run_server()