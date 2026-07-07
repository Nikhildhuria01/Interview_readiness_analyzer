from interview.speech_to_text import generate_transcript
from interview.advanced_fluency import analyze_advanced_fluency
from interview.ideal_answer_generator import generate_ideal_answer
from interview.correctness_analysis import calculate_correctness


def analyze_answer(
    question: str,
    audio_file: str,
    transcript_file: str,
    answer_duration: int = 30,
):
    """
    Analyze one interview answer.
    """

    transcript = generate_transcript(
        audio_file,
        transcript_file,
    )

    fluency = analyze_advanced_fluency(
        transcript,
        answer_duration,
    )

    ideal_answer = generate_ideal_answer(question)

    correctness = calculate_correctness(
        question,
        transcript,
        ideal_answer,
    )

    return {
        "question": question,
        "transcript": transcript,
        "ideal_answer": ideal_answer,
        "fluency_score": fluency["fluency_score"],
        "correctness_score": correctness["score"],
        "feedback": correctness["feedback"],
    }
