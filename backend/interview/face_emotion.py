from deepface import DeepFace
import cv2
import time

from emotion_scorer import (
    calculate_emotion_scores
)

from feature_saver import (
    save_emotion_features
)

cap = cv2.VideoCapture(0)

print("Interview Started...")
print("Camera will close automatically after 15 seconds.")

emotion = "neutral"
confidence = 0
engagement = 0
nervousness = 0

start_time = time.time()

while True:

    # Auto stop after 15 seconds

    if time.time() - start_time > 15:

        print(
            "\nInterview session completed."
        )

        break

    ret, frame = cap.read()

    if not ret:
        break

    try:

        result = DeepFace.analyze(
            frame,
            actions=["emotion"],
            enforce_detection=False
        )

        emotion = result[0]["dominant_emotion"]

        scores = calculate_emotion_scores(
            emotion
        )

        confidence = scores[
            "confidence_score"
        ]

        engagement = scores[
            "engagement_score"
        ]

        nervousness = scores[
            "nervousness_score"
        ]

        cv2.putText(
            frame,
            f"Emotion: {emotion}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            f"Confidence: {confidence}",
            (20, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 0, 0),
            2
        )

    except Exception as e:

        print(e)

    cv2.imshow(
        "Interview Camera",
        frame
    )

    key = cv2.waitKey(1)

    if key == ord("q") or key == ord("Q") or key == 27:

        print(
            "\nInterview stopped manually."
        )

        break

cap.release()

cv2.destroyAllWindows()

save_emotion_features(
    emotion,
    confidence,
    engagement,
    nervousness
)

print(
    "\nEmotion Features Saved Successfully!"
)