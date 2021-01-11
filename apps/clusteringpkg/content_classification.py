import pathlib

import dash_html_components as html
from app import app
import pandas as pd
import plotly.graph_objects as go
import dash_core_components as dcc
import plotly.express as px


PATH = pathlib.Path(__file__).parent

# Server path
# DATA_PATH = PATH.joinpath("/home/datascienceLABB/mysite/data").resolve()
# Local path
DATA_PATH = PATH.joinpath("../../data").resolve()

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

#CODE METHODE 2 SUITE 1 GRAPHE
models_tune = ['Linear SVC', 'Perceptron','Logistic Regression']
best_scores = [0.8560729166655283, 0.881930188644105, 0.8865822950090629]
result = pd.DataFrame({'model tune':models_tune, 'best score balanced accuracy': best_scores})

fig43 = go.Figure(data=[
    go.Bar(name='training accuracy', x=result['model tune'].to_numpy(), y=result['best score balanced accuracy'].to_numpy()),
          ])
# Change the bar mode
fig43.update_layout(barmode='group')

CENTERED_STYLE = {
      "padding": "100px 300px 50px "
}
model = ["linearsvc", "Perceptron"]
training_accuracy = [0.9543111111111111, 0.9852888888888889]
validation_accuracy = [0.8906666666666667, 0.9209333333333334]
balanced_validation_accuracy = [0.9014301867980647, 0.8464531194881911]

###### Graph 4
model = ["Perceptron","LinearSVC"]
result_accuracy = [0.9456,0.9165]
balanced_accuracy = [0.870608,0.907227]

fig44 = go.Figure(data=[
    go.Bar(name='final test accuracy', x=model, y=result_accuracy),
    go.Bar(name='balanced final test accuracy', x=model, y=balanced_accuracy)
          ])
# Change the bar mode
fig44.update_layout(barmode='group')

######

fig45 = go.Figure(data=[
    go.Bar(name='training accuracy', x=model, y=training_accuracy),
    go.Bar(name='validation accuracy', x=model, y=validation_accuracy),
    go.Bar(name='balanced validation accuracy', x=model, y=balanced_validation_accuracy)
          ])
# Change the bar mode
fig45.update_layout(barmode='group')

###### Graph 6

model = ["Perceptron","LinearSVC"]
training_time = [91.754978 ,102.687572]
predict_time = [23.323546,25.757968]

fig46 = go.Figure(data=[
    go.Bar(name='training time', x=model, y=training_time),
    go.Bar(name='predict time', x=model, y=predict_time)
          ])
# Change the bar mode
fig46.update_layout(barmode='group')

layout = html.Div([
    html.H1('III - Classification par contenu', style={"textAlign": "center"}),
    html.Br(),
    html.H2("Entraînement des modèles", style={"textAlign": "center"}),
    dcc.Graph(id='fig41', figure=fig41),
    html.Br(),
    html.H2("Cross-validation", style={"textAlign": "center"}),
    dcc.Graph(id='fig42', figure=fig42),
    html.Br(),
    html.H2("Fine tuning", style={"textAlign": "center"}),
    dcc.Graph(id='fig43', figure=fig43),
    html.Br(),
    html.H2("Nouveau test sur le validation set", style={"textAlign": "center"}),
    dcc.Graph(id='fig44', figure=fig44),
    html.Br(),
    html.H2("Resultat de précision sur le test final", style={"textAlign": "center"}),
    dcc.Graph(id='fig45', figure=fig45),
    html.Br(),
    html.H2("Mesure du temps d'entraînement et de prédiction", style={"textAlign": "center"}),
    dcc.Graph(id='fig46', figure=fig46),
    html.Br(),

],style=CENTERED_STYLE)

