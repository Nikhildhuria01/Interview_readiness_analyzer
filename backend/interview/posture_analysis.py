import cv2
import mediapipe as mp

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    rgb = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )

    results = pose.process(rgb)

    if results.pose_landmarks:

        mp.solutions.drawing_utils.draw_landmarks(
            frame,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS
        )

        left_shoulder = (
            results.pose_landmarks.landmark[
                mp_pose.PoseLandmark.LEFT_SHOULDER
            ]
        )

        right_shoulder = (
            results.pose_landmarks.landmark[
                mp_pose.PoseLandmark.RIGHT_SHOULDER
            ]
        )

        shoulder_diff = abs(
            left_shoulder.y -
            right_shoulder.y
        )

        if shoulder_diff < 0.05:

            posture = "Good"

        else:

            posture = "Bad"

        cv2.putText(
            frame,
            f"Posture: {posture}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,255,0),
            2
        )

    cv2.imshow(
        "Posture Analysis",
        frame
    )

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()