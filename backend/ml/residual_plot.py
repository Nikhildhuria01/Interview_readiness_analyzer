import joblib
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

# =====================================
# LOAD DATA
# =====================================

df = pd.read_csv(
    "backend/ml/interview_training_dataset.csv"
)

X = df[
    [
        "fluency",
        "correctness",
        "eye_contact",
        "posture",
        "head_stability"
    ]
]

y = df["readiness"]

# =====================================
# SPLIT
# =====================================

X_train, X_test, y_train, y_test = train_test_split(

    X,

    y,

    test_size=0.2,

    random_state=42

)

# =====================================
# LOAD MODEL
# =====================================

model = joblib.load(
    "backend/ml/readiness_model.pkl"
)

predictions = model.predict(X_test)

# =====================================
# RESIDUALS
# =====================================

residuals = y_test - predictions

# =====================================
# PLOT
# =====================================

plt.figure(figsize=(8,5))

plt.scatter(

    predictions,

    residuals,

    alpha=0.7

)

plt.axhline(

    y=0,

    color="red",

    linestyle="--"

)

plt.xlabel(

    "Predicted Readiness Score"

)

plt.ylabel(

    "Residual Error"

)

plt.title(

    "Residual Plot"

)

plt.tight_layout()

plt.savefig(

    "backend/ml/residual_plot.png",

    dpi=300

)

plt.show()

print("Residual Plot Saved!")