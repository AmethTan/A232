import pandas as pd
import json
import requests
import pprint
from pandasql import sqldf

def data():
    url_population_state = 'https://storage.dosm.gov.my/population/population_district.parquet'

    df = pd.read_parquet(url_population_state)
    if 'date' in df.columns: df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year
    df['population'] = df['population'].mul(1000).round(0)
    df.head()

    url_income_expenditure_state = "https://api.data.gov.my/data-catalogue?id=hies_district" 

    response_json_01 = requests.get(url=url_income_expenditure_state).json()
    pprint.pprint(response_json_01)
    income_expenditure_df = pd.DataFrame(response_json_01)
    if 'date' in income_expenditure_df.columns: income_expenditure_df['date'] = pd.to_datetime(income_expenditure_df['date'])

    url_labour_force_state = "https://api.data.gov.my/data-catalogue?id=lfs_qtr_state" 

    response_json_02 = requests.get(url=url_labour_force_state).json()
    pprint.pprint(response_json_02)
    labour_force_df = pd.DataFrame(response_json_02)
    if 'date' in labour_force_df.columns: labour_force_df['date'] = pd.to_datetime(labour_force_df['date'])

    url_cpi_state = "https://api.data.gov.my/data-catalogue?id=cpi_state_inflation" 

    response_json_03 = requests.get(url=url_cpi_state).json()
    pprint.pprint(response_json_03)
    cpi_df = pd.DataFrame(response_json_03)
    if 'date' in cpi_df.columns: cpi_df['date'] = pd.to_datetime(cpi_df['date'])

    pysqldf = lambda q: sqldf(q, globals())

    query = """
    SELECT *
    FROM df d
    JOIN income_expenditure_df ied ON (d.date = ied.date AND d.state = ied.state AND d.district = ied.district)
    JOIN labour_force_df lfd ON (d.date = lfd.date AND d.state = lfd.state)
    JOIN cpi_df cd ON (d.date = cd.date AND d.state = cd.state)
    """

    df_combined = pysqldf(query)

    return df

print(data())