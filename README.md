# 📊 Customer Churn Prediction App

A machine learning web application built with **Streamlit** that predicts whether a customer will **Churn** or **Stay** using a **Random Forest** classifier.

🔴 **Live App:** [Click here to try the app!](https://customer-churn-prediction-vqywtwsyqceqfabrtuyvry.streamlit.app/)

---

## 📌 Project Overview

This project uses a dataset of 10,000 customer records to train a Random Forest model that predicts customer churn based on features like tenure, monthly charges, contract type, support calls, and more.

---

## 🚀 Live Demo

👉 https://customer-churn-prediction-vqywtwsyqceqfabrtuyvry.streamlit.app/

---

## ✨ Features

- Predicts Churn or Not Churn in real time
- Shows churn probability vs retention probability
- Provides actionable retention suggestions for at-risk customers
- Interactive bar chart of prediction probabilities
- Clean and user-friendly Streamlit interface

---

## 🛠️ Technologies Used

- Python 3
- Streamlit - Interactive web application
- Scikit-learn - Random Forest model and StandardScaler
- Pandas and NumPy - Data manipulation
- Pickle - Model serialization
- Jupyter Notebook - EDA and model training

---

## 📁 Project Structure

```
customer-churn-prediction/
├── app.py                         # Streamlit web application
├── train_model.py                 # Model training script
├── generate_dataset.py            # Dataset generation script
├── customer_churn_dataset.csv     # Dataset (10,000 records)
├── churn_model.pkl                # Trained Random Forest model
├── churn_scaler.pkl               # StandardScaler for input features
├── feature_names.pkl              # Feature names
├── requirements.txt               # Python dependencies
└── README.md                      # Project documentation
```

---

## 🧠 Model Details

- **Algorithm:** Random Forest Classifier
- **Dataset:** 10,000 customer records
- **Accuracy:** ~70%
- **Input Features:**
  - Age, Gender
  - Tenure (months)
  - Monthly Charges and Total Charges
  - Number of Products
  - Has Credit Card
  - Is Active Member
  - Contract Type (Month-to-Month / One Year / Two Year)
  - Payment Method
  - Support Calls
- **Output:** Churn (1) or Not Churn (0)

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/marganipragathi8-debug/customer-churn-prediction.git
cd customer-churn-prediction
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit app
```bash
streamlit run app.py
```

### 4. Open in browser
```
http://localhost:8501
```

---

## 📈 Project Workflow

1. **Data Generation** - 10,000 synthetic customer records
2. **Data Preprocessing** - Label encoding, feature scaling
3. **Model Training** - Random Forest Classifier
4. **Model Evaluation** - Accuracy, Precision, Recall, F1-Score
5. **Deployment** - Streamlit web app hosted on Streamlit Cloud

---

## 🙋‍♀️ Author

**Pragathi Margani**
- GitHub: [@marganipragathi8-debug](https://github.com/marganipragathi8-debug)
- Live App: [Customer Churn Prediction](https://customer-churn-prediction-vqywtwsyqceqfabrtuyvry.streamlit.app/)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
