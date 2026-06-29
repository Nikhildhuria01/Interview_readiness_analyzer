import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

from xgboost import XGBRegressor

import joblib

# =====================
# LOAD DATASET
# =====================

df = pd.read_csv("backend/ml/interview_dataset.csv")

# =====================
# FEATURES
# =====================

X = df[["fluency", "correctness", "eye_contact", "posture", "head_stability"]]

y = df["readiness_score"]

# =====================
# TRAIN TEST SPLIT
# =====================

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# =====================
# MODEL
# =====================

model = XGBRegressor(n_estimators=100, learning_rate=0.1, max_depth=5, random_state=42)

# =====================
# TRAIN
# =====================

model.fit(X_train, y_train)

# =====================
# PREDICT
# =====================

predictions = model.predict(X_test)

# =====================
# EVALUATION
# =====================

mae = mean_absolute_error(y_test, predictions)

mse = mean_squared_error(y_test, predictions)

r2 = r2_score(y_test, predictions)

print("\nMODEL EVALUATION")

print(f"MAE: {mae:.2f}")

print(f"MSE: {mse:.2f}")

print(f"R2 Score: {r2:.4f}")

# =====================
# SAVE MODEL
# =====================

joblib.dump(model, "backend/ml/readiness_model.pkl")

print("\nModel Saved Successfully!")
