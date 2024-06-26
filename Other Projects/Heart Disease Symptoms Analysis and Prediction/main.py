import streamlit as st
import joblib
import numpy as np
import glob 
st.set_page_config(layout="wide")
# Function to predict Parkinson's disease
def predict_Heart_Disease(features):
    # Load the trained machine learning model
    model = joblib.load('heart_disease_model.pkl')
    # Convert input features to a numpy array and reshape it
    features_array = np.array(features).reshape(1, -1)
    # Make prediction
    prediction = model.predict(features_array)
    # Return prediction
    return int(prediction[0])

def home_page():
    # Add header
    st.title('Heart Disease Prediction')
    st.write('Welcome to our Heart disease prediction app.')
    st.write("The heart disease prediction app utilizes various patient variables to assess the risk of heart disease. These variables include age, chest pain type, blood pressure (BP), cholesterol levels, presence of fasting blood sugar (FBS) over 120 mg/dl, electrocardiogram (EKG) results, maximum heart rate (Max HR), exercise-induced angina, ST depression, slope of ST segment, number of vessels shown by fluoroscopy, thallium stress test results, and gender (Male). The target variable is the presence of heart disease. By analyzing these factors, the app provides insights into the likelihood of a patient having heart disease, aiding in early detection and prevention efforts.")

    # Add instructions
    st.write('Please enter the following parameters to predict Heart disease:')
    
    # Arrange input fields in horizontal lines
    col1, col2, col3 = st.columns(3)
    
    # Input fields for the parameters (arranged in columns)
    with col1:       
    	Age = st.number_input('Age', value=0.0)
    	Chest_pain_type = st.number_input('Chest pain type', value=0.0)
    	BP = st.number_input('BP', value=0.0)
    	Cholesterol = st.number_input('Cholesterol', value=0.0)
    	FBS_over_120 = st.number_input('FBS over 120', value=0.0)

    with col2:
    	EKG_results = st.number_input('EKG results', value=0.0)
    	Max_HR = st.number_input('Max HR', value=0.0)
    	Exercise_angina = st.number_input('Exercise angina', value=0.0)
    	ST_depression = st.number_input('ST depression', value=0.0)
    	Slope_of_ST = st.number_input('Slope of ST', value=0.0)
    
    with col3:
    	Number_of_vessels_fluro = st.number_input('Number of vessels fluro', value=0.0)
    	Thallium = st.number_input('Thallium', value=0.0)
    	Sex_Male = st.number_input('Sex_Male', value=0.0)

    
    # Predict button
    if st.button('Predict'):
        # Gather input features
        features_array = [Age, Chest_pain_type, BP, Cholesterol, FBS_over_120, EKG_results, Max_HR, Exercise_angina, ST_depression, Slope_of_ST, Number_of_vessels_fluro, Thallium, Sex_Male]        
        # Predict Heart disease
        prediction = predict_Heart_Disease(features_array)
        if prediction == 1:
            st.success('Prediction: Heart disease - Positive')
        else:
            st.success('Prediction: Heart disease - Negative')

def function_data_science_lifecycle_page():
   
    page_selection = st.sidebar.radio("Go to", [i.replace(".html", "") for i in glob.glob("*.html")])

    with open(page_selection + ".html", "r") as f:
            html_content = f.read()
    st.components.v1.html(html_content, width=1000, height=1000000, scrolling=True)


def function_sql_server_queries_page():
    st.title('SQL Server Code for Analysis Using SQL Queries')

    # Read SQL code from .sql file
    with open('SQL Server Queries for Data Analysis.sql', 'r') as file:
        sql_code = file.read()
    
    st.code(sql_code, language='sql')


def function_power_bi_dashboard_page():
    st.title('Power-Bi Dashboard Analysis')
    # Display PNG file
    image = open("Dashoboard Pic.png", "rb").read()
    st.image(image, caption='Power-Bi Dashboard', use_column_width=True)

def main():
    st.sidebar.title('Navigation')
    page_selection = st.sidebar.radio("Go to", ["Home", "Data Science Lifecycle", "SQL Server Queries", "Power-Bi Dashboard"])

    if page_selection == "Home":
        home_page()
    elif page_selection == "Data Science Lifecycle":
        function_data_science_lifecycle_page()
    elif page_selection == "SQL Server Queries":
        function_sql_server_queries_page()
    elif page_selection == "Power-Bi Dashboard":
        function_power_bi_dashboard_page()

if __name__ == '__main__':
    main()