import dash_core_components as dcc
import dash_html_components as html
import pathlib
import pandas as pd
import plotly.express as px

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../../../datasets").resolve()

data = pd.read_csv(DATA_PATH.joinpath("mail_clean.csv"))
df = data

# figure 3
df_temp = df[['DayWeek','Years']].groupby(['DayWeek','Years']).size().to_frame('mails').reset_index()
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

fig5 = px.box(df[df['content_char_len']<5000], x="DayWeek", y="content_char_len",color='Years')
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
# figure 7

fig7 = px.histogram(df, x="Hours", color="Years", barmode='group')
fig7.update_layout(
    height=800,
    title_text='Répartition du nombre de mail en fonction des heures de la journée'
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


layout = html.Div([
    html.H1('A - Temporalité', style={"textAlign": "center"}),
    html.H2('A.1 - Jours de la semaine', style={"textAlign": "center"}),
    html.B("Feel the magic in the air"),

    dcc.Graph(id='fig3', figure=fig3),
    dcc.Graph(id='fig4', figure=fig4),
    dcc.Graph(id='fig5', figure=fig5),

    html.H2("A.2 - Heure de la journée", style={"textAlign": "center"}),

    dcc.Graph(id='fig6', figure=fig6),
    dcc.Graph(id='fig7', figure=fig7),

    html.H2("A.3 - Mois de l'année", style={"textAlign": "center"}),

    dcc.Graph(id='fig9', figure=fig9),
    dcc.Graph(id='fig10', figure=fig10),

])