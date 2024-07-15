from autogluon.tabular import TabularPredictor
import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix



def hourly_probability_predictor(raw_data):
    

    #STEP 1 OF REAL TIME DETECTION: Take a raw CSV file and running the LR algorithm on it for each hour of the csv file
    predictor = TabularPredictor.load("C:/Users/faith/OneDrive/Documents/FaithZhang/SURF/RealTimeDetection/daily_maxmin/REPO/auto_gluonModels/daily_target_accuracy_penaltyLR", require_version_match= False)
    actual_predictions= predictor.predict(raw_data)
    y_pred_proba = predictor.predict_proba((raw_data))
    print("printing here:", actual_predictions, y_pred_proba)

    #STEP 2: For the latest hour the doctor is predicting, give a list of statistics about that prediction
    #1) Feature Importance
    feature_importance = predictor.feature_importance(raw_data)
    print(feature_importance)

    # #STEP 3: creating a SECOND CSV file that combines the basic information of each hour and the predicted risk for each hour

    hadm_id= raw_data['hadm_id'][0]

    df_predictions= pd.DataFrame({
        'time': raw_data['time'],
        'hadm_id': raw_data['hadm_id'],
        'Prediction: Risk of AKI': y_pred_proba[1],
        'Actual AKI Risk Result': raw_data['AKI_in_24'] #ACTUALly GET RID OF THIS FOR NORMAL DATA!!!!!
        })


    return feature_importance, df_predictions


    


































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
