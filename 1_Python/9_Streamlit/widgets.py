import streamlit as st
import pandas as pd

# Title of the application
st.title("Streamlit Text Input")

# Text Input
name = st.text_input("Enter your name:")

if name:
    st.write(f"Hello my name is {name}.")

# Creating a slider

age = st.slider("Enter your age:", 0, 100, 18)
st.write(f"My age is {age}.")

# Creating a dropdown menu
options = ['English', 'Hindi', 'Arabic', 'Urdu', 'Gujrati', 'Sanskrit']
lang = st.selectbox("Select your Mother Tongue", options)
st.write(f"Your Mother Tongue is {lang}")

# DataFrame
data = {
    'Height': [162, 164, 170, 180],
    'Experience': [4, 7, 5, 8],
    'Salary': [60000, 180000, 55000, 90000]
}

df = pd.DataFrame(data)
st.write(df)

# Uploading a CSV file

uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, index_col=0)
    st.write(df)
    