import streamlit as st 
import pandas as pd

st.header("Hello World 👏")
st.write("This is my first app")

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv "
df = pd.read_csv(url)

df2 = df.groupby('species')['body_mass_g'].mean()

st.bar_chart(df2)

genre = st.radio(
     "What's your favorite movie genre",
     ('Comedy', 'Drama', 'Documentary'))

if genre == 'Comedy':
     st.write('You selected comedy.')
elif genre == 'Drama':
     st.write('You selected drama.')
else:
     st.write("Wow! You like documentary.")