# app.py

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy data for initial testing
recipes = [
    {"id": 1, "title": "Paneer Butter Masala", "ingredients": ["paneer", "tomatoes", "cream", "butter", "spices"], "instructions": "Cook paneer in a rich and creamy tomato-based curry."},
    {"id": 2, "title": "Chocolate Cake", "ingredients": ["flour", "sugar", "cocoa powder"], "instructions": "Mix ingredients and bake in the oven."},
]

# Home page - display all recipes
@app.route('/')
def home():
    return render_template('index.html', recipes=recipes)

# Recipe details page
@app.route('/recipe/<int:recipe_id>')
def recipe_details(recipe_id):
    recipe = next((r for r in recipes if r["id"] == recipe_id), None)
    if recipe:
        return render_template('recipe_details.html', recipe=recipe)
    else:
        return "Recipe not found."

# Form to add a new recipe
@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'POST':
        title = request.form['title']
        ingredients = request.form['ingredients'].split(',')
        instructions = request.form['instructions']

        new_recipe = {
            "id": len(recipes) + 1,
            "title": title,
            "ingredients": ingredients,
            "instructions": instructions
        }

        recipes.append(new_recipe)
        return redirect(url_for('home'))

    return render_template('add_recipe.html')

if __name__ == '__main__':
    app.run(debug=True)
