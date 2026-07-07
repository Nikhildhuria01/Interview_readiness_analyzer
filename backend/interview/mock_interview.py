import cv2
import time
import json

from eye_contact_analysis import get_eye_contact_score
from posture_analysis import get_posture_score
from head_stability import get_head_stability_score


def run_camera_interview():

    cap = cv2.VideoCapture(0)

    print("Mock Interview Started...")
    print("Camera will stop automatically after 60 seconds.")

    start_time = time.time()

    eye_scores = []
    posture_scores = []
    stability_scores = []

    while True:

        if time.time() - start_time > 60:

            print("\nInterview Session Completed.")
            break

        ret, frame = cap.read()

        if not ret:
            break

        eye_score = get_eye_contact_score(frame)

        posture_score = get_posture_score(frame)

        stability_score = get_head_stability_score(frame)

        eye_scores.append(eye_score)

        posture_scores.append(posture_score)

        stability_scores.append(stability_score)

        cv2.putText(
            frame,
            f"Eye Contact: {eye_score}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 0, 0),
            2,
        )

        cv2.putText(
            frame,
            f"Posture: {posture_score}",
            (20, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 0, 0),
            2,
        )

        cv2.putText(
            frame,
            f"Head Stability: {stability_score}",
            (20, 120),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 0, 0),
            2,
        )

        cv2.imshow("AI Mock Interview", frame)

        key = cv2.waitKey(1)

        if key == ord("q") or key == 27:

            print("\nStopped Manually.")
            break

    cap.release()
    cv2.destroyAllWindows()

    avg_eye_contact = (
        round(sum(eye_scores) / len(eye_scores), 2)
        if eye_scores else 0
    )

    avg_posture = (
        round(sum(posture_scores) / len(posture_scores), 2)
        if posture_scores else 0
    )

    avg_stability = (
        round(sum(stability_scores) / len(stability_scores), 2)
        if stability_scores else 0
    )

    print("\nFinal Scores")
    print(f"Eye Contact: {avg_eye_contact}")
    print(f"Posture: {avg_posture}")
    print(f"Head Stability: {avg_stability}")

    features = {
        "eye_contact": avg_eye_contact,
        "posture": avg_posture,
        "head_stability": avg_stability,
    }

    with open(
        "interview/interview_features.json",
        "w"
    ) as f:

        json.dump(
            features,
            f,
            indent=4
        )

    print("\nFeatures Saved Successfully!")

    return features


if __name__ == "__main__":

    run_camera_interview()