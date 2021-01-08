import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Connect to main app.py file
from app import app
from app import server

# Connect to your app pages
from apps import vgames, global_sales, eda
from apps.edapkg.categorical_features import temporalite, expediteur, categorie
from apps.edapkg.continuous_features import continuous



app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        dcc.Link('Video Games|', href='/apps/vgames'),
        dcc.Link('Other Products|', href='/apps/global_sales'),
        dcc.Link('Eda', href='/apps/eda'),
    ], className="row"),
    html.Div(id='page-content', children=[])
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/vgames':
        return vgames.layout
    if pathname == '/apps/global_sales':
        return global_sales.layout
    if pathname == '/apps/eda':
        return eda.layout
    if pathname == '/apps/eda/temporalite':
        return temporalite.layout
    if pathname == '/apps/eda/expediteur':
        return expediteur.layout
    if pathname == '/apps/eda/categorie':
        return categorie.layout
    if pathname == '/apps/eda/continuous':
        return continuous.layout


if __name__ == '__main__':
    app.run_server(debug=False)
