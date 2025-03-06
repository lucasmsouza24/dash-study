from dash import Input, Output
import pandas as pd
import os
import psutil
import gc

from data import get_data

def register_callbacks(app):

    # read and inject data on DCC Store
    @app.callback(
        Output('store-data', 'data'),
        Input('store-data', 'id')
    )
    def inject_dataframe(_):
        gc.collect()
        
        df = get_data()
        result = df.to_dict('records')

        del df
        gc.collect()
        return result
    
    # set dropdown options and default value
    @app.callback(
        [Output('dropdown-country', 'options'),
        Output('dropdown-country', 'value')],
        Input('store-data', 'data'),
        prevent_initial_call=True
    )
    def init_dropdown_country(data):
        gc.collect()
        data = pd.DataFrame(data)

        options = [{'label': country, 'value': country} for country in data['Country'].unique()]
        default_value = options[0]['value']

        del data
        gc.collect()
        return [options, default_value]

    # apply filter
    @app.callback(
        Output("data-table", "data"),
        Input("dropdown-country", "value"),
        Input("store-data", "data"),
        prevent_initial_call=True
    )
    def update_table(selected_country, data):
        gc.collect()
        data = pd.DataFrame(data)

        if selected_country:
            data = data[data["Country"] == selected_country]

        result = data.to_dict("records")

        del data
        gc.collect()
        return result
