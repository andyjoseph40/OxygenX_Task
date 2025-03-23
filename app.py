import os
import pickle
import streamlit as st

# Load the trained model
model_path = r"C:\Users\Blessing\OneDrive\Documents\Andy\OxygenX\logistic_regression_model.pkl"

with open(model_path, 'rb') as file:
    classifier = pickle.load(file)

# Define categorical mappings
gender_mapping = {"Female": 0, "Male": 1}
employment_status_mapping = {"Full-time": 0, "Part-time": 1, "Self-employed": 2, "Unemployed": 3}
credit_score_category_mapping = {"Low": 0, "Medium": 1, "High": 2}

# Function to categorize credit score
def categorize_credit_score(score):
    if score < 580:
        return "Low"
    elif 580 <= score < 700:
        return "Medium"
    else:
        return "High"

# Function to make predictions
@st.cache_data()
def prediction(age, gender, income, loan_amount, tenure_months, credit_score, employment_status, 
               bank_balance, number_of_loans, missed_payments):

    # Derived Features
    debt_to_income_ratio = loan_amount / income if income > 0 else 0
    loan_to_bank_balance_ratio = loan_amount / bank_balance if bank_balance > 0 else 0
    credit_score_category = categorize_credit_score(credit_score)
    missed_payment_rate = (missed_payments / number_of_loans) if number_of_loans > 0 else 0

    # Map categorical values
    gender_numeric = gender_mapping[gender]
    employment_status_numeric = employment_status_mapping[employment_status]
    credit_score_category_numeric = credit_score_category_mapping[credit_score_category]

    # Making Predictions
    prediction = classifier.predict([[age, gender_numeric, income, loan_amount, tenure_months, 
                                      credit_score, employment_status_numeric, bank_balance, 
                                      number_of_loans, missed_payments, debt_to_income_ratio, 
                                      loan_to_bank_balance_ratio, credit_score_category_numeric, 
                                      missed_payment_rate]])

    return "Default Risk" if prediction == 1 else "No Default Risk"

# Main function to define the Streamlit web app
def main():
    # UI Styling
    html_temp = '''
    <div style='background-color: green; padding:13px'>
    <h1 style='color: black; text-align: center;'>Loan Default Prediction ML App</h1>
    </div>
    '''
    st.markdown(html_temp, unsafe_allow_html=True)

    # Input fields
    age = st.number_input("Age", min_value=18, max_value=100, value=30)
    gender = st.selectbox("Gender", tuple(gender_mapping.keys()))
    income = st.number_input("Income", min_value=0.0, value=50000.0)
    loan_amount = st.number_input("Loan Amount", min_value=0.0, value=10000.0)
    tenure_months = st.number_input("Loan Tenure (Months)", min_value=1, max_value=360, value=24)
    credit_score = st.number_input("Credit Score", min_value=300, max_value=850, value=650)
    employment_status = st.selectbox("Employment Status", tuple(employment_status_mapping.keys()))
    bank_balance = st.number_input("Bank Balance", min_value=0.0, value=5000.0)
    number_of_loans = st.number_input("Number of Loans", min_value=0, value=1)
    missed_payments = st.number_input("Missed Payments", min_value=0, value=0)

    result = ""

    # Predict button
    if st.button("Predict"):
        result = prediction(age, gender, income, loan_amount, tenure_months, credit_score, 
                            employment_status, bank_balance, number_of_loans, missed_payments)
        st.success(f"Prediction: {result}")

if __name__ == '__main__':
    main()
