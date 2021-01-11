import pathlib

import dash_html_components as html
from app import app
import pandas as pd
import plotly.graph_objects as go
import dash_core_components as dcc
import plotly.express as px

# CODE METHODE 1 GRAPHE 1
models = ['DecisionTreeClassifier', 'RandomForestClassifier', 'Logistic Regression',
          'KNearestNeighbours', 'Perceptron', 'Adaboost with DecisionTree', 'Xgboost', "Mlp sequential"]

training = [0.98977, 0.990367, 0.574836, 0.933622, 0.363054, 0.989741, 0.699779, 0.994259]

valid = [0.939947, 0.945953, 0.579882, 0.852496, 0.364819, 0.945828, 0.696985, 0.997373]

valid_balanced = [0.920562, 0.90041, 0.515173, 0.854414, 0.491715, 0.913971, 0.639803, 0.982797]

result = pd.DataFrame({'model': models, 'training': training, 'valid': valid, 'valid_balanced': valid_balanced})

fig51 = go.Figure(data=[
    go.Bar(name='training accuracy', x=result['model'].to_numpy(), y=result['training'].to_numpy()),
    go.Bar(name='validation accuracy', x=result['model'].to_numpy(), y=result['valid'].to_numpy()),
    go.Bar(name='balanced validation accuracy', x=result['model'].to_numpy(), y=result['valid_balanced'].to_numpy())
])
# Change the bar mode
fig51.update_layout(barmode='group')

# CODE METHODE 1 GRAPHE 2
models = ['RandomForestClassifier', 'KnearestNeighbours', 'Adaboost', 'DecisionTreeClassifier']

bal_acc_mean = [0.89076, 0.829622, 0.895015, 0.891846]
bal_acc_std = [0.010425, 0.010966, 0.012215, 0.012985]

result = pd.DataFrame({'model': models, 'acc_mean': bal_acc_mean, 'acc_std': bal_acc_std})

fig52 = go.Figure(data=[
    go.Bar(name='balanced accuracy mean', x=result['model'].to_numpy(), y=result['acc_mean'].to_numpy()),
    go.Bar(name='balanced accuracy std', x=result['model'].to_numpy(), y=result['acc_std'].to_numpy()),

])
# Change the bar mode
fig52.update_layout(barmode='group')

# CODE METHODE 1 GRAPHE 3
models = ['RandomForestClassifier', 'DecisionTreeClassifier', 'Adaboost', 'KnearestNeighbours']

best_score = [0.828210, 0.705494, 0.927511, 0.876437]

result = pd.DataFrame({'model': models, 'best score': best_score})

fig53 = go.Figure(data=[
    go.Bar(name='best balanced accuracy', x=result['model'].to_numpy(), y=result['best score'].to_numpy()),

])
# Change the bar mode
fig53.update_layout(barmode='group')

# CODE METHODE 1 GRAPHE 4
models = ['Voting', 'KNN', 'RandomForest']

acc_train = [0.986155, 0.985654, 0.911200]
acc_valid = [0.934192, 0.928813, 0.867634]
acc_balanced = [0.882852, 0.840607, 0.850187]

result = pd.DataFrame({'model': models, 'acc_train': acc_train, 'acc valid': acc_valid, 'acc balanced': acc_balanced})

fig54 = go.Figure(data=[
    go.Bar(name='training accuracy', x=result['model'].to_numpy(), y=result['acc_train'].to_numpy()),
    go.Bar(name='validation accuracy', x=result['model'].to_numpy(), y=result['acc valid'].to_numpy()),
    go.Bar(name='balanced validation accuracy', x=result['model'].to_numpy(), y=result['acc balanced'].to_numpy())

])
# Change the bar mode
fig54.update_layout(barmode='group')

# CODE METHODE 1 GRAPHE 5
models = ['Adaboost', 'VotingClassifier', 'Sequential MLP']

acc_train = [0.997442, 0.987489, 0.99555165]
acc_valid = [0.981859, 0.934818, 0.997122]
acc_balanced = [0.971922, 0.889968, 0.997898]

result = pd.DataFrame({'model': models, 'acc_train': acc_train, 'acc valid': acc_valid, 'acc balanced': acc_balanced})

fig55 = go.Figure(data=[
    go.Bar(name='training accuracy', x=result['model'].to_numpy(), y=result['acc_train'].to_numpy()),
    go.Bar(name='validation accuracy', x=result['model'].to_numpy(), y=result['acc valid'].to_numpy()),
    go.Bar(name='balanced validation accuracy', x=result['model'].to_numpy(), y=result['acc balanced'].to_numpy())

])
# Change the bar mode
fig55.update_layout(barmode='group')

# CODE METHODE 1 GRAPHE 6
models = ['Adaboost', 'Sequential MLP']

acc = [0.983336, 0.998649]
bal_acc = [0.983078, 0.999349]

result = pd.DataFrame({'model': models, 'acc': acc, 'acc bal': bal_acc})

fig56 = go.Figure(data=[
    go.Bar(name='accuracy', x=result['model'].to_numpy(), y=result['acc'].to_numpy()),
    go.Bar(name='balanced accuracy', x=result['model'].to_numpy(), y=result['acc bal'].to_numpy()),

])
# Change the bar mode
fig56.update_layout(barmode='group')

#CODE METHODE 1 GRAPHE 6 (dernier)
models = ['Adaboost', 'Sequential MLP']

train_time = [13.086756, 559.519064]
pred_time = [0.799937, 1.230662]

result = pd.DataFrame({'model': models, 'train': train_time, 'pred': pred_time})

fig57 = go.Figure(data=[
    go.Bar(name='Training Time', x=result['model'].to_numpy(), y=result['train'].to_numpy()),
    go.Bar(name='Predict Time', x=result['model'].to_numpy(), y=result['pred'].to_numpy()),

])
# Change the bar mode
fig57.update_layout(barmode='group')

CENTERED_STYLE = {
    "padding": "100px 300px 50px "
}

layout = html.Div([
    html.H1('II - Classification par attribut', style={"textAlign": "center"}),
    html.Br(),
    html.H2("Entraînement des modèles", style={"textAlign": "center"}),
    dcc.Graph(id='fig51', figure=fig51),
    html.P("Le MLP Sequential classifier, le DecisionTreeClassifier, le RandomForestClassifier et Adaboost semblent "
           "être les plus performants et ce à tout niveau. Ils sont peut être même trop performants. Pour bien "
           "choisir notre modèle, nous devons vérifier qu'il ne tend pas à l'over fitting ou à l'under fitting. Les "
           "balanced score sont bon, cela veut dire qu'il y a une bonne classification au sein même des classes. Si "
           "nous n'avions pas utilisé de méthodes de resampling, cela aurait pu être désastreux. Les modèles "
           "Perceptron, Logistic Regression et Xgboost sont très peu performants comparés aux autres, nous les avons "
           "donc laissés de côté pour la suite du processus. On peut noter que les modèles linéaires ont l’air d’être "
           "peu performant sur notre jeu de données."),
    html.Br(),
    html.H2("Cross-validation", style={"textAlign": "center"}),
    dcc.Graph(id='fig52', figure=fig52),
    html.P(
        "Ces résultats témoignent d’une bonne performance de précision au sein même des classes. Cependant, on observe "
        "que le modèle KNN est pour l’instant en dessous des trois autres modèles."),
    html.Br(),
    html.H2("Paramétrage", style={"textAlign": "center"}),
    dcc.Graph(id='fig53', figure=fig53),
    html.P(
        "Pour régler le problème d’overfitting, nous avons imposé plusieurs paramètres à certains de nos modèles, "
        "comme la profondeur maximale pour les Decision Tree et Random Forest. Malheureusement ces derniers ont de "
        "moins bons scores qu'auparavant, nous pourrions leur laisser plus de liberté quant à leurs paramètres mais "
        "nous préférons privilégier la fiabilité. Par conséquent, nous avons choisi d’éliminer le moins bon d’entre "
        "eux : le Decision Tree Classifier. Mis à part le MLP Sequential, on constate qu’Adaboost est en tête, "
        "devant  les KNN et le Random Forest Classifier. Cependant, les scores de ces derniers restent plutôt bons. "
        "C’est pourquoi nous avons pensé à utiliser une méthode de bagging dont le but est de les rassembler afin "
        "qu’ils ne forment plus qu’un modèle dont les performances pourraient dépasser celles des deux modèles "
        "séparément."),
    html.Br(),
    html.H2("Bagging", style={"textAlign": "center"}),
    dcc.Graph(id='fig54', figure=fig54),
    html.P(
        "Effectivement, ce fut une bonne idée de les réunir au sein d’un Voting Classifier, ensemble ils semblent "
        "être plus performant."),
    html.Br(),
    html.H2("Nouveau test sur le validation set", style={"textAlign": "center"}),
    dcc.Graph(id='fig55', figure=fig55),
    html.Br(),
    html.H2("Resultat de précision sur le test final", style={"textAlign": "center"}),
    dcc.Graph(id='fig56', figure=fig56),
    html.Br(),
    html.H2("Mesure du temps d'entraînement et de prediction", style={"textAlign": "center"}),
    dcc.Graph(id='fig57', figure=fig57),
], style=CENTERED_STYLE)
