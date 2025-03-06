import psutil
import os
import pandas as pd
import numpy as np

def memory_usage(num):
    process = psutil.Process(os.getpid())
    mem = process.memory_info().rss / (1024 * 1024)  # Convertendo para MB
    print(f"> [MEMORY USAGE] >> {num} -> {mem:.2f} MB")

def tamanho_df_mb(df):
    """Retorna o tamanho do DataFrame em MB."""
    return df.memory_usage(deep=True).sum() / 1_048_576  # Convertendo bytes para MB

def optimize_dataframe(df: pd.DataFrame):

    for col in df.columns:
        col_type = df[col].dtype

        if col_type == 'object':
            unique_count = df[col].nunique()
            total_count = len(df[col])

            if unique_count / total_count < 0.5:
                df[col] = df[col].astype('category')
        
        elif np.issubdtype(col_type, np.integer):
            df[col] = pd.to_numeric(df[col], downcast='integer')
        
        elif np.issubdtype(col_type, np.floating):
            df[col] = pd.to_numeric(df[col], downcast='float')