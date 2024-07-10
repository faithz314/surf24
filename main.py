import animatedgraph1



predictions, df_predictions= animatedgraph1.make_file('C:/Users/faith/OneDrive/Documents/FaithZhang/SURF/RealTimeDetection/daily_maxmin/REPO/sample-patient.csv')

animatedgraph1.create_animation(predictions, df_predictions)


