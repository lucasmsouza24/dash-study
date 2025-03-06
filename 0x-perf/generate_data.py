import random
import pandas as pd

# Dados para o DataFrame
countries = ["Brazil", "Argentina", "Chile"]
years = list(range(2015, 2024 + 1))  # De 2015 a 2023
periods = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
exp_or_imp = ["Exportação", "Importação"]

# Gerar 50 linhas de dados
data_quantity = 100

data = {
    "Country": [random.choice(countries) for _ in range(data_quantity)],
    "Year": [random.choice(years) for _ in range(data_quantity)],
    "Period": [random.choice(periods) for _ in range(data_quantity)],
    "Exp_or_Imp": [random.choice(exp_or_imp) for _ in range(data_quantity)],
    "Volume(Mt)": [round(random.uniform(0.1, float(data_quantity)), 2) for _ in range(data_quantity)],  # Volume em Megatoneladas
}

df = pd.DataFrame(data)

df.to_csv('data.csv', index=False)