#######################
# Import libraries
import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import json
import folium
from streamlit_folium import st_folium
import math
import requests
import pprint

#######################
# Page configuration
st.set_page_config(
    page_title="Malaysia Population Dashboard",
    page_icon="🏝️",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")


#######################
# Load data
url_population_state = 'https://storage.dosm.gov.my/population/population_state.parquet'

df = pd.read_parquet(url_population_state)
if 'date' in df.columns: df['date'] = pd.to_datetime(df['date'])
df['year'] = df['date'].dt.year
df['population'] = df['population'].mul(1000).round(0)
df.head()

url_income_expenditure_state = "https://api.data.gov.my/data-catalogue?id=hies_district" 

response_json = requests.get(url=url_income_expenditure_state).json()
pprint.pprint(response_json)
income_expenditure_df = pd.DataFrame(response_json)

url_labour_force_state = "https://api.data.gov.my/data-catalogue?id=lfs_qtr_state" 

response_json = requests.get(url=url_labour_force_state).json()
pprint.pprint(response_json)
labour_force_df = pd.DataFrame(response_json)

url_cpi_state = "https://api.data.gov.my/data-catalogue?id=cpi_state_inflation" 

response_json = requests.get(url=url_cpi_state).json()
pprint.pprint(response_json)
cpi_df = pd.DataFrame(response_json)

#######################
# Data modification

df_reshaped = df
totalPop_df = df[(df['sex'] == 'both') & (df['age'] == 'overall') & (df['ethnicity'] == 'overall')].copy()
population_by_year_df = totalPop_df.groupby('year')['population'].sum().reset_index()
population_by_year_df['state'] = 'Overall'

#######################
# Sidebar
with st.sidebar:
    st.title('🏝️ Malaysia Population Dashboard')


#######################
# Plots




# Convert population to text 
def format_number(num):
    return f'{round(num, 0)}'

# Calculation year-over-year population increment or decrement
def calculate_population_difference(input_df, input_year):
    input_year = int(input_year)
    selected_year_data = input_df[input_df['year'] == input_year].reset_index()
    previous_year_data = input_df[input_df['year'] == input_year - 1].reset_index()
    selected_year_data['population_difference'] = selected_year_data.population.sub(previous_year_data.population, fill_value=0)
    return pd.concat([selected_year_data.state, selected_year_data.population, selected_year_data.population_difference], axis=1).sort_values(by="population_difference", ascending=False)

#######################
# Dashboard Main Panel
col = st.columns((6, 2), gap='medium')

with col[0]:
    st.dataframe(income_expenditure_df)

with col[1]:
    st.write('')
    with st.expander('About', expanded=True):
        st.write('''
            - Data: [Department of Statistics Malaysia](https://storage.dosm.gov.my/population/population_state.parquet).
            - :orange[**Gains/Losses**]: Overall increase or decrease in population. 
            - :orange[**Highest Increase By State**: states with highest population increase.
            ''')     
    
    