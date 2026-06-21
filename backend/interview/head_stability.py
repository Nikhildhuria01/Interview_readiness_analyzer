nose_history = []


def get_head_stability_score(frame):

    import mediapipe as mp

    global nose_history

    mp_face_mesh = mp.solutions.face_mesh

    if not hasattr(get_head_stability_score, "face_mesh"):

        get_head_stability_score.face_mesh = mp_face_mesh.FaceMesh(
            refine_landmarks=True, max_num_faces=1
        )

    rgb = frame[:, :, ::-1]

    results = get_head_stability_score.face_mesh.process(rgb)

    stability_score = 100

    if results.multi_face_landmarks:

        face = results.multi_face_landmarks[0]

        nose = face.landmark[1]

        nose_history.append((nose.x, nose.y))

        if len(nose_history) > 50:

            nose_history.pop(0)

        if len(nose_history) > 10:

            x_values = [p[0] for p in nose_history]

            y_values = [p[1] for p in nose_history]

            movement = (max(x_values) - min(x_values)) + (max(y_values) - min(y_values))

            stability_score = max(0, int(100 - movement * 250))

    return stability_score
