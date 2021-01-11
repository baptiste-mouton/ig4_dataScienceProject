import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from apps import *

# Connect to main app.py file
from app import app

import dash_bootstrap_components as dbc
from apps import eda
# Connect to your app pages
from apps.edapkg.categorical_features import temporalite, expediteur, categorie
from apps.edapkg.continuous_features import continuous
from apps.clusteringpkg import content_classification, attribute_classification
import pandas as pd

# link fontawesome to get the chevron icons
FA = "https://use.fontawesome.com/releases/v5.8.1/css/all.css"

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP, FA])

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "20rem",
    "padding": "2rem 1rem",
    "background-color": "#BDCFB8",
    "font": "bold 14px Arial",
    "text-decoration": "none",
    "color": "#333333",
    "border-top": "1px solid #CCCCCC",
    "border-right": "1px solid #333333",
    "border-bottom": "1px solid #333333",
    "border-left": "1px solid #CCCCCC"
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

submenu_0 = [
    html.Li(
        # use Row and Col components to position the chevrons
        dbc.Row(
            [
                dbc.NavLink("Accueil", href="/"),
            ],
            className="my-1",
        ),
        style={"cursor": "pointer", "padding-left": "5px"},
        id="submenu-0",
    ),
]

submenu_1 = [
    html.Li(
        # use Row and Col components to position the chevrons
        dbc.Row(
            [
                dbc.Col("I - EDA"),
                dbc.Col(
                    html.I(className="fas fa-chevron-right mr-3"), width="auto"
                ),
            ],
            className="my-1",
        ),
        style={"cursor": "pointer"},
        id="submenu-1",
    ),
    # we use the Collapse component to hide and reveal the navigation links
    dbc.Collapse(
        [
            dbc.NavLink("Description", href="/eda"),
            dbc.NavLink("A - Temporalité", href="/eda/temporalite"),
            dbc.NavLink("B - Expéditeur", href="/eda/expediteur"),
            dbc.NavLink("C - Contenu", href="/eda/contenu"),
        ],
        id="submenu-1-collapse",
    ),
]

submenu_2 = [
    html.Li(
        dbc.Row(
            [
                dbc.Col("II - Classification par attribut"),
                dbc.Col(
                    html.I(className="fas fa-chevron-right mr-3"), width="auto"
                ),
            ],
            className="my-1",
        ),
        style={"cursor": "pointer"},
        id="submenu-2",
    ),
    dbc.Collapse(
        [
            dbc.NavLink("Analyse", href="/classification/classification_attribut"),
        ],
        id="submenu-2-collapse",
    ),
]

submenu_3 = [
    html.Li(
        dbc.Row(
            [
                dbc.Col("III - Classification par contenu"),
                dbc.Col(
                    html.I(className="fas fa-chevron-right mr-3"), width="auto"
                ),
            ],
            className="my-1",
        ),
        style={"cursor": "pointer"},
        id="submenu-3",
    ),
    dbc.Collapse(
        [
            dbc.NavLink("Analyse", href="/classification/classification_contenu"),
        ],
        id="submenu-3-collapse",
    ),
]

sidebar = html.Div(
    [
        html.H2("Axes", className="display-4"),
        html.Hr(),
        html.P(
            "Naviguez à travers les différents axes de notre projet", className="lead"
        ),
        dbc.Nav(submenu_0 + submenu_1 + submenu_2 + submenu_3, vertical=True),
    ],
    style=SIDEBAR_STYLE,
    id="sidebar",
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


# this function is used to toggle the is_open property of each Collapse
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


# this function applies the "open" class to rotate the chevron
def set_navitem_class(is_open):
    if is_open:
        return "open"
    return ""


for i in [1, 2, 3, 4]:
    app.callback(
        Output(f"submenu-{i}-collapse", "is_open"),
        [Input(f"submenu-{i}", "n_clicks")],
        [State(f"submenu-{i}-collapse", "is_open")],
    )(toggle_collapse)

    app.callback(
        Output(f"submenu-{i}", "className"),
        [Input(f"submenu-{i}-collapse", "is_open")],
    )(set_navitem_class)


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return dbc.Jumbotron(
            [
                html.H1("Projet Data Science : Classification des mails"),
                html.Img(src=app.get_asset_url('EnronLogo.png'), style={'height': '7%', 'width': '7%'}),
                html.H3("I. Présentation du projet"),
                html.P(
                    "Dans le cadre de notre projet data-science en IG4, nous avons choisi de travailler sur le thème "
                    "1 : “Analyse de mails, sur données de test en vue de l’application à des données réelles du "
                    "projet HUT” et sur le sujet 3 : “Classification de mails”."),
                html.P(
                    "Nous avons fait ce choix car il nous semblait très intéressant de mettre en pratique ce que l’on "
                    "avait appris lors de ce semestre sur ce type de données, de plus, l’intitulé du sujet nous "
                    "laissait une marge de liberté assez large pour l’aborder de la manière dont on le souhaitait."),
                html.P(
                    "Les données Enron, sur lesquelles notre analyse porte, comportent une centaine de milliers de "
                    "mails provenant de l’entreprise américaine Enron. Enron était une entreprise américaine des "
                    "secteurs de l’énergie (gaz naturel) et du courtage (achat et revente d’électricité)."),
                html.P(
                    "À son apogée, elle était l’une des plus grandes entreprises américaines de son époque de par sa "
                    "capitalisation boursière. La société Enron fait faillite en décembre 2001 à la suite de fraudes "
                    "comptables."),
                html.P(
                    "Une des principales difficultés à laquelle nous avons été confrontés était d’arriver à orienter "
                    "notre étude : comme dit ci-dessus, le sujet est relativement ouvert et nous avions par "
                    "conséquent de nombreuses possibilités. Nous avons donc passé beaucoup de temps à nettoyer et à "
                    "analyser les données afin de déterminer quels axes d’études il serait pertinent d’explorer."),
                html.Br(),  # Saut de ligne

                html.H3("II. Présentation des membres du groupe"),
                html.P(
                    "Nous sommes un groupe d'étudiants en 4ème année à Polytech Montpellier. Le groupe est composé "
                    "d'Ayoub MOUJANE, Baptiste MOUTON, Birane BA et de Lucas GONTHIER."),

                html.Img(src=app.get_asset_url('ay.png'), style={'height': '7%', 'width': '7%'}),
                html.Img(src=app.get_asset_url('bt.png'), style={'height': '7%', 'width': '7%'}),
                html.Img(src=app.get_asset_url('bi.png'), style={'height': '7%', 'width': '7%'}),
                html.Img(src=app.get_asset_url('lcs.png'), style={'height': '7%', 'width': '7%'})

            ]
        )
    elif pathname == "/eda":
        return eda.layout
    elif pathname == "/eda/temporalite":
        return temporalite.layout
    elif pathname == "/eda/categorie":
        return categorie.layout
    elif pathname == "/eda/expediteur":
        return expediteur.layout
    elif pathname == "/eda/contenu":
        return continuous.layout
    elif pathname == "/classification/classification_contenu":
        return content_classification.layout
    elif pathname == "/classification/classification_attribut":
        return attribute_classification.layout
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )

if __name__ == '__main__':
    app.run_server(debug=False)
