from datetime import datetime

from report_summary import generate_summary

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_report(
    role,
    readiness_score,
    resume_skills,
    matched,
    missing,
    role_questions,
    missing_questions,
):

    # ==========================================
    # AI SUMMARY
    # ==========================================

    summary = generate_summary(role, readiness_score, matched, missing)

    # ==========================================
    # READINESS STATUS
    # ==========================================

    if readiness_score >= 80:

        status = "Interview Ready"

    elif readiness_score >= 60:

        status = "Moderately Ready"

    else:

        status = "Needs Preparation"

    # ==========================================
    # CURRENT DATE
    # ==========================================

    current_date = datetime.now().strftime("%d %B %Y")

    # ==========================================
    # PDF SETUP
    # ==========================================

    doc = SimpleDocTemplate("Interview_Report.pdf")

    styles = getSampleStyleSheet()

    content = []

    # ==========================================
    # TITLE
    # ==========================================

    content.append(Paragraph("Interview Readiness Report", styles["Title"]))

    content.append(Spacer(1, 12))

    # ==========================================
    # DATE
    # ==========================================

    content.append(Paragraph(f"<b>Generated On:</b> {current_date}", styles["Normal"]))

    content.append(Spacer(1, 12))

    # ==========================================
    # ROLE
    # ==========================================

    content.append(Paragraph(f"<b>Target Role:</b> {role}", styles["Normal"]))

    content.append(
        Paragraph(f"<b>Readiness Score:</b> {readiness_score:.2f} %", styles["Normal"])
    )

    content.append(Paragraph(f"<b>Readiness Status:</b> {status}", styles["Normal"]))

    content.append(Spacer(1, 15))

    # ==========================================
    # RESUME SKILLS
    # ==========================================

    content.append(Paragraph("Resume Skills", styles["Heading2"]))

    for skill in resume_skills:

        content.append(Paragraph(f"• {skill}", styles["Normal"]))

    content.append(Spacer(1, 10))

    # ==========================================
    # MATCHED SKILLS
    # ==========================================

    content.append(Paragraph("Matched Skills", styles["Heading2"]))

    for skill in matched:

        content.append(Paragraph(f"✓ {skill}", styles["Normal"]))

    content.append(Spacer(1, 10))

    # ==========================================
    # MISSING SKILLS
    # ==========================================

    content.append(Paragraph("Missing Skills", styles["Heading2"]))

    for skill in missing:

        content.append(Paragraph(f"✗ {skill}", styles["Normal"]))

    content.append(Spacer(1, 15))

    # ==========================================
    # QUESTIONS
    # ==========================================

    content.append(Paragraph("Recommended Questions", styles["Heading2"]))

    for q in role_questions[:5]:

        content.append(Paragraph(f"• {q}", styles["Normal"]))

    for q in missing_questions[:10]:

        content.append(Paragraph(f"• {q}", styles["Normal"]))

    content.append(Spacer(1, 15))

    # ==========================================
    # AI ASSESSMENT
    # ==========================================

    content.append(Paragraph("AI Assessment", styles["Heading2"]))

    content.append(Paragraph(summary.replace("\n", "<br/>"), styles["Normal"]))

    # ==========================================
    # BUILD PDF
    # ==========================================

    doc.build(content)

    print("\nPDF Generated Successfully!")
