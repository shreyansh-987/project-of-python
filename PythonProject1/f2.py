from dash import Dash, dcc, html, Output, Input
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])

server = app.server

app.layout = dbc.Container([
    dcc.Input(
        id='my_text',
        value='Type Text new now'
    ),
    dcc.Markdown(
        id='my_output',
        children=''
    ),
])

@app.callback(
    Output(component_id='my_output', component_property='children'),
    Input(component_id='my_text', component_property='value')
)
def update_text(el_text):
    return el_text

if __name__ == '__main__':
    app.run(debug=True)