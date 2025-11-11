import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open('loan_model.pkl', 'rb'))

st.title("💰 LoanSure - Loan Approval Prediction App")
st.write("Predict whether a loan application will be approved based on applicant details.")

# User Inputs
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
dependents = st.number_input("Number of Dependents", min_value=0, max_value=10, step=1)
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
applicant_income = st.number_input("Applicant Income", min_value=0)
coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
loan_amount = st.number_input("Loan Amount (in thousands)", min_value=0)
loan_term = st.selectbox("Loan Amount Term (in days)", [120, 180, 240, 300, 360])
credit_history = st.selectbox("Credit History (1: Yes, 0: No)", [1, 0])
property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

# Encoding inputs manually (same as training)
def encode_inputs():
    gender_val = 1 if gender == "Male" else 0
    married_val = 1 if married == "Yes" else 0
    education_val = 1 if education == "Graduate" else 0
    self_emp_val = 1 if self_employed == "Yes" else 0
    prop_dict = {"Urban": 2, "Semiurban": 1, "Rural": 0}
    property_val = prop_dict[property_area]

    return np.array([[gender_val, married_val, dependents, education_val, self_emp_val,
                      applicant_income, coapplicant_income, loan_amount, loan_term,
                      credit_history, property_val]])

# Prediction
if st.button("Predict Loan Approval"):
    features = encode_inputs()
    prediction = model.predict(features)
    result = "✅ Loan Approved" if prediction[0] == 1 else "❌ Loan Not Approved"
    st.success(result)
