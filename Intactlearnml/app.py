from functions.get_sidebar import *

import numpy as np
import pandas as pd
import streamlit as st

def main():
    
    st.set_page_config(page_title='Interactive ML Dashboard', page_icon = 'images/ml.ico')
    
    ########### Sidebar ###########
    
    st.sidebar.subheader('Dataset')
    data_upload = st.sidebar.file_uploader("Upload a Clean Dataset", type=("csv"))
    
    if data_upload:
        df = pd.read_csv(data_upload)
        df = df.dropna()   
    
        if df.shape[1] < 3:
            st.sidebar.warning('Please Use Other Data with at Least\
                               3 Columns (2 Features and 1 Label)')
            
        else:
            upload_expander = st.sidebar.beta_expander('Choose the Feature and Label')

            X_col = upload_expander.multiselect('Feature(s)', df.columns.tolist())
            y_col = upload_expander.multiselect('Label(s)', df.columns.tolist())
            X_upload = np.array(df[X_col])
            from sklearn.preprocessing import LabelEncoder
            label = LabelEncoder()
            
            y_upload = label.fit_transform(df[y_col])
            y_upload = np.array(y_upload)
            
    dataset_name = st.sidebar.selectbox(
        'Or Choose Predefined Dataset',
        ('None', 'Iris', 'Cancer', 'Wine', 'Digits', 'XoR', 'Donut'),
        index=0)
        
    ########### DOUBLE ###########
        
    if data_upload is not None and dataset_name != 'None':
        st.sidebar.warning('Please Choose Only One Dataset')

    ########### Data Upload ###########
    
    elif data_upload is not None and df.shape[1] >= 3:
        dataset_name = data_upload.name[:-4].title()
        empty = np.empty([0], dtype='float64')
        
        if X_col != empty and y_col != empty:
            get_sidebar_xy(dataset_name, X_upload, y_upload)
            
        else:
            upload_expander.warning('Choose the Feature and Label')
        
    ########### Data Predefined ###########
    
    elif dataset_name != 'None':
        get_sidebar(dataset_name)
    
    ########### Home ###########
    
    else:
        st.markdown("""
                    <h1 style='text-align: center;'>\
                        Interact Learn</h1>
                    """, 
                    unsafe_allow_html=True)
        
        gif_url = "https://media.giphy.com/media/A0B7BnpAVRjMJYBZWD/giphy.gif"

        st.markdown(
            
            f'<div style="display: flex; justify-content: center; align-items: center; height: 60vh;">'
            f'<img src="{gif_url}" width="500" style="object-fit: contain;">'
            f'</div>',
            unsafe_allow_html=True
)
        
        st.markdown(
    """
    <div style="font-size: 24px; text-align: center;">
        Project by: 
        <img src="https://media.giphy.com/media/HQTYdpx1yhxWpugAi2/giphy.gif" alt="Project Gif" width="70" height="70">
        <a href="https://www.linkedin.com/in/sujalsethi44/" target="_blank">Sujal Sethi</a>, 
        <a href="https://www.linkedin.com/in/dawarmuskan4/" target="_blank">Muskan Dawar</a>, 
        <a href="https://www.linkedin.com/in/nimish-batra/" target="_blank">Nimish Batra</a>
    </div>
    """,
    unsafe_allow_html=True
)
        
if __name__ == '__main__':
    main()
    
