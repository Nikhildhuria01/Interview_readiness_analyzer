import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh

face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True, max_num_faces=1)


def get_eye_contact_score(frame):

    rgb = frame[:, :, ::-1]

    results = face_mesh.process(rgb)

    eye_score = 0

    if results.multi_face_landmarks:

        face = results.multi_face_landmarks[0]

        try:

            left_iris = face.landmark[468]

            left_eye_left = face.landmark[33]

            left_eye_right = face.landmark[133]

            eye_ratio = (left_iris.x - left_eye_left.x) / (
                left_eye_right.x - left_eye_left.x
            )

            eye_score = max(0, min(100, int(100 - abs(eye_ratio - 0.5) * 250)))

        except:

            pass

    return eye_score
