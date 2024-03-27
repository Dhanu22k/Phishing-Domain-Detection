from finalModel.prediction import predict
from finalModel.url_extraction import extract_features
import pandas as pd

def save_features_to_csv(features, filename='input_data.csv'):
    df = pd.DataFrame([features])
    df.to_csv(filename, index=False)

print("----Testing Phishing Url-------")
url=input("Enter the Url:")
print("Extracting the features of domain......")
url_features = extract_features(url)
print("Saving to csv.....")
save_features_to_csv(url_features)
print("Predicting.....")
prediction=predict();
if(prediction):
    print("Url is phishing")
else:
    print(f"The Entered Url:{url} is not phishing")
