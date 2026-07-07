import joblib
import pandas as pd

from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import r2_score
from xgboost import XGBRegressor

# ==============================
# LOAD DATA
# ==============================

df = pd.read_csv("ml/interview_training_dataset.csv")

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

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ==============================
# MODEL
# ==============================

model = XGBRegressor(random_state=42)

# ==============================
# PARAMETERS
# ==============================

params = {
    "n_estimators": [200, 300, 400],
    "learning_rate": [0.03, 0.05, 0.1],
    "max_depth": [4, 5, 6],
    "subsample": [0.8, 1.0],
}

# ==============================
# GRID SEARCH
# ==============================

grid = GridSearchCV(
    estimator=model, param_grid=params, cv=5, scoring="r2", verbose=2, n_jobs=-1
)

print("Searching Best Parameters...\n")

grid.fit(X_train, y_train)

print("\nBest Parameters:")

print(grid.best_params_)

best_model = grid.best_estimator_

pred = best_model.predict(X_test)

print("\nFinal R2 Score:")

print(r2_score(y_test, pred))

joblib.dump(best_model, "ml/readiness_model.pkl")

print("\nOptimized Model Saved!")
