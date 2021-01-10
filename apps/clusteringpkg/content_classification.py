import pathlib

import dash_html_components as html
from app import app
import pandas as pd
import plotly.graph_objects as go
import dash_core_components as dcc
import plotly.express as px


PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../../datasets").resolve()
result = pd.read_csv(DATA_PATH.joinpath("result_first_training.csv"))

fig41 = go.Figure(data=[
    go.Bar(name='training accuracy', x=result['model'].to_numpy(), y=result['training accuracy'].to_numpy()),
    go.Bar(name='validation accuracy', x=result['model'].to_numpy(), y=result['validation accuracy'].to_numpy()),
    go.Bar(name='balanced validation accuracy', x=result['model'].to_numpy(), y=result['validation balanced accuracy'].to_numpy())
          ])
# Change the bar mode
fig41.update_layout(barmode='group')

cv_df = pd.read_csv(DATA_PATH.joinpath("crossval_boxplot.csv"))
fig42 = px.box(cv_df, x="model_name", y="accuracy", points="all")

CENTERED_STYLE = {
      "padding": "100px 300px 50px "
}

layout = html.Div([
    html.H1('III - Classification par contenu', style={"textAlign": "center"}),
    dcc.Graph(id='fig41', figure=fig41),
    dcc.Graph(id='fig42', figure=fig42),

],style=CENTERED_STYLE)

