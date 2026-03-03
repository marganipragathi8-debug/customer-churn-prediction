import streamlit as st
import pickle
import numpy as np
import pandas as pd
import os

# Page config
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="centered"
)

# Load model, scaler
base_path = os.path.dirname(__file__)

with open(os.path.join(base_path, 'churn_model.pkl'), 'rb') as f:
    model = pickle.load(f)

with open(os.path.join(base_path, 'churn_scaler.pkl'), 'rb') as f:
    scaler = pickle.load(f)

# Title
st.title("📊 Customer Churn Prediction App")
st.write("Fill in the customer details below to predict whether they will **Churn** or **Stay**.")
st.markdown("---")

# Input fields
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=18, max_value=100, value=35)
    gender = st.selectbox("Gender", ["Male", "Female"])
    tenure = st.number_input("Tenure (months)", min_value=0, max_value=120, value=12)
    monthly_charges = st.number_input("Monthly Charges ($)", min_value=0.0, max_value=500.0, value=65.0)
    total_charges = st.number_input("Total Charges ($)", min_value=0.0, max_value=10000.0, value=800.0)
    num_products = st.number_input("Number of Products", min_value=1, max_value=10, value=2)

with col2:
    has_credit_card = st.selectbox("Has Credit Card", ["Yes", "No"])
    is_active = st.selectbox("Is Active Member", ["Yes", "No"])
    contract_type = st.selectbox("Contract Type", ["Month-to-Month", "One Year", "Two Year"])
    payment_method = st.selectbox("Payment Method", ["Electronic Check", "Mailed Check", "Bank Transfer", "Credit Card"])
    support_calls = st.number_input("Support Calls", min_value=0, max_value=20, value=2)

st.markdown("---")

# Encode inputs
gender_enc = 1 if gender == "Male" else 0
has_cc_enc = 1 if has_credit_card == "Yes" else 0
is_active_enc = 1 if is_active == "Yes" else 0
contract_enc = {"Month-to-Month": 0, "One Year": 1, "Two Year": 2}[contract_type]
payment_enc = {"Bank Transfer": 0, "Credit Card": 1, "Electronic Check": 2, "Mailed Check": 3}[payment_method]

input_data = np.array([[age, gender_enc, tenure, monthly_charges, total_charges,
                        num_products, has_cc_enc, is_active_enc,
                        contract_enc, payment_enc, support_calls]])

# Predict button
if st.button("🔍 Predict Churn"):
    scaled_input = scaler.transform(input_data)
    prediction = model.predict(scaled_input)[0]
    probability = model.predict_proba(scaled_input)[0]

    st.markdown("---")
    if prediction == 1:
        st.error(f"⚠️ **This customer is likely to CHURN!**")
        st.metric("Churn Probability", f"{probability[1]*100:.1f}%")
        st.markdown("### 💡 Retention Suggestions:")
        st.write("- Offer a discount or loyalty reward")
        st.write("- Switch customer to a longer contract plan")
        st.write("- Assign a dedicated support agent")
        st.write("- Provide personalized product recommendations")
    else:
        st.success(f"✅ **This customer is likely to STAY!**")
        st.metric("Retention Probability", f"{probability[0]*100:.1f}%")
        st.markdown("### 🌟 Keep Up the Good Work:")
        st.write("- Continue providing excellent service")
        st.write("- Offer upsell opportunities")
        st.write("- Send appreciation messages")

    # Show probability bar
    st.markdown("---")
    st.markdown("### 📊 Prediction Probabilities")
    prob_df = pd.DataFrame({
        'Outcome': ['Stay (Not Churn)', 'Churn'],
        'Probability': [probability[0], probability[1]]
    })
    st.bar_chart(prob_df.set_index('Outcome'))
