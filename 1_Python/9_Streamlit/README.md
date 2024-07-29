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
