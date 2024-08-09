import streamlit as st

# Streamlit app
st.title('Diabetes Prediction Model')
st.write("By Bonny_Makuwa")

st.write("""
## Project Description
This diabetes prediction model is developed to evaluate the likelihood of diabetes based on various health parameters. It uses commonly recognized thresholds to assess risk levels and provide insights based on user inputs.
""")

st.write("### Creator Information")

# Display author details and image
col1, col2 = st.columns([1, 3])  # Create two columns with different widths

with col1:
    # Adjust the path if necessary
    st.image("C:/Users/bonnym/OneDrive - Small Enterprise Finance Agency/Documents/WP/Models/Diabetes/Bonny (2).jpg", width=150)  # Adjust the width as needed

with col2:
    st.write("**Name:** Bonny Makuwa")
    st.write("**Bio:** Focusing on predictive modeling and data analysis. Proficient in Power BI, Python, SQL, and machine learning techniques. Experienced in creating and optimizing models to drive insights and enhance decision-making processes.")
    st.write("**LinkedIn:** [Bonny Makuwa LinkedIn](https://www.linkedin.com/in/bonny-makuwa-04a8b6153/)")
    st.write("**GitHub:** [Bonny Makuwa GitHub](https://github.com/Bonnymakuwa)")
    st.write("**Email:** [Bonny Makuwa Email](mailto:bonnymakuwa@gmail.com)")

# User input
age = st.slider('**Age**', 0, 120, 30)
sex = st.selectbox('**Sex**', ['Female', 'Male'])
blood_glucose = st.slider('**Blood Glucose Level (mg/dl)**', 0, 300, 100)
body_mass_index = st.slider('**Body Mass Index (BMI)**', 0, 50, 25)
family_history = st.selectbox('**Family History of Diabetes**', ['No', 'Yes'])
physical_activity = st.selectbox('**Physical Activity**', ['Regular Exercise', 'Sedentary Lifestyle'])
diet = st.selectbox('**Diet**', ['Healthy Diet', 'High-Sugar/High-Fat Diet'])
blood_pressure = st.slider('**Blood Pressure (mm Hg)**', 0, 200, 120)
cholesterol = st.slider('**Cholesterol (mg/dl)**', 0, 600, 200)

# Prediction logic
def predict_diabetes(age, sex, blood_glucose, body_mass_index, family_history, physical_activity, diet, blood_pressure, cholesterol):
    risk_score = 0
    
    # Age
    if age >= 65:
        risk_score += 2
    elif age >= 45:
        risk_score += 1
    
    # Sex
    if sex == 'Male':
        risk_score += 1
    
    # Blood Glucose Level
    if blood_glucose >= 126:
        risk_score += 3
    elif blood_glucose >= 100:
        risk_score += 2
    
    # Body Mass Index (BMI)
    if body_mass_index >= 30:
        risk_score += 3
    elif body_mass_index >= 25:
        risk_score += 2
    
    # Family History
    if family_history == 'Yes':
        risk_score += 2
    
    # Physical Activity
    if physical_activity == 'Sedentary Lifestyle':
        risk_score += 2
    
    # Diet
    if diet == 'High-Sugar/High-Fat Diet':
        risk_score += 2
    
    # Blood Pressure
    if blood_pressure >= 130:
        risk_score += 2
    
    # Cholesterol
    if cholesterol >= 240:
        risk_score += 2
    elif cholesterol >= 200:
        risk_score += 1
    
    # Risk assessment based on score
    if risk_score >= 12:
        return "High risk of diabetes"
    elif risk_score >= 6:
        return "Moderate risk of diabetes"
    else:
        return "Low risk of diabetes"

# Predict diabetes
prediction = predict_diabetes(
    age,
    sex,
    blood_glucose,
    body_mass_index,
    family_history,
    physical_activity,
    diet,
    blood_pressure,
    cholesterol
)

# Display results with increased emphasis
st.markdown(f"""
### **Prediction**
**{prediction}**
""", unsafe_allow_html=True)
