import joblib
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

# ======================================
# LOAD DATASET
# ======================================

df = pd.read_csv("backend/ml/interview_training_dataset.csv")

X = df[["fluency", "correctness", "eye_contact", "posture", "head_stability"]]

y = df["readiness"]

# ======================================
# TRAIN TEST SPLIT
# ======================================

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ======================================
# LOAD MODEL
# ======================================

model = joblib.load("backend/ml/readiness_model.pkl")

predictions = model.predict(X_test)

# ======================================
# PLOT
# ======================================

plt.figure(figsize=(7, 7))

plt.scatter(y_test, predictions, alpha=0.7)

plt.plot([0, 100], [0, 100], color="red", linestyle="--")

plt.xlabel("Actual Readiness Score")

plt.ylabel("Predicted Readiness Score")

plt.title("Actual vs Predicted")

plt.tight_layout()

plt.savefig("backend/ml/actual_vs_predicted.png", dpi=300)

plt.show()

print("Graph Saved Successfully!")
