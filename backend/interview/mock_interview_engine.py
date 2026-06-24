import time
import platform
import subprocess
import threading
import pyttsx3
import cv2

from eye_contact_analysis import get_eye_contact_score
from posture_analysis import get_posture_score
from head_stability import get_head_stability_score

print("1")
from question_engine import generate_interview_questions

print("2")
from audio_recorder import record_answer

print("3")
from speech_to_text import generate_transcript

print("4")
from advanced_fluency import analyze_advanced_fluency

print("5")
from ideal_answer_generator import generate_ideal_answer

print("6")
from correctness_analysis import calculate_correctness

print("7")
from save_results import save_results

print("8")
from feature_aggregator import calculate_overall_score
from report_generator import generate_report

print("9")

# =====================
# CONFIG
# =====================

ANSWER_DURATION = 30
CAMERA_FRAME_INTERVAL = 0.05
CAMERA_WINDOW_NAME = "AI Mock Interview"


# =====================
# SPEAK
# =====================


def speak(text):
    try:
        if platform.system() == "Darwin":
            subprocess.run(["say", "-v", "Daniel", text])
        else:
            engine = pyttsx3.init()
            engine.setProperty("rate", 140)
            engine.setProperty("volume", 1.0)
            engine.say(text)
            engine.runAndWait()
            engine.stop()
    except Exception as e:
        print(f"Speech Error: {e}")


# =====================
# CAMERA BACKEND (cross-platform)
# cv2.CAP_DSHOW is Windows-only (DirectShow). On macOS this causes
# VideoCapture to fail to open, which is why it worked on Windows but
# not on Mac. Pick the right backend per-OS, with a safe fallback.
# =====================


def open_camera(index=0):
    system = platform.system()
    if system == "Windows":
        backends = [cv2.CAP_DSHOW, cv2.CAP_MSMF, cv2.CAP_ANY]
    elif system == "Darwin":
        backends = [cv2.CAP_AVFOUNDATION, cv2.CAP_ANY]
    else:
        backends = [cv2.CAP_V4L2, cv2.CAP_ANY]

    for backend in backends:
        cap = cv2.VideoCapture(index, backend)
        if cap.isOpened():
            return cap
        cap.release()

    # Last resort: let OpenCV pick automatically (no backend flag at all)
    return cv2.VideoCapture(index)


# =====================
# OVERLAY
# Fix: weights must sum to 1.0  →  0.6 + 0.4 = 1.0  (no gray bleed)
# Fix: draw ALL text AFTER addWeighted so it isn't blended away
# =====================


def draw_camera_overlay(
    frame,
    question,
    question_number,
    total_questions,
    eye_score,
    posture_score,
    head_score,
    recording=False,
    status_text="",
):
    h, w = frame.shape[:2]

    # --- semi-transparent banner (top 250 px) ---
    # Draw the dark rectangle on a copy FIRST, then blend.
    # Weights 0.60 + 0.40 = 1.0  → no gray artifact
    banner_copy = frame.copy()
    # cv2.rectangle(banner_copy, (0, 0), (w, 250), (20, 20, 20), -1)
    # cv2.addWeighted(banner_copy, 0.60, frame, 0.40, 0, frame)
    # Now draw text ON TOP of the already-blended frame

    # Question counter
    q_label = (
        f"Question {question_number} / {total_questions}"
        if question_number > 0
        else "Preparing Interview..."
    )
    cv2.putText(frame, q_label, (20, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 0), 2)

    # Word-wrap question text (~58 chars per line, max 3 lines)
    words = question.split()
    lines, cur = [], ""
    for word in words:
        if len(cur) + len(word) + 1 <= 58:
            cur += (" " if cur else "") + word
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    for idx, line in enumerate(lines[:3]):
        cv2.putText(
            frame,
            line,
            (20, 72 + idx * 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.75,
            (0, 0, 0),
            2,
        )

    # Scores
    cv2.putText(
        frame,
        f"Eye Contact:    {eye_score:.2f}",
        (20, 175),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.75,
        (0, 0, 0),
        2,
    )
    cv2.putText(
        frame,
        f"Posture:        {posture_score:.2f}",
        (20, 203),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.75,
        (0, 0, 0),
        2,
    )
    cv2.putText(
        frame,
        f"Head Stability: {head_score:.2f}",
        (20, 231),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.75,
        (0, 0, 0),
        2,
    )

    # Status text (processing / analysing…) – bottom-left
    if status_text:
        cv2.putText(
            frame,
            status_text,
            (20, h - 20),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.75,
            (0, 0, 0),
            2,
        )

    # REC indicator – bottom-right
    if recording:
        cv2.circle(frame, (w - 30, h - 30), 12, (0, 0, 220), -1)
        cv2.putText(
            frame,
            "REC",
            (w - 72, h - 22),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.55,
            (0, 0, 0),
            2,
        )


# =====================
# CAMERA THREAD
# Owns cap entirely; pushes annotated frames into shared_frame[0].
# Never calls imshow – only the main thread does that.
# =====================


def camera_monitor_thread(
    interview_state,
    stop_event,
    eye_scores,
    posture_scores,
    head_scores,
    frame_lock,
    shared_frame,
):
    print("CAMERA THREAD: starting")
    cap = open_camera(0)
    print("CAMERA THREAD: VideoCapture created")

    if not cap.isOpened():
        print("Camera Error: Unable to open camera.")
        stop_event.set()
        return

    last_eye = last_posture = last_head = 0.0

    try:
        while not stop_event.is_set():
            ret, frame = cap.read()
            if not ret:
                time.sleep(CAMERA_FRAME_INTERVAL)
                continue

            # Analyse frame
            last_eye = get_eye_contact_score(frame)
            last_posture = get_posture_score(frame)
            last_head = get_head_stability_score(frame)

            eye_scores.append(last_eye)
            posture_scores.append(last_posture)
            head_scores.append(last_head)

            # Read shared state under lock
            with frame_lock:
                question = interview_state.get("question", "")
                question_number = interview_state.get("question_number", 0)
                total_questions = interview_state.get("total_questions", 0)
                recording = interview_state.get("recording", False)
                status_text = interview_state.get("status_text", "")

            display = frame.copy()
            draw_camera_overlay(
                display,
                question,
                question_number,
                total_questions,
                last_eye,
                last_posture,
                last_head,
                recording=recording,
                status_text=status_text,
            )

            with frame_lock:
                shared_frame[0] = display

            time.sleep(CAMERA_FRAME_INTERVAL)

    finally:
        cap.release()
        print("CAMERA THREAD: released cap")


# =====================
# HELPERS
# =====================


def refresh_display(frame_lock, shared_frame, window_name):
    """Show the latest frame. Must be called from the main thread."""
    with frame_lock:
        frame = shared_frame[0]
    if frame is not None:
        cv2.imshow(window_name, frame)
    cv2.waitKey(1)


def run_in_background_with_live_camera(
    target_fn,
    args,
    frame_lock,
    shared_frame,
    window_name,
    poll_interval=0.05,
):
    """
    Run target_fn(*args) in a daemon thread while keeping the camera
    window refreshed on the main thread.  Returns the function's return
    value via a result container.
    """
    result_box = [None]
    error_box = [None]

    def wrapper():
        try:
            result_box[0] = target_fn(*args)
        except Exception as exc:
            error_box[0] = exc

    t = threading.Thread(target=wrapper, daemon=True)
    t.start()
    while t.is_alive():
        refresh_display(frame_lock, shared_frame, window_name)
        time.sleep(poll_interval)
    t.join()

    if error_box[0]:
        raise error_box[0]
    return result_box[0]


# =====================
# MAIN
# =====================


def run_audio_interview():

    resume_skills = ["Python", "Docker", "AWS"]
    jd_skills = ["Python", "Docker", "AWS", "Kubernetes", "CI/CD", "Jenkins"]

    questions = generate_interview_questions(resume_skills, jd_skills)
    questions = list(dict.fromkeys(questions))
    questions = questions[:10]

    all_fluency_scores = []
    all_correctness_scores = []
    question_results = []

    frame_lock = threading.Lock()
    shared_frame = [None]

    interview_state = {
        "question": "",
        "question_number": 0,
        "total_questions": len(questions),
        "recording": False,
        "status_text": "",
    }

    eye_scores = []
    posture_scores = []
    head_scores = []

    stop_camera_event = threading.Event()

    camera_thread = threading.Thread(
        target=camera_monitor_thread,
        args=(
            interview_state,
            stop_camera_event,
            eye_scores,
            posture_scores,
            head_scores,
            frame_lock,
            shared_frame,
        ),
        daemon=True,
    )

    print("\n==========================")
    print("AI MOCK INTERVIEW STARTED")
    print("==========================")
    print(f"Total Questions: {len(questions)}")

    # Main thread owns the window
    cv2.namedWindow(CAMERA_WINDOW_NAME, cv2.WINDOW_NORMAL)
    camera_thread.start()

    # Warm-up: wait until camera produces its first frame
    print("Warming up camera...")
    warm_up_deadline = time.time() + 3.0
    while time.time() < warm_up_deadline:
        refresh_display(frame_lock, shared_frame, CAMERA_WINDOW_NAME)
        time.sleep(0.05)

    try:
        for i, question in enumerate(questions, start=1):

            # ── show question on screen ──────────────────────────────────
            with frame_lock:
                interview_state["question"] = question
                interview_state["question_number"] = i
                interview_state["status_text"] = ""

            print(f"\n{'='*60}")
            print(f"QUESTION {i}: {question}")
            print("=" * 60)

            # ── speak question (camera stays live) ───────────────────────
            print("Asking question...")
            run_in_background_with_live_camera(
                speak, (question,), frame_lock, shared_frame, CAMERA_WINDOW_NAME
            )
            time.sleep(0.4)

            # ── record answer (camera stays live, REC dot shown) ─────────
            answer_file = f"backend/interview/answers/answer_{i}.wav"
            print(f"Recording answer {i}  ({ANSWER_DURATION}s)…")

            with frame_lock:
                interview_state["recording"] = True
                interview_state["status_text"] = ""

            record_start = time.time()

            def _timed_record():
                record_answer(answer_file, ANSWER_DURATION)

            rec_done = [False]

            def _record_wrapper():
                _timed_record()
                rec_done[0] = True

            rec_thread = threading.Thread(target=_record_wrapper, daemon=True)
            rec_thread.start()

            while rec_thread.is_alive():
                elapsed = time.time() - record_start
                remaining = max(0, ANSWER_DURATION - elapsed)
                cv2.setWindowTitle(
                    CAMERA_WINDOW_NAME,
                    f"{CAMERA_WINDOW_NAME}   ●  Recording… {remaining:.0f}s left",
                )
                refresh_display(frame_lock, shared_frame, CAMERA_WINDOW_NAME)
                time.sleep(0.05)

            rec_thread.join()

            with frame_lock:
                interview_state["recording"] = False

            cv2.setWindowTitle(CAMERA_WINDOW_NAME, CAMERA_WINDOW_NAME)
            print(f"Answer saved: {answer_file}")

            # ── transcript ───────────────────────────────────────────────
            transcript_file = f"backend/interview/transcripts/transcript_{i}.txt"

            with frame_lock:
                interview_state["status_text"] = ""

            transcript = run_in_background_with_live_camera(
                generate_transcript,
                (answer_file, transcript_file),
                frame_lock,
                shared_frame,
                CAMERA_WINDOW_NAME,
            )
            print(f"Transcript: {transcript}")

            # ── fluency ──────────────────────────────────────────────────
            with frame_lock:
                interview_state["status_text"] = ""

            fluency_results = run_in_background_with_live_camera(
                analyze_advanced_fluency,
                (transcript, ANSWER_DURATION),
                frame_lock,
                shared_frame,
                CAMERA_WINDOW_NAME,
            )
            fluency_score = fluency_results["fluency_score"]
            all_fluency_scores.append(fluency_score)
            print(f"Fluency Score: {fluency_score}")

            # ── ideal answer ─────────────────────────────────────────────
            with frame_lock:
                interview_state["status_text"] = ""

            ideal_answer = run_in_background_with_live_camera(
                generate_ideal_answer,
                (question,),
                frame_lock,
                shared_frame,
                CAMERA_WINDOW_NAME,
            )
            print(f"Ideal Answer: {ideal_answer}")

            # ── correctness ──────────────────────────────────────────────
            with frame_lock:
                interview_state["status_text"] = ""

            correctness_result = run_in_background_with_live_camera(
                calculate_correctness,
                (question, transcript, ideal_answer),
                frame_lock,
                shared_frame,
                CAMERA_WINDOW_NAME,
            )
            correctness_score = correctness_result["score"]
            feedback = correctness_result["feedback"]
            all_correctness_scores.append(correctness_score)
            print(f"Correctness: {correctness_score}  |  Feedback: {feedback}")

            # ── clear status, ready for next question ────────────────────
            with frame_lock:
                interview_state["status_text"] = ""

            question_results.append(
                {
                    "question": question,
                    "candidate_answer": transcript,
                    "ideal_answer": ideal_answer,
                    "fluency_score": fluency_score,
                    "correctness_score": correctness_score,
                    "feedback": feedback,
                }
            )

            refresh_display(frame_lock, shared_frame, CAMERA_WINDOW_NAME)

    finally:
        stop_camera_event.set()
        camera_thread.join(timeout=5)
        cv2.destroyAllWindows()

    # ── final scores ─────────────────────────────────────────────────────
    avg_fluency = round(sum(all_fluency_scores) / max(1, len(all_fluency_scores)), 2)
    avg_correctness = round(
        sum(all_correctness_scores) / max(1, len(all_correctness_scores)), 2
    )
    eye_score = round(sum(eye_scores) / max(1, len(eye_scores)), 2)
    post_score = round(sum(posture_scores) / max(1, len(posture_scores)), 2)
    head_score = round(sum(head_scores) / max(1, len(head_scores)), 2)

    overall = calculate_overall_score(
        avg_fluency, avg_correctness, eye_score, post_score, head_score
    )

    save_results(
        {
            "average_fluency": avg_fluency,
            "average_correctness": avg_correctness,
            "eye_contact_score": eye_score,
            "posture_score": post_score,
            "head_stability_score": head_score,
            "overall_score": overall,
            "questions": question_results,
        }
    )
    generate_report()

    print("\n==========================")
    print("INTERVIEW COMPLETED")
    print("==========================")
    print(f"Average Fluency:     {avg_fluency}")
    print(f"Average Correctness: {avg_correctness}")
    print(f"Eye Contact:         {eye_score}")
    print(f"Posture:             {post_score}")
    print(f"Head Stability:      {head_score}")
    print(f"Overall Score:       {overall}")
    print("Interview Results Saved!")


if __name__ == "__main__":
    run_audio_interview()
