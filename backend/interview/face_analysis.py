import cv2
import mediapipe as mp
import numpy as np

# ==========================================
# MEDIAPIPE SETUP
# ==========================================

mp_face_mesh = mp.solutions.face_mesh

face_mesh = mp_face_mesh.FaceMesh(
    static_image_mode=False,
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5,
)

# ==========================================
# ANALYZE FACE
# ==========================================


def analyze_face():

    cap = cv2.VideoCapture(0)

    eye_contact_scores = []
    smile_scores = []
    head_positions = []

    print("Press Q to stop analysis")

    while cap.isOpened():

        success, frame = cap.read()

        if not success:
            break

        frame = cv2.flip(frame, 1)

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = face_mesh.process(rgb_frame)

        if results.multi_face_landmarks:

            landmarks = results.multi_face_landmarks[0]

            h, w, _ = frame.shape

            # ======================================
            # LEFT EYE
            # ======================================

            left_eye = landmarks.landmark[33]

            # ======================================
            # RIGHT EYE
            # ======================================

            right_eye = landmarks.landmark[263]

            # ======================================
            # NOSE
            # ======================================

            nose = landmarks.landmark[1]

            # ======================================
            # MOUTH
            # ======================================

            upper_lip = landmarks.landmark[13]

            lower_lip = landmarks.landmark[14]

            # ======================================
            # EYE CONTACT
            # ======================================

            eye_distance = abs(left_eye.x - right_eye.x)

            eye_contact = min(100, eye_distance * 300)

            eye_contact_scores.append(eye_contact)

            # ======================================
            # SMILE SCORE
            # ======================================

            smile_gap = abs(upper_lip.y - lower_lip.y)

            smile_score = min(100, smile_gap * 1500)

            smile_scores.append(smile_score)

            # ======================================
            # HEAD STABILITY
            # ======================================

            head_positions.append(nose.x)

            # ======================================
            # DISPLAY
            # ======================================

            cv2.putText(
                frame,
                f"Eye Contact: {eye_contact:.0f}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2,
            )

            cv2.putText(
                frame,
                f"Smile: {smile_score:.0f}",
                (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 0, 0),
                2,
            )

        cv2.imshow("Face Analysis", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()

    cv2.destroyAllWindows()

    # ==========================================
    # FINAL SCORES
    # ==========================================

    avg_eye_contact = np.mean(eye_contact_scores) if eye_contact_scores else 0

    avg_smile = np.mean(smile_scores) if smile_scores else 0

    if len(head_positions) > 1:

        movement = np.std(head_positions)

        head_stability = max(0, 100 - movement * 1000)

    else:

        head_stability = 0

    return {
        "eye_contact": round(avg_eye_contact, 2),
        "smile_score": round(avg_smile, 2),
        "head_stability": round(head_stability, 2),
    }


if __name__ == "__main__":

    scores = analyze_face()

    print("\nFace Analysis Results")
    print(scores)
