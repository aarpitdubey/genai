## Streamlit

Firstly, install the streamlit package

```python
pip install streamlit
```

Then, create a python file like app.py and import the streamlit modules

```python
import streamlit as st
import pandas as pd
import numpy as np

st.title("Title you want to show")
```

![img](./img/streamlit.gif "Author: Arpit Dubey")

Lets add a Text "Successfully Login!!"

```python
import streamlit as st
import pandas as pd
import numpy as np

# Title of the application
st.title('Welcome Arpit Dubey!')

# Display a Simple Text
st.write('Successfully Login!!')
```

![img](./img/streamlit1.gif "Author: Arpit Dubey")

Now, let's show a DataFrame using pandas library

let's create a dummy dataset in dictionary format :

```python
df = pd.DataFrame({
    'Height': [162, 164, 170, 180],
    'Experience': [4, 7, 5, 8],
    'Salary': [60000, 180000, 55000, 90000]
})
```

Here the code :

```python
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
```

![img](./img/st_dataframe.gif "Author: Arpit Dubey")

Let's Create a Line Chart :

```python
# Let's create a line Chart
st.write('This is the line chart :')
line_chart = pd.DataFrame(
    np.random.randn(12, 3), columns=['Microsoft', 'Intel', 'Google']
)

st.line_chart(line_chart)
```

![img](./img/line_chart.gif "Author: Arpit Dubey")

Let's us create a slider for age, selectbox for language and Uploading a file.

```python
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
  
```

![img](./img/slider_selectbox_upload_file.gif "Author: Arpit Dubey")
