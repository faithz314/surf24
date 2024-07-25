from autogluon.tabular import TabularPredictor
import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix
import streamlit as st
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation




def hourly_probability_predictor(raw_data):
    #STEP 1 OF REAL TIME DETECTION: Take a raw CSV file and running the LR algorithm on it for each hour of the csv file
    predictor = TabularPredictor.load("./auto_gluonModels/daily_target_accuracy_penaltyLR", require_py_version_match=False)

    actual_predictions= predictor.predict(raw_data)
    y_pred_proba = predictor.predict_proba((raw_data))
    print("printing here:", actual_predictions, y_pred_proba)
    print('RAWS', raw_data)

    # #STEP 2: creating a SECOND CSV file that combines the basic information of each hour and the predicted risk for each hour
    hadm_id= raw_data['hadm_id'][0]
    df_predictions= pd.DataFrame({
        'time': raw_data['time'],
        'hadm_id': raw_data['hadm_id'],
        'Prediction: Risk of AKI': y_pred_proba[1],
        'AKI In 24?': raw_data['AKI_in_24'] 
        })
    



    return df_predictions 



def feature_importance(raw_data):
    #STEP 3: For the latest hour the doctor is predicting, give a list of statistics about that prediction
    #1) Feature Importance ONLY IF they ask for it
    predictor = TabularPredictor.load("./auto_gluonModels/daily_target_accuracy_penaltyLR", require_py_version_match=False)
    feature_importance = predictor.feature_importance(raw_data)
    print(feature_importance)

    # predictor.feature_importance.plot()
    # predictor.feature_importance.plot_pdp('FeatureName')


    return(feature_importance)



def features_visual(feature_df):

    plt.figure(figsize=(10, 6))
        #WE USE feature_df.INDEX because the vitals do not 

    plt.bar(feature_df.index[feature_df['importance']!=0], feature_df['importance'][feature_df['importance']!=0], color='skyblue')
    plt.xlabel('Importance Score')
    plt.title('Feature Importance')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    st.pyplot(plt)
    # plt.show()



#raw data isn't actually raw- it's read by read_csv
# print(hourly_probability_predictor(pd.read_csv('sample-raw.csv')))


#RAW DATA IS A READ CSV
def halfday_probability_predictor(raw_data):
    predictor = TabularPredictor.load("./ag_models_12hour/halfday_target_accuracy_penaltyLR", require_py_version_match=False)


def probability_predictor_24_12(raw_data):
    predictor = TabularPredictor.load("PLACEHOLDER", require_py_version_match=False)


def expanding_window_predictor(raw_data):
    predictor = TabularPredictor.load("PLACEHOLDER", require_py_version_match=False)





def visualizations(predictions):





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































# #STEP 1 OF REAL TIME DETECTION: Take a raw CSV file and running the LR algorithm on it for each hour of the csv file
# raw_data= 'C:/Users/faith/OneDrive/Documents/FaithZhang/SURF/RealTimeDetection/daily_maxmin/REPO/sample-raw.csv'
# predictor = TabularPredictor.load("C:/Users/faith/OneDrive/Documents/FaithZhang/SURF/RealTimeDetection/daily_maxmin/REPO/auto_gluonModels/daily_target_accuracy_penaltyLR")
# actual_predictions= predictor.predict(raw_data)
# y_pred_proba = predictor.predict_proba((raw_data))
# print(actual_predictions)

# #STEP 2: For the latest hour the doctor is predicting, give a list of statistics about that prediction
# #1) Feature Importance
# feature_importance = predictor.feature_importance(raw_data)
# print(feature_importance)




# #STEP 3: creating a SECOND CSV file that combines the basic information of each hour and the predicted risk for each hour
# csv_raw = pd.read_csv('C:/Users/faith/OneDrive/Documents/FaithZhang/SURF/RealTimeDetection/daily_maxmin/REPO/sample-raw.csv')

# hadm_id= csv_raw['hadm_id'][1]

# df_predictions= pd.DataFrame({
#     'time': csv_raw['time'],
#     'hadm_id': csv_raw['hadm_id'],
#     'Prediction: Risk of AKI': y_pred_proba[1],
#     'Actual AKI Risk Result': csv_raw['AKI_in_24']
#      })

# df_predictions.to_csv(f'{hadm_id}.csv', index=False)




# print(y_pred_proba, df_predictions)
