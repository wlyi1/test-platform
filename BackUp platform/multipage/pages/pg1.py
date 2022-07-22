import streamlit as st

def tit():
    st.title("My Amazing App")
    name = st.text_input("Your Name: ")
    st.write(f"Hello {name}!")