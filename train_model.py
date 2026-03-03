import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import pickle

# Load dataset
df = pd.read_csv('customer_churn_dataset.csv')
print("Dataset loaded. Shape:", df.shape)

# Drop CustomerID
df = df.drop('CustomerID', axis=1)

# Encode categorical columns
le = LabelEncoder()
df['Gender'] = le.fit_transform(df['Gender'])
df['ContractType'] = le.fit_transform(df['ContractType'])
df['PaymentMethod'] = le.fit_transform(df['PaymentMethod'])

# Features and target
X = df.drop('Churn', axis=1)
y = df['Churn']

# Save feature names
feature_names = list(X.columns)
with open('feature_names.pkl', 'wb') as f:
    pickle.dump(feature_names, f)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# Evaluate
y_pred = model.predict(X_test_scaled)
print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Save model and scaler
with open('churn_model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('churn_scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)

print("\nModel and scaler saved successfully!")
