# Python file for streamlit app

import matplotlib
# matplotlib.use('TkAgg') 
import streamlit as st
import time

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation



#import seaborn as sns
# import mplcursors

#sns.set(style='ticks', palette='muted')



def make_file(predictions):
    #predictions= pd.read_csv(csv) #C:/Users/faith/OneDrive/Documents/FaithZhang/SURF/RealTimeDetection/daily_maxmin/REPO/sample-patient.csv
    #predictions.head()


    df_predictions = pd.DataFrame({
        'Hour': predictions['time'],
        'Predicted': predictions['Prediction: Risk of AKI'],
        'Actual':predictions['Actual AKI Risk Result'],
    })
    print("MADE IT")
    return predictions, df_predictions





    #fig, ax = plt.subplot()


def update(predictions, df_predictions, fig, ax, frame):
    ax.clear()  # clears the plot
    ax.axhline(y=0.5, color='green', linestyle='-', label='50% Risk Of AKI')

    ax.plot(df_predictions['Hour'][:frame+1], df_predictions['Predicted'][:frame+1], label='Predicted Risk')
    ax.fill_between(df_predictions['Hour'][:frame+1], 0, 1,where=(df_predictions['Actual'][:frame+1] ==1), color='red', alpha=0.3, label= "AKI Actually Detected")

    patient_no = predictions['hadm_id'][0]
    hour= df_predictions['Hour'][frame]


    ax.legend()
    ax.set_xlabel('Hours (After ICU Admission)')
    ax.set_ylabel('% Risk of AKI For The Next 24 Hours')
    ax.set_title(f'Hourly Predictions of AKI Risk For Patient No.: {patient_no}')


    ax.set_xlim(0,len(df_predictions))
    ax.set_ylim(df_predictions['Predicted'].min(),1)
    ax.grid(True)
    # ax.tight_layout()


def animate(predictions, df_predictions, fig, axs):
    for frame in range(len(df_predictions)):
        update(predictions, df_predictions, fig, axs, frame)
        #plt.pause(0.1)  # Pause for 0.1 seconds (adjust as needed)
        time.sleep(0.1)
        plt.draw()  # Update the plot



    # st.pyplot(fig)

    
    # anim = animation.FuncAnimation(fig, update, frames=len(df_predictions1), interval=100)

    #plt.show()



    # if st.button('Generate Plot'):
    #     # Clear previous plot (if any)
    #     plt.clf()
    #     generate_plot()

    #     # Display the plot within the Streamlit app
    #     st.pyplot()


