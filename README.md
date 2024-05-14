Recipe Assistant
Overview
Recipe Assistant is a Streamlit application that helps users find recipes based on their dietary preferences, preparation methods, meal types, and available ingredients. Users can filter recipes using various criteria and view detailed cooking instructions and ingredients.

Features
Filter by Diet: Select from a variety of diets such as Dairy Free, Gluten Free, Keto Recipes, Vegan, and more.
Filter by Preparation Type: Choose recipes that are Kid Friendly, suitable for Meal Prep, Slow Cooker Recipes, Under 30 Minutes, and more.
Filter by Meal Type: Find recipes for Breakfast, Brunch, Lunch, Dinner, Snacks, Main Dishes, Side Dishes, Appetizers, and Soups.
Ingredient-based Search: Enter available ingredients to find recipes that can be made with what you have.
Detailed Recipe Information: View cuisine type, preparation time, servings, tags, cooking method, and ingredients.
Images: Visualize the recipes with accompanying images.


Getting Started

Prerequisites
Python 3.x
Streamlit
Pandas

Installation
Clone the repository:

git clone https://github.com/yourusername/recipe-assistant.git
cd recipe-assistant
Create and activate a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the required packages:

pip install -r requirements.txt
Download the dataset:


Go to Kaggle - Recipe Dataset
Download the recipes_82k.csv file.
Place the recipes_82k.csv file in the project directory.

Running the App

streamlit run app.py
Usage
Select your dietary preferences from the sidebar.
Choose preparation methods and meal types.
Enter the main ingredients you have available.
Click "Generate Recipe" to find recipes that match your criteria.
View the detailed recipe information including cooking steps and ingredients.
