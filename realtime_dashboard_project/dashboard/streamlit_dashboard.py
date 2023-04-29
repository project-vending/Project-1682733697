python
import streamlit as st
import pandas as pd

# Load data from a CSV file
data = pd.read_csv("../data/streaming_data.csv")

# Display data in a table
st.dataframe(data)

# Display a bar chart of data
st.bar_chart(data)
