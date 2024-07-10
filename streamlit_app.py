# app.py
from autogluon.tabular import TabularDataset, TabularPredictor

import streamlit as st
import RealTimeDetection
import pandas as pd
import numpy as np
import animatedgraph1
import matplotlib
matplotlib.use('TkAgg') 
from io import BytesIO


import matplotlib.pyplot as plt
# import plt.animation as animation

def main():
    id_placeholder= 'XXXXXXX'

    # Sidebar
    text_input = st.sidebar.text_input('Clinician Name', '[Enter Name Here]')
    st.sidebar.header('AKI Prediction Range')
    slider_value = st.sidebar.slider('Select a range', 24, 200, (25, 75))
    checkbox = st.sidebar.checkbox('Show data')


    #Main interface
    title_placeholder = st.empty()
    title_placeholder.markdown(f'## AKI Prediction Dashboard- Patient No. : {id_placeholder}')
    st.write(f'Hello, {text_input}!')
    
    # if checkbox:
    #     st.subheader('Selected range:')
    #     st.write(slider_value)




    #Replicated Plot here:
    csv_placeholder= pd.read_csv('C:/Users/faith/OneDrive/Documents/FaithZhang/SURF/RealTimeDetection/daily_maxmin/REPO/sample-patient.csv')

    if st.button('See Sample Prediction Graph'):
        predictions, df_predictions = animatedgraph1.make_file(csv_placeholder)
        st.write("### Original DataFrame")
        st.write(predictions.head())  # Display some data from the CSV file
        animatedgraph1.create_animation(predictions, df_predictions)
        st.pyplot()


    #1)UPLOAD RAW CSV data here
    uploaded_file = st.file_uploader("Upload a valid CSV file here:", type=["csv"])
    if uploaded_file is not None:
        csv = pd.read_csv(uploaded_file)
        actual_id= csv['hadm_id'][0]
        title_placeholder.markdown(f"## AKI Prediction Dashboard- Patient No. : {actual_id}")
        st.write(csv)

    
    #2/3)RUN THE MACHINE LEARNING ALGORITHM ON IT + spits out statistics/visualizations
        if st.button('Predict AKI'):
            features, new_df= RealTimeDetection.hourly_probability_predictor(csv)
            new_csv= new_df.to_csv(index=False).encode('utf-8')

    #4)  SPITS OUT A NEW CSV FILE WITH EACH HOURLY PREDICTION
            st.write(features)
            st.download_button(
            "Download Prediction Data",
            new_csv,
            file_name= f'{actual_id}.csv',
            mime='text/csv'
            )


if __name__ == '__main__':
    main()










