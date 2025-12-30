from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def bmi():
    bmi = None
    category = None
    color = None
    message = None
    ideal_weight = None

    if request.method == "POST":
        try:
            weight = float(request.form["weight"])
            height_cm = float(request.form["height"])

            height_m = height_cm / 100
            bmi = round(weight / (height_m ** 2), 2)

            min_weight = round(18.5 * (height_m ** 2), 1)
            max_weight = round(24.9 * (height_m ** 2), 1)
            ideal_weight = f"{min_weight} kg – {max_weight} kg"

            if bmi < 18.5:
                category = "Underweight"
                color = "blue"
                message = "You should increase calorie intake 🍽️"
            elif bmi < 25:
                category = "Normal weight"
                color = "green"
                message = "Great! Maintain your healthy lifestyle 💪"
            elif bmi < 30:
                category = "Overweight"
                color = "orange"
                message = "Regular exercise is recommended 🏃"
            else:
                category = "Obese"
                color = "red"
                message = "Consult a healthcare professional 🏥"

        except:
            message = "Invalid input!"

    return render_template(
        "index.html",
        bmi=bmi,
        category=category,
        color=color,
        message=message,
        ideal_weight=ideal_weight
    )

if __name__ == "__main__":
    app.run(debug=True)
