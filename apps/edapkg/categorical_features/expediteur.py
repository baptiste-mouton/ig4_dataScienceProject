import pathlib

import dash_html_components as html
import pandas as pd
import plotly.express as px
import dash_core_components as dcc
from apps.csv_import import data

df = data

# Figure 1
user = df.From.unique()
counter_user = []

for i in user:
    counter = 0
    for j in df['From']:
        if i == j:
            counter += 1
    counter_user.append(counter)

user_sorted = sorted(list(zip(counter_user, user)), reverse=True)[0:10]

nb_mail, user = zip(*user_sorted)


fig31 = px.bar(x=list(nb_mail), y=list(user), orientation='h')

count = [1 for i in range(0, len(df.From))]
data_user_cat = df[['From', 'Years']]
data_user_cat['count'] = count

sum_by_cat = data_user_cat.groupby(['From','Years']).sum().reset_index()


for index, row in sum_by_cat.iterrows():
    if row['From'] not in user:
        sum_by_cat.drop(index, inplace=True)

# On convertit au format string sinon express interpretera comme valeur continue.
sum_by_cat['Years'] = sum_by_cat['Years'].astype(str)

fig32 = px.bar(sum_by_cat, x='count', y='From', color='Years', barmode='group' )

CENTERED_STYLE = {
      "padding": "100px 300px 50px "
}

layout = html.Div([
    html.H1('B - Expéditeur', style={"textAlign": "center"}),
    dcc.Graph(id='fig31', figure=fig31),
    dcc.Graph(id='fig32', figure=fig32),
    html.P("Ce graphe représente la répartition du nombre de mails envoyés en fonction de l'expéditeur. Nous "
           "remarquons que l'expéditeur Jeff Dasovich a envoyé plus de mails que les autres expéditeurs avec près de "
           "10000 mails envoyés. La majorité des mails qu'il a envoyé l'ont été en 2001 contrairement aux autres "
           "expéditeurs qui ont majoritairement envoyés plus de mails durant l'année 2000. Notons que ces autres "
           "expéditeurs ont envoyé un nombre de mails inférieur ou égal à 5000 mails, ce qui représente la moitié des "
           "mails envoyés de Jeff Dasovich")

],style=CENTERED_STYLE)
