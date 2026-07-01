import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

from xgboost import XGBRegressor

# =====================================
# LOAD DATASET
# =====================================

df = pd.read_csv("backend/ml/interview_training_dataset.csv")

# =====================================
# FEATURES
# =====================================

X = df[
    [
        "fluency",
        "correctness",
        "eye_contact",
        "posture",
        "head_stability",
    ]
]

y = df["readiness"]

# =====================================
# TRAIN TEST SPLIT
# =====================================

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# =====================================
# MODEL
# =====================================

model = XGBRegressor(
    n_estimators=300,
    learning_rate=0.05,
    max_depth=6,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42,
)

print("Training Model...")

model.fit(X_train, y_train)

print("Training Completed!")

# =====================================
# PREDICTIONS
# =====================================

predictions = model.predict(X_test)

# =====================================
# METRICS
# =====================================

mae = mean_absolute_error(y_test, predictions)

mse = mean_squared_error(y_test, predictions)

r2 = r2_score(y_test, predictions)

print("\nMODEL EVALUATION")

print(f"MAE : {mae:.2f}")

print(f"MSE : {mse:.2f}")

print(f"R2 Score : {r2:.4f}")

import json

evaluation = {
    "model": "XGBoost Regressor",
    "dataset_size": len(df),
    "mae": round(mae, 2),
    "mse": round(mse, 2),
    "rmse": round(mse**0.5, 2),
    "r2": round(r2, 4),
    "best_parameters": model.get_params(),
}

with open("backend/ml/model_evaluation.json", "w") as f:

    json.dump(evaluation, f, indent=4)

print("Evaluation JSON Saved!")
# =====================================
# SAVE MODEL
# =====================================

joblib.dump(model, "backend/ml/readiness_model.pkl")

print("\nModel Saved Successfully!")
