#README#

<h1>Recipe Assistant</h1>
<h2>Overview</h2>
Recipe Assistant is a Streamlit application that helps users find recipes based on their dietary preferences, preparation methods, meal types, and available ingredients. Users can filter recipes using various criteria and view detailed cooking instructions and ingredients.

<h2>Features</h2>
<h6>Filter by Diet:</h6> Select from a variety of diets such as Dairy Free, Gluten Free, Keto Recipes, Vegan, and more.
<h6>Filter by Preparation Type:</h6> Choose recipes that are Kid Friendly, suitable for Meal Prep, Slow Cooker Recipes, Under 30 Minutes, and more.
<h6>Filter by Meal Type:</h6> Find recipes for Breakfast, Brunch, Lunch, Dinner, Snacks, Main Dishes, Side Dishes, Appetizers, and Soups.
<h6>Ingredient-based Search:</h6> Enter available ingredients to find recipes that can be made with what you have.
<h6>Detailed Recipe Information:</h6> View cuisine type, preparation time, servings, tags, cooking method, and ingredients.
<h6>Images:</h6> Visualize the recipes with accompanying images.


<h2>Getting Started</h2>
<h3>Prerequisites</h3>
Python 3.x
Streamlit
Pandas

<h2>Installation</h2>
<h6>Clone the repository:</h6>
git clone https://github.com/yourusername/recipe-assistant.git
cd recipe-assistant

<h6>Create and activate a virtual environment (optional but recommended):</h6>
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

<h6>Install the required packages:</h6>
pip install -r requirements.txt

<h6>Download the dataset:</h6>
Go to Kaggle - Recipe Dataset
Download the recipes_82k.csv file.
Place the recipes_82k.csv file in the project directory.

<h2>Running the App</h2>
streamlit run app.py

<h2>Usage</h2>
Select your dietary preferences from the sidebar.
Choose preparation methods and meal types.
Enter the main ingredients you have available.
Click "Generate Recipe" to find recipes that match your criteria.
View the detailed recipe information including cooking steps and ingredients.
