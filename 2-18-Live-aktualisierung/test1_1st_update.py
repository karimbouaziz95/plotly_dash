import dash
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash()

crash_free = 0


def update_layout():
    global crash_free
    crash_free += 1
    return html.H1("Crash free for {} .th time after refreshing".format(crash_free))


app.layout = update_layout

if __name__ == "__main__":
    app.run_server()
