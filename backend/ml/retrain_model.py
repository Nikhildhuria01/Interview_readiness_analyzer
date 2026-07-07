import pandas as pd
import joblib

from xgboost import XGBRegressor

DATASET = "ml/real_interview_dataset.csv"

MODEL_PATH = "ml/readiness_model.pkl"


def retrain_model():

    print("Loading interview dataset...")

    df = pd.read_csv(DATASET)

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

    model = XGBRegressor(
        n_estimators=200, learning_rate=0.05, max_depth=5, random_state=42
    )

    model.fit(X, y)

    joblib.dump(model, MODEL_PATH)

    print("Model retrained successfully!")

    print("\nFeature Importance:\n")

    features = X.columns

    importance = model.feature_importances_

    for feature, score in zip(features, importance):

        print(f"{feature:20} {score:.3f}")


if __name__ == "__main__":

    retrain_model()
