import pandas as pd
import numpy as np

np.random.seed(42)
n = 10000

df = pd.DataFrame({
    'CustomerID': range(1, n+1),
    'Age': np.random.randint(18, 70, n),
    'Gender': np.random.choice(['Male', 'Female'], n),
    'Tenure': np.random.randint(1, 72, n),
    'MonthlyCharges': np.round(np.random.uniform(20, 120, n), 2),
    'TotalCharges': np.round(np.random.uniform(100, 8000, n), 2),
    'NumOfProducts': np.random.randint(1, 5, n),
    'HasCreditCard': np.random.choice([0, 1], n),
    'IsActiveMember': np.random.choice([0, 1], n),
    'ContractType': np.random.choice(['Month-to-Month', 'One Year', 'Two Year'], n),
    'PaymentMethod': np.random.choice(['Electronic Check', 'Mailed Check', 'Bank Transfer', 'Credit Card'], n),
    'SupportCalls': np.random.randint(0, 10, n),
})

# Generate churn based on logic
churn_prob = (
    (df['Tenure'] < 12).astype(int) * 0.3 +
    (df['MonthlyCharges'] > 80).astype(int) * 0.2 +
    (df['SupportCalls'] > 5).astype(int) * 0.2 +
    (df['ContractType'] == 'Month-to-Month').astype(int) * 0.2 +
    (df['IsActiveMember'] == 0).astype(int) * 0.1
)
churn_prob = churn_prob / churn_prob.max()
df['Churn'] = (np.random.rand(n) < churn_prob).astype(int)

df.to_csv('customer_churn_dataset.csv', index=False)
print(f"Dataset created! Shape: {df.shape}")
print(f"Churn rate: {df['Churn'].mean():.2%}")
