import pandas as pd
import streamlit as st

df = pd.DataFrame({
    'Name': ['Alice','Bob','Charlies'],
    'Age': [24,22,27],
    'City':['Los Angeles','New York','Prishtine']

})

st.write(df)

