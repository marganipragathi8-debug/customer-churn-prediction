# 📊 Customer Churn Prediction App

A machine learning web application built with **Streamlit** that predicts whether a customer will **Churn** or **Stay** using a **Random Forest** classifier.

---

## 📌 Project Overview

This project uses a dataset of 10,000 customer records to train a Random Forest model that predicts customer churn based on features like tenure, monthly charges, contract type, and more.

---

## 🚀 Features

- ✅ Predicts **Churn** or **Not Churn**
- ✅ Shows **probability** of churn vs retention
- ✅ Provides **retention suggestions** for at-risk customers
- ✅ Interactive **bar chart** of prediction probabilities

---

## 🛠️ Technologies Used

| Tool | Purpose |
|---|---|
| Python 3 | Core programming language |
| Streamlit | Interactive web application |
| Scikit-learn | Random Forest model & scaling |
| Pandas & NumPy | Data manipulation |
| Pickle | Model serialization |

---

## 📁 Project Structure

```
customer-churn-prediction/
│
├── app.py                      # Streamlit web application
├── train_model.py              # Model training script
├── generate_dataset.py         # Dataset generation script
├── customer_churn_dataset.csv  # Dataset (10,000 records)
├── churn_model.pkl             # Trained Random Forest model
├── churn_scaler.pkl            # StandardScaler for input features
├── feature_names.pkl           # Feature names
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

---

## 🧠 Model Details

- **Algorithm:** Random Forest Classifier
- **Dataset:** 10,000 customer records
- **Input Features:**
  - 👤 Age, Gender
  - 📅 Tenure (months)
  - 💰 Monthly Charges & Total Charges
  - 📦 Number of Products
  - 💳 Has Credit Card
  - ✅ Is Active Member
  - 📝 Contract Type
  - 💳 Payment Method
  - 📞 Support Calls
- **Output:** Churn (1) or Not Churn (0)

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/customer-churn-prediction.git
cd customer-churn-prediction
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Generate dataset & train model
```bash
python generate_dataset.py
python train_model.py
```

### 4. Run the Streamlit app
```bash
streamlit run app.py
```

### 5. Open in browser
```
http://localhost:8501
```

---

## 📈 Project Workflow

1. **Data Generation** - 10,000 synthetic customer records
2. **Data Preprocessing** - Label encoding, feature scaling
3. **Model Training** - Random Forest Classifier
4. **Model Evaluation** - Accuracy, Precision, Recall, F1-Score
5. **Deployment** - Streamlit web app

---

## 🙋‍♀️ Author

**Pragathi Margani**
- GitHub: [@marganipragathi8-debug](https://github.com/marganipragathi8-debug)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
