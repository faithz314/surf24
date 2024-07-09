# app.py

import streamlit as st

def main():
    st.title('AKI Prediction Dashboard')
    st.write("Hello, world!")

    st.sidebar.header('User Input')
    slider_value = st.sidebar.slider('Select a range', 0, 100, (25, 75))
    text_input = st.sidebar.text_input('Enter your name', 'John Doe')
    checkbox = st.sidebar.checkbox('Show data')

if __name__ == '__main__':
    main()
