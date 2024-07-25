import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

#RAW DATA BEING A CSV FILE THAT HAS BEEN READ ALREADY
def creatinine_comparison(raw_data, risk_results):
    #RISK RESULTS BEING THE DATAFRAME FROM PREDICTING ALGORITHM

    x= raw_data['time']
    y1= raw_data['creatinine_max']
    y2= raw_data['creatinine_min']
    y3= risk_results['Prediction: Risk of AKI']


    plt.figure(figsize=(8, 6)) 
    plt.plot(x, y1, color= 'blue')
    plt.plot(y2, color= 'green')
    plt.plot(y3, color='red')
    plt.fill_between(x, y1, y2, where=(y1 > y2), interpolate=True, color='green', alpha=0.3, label='Minimum and Maximum Creatinine Levels of the previous 24 hours at each hour')

    
    plt.xlabel('Time')
    plt.ylabel('Creatinine Levels (Min and Max of each 24 hour block)')
    plt.title('Predicted AKI Risk vs. Creatinine Levels Over Time')

    st.pyplot(plt)



def heatmap():
    null


