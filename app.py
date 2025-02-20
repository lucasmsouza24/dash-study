from dash import Dash, html, dcc, dash_table
import pandas as pd

# Inicializando o app
app = Dash(__name__)

# Layout da aplicação
app.layout = html.Div(children=[
    dcc.Store(id='store-data'),

    html.H1("Dash Simple App", style={'textAlign': 'center'}),

    html.Div([
        html.Label("Select Country:"),
        dcc.Dropdown(
            id='dropdown-country',
            options=[],
            value=None,
            multi=False
        )
    ], style={'width': '50%', 'margin': 'auto'}),

    html.Br(),

    dash_table.DataTable(
        id="data-table",
        columns=[
            {"name": "Country", "id": "Country"},
            {"name": "Year", "id": "Year"},
            {"name": "Volume(Mt)", "id": "Volume(Mt)"}
        ],
        style_table={'overflowX': 'auto'}
    )
])

# Importando as callbacks DEPOIS da criação do app
from callbacks import register_callbacks
register_callbacks(app)

# Rodando o app
if __name__ == '__main__':
    app.run(debug=True)
