def run():
    import streamlit as st
    import datetime
    from datetime import datetime as dt
    import streamlit as st
    import streamlit.components.v1 as components
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns


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


    st.markdown("""<hr style="height:5px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)
    st.title('Take Action !')

    #input action from PJ
    @st.cache(allow_output_mutation=True)
    def get_data_input():
        return[]

    @st.cache(allow_output_mutation=True)
    def get_data_output():
        return[]

    emoji = st.markdown(':smiley:')

    aksi = st.radio(f'Hallo Iqbal, apa yang sudah dilakukan untuk data anomali ini ?', ('Kalibrasi ulang', 'Mencelupkan sensor ke air                     bersih','Reset logger', 'Membersihkan sensor'))
    tgl_aksi = datetime.datetime.now()

    if st.button('add input'):
        get_data_input().append({'Tanggal Aksi': tgl_aksi, 'Aksi':aksi})
        input_41 = pd.DataFrame(get_data_input())
        input_41.tail(1).to_csv('log_41.csv', mode='a', index = False, header = False)

    kasus = st.text_input(f'Apakah ada kasus di KLHK 41?')

    if st.button('add'):
        get_data_input().append({'Tanggal Aksi': tgl_aksi, 'Aksi':kasus})
        input_41 = pd.DataFrame(get_data_input())
        input_41.tail(1).to_csv('log_41.csv', mode='a', index = False, header = False)


    hasil = st.radio('Bagaimana hasilnya?', ('Pembacaan sensor normal', 'Pembacaan sensor masih anomali', 'Logger online kembali'))
    tgl_hasil = datetime.datetime.now()

    if st.button('add output'):
        get_data_output().append({'Tanggal Hasil': tgl_hasil, 'Hasil':hasil})
        hasil_41 = pd.DataFrame(get_data_output())
        hasil_41.tail(1).to_csv('log_hasil_41.csv', mode='a', index=False, header=False)




    st.subheader('Datalog Aksi')
    st.write(pd.DataFrame(get_data_input()))

    st.subheader('Datalog Hasil')
    st.write(pd.DataFrame(get_data_output()))

        

if __name__ == '__main__':
    run()
            
