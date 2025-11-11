# Loan-Prediction-ML-Project

Live Application Link is Below 

https://loan-prediction-ml-project-wrs6xvxvkvn8oem2csxjv7.streamlit.app/




# 💰 Loan Prediction ML Project

## 📋 Description

The **Loan Prediction ML Project** is a machine learning–based web application designed to predict whether a loan applicant is likely to be approved or not based on key financial and personal factors. The system uses a trained classification model to analyze input features such as income, credit history, loan amount, and employment details to generate a reliable prediction.

This project showcases how **Machine Learning** can help financial institutions automate and improve the loan approval process by reducing human error and decision time.

---

## 🚀 Features

* 🤖 Predicts loan approval status using a trained ML model
* 💻 Interactive user interface built with **Streamlit**
* ⚙️ Accepts multiple user inputs and provides instant results
* 📊 Model trained using historical loan applicant data
* 🔍 Provides insights into how various factors affect loan eligibility

---

## 🧩 Tech Stack

* **Programming Language:** Python
* **Frontend Framework:** Streamlit
* **Machine Learning Library:** Scikit-learn
* **Other Libraries:**

  * Pandas
  * NumPy
  * Matplotlib / Seaborn
  * Pickle (for saving and loading the trained model)

---

## 🧠 How It Works

1. The user enters loan application details such as:

   * Applicant’s Gender
   * Marital Status
   * Education
   * Applicant Income & Co-applicant Income
   * Loan Amount & Loan Term
   * Credit History
   * Property Area
2. The app preprocesses the input data and applies the same transformations used during model training.
3. The trained classification model (saved as a `.pkl` file) predicts the loan approval status.
4. The result (“Approved” or “Not Approved”) is displayed instantly on the dashboard.

---

## ⚙️ Setup and Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/loan-prediction-ml-project.git
   cd loan-prediction-ml-project
   ```
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

---

## 📈 Model Training (Optional)

If you want to retrain the model:

1. Open the `model_training.ipynb` notebook.
2. Load and preprocess the dataset.
3. Train using classification algorithms (e.g., Logistic Regression, Random Forest, Decision Tree).
4. Save the trained model as a `.pkl` file:

   ```python
   import pickle
   pickle.dump(model, open('loan_model.pkl', 'wb'))
   ```

---

## 🖼️ Screenshot

<img width="742" height="819" alt="image" src="https://github.com/user-attachments/assets/b0b63085-fd5d-4c76-b4b8-66b9ed16c533" />



---

## 📚 Future Enhancements

* Integration with real-time credit scoring APIs
* Adding visual analytics dashboard for loan trends
* Deployment on cloud platforms (Heroku / AWS / Streamlit Cloud)
* Improving model accuracy with advanced ensemble techniques

---

## 👨‍💻 Author

**Developed by:** [Om Bankar]
**Email:** [ombankar25@gmail.com]

---


