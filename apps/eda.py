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
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()

data = pd.read_csv(DATA_PATH.joinpath("mail_clean.csv"))

df = data

# figure 2
fig2 = px.box(df[df['content_char_len'] < 5000], x="Years", y="content_char_len")

# figure 8
# unreadable


layout = html.Div([

    html.H1('EDA ', style={"textAlign": "center"}),
    dcc.Graph(id='fig2', figure=fig2),
    html.Div([
        dcc.Link('temporalite|', href='/apps/eda/temporalite'),
        dcc.Link('expediteur|', href='/apps/eda/expediteur'),
        dcc.Link('categorie|', href='/apps/eda/categorie'),
        dcc.Link('continuous', href='/apps/eda/continuous'),
    ], className="row"),
    html.Div(id='eda-content', children=[])

])


