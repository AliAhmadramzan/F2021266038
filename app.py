import streamlit as st
import pickle
import numpy as np

# Load the trained SVM model
with open("svm_model.pkl", "rb") as model_file:
    svm_model = pickle.load(model_file)

# Function to make prediction
def predict_purchase(gender, age, salary):
    # Encode gender: Male = 1, Female = 0
    gender_encoded = 1 if gender == 'Male' else 0

    # Create the input array for prediction
    input_data = np.array([[gender_encoded, age, salary]])
    
    # Predict using the SVM model
    prediction = svm_model.predict(input_data)
    
    # Convert prediction to label
    if prediction == 1:
        return "Yes"
    else:
        return "No"

# Apply custom background style
st.markdown(
    """
    <style>
    body {
        background-color: #f0f0f0; /* Light grey background */
    }
    .main-heading {
        color: #333333;
        font-size: 40px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 30px;
    }
    .input-container {
        background-color: #ffffff; /* White card background */
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Main heading
st.markdown('<div class="main-heading">Purchase Prediction App</div>', unsafe_allow_html=True)

# Input container
with st.container():
    st.markdown('<div class="input-container">', unsafe_allow_html=True)

    # Input fields arranged in a row
    col1, col2, col3 = st.columns(3)
    
    with col1:
        gender = st.selectbox("Gender", ["Male", "Female"])
    with col2:
        age = st.number_input("Age", min_value=0, max_value=100, step=1)
    with col3:
        salary = st.number_input("Salary", min_value=0, step=1000)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Predict button
if st.button("Predict"):
    result = predict_purchase(gender, age, salary)
    st.success(f"Prediction: {result}")
