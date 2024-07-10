# app.py

import streamlit as st
import Animation
import pandas as pd
import numpy as np
import matplotlib
# matplotlib.use('TkAgg') 

# import matplotlib.pyplot as plt
# import matplotlib.animation as animation

def main():
    hadm_id= 'placeholder-here-for-now'

    # Sidebar
    text_input = st.sidebar.text_input('Clinician Name', 'John Doe')
    st.sidebar.header('AKI Prediction Range')
    slider_value = st.sidebar.slider('Select a range', 24, 200, (25, 75))
    checkbox = st.sidebar.checkbox('Show data')


    #Main interface
    st.title('AKI Prediction Dashboard')
    st.write("For Patient No:", hadm_id)

    #user inputs:
    st.write(f'Hello, {text_input}!')
    
    # if checkbox:
    #     st.subheader('Selected range:')
    #     st.write(slider_value)



    st.title("Upload valid csv file here containing patient data")
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

    # Check if file was uploaded and process if so
    if uploaded_file is not None:
        # Read CSV file
        df = pd.read_csv(uploaded_file)
        
        # Display the dataframe
        st.write("### Uploaded Data:")
        st.write(df)



    # Plotting example
    if st.button('Plot'):
        data = np.random.randn(100, 2)
        df = pd.DataFrame(data, columns=['x', 'y'])
        plt.scatter(df['x'], df['y'])
        st.pyplot()


    #Plotting ACTUAL
    predictions, df_predictions= Animation.make_file(uploaded_file)
    Animation.create_animation(df_predictions)





if __name__ == '__main__':
    main()





