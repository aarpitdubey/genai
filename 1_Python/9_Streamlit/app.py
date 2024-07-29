import streamlit as st
import pandas as pd
import numpy as np

# Title of the application
st.title('Welcome Arpit Dubey!')

# Display a Simple Text
st.write('Successfully Login!!')

# Creating a Simple dataframe

df = pd.DataFrame({
    'Height': [162, 164, 170, 180],
    'Experience': [4, 7, 5, 8],
    'Salary': [60000, 180000, 55000, 90000]
})

# Display Dataframe
st.write('This is the simple dataframe :')
st.write(df)