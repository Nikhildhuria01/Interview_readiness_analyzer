import time
import platform
import subprocess
import multiprocessing
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
# from load_features import load_features

print("9")
from feature_aggregator import calculate_overall_score
from report_generator import generate_report

# =====================
# CONFIG
# =====================

ANSWER_DURATION = 30
CAMERA_FRAME_INTERVAL = 0.05
CAMERA_WINDOW_NAME = "AI Mock Interview"


# =====================
# SPEAK FUNCTION
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
# TEST DATA
# =====================
def draw_camera_overlay(
    frame,
    question,
    question_number,
    total_questions,
    eye_score,
    posture_score,
    head_score,
):

    question_label = f"Question {question_number}/{total_questions}"

    if question_number == 0:

        question_label = "Preparing interview"

    cv2.putText(
        frame,
        question_label,
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 0, 0),
        2,
    )

    cv2.putText(
        frame,
        question[:60],
        (20, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (0, 0, 0),
        2,
    )

    cv2.putText(
        frame,
        f"Eye Contact: {eye_score}",
        (20, 140),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (0, 0, 0),
        2,
    )

    cv2.putText(
        frame,
        f"Posture: {posture_score}",
        (20, 180),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (0, 0, 0),
        2,
    )

    cv2.putText(
        frame,
        f"Head Stability: {head_score}",
        (20, 220),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (0, 0, 0),
        2,
    )


def camera_monitor_process(
    interview_state,
    stop_event,
    eye_scores,
    posture_scores,
    head_scores,
):

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():

        print("Camera Error: Unable to open camera.")

        stop_event.set()

        return

    try:

        while not stop_event.is_set():

            ret, frame = cap.read()

            if not ret:

                time.sleep(CAMERA_FRAME_INTERVAL)

                continue

            question = interview_state.get("question", "")

            question_number = interview_state.get("question_number", 0)

            total_questions = interview_state.get("total_questions", 0)

            eye_score = get_eye_contact_score(frame)

            posture_score = get_posture_score(frame)

            head_score = get_head_stability_score(frame)

            eye_scores.append(eye_score)

            posture_scores.append(posture_score)

            head_scores.append(head_score)

            draw_camera_overlay(
                frame,
                question,
                question_number,
                total_questions,
                eye_score,
                posture_score,
                head_score,
            )

            cv2.imshow(CAMERA_WINDOW_NAME, frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):

                stop_event.set()

                break

            time.sleep(CAMERA_FRAME_INTERVAL)

    finally:

        cap.release()

        cv2.destroyAllWindows()


def run_audio_interview():

    resume_skills = ["Python", "Docker", "AWS"]

    jd_skills = ["Python", "Docker", "AWS", "Kubernetes", "CI/CD", "Jenkins"]

    questions = generate_interview_questions(resume_skills, jd_skills)

    questions = list(dict.fromkeys(questions))

    questions = questions[:10]

    all_fluency_scores = []

    all_correctness_scores = []

    question_results = []

    camera_manager = multiprocessing.Manager()

    interview_state = camera_manager.dict(
        {
            "question": "",
            "question_number": 0,
            "total_questions": len(questions),
        }
    )

    eye_scores = camera_manager.list()

    posture_scores = camera_manager.list()

    head_scores = camera_manager.list()

    stop_camera_event = multiprocessing.Event()

    camera_process = multiprocessing.Process(
        target=camera_monitor_process,
        args=(
            interview_state,
            stop_camera_event,
            eye_scores,
            posture_scores,
            head_scores,
        ),
    )

    print("\n==========================")

    print("AI MOCK INTERVIEW STARTED")

    print("==========================")

    print(f"\nTotal Questions: {len(questions)}")

    camera_process.start()

    try:

        for i, question in enumerate(questions, start=1):

            interview_state["question"] = question

            interview_state["question_number"] = i

            print("\n" + "=" * 60)

            print(f"QUESTION {i}")

            print(question)

            print("=" * 60)

            print("\nAsking Question...")

            speak(question)

            time.sleep(1)

            answer_file = f"backend/interview/answers/answer_{i}.wav"

            print(f"\nRecording Answer {i}")

            print(f"You have {ANSWER_DURATION} seconds.")

            record_answer(answer_file, duration=ANSWER_DURATION)

            print(f"Answer Saved: {answer_file}")

            transcript_file = f"backend/interview/transcripts/transcript_{i}.txt"

            transcript = generate_transcript(answer_file, transcript_file)

            print("\nTranscript:")

            print(transcript)

            fluency_results = analyze_advanced_fluency(transcript, ANSWER_DURATION)

            fluency_score = fluency_results["fluency_score"]

            all_fluency_scores.append(fluency_score)

            print("\nFluency Analysis")

            print(f"Word Count: {fluency_results['word_count']}")

            print(f"Filler Count: {fluency_results['filler_count']}")

            print(f"Words Per Minute: {fluency_results['words_per_minute']}")

            print(f"Repeated Words: {fluency_results['repeated_words']}")

            print(f"Fluency Score: {fluency_score}")

            print("\nSTEP 1: Transcript Generated")

            print("STEP 2: Generating Ideal Answer...")

            ideal_answer = generate_ideal_answer(question)

            print("STEP 3: Ideal Answer Generated")

            print("\nIdeal Answer:")

            print(ideal_answer)

            print("\nSTEP 4: Calculating Correctness...")

            correctness_result = calculate_correctness(
                question, transcript, ideal_answer
            )

            correctness_score = correctness_result["score"]

            feedback = correctness_result["feedback"]

            print("STEP 5: Correctness Calculated")

            all_correctness_scores.append(correctness_score)

            print(f"\nCorrectness Score: {correctness_score}")

            print(f"Feedback: {feedback}")

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

    finally:

        stop_camera_event.set()

        camera_process.join(timeout=5)

        if camera_process.is_alive():

            camera_process.terminate()

            camera_process.join()

    eye_scores = list(eye_scores)

    posture_scores = list(posture_scores)

    head_scores = list(head_scores)

    camera_manager.shutdown()

    average_fluency = 0

    if len(all_fluency_scores) > 0:

        average_fluency = round(sum(all_fluency_scores) / len(all_fluency_scores), 2)

    average_correctness = 0

    if len(all_correctness_scores) > 0:

        average_correctness = round(
            sum(all_correctness_scores) / len(all_correctness_scores), 2
        )

    eye_contact_score = round(
        sum(eye_scores) / max(1, len(eye_scores)),
        2,
    )

    posture_score = round(
        sum(posture_scores) / max(1, len(posture_scores)),
        2,
    )

    head_stability_score = round(
        sum(head_scores) / max(1, len(head_scores)),
        2,
    )

    overall_score = calculate_overall_score(
        average_fluency,
        average_correctness,
        eye_contact_score,
        posture_score,
        head_stability_score,
    )

    results = {
        "average_fluency": average_fluency,
        "average_correctness": average_correctness,
        "eye_contact_score": eye_contact_score,
        "posture_score": posture_score,
        "head_stability_score": head_stability_score,
        "overall_score": overall_score,
        "questions": question_results,
    }

    save_results(results)

    generate_report()

    print("\n==========================")

    print("INTERVIEW COMPLETED")

    print("==========================")

    print(f"\nAverage Fluency Score: {average_fluency}")

    print(f"Average Correctness Score: {average_correctness}")

    print(f"\nEye Contact Score: {eye_contact_score}")

    print(f"Posture Score: {posture_score}")

    print(f"Head Stability Score: {head_stability_score}")

    print(f"\nOverall Interview Score: {overall_score}")

    print("\nInterview Results Saved!")


if __name__ == "__main__":

    multiprocessing.freeze_support()

    run_audio_interview()
