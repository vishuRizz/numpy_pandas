import streamlit as st
import pandas as pd

st.title("Welcome to the App")

name = st.text_input("Enter your name")
if name:
    st.write(f"Hello {name}, how are you?")

uploaded_file = st.file_uploader("Choose a CSV file", type='csv')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
    
    df1 = df.isnull().sum()
    st.write("Null values in each column of your uploaded file:", df1)
else:
    st.write("Please upload a CSV file to display data.")
