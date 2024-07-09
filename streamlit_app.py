# app.py

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib as plt

def main():
    st.title('AKI Prediction Dashboard')
    st.write("Hello, world!")

    st.sidebar.header('User Input')
    slider_value = st.sidebar.slider('Select a range', 0, 100, (25, 75))
    text_input = st.sidebar.text_input('Clinician Name', 'John Doe')
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
