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
URL_DATA = 'https://storage.dosm.gov.my/population/population_state.parquet'

df = pd.read_parquet(URL_DATA)
if 'date' in df.columns: df['date'] = pd.to_datetime(df['date'])
df['year'] = df['date'].dt.year
df['population'] = df['population'].mul(1000).round(0)
df.head()

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

    df_reshaped = df_reshaped.assign(year=df_reshaped['year'].astype(int))
    year_list = list(df_reshaped['year'].unique())[::-1]
    
    selected_year = st.selectbox('Select a year', year_list)
    df_selected_year = df_reshaped[df_reshaped['year'] == selected_year]
    df_selected_year_sorted = df_selected_year.sort_values(by="population", ascending=False)
    df_selected_year_totalPop = totalPop_df[totalPop_df['year'] == selected_year]
    df_selected_year_totalPop_sorted = df_selected_year_totalPop.sort_values(by="population", ascending=False)

    color_theme_list = ['blues', 'cividis', 'greens', 'inferno', 'magma', 'plasma', 'reds', 'rainbow', 'turbo', 'viridis']
    selected_color_theme = st.selectbox('Select a color theme', color_theme_list)


#######################
# Plots


# Heatmap
def make_heatmap(input_df, input_y, input_x, input_color, input_color_theme):
    heatmap = alt.Chart(input_df).mark_rect().encode(
            y=alt.Y(f'{input_y}:O', axis=alt.Axis(title="Year", titleFontSize=18, titlePadding=15, titleFontWeight=900, labelAngle=0)),
            x=alt.X(f'{input_x}:O', axis=alt.Axis(title="", titleFontSize=18, titlePadding=15, titleFontWeight=900)),
            color=alt.Color(f'max({input_color}):Q',
                             legend=None,
                             scale=alt.Scale(scheme=input_color_theme)),
            stroke=alt.value('black'),
            strokeWidth=alt.value(0.25),
        ).properties(width=900
        ).configure_axis(
        labelFontSize=12,
        titleFontSize=12
        ) 
    # height=300
    return heatmap


# Donut chart
def make_donut(input_response, input_text, input_color):
  if input_color == 'blue':
      chart_color = ['#29b5e8', '#155F7A']
  if input_color == 'green':
      chart_color = ['#27AE60', '#12783D']
  if input_color == 'orange':
      chart_color = ['#F39C12', '#875A12']
  if input_color == 'red':
      chart_color = ['#E74C3C', '#781F16']
    
  source = pd.DataFrame({
      "Topic": ['', input_text],
      "% value": [100-input_response, input_response]
  })
  source_bg = pd.DataFrame({
      "Topic": ['', input_text],
      "% value": [100, 0]
  })
    
  plot = alt.Chart(source).mark_arc(innerRadius=45, cornerRadius=25).encode(
      theta="% value",
      color= alt.Color("Topic:N",
                      scale=alt.Scale(
                          #domain=['A', 'B'],
                          domain=[input_text, ''],
                          # range=['#29b5e8', '#155F7A']),  # 31333F
                          range=chart_color),
                      legend=None),
  ).properties(width=130, height=130)
    
  text = plot.mark_text(align='center', color="#29b5e8", font="Lato", fontSize=32, fontWeight=700, fontStyle="italic").encode(text=alt.value(f'{input_response} %'))
  plot_bg = alt.Chart(source_bg).mark_arc(innerRadius=45, cornerRadius=20).encode(
      theta="% value",
      color= alt.Color("Topic:N",
                      scale=alt.Scale(
                          # domain=['A', 'B'],
                          domain=[input_text, ''],
                          range=chart_color),  # 31333F
                      legend=None),
  ).properties(width=130, height=130)
  return plot_bg + plot + text



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
col = st.columns((1.5, 4.5, 2), gap='medium')

with col[0]:
    st.markdown('#### Gains/Losses')

    df_population_difference_sorted = calculate_population_difference(totalPop_df, selected_year)
    df_country_population_difference_sorted = calculate_population_difference(population_by_year_df, selected_year)
    selected_year = int(selected_year)

    if selected_year > 2020:
        pop_name = "Overall"
        pop_population = format_number(df_country_population_difference_sorted.population.values[0])
        pop_delta = format_number(df_country_population_difference_sorted.population_difference.values[0])
    else:
        pop_name = '-'
        pop_population = '-'
        pop_delta = ''
    st.metric(label=pop_name, value=pop_population, delta=pop_delta)

    if selected_year > 2020:
        max_state_name = df_population_difference_sorted.state.iloc[df_population_difference_sorted['population_difference'].idxmax()]
        max_state_population = format_number(df_population_difference_sorted.population.iloc[df_population_difference_sorted['population_difference'].idxmax()])   
        max_state_delta = format_number(df_population_difference_sorted.population_difference.iloc[df_population_difference_sorted['population_difference'].idxmax()])   
    else:
        max_state_name = '-'
        max_state_population = '-'
        max_state_delta = ''
    st.metric(label=max_state_name, value=max_state_population, delta=max_state_delta)

    
    st.markdown('#### Percentages')

    male_population_sum = df_reshaped[(df_reshaped['sex'] == 'male') & (df_reshaped['year'] == selected_year)]['population'].sum()
    female_population_sum = df_reshaped[(df_reshaped['sex'] == 'female') & (df_reshaped['year'] == selected_year)]['population'].sum()
    population_sum = df_reshaped[(df_reshaped['sex'] == 'both') & (df_reshaped['year'] == selected_year)]['population'].sum()
    male_percentage = male_population_sum / population_sum * 100
    female_percentage = female_population_sum / population_sum * 100
    male_percentage = math.ceil(male_percentage)
    female_percentage = math.ceil(female_percentage)

    if selected_year > 2020:
        donut_chart_greater = make_donut(male_percentage, 'Male', 'blue')
        donut_chart_less = make_donut(female_percentage, 'Female', 'red')

    migrations_col = st.columns((0.2, 1, 0.2))
    with migrations_col[1]:
        st.write('Male Population')
        st.altair_chart(donut_chart_greater)
        st.write('Female Population')
        st.altair_chart(donut_chart_less)

with col[1]:
    st.markdown('#### Total Population')
    
    heatmap = make_heatmap(df_reshaped, 'year', 'state', 'population', selected_color_theme)
    st.altair_chart(heatmap, use_container_width=True)
    

with col[2]:
    st.markdown('#### Top States')

    st.dataframe(df_selected_year_totalPop_sorted,
                 column_order=("state", "population"),
                 hide_index=True,
                 width=None,
                 column_config={
                    "state": st.column_config.TextColumn(
                        "State",
                     ),
                    "population": st.column_config.ProgressColumn(
                        "Population",
                        format="%f",
                        min_value=0,
                        max_value=max(df_selected_year_totalPop_sorted.population),
                    )}
                 )
    
    with st.expander('About', expanded=True):
        st.write('''
            - Data: [Department of Statistics Malaysia](https://storage.dosm.gov.my/population/population_state.parquet).
            ''')     
    
    



