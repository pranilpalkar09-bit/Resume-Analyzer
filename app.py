import streamlit as st
import pandas as pd
import plotly.express as px
from utils.pdf_parser import extract_text_from_pdf
from utils.skills import extract_skills
from utils.ats import calculate_ats_score
from utils.missing_skills import find_missing_skills
from utils.gemini import analyze_resume
from utils.cover_letter import generate_cover_letter
from utils.interview_questions import generate_interview_questions
from utils.pdf_report import create_pdf_report

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# ---------------- SESSION STATE ----------------

if "review" not in st.session_state:
    st.session_state.review = ""

if "cover_letter" not in st.session_state:
    st.session_state.cover_letter = ""

if "questions" not in st.session_state:
    st.session_state.questions = ""

# ---------------- SIDEBAR ----------------

with st.sidebar:

    st.title("🤖 AI Resume Analyzer")

    st.markdown("---")

    st.write("### Features")

    st.write("✅ Resume Upload")
    st.write("✅ Skill Detection")
    st.write("✅ ATS Score")
    st.write("✅ Missing Skills")
    st.write("✅ AI Resume Review")
    st.write("✅ AI Cover Letter")
    st.write("✅ AI Interview Questions")
    st.write("✅ PDF Report")

    st.markdown("---")

    st.info("Made by Pranil Palkar")

# ---------------- MAIN PAGE ----------------

st.title("📄 AI Resume Analyzer")

st.write("Upload your resume and get AI-powered insights.")

uploaded_file = st.file_uploader(
    "Upload your Resume (PDF)",
    type=["pdf"]
)

# ---------------- RESUME ----------------

if uploaded_file is not None:

    st.success("Resume uploaded successfully!")

    resume_text = extract_text_from_pdf(uploaded_file)

    skills = extract_skills(resume_text)

    st.subheader("🧠 Detected Skills")

    if skills:
        st.write(", ".join(skills))
    else:
        st.warning("No skills detected.")

    st.subheader("📄 Extracted Resume Text")

    st.text_area(
        "Resume Content",
        resume_text,
        height=350
    )

    # ---------------- JOB DESCRIPTION ----------------

    st.subheader("📋 Job Description")

    job_description = st.text_area(
        "Paste the Job Description here"
    )

    if job_description:

        # ---------------- ATS SCORE ----------------

        score = calculate_ats_score(
            resume_text,
            job_description
        )

        missing = find_missing_skills(
            resume_text,
            job_description
        )

        st.subheader("📊 ATS Dashboard")

        col1, col2, col3 = st.columns(3)

        col1.metric("ATS Score", f"{score}%")
        col2.metric("Detected Skills", len(skills))
        col3.metric("Missing Skills", len(missing))

        st.progress(int(score))

        st.subheader("📈 Resume Analytics")

        chart_data = {
            "Category": ["Detected Skills", "Missing Skills"],
            "Count": [len(skills), len(missing)]
        }

        fig = px.pie(
            values=chart_data["Count"],
            names=chart_data["Category"],
            title="Skills Distribution"
        )

        st.plotly_chart(fig, use_container_width=True)

        st.subheader("📊 Skills Overview")

        df = pd.DataFrame({
            "Category": ["Detected Skills", "Missing Skills"],
            "Count": [len(skills), len(missing)]
        })

        bar_fig = px.bar(
            df,
            x="Category",
            y="Count",
            title="Detected vs Missing Skills",
            text="Count"
        )

        st.plotly_chart(bar_fig, use_container_width=True)

        # ---------------- MISSING SKILLS ----------------

        st.subheader("❌ Missing Skills")

        if missing:
            for skill in missing:
                st.write(f"• {skill}")
        else:
            st.success("🎉 No missing skills found!")

        # ---------------- AI REVIEW ----------------

        st.subheader("🤖 AI Resume Review")
        if st.button("Analyze Resume with AI"):

            with st.spinner("Analyzing Resume..."):

                st.session_state.review = analyze_resume(
                    resume_text
                )

        if st.session_state.review:

            st.write(st.session_state.review)

        # ---------------- COVER LETTER ----------------

        st.subheader("📄 AI Cover Letter")

        if st.button("Generate Cover Letter"):

            with st.spinner("Generating Cover Letter..."):

                st.session_state.cover_letter = generate_cover_letter(
                    resume_text,
                    job_description
                )

        if st.session_state.cover_letter:

            st.write(st.session_state.cover_letter)

        # ---------------- INTERVIEW QUESTIONS ----------------

        st.subheader("🎤 AI Interview Questions")

        if st.button("Generate Interview Questions"):

            with st.spinner("Generating Questions..."):

                st.session_state.questions = generate_interview_questions(
                    resume_text,
                    job_description
                )

        if st.session_state.questions:

            st.write(st.session_state.questions)

        # ---------------- PDF REPORT ----------------

        st.subheader("📥 Download Report")

        if st.button("Generate PDF Report"):

            create_pdf_report(
                "Resume_Report.pdf",
                score,
                skills,
                missing,
                st.session_state.review,
                st.session_state.cover_letter,
                st.session_state.questions
            )

            st.success("✅ PDF Generated Successfully!")

        try:

            with open("Resume_Report.pdf", "rb") as pdf_file:

                st.download_button(
                    label="⬇ Download PDF",
                    data=pdf_file,
                    file_name="Resume_Report.pdf",
                    mime="application/pdf"
                )

        except FileNotFoundError:
            pass

# ---------------- FOOTER ----------------

st.markdown("---")

st.caption(
    "🚀 AI Resume Analyzer | Built with Streamlit, Python & Google Gemini"
)