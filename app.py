import math
from pathlib import Path

from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load(Path(__file__).resolve().parent / "student_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if not request.is_json:
        return jsonify({"error": "Request must use application/json."}), 415

    data = request.get_json()
    if not isinstance(data, dict):
        return jsonify({"error": "Request body must be a JSON object."}), 400

    features = {}
    limits = {"hours": (0, 24), "marks": (0, 100), "attendance": (0, 100)}
    for field, (minimum, maximum) in limits.items():
        try:
            value = float(data[field])
        except (KeyError, TypeError, ValueError):
            return jsonify({"error": f"{field} must be a number."}), 400

        if not math.isfinite(value) or not minimum <= value <= maximum:
            return jsonify({"error": f"{field} must be between {minimum} and {maximum}."}), 400
        features[field] = value

    model_input = pd.DataFrame([{
        "study_hours": features["hours"],
        "previous_marks": features["marks"],
        "attendance": features["attendance"],
    }])
    prediction = model.predict(model_input)[0]

    predicted_marks = max(0, min(100, prediction))
    predicted_marks = round(predicted_marks, 2)

    if predicted_marks >= 75:
        result = "Excellent"
    elif predicted_marks >= 40:
        result = "Average"
    else:
        result = "Needs Improvement"

    return jsonify({
        "predicted_marks": predicted_marks,
        "performance": result
    })

if __name__ == "__main__":
    app.run()