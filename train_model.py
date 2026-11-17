from pathlib import Path

import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

PROJECT_DIR = Path(__file__).resolve().parent
data = pd.read_csv(PROJECT_DIR / "students.csv")

X = data[["study_hours", "previous_marks", "attendance"]]
y = data["final_marks"]

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, PROJECT_DIR / "student_model.pkl")

print("ML Model trained successfully!")
print("Model saved as student_model.pkl")
