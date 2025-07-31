import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open("best_model.pkl", "rb"))

st.set_page_config(page_title="NSAP Scheme Eligibility Predictor", page_icon="🤖", layout="wide")

st.title("NSAP Scheme Eligibility Predictor")
st.markdown("### Fill the details to know which NSAP welfare scheme you are eligible for")

age = st.slider("Age", 18, 100, 30)
gender = st.selectbox("Gender", ["Male", "Female"])
marital_status = st.selectbox("Marital Status", ["Married", "Unmarried", "Widow/Widower"])
income = st.number_input("Monthly Income (₹)", min_value=0, max_value=50000, value=5000)
disability = st.selectbox("Disability", ["Yes", "No"])
bpl_status = st.selectbox("BPL Status", ["Yes", "No"])
dependents = st.slider("Number of Dependents", 0, 10, 2)

input_data = pd.DataFrame({
    "age": [age],
    "gender": [gender],
    "marital_status": [marital_status],
    "income": [income],
    "disability": [disability],
    "bpl_status": [bpl_status],
    "dependents": [dependents]
})

if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    st.success(f"✅ You are eligible for **{prediction}** scheme")
    st.balloons()
