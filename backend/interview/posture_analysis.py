import mediapipe as mp

mp_pose = mp.solutions.pose

pose = mp_pose.Pose()


def get_posture_score(frame):

    rgb = frame[:, :, ::-1]

    results = pose.process(rgb)

    posture_score = 0

    if results.pose_landmarks:

        left_shoulder = results.pose_landmarks.landmark[
            mp_pose.PoseLandmark.LEFT_SHOULDER
        ]

        right_shoulder = results.pose_landmarks.landmark[
            mp_pose.PoseLandmark.RIGHT_SHOULDER
        ]

        shoulder_diff = abs(left_shoulder.y - right_shoulder.y)

        posture_score = max(0, min(100, int(100 - shoulder_diff * 1000)))

    return posture_score
