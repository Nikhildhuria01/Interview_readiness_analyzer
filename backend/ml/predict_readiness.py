import joblib

model = joblib.load("backend/ml/readiness_model.pkl")


def predict_readiness(fluency, correctness, eye_contact, posture, head_stability):

    prediction = model.predict(
        [[fluency, correctness, eye_contact, posture, head_stability]]
    )

    return float(round(prediction[0],2))

if __name__ == "__main__":

    score = predict_readiness(85, 90, 88, 82, 84)

    print(f"Predicted Readiness Score: {score}")


def get_readiness_status(score):

    if score >= 90:

        return "Interview Ready"

    elif score >= 75:

        return "Almost Ready"

    elif score >= 60:

        return "Needs Improvement"

    else:

        return "Needs Significant Practice"
