#from functions import get_urls_metrics
import pandas as pd
import streamlit as st
import base64
import io


# Hello World
#print('Hello World')

st.write("""

# Welcome to this prototype

Here we are, making our first Streamlit data science app

""")

uploaded_file = st.file_uploader('Choose the xls file')
if uploaded_file is not None:
    #read xls or xlsx
    df1 = pd.read_excel(uploaded_file)
    filename = uploaded_file.name
    filename_new = filename.split('.')
    filename_new = filename_new[0]  + ' new.xlsx'

    st.dataframe(df1.head())
    df1['age'] = df1['age'] + 1

    st.markdown('Streamlit is **_really_ cool**. Now we are making the dataframe transformation:')
    
    st.dataframe(df1.head())

    towrite = io.BytesIO()
    downloaded_file = df1.to_excel(towrite, encoding='utf-8', index=False, header=True) # write to BytesIO buffer
    towrite.seek(0)  # reset pointer
    b64 = base64.b64encode(towrite.read()).decode() 
    linko= f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="{filename_new}">Download new excel file</a>'
    st.markdown(linko, unsafe_allow_html=True)


else:
    st.warning('You need to upload the sample excel file provided.')