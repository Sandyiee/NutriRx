import streamlit as st

def app():
    # About Us
    st.header("About :violet[NutriRx]")
    st.write("""    
    NutriRx is developed by a team of nutrition experts dedicated to promoting healthy eating habits and managing dietary needs effectively. 
    Our mission is to empower individuals to make informed choices about their diet and nutrition.
    """)

    # Testimonials
    st.header("Testimonials")
    st.write("""
    "I've been using NutriRx for a month now, and it's helped me manage my diabetes with personalized meal plans and nutritional guidance." - Sarah
    """)

    # Call-to-Action
    st.write("Ready to get started?")
    st.button("Get Started")

    # Contact Us
    st.header("Contact :violet[NutriRx]")
    st.write("Have questions or feedback? Reach out to us at [contact@nutrirx.com](mailto:contact@nutrirx.com)")

    # Footer
    st.write("© 2024 NutriRx. All rights reserved.")

if __name__ == "__main__":
    app()

