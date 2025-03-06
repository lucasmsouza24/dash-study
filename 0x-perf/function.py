def generate_summary_table_raw(df, locations_list_asc, years):
    data_df = df.copy()

    if not locations_list_asc:
        return data_df.to_dict('records')
    
    renamed_df = data_df.rename(columns={
        'ReportingCountry': 'Country',
        'Volume': 'Volume(Mt)'
    })
    
    filtred_location = renamed_df[renamed_df['Country'].isin(locations_list_asc)]

    filtred_years = filtred_location[filtred_location['Year'].isin(years)]

    filtred_columns_df = filtred_years[['Country', 'Year', 'Period', 'Exp_or_Imp', 'Volume(Mt)']]

    style_data_conditional = None

    return filtred_columns_df, style_data_conditional