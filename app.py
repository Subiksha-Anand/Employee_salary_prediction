import streamlit as st
import pandas as pd
import joblib


# Load model and label encoders
model = joblib.load("best_lgbm_model.pkl")

# Define input fields
st.title("Employee Income Prediction App")
st.write("Predict whether an individual's income is >50K or <=50K based on census data.")

# Define input fields
age = st.slider("Age", 18, 90, 30)
workclass = st.selectbox("Workclass", ['Private', 'Self-emp-not-inc', 'Self-emp-inc', 'Federal-gov', 
                                       'Local-gov', 'State-gov', 'Without-pay', 'Never-worked'])
education = st.selectbox("Education", ['Bachelors', 'HS-grad', '11th', 'Masters', '9th', 'Some-college', 
                                       'Assoc-acdm', 'Assoc-voc', '7th-8th', 'Doctorate', '5th-6th'])
education_num = st.slider("Education Number", 1, 16, 9)
marital_status = st.selectbox("Marital Status", ['Married-civ-spouse', 'Divorced', 'Never-married', 
                                                 'Separated', 'Widowed', 'Married-spouse-absent'])
occupation = st.selectbox("Occupation", ['Tech-support', 'Craft-repair', 'Other-service', 'Sales', 'Exec-managerial',
                                         'Prof-specialty', 'Handlers-cleaners', 'Machine-op-inspct', 'Adm-clerical',
                                         'Farming-fishing', 'Transport-moving', 'Priv-house-serv', 'Protective-serv', 'Armed-Forces'])
relationship = st.selectbox("Relationship", ['Wife', 'Own-child', 'Husband', 'Not-in-family', 'Other-relative', 'Unmarried'])
race = st.selectbox("Race", ['White', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo', 'Other', 'Black'])
sex = st.selectbox("Sex", ['Female', 'Male'])
capital_gain = st.number_input("Capital Gain", 0, 99999, 0)
capital_loss = st.number_input("Capital Loss", 0, 99999, 0)
hours_per_week = st.slider("Hours per Week", 1, 99, 40)
native_country = st.selectbox("Native Country", ['United-States', 'Mexico', 'Greece', 'Vietnam', 'Philippines', 
                                                 'Ireland', 'India', 'Canada', 'England', 'Germany', 'Other'])

# Manual encoding (replicate label encoders from training)
input_dict = {
    'age': age,
    'workclass': {'Private': 6, 'Self-emp-not-inc': 4, 'Self-emp-inc': 3, 'Federal-gov': 0, 
                  'Local-gov': 1, 'State-gov': 5, 'Without-pay': 7, 'Never-worked': 2}[workclass],
    'education': {'Bachelors': 0, 'HS-grad': 5, '11th': 1, 'Masters': 8, '9th': 6, 'Some-college': 13, 
                  'Assoc-acdm': 2, 'Assoc-voc': 3, '7th-8th': 11, 'Doctorate': 4, '5th-6th': 7}[education],
    'education-num': education_num,
    'marital-status': {'Married-civ-spouse': 2, 'Divorced': 1, 'Never-married': 4, 'Separated': 5,
                       'Widowed': 6, 'Married-spouse-absent': 3}[marital_status],
    'occupation': {'Tech-support': 12, 'Craft-repair': 0, 'Other-service': 8, 'Sales': 9, 'Exec-managerial': 1,
                   'Prof-specialty': 7, 'Handlers-cleaners': 4, 'Machine-op-inspct': 5, 'Adm-clerical': 10,
                   'Farming-fishing': 2, 'Transport-moving': 13, 'Priv-house-serv': 11, 'Protective-serv': 6, 
                   'Armed-Forces': 3}[occupation],
    'relationship': {'Wife': 5, 'Own-child': 1, 'Husband': 0, 'Not-in-family': 2, 
                     'Other-relative': 3, 'Unmarried': 4}[relationship],
    'race': {'White': 4, 'Asian-Pac-Islander': 1, 'Amer-Indian-Eskimo': 0, 'Other': 2, 'Black': 3}[race],
    'sex': {'Female': 0, 'Male': 1}[sex],
    'capital-gain': capital_gain,
    'capital-loss': capital_loss,
    'hours-per-week': hours_per_week,
    'native-country': {'United-States': 39, 'Mexico': 24, 'Greece': 15, 'Vietnam': 67, 'Philippines': 57,
                       'Ireland': 17, 'India': 16, 'Canada': 7, 'England': 13, 'Germany': 14, 'Other': 0}[native_country]
}

# Convert to DataFrame
input_df = pd.DataFrame([input_dict])

# Predict
if st.button("Predict Income Level"):
    prediction = model.predict(input_df)[0]
    result = ">50K" if prediction == 1 else "<=50K"
    st.success(f"💰 Predicted Income: {result}")
