import streamlit as st
import numpy as np
import pandas as pd
import chardet
import Levenshtein

def app():
    # Detect encoding of the CSV files
    with open(r"D:/projects/NutriRx/diseases_dataset.csv", 'rb') as f:
        encoding_diseases = chardet.detect(f.read())['encoding']

    with open(r"D:/projects/NutriRx/food_calories.csv", 'rb') as f:
        encoding_food = chardet.detect(f.read())['encoding']

    # Load datasets with the detected encodings
    df = pd.read_csv(r"D:/projects/NutriRx/diseases_dataset.csv", encoding=encoding_diseases)
    df1 = pd.read_csv(r"D:/projects/NutriRx/food_calories.csv", encoding=encoding_food)

    def get_recommendation(disease_name, meal_time):
        days = np.random.choice(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']).split(',')

        try:
            filtered_df = df[df['Name of the Disease'] == disease_name]
            recommendations = filtered_df[meal_time][filtered_df['Days'].apply(lambda x: any(i in x for i in days))].tolist()
            caloric_intake = filtered_df['Caloric_intake_for_adult'].iloc[0]
            recommended0 = recommendations[0].split(',')
            recommended1=[]
            for i in range(len(recommended0)):
                recommended1.append(str(i+1)+': '+recommended0[i])

            return f'Recommended meal: {recommended1}. Caloric intake recommendation: {caloric_intake} kcal/day.'
        except IndexError:
            return f"No recommendation found for {disease_name}, {meal_time}, or {', '.join(days)}. Caloric intake recommendation: N/A kcal."

    def calculate_total_calories(food_choices):
        selected_indices = [int(idx) - 1 for idx in food_choices.split(',') if idx.strip()]

        if not food_choices or not all(0 <= idx < len(df1) for idx in selected_indices):
            return "Please enter valid food choices."

        total_calories = sum(df1['Total Calories'].iloc[idx] for idx in selected_indices)
        return f"Total Calories for selected foods: {total_calories}"

    # Create Streamlit app
    st.title(":violet[NutriRx] Recommendation System")

    # Disease and meal options from dataset
    disease_options = df['Name of the Disease'].unique().tolist()
    meal_options = df.columns[1:].tolist()

    # Meal Recommendation
    st.header(" :green[Meal] Recommendation")
    disease_name = st.selectbox("Select disease:", disease_options)
    meal_time = st.selectbox("Select mealtime:", meal_options)
    if st.button("Get Recommendation"):
        recommendation = get_recommendation(disease_name, meal_time)
        st.write(recommendation)

    # Food Calories
    st.header(" :green[Food] Calories")
    food_choices = st.text_input("Enter the numbers corresponding to your choices (separated by commas):")
    if st.button("Calculate Total Calories"):
        total_calories_result = calculate_total_calories(food_choices)
        st.write(total_calories_result)

if __name__ == "__main__":
    app()

