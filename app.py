from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load dataset
data = pd.read_csv("recipes.csv")

def recommend_recipes(user_ingredients):
    results = []

    for index, row in data.iterrows():
        recipe_ingredients = row['ingredients'].lower().split(",")

        match_count = sum(
            1 for ingredient in user_ingredients
            if ingredient in recipe_ingredients
        )

        if match_count > 0:
            results.append({
                "recipe": row['recipe'],
                "instructions": row['instructions'],
                "score": match_count
            })

    results = sorted(results, key=lambda x: x['score'], reverse=True)
    return results


@app.route("/", methods=["GET", "POST"])
def home():
    recipes = []

    if request.method == "POST":
        ingredients = request.form["ingredients"]
        user_ingredients = [
            i.strip().lower() for i in ingredients.split(",")
        ]
        recipes = recommend_recipes(user_ingredients)

    return render_template("index.html", recipes=recipes)


if __name__ == "__main__":
    app.run(debug=True)
