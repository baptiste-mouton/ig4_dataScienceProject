import dash_html_components as html
import pandas as pd
import plotly.express as px
import pathlib
import dash_core_components as dcc

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../../../datasets").resolve()

data = pd.read_csv(DATA_PATH.joinpath("mail_clean.csv"))
df = data

# figure 15

from sklearn import preprocessing
x = df[['content_char_len','To_count']].values



min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(x)
df_scaled = pd.DataFrame(x_scaled, columns=['content_char_len_scaled','To_count_scaled'])
df_scaled = pd.concat([df,df_scaled],axis=1, join='inner')

fig15 = px.scatter(df_scaled, x='content_char_len_scaled',y='To_count_scaled',color='Years', facet_col='DayWeek', facet_col_wrap=3,
                category_orders={'DayWeek': range(0,7)})
# figure 16

fig16 = px.scatter(df_scaled, x='content_char_len_scaled',y='To_count_scaled',color='Years', facet_col='Hours', facet_col_wrap=5,
                 category_orders={'Hours': range(0,24)})

# figure 17

fig17 = px.scatter(df_scaled, x='content_char_len_scaled',y='To_count_scaled',color='Years', facet_col='Month', facet_col_wrap=3,
                 category_orders={'Month': range(1,13)})
# figure 18

fig18 = px.scatter(df_scaled, x='content_char_len_scaled',y='To_count_scaled', facet_col='Years', facet_col_wrap=3,category_orders={'Years': range(1980,2021)})


layout = html.Div([
    html.H1('II - Continuous feature', style={"textAlign": "center"}),
    dcc.Graph(id='fig15', figure=fig15),
    dcc.Graph(id='fig16', figure=fig16),
    dcc.Graph(id='fig17', figure=fig17),
    dcc.Graph(id='fig18', figure=fig18),

])