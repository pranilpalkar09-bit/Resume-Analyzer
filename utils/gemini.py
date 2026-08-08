from google import genai
import streamlit as st

client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)


def analyze_resume(resume_text):

    prompt = f"""
You are an expert HR recruiter and ATS specialist.

Analyze the following resume and provide:

1. Overall Resume Score (out of 10)
2. Overall Review
3. Strengths
4. Weaknesses
5. Missing Skills
6. Suggestions for Improvement
7. ATS Optimization Tips

Resume:
{resume_text}
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return response.text