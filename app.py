import streamlit as st
import pandas as pd

# Streamlit app configuration
st.set_page_config(page_title="NutriChef")
st.title("NutriChef")

# Sidebar for user selections
st.sidebar.header("Filter Recipes")

# Define diets and sort them alphabetically
selected_diets = st.sidebar.multiselect("Select your diets", sorted([
    "Dairy Free", "Gluten Free", "Keto Recipes", "Low Carb", "Paleo", "Vegetarian",
    "Low Sodium", "Vegan", "Low-Fat", "High Fiber", "Low-Cholesterol", "Heart-Healthy"
]))

# Define additional filters
selected_prep = st.sidebar.multiselect("Select Preparation Type", [
    "Kid Friendly", "Meal Prep Recipes", "Slow Cooker Recipes", "Under 30 Minutes", "Whole 30 Recipes", "Air Fryer Recipes"
])

# Define meals filter
selected_meals = st.sidebar.multiselect("Select Meal Type", [
    "Breakfast", "Brunch", "Lunch", "Dinner", "Snack", "Main Dish", "Side Dish", "Appetizer", "Soup"
])

# User input for available ingredients
user_query = st.sidebar.text_input("Type your INGREDIENTS or desired DISH here...")

st.sidebar.markdown("**⚠️ Remember to separate your ingredients with a comma!**")


# Function to filter recipes from the CSV
def filter_recipes(data, user_query, selected_diets, selected_prep, selected_meals):
    filtered_data = data.copy()

    # Filter by ingredients
    if user_query:
        ingredients = [ingredient.strip().lower() for ingredient in user_query.split(',')]
        filtered_data = filtered_data[filtered_data['ingredients'].apply(
            lambda x: all(ingredient in x.lower() for ingredient in ingredients)
        )]

    # Filter by diets (assuming diets are part of the tags column)
    if selected_diets:
        filtered_data = filtered_data[filtered_data['tags'].apply(
            lambda x: any(diet.lower() in x.lower() for diet in selected_diets if pd.notna(x))
        )]

    # Filter by additional filters
    if selected_prep:
        filtered_data = filtered_data[filtered_data['tags'].apply(
            lambda x: any(prep.lower() in x.lower() for prep in selected_prep if pd.notna(x))
        )]

    # Filter by meal type
    if selected_meals:
        filtered_data = filtered_data[filtered_data['tags'].apply(
            lambda x: any(meal.lower() in x.lower() for meal in selected_meals if pd.notna(x))
        )]

    return filtered_data

# Load the CSV file
@st.cache_data
def load_data():
    data = pd.read_csv('recipes_82k.csv')
    return data

data = load_data()

# Process user input and generate response on button click
if st.sidebar.button("Generate Recipe"):
    if user_query or selected_diets or selected_prep or selected_meals:
        filtered_recipes = filter_recipes(data, user_query, selected_diets, selected_prep, selected_meals)
        if not filtered_recipes.empty:
            st.header("Recipes")
            for _, recipe in filtered_recipes.iterrows():
                st.subheader(recipe['recipe_name'])
                if pd.isna(recipe['cuisine']) or not recipe['cuisine']:
                    continue
                st.write("Cuisine:", ', '.join(eval(recipe['cuisine'])))
                st.write("Prep Time:", recipe['prep_time'])
                st.write("Serves:", recipe['serves'])
                st.write("Tags:", recipe['tags'] if pd.notna(recipe['tags']) else "None")
                st.write("Cooking Method:")
                cooking_method = ' '.join(eval(recipe['cooking_method'])).replace('.', '.\n')
                st.write(cooking_method)
                st.write("Ingredients:")
                ingredients = ', '.join(eval(recipe['ingredients'])).replace(', ', ',\n')
                st.write(ingredients)
                st.image(recipe['image'], caption='Meal Image', use_column_width=True)
        else:
            st.write("No recipes found matching your criteria.")
    else:
        st.write("Please enter ingredients or select diets/filters to filter recipes.")
else:
    st.write("Click 'Generate Recipe' to search for recipes.")
