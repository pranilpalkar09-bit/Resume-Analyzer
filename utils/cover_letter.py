from google import genai
import streamlit as st

client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)


def generate_cover_letter(resume_text, job_description):

    prompt = f"""
You are an expert HR recruiter.

Write a professional one-page cover letter based on the following resume and job description.

Resume:
{resume_text}

Job Description:
{job_description}

The cover letter should:

- Address the hiring manager.
- Explain why the candidate is suitable.
- Highlight relevant skills.
- Be professional and concise.
- Avoid making up experience or qualifications.
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return response.text