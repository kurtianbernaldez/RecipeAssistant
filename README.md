# README

<h1>Recipe Assistant</h1>
<h2>Overview</h2>
Recipe Assistant is a Streamlit application that helps users find recipes based on their dietary preferences, preparation methods, meal types, and available ingredients. Users can filter recipes using various criteria and view detailed cooking instructions and ingredients.

<h2>Features</h2>
<h4>Filter by Diet:</h4> Select from a variety of diets such as Dairy Free, Gluten Free, Keto Recipes, Vegan, and more.
<h4>Filter by Preparation Type:</h4> Choose recipes that are Kid Friendly, suitable for Meal Prep, Slow Cooker Recipes, Under 30 Minutes, and more.
<h4>Filter by Meal Type:</h4> Find recipes for Breakfast, Brunch, Lunch, Dinner, Snacks, Main Dishes, Side Dishes, Appetizers, and Soups.
<h4>Ingredient-based Search:</h4> Enter available ingredients to find recipes that can be made with what you have.
<h4>Detailed Recipe Information:</h4> View cuisine type, preparation time, servings, tags, cooking method, and ingredients.
<h4>Images:</h4> Visualize the recipes with accompanying images.


<h2>Getting Started</h2>
<h3>Prerequisites</h3>
Python 3.x <br/>
Streamlit <br/>
Pandas

<h2>Installation</h2>
<h4>Clone the repository:</h4>
git clone https://github.com/yourusername/recipe-assistant.git <br/>
cd recipe-assistant

<h4>Create and activate a virtual environment (optional but recommended):</h4>
python -m venv venv <br/>
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

<h4>Install the required packages:</h4>
pip install -r requirements.txt

<h4>Download the dataset:</h4>
Go to Kaggle - Recipe Dataset <br/>
Download the recipes_82k.csv file. <br/>
Place the recipes_82k.csv file in the project directory.

<h2>Running the App</h2>
streamlit run app.py

<h2>Usage</h2>
Select your dietary preferences from the sidebar. <br/>
Choose preparation methods and meal types. <br/>
Enter the main ingredients you have available. <br/>
Click "Generate Recipe" to find recipes that match your criteria. <br/>
View the detailed recipe information including cooking steps and ingredients.
