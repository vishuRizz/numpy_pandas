import streamlit as st
import pandas as pd
import numpy as np

# title of stramlit
st.title("hey streamlit")
# to run app use cmd - streamlit run app.py

# to display a simple text
st.write("hello")

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
#lets display this dataframe
st.write(df)
# lets make line chart
chart_data = pd.DataFrame(
    np.random.randn(20,3)
)
st.line_chart(chart_data)