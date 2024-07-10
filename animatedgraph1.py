# Python file for streamlit app

import matplotlib
matplotlib.use('TkAgg') 


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation


#import seaborn as sns
# import mplcursors

#sns.set(style='ticks', palette='muted')



def make_file(csv):
    predictions= pd.read_csv(csv) #C:/Users/faith/OneDrive/Documents/FaithZhang/SURF/RealTimeDetection/daily_maxmin/REPO/sample-patient.csv
    predictions.head()


    df_predictions = pd.DataFrame({
        'Hour': predictions['time'],
        'Predicted': predictions['Prediction: Risk of AKI'],
        'Actual':predictions['Actual AKI Risk Result'],
    })

    return predictions, df_predictions




def create_animation(predictions1, df_predictions1):

    fig = plt.figure(figsize=(10, 6))


    def update(predictions, df_predictions, frame):
        plt.cla()  # clears the plot
        plt.axhline(y=0.5, color='green', linestyle='-', label='50% Risk Of AKI')

        plt.plot(df_predictions['Hour'][:frame+1], df_predictions['Predicted'][:frame+1], label='Predicted Risk')
        plt.fill_between(df_predictions['Hour'][:frame+1], 0, 1,where=(df_predictions['Actual'][:frame+1] ==1), color='red', alpha=0.3, label= "AKI Actually Detected")

        patient_no = predictions['hadm_id'][0]
        hour= df_predictions['Hour'][frame]


        plt.legend()
        plt.xlabel('Hours (After ICU Admission)')
        plt.ylabel('% Risk of AKI For The Next 24 Hours')
        plt.title(f'Hourly Predictions of AKI Risk For Patient No.: {patient_no}')


        plt.xlim(0,len(df_predictions))
        plt.ylim(df_predictions['Predicted'].min(),1)
        plt.grid(True)
        plt.tight_layout()


    for frame in range(len(df_predictions1)):
        update(predictions1, df_predictions1, frame)
        plt.pause(0.1)  # Pause for 0.1 seconds (adjust as needed)
        plt.draw()  # Update the plot

    
    # anim = animation.FuncAnimation(fig, update, frames=len(df_predictions1), interval=100)

    plt.show()


