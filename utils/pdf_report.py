from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def create_pdf_report(
    filename,
    ats_score,
    skills,
    missing_skills,
    ai_review,
    cover_letter,
    interview_questions,
):
    styles = getSampleStyleSheet()

    doc = SimpleDocTemplate(filename)

    story = []

    story.append(Paragraph("<b>AI Resume Analyzer Report</b>", styles["Title"]))

    story.append(Paragraph(f"<b>ATS Score:</b> {ats_score}%", styles["BodyText"]))

    story.append(
        Paragraph(
            f"<b>Detected Skills:</b> {', '.join(skills)}",
            styles["BodyText"],
        )
    )

    story.append(
        Paragraph(
            f"<b>Missing Skills:</b> {', '.join(missing_skills)}",
            styles["BodyText"],
        )
    )

    story.append(Paragraph("<b>AI Resume Review</b>", styles["Heading2"]))
    story.append(Paragraph(ai_review.replace("\n", "<br/>"), styles["BodyText"]))

    story.append(Paragraph("<b>AI Cover Letter</b>", styles["Heading2"]))
    story.append(Paragraph(cover_letter.replace("\n", "<br/>"), styles["BodyText"]))

    story.append(Paragraph("<b>Interview Questions</b>", styles["Heading2"]))
    story.append(
        Paragraph(interview_questions.replace("\n", "<br/>"), styles["BodyText"])
    )

    doc.build(story)