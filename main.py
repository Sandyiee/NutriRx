import streamlit as st
from streamlit_option_menu import option_menu
import BMI, Home, meal_recommendation,account,about

st.set_page_config(
    page_title="NutriRx",
    page_icon="🥗",
)

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })

    def run(self):
        with st.sidebar:
            app = option_menu(
                menu_title="NutriRx",
                options=["Home","Account", "BMI", "Meal Recommendation","About"],
                icons=["house-fill", "person-circle", "chat-fill","trophy-fill","info-circle-fill"],
                menu_icon="chat-text-fill",
                default_index=1,
                styles={
                    "container": {"padding": "5px", "background-color":"black"},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left","margin":"0px"},
                    "nav-link-selected": {"background-color": "#02ab21"}
                }
            )
        if app == "Home":
            Home.app()
        elif app == "BMI":
            BMI.app()
        elif app == "Meal Recommendation":
            meal_recommendation.app()
        elif app == "Account":
            account.app()
        elif app == "About":
            about.app()
    
if __name__ == "__main__":
    multi_app = MultiApp()
    multi_app.run()





