import streamlit as st

def calculate_bmi(age, weight, height):
    try:
        age = int(age)
        weight = float(weight)
        height = float(height)
    except ValueError:
        return "Please enter valid numeric values for age, weight, and height."

    bmi = weight / (height ** 2)

    if bmi < 18.5:
        bmi_level = "Underweight"
    elif 18.5 <= bmi < 25:
        bmi_level = "Normal weight"
    elif 25 <= bmi < 30:
        bmi_level = "Overweight"
    else:
        bmi_level = "Obese"
        

    return f"Your BMI is {bmi:.2f}, which is classified as {bmi_level}."

def app():
    st.title(":violet[NutriRx] BMI Analysis ")
    # Get user's name
    user_name = st.text_input("Enter your name:")

    # Get user's age, weight, and height
    age = st.number_input("Enter your age:", min_value=0, max_value=150, step=1, value=30)
    weight = st.number_input("Enter your weight (kg):", min_value=0.0, max_value=1000.0, step=0.1)
    height = st.number_input("Enter your height (m):", min_value=0.1, max_value=3.0, step=0.01)

    # Calculate BMI
    bmi_report = calculate_bmi(age, weight, height)

    # Display BMI report in a popup menu
    if st.button("Show BMI Report"):
        st.success(f"Hello {user_name}, {bmi_report}")

if __name__ == "__main__":
    app()
