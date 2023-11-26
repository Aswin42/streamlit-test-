
import streamlit as st
import pandas as pd

st.write("Hello, trying to deploy my streamit app. pls work")

csv_file = pd.read_csv("test.csv")

st.dataframe(csv_file)
