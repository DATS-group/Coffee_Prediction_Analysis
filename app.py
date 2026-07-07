
from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    features = [

        float(request.form["year"]),
        float(request.form["average_kenyan_coffee_price_usd"]),
        float(request.form["average_foreign_coffee_price_usd"]),
        float(request.form["current_total_factor_productivity"]),
        float(request.form["germany_import_coffee_price_usd"]),
        float(request.form["belgium_import_coffee_price_usd"]),
        float(request.form["united_states_import_coffee_price_usd"]),
        float(request.form["south_korea_import_coffee_price_usd"]),
        float(request.form["annual_coffee_production"]),
        float(request.form["annual_exportable_coffee"]),
        float(request.form["real_exchange_rate_percent"]),
        float(request.form["nominal_exchange_rate_percent"]),
        float(request.form["average_agricultural_price"]),
        float(request.form["total_annual_imports"]),
        float(request.form["total_annual_exports"]),
        float(request.form["real_gdp_growth_percent"]),
        float(request.form["gross_capital_formation_percent"]),
        float(request.form["population_growth_rate_percent"]),
        float(request.form["real_interest_rate_percent"]),
        float(request.form["natural_resource_endowment"])

    ]

    data = pd.DataFrame([features])

    data = scaler.transform(data)

    prediction = model.predict(data)[0]

    return render_template(
        "index.html",
        prediction=round(prediction,2)
    )


if __name__ == "__main__":
    app.run(debug=True)