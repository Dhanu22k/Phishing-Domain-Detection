import pandas as pd
import pickle
def predict():
    # Load the serialized model
    with open('trained_model.pkl', 'rb') as f:
        loaded_model = pickle.load(f)

    # Load the scaler used for scaling the training data
    with open('scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)

    # Load the input data from the CSV file
    input_df = pd.read_csv('input_data.csv')

    # Remove 'phishing' column if it exists
    if 'phishing' in input_df.columns:
        input_df.drop('phishing', axis=1, inplace=True)

    # Scale the input data using the loaded scaler
    input_scaled = scaler.transform(input_df)

    # Make prediction using the loaded model
    prediction = loaded_model.predict(input_scaled)
    return prediction[0]
