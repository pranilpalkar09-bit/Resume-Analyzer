import streamlit as st
from google import genai

client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)
def generate_interview_questions(resume_text, job_description):
    prompt = f"""
You are a senior technical interviewer.

Based on the following resume and job description, generate:

1. 10 Technical Interview Questions
2. 5 HR Interview Questions
3. 5 Project-based Questions
4. 5 Python Coding Questions

Resume:
{resume_text}

Job Description:
{job_description}
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt,
    )

    return response.text