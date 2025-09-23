import streamlit as st
import pandas as pd

import preprocessor, helper
df=pd.read_csv('athlete_events.csv')
region_df=pd.read_csv('noc_regions.csv')
df = preprocessor.preprocess(df, region_df)

st.sidebar.title("Olympics Analysis")
user_menu= st.sidebar.radio(
    'Select an option',
    ('Medal Tally', 'Overall Analysis', 'Country-wise analysis','Athlete wise Analysis')

)

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
    st.table(medal_tally)

if user_menu == 'Overall Analysis':
    editions = df['Year'].nunique() - 1
    cities = df['City'].nunique()
    sports = df['Sport'].nunique()
    events = df['Event'].nunique()
    athletes = df['Name'].nunique()
    nations = df['region'].nunique()

    # Create 3 columns
    col1, col2, col3, col4,col5, col6 = st.columns(6)
    with col1:
        st.header("Editions ")
        st.title(editions)
    with col2:
        st.header("Host ")
        st.title(cities)
    with col3:
        st.header("Sports ")
        st.title(sports)
    with col4:
        st.header("Events ")
        st.title(events)
    with col5:
        st.header("Athlets ")
        st.title(athletes)
    with col6:
        st.header("nations ")
        st.title(nations)

