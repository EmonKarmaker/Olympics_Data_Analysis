import streamlit as st
import pandas as pd

import preprocessor

df=preprocessor.preprocess()

st.sidebar.radio(
    'Select an option',
    ('Medal Tally', 'Ovarall Analysis', 'Country-wise analysis','Athlete wise Analysis')

)
st. dataframe(df)