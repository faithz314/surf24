# app.py

import streamlit as st
import pandas as pd
import numpy as np
#import matplotlib as plt

def main():
    hadm_id= 'placeholder-here-for-now'
    st.title('AKI Prediction Dashboard')
    st.write("For Patient No:", hadm_id)

    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

    # Check if file was uploaded and process if so
    if uploaded_file is not None:
        # Read CSV file
        df = pd.read_csv(uploaded_file)
        
        # Display the dataframe
        st.write("### Uploaded DataFrame:")
        st.write(df)






    text_input = st.sidebar.text_input('Clinician Name', 'John Doe')
    st.sidebar.header('User Input')
    slider_value = st.sidebar.slider('Select a range', 0, 100, (25, 75))
    
    checkbox = st.sidebar.checkbox('Show data')

    # Displaying content based on user inputs
    st.write(f'Hello, {text_input}!')
    
    if checkbox:
        st.subheader('Selected range:')
        st.write(slider_value)

    # Plotting example
    if st.button('Plot'):
        data = np.random.randn(100, 2)
        df = pd.DataFrame(data, columns=['x', 'y'])
        plt.scatter(df['x'], df['y'])
        st.pyplot()


if __name__ == '__main__':
    main()
