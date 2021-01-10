import pathlib
import pandas as pd
import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Connect to main app.py file
from app import app

# Connect to your app pages

# get relative data folder
# PATH = pathlib.Path(__file__).parent
# DATA_PATH = PATH.joinpath("../datasets").resolve()
#
# data = pd.read_csv(DATA_PATH.joinpath("mail_clean.csv"))
#
# df = data
#
# # figure 2
# fig2 = px.box(df[df['content_char_len'] < 5000], x="Years", y="content_char_len")

CENTERED_STYLE = {
      "padding": "100px 300px 50px "
}

layout = html.Div([

    html.H1('EDA', style={"textAlign": "center"}),
    html.H2('Exploratory data analysis - analyse exploratoire'),
    html.P("Dans cette étape nous explorons les données que nous avons nettoyées préalablement. C'est une étape très "
           "importante puisqu'elle nous permet d'explorer et de mieux comprendre les données que nous traitons. Même "
           "si tous les élements présentés ne seront pas forcément exploités elle nous permet de mieux appréhender "
           "les données."),
    html.Br(),
    html.P("L'exploration se divise en 3 axes:"),
    html.B("A - Temporalité (jours, années, mois, heures)"), html.Br(),
    html.B("B - Expéditeur"), html.Br(),
    html.B("C - Longueur du contenu"),
    # dcc.Graph(id='fig2', figure=fig2),
    # html.Div(id='eda-content', children=[]),
], style=CENTERED_STYLE)
