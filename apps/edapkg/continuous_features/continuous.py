import dash_html_components as html
import pandas as pd
import plotly.express as px
import pathlib
import dash_core_components as dcc

from apps.csv_import import data

df = data
df = df[~((df.Years == 1998) | (df.Years == 2004) | (df.Years == 2012) | (df.Years == 2020))]
df = df[~(df.Years == 1980)]

# figure 15

from sklearn import preprocessing

x = df[['content_char_len', 'To_count']].values

min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(x)
df_scaled = pd.DataFrame(x_scaled, columns=['content_char_len_scaled', 'To_count_scaled'])
df_scaled = pd.concat([df, df_scaled], axis=1, join='inner')

fig15 = px.scatter(df_scaled, x='content_char_len_scaled', y='To_count_scaled', color='Years', facet_col='DayWeek',
                   facet_col_wrap=3,
                   category_orders={'DayWeek': range(0, 7)})
# figure 16

fig16 = px.scatter(df_scaled, x='content_char_len_scaled', y='To_count_scaled', color='Years', facet_col='Hours',
                   facet_col_wrap=5,
                   category_orders={'Hours': range(0, 24)})

# figure 17

fig17 = px.scatter(df_scaled, x='content_char_len_scaled', y='To_count_scaled', color='Years', facet_col='Month',
                   facet_col_wrap=3,
                   category_orders={'Month': range(1, 13)})
# figure 18

fig18 = px.scatter(df_scaled, x='content_char_len_scaled', y='To_count_scaled', facet_col='Years', facet_col_wrap=3,
                   category_orders={'Years': range(1980, 2021)})

CENTERED_STYLE = {
    "padding": "100px 300px 50px "
}

layout = html.Div([
    html.H1('C - Contenu', style={"textAlign": "center"}),
    html.B(
        "Dans cette partie nous étudions la longueur des mails en fonctions des 4 contraintes temporelles (année,"
        "mois,jours du mois et jours de la semaine)"),
    dcc.Graph(id='fig15', figure=fig15),
    html.B("Les mails en weekend sont en général plus courts et concernent moins de personnes"),
    dcc.Graph(id='fig16', figure=fig16),
    html.B("Les mails envoyés durant la nuit, aussi sont en général plus courts et concernent moins de personnes"),
    dcc.Graph(id='fig17', figure=fig17),
    dcc.Graph(id='fig18', figure=fig18),
    html.B("Ces graphes représentant les nuages de points du nombre de destinataires normalisés en fonction de la "
           "longueur du contenu des mails suivant les différentes temporalités possibles nous montrent que le nombre "
           "de destinataires d'un mail et son nombre de caractères sont liés de la même manière quelque soit le type "
           "de temporalité en question. De plus, nous voyons toujours que le contenu des mails de l'année 2001 "
           "contient beaucoup plus de caractères.")

], style=CENTERED_STYLE)
