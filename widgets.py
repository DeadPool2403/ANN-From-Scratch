import streamlit as st
import pandas as pd

st.title("StreamLit Text Input")

name=st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}")

age=st.slider("Select your age",0,100,25)
st.write(age)

options = ["C++","Java","Python"]
lang=st.selectbox("Choose language: ", options)
st.write(f"Language: {lang}")

df = pd.DataFrame({
    'first column': [1,2,3,4],
    'second column': [10,20,30,40]
})
df.to_csv("sample.csv")
st.write("Here is the dataframe")
st.write(df)

uploaded_file=st.file_uploader("Upload CSV",type="csv")
if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)