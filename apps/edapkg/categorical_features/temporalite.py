import dash_core_components as dcc
import dash_html_components as html
import pathlib
import pandas as pd
import plotly.express as px

# get relative data folder
from app import app
from apps.csv_import import data

df = data

# figure 1
# directement via png

# figure 3
df_temp = df[['DayWeek', 'Years']].groupby(['DayWeek', 'Years']).size().to_frame('mails').reset_index()
fig3 = px.line(df_temp, x='DayWeek', y='mails', color='Years')
fig3.update_layout(
    height=800,
    title_text='Evolution du nombre de mail en fonction des jours de la semaine'
)

# figure 4
fig4 = px.histogram(df, x="DayWeek", color="Years", barmode='group')
fig4.update_layout(
    height=800,
    title_text='Répartition du nombre de mail en fonction des jours de la semaine'
)
# figure 5
df = df[~((df.Years == 1980))]
df['Years'].value_counts()

fig5 = px.box(df[df['content_char_len'] < 5000], x="DayWeek", y="content_char_len", color='Years')
fig5.update_layout(
    height=800,
    title_text='Box plot de la longueur du contenu en fonction des jours de la semaine'
)

# figure 6

df_temp = df[['Hours','Years']].groupby(['Hours','Years']).size().to_frame('mails').reset_index()
fig6 = px.line(df_temp, x='Hours', y='mails', color='Years')
fig6.update_layout(
    height=800,
    title_text='Evolution du nombre de mail en fonction des heures de la journée'
)

# figure 9

df_temp = df[['Day','Years']].groupby(['Day','Years']).size().to_frame('mails').reset_index()
fig9 = px.line(df_temp, x='Day', y='mails', color='Years')
fig9.update_layout(
    height=800,
    title_text='Evolution du nombre de mail en fonction des jours du mois'
)
# figure 10

fig10 = px.histogram(df, x="Day", color="Years", barmode='group')
fig10.update_layout(
    height=800,
    title_text='Répartition du nombre de mail en fonction des jours du mois'
)

# figure 11
fig11 = px.histogram(df, x="Month", color="Years", barmode='group')
fig11.update_layout(
    height=800,
    title_text="Répartition du nombre de mail en fonction des mois de l'année"
)

# figure 12
fig12 = px.box(df[df['content_char_len']<5000], x="Month", y="content_char_len", color='Years')
fig12.update_layout(
    height=800,
    title_text="Box plot de la longueur du contenu en fonction des mois de l'année"
)

# figure 13
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

fig13 = px.bar(x=list(nb_mail), y=list(user), orientation='h')

# figure 14
count = [1 for i in range(0,len(df.From))]
data_user_cat = df[['From', 'Years']]
data_user_cat['count'] = count

sum_by_cat = data_user_cat.groupby(['From','Years']).sum().reset_index()
for index, row in sum_by_cat.iterrows():
    if row['From'] not in user:
        sum_by_cat.drop(index, inplace=True)

# On convertit au format string sinon express interpretera comme valeur continue.
sum_by_cat['Years'] = sum_by_cat['Years'].astype(str)

fig14 = px.bar(sum_by_cat, x='count', y='From', color='Years', barmode='group')

CENTERED_STYLE = {
      "padding": "100px 300px 50px "
}

layout = html.Div([
    html.H1('A - Temporalité', style={"textAlign": "center"}),
    html.B(
        "Dans la partie temporalité nous analysons les données temporelles des données à travers 3 axes: Les jours de "
        "la semaine, l'heure de la journée et le mois de l'année"),

    html.Img(src=app.get_asset_url('repartition_mail_annee.png'), style={'height': '100%', 'width': '100%'}),
    html.B("L'envoi de mail se répartie très majoritairement sur deux années, 2000 et 2001. Cela semble logique "
           "puisque l'année 2002 correspond à l'arrêt de l'entreprise."),
    html.H2('A.1 - Jours de la semaine', style={"textAlign": "center"}),
    dcc.Graph(id='fig3', figure=fig3),
    html.B("Une tendance générale montre qu'il y a plus de mails envoyés en semaine qu'en weekend, surtout pour les "
           "années 2000 et 2001, pour ces années cela illustre bien l'activité de l'entreprise qui se fait en "
           "semaine.", style={"textAlign": "center"}),

    dcc.Graph(id='fig4', figure=fig4),

    html.B(
        "Il semblerait que tous les mails de l'année 1980 aient été envoyés un mardi, après vérification c'était le "
        "même mardi, On peut remarquer la date 01/01/01 à la première heure."),
    html.B("Le contenu semble parfaitement normal, la date doit sans doute être une erreur."),
    html.B(
        "Par ailleurs, si l'on regarde précisement le contenu des mails, on peut voir la vraie date de certains mails "
        "où il y a marqué 2001 pour le 55ème mail par exemple."),
    html.B("Nous avons donc ici plusieurs problèmes:"),
    html.Br(),
    html.Ul([html.Li("La date de certains mails n'est pas la bonne, peut être même tous."),
             html.Li(
                 "Il semble compliqué de déterminer la vraie date des mails avec seulement le contenu pour certains "
                 "mails")]),
    html.Br(),
    html.B("Un choix s'impose:"),
    html.Ul([html.Li("Nous pouvons ne pas prendre en compte ces mails."),
             html.Li("Ou trouver une solution pour intégrer ces mails à leur vraie date."),
             html.Li(
                 "Le problème est qu'il est fort probable que ces mails ne soient pas du tout de l'année 1980. En "
                 "effet, la démocratisation de l'envoi de mail dans les institutions date de 1985. Nous allons donc "
                 "nous passer de ces données.")
             ]),
    dcc.Graph(id='fig5', figure=fig5),

    html.H2("A.2 - Heure de la journée", style={"textAlign": "center"}),

    dcc.Graph(id='fig6', figure=fig6),
    html.B("On voit que l'envoi de mail en fonction de l'heure de la journée varie de manière conséquente en fonction "
           "de l'année. On observe par exemple qu'en 2001 autant de mail étaient envoyés à 00h qu'en matiné alors "
           "qu'en 2000, l'envoi de mail diminuait drastiquement. Cela pourrait mettre en évidence un changement de la "
           "méthode de travail au sein de l'entreprise par exemple l'aumentation des heures supp"),

    html.H2("A.3 - Mois de l'année", style={"textAlign": "center"}),

    dcc.Graph(id='fig9', figure=fig9),
    html.B("On observe une distribution assez stable des mails tout au long du mois à part en 2001 où on semble avoir "
           "un pic d'envoi de mail en fin de mois vers le 27")

], style=CENTERED_STYLE)
