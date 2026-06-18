import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

from xgboost import XGBRegressor

# ==========================================
# LOAD DATA
# ==========================================

df = pd.read_csv("data/raw/interview_dataset.csv")

print("\nDataset Shape:")
print(df.shape)

# ==========================================
# FEATURES & TARGET
# ==========================================

X = df[
    [
        "correctness",
        "eye_contact",
        "posture",
        "fluency",
        "speech_rate",
        "pause_count",
        "filler_count",
        "smile_score",
        "head_stability",
    ]
]

y = df["confidence_label"]

# ==========================================
# TRAIN TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ==========================================
# MODEL
# ==========================================

model = XGBRegressor(n_estimators=200, learning_rate=0.05, max_depth=6, random_state=42)

# ==========================================
# TRAIN
# ==========================================

model.fit(X_train, y_train)

# ==========================================
# PREDICTION
# ==========================================

predictions = model.predict(X_test)

# ==========================================
# EVALUATION
# ==========================================

mae = mean_absolute_error(y_test, predictions)

mse = mean_squared_error(y_test, predictions)

rmse = mse**0.5

r2 = r2_score(y_test, predictions)

print("\nModel Evaluation")
print("-" * 30)

print(f"MAE  : {mae:.2f}")

print(f"RMSE : {rmse:.2f}")

print(f"R2   : {r2:.4f}")

# ==========================================
# SAVE MODEL
# ==========================================

joblib.dump(model, "models/confidence_model.pkl")

print("\nModel saved successfully!")
