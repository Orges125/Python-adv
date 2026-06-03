import streamlit as st
import pandas as pd
import plotly.express as px

books_df = pd.read_csv('file1.csv')

#print(books_df)

st.title("Bestselling Books Analysis")
st.write("This app analyzes the Amazon Top Selling from 2009 to 2022")

st.subheader("Summary Statistics")
total_books = books_df.shape[0]
unique_titles = books_df['Name'].nunique()