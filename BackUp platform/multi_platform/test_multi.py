import streamlit as st
from stlib import klhk41
from stlib import klhk42


message = """__Select an application from the list below__"""

with st.sidebar:
    st.markdown(message)
    A1 = st.selectbox('Select:', ['KLHK 41', 'KLHK 42'])
    A2 = st.selectbox('Select:', [str(x) for x in range(80)])
    
if A1 == 'KLHK 41':
    klhk41.run()
elif A1 == 'KLHK 42':
    klhk42.run()
    
if A2 == 'KLHK 43':
    klhk41.run()
elif A2 == 'KLHK 44':
    klhk42.run()    