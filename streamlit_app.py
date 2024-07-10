# app.py

import streamlit as st
import animatedgraph1
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('TkAgg') 

import matplotlib.pyplot as plt
# import plt.animation as animation

def main():
    hadm_id= 'placeholder-here-for-now'

    # Sidebar
    text_input = st.sidebar.text_input('Clinician Name', '[John Doe]')
    st.sidebar.header('AKI Prediction Range')
    slider_value = st.sidebar.slider('Select a range', 24, 200, (25, 75))
    checkbox = st.sidebar.checkbox('Show data')


    #Main interface
    st.title('AKI Prediction Dashboard- Patient No.:', hadm_id)

    #user inputs:
    st.write(f'Hello, {text_input}!')
    
    # if checkbox:
    #     st.subheader('Selected range:')
    #     st.write(slider_value)


    uploaded_file = st.file_uploader("Upload valid CSV file here", type=["csv"])

    if uploaded_file is not None:
        csv = pd.read_csv(uploaded_file)
        

        predictions, df_predictions = animatedgraph1.make_file(csv)
        st.write("### Original DataFrame")
        st.write(predictions.head())  # Display some data from the CSV file

        animatedgraph1.create_animation(predictions, df_predictions)






if __name__ == '__main__':
    main()








