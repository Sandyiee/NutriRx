import streamlit as st
from PIL import Image

def app():
    # Header
    st.title("Welcom to :violet[NutriRx]")
    st.markdown("---")
    st.write("Your Personalized Food Recommender System")

    # Hero Section
    image = Image.open(r"D:/projects/NutriRx/images/pic1.jpg")  # Adjust the file path accordingly
    st.image(image, caption='NutriRx', use_column_width=True)

    # Features or Services
    st.header("How It :green[ Works]")
    st.write("""
    - **Personalized Meal Plans:** Based on specific diseases or health conditions.
    - **Nutritional Analysis:** Get insights into recommended foods.
    - **Easy-to-Use Interface:** Manage dietary preferences and restrictions effortlessly.
    """)

    # How It Works
    st.header("How It :green[ Works]")
    st.write("""
    1. **Sign Up or Log In:** Create your NutriRx account.
    2. **Provide Information:** Share your health profile and dietary preferences.
    3. **Receive Recommendations:** Get personalized food recommendations.
    4. **Explore Resources:** Access meal plans, and nutritional information.
    5. **BMI report:** To view the BMI report
    """)

if __name__ == "__main__":
    app()
