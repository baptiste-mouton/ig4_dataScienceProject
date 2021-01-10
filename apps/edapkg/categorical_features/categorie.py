import dash_html_components as html
from app import app

CENTERED_STYLE = {
      "padding": "100px 300px 50px "
}

layout = html.Div([
    html.H1('C- Categorie', style={"textAlign": "center"}),
    html.Img(src=app.get_asset_url('repartition_categorie_mail.png'))


],style=CENTERED_STYLE)
