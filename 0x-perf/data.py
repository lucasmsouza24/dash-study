import pandas as pd
from utils.functions import optimize_dataframe

path = 'data.csv'

def get_data():
    data = pd.read_csv(path)
    optimize_dataframe(data)
    return data