from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    recipe_name = None
    recipe_instructions = None

    if request.method == "POST":
        ingredients = request.form["ingredients"]

        # sample output
        recipe_name = "Egg Fried Rice"
        recipe_instructions = "Cook rice and mix with egg."

    return render_template(
        "index.html",
        recipe_name=recipe_name,
        recipe_instructions=recipe_instructions
    )

if __name__ == "__main__":
    app.run(debug=True)
