import streamlit as st
from stlib import KLHK_41
from stlib import KLHK_42


message = """__Select an application from the list below__"""

with st.sidebar:
    st.markdown(message)
    page = st.selectbox('Select:', ['KLHK 41', 'KLHK 42'])
    
if page == 'KLHK 41':
    KLHK_41.run()
else:
    KLHK_42.run()