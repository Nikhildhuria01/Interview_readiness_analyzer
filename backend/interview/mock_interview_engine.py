import time
import platform
import subprocess
import pyttsx3

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
from load_features import load_features

print("9")
from feature_aggregator import calculate_overall_score
from report_generator import generate_report

# =====================
# CONFIG
# =====================

ANSWER_DURATION = 30


# =====================
# SPEAK FUNCTION
# =====================

def speak(text):

    try:

        if platform.system() == "Darwin":

            subprocess.run(
                [
                    "say",
                    "-v",
                    "Daniel",
                    text
                ]
            )

        else:

            engine = pyttsx3.init()

            engine.setProperty(
                "rate",
                140
            )

            engine.setProperty(
                "volume",
                1.0
            )

            engine.say(text)

            engine.runAndWait()

            engine.stop()

    except Exception as e:

        print(
            f"Speech Error: {e}"
        )


# =====================
# TEST DATA
# =====================
def run_audio_interview():

    resume_skills = [
        "Python",
        "Docker",
        "AWS"
    ]

    jd_skills = [
        "Python",
        "Docker",
        "AWS",
        "Kubernetes",
        "CI/CD",
        "Jenkins"
    ]


    # =====================
    # GENERATE QUESTIONS
    # =====================

    questions = generate_interview_questions(
        resume_skills,
        jd_skills
    )

    questions = list(
        dict.fromkeys(
            questions
        )
    )

    questions = questions[:10]


    # =====================
    # RESULTS STORAGE
    # =====================

    all_fluency_scores = []

    all_correctness_scores = []

    question_results = []


    # =====================
    # START INTERVIEW
    # =====================

    print("\n==========================")

    print("AI MOCK INTERVIEW STARTED")

    print("==========================")

    print(
        f"\nTotal Questions: {len(questions)}"
    )


    # =====================
    # ASK QUESTIONS
    # =====================

    for i, question in enumerate(
        questions,
        start=1
    ):

        print(
            "\n" + "=" * 60
        )

        print(
            f"QUESTION {i}"
        )

        print(question)

        print(
            "=" * 60
        )

        # =====================
        # SPEAK QUESTION
        # =====================

        print(
            "\nAsking Question..."
        )

        speak(question)

        time.sleep(1)

        # =====================
        # RECORD ANSWER
        # =====================

        answer_file = (
            f"backend/interview/answers/answer_{i}.wav"
        )

        print(
            f"\nRecording Answer {i}"
        )

        print(
            f"You have {ANSWER_DURATION} seconds."
        )

        record_answer(
            answer_file,
            duration=ANSWER_DURATION
        )

        print(
            f"Answer Saved: {answer_file}"
        )

        # =====================
        # TRANSCRIPTION
        # =====================

        transcript_file = (
            f"backend/interview/transcripts/transcript_{i}.txt"
        )

        transcript = generate_transcript(
            answer_file,
            transcript_file
        )

        print(
            "\nTranscript:"
        )

        print(
            transcript
        )

        # =====================
        # FLUENCY ANALYSIS
        # =====================

        fluency_results = analyze_advanced_fluency(
            transcript,
            ANSWER_DURATION
        )

        fluency_score = (
            fluency_results[
                "fluency_score"
            ]
        )

        all_fluency_scores.append(
            fluency_score
        )

        print(
            "\nFluency Analysis"
        )

        print(
            f"Word Count: {fluency_results['word_count']}"
        )

        print(
            f"Filler Count: {fluency_results['filler_count']}"
        )

        print(
            f"Words Per Minute: {fluency_results['words_per_minute']}"
        )

        print(
            f"Repeated Words: {fluency_results['repeated_words']}"
        )

        print(
            f"Fluency Score: {fluency_score}"
        )

        # =====================
        # CORRECTNESS ANALYSIS
        # =====================

        print(
            "\nSTEP 1: Transcript Generated"
        )

        print(
            "STEP 2: Generating Ideal Answer..."
        )

        ideal_answer = generate_ideal_answer(
            question
        )

        print(
            "STEP 3: Ideal Answer Generated"
        )

        print(
            "\nIdeal Answer:"
        )

        print(
            ideal_answer
        )

        print(
            "\nSTEP 4: Calculating Correctness..."
        )

        correctness_result = calculate_correctness(
            question,
            transcript,
            ideal_answer
        )

        correctness_score = (
            correctness_result[
                "score"
            ]
        )

        feedback = (
            correctness_result[
                "feedback"
            ]
        )

        print(
            "STEP 5: Correctness Calculated"
        )

        all_correctness_scores.append(
            correctness_score
        )

        print(
            f"\nCorrectness Score: {correctness_score}"
        )

        print(
            f"Feedback: {feedback}"
        )

        # =====================
        # SAVE QUESTION RESULT
        # =====================

        question_results.append({

            "question": question,

            "candidate_answer": transcript,

            "ideal_answer": ideal_answer,

            "fluency_score": fluency_score,

            "correctness_score": correctness_score,

            "feedback": feedback

        })


    # =====================
    # FINAL RESULTS
    # =====================

    average_fluency = 0

    if len(all_fluency_scores) > 0:

        average_fluency = round(

            sum(all_fluency_scores)

            /

            len(all_fluency_scores),

            2

        )

    average_correctness = 0

    if len(all_correctness_scores) > 0:

        average_correctness = round(

            sum(all_correctness_scores)

            /

            len(all_correctness_scores),

            2

        )


    # =====================
    # LOAD CAMERA FEATURES
    # =====================

    features = load_features()

    eye_contact_score = features[
        "eye_contact"
    ]

    posture_score = features[
        "posture"
    ]

    head_stability_score = features[
        "head_stability"
    ]


    # =====================
    # OVERALL SCORE
    # =====================

    overall_score = calculate_overall_score(

        average_fluency,

        average_correctness,

        eye_contact_score,

        posture_score,

        head_stability_score

    )


    # =====================
    # SAVE JSON RESULTS
    # =====================

    results = {

        "average_fluency": average_fluency,

        "average_correctness": average_correctness,

        "eye_contact_score": eye_contact_score,

        "posture_score": posture_score,

        "head_stability_score": head_stability_score,

        "overall_score": overall_score,

        "questions": question_results

    }

    save_results(
        results
    )

    generate_report()


    # =====================
    # PRINT RESULTS
    # =====================

    print(
        "\n=========================="
    )

    print(
        "INTERVIEW COMPLETED"
    )

    print(
        "=========================="
    )

    print(
        f"\nAverage Fluency Score: {average_fluency}"
    )

    print(
        f"Average Correctness Score: {average_correctness}"
    )

    print(
        f"\nEye Contact Score: {eye_contact_score}"
    )

    print(
        f"Posture Score: {posture_score}"
    )

    print(
        f"Head Stability Score: {head_stability_score}"
    )

    print(
        f"\nOverall Interview Score: {overall_score}"
    )

    print(
        "\nInterview Results Saved!"
    )

if __name__ == "__main__":

    run_audio_interview()