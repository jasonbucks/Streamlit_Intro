import streamlit as st
import pandas as pd

st.write("# Python Web App")

st.write("Hi Tanyax, Dude here.  I don't know how to add the tilda to the 'n' on a computer keyboard. :sunglasses:")

df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
st.write(df)

input_value = st.text_input("Enter a Message for Me to Tell Jack")

if st.button("Display Message"):
    st.write(input_value)