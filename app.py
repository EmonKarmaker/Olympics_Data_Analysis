import streamlit as st
import pandas as pd

import preprocessor, helper
df=pd.read_csv('athlete_events.csv')
region_df=pd.read_csv('noc_regions.csv')
df = preprocessor.preprocess(df, region_df)

st.sidebar.title("Olympics Analysis")
user_menu= st.sidebar.radio(
    'Select an option',
    ('Medal Tally', 'Ovarall Analysis', 'Country-wise analysis','Athlete wise Analysis')

)
st. dataframe(df)
if user_menu == 'Medal Tally':
    st.sidebar.header("Medal Tally")
    years,country=helper.country_year_list(df)
    selected_year = st.sidebar.selectbox("Select Year",years)
    selected_country=st.sidebar.selectbox("Select Country", country)
    medal_tally=helper.fetch_medal_tally(df,selected_year,selected_country)
    if selected_year=='Overall' and selected_country=='Overall':
        st.title("Overall Tally")

    if selected_year !='Overall' and selected_country=='Overall':
        st.title("Medal tally in "+ str(selected_year))

    if selected_year == 'Overall' and selected_country!='Overall':
        st.title(selected_country + "overall performence")

    if selected_year != 'Overall' and selected_country!='Overall':
        st.title(selected_country + "Performence in " + str(selected_year))
    st.dataframe(medal_tally)
