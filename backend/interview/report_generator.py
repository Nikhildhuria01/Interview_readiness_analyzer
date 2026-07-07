import json

from reportlab.platypus import (

    SimpleDocTemplate,

    Paragraph,

    Spacer,

    PageBreak

)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


def generate_report():

    with open(

        "interview/interview_results.json",

        "r",

        encoding="utf-8"

    ) as f:

        data = json.load(f)

    pdf = SimpleDocTemplate(

        "Interview_Report.pdf"

    )

    styles = getSampleStyleSheet()

    content = []

    # =====================
    # TITLE
    # =====================

    content.append(

        Paragraph(

            "AI Interview Readiness Report",

            styles["Title"]

        )

    )

    content.append(
        Spacer(1, 20)
    )

    # =====================
    # SUMMARY
    # =====================

    content.append(

        Paragraph(

            f"Overall Score: {data['overall_score']}",

            styles["Heading2"]

        )

    )

    content.append(

        Paragraph(

            f"Fluency Score: {data['average_fluency']}",

            styles["Normal"]

        )

    )

    content.append(

        Paragraph(

            f"Correctness Score: {data['average_correctness']}",

            styles["Normal"]

        )

    )

    content.append(

        Paragraph(

            f"Eye Contact Score: {data['eye_contact_score']}",

            styles["Normal"]

        )

    )

    content.append(

        Paragraph(

            f"Posture Score: {data['posture_score']}",

            styles["Normal"]

        )

    )

    content.append(

        Paragraph(

            f"Head Stability Score: {data['head_stability_score']}",

            styles["Normal"]

        )

    )

    content.append(
        Spacer(1, 20)
    )

    # =====================
    # QUESTIONS
    # =====================

    for index, q in enumerate(

        data["questions"],

        start=1

    ):

        content.append(

            Paragraph(

                f"Question {index}",

                styles["Heading2"]

            )

        )

        content.append(

            Paragraph(

                f"<b>Question:</b> {q['question']}",

                styles["Normal"]

            )

        )

        content.append(

            Paragraph(

                f"<b>Candidate Answer:</b> {q['candidate_answer']}",

                styles["Normal"]

            )

        )

        content.append(

            Paragraph(

                f"<b>Ideal Answer:</b> {q['ideal_answer']}",

                styles["Normal"]

            )

        )

        content.append(

            Paragraph(

                f"<b>Fluency:</b> {q['fluency_score']}",

                styles["Normal"]

            )

        )

        content.append(

            Paragraph(

                f"<b>Correctness:</b> {q['correctness_score']}",

                styles["Normal"]

            )

        )

        content.append(

            Paragraph(

                f"<b>Feedback:</b> {q['feedback']}",

                styles["Normal"]

            )

        )

        content.append(
            Spacer(1, 15)
        )

    pdf.build(
        content
    )

    print(
        "\nInterview_Report.pdf Generated Successfully!"
    )