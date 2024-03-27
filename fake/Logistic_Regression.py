import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import pickle

# Load the dataset
new_url = "https://drive.google.com/uc?id=1ikC81n7Fal81vAO5aLIZlTN6OMxOxHUP"
# 1pZlH6OVkdPVtjcE12yNreVXykpm__ghY
df = pd.read_csv(new_url)

# Data preprocessing
df.dropna(inplace=True)
X = df.drop(columns=['phishing'])
y = df['phishing']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train Logistic Regression model
lr_model = LogisticRegression(max_iter=1000)  # Increase max_iter to avoid convergence warning
lr_model.fit(X_train_scaled, y_train)

# Make predictions
y_pred_train = lr_model.predict(X_train_scaled)
y_pred_test = lr_model.predict(X_test_scaled)

# Evaluate model performance
train_accuracy = accuracy_score(y_train, y_pred_train)
test_accuracy = accuracy_score(y_test, y_pred_test)

print("Training Accuracy:", train_accuracy)
print("Testing Accuracy:", test_accuracy)

# Classification report
print("\nClassification Report on Testing Data:")
print(classification_report(y_test, y_pred_test))

# Serialize the trained model
with open('../finalModel/trained_model.pkl', 'wb') as f:
    pickle.dump(lr_model, f)

# Deserialize the trained model
with open('../finalModel/trained_model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

# Serialize the scaler object
with open('../finalModel/scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)


