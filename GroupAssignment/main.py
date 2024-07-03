import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px

st.set_page_config(
    page_title="Malaysia Population Dashboard",
    page_icon="🏝️",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")

URL_DATA = 'https://storage.dosm.gov.my/population/population_state.parquet'

df = pd.read_parquet(URL_DATA)
if 'date' in df.columns: df['date'] = pd.to_datetime(df['date'])

pd.set_option('display.max_columns', None)
df.head()

print(df)