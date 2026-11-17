from pathlib import Path

import pandas as pd
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import LeaveOneOut, cross_val_predict


PROJECT_DIR = Path(__file__).resolve().parent
data = pd.read_csv(PROJECT_DIR / "students.csv")
features = data[["study_hours", "previous_marks", "attendance"]]
target = data["final_marks"]

models = {
    "Linear regression": LinearRegression(),
    "Mean baseline": DummyRegressor(strategy="mean"),
}

for name, model in models.items():
    predictions = cross_val_predict(model, features, target, cv=LeaveOneOut())
    mae = mean_absolute_error(target, predictions)
    rmse = mean_squared_error(target, predictions) ** 0.5
    r_squared = r2_score(target, predictions)
    print(f"{name}: MAE={mae:.3f}, RMSE={rmse:.3f}, R2={r_squared:.3f}")
