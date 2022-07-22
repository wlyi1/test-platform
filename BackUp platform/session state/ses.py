import streamlit as st
import datetime
from datetime import datetime as dt
import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


st.title('Counter')
if 'count' not in st.session_state:
    st.session_state.count = 0
    st.session_state.last_updated = datetime.time(0,0)

def update_counter():
    st.session_state.count += st.session_state.increment_value
    st.session_state.last_updated = st.session_state.update_time

with st.form(key='my_form'):
    st.time_input(label='Enter the time', value=datetime.datetime.now().time(), key='update_time')
    st.number_input('Enter a value', value=0, step=1, key='increment_value')
    submit = st.form_submit_button(label='Update', on_click=update_counter)

st.write('Current Count = ', st.session_state.count)
st.write('Last Updated = ', st.session_state.last_updated)

st.title('KLHK 41')

def chart(ylabel, xlabel, yvalues, xvalues, title=''):
    #create new graph
    
    fig = plt.figure(figsize = (10,7))
    plt.plot(xvalues, yvalues)
    plt.title(title, fontsize = 20, fontweight = 'bold')
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    return fig

df = pd.read_csv('OL41_2022.csv')
df['new_date']=pd.to_datetime(df['DATE'])
df['tgl'] = pd.to_datetime(df['DATE'] + ' ' + df['TIME'])

#st.title('KLHK 41')

option = st.selectbox('Parameter untuk dilihat data dan grafiknya', ('pH', 'DO', 'NH4', 'NO3'))

#empty chart
c1, c2 = st.columns(2)
with c1:
    if 'space_initial' not in st.session_state:
        st.session_state.space_initial = st.empty()
with c2:
    if 'space_initial_2' not in st.session_state:
        st.session_state.space_initial_2 = st.empty()
        
#chart parameter
pH = chart('pH', 'Date', df[-24:]['pH'], df[-24:]['tgl'], title= 'Grafik pH')
DO = chart('DO', 'Date', df[-24:]['DO'], df[-24:]['tgl'], title= 'Grafik DO')
suhu = chart('Suhu', 'Date', df[-24:]['TEMP'], df[-24:]['tgl'], title= 'Grafik Suhu')
NH = chart('NH', 'Date', df[-24:]['NH4'], df[-24:]['tgl'], title= 'Grafik NH')
NO = chart('NO', 'Date', df[-24:]['NO3'], df[-24:]['tgl'], title= 'Grafik NO')

#dataframe parameter
data_pH = df[-24:][['tgl', 'pH']]
data_DO = df[-24:][['tgl', 'DO']]
data_NH = df[-24:][['tgl', 'NH4']]
data_NO = df[-24:][['tgl', 'NO']]
data_T0 = df[-24:][['tgl', 'TEMP']]

#chart column
    
if option == 'pH':
    st.session_state.space_initial.write(pH)
    st.session_state.space_initial_2.write(data_pH)
elif option == 'DO':
    st.session_state.space_initial.write(DO)
    st.session_state.space_initial_2.write(data_DO)
elif option == 'NH4':
    st.session_state.space_initial.write(NH)
    st.session_state.space_initial_2.write(data_NH)
elif option == 'NO3':
    st.session_state.space_initial.write(NO)
    st.session_state.space_initial_2.write(data_NO)

    
if st.button('add input'):
    st.write('Test 41')