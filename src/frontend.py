import streamlit as st
import requests
import pandas as pd
import os

API_HOST = os.getenv("API_HOST")

if API_HOST:
    API_URL = f"https://{API_HOST}/predict-credit-risk"
else:
    API_URL = "http://127.0.0.1:8000/predict-credit-risk"

st.set_page_config(page_title="FinTech AI Decision Portal", layout="centered")

st.title("🏦 Bank of Mumbai: AI Loan Approval")
st.markdown("---")

with st.form("credit_form"):
    st.subheader("Applicant Details")
    
    col1, col2 = st.columns(2)
    
    with col1:
        income = st.number_input("Annual Gross Income (INR)", min_value=0, value=500000)
        loan_amount = st.number_input("Desired Loan Amount (INR)", min_value=0, value=50000)
        age = st.slider("Applicant Age", 18, 100, 30) # Optional but good for context
        
    with col2:
        loan_percent_income = round(loan_amount / income if income > 0 else 0, 2)
        st.write(f"**Loan-to-Income Ratio:** {loan_percent_income}")
        
        home_ownership = st.selectbox("Housing Status", ["RENT", "OWN", "MORTGAGE"])
        previous_default = st.selectbox("History of Default?", ["N", "Y"])

    submit_button = st.form_submit_button("Get Instant Decision")

if submit_button:
    payload = {
        "person_income": income,
        "loan_amnt": loan_amount,
        "loan_percent_income": loan_percent_income,
        "person_home_ownership": home_ownership,
        "cb_person_default_on_file": previous_default
    }

    try:
        with st.spinner("Analyzing Risk Profile..."):
            response = requests.post(API_URL, json=payload) 
            result = response.json()

        if result["decision"] == "Approve":
            st.success(f"✅ Application Approved! Probability of Default: {result['probability_of_default']:.2%}")
            st.balloons()
        else:
            st.error(f"❌ Application Rejected. Probability of Default: {result['probability_of_default']:.2%}")
            
        st.info(f"**Policy Reference:** {result['policy_reference']}")
        st.write(f"**Next Steps:** {result['next_steps']}")

    except Exception as e:
        st.error(f"Error connecting to AI Server: {e}. Please ensure FastAPI is running.")